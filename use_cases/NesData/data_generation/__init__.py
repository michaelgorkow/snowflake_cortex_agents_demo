from .customers import create_customers
from .products import create_products
from .transactions_sessions import create_transactions_sessions


def create_demo_data(session):
    customers_df = create_customers(2000)
    products_df = create_products()
    transactions_df, sessions_df = create_transactions_sessions(customers_df, products_df)

    # Final dataframes
    snow_products_df = session.write_pandas(
        df=products_df[['PRODUCT_ID','PRODUCT_NAME','CATEGORY','UNIT_COST','UNIT_PRICE']], 
        table_name='PRODUCTS', 
        auto_create_table=True, 
        overwrite=True, 
        use_logical_type=True
    )
    
    snow_customers_df = session.write_pandas(
        df=customers_df[['CUST_ID','GENDER','FIRST_NAME','LAST_NAME','AGE','COUNTRY']],
        table_name='CUSTOMERS', 
        auto_create_table=True, 
        overwrite=True, 
        use_logical_type=True
    )
    
    
    snow_transactions_df = session.write_pandas(
        df=transactions_df,
        table_name='CUSTOMER_TRANSACTIONS', 
        auto_create_table=True, 
        overwrite=True, 
        use_logical_type=True
    )
    
    snow_sessions_df = session.write_pandas(
        df=sessions_df,
        table_name='CUSTOMER_SESSIONS', 
        auto_create_table=True, 
        overwrite=True, 
        use_logical_type=True
    )
    print('Successfully created demo data.')