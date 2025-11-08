"""Tests for multilingual name handling utilities.

Following TDD approach: These tests are written FIRST to define expected behavior.
"""

import pytest
from nes2.core.utils.multilingual import (
    match_names_cross_language,
    phonetic_search_nepali,
    fuzzy_match_transliterations,
    normalize_name,
    extract_name_variants,
)


class TestCrossLanguageNameMatching:
    """Test cross-language name matching functionality."""
    
    def test_match_exact_names_same_language(self):
        """Test matching identical names in the same language."""
        assert match_names_cross_language("Ram Chandra Poudel", "Ram Chandra Poudel") is True
        assert match_names_cross_language("राम चन्द्र पौडेल", "राम चन्द्र पौडेल") is True
    
    def test_match_names_different_languages(self):
        """Test matching names across Nepali and English."""
        # Should match transliterated versions
        result = match_names_cross_language("Ram Chandra Poudel", "राम चन्द्र पौडेल")
        assert result is True or result > 0.7  # High confidence match
        
        result = match_names_cross_language("Pushpa Kamal Dahal", "पुष्पकमल दाहाल")
        assert result is True or result > 0.7
    
    def test_match_names_with_spelling_variations(self):
        """Test matching names with common spelling variations."""
        # Common variations in romanization
        assert match_names_cross_language("Sher Bahadur", "Sher Bahadur") is True
        
        # Should handle minor differences
        result = match_names_cross_language("Baburam", "Babu Ram")
        assert result is True or result > 0.6
    
    def test_no_match_different_names(self):
        """Test that different names don't match."""
        result = match_names_cross_language("Ram Chandra Poudel", "Pushpa Kamal Dahal")
        assert result is False or result < 0.3
        
        result = match_names_cross_language("राम चन्द्र पौडेल", "पुष्पकमल दाहाल")
        assert result is False or result < 0.3
    
    def test_match_partial_names(self):
        """Test matching partial names (first name only, etc.)."""
        result = match_names_cross_language("Ram Poudel", "Ram Chandra Poudel")
        assert result is True or result > 0.5
        
        result = match_names_cross_language("Poudel", "Ram Chandra Poudel")
        assert result is True or result > 0.4


class TestPhoneticSearchNepali:
    """Test phonetic search for Nepali names."""
    
    def test_phonetic_search_exact_match(self):
        """Test phonetic search with exact matches."""
        candidates = [
            "राम चन्द्र पौडेल",
            "पुष्पकमल दाहाल",
            "शेरबहादुर देउवा"
        ]
        
        results = phonetic_search_nepali("राम चन्द्र पौडेल", candidates)
        assert len(results) > 0
        assert results[0]["name"] == "राम चन्द्र पौडेल"
        assert results[0]["score"] > 0.9
    
    def test_phonetic_search_similar_names(self):
        """Test phonetic search finds similar sounding names."""
        candidates = [
            "राम चन्द्र पौडेल",
            "राम चन्द्र पौडेल",  # Slight variation
            "रामचन्द्र पौडेल",    # No space
        ]
        
        results = phonetic_search_nepali("राम चन्द्र पौडेल", candidates)
        assert len(results) >= 2
        # All should have high scores
        for result in results[:2]:
            assert result["score"] > 0.7
    
    def test_phonetic_search_roman_query(self):
        """Test phonetic search with Roman query against Nepali names."""
        candidates = [
            "राम चन्द्र पौडेल",
            "पुष्पकमल दाहाल",
            "शेरबहादुर देउवा"
        ]
        
        results = phonetic_search_nepali("Ram Chandra Poudel", candidates)
        assert len(results) > 0
        # Should find the matching name
        assert any("राम" in r["name"] for r in results)
    
    def test_phonetic_search_no_matches(self):
        """Test phonetic search with no good matches."""
        candidates = [
            "राम चन्द्र पौडेल",
            "पुष्पकमल दाहाल"
        ]
        
        results = phonetic_search_nepali("John Smith", candidates)
        # Should return empty or very low scores
        assert len(results) == 0 or all(r["score"] < 0.3 for r in results)


class TestFuzzyMatchTransliterations:
    """Test fuzzy matching for transliteration variations."""
    
    def test_fuzzy_match_common_variations(self):
        """Test fuzzy matching of common transliteration variations."""
        # Common variations in Nepali name romanization
        assert fuzzy_match_transliterations("Poudel", "Paudel") > 0.8
        assert fuzzy_match_transliterations("Dahal", "Dhahal") > 0.8
        assert fuzzy_match_transliterations("Oli", "Olii") > 0.8
    
    def test_fuzzy_match_spacing_differences(self):
        """Test fuzzy matching with spacing differences."""
        assert fuzzy_match_transliterations("Ram Chandra", "Ramchandra") > 0.8
        assert fuzzy_match_transliterations("Babu Ram", "Baburam") > 0.8
    
    def test_fuzzy_match_case_insensitive(self):
        """Test that fuzzy matching is case-insensitive."""
        assert fuzzy_match_transliterations("POUDEL", "poudel") > 0.95
        assert fuzzy_match_transliterations("Ram Chandra", "ram chandra") > 0.95
    
    def test_fuzzy_match_different_names(self):
        """Test that different names have low similarity."""
        assert fuzzy_match_transliterations("Poudel", "Dahal") < 0.5
        assert fuzzy_match_transliterations("Ram", "Shyam") < 0.6
    
    def test_fuzzy_match_partial_overlap(self):
        """Test fuzzy matching with partial name overlap."""
        score = fuzzy_match_transliterations("Ram Chandra Poudel", "Ram Poudel")
        assert 0.5 < score < 0.9  # Partial match


class TestNameNormalization:
    """Test name normalization for Nepali and English variants."""
    
    def test_normalize_english_name(self):
        """Test normalization of English names."""
        assert normalize_name("Ram Chandra Poudel") == "ram chandra poudel"
        assert normalize_name("  PUSHPA  KAMAL  ") == "pushpa kamal"
    
    def test_normalize_nepali_name(self):
        """Test normalization of Nepali names."""
        result = normalize_name("राम चन्द्र पौडेल")
        assert "राम" in result
        assert "  " not in result  # No double spaces
    
    def test_normalize_removes_extra_whitespace(self):
        """Test that normalization removes extra whitespace."""
        assert normalize_name("Ram  Chandra   Poudel") == "ram chandra poudel"
        assert normalize_name("\n\tRam Poudel\n") == "ram poudel"
    
    def test_normalize_handles_special_characters(self):
        """Test normalization with special characters."""
        # Should preserve Nepali characters but normalize spacing
        result = normalize_name("राम चन्द्र पौडेल।")
        assert "राम" in result
    
    def test_normalize_empty_string(self):
        """Test normalization of empty string."""
        assert normalize_name("") == ""
        assert normalize_name("   ") == ""
    
    def test_normalize_mixed_script(self):
        """Test normalization of mixed Devanagari and Roman."""
        result = normalize_name("Ram राम Poudel पौडेल")
        assert "ram" in result.lower()
        assert "राम" in result


class TestNameVariantExtraction:
    """Test extraction of name variants from multilingual names."""
    
    def test_extract_variants_from_full_name(self):
        """Test extracting variants from a full name."""
        variants = extract_name_variants("Ram Chandra Poudel")
        
        assert "Ram Chandra Poudel" in variants
        assert "Ram Poudel" in variants  # First + Last
        assert "Poudel" in variants  # Last name only
        assert len(variants) >= 3
    
    def test_extract_variants_from_nepali_name(self):
        """Test extracting variants from Nepali name."""
        variants = extract_name_variants("राम चन्द्र पौडेल")
        
        assert "राम चन्द्र पौडेल" in variants
        # Should include parts
        assert any("राम" in v for v in variants)
        assert any("पौडेल" in v for v in variants)
    
    def test_extract_variants_single_name(self):
        """Test extracting variants from single name."""
        variants = extract_name_variants("Poudel")
        
        assert "Poudel" in variants
        assert len(variants) >= 1
    
    def test_extract_variants_with_aliases(self):
        """Test extracting variants including common aliases."""
        # For names with common short forms
        variants = extract_name_variants("Baburam Bhattarai")
        
        assert "Baburam Bhattarai" in variants
        assert "Baburam" in variants
        assert "Bhattarai" in variants
    
    def test_extract_variants_preserves_order(self):
        """Test that variants are ordered by relevance."""
        variants = extract_name_variants("Ram Chandra Poudel")
        
        # Full name should be first
        assert variants[0] == "Ram Chandra Poudel"


class TestMultilingualEdgeCases:
    """Test edge cases in multilingual name handling."""
    
    def test_handle_empty_names(self):
        """Test handling of empty names."""
        assert match_names_cross_language("", "") is False
        assert normalize_name("") == ""
        assert extract_name_variants("") == []
    
    def test_handle_single_character_names(self):
        """Test handling of single character names."""
        variants = extract_name_variants("K")
        assert "K" in variants
    
    def test_handle_names_with_titles(self):
        """Test handling of names with titles."""
        result = normalize_name("Dr. Ram Chandra Poudel")
        assert "ram chandra poudel" in result.lower()
        
        result = normalize_name("श्री राम चन्द्र पौडेल")
        assert "राम" in result
    
    def test_handle_names_with_numbers(self):
        """Test handling of names with numbers."""
        result = normalize_name("Ram Poudel 2")
        assert "ram poudel" in result.lower()
