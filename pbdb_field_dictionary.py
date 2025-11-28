"""
Paleobiology Database (PBDB) Field Name Dictionary
===================================================

This dictionary translates PBDB's abbreviated field names (compact format)
to their full, readable names (verbose format).

Source: https://paleobiodb.org/data1.2/occs/list_doc.html
Last Updated: November 2024

Usage:
------
# Import the dictionary
from pbdb_field_dictionary import pbdb_fields

# Rename columns in your DataFrame
df = df.rename(columns=pbdb_fields)

# Or access individual translations
full_name = pbdb_fields.get('tna', 'accepted_name')

Note for Students:
------------------
PBDB offers two formats for data downloads:
1. COMPACT: Short field names (e.g., 'tna', 'oid', 'cid') - saves bandwidth
2. VERBOSE: Full field names (e.g., 'accepted_name', 'occurrence_id') - more readable

This dictionary helps you convert compact to verbose format in your analysis.
"""

# Complete PBDB field name translations
pbdb_fields = {
    
    # =======================================================================
    # IDENTIFICATION FIELDS
    # =======================================================================
    # These fields uniquely identify records in the database
    
    'oid': 'occurrence_id',          # Unique identifier for fossil occurrence
    'cid': 'collection_no',          # Unique identifier for collection
    'ids': 'species_name',           # The species name (if any)
    'rid': 'reference_id',           # Primary reference for this record
    'eid': 'early_id',               # Identifier for early interval
    'lid': 'late_id',                # Identifier for late interval
    'iid': 'identified_by_id',       # Person who identified the specimen
    'reid': 'reidentified_by_id',    # Person who reidentified the specimen
    
    # =======================================================================
    # TAXONOMY - ACCEPTED (CURRENT) NAMES
    # =======================================================================
    # The currently accepted taxonomic classification
    
    'tna': 'accepted_name',          # Currently accepted taxonomic name
    'rnk': 'accepted_rank',          # Rank (species, genus, family, etc.)
    'tid': 'taxon_id',               # Unique identifier for accepted taxon
    'tnr': 'taxon_no',               # Alternative taxon number
    
    # Taxonomic hierarchy - labels
    'phl': 'phylum',                 # Phylum name
    'cll': 'class',                  # Class name
    'odl': 'order',                  # Order name  
    'fml': 'family',                 # Family name
    'gnl': 'genus',                  # Genus name
    'sgn': 'subgenus',               # Subgenus name (if applicable)
    
    # Taxonomic hierarchy - numeric identifiers
    'phn': 'phylum_no',              # Phylum numeric ID
    'cln': 'class_no',               # Class numeric ID
    'odn': 'order_no',               # Order numeric ID
    'fmn': 'family_no',              # Family numeric ID
    'gnn': 'genus_no',               # Genus numeric ID
    
    # =======================================================================
    # TAXONOMY - ORIGINAL IDENTIFICATION
    # =======================================================================
    # The original name as published (may differ from accepted name)
    
    'idn': 'identified_name',        # Original identification name
    'idq': 'identification_qualifier', # Qualifier (cf., aff., ?, etc.)
    'idr': 'identified_rank',        # Rank of original identification
    
    # =======================================================================
    # TEMPORAL (TIME) DATA
    # =======================================================================
    # Age and geological time information
    
    'eag': 'max_ma',              # Early age (older bound in Ma)
    'lag': 'min_ma',               # Late age (younger bound in Ma)
    'oei': 'early_interval',         # Early time interval name
    'oli': 'late_interval',          # Late time interval name
    
    # =======================================================================
    # SPATIAL (GEOGRAPHIC) DATA
    # =======================================================================
    # Location information
    
    'lat': 'lat',                    # Latitude (decimal degrees)
    'lng': 'lng',                    # Longitude (decimal degrees)
    'pla': 'paleolat',               # Paleolatitude (reconstructed)
    'pln': 'paleolng',               # Paleolongitude (reconstructed)
    'gsc': 'geogscale',              # Geographic scale/precision
    'cc':  'cc',                     # Country code (ISO 2-letter)
    'stp': 'state',                  # State/province name
    'cny': 'county',                 # County name
    
    # =======================================================================
    # GEOLOGICAL CONTEXT
    # =======================================================================
    # Stratigraphic and geological information
    
    'fmn': 'formation',              # Geological formation name
    'sgr': 'stratigraphic_group',    # Stratigraphic group
    'mbr': 'member',                 # Member name
    'lth': 'lithology1',             # Primary lithology
    'lt2': 'lithology2',             # Secondary lithology
    'env': 'environment',            # Depositional environment
    
    # =======================================================================
    # TAPHONOMY & PRESERVATION
    # =======================================================================
    # Information about fossil preservation
    
    'prs': 'preservation',           # Type of preservation
    'prl': 'preservation_quality',   # Quality of preservation
    
    # =======================================================================
    # ABUNDANCE & ECOLOGY
    # =======================================================================
    # Quantitative and ecological information
    
    'abv': 'abundance_value',        # Abundance count/estimate
    'abu': 'abundance_unit',         # Unit of abundance measurement
    'lif': 'life_habit',             # Life habit (e.g., mobile, sessile)
    'mht': 'microhabitat',           # Specific habitat within environment
    'die': 'diet',                   # Dietary preference
    'vis': 'vision',                 # Visual capability
    'loc': 'locomotion',             # Mode of locomotion
    'rep': 'reproduction',           # Reproductive mode
    'ont': 'ontogeny',               # Ontogenetic stage
    
    # =======================================================================
    # COLLECTION METHODS & METADATA
    # =======================================================================
    # How and when the data was collected
    
    'col': 'collection_name',        # Name of collection
    'cln': 'collection_no',          # Collection number
    'prc': 'collection_method',      # Collection method
    'siz': 'collection_size',        # Size of collection
    'cc1': 'collection_coverage',    # Areal coverage of collection
    'cny': 'collectors',             # Names of collectors
    'cdt': 'collection_dates',       # Date(s) of collection
    
    # =======================================================================
    # REFERENCES & AUTHORIZERS
    # =======================================================================
    # Publication and authorization information
    
    'ref': 'reference_no',           # Reference number
    'rft': 'ref_type',               # Type of reference
    'ati': 'ref_author',             # Author(s) of reference
    'pbt': 'ref_pubyr',              # Publication year
    'rfp': 'ref_publication',        # Publication name
    'aut': 'authorizer',             # Person who authorized entry
    'eni': 'enterer',                # Person who entered data
    'mdf': 'modifier',               # Person who last modified entry
    'ath': 'authorized_by',          # Authorization information
    'ent': 'entered_by',             # Entry information
    'mdb': 'modified_by',            # Modification information
    'crd': 'created',                # Creation date
    'mdd': 'modified',               # Last modification date
    
    # =======================================================================
    # SPECIMEN INFORMATION
    # =======================================================================
    # Details about specific specimens
    
    'spe': 'specimen_id',            # Specimen identifier
    'sid': 'specimen_no',            # Specimen number
    'sex': 'sex',                    # Biological sex
    'prt': 'part',                   # Body part preserved
    
    # =======================================================================
    # RESEARCH GROUP & PROJECT
    # =======================================================================
    # Research context
    
    'rgp': 'research_group',         # Research group name
    'prj': 'project_name',           # Project name
    
    # =======================================================================
    # TAXONOMIC OPINION FIELDS
    # =======================================================================
    # Fields related to taxonomic decisions
    
    'opi': 'opinion_no',             # Opinion number
    'ops': 'opinion_status',         # Status of opinion
    'opb': 'opinion_basis',          # Basis for opinion
    'opr': 'opinion_ref',            # Reference for opinion
    
    # =======================================================================
    # MEASUREMENT & MORPHOLOGY
    # =======================================================================
    # Quantitative measurements (when available)
    
    'msf': 'measurement_source',     # Source of measurements
    'ms1': 'measurement_1',          # First measurement
    'ms2': 'measurement_2',          # Second measurement
    'ms3': 'measurement_3',          # Third measurement
    
    # =======================================================================
    # PLANT-SPECIFIC FIELDS
    # =======================================================================
    # Fields specific to plant fossils
    
    'plo': 'plant_organ',            # Plant organ type
    'plf': 'plant_form',             # Plant form/architecture
    
    # =======================================================================
    # TRACE FOSSIL FIELDS
    # =======================================================================
    # Fields for ichnofossils (trace fossils)
    
    'ich': 'ichnofossil_type',       # Type of trace fossil
    'bhv': 'behavior',               # Behavior represented
    
    # =======================================================================
    # ADDITIONAL CONTEXT
    # =======================================================================
    # Miscellaneous important fields
    
    'typ': 'occurrence_type',        # Type of occurrence record
    'fld': 'associated_fields',      # Fields present in this record
    'rer': 'reid_reason',            # Reason for reidentification
    'cmt': 'comments',               # Free-text comments
    'pco': 'private_comment',        # Private comments (may not be public)
}


# =======================================================================
# REVERSE DICTIONARY (for converting verbose back to compact)
# =======================================================================
pbdb_fields_reverse = {v: k for k, v in pbdb_fields.items()}


# =======================================================================
# FIELD CATEGORIES FOR TEACHING
# =======================================================================
# Organized by category to help students understand field relationships
field_categories = {
    'identification': [
        'occurrence_id', 'collection_id', 'reference_id', 'taxon_id'
    ],
    
    'taxonomy': [
        'accepted_name', 'accepted_rank', 'phylum', 'class', 'order',
        'family', 'genus', 'subgenus'
    ],
    
    'temporal': [
        'max_ma', 'min_ma', 'mid_ma', 'early_interval', 'late_interval'
    ],
    
    'spatial': [
        'lat', 'lng', 'paleolat', 'paleolng', 'country', 'state', 'county'
    ],
    
    'geological': [
        'formation', 'member', 'stratigraphic_group', 'lithology1',
        'lithology2', 'environment'
    ],
    
    'ecology': [
        'life_habit', 'diet', 'locomotion', 'environment', 'microhabitat'
    ],
    
    'preservation': [
        'preservation', 'preservation_quality', 'part'
    ],
    
    'abundance': [
        'abundance_value', 'abundance_unit'
    ]
}


# =======================================================================
# ESSENTIAL FIELDS FOR COMMON ANALYSES
# =======================================================================
# Recommended fields to include for different research questions

essential_fields_by_analysis = {
    'diversity_analysis': [
        'occurrence_id', 'collection_id', 'accepted_name', 'accepted_rank',
        'phylum', 'class', 'order', 'family', 'genus',
        'max_ma', 'min_ma', 'early_interval', 'late_interval'
    ],
    
    'paleogeography': [
        'occurrence_id', 'accepted_name', 'lat', 'lng', 
        'paleolat', 'paleolng', 'max_ma', 'min_ma'
    ],
    
    'paleoecology': [
        'occurrence_id', 'accepted_name', 'environment', 'life_habit',
        'diet', 'locomotion', 'lithology1', 'max_ma', 'min_ma'
    ],
    
    'taphonomy': [
        'occurrence_id', 'accepted_name', 'preservation', 
        'preservation_quality', 'part', 'lithology1', 'environment'
    ],
    
    'temporal_patterns': [
        'occurrence_id', 'collection_id', 'accepted_name', 'accepted_rank',
        'max_ma', 'min_ma', 'early_interval', 'late_interval'
    ],
    
    'sampling_bias': [
        'occurrence_id', 'collection_id', 'lat', 'lng',
        'max_ma', 'min_ma', 'formation', 'lithology1',
        'collection_method', 'reference_id'
    ]
}


# =======================================================================
# HELPER FUNCTIONS
# =======================================================================

def translate_columns(df, direction='compact_to_verbose'):
    """
    Translate DataFrame column names between compact and verbose formats.
    
    Parameters:
    -----------
    df : pandas.DataFrame
        DataFrame with PBDB data
    direction : str
        'compact_to_verbose' (default) or 'verbose_to_compact'
    
    Returns:
    --------
    pandas.DataFrame
        DataFrame with translated column names
    
    Example:
    --------
    >>> df_verbose = translate_columns(df_compact, 'compact_to_verbose')
    >>> df_compact = translate_columns(df_verbose, 'verbose_to_compact')
    """
    if direction == 'compact_to_verbose':
        return df.rename(columns=pbdb_fields)
    elif direction == 'verbose_to_compact':
        return df.rename(columns=pbdb_fields_reverse)
    else:
        raise ValueError("direction must be 'compact_to_verbose' or 'verbose_to_compact'")


def get_fields_for_analysis(analysis_type):
    """
    Get recommended fields for a specific type of analysis.
    
    Parameters:
    -----------
    analysis_type : str
        Type of analysis (e.g., 'diversity_analysis', 'paleogeography')
    
    Returns:
    --------
    list
        List of recommended field names (verbose format)
    
    Example:
    --------
    >>> fields = get_fields_for_analysis('diversity_analysis')
    >>> df_subset = df[fields]
    """
    if analysis_type in essential_fields_by_analysis:
        return essential_fields_by_analysis[analysis_type]
    else:
        available = ', '.join(essential_fields_by_analysis.keys())
        raise ValueError(f"Unknown analysis type. Available: {available}")


def print_field_info(field_name, dictionary=pbdb_fields):
    """
    Print information about a specific field.
    
    Parameters:
    -----------
    field_name : str
        Either compact or verbose field name
    
    Example:
    --------
    >>> print_field_info('tna')
    Compact: tna
    Verbose: accepted_name
    Category: taxonomy
    """
    # Check if it's compact or verbose
    if field_name in pbdb_fields:
        compact = field_name
        verbose = pbdb_fields[field_name]
    elif field_name in pbdb_fields_reverse:
        compact = pbdb_fields_reverse[field_name]
        verbose = field_name
    else:
        print(f"Field '{field_name}' not found in dictionary")
        return
    
    # Find category
    category = None
    for cat, fields in field_categories.items():
        if verbose in fields:
            category = cat
            break
    
    print(f"Compact name: {compact}")
    print(f"Verbose name: {verbose}")
    if category:
        print(f"Category: {category}")


def show_all_fields_by_category():
    """
    Print all available fields organized by category.
    Useful for teaching and reference.
    """
    print("=" * 70)
    print("PBDB FIELD REFERENCE - ORGANIZED BY CATEGORY")
    print("=" * 70)
    
    for category, fields in field_categories.items():
        print(f"\n{category.upper().replace('_', ' ')}")
        print("-" * 70)
        for field in fields:
            compact = pbdb_fields_reverse.get(field, 'N/A')
            print(f"  {compact:6s} → {field}")


# =======================================================================
# MAIN EXECUTION (for testing and demonstration)
# =======================================================================

if __name__ == "__main__":
    """
    Demonstration of dictionary usage for students.
    """
    
    print("PBDB Field Dictionary - Usage Examples")
    print("=" * 70)
    
    # Example 1: Show all fields by category
    print("\n1. All fields organized by category:")
    print("-" * 70)
    show_all_fields_by_category()
    
    # Example 2: Look up a specific field
    print("\n\n2. Looking up a specific field:")
    print("-" * 70)
    print_field_info('tna')
    
    # Example 3: Get fields for an analysis
    print("\n\n3. Recommended fields for diversity analysis:")
    print("-" * 70)
    fields = get_fields_for_analysis('diversity_analysis')
    print(f"Number of fields: {len(fields)}")
    print("Fields:", ', '.join(fields))
    
    # Example 4: Show statistics
    print("\n\n4. Dictionary Statistics:")
    print("-" * 70)
    print(f"Total fields in dictionary: {len(pbdb_fields)}")
    print(f"Number of categories: {len(field_categories)}")
    print(f"Analysis types available: {len(essential_fields_by_analysis)}")
    
    print("\n" + "=" * 70)
    print("✓ Dictionary loaded successfully!")
    print("  Import this file to use translations in your analysis")
    print("=" * 70)
