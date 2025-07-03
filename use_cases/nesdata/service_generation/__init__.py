def create_cortex_search_service(session, folder):
    session.sql(f"""
    CREATE OR REPLACE TABLE _UNSTR_RAW_DOCUMENTS_{folder.upper()} AS
        SELECT 
            RELATIVE_PATH,
            TO_VARCHAR (
                SNOWFLAKE.CORTEX.PARSE_DOCUMENT (
                    '@DOCUMENTS',
                    RELATIVE_PATH,
                    {{'mode': 'LAYOUT'}} ):content
                ) AS EXTRACTED_LAYOUT 
        FROM 
            DIRECTORY('@DOCUMENTS')
        WHERE
            startswith(RELATIVE_PATH, '{folder}/');
    """).collect()
    print(f'Generated table with raw documents: _UNSTR_RAW_DOCUMENTS_{folder.upper()}')

    session.sql(f"""
    CREATE OR REPLACE TABLE _UNSTR_CHUNKED_DOCUMENTS_{folder.upper()} AS
        SELECT
           RELATIVE_PATH,
           GET_PRESIGNED_URL(@DOCUMENTS, RELATIVE_PATH, 604800) AS URL,
           c.INDEX::INTEGER AS CHUNK_INDEX,
           c.value::TEXT AS CHUNK_TEXT
        FROM
           _UNSTR_RAW_DOCUMENTS_{folder.upper()},
           LATERAL FLATTEN( input => SNOWFLAKE.CORTEX.SPLIT_TEXT_RECURSIVE_CHARACTER (
              EXTRACTED_LAYOUT,
              'markdown',
              4000,
              0,
              ['\n\n', '\n', ' ', '']
           )) c;
    """).collect()
    print(f'Generated table with chunked documents: _UNSTR_CHUNKED_DOCUMENTS_{folder.upper()}')

    session.sql(f"""
    CREATE OR REPLACE CORTEX SEARCH SERVICE SEARCH_{folder.upper()}
      ON CHUNK_TEXT
      ATTRIBUTES RELATIVE_PATH, CHUNK_INDEX
      WAREHOUSE = COMPUTE_WH

      
      TARGET_LAG = '1 hour'
      EMBEDDING_MODEL = 'snowflake-arctic-embed-l-v2.0'
    AS (
      SELECT
          CHUNK_TEXT,
          RELATIVE_PATH,
          CHUNK_INDEX,
          URL
      FROM _UNSTR_CHUNKED_DOCUMENTS_{folder.upper()}
    );
    """).collect()
    print(f'Generated Cortex Search Service : SEARCH_{folder.upper()}')