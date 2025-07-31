# NesData

![NesData](resources/nesdata_intro.jpg)

## Overview
**NesData** is a global food and beverage company that creates products for everyday moments and special occasions. From chocolate and coffee to bottled water, frozen meals, and pet nutrition, NesData offers a diverse portfolio of trusted brands found in kitchens and pantries worldwide.

NesData's analysts want to better understand what drives their business and therefore build a Cortex Agent that connects to multiple different data sources including sales data, revenue forecasts, marketing documents as well as news articles.

## Use Case Deployment
Make sure you have setup your AI playground environment as described [here](https://github.com/michaelgorkow/snowflake_cortex_agents_demo/tree/main/Readme.md).  

Execute this SQL Query to create and run the notebook in your account which will generate data and required services.
```sql
EXECUTE IMMEDIATE FROM @CORTEX_AGENTS_DEMO.PUBLIC.GITHUB_REPO_CORTEX_AGENTS_DEMO/branches/main/use_cases/nesdata/setup.sql
  USING (BRANCH => 'main', EXECUTE_NOTEBOOKS => TRUE) DRY_RUN = FALSE;
```

If you want to execute the notebook on your own you can set __EXECUTE_NOTEBOOKS => FALSE__.

## Use Case Architecture
This repository contains a **fictional dataset** from _NesData_ about sales transactions, customers, products, social media channel traffic as well as unstructured PDF documents about NesData's marketing campaigns and relevant news articles. In addition to that we also have unstructured data for marketing campaigns and news articles.

The entire architecture of the Agent looks like this:
![NesData Architecture](resources/nesdata_architecture_v2.jpeg)

## Use Case Tools
| Tool Type | Tool Name | Tool Description |
|---|---|---|
| Semantic View | Sales, Marketing & Forecast Data | Allows to query the main data model |
| Search Service | Marketing Campaigns | Provides access to PDF documents from marketing campaigns. |
| Search Service | News Articles | Provides access to PDF documents from news outlets. |
| Custom Tool | create_revenue_forecast | Python Tool using Facebook's [Prophet](https://github.com/facebook/prophet) library to generate a revenue forecast for a product. |
| Custom Tool | search_news | Python Tool that retrieves news from Google News for a given search string and time period. |

## Example Questions

| Question | Complexity |
|----------|---------|


## What makes questions complex?

This demo goes far beyond simple Text-to-SQL or RAG use cases. Let's examine what happens behind the scenes when you ask the following question:

> **"Which products were featured in the Stay hydrated campaign and how did their individual sales perform during the campaign and the 2 months before the campaign? Visualize sales revenue peer week in a line plot."**

![Example_Question](_resources/agents_example_question.png)

### 1. Document Analysis
The agent first identifies that this question requires finding the relevant PDF containing information about the marketing campaign, including which products were included.

It discovers the following products:
- **PureLife Natural**
- **PureLife Sparkling** 
- **PureLife Flavoured**

It also recognizes that the campaign is run between **June 1st to July 30th, 2025** which it correctly translates into the right filter criteria for the SQL query.

### 2. Complex SQL Generation
With the products and campaign period identified from the PDF document, the agent creates a sophisticated SQL query:

```sql
SELECT
    t.month_name,
    p.product_name,
    SUM(s.total_revenue) AS monthly_sales
FROM
    ai_development.si_nesdata.sales s
    INNER JOIN ai_development.si_nesdata.products p ON s.product_id = p.product_id
    INNER JOIN ai_development.si_nesdata.time_periods t ON s.period_id = t.period_id
WHERE
    p.product_name IN (
        'PureLife Natural',
        'PureLife Sparkling',
        'PureLife Flavored'
    )
    AND ct.date >= '2025-04-01'
    AND ct.date <= '2025-07-30'
GROUP BY
    t.month_name,
    t.year,
    p.product_name
ORDER BY
    t.month_name DESC NULLS LAST,
    p.product_name;
```

### 3. Intelligent Name Matching
**Note:** The product names from the PDF are not identical to those in the dataset. Did you notice the difference?

- **PDF**: "PureLife Flav**ou**red"
- **Database**: "PureLife Flav**o**red"

The agent handles this discrepancy by utilizing [Snowflake's Cortex Search integration for Semantic Models](https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-analyst/cortex-analyst-search-integration), which enables dynamic retrieval of relevant literals using hybrid search (combining lexical search with embedding search).

### 4. Visualization Generation
Finally, the agent generates the requested chart using the `data_to_chart` tool that is available to all agents by default.