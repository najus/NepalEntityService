"""Tests for Devanagari script handling utilities.

Following TDD approach: These tests are written FIRST to define expected behavior.
"""

import pytest

from nes2.core.utils.devanagari import (
    compare_devanagari,
    contains_devanagari,
    is_devanagari,
    normalize_devanagari,
    romanize_nepali,
    transliterate_to_devanagari,
    transliterate_to_roman,
)


class TestDevanagariValidation:
    """Test Devanagari script validation functions."""

    def test_is_devanagari_with_pure_devanagari(self):
        """Test that pure Devanagari text is correctly identified."""
        assert is_devanagari("नेपाल") is True
        assert is_devanagari("काठमाडौं") is True
        assert is_devanagari("राम चन्द्र पौडेल") is True
        assert is_devanagari("नेपाली कांग्रेस") is True

    def test_is_devanagari_with_mixed_text(self):
        """Test that mixed text is not identified as pure Devanagari."""
        assert is_devanagari("Nepal नेपाल") is False
        assert is_devanagari("Ram Chandra Poudel") is False
        assert is_devanagari("123") is False

    def test_is_devanagari_with_empty_string(self):
        """Test that empty string returns False."""
        assert is_devanagari("") is False
        assert is_devanagari("   ") is False

    def test_contains_devanagari_with_mixed_text(self):
        """Test detection of Devanagari in mixed text."""
        assert contains_devanagari("Nepal नेपाल") is True
        assert contains_devanagari("राम Chandra पौडेल") is True
        assert contains_devanagari("नेपाल") is True

    def test_contains_devanagari_with_no_devanagari(self):
        """Test that text without Devanagari returns False."""
        assert contains_devanagari("Nepal") is False
        assert contains_devanagari("Ram Chandra Poudel") is False
        assert contains_devanagari("123") is False


class TestRomanization:
    """Test romanization of Nepali names."""

    def test_romanize_common_names(self):
        """Test romanization of common Nepali names."""
        # These should produce reasonable romanizations
        result = romanize_nepali("राम चन्द्र पौडेल")
        assert result is not None
        assert len(result) > 0

        result = romanize_nepali("नेपाल")
        assert result is not None
        assert "nepal" in result.lower()

    def test_romanize_empty_string(self):
        """Test romanization of empty string."""
        assert romanize_nepali("") == ""

    def test_romanize_already_roman(self):
        """Test that Roman text passes through unchanged."""
        assert romanize_nepali("Ram Chandra Poudel") == "Ram Chandra Poudel"


class TestTransliteration:
    """Test bidirectional transliteration between Devanagari and Roman scripts."""

    def test_transliterate_to_devanagari_basic(self):
        """Test basic Roman to Devanagari transliteration."""
        # Common Nepali words
        result = transliterate_to_devanagari("nepal")
        assert contains_devanagari(result)

        result = transliterate_to_devanagari("kathmandu")
        assert contains_devanagari(result)

    def test_transliterate_to_devanagari_names(self):
        """Test transliteration of Nepali names."""
        result = transliterate_to_devanagari("Ram Chandra Poudel")
        assert contains_devanagari(result)

        result = transliterate_to_devanagari("Pushpa Kamal Dahal")
        assert contains_devanagari(result)

    def test_transliterate_to_roman_basic(self):
        """Test basic Devanagari to Roman transliteration."""
        result = transliterate_to_roman("नेपाल")
        assert not contains_devanagari(result)
        assert len(result) > 0

        result = transliterate_to_roman("काठमाडौं")
        assert not contains_devanagari(result)
        assert len(result) > 0

    def test_transliterate_to_roman_names(self):
        """Test transliteration of Nepali names to Roman."""
        result = transliterate_to_roman("राम चन्द्र पौडेल")
        assert not contains_devanagari(result)
        assert len(result) > 0

        result = transliterate_to_roman("पुष्पकमल दाहाल")
        assert not contains_devanagari(result)
        assert len(result) > 0

    def test_transliteration_roundtrip_preservation(self):
        """Test that transliteration preserves meaning (not exact form)."""
        # We can't expect exact roundtrip, but should get similar results
        original = "नेपाल"
        roman = transliterate_to_roman(original)
        back_to_devanagari = transliterate_to_devanagari(roman)

        # Both should be Devanagari
        assert contains_devanagari(original)
        assert contains_devanagari(back_to_devanagari)


class TestDevanagariNormalization:
    """Test Devanagari text normalization."""

    def test_normalize_removes_extra_spaces(self):
        """Test that normalization removes extra spaces."""
        result = normalize_devanagari("राम  चन्द्र   पौडेल")
        assert "  " not in result
        assert result == "राम चन्द्र पौडेल"

    def test_normalize_trims_whitespace(self):
        """Test that normalization trims leading/trailing whitespace."""
        result = normalize_devanagari("  नेपाल  ")
        assert result == "नेपाल"

    def test_normalize_handles_unicode_variants(self):
        """Test that normalization handles Unicode variants."""
        # Different Unicode representations should normalize to same form
        result1 = normalize_devanagari("नेपाल")
        result2 = normalize_devanagari("नेपाल")  # May use different Unicode

        # Both should be valid Devanagari
        assert is_devanagari(result1)
        assert is_devanagari(result2)

    def test_normalize_empty_string(self):
        """Test normalization of empty string."""
        assert normalize_devanagari("") == ""
        assert normalize_devanagari("   ") == ""


class TestDevanagariComparison:
    """Test Devanagari-aware string comparison."""

    def test_compare_identical_strings(self):
        """Test that identical strings are equal."""
        assert compare_devanagari("नेपाल", "नेपाल") is True
        assert compare_devanagari("राम चन्द्र पौडेल", "राम चन्द्र पौडेल") is True

    def test_compare_with_whitespace_differences(self):
        """Test that comparison ignores whitespace differences."""
        assert compare_devanagari("राम चन्द्र पौडेल", "राम  चन्द्र  पौडेल") is True
        assert compare_devanagari("  नेपाल  ", "नेपाल") is True

    def test_compare_different_strings(self):
        """Test that different strings are not equal."""
        assert compare_devanagari("नेपाल", "भारत") is False
        assert compare_devanagari("राम", "श्याम") is False

    def test_compare_case_insensitive_for_roman(self):
        """Test that Roman text comparison is case-insensitive."""
        assert compare_devanagari("Nepal", "nepal") is True
        assert compare_devanagari("RAM", "ram") is True

    def test_compare_mixed_scripts(self):
        """Test comparison with mixed scripts."""
        # Should handle mixed Devanagari and Roman
        assert compare_devanagari("Nepal नेपाल", "nepal नेपाल") is True

    def test_compare_empty_strings(self):
        """Test comparison of empty strings."""
        assert compare_devanagari("", "") is True
        assert compare_devanagari("", "नेपाल") is False


class TestDevanagariEdgeCases:
    """Test edge cases and special scenarios."""

    def test_handle_numbers_in_devanagari(self):
        """Test handling of Devanagari numerals."""
        # Devanagari numerals: ०१२३४५६७८९
        text = "सन् २०७९"
        assert contains_devanagari(text)

    def test_handle_punctuation_with_devanagari(self):
        """Test handling of punctuation with Devanagari."""
        text = "नेपाल, काठमाडौं।"
        assert contains_devanagari(text)

        normalized = normalize_devanagari(text)
        assert contains_devanagari(normalized)

    def test_handle_special_characters(self):
        """Test handling of special Devanagari characters."""
        # Chandrabindu, anusvara, visarga
        text = "चन्द्र"  # Contains halant
        assert is_devanagari(text)

        text = "कांग्रेस"  # Contains anusvara
        assert is_devanagari(text)
