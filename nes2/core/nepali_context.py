"""Nepali cultural and political context for the entity service.

This module provides comprehensive documentation and reference data
about Nepal's political system, administrative structure, and cultural context
to guide proper entity classification and relationship modeling.
"""

from typing import Dict, List

# Nepal's Political System
POLITICAL_SYSTEM_OVERVIEW = """
Nepal's Political System (Federal Democratic Republic since 2008):

Government Structure:
  - Federal Democratic Republic established in 2008
  - Three-tier federal structure: Federal, Provincial, Local
  - Parliamentary system with multi-party democracy
  - President as Head of State (ceremonial role)
  - Prime Minister as Head of Government (executive power)

Legislature:
  - Bicameral Federal Parliament:
    * House of Representatives (प्रतिनिधि सभा): 275 members
      - 165 elected through FPTP (First-Past-The-Post)
      - 110 elected through PR (Proportional Representation)
    * National Assembly (राष्ट्रिय सभा): 59 members
      - Elected by provincial assemblies and local governments

Executive:
  - President (राष्ट्रपति): Elected by electoral college
  - Vice President (उपराष्ट्रपति): Elected by electoral college
  - Prime Minister (प्रधानमन्त्री): Leader of majority party/coalition
  - Council of Ministers (मन्त्रिपरिषद्): Cabinet appointed by PM

Judiciary:
  - Supreme Court (सर्वोच्च अदालत): Highest judicial authority
  - High Courts: 7 high courts (one per province)
  - District Courts: Courts in each of 77 districts

Constitutional Bodies:
  - Election Commission (निर्वाचन आयोग)
  - Commission for Investigation of Abuse of Authority (CIAA)
  - National Human Rights Commission
  - Public Service Commission
"""


# Administrative Divisions
ADMINISTRATIVE_DIVISIONS = {
    "provinces": {
        "count": 7,
        "nepali": "प्रदेश",
        "description": "Highest administrative division since 2015 constitution",
        "list": [
            {
                "number": 1,
                "name": "Koshi Province",
                "nepali": "कोशी प्रदेश",
                "capital": "Biratnagar",
            },
            {
                "number": 2,
                "name": "Madhesh Province",
                "nepali": "मधेश प्रदेश",
                "capital": "Janakpur",
            },
            {
                "number": 3,
                "name": "Bagmati Province",
                "nepali": "बागमती प्रदेश",
                "capital": "Hetauda",
            },
            {
                "number": 4,
                "name": "Gandaki Province",
                "nepali": "गण्डकी प्रदेश",
                "capital": "Pokhara",
            },
            {
                "number": 5,
                "name": "Lumbini Province",
                "nepali": "लुम्बिनी प्रदेश",
                "capital": "Deukhuri",
            },
            {
                "number": 6,
                "name": "Karnali Province",
                "nepali": "कर्णाली प्रदेश",
                "capital": "Birendranagar",
            },
            {
                "number": 7,
                "name": "Sudurpashchim Province",
                "nepali": "सुदूरपश्चिम प्रदेश",
                "capital": "Godawari",
            },
        ],
    },
    "districts": {
        "count": 77,
        "nepali": "जिल्ला",
        "description": "Second-level administrative division, historical units maintained",
    },
    "local_bodies": {
        "total": 753,
        "types": {
            "metropolitan_city": {
                "count": 6,
                "nepali": "महानगरपालिका",
                "criteria": "Population > 300,000",
                "list": [
                    "Kathmandu",
                    "Pokhara",
                    "Lalitpur",
                    "Bharatpur",
                    "Biratnagar",
                    "Birgunj",
                ],
            },
            "sub_metropolitan_city": {
                "count": 11,
                "nepali": "उपमहानगरपालिका",
                "criteria": "Population 100,000-300,000",
            },
            "municipality": {
                "count": 276,
                "nepali": "नगरपालिका",
                "criteria": "Urban areas",
            },
            "rural_municipality": {
                "count": 460,
                "nepali": "गाउँपालिका",
                "criteria": "Rural areas",
            },
        },
    },
    "wards": {
        "total": 6743,
        "nepali": "वडा",
        "description": "Smallest administrative unit within local bodies",
    },
}


# Political Parties
MAJOR_POLITICAL_PARTIES = [
    {
        "name": "Nepali Congress",
        "nepali": "नेपाली कांग्रेस",
        "abbreviation": "NC",
        "founded": 1947,
        "ideology": ["Social Democracy", "Democratic Socialism"],
        "symbol": "Tree",
        "color": "Green",
        "description": "Oldest democratic party, center-left ideology",
    },
    {
        "name": "Communist Party of Nepal (Unified Marxist-Leninist)",
        "nepali": "नेपाल कम्युनिष्ट पार्टी (एकीकृत मार्क्सवादी-लेनिनवादी)",
        "abbreviation": "CPN-UML",
        "founded": 1991,
        "ideology": ["Communism", "Marxism-Leninism"],
        "symbol": "Sun",
        "color": "Red",
        "description": "Major communist party, center-left to left ideology",
    },
    {
        "name": "Communist Party of Nepal (Maoist Centre)",
        "nepali": "नेपाल कम्युनिष्ट पार्टी (माओवादी केन्द्र)",
        "abbreviation": "CPN-MC",
        "founded": 2009,
        "ideology": ["Maoism", "Communism"],
        "symbol": "Hammer and Sickle",
        "color": "Red",
        "description": "Former rebel group, now mainstream political party",
    },
    {
        "name": "Rastriya Swatantra Party",
        "nepali": "राष्ट्रिय स्वतन्त्र पार्टी",
        "abbreviation": "RSP",
        "founded": 2022,
        "ideology": ["Good Governance", "Anti-Corruption"],
        "symbol": "Bell",
        "color": "Blue",
        "description": "New party focused on governance reform",
    },
    {
        "name": "Rastriya Prajatantra Party",
        "nepali": "राष्ट्रिय प्रजातन्त्र पार्टी",
        "abbreviation": "RPP",
        "founded": 1990,
        "ideology": ["Constitutional Monarchy", "Hindu State"],
        "symbol": "Plow",
        "color": "Yellow",
        "description": "Pro-monarchy, Hindu nationalist party",
    },
]


# Government Ministries
GOVERNMENT_MINISTRIES = [
    {"name": "Office of the President", "nepali": "राष्ट्रपति कार्यालय"},
    {
        "name": "Office of the Prime Minister and Council of Ministers",
        "nepali": "प्रधानमन्त्री तथा मन्त्रिपरिषद्को कार्यालय",
    },
    {"name": "Ministry of Home Affairs", "nepali": "गृह मन्त्रालय"},
    {"name": "Ministry of Foreign Affairs", "nepali": "परराष्ट्र मन्त्रालय"},
    {"name": "Ministry of Finance", "nepali": "अर्थ मन्त्रालय"},
    {"name": "Ministry of Defense", "nepali": "रक्षा मन्त्रालय"},
    {
        "name": "Ministry of Education, Science and Technology",
        "nepali": "शिक्षा, विज्ञान तथा प्रविधि मन्त्रालय",
    },
    {
        "name": "Ministry of Health and Population",
        "nepali": "स्वास्थ्य तथा जनसंख्या मन्त्रालय",
    },
    {
        "name": "Ministry of Law, Justice and Parliamentary Affairs",
        "nepali": "कानून, न्याय तथा संसदीय मामिला मन्त्रालय",
    },
    {
        "name": "Ministry of Federal Affairs and General Administration",
        "nepali": "संघीय मामिला तथा सामान्य प्रशासन मन्त्रालय",
    },
]


# Constitutional Bodies
CONSTITUTIONAL_BODIES = [
    {
        "name": "Election Commission",
        "nepali": "निर्वाचन आयोग",
        "role": "Conduct elections",
    },
    {
        "name": "Commission for Investigation of Abuse of Authority",
        "nepali": "अख्तियार दुरुपयोग अनुसन्धान आयोग",
        "role": "Anti-corruption",
    },
    {
        "name": "National Human Rights Commission",
        "nepali": "राष्ट्रिय मानव अधिकार आयोग",
        "role": "Human rights protection",
    },
    {
        "name": "Public Service Commission",
        "nepali": "लोक सेवा आयोग",
        "role": "Civil service recruitment",
    },
    {"name": "Auditor General", "nepali": "महालेखा परीक्षक", "role": "Government audit"},
]


# Electoral System
ELECTORAL_SYSTEM = """
Nepal's Electoral System:

House of Representatives (275 seats):
  - 165 seats: First-Past-The-Post (FPTP) from single-member constituencies
  - 110 seats: Proportional Representation (PR) from party lists
  - Term: 5 years
  - Voting age: 18 years

Provincial Assemblies (550 seats total across 7 provinces):
  - 60% seats: FPTP from constituencies
  - 40% seats: PR from party lists
  - Each province has different number of seats based on population

Local Elections:
  - Direct election of mayors/chairpersons and ward representatives
  - Separate elections for local bodies every 5 years
  - Reserved seats for women and marginalized communities

Electoral Constituencies:
  - 165 parliamentary constituencies for FPTP elections
  - Constituencies based on population and geography
  - Periodic delimitation by Election Commission
"""


# Cultural Context
CULTURAL_CONTEXT = """
Nepal's Cultural and Social Context:

Demographics:
  - Population: ~30 million (2021 census)
  - Ethnic groups: 125+ distinct ethnic groups
  - Languages: 123 languages spoken (Nepali is official language)
  - Religions: Hinduism (81%), Buddhism (9%), Islam (4%), others

Name Conventions:
  - Most Nepalis have 2-3 part names
  - Caste/ethnic surnames are common (Poudel, Sharma, Gurung, Tamang, etc.)
  - Some use single names or titles
  - Devanagari script (नेपाली) is official script
  - Romanization varies (Poudel/Paudel, Oli/Olii, etc.)

Political Culture:
  - Multi-party democracy since 1990
  - Coalition governments are common
  - Frequent government changes
  - Strong regional and ethnic identity politics
  - Youth engagement increasing in recent years

Historical Context:
  - Unified by Prithvi Narayan Shah in 1768
  - Never colonized (maintained independence)
  - Constitutional monarchy until 2008
  - Federal republic since 2008
  - New constitution in 2015 establishing federal structure
"""


# Relationship Types in Nepali Politics
POLITICAL_RELATIONSHIP_TYPES = {
    "MEMBER_OF": "Party membership",
    "LEADER_OF": "Party leadership position",
    "AFFILIATED_WITH": "Political affiliation or alliance",
    "REPRESENTS": "Electoral representation (constituency)",
    "MINISTER_IN": "Cabinet position in government",
    "ELECTED_FROM": "Electoral constituency",
    "BORN_IN": "Place of birth",
    "RESIDES_IN": "Place of residence",
    "EDUCATED_AT": "Educational institution",
    "FOUNDED": "Founded organization/party",
    "SUCCEEDED_BY": "Political succession",
    "PRECEDED_BY": "Previous holder of position",
    "COALITION_WITH": "Political coalition/alliance",
    "OPPOSED_TO": "Political opposition",
}


def get_province_info(province_name: str) -> Dict:
    """Get information about a specific province.

    Args:
        province_name: Name of the province (English or Nepali)

    Returns:
        Dictionary with province information
    """
    for province in ADMINISTRATIVE_DIVISIONS["provinces"]["list"]:
        if (
            province["name"].lower() == province_name.lower()
            or province["nepali"] == province_name
        ):
            return province
    return {}


def get_party_info(party_name: str) -> Dict:
    """Get information about a specific political party.

    Args:
        party_name: Name of the party (English or Nepali)

    Returns:
        Dictionary with party information
    """
    for party in MAJOR_POLITICAL_PARTIES:
        if party["name"].lower() == party_name.lower() or party["nepali"] == party_name:
            return party
    return {}


def validate_administrative_hierarchy(
    location_type: str, parent_type: str = None
) -> bool:
    """Validate if a location type can be a child of a parent type.

    Args:
        location_type: Type of the location (province, district, etc.)
        parent_type: Type of the parent location (optional)

    Returns:
        True if the hierarchy is valid
    """
    hierarchy = {
        "province": [],  # Top level
        "district": ["province"],
        "metropolitan_city": ["district", "province"],
        "sub_metropolitan_city": ["district", "province"],
        "municipality": ["district", "province"],
        "rural_municipality": ["district", "province"],
        "ward": [
            "metropolitan_city",
            "sub_metropolitan_city",
            "municipality",
            "rural_municipality",
        ],
        "constituency": ["district", "province"],
    }

    if location_type not in hierarchy:
        return False

    if parent_type is None:
        return True

    return parent_type in hierarchy[location_type]
