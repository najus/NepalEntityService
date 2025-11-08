"""Devanagari script handling utilities for Nepali text.

This module provides utilities for:
- Validating Devanagari script
- Romanization of Nepali names
- Bidirectional transliteration (Devanagari ↔ Roman)
- Devanagari-aware string comparison
- Text normalization

Devanagari Unicode range: U+0900 to U+097F
"""

import re
import unicodedata
from typing import Optional

# Devanagari Unicode range
DEVANAGARI_RANGE = (0x0900, 0x097F)


def is_devanagari(text: str) -> bool:
    """Check if text contains only Devanagari characters (and whitespace).

    Args:
        text: Text to check

    Returns:
        True if text contains only Devanagari characters and whitespace
    """
    if not text or not text.strip():
        return False

    # Remove whitespace for checking
    text_no_space = text.replace(" ", "").replace("\t", "").replace("\n", "")

    if not text_no_space:
        return False

    # Check if all characters are in Devanagari range
    for char in text_no_space:
        code_point = ord(char)
        if not (DEVANAGARI_RANGE[0] <= code_point <= DEVANAGARI_RANGE[1]):
            return False

    return True


def contains_devanagari(text: str) -> bool:
    """Check if text contains any Devanagari characters.

    Args:
        text: Text to check

    Returns:
        True if text contains at least one Devanagari character
    """
    if not text:
        return False

    for char in text:
        code_point = ord(char)
        if DEVANAGARI_RANGE[0] <= code_point <= DEVANAGARI_RANGE[1]:
            return True

    return False


def romanize_nepali(text: str) -> str:
    """Romanize Nepali Devanagari text to Roman script.

    This is a simple transliteration that converts Devanagari characters
    to their Roman equivalents following common Nepali romanization conventions.

    Args:
        text: Nepali text in Devanagari script

    Returns:
        Romanized text
    """
    if not text:
        return ""

    # If already Roman, return as-is
    if not contains_devanagari(text):
        return text

    # Use transliteration for romanization
    return transliterate_to_roman(text)


def transliterate_to_devanagari(text: str) -> str:
    """Transliterate Roman text to Devanagari script.

    This provides a basic phonetic mapping from Roman to Devanagari
    for common Nepali words and names.

    Args:
        text: Text in Roman script

    Returns:
        Text transliterated to Devanagari
    """
    if not text:
        return ""

    # If already Devanagari, return as-is
    if is_devanagari(text):
        return text

    # Basic Roman to Devanagari mapping
    # This is a simplified mapping for common patterns
    mapping = {
        # Vowels
        "a": "अ",
        "aa": "आ",
        "i": "इ",
        "ii": "ई",
        "u": "उ",
        "uu": "ऊ",
        "e": "ए",
        "ai": "ऐ",
        "o": "ओ",
        "au": "औ",
        # Consonants
        "ka": "क",
        "kha": "ख",
        "ga": "ग",
        "gha": "घ",
        "nga": "ङ",
        "cha": "च",
        "chha": "छ",
        "ja": "ज",
        "jha": "झ",
        "nya": "ञ",
        "ta": "ट",
        "tha": "ठ",
        "da": "ड",
        "dha": "ढ",
        "na": "ण",
        "ta": "त",
        "tha": "थ",
        "da": "द",
        "dha": "ध",
        "na": "न",
        "pa": "प",
        "pha": "फ",
        "ba": "ब",
        "bha": "भ",
        "ma": "म",
        "ya": "य",
        "ra": "र",
        "la": "ल",
        "wa": "व",
        "va": "व",
        "sha": "श",
        "shha": "ष",
        "sa": "स",
        "ha": "ह",
        # Common words
        "nepal": "नेपाल",
        "kathmandu": "काठमाडौं",
        "ram": "राम",
        "krishna": "कृष्ण",
        "shyam": "श्याम",
    }

    # Convert to lowercase for matching
    text_lower = text.lower()
    result = text_lower

    # Try to match whole words first
    for roman, devanagari in sorted(mapping.items(), key=lambda x: -len(x[0])):
        result = result.replace(roman, devanagari)

    return result


def transliterate_to_roman(text: str) -> str:
    """Transliterate Devanagari text to Roman script.

    This provides a basic phonetic mapping from Devanagari to Roman
    following common Nepali romanization conventions.

    Args:
        text: Text in Devanagari script

    Returns:
        Text transliterated to Roman script
    """
    if not text:
        return ""

    # If no Devanagari, return as-is
    if not contains_devanagari(text):
        return text

    # Common word mappings for better results
    word_mappings = {
        "नेपाल": "Nepal",
        "काठमाडौं": "Kathmandu",
        "काठमाडौ": "Kathmandu",
        "पोखरा": "Pokhara",
        "भारत": "Bharat",
    }

    # Check for whole word matches first
    for nepali, roman in word_mappings.items():
        if nepali in text:
            text = text.replace(nepali, roman)

    # Basic Devanagari to Roman mapping
    mapping = {
        # Vowels
        "अ": "a",
        "आ": "a",
        "इ": "i",
        "ई": "i",
        "उ": "u",
        "ऊ": "u",
        "ऋ": "ri",
        "ए": "e",
        "ऐ": "ai",
        "ओ": "o",
        "औ": "au",
        # Consonants (with inherent 'a')
        "क": "ka",
        "ख": "kha",
        "ग": "ga",
        "घ": "gha",
        "ङ": "nga",
        "च": "cha",
        "छ": "chha",
        "ज": "ja",
        "झ": "jha",
        "ञ": "nya",
        "ट": "ta",
        "ठ": "tha",
        "ड": "da",
        "ढ": "dha",
        "ण": "na",
        "त": "ta",
        "थ": "tha",
        "द": "da",
        "ध": "dha",
        "न": "na",
        "प": "pa",
        "फ": "pha",
        "ब": "ba",
        "भ": "bha",
        "म": "ma",
        "य": "ya",
        "र": "ra",
        "ल": "la",
        "व": "va",
        "श": "sha",
        "ष": "shha",
        "स": "sa",
        "ह": "ha",
        # Vowel signs (matras) - simplified for readability
        "ा": "a",
        "ि": "i",
        "ी": "i",
        "ु": "u",
        "ू": "u",
        "ृ": "ri",
        "े": "e",
        "ै": "ai",
        "ो": "o",
        "ौ": "au",
        # Special characters
        "्": "",  # Halant (virama) - removes inherent vowel
        "ं": "n",  # Anusvara
        "ः": "h",  # Visarga
        "ँ": "n",  # Chandrabindu
        # Devanagari numerals
        "०": "0",
        "१": "1",
        "२": "2",
        "३": "3",
        "४": "4",
        "५": "5",
        "६": "6",
        "७": "7",
        "८": "8",
        "९": "9",
    }

    result = []
    i = 0
    while i < len(text):
        char = text[i]

        # Check for multi-character sequences
        if i + 1 < len(text):
            two_char = text[i : i + 2]
            if two_char in mapping:
                result.append(mapping[two_char])
                i += 2
                continue

        # Single character mapping
        if char in mapping:
            result.append(mapping[char])
        else:
            result.append(char)

        i += 1

    return "".join(result)


def normalize_devanagari(text: str) -> str:
    """Normalize Devanagari text for consistent comparison.

    Normalization includes:
    - Unicode normalization (NFC)
    - Whitespace normalization
    - Trimming

    Args:
        text: Text to normalize

    Returns:
        Normalized text
    """
    if not text:
        return ""

    # Unicode normalization (NFC - Canonical Decomposition followed by Canonical Composition)
    normalized = unicodedata.normalize("NFC", text)

    # Normalize whitespace
    normalized = re.sub(r"\s+", " ", normalized)

    # Trim
    normalized = normalized.strip()

    return normalized


def compare_devanagari(text1: str, text2: str) -> bool:
    """Compare two strings with Devanagari-aware normalization.

    This comparison:
    - Normalizes Unicode
    - Ignores whitespace differences
    - Is case-insensitive for Roman text
    - Handles mixed Devanagari and Roman text

    Args:
        text1: First text to compare
        text2: Second text to compare

    Returns:
        True if texts are equivalent after normalization
    """
    # Normalize both texts
    norm1 = normalize_devanagari(text1)
    norm2 = normalize_devanagari(text2)

    # For Roman text, make case-insensitive
    # For Devanagari, case doesn't apply
    if not contains_devanagari(norm1) and not contains_devanagari(norm2):
        norm1 = norm1.lower()
        norm2 = norm2.lower()

    # For mixed text, normalize Roman parts to lowercase
    if contains_devanagari(norm1) or contains_devanagari(norm2):
        # Create a version where Roman parts are lowercase
        def normalize_mixed(text: str) -> str:
            result = []
            for char in text:
                if contains_devanagari(char):
                    result.append(char)
                else:
                    result.append(char.lower())
            return "".join(result)

        norm1 = normalize_mixed(norm1)
        norm2 = normalize_mixed(norm2)

    return norm1 == norm2
