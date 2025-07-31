--!jinja
-- Switch context
USE ROLE AI_ENGINEER;
USE WAREHOUSE AI_WH;
USE DATABASE AI_DEVELOPMENT;
CREATE OR REPLACE SCHEMA SI_NESDATA;

-- Create the table for customer customers
CREATE FILE FORMAT nesdata_format
  TYPE = parquet;

CREATE OR REPLACE TABLE CUSTOMERS
  USING TEMPLATE (
    SELECT ARRAY_AGG(OBJECT_CONSTRUCT(*))
    WITHIN GROUP (ORDER BY order_id)
      FROM TABLE(
        INFER_SCHEMA(
          LOCATION => '@DEMO_DATA/customers.parquet',
          FILE_FORMAT => 'nesdata_format'
        )
      )
  );

COPY INTO CUSTOMERS
  FROM @DEMO_DATA/customers.parquet
  FILE_FORMAT = 'nesdata_format'
  MATCH_BY_COLUMN_NAME = CASE_INSENSITIVE;

-- Create the table for products
CREATE OR REPLACE TABLE PRODUCTS
  USING TEMPLATE (
    SELECT ARRAY_AGG(OBJECT_CONSTRUCT(*))
    WITHIN GROUP (ORDER BY order_id)
      FROM TABLE(
        INFER_SCHEMA(
          LOCATION => '@DEMO_DATA/products.parquet',
          FILE_FORMAT => 'nesdata_format'
        )
      )
  );

COPY INTO PRODUCTS
  FROM @DEMO_DATA/products.parquet
  FILE_FORMAT = 'nesdata_format'
  MATCH_BY_COLUMN_NAME = CASE_INSENSITIVE;

-- Create the table for customer transactions
CREATE OR REPLACE TABLE CUSTOMER_TRANSACTIONS
  USING TEMPLATE (
    SELECT ARRAY_AGG(OBJECT_CONSTRUCT(*))
    WITHIN GROUP (ORDER BY order_id)
      FROM TABLE(
        INFER_SCHEMA(
          LOCATION => '@DEMO_DATA/customer_transactions.parquet',
          FILE_FORMAT => 'nesdata_format'
        )
      )
  );

COPY INTO CUSTOMER_TRANSACTIONS
  FROM @DEMO_DATA/customer_transactions.parquet
  FILE_FORMAT = 'nesdata_format'
  MATCH_BY_COLUMN_NAME = CASE_INSENSITIVE;

-- Create the table for customer sessions
CREATE OR REPLACE TABLE CUSTOMER_SESSIONS
  USING TEMPLATE (
    SELECT ARRAY_AGG(OBJECT_CONSTRUCT(*))
    WITHIN GROUP (ORDER BY order_id)
      FROM TABLE(
        INFER_SCHEMA(
          LOCATION => '@DEMO_DATA/customer_sessions.parquet',
          FILE_FORMAT => 'nesdata_format'
        )
      )
  );

COPY INTO CUSTOMER_SESSIONS
  FROM @DEMO_DATA/customer_transactions.parquet
  FILE_FORMAT = 'customer_sessions'
  MATCH_BY_COLUMN_NAME = CASE_INSENSITIVE;

-- Create Demo Notebook
CREATE OR REPLACE NOTEBOOK SI_NESDATA_DEMO_SETUP
    FROM '@AI_DEVELOPMENT.PUBLIC.GITHUB_REPO_CORTEX_AGENTS_DEMO/branches/{{BRANCH}}/use_cases/newsdata' 
        MAIN_FILE = 'SETUP_AGENT_STAYBNB.ipynb' 
        QUERY_WAREHOUSE = AI_WH;
ALTER NOTEBOOK SI_NESDATA_DEMO_SETUP ADD LIVE VERSION FROM LAST;

-- Whether to execute the notebook or not during initial demo setup
{% if EXECUTE_NOTEBOOKS %}
    EXECUTE NOTEBOOK SI_NESDATA_DEMO_SETUP();
{%- endif -%}