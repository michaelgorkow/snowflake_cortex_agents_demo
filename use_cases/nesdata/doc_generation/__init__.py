from .customer_contracts import create_customer_contracts
from .financial_operations import create_financial_operational_reports
from .marketing_campaigns import create_marketing_campaign_documents
from .product_specifications import create_product_specification_sheets
from .regional_market_reports import create_regional_market_reports

def generate_demo_documents(session):
    create_customer_contracts(session)
    create_financial_operational_reports(session)
    create_marketing_campaign_documents(session)
    create_product_specification_sheets(session)
    create_regional_market_reports(session)
    session.sql('ALTER STAGE DOCUMENTS REFRESH').collect()
    print('Finished generating demo documents.')