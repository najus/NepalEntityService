"""Utility functions for nes2."""

from nes2.core.utils.devanagari import (
    is_devanagari,
    contains_devanagari,
    romanize_nepali,
    transliterate_to_devanagari,
    transliterate_to_roman,
    normalize_devanagari,
    compare_devanagari,
)

from nes2.core.utils.multilingual import (
    match_names_cross_language,
    phonetic_search_nepali,
    fuzzy_match_transliterations,
    normalize_name,
    extract_name_variants,
)

__all__ = [
    # Devanagari utilities
    "is_devanagari",
    "contains_devanagari",
    "romanize_nepali",
    "transliterate_to_devanagari",
    "transliterate_to_roman",
    "normalize_devanagari",
    "compare_devanagari",
    # Multilingual utilities
    "match_names_cross_language",
    "phonetic_search_nepali",
    "fuzzy_match_transliterations",
    "normalize_name",
    "extract_name_variants",
]
