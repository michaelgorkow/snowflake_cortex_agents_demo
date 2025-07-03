USE ROLE ACCOUNTADMIN;
USE WAREHOUSE COMPUTE_WH;
CREATE OR REPLACE SCHEMA CORTEX_AGENTS_DEMO.FINANCE_FOOD_BEVERAGE;

CREATE OR REPLACE STAGE DOCUMENTS
  DIRECTORY = (ENABLE = TRUE)
  ENCRYPTION = ( TYPE = 'SNOWFLAKE_SSE' );

CREATE OR REPLACE NOTEBOOK SETUP_AGENT_FINANCE_FOOD_BEVERAGE
    FROM '@CORTEX_AGENTS_DEMO.PUBLIC.GITHUB_REPO_CORTEX_AGENTS_DEMO/branches/{{BRANCH}}/use_cases/nesdata' 
        MAIN_FILE = 'SETUP_AGENT_FINANCE_FOOD_BEVERAGE.ipynb' 
        QUERY_WAREHOUSE = COMPUTE_WH;
ALTER NOTEBOOK SETUP_AGENT_FINANCE_FOOD_BEVERAGE ADD LIVE VERSION FROM LAST;

-- Whether to execute the notebook or not during initial demo setup
{% if EXECUTE_NOTEBOOKS %}
    EXECUTE NOTEBOOK SETUP_AGENT_FINANCE_FOOD_BEVERAGE();
{%- endif -%}

-- Creating the semantic view
create or replace semantic view CORTEX_AGENTS_DEMO.FINANCE_FOOD_BEVERAGE.FINANCE_SEMANTIC_MODEL
	tables (
		CAMPAIGNS primary key (CATEGORY) with synonyms=('advertisements','promotions','marketing campaigns','ad campaigns','promotional activities','sales promotions','advertising initiatives') comment='This table stores information about marketing campaigns, including the campaign''s unique identifier, name, category, start and end periods, allocated budget, and discount percentage offered during the campaign.',
		CUSTOMERS primary key (CUSTOMER_ID) with synonyms=('clients','patrons','buyers','consumers','customers_list','customer_base','client_base','customer_database') comment='This table stores information about customers, including their unique identifier, name, type (e.g. individual, business, etc.), geographic region, and credit limit.',
		PRODUCTS primary key (CATEGORY,PRODUCT_ID) with synonyms=('items','goods','merchandise','commodities','stock','inventory','products_list','product_catalog') comment='This table stores information about the products offered by a company, including a unique identifier, product name, category, and pricing details.',
		SALES primary key (PRODUCT_ID) with synonyms=('SALES_DATA','SALES_INFO','SALES_RECORDS','TRANSACTION_DATA','SALES_TRANSACTIONS','REVENUE_DATA') comment='This table stores sales transaction data, capturing key information about each sale, including the transaction ID, customer and product details, sales period, quantity sold, pricing, revenue, cost, and profit.',
		TIME_PERIODS primary key (PERIOD_ID) with synonyms=('time_periods','time_frames','periods','time_intervals','date_ranges','calendar_periods','fiscal_periods','reporting_periods') comment='This table stores information about specific time periods, including the period ID, year, month, quarter, month name, and a specific date. It appears to be a date dimension table, which is commonly used in data warehousing and business intelligence applications to provide a centralized repository of date-related data for reporting and analysis purposes.'
	)
	relationships (
		CAMPAIGNS_TO_TIME_PERIOD_END as CAMPAIGNS(END_PERIOD) references TIME_PERIODS(PERIOD_ID),
		CAMPAIGNS_TO_TIME_PERIOD_START as CAMPAIGNS(START_PERIOD) references TIME_PERIODS(PERIOD_ID),
		CAMPAIGNS_TO_PRODUCT as PRODUCTS(CATEGORY) references CAMPAIGNS(CATEGORY),
		SALES_TO_PRODUCT as PRODUCTS(PRODUCT_ID) references SALES(PRODUCT_ID),
		SALES_TO_CUSTOMERS as SALES(CUSTOMER_ID) references CUSTOMERS(CUSTOMER_ID),
		SALES_TO_TIME_PERIODS as SALES(PERIOD_ID) references TIME_PERIODS(PERIOD_ID)
	)
	facts (
		CAMPAIGNS.BUDGET as BUDGET with synonyms=('funds_allocated','allocated_amount','financial_plan','cost_plan','expense_limit','financial_allocation','allocated_funds','cost_estimate') comment='The budget allocated for each marketing campaign.',
		CAMPAIGNS.DISCOUNT_PERCENT as DISCOUNT_PERCENT with synonyms=('discount_rate','percentage_off','promo_percentage','sale_percentage','markdown_percentage','percent_discount','discount_percentage_value') comment='The percentage discount offered to customers as part of a marketing campaign.',
		CUSTOMERS.CREDIT_LIMIT as CREDIT_LIMIT with synonyms=('max_credit','credit_ceiling','credit_maximu','credit_upper_limit','maximum_credit_allowed','credit_limit_amount') comment='The maximum amount of credit that a customer is a allowed to use for purchases.',
		PRODUCTS.UNIT_COST as UNIT_COST with synonyms=('cost_per_unit','unit_price_base','base_cost','cost_per_item','unit_expense','item_cost') comment='The cost of a single unit of each product, representing the amount the company pays to produce or purchase one item.',
		PRODUCTS.UNIT_PRICE as UNIT_PRICE with synonyms=('price_per_unit','selling_price','list_price','retail_price','item_price') comment='The price of each product per unit.',
		SALES.GROSS_PROFIT as GROSS_PROFIT with synonyms=('gross_margin','profit','net_gain','earnings','total_profit','revenue_surplus','income','net_earnings','profit_margin') comment='The total profit earned from sales after deducting the cost of goods sold, representing the amount left over to cover operating expenses and generate net income.',
		SALES.QUANTITY_SOLD as QUANTITY_SOLD with synonyms=('units_sold','items_sold','sales_volume','quantity_purchased','amout_sold','volume_sold','sales_quantity') comment='The total number of units of a product sold during a transaction.',
		SALES.TOTAL_COST as TOTAL_COST with synonyms=('total_expense','total_spend','total_outlay','total_expenditure','overall_cost','total_outgoings') comment='The total cost of a sale, representing the overall amount spent by a customer on a particular transaction.',
		SALES.TOTAL_REVENUE as TOTAL_REVENUE with synonyms=('total_sales','total_income','revenue_total','total_revenue_generated','total_turnover','total_receipts','total_earnings') comment='The total revenue generated from sales, representing the total amount of money earned from the sale of products or services.',
		SALES.UNIT_PRICE as UNIT_PRICE with synonyms=('item_price','price_per_unit','cost_per_item','unit_cost','base_price','list_price','selling_price','price_per_item') comment='The price of a single unit of a product sold.'
	)
	dimensions (
		CAMPAIGNS.CAMPAIGN_ID as CAMPAIGN_ID with synonyms=('campaign_key','campaign_number','campaign_code','marketing_id','promo_id','ad_id') comment='Unique identifier for a marketing campaign.',
		CAMPAIGNS.CAMPAIGN_NAME as CAMPAIGN_NAME with synonyms=('advertising_name','marketing_campaign','promotion_name','campaign_title','ad_name','promo_name') comment='The name of a specific marketing campaign run by the company.',
		CAMPAIGNS.CATEGORY as CATEGORY with synonyms=('type','classification','group','genre','kind','class','sort','label','designation') comment='The category of product or service being promoted in the campaign.',
		CAMPAIGNS.END_PERIOD as END_PERIOD with synonyms=('end_date','end_time','period_end','expiration_date','termination_date','closing_period','final_date','last_date') comment='The end date of the campaign period, represented as a numerical value.',
		CAMPAIGNS.START_PERIOD as START_PERIOD with synonyms=('start_date','initial_period','beginning_period','commencement_date','kickoff_date','launch_date','period_start','start_time') comment='The start period of a campaign, representing the month when the campaign was initiated, with values ranging from 3 to 8, likely corresponding to the third to eighth months of the year.',
		CUSTOMERS.CUSTOMER_ID as CUSTOMER_ID with synonyms=('customer_key','client_id','account_number','customer_number','client_id_number','account_id') comment='Unique identifier for each customer in the database, used to distinguish and reference individual customers across various transactions and interactions.',
		CUSTOMERS.CUSTOMER_NAME as CUSTOMER_NAME with synonyms=('client_name','account_holder','account_name','client_title','customer_title','full_name','account_owner') comment='The name of the customer, which can be a physical store location or an online entity.',
		CUSTOMERS.CUSTOMER_TYPE as CUSTOMER_TYPE with synonyms=('customer_category','client_type','account_type','customer_classification','client_classification','account_classification') comment='The type of business or organization that the customer represents, such as a retail store, supermarket, or wholesale distributor.',
		CUSTOMERS.REGION as REGION with synonyms=('area','territory','zone','district','location','geographic_area','province','state','county','municipality') comment='Geographic region where the customer is located.',
		PRODUCTS.CATEGORY as CATEGORY with synonyms=('type','classification','group','product_type','product_group','class','genre','kind') comment='The category of the product, which can be one of the 3 types: Coffee, Water, or Chocolate, indicating the main classification or grouping of the product.',
		PRODUCTS.PRODUCT_ID as PRODUCT_ID with synonyms=('product_key','item_id','product_number','item_number','product_code','sku','product_identifier') comment='Unique identifier for each product in the catalog.',
		PRODUCTS.PRODUCT_NAME as PRODUCT_NAME with synonyms=('item_name','product_title','item_title','product_description','product_label','item_label') comment='The type of NesKafe coffee product beign sold.',
		SALES.CUSTOMER_ID as CUSTOMER_ID with synonyms=('client_id','customer_number','account_id','client_number','account_holder_id','user_id') comment='Unique identifier for the customer who made the purchase.',
		SALES.PERIOD_ID as PERIOD_ID with synonyms=('time_period','reporting_period','fiscal_period','accounting_period','cycle_id','interval_id','time_interval','period_number') comment='A unique identifier for a specific time period, such as a month, quarter, or year, used to track sales performance over time.',
		SALES.PRODUCT_ID as PRODUCT_ID with synonyms=('item_id','product_code','item_code','product_number','sku','product_key') comment='Unique identifier for the product being sold.',
		SALES.TRANSACTION_ID as TRANSACTION_ID with synonyms=('order_id','transaction_number','sale_id','invoice_number','purchase_id','deal_id','trade_id') comment='Unique identifier for each sales transaction.',
		TIME_PERIODS.DATE as DATE with synonyms=('day','calendar_date','timestamp','datestamp','calendar_day','date_value') comment='Date dimension representing specific points in time, used to track and analyze data over distinct periods.',
		TIME_PERIODS.MONTH as MONTH with synonyms=('month_number','month_value','month_code','calendar_month','month_of_year','month_index') comment='The month of the year in which a specific event or transaction occurred, represented by a numerical value (1-12), with the provided values indicating January, March, and April.',
		TIME_PERIODS.MONTH_NAME as MONTH_NAME with synonyms=('month_description','month_full_name','full_month_name','month_label','month_title','month_text') comment='The month of the year in which a specific event or transaction occurred.',
		TIME_PERIODS.PERIOD_ID as PERIOD_ID with synonyms=('period_key','time_period_identifier','id','time_id','interval_id','cycle_id') comment='Unique identifier for a specific time period, used to distinguish between different intervals of time.',
		TIME_PERIODS.QUARTER as QUARTER with synonyms=('quarterly_period','financial_quarter','qtr','fiscal_quarter','quarterly_term') comment='The quarter of the year in which a specific event or metric occurred, with possible values being Q1 (January to March), Q2 (April to June), and Q3 (July to September).',
		TIME_PERIODS.YEAR as YEAR with synonyms=('year_value','annual_period','fiscal_year','calendar_year','yearly_period','twelve_month_period') comment='The year in which the data was recorded or the event occurred.'
	)
	comment='This models represents the global sales and marketing operations of a major food and beverage company, tracking financial performance across key product categories including coffee, water, chocolate, baby food, dairy, cereals, and pet care products. The data captures 24 months of transactional sales data from diverse customer channels (supermarkets, hypermarkets, online retailers, and distributors) across five major geographic regions, enabling comprehensive revenue, profitability, and market performance analysis. Additionally, the dataset includes marketing campaign information to measure promotional effectiveness and seasonal trends, providing insights for strategic decision-making in product portfolio management and customer relationship optimization.'
	with extension (CA='{"tables":[{"name":"CAMPAIGNS","dimensions":[{"name":"CAMPAIGN_ID","sample_values":["1","2","3"]},{"name":"CAMPAIGN_NAME","cortex_search_service":{"database":"CORTEX_AGENTS_DEMO","schema":"FINANCE_FOOD_BEVERAGE","service":"_ANALYST_CAMPAIGN_SEARCH"}},{"name":"CATEGORY","sample_values":["Coffee","Water","Cereals"]},{"name":"END_PERIOD","sample_values":["5","8","9"]},{"name":"START_PERIOD","sample_values":["3","6","8"]}],"facts":[{"name":"BUDGET","sample_values":["500000","750000","400000"]},{"name":"DISCOUNT_PERCENT","sample_values":["15","10","20"]}]},{"name":"CUSTOMERS","dimensions":[{"name":"CUSTOMER_ID","sample_values":["1","2","3"]},{"name":"CUSTOMER_NAME","cortex_search_service":{"database":"CORTEX_AGENTS_DEMO","schema":"FINANCE_FOOD_BEVERAGE","service":"_ANALYST_CUSTOMER_NAME_SEARCH"}},{"name":"CUSTOMER_TYPE","sample_values":["Convenience Store","Supermarket","Distributor"]},{"name":"REGION","sample_values":["Middle East & Africa","North America","Europe"]}],"facts":[{"name":"CREDIT_LIMIT","sample_values":["500000","50000","1000000"]}]},{"name":"PRODUCTS","dimensions":[{"name":"CATEGORY","sample_values":["Coffee","Water","Chocolate"]},{"name":"PRODUCT_ID","sample_values":["1","2","3"]},{"name":"PRODUCT_NAME","cortex_search_service":{"database":"CORTEX_AGENTS_DEMO","schema":"FINANCE_FOOD_BEVERAGE","service":"_ANALYST_PRODUCT_NAME_SEARCH"}}],"facts":[{"name":"UNIT_COST","sample_values":["9.77","4.49","11.18"]},{"name":"UNIT_PRICE","sample_values":["1.6","6.36","17.24"]}]},{"name":"SALES","dimensions":[{"name":"CUSTOMER_ID","sample_values":["4","26","16"]},{"name":"PERIOD_ID","sample_values":["1","2","3"]},{"name":"PRODUCT_ID","sample_values":["42","22","13"]},{"name":"TRANSACTION_ID","sample_values":["1","2","3"]}],"facts":[{"name":"GROSS_PROFIT","sample_values":["7890.2","3917.07","-1067.76"]},{"name":"QUANTITY_SOLD","sample_values":["671","829","204"]},{"name":"TOTAL_COST","sample_values":["6025.58","3150.2","2933.52"]},{"name":"TOTAL_REVENUE","sample_values":["13915.78","7067.27","1865.76"]},{"name":"UNIT_PRICE","sample_values":["20.74","8.53","9.15"]}]},{"name":"TIME_PERIODS","dimensions":[{"name":"MONTH","sample_values":["1","3","4"]},{"name":"MONTH_NAME","sample_values":["January","March","April"]},{"name":"PERIOD_ID","sample_values":["1","2","3"]},{"name":"QUARTER","sample_values":["Q1","Q2","Q3"]},{"name":"YEAR","sample_values":["2022","2023"]}],"time_dimensions":[{"name":"DATE","sample_values":["2022-01-01","2022-03-02","2022-05-31"]}]}],"relationships":[{"name":"CAMPAIGNS_TO_TIME_PERIOD_END","relationship_type":"many_to_one","join_type":"inner"},{"name":"CAMPAIGNS_TO_TIME_PERIOD_START","relationship_type":"many_to_one","join_type":"inner"},{"name":"CAMPAIGNS_TO_PRODUCT","relationship_type":"many_to_one"},{"name":"SALES_TO_PRODUCT","relationship_type":"one_to_one","join_type":"left_outer"},{"name":"SALES_TO_CUSTOMERS","relationship_type":"many_to_one","join_type":"inner"},{"name":"SALES_TO_TIME_PERIODS","relationship_type":"many_to_one","join_type":"inner"}],"verified_queries":[{"name":"campaign_impact","question":"What''s the impact of marketing campaigns on sales performance?","use_as_onboarding_question":false,"sql":"SELECT camp.campaign_name, SUM(CASE WHEN t.period_id BETWEEN camp.start_period AND camp.end_period THEN s.total_revenue ELSE 0 END) AS campaign_revenue, SUM(CASE WHEN NOT t.period_id BETWEEN camp.start_period AND camp.end_period THEN s.total_revenue ELSE 0 END) AS non_campaign_revenue, camp.budget FROM campaigns AS camp JOIN products AS p ON camp.category = p.category JOIN sales AS s ON p.product_id = s.product_id JOIN time_periods AS t ON s.period_id = t.period_id GROUP BY camp.campaign_id, camp.campaign_name, camp.budget","verified_by":"Michael Gorkow","verified_at":1751456609},{"name":"monthly_rolling_average_per_category","question":"Calculate the 3-month rolling average revenue for each product category.","use_as_onboarding_question":false,"sql":"WITH monthly_category_revenue AS (SELECT p.category, t.year, t.month, SUM(s.total_revenue) AS monthly_revenue FROM sales AS s JOIN products AS p ON s.product_id = p.product_id JOIN time_periods AS t ON s.period_id = t.period_id GROUP BY p.category, t.year, t.month) SELECT category, year, month, AVG(monthly_revenue) OVER (PARTITION BY category ORDER BY year, month ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) AS rolling_3month_avg FROM monthly_category_revenue ORDER BY category, year, month","verified_by":"Michael Gorkow","verified_at":1751456896}]}');

-- Add the agent to Snowflake Intelligence
INSERT INTO SNOWFLAKE_INTELLIGENCE.AGENTS.CONFIG 
(
    AGENT_NAME,
    AGENT_DESCRIPTION,
    GRANTEE_ROLES,
    TOOLS,
    TOOL_RESOURCES,
    TOOL_CHOICE,
    RESPONSE_INSTRUCTION,
    SAMPLE_QUESTIONS
)
SELECT 
    'FINANCE_FOOD_BEVERAGE2',
    'AI agent specialized in answering finance and sales questions.',
    ['PUBLIC'],
    PARSE_JSON('[
      {
        "tool_spec": {
          "name": "SEARCH_CUSTOMER_CONTRACTS",
          "type": "cortex_search"
        }
      },
      {
        "tool_spec": {
          "name": "SEARCH_FINANCIAL_OPERATIONS_REPORTS",
          "type": "cortex_search"
        }
      },
      {
        "tool_spec": {
          "name": "SEARCH_MARKETING_CAMPAIGNS",
          "type": "cortex_search"
        }
      },
      {
        "tool_spec": {
          "name": "SEARCH_PRODUCT_SPECIFICATIONS",
          "type": "cortex_search"
        }
      },
      {
        "tool_spec": {
          "name": "SEARCH_REGIONAL_MARKET_REPORTS",
          "type": "cortex_search"
        }
      },
      {
        "tool_spec": {
          "name": "FINANCE_SEMANTIC_MODEL",
          "type": "cortex_analyst_text_to_sql"
        }
      }
    ]'),
    PARSE_JSON('{
      "FINANCE_SEMANTIC_MODEL": {
        "semantic_view": "CORTEX_AGENTS_DEMO.FINANCE_FOOD_BEVERAGE.FINANCE_SEMANTIC_MODEL"
      },
      "SEARCH_CUSTOMER_CONTRACTS": {
        "id_column": "URL",
        "name": "CORTEX_AGENTS_DEMO.FINANCE_FOOD_BEVERAGE.SEARCH_CUSTOMER_CONTRACTS"
      },
      "SEARCH_FINANCIAL_OPERATIONS_REPORTS": {
        "id_column": "URL",
        "name": "CORTEX_AGENTS_DEMO.FINANCE_FOOD_BEVERAGE.SEARCH_FINANCIAL_OPERATIONS_REPORTS"
      },
      "SEARCH_MARKETING_CAMPAIGNS": {
        "id_column": "URL",
        "name": "CORTEX_AGENTS_DEMO.FINANCE_FOOD_BEVERAGE.SEARCH_MARKETING_CAMPAIGNS"
      },
      "SEARCH_PRODUCT_SPECIFICATIONS": {
        "id_column": "URL",
        "name": "CORTEX_AGENTS_DEMO.FINANCE_FOOD_BEVERAGE.SEARCH_PRODUCT_SPECIFICATIONS"
      },
      "SEARCH_REGIONAL_MARKET_REPORTS": {
        "id_column": "URL",
        "name": "CORTEX_AGENTS_DEMO.FINANCE_FOOD_BEVERAGE.SEARCH_REGIONAL_MARKET_REPORTS"
      }
    }'),
    NULL,
    '',
    [];