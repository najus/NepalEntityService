"""Multilingual name handling utilities for Nepali and English names.

This module provides utilities for:
- Cross-language name matching
- Phonetic search for Nepali names
- Fuzzy matching for transliteration variations
- Name normalization
- Name variant extraction
"""

import re
from difflib import SequenceMatcher
from typing import Dict, List, Union

from nes.core.utils.devanagari import (
    compare_devanagari,
    contains_devanagari,
    normalize_devanagari,
    transliterate_to_devanagari,
    transliterate_to_roman,
)


def match_names_cross_language(name1: str, name2: str) -> Union[bool, float]:
    """Match names across Nepali and English with confidence scoring.

    This function handles:
    - Same language exact matches
    - Cross-language transliteration matching
    - Spelling variations
    - Partial name matching

    Args:
        name1: First name (Nepali or English)
        name2: Second name (Nepali or English)

    Returns:
        True for exact match, False for no match, or float confidence score (0-1)
    """
    if not name1 or not name2:
        return False

    # Normalize both names
    norm1 = normalize_name(name1)
    norm2 = normalize_name(name2)

    # Check for exact match after normalization
    if norm1 == norm2:
        return True

    # If both are same script, use fuzzy matching
    has_dev1 = contains_devanagari(name1)
    has_dev2 = contains_devanagari(name2)

    if has_dev1 == has_dev2:
        # Same script - use fuzzy matching
        score = fuzzy_match_transliterations(norm1, norm2)
        if score > 0.9:
            return True
        elif score > 0.6:
            return score
        else:
            return False

    # Different scripts - transliterate and compare
    if has_dev1:
        # name1 is Devanagari, transliterate to Roman
        name1_roman = transliterate_to_roman(name1)
        score = fuzzy_match_transliterations(normalize_name(name1_roman), norm2)
    else:
        # name2 is Devanagari, transliterate to Roman
        name2_roman = transliterate_to_roman(name2)
        score = fuzzy_match_transliterations(norm1, normalize_name(name2_roman))

    if score > 0.85:
        return True
    elif score > 0.6:
        return score
    else:
        return False


def phonetic_search_nepali(
    query: str, candidates: List[str], top_k: int = 5
) -> List[Dict[str, Union[str, float]]]:
    """Perform phonetic search for Nepali names.

    This function finds names that sound similar to the query,
    handling both Nepali and English text.

    Args:
        query: Search query (Nepali or English)
        candidates: List of candidate names to search
        top_k: Number of top results to return

    Returns:
        List of dicts with 'name' and 'score' keys, sorted by score
    """
    if not query or not candidates:
        return []

    # Normalize query
    norm_query = normalize_name(query)
    query_has_dev = contains_devanagari(query)

    # Score each candidate
    results = []
    for candidate in candidates:
        if not candidate:
            continue

        # Calculate similarity score
        score = _calculate_phonetic_score(norm_query, candidate, query_has_dev)

        if score > 0.3:  # Minimum threshold
            results.append({"name": candidate, "score": score})

    # Sort by score descending
    results.sort(key=lambda x: x["score"], reverse=True)

    return results[:top_k]


def _calculate_phonetic_score(query: str, candidate: str, query_has_dev: bool) -> float:
    """Calculate phonetic similarity score between query and candidate.

    Args:
        query: Normalized query string
        candidate: Candidate name
        query_has_dev: Whether query contains Devanagari

    Returns:
        Similarity score between 0 and 1
    """
    norm_candidate = normalize_name(candidate)
    candidate_has_dev = contains_devanagari(candidate)

    # If same script, direct comparison
    if query_has_dev == candidate_has_dev:
        return fuzzy_match_transliterations(query, norm_candidate)

    # Different scripts - transliterate
    if query_has_dev:
        query_roman = transliterate_to_roman(query)
        return fuzzy_match_transliterations(normalize_name(query_roman), norm_candidate)
    else:
        candidate_roman = transliterate_to_roman(candidate)
        return fuzzy_match_transliterations(query, normalize_name(candidate_roman))


def fuzzy_match_transliterations(text1: str, text2: str) -> float:
    """Fuzzy match two texts accounting for transliteration variations.

    This function handles:
    - Case differences
    - Spacing differences
    - Common transliteration variations
    - Character substitutions

    Args:
        text1: First text
        text2: Second text

    Returns:
        Similarity score between 0 and 1
    """
    if not text1 or not text2:
        return 0.0

    # Normalize for comparison
    norm1 = _normalize_for_fuzzy_match(text1)
    norm2 = _normalize_for_fuzzy_match(text2)

    # Use SequenceMatcher for similarity
    matcher = SequenceMatcher(None, norm1, norm2)
    base_score = matcher.ratio()

    # Boost score for common transliteration patterns
    boost = 0.0

    # Check for common substitutions
    substitutions = [
        ("ou", "au"),  # Poudel/Paudel
        ("dh", "d"),  # Dahal/Dhahal
        ("ii", "i"),  # Oli/Olii
        ("aa", "a"),  # Common vowel variations
    ]

    for sub1, sub2 in substitutions:
        if (sub1 in norm1 and sub2 in norm2) or (sub2 in norm1 and sub1 in norm2):
            boost += 0.05

    # Boost for partial matches (one is substring of other)
    if norm1 in norm2 or norm2 in norm1:
        boost += 0.1

    final_score = min(1.0, base_score + boost)
    return final_score


def _normalize_for_fuzzy_match(text: str) -> str:
    """Normalize text for fuzzy matching.

    Args:
        text: Text to normalize

    Returns:
        Normalized text
    """
    # Convert to lowercase
    text = text.lower()

    # Remove extra whitespace
    text = re.sub(r"\s+", "", text)

    # Remove punctuation
    text = re.sub(r"[^\w\u0900-\u097F]", "", text)

    return text


def normalize_name(name: str) -> str:
    """Normalize a name for consistent comparison.

    Normalization includes:
    - Lowercasing (for Roman text)
    - Whitespace normalization
    - Devanagari normalization
    - Trimming

    Args:
        name: Name to normalize

    Returns:
        Normalized name
    """
    if not name:
        return ""

    # If contains Devanagari, use Devanagari normalization
    if contains_devanagari(name):
        return normalize_devanagari(name)

    # Roman text normalization
    # Convert to lowercase
    normalized = name.lower()

    # Remove extra whitespace
    normalized = re.sub(r"\s+", " ", normalized)

    # Trim
    normalized = normalized.strip()

    # Remove common titles
    titles = ["dr.", "mr.", "mrs.", "ms.", "prof."]
    for title in titles:
        if normalized.startswith(title + " "):
            normalized = normalized[len(title) + 1 :]

    return normalized


def extract_name_variants(name: str) -> List[str]:
    """Extract common variants of a name for search and matching.

    Variants include:
    - Full name
    - First + Last name
    - Last name only
    - First name only
    - Common abbreviations

    Args:
        name: Full name

    Returns:
        List of name variants, ordered by relevance
    """
    if not name or not name.strip():
        return []

    variants = []

    # Add full name first
    variants.append(name.strip())

    # Split into parts
    parts = name.strip().split()

    if len(parts) == 0:
        return variants

    if len(parts) == 1:
        # Single name - just return it
        return variants

    # Multiple parts
    if len(parts) >= 2:
        # First + Last
        first_last = f"{parts[0]} {parts[-1]}"
        if first_last not in variants:
            variants.append(first_last)

        # Last name only
        if parts[-1] not in variants:
            variants.append(parts[-1])

        # First name only
        if parts[0] not in variants:
            variants.append(parts[0])

    if len(parts) >= 3:
        # Middle name combinations
        # First + Middle
        first_middle = f"{parts[0]} {parts[1]}"
        if first_middle not in variants:
            variants.append(first_middle)

    return variants
