import pandas as pd
import numpy as np
import random
from datetime import datetime, date

np.random.seed(42)
random.seed(42)

def create_increasing_list_random(size, start_value=1000, increase=True):
    """
    Creates a list of increasing values with random increase each iteration.
    
    Args:
        size: Number of elements in the list
        start_value: Starting value (default: 100)
    
    Returns:
        List of increasing values
    """
    values = [start_value]
    
    for i in range(1, size):
        if increase == True:
            increase_percent = random.uniform(0.002, 0.003)
        else:
            increase_percent = random.uniform(-0.002, -0.003)
        next_value = values[-1] * (1 + increase_percent)
        values.append(int(next_value))
    
    return values

campaigns = {
    'cocoa_issues':{
        'dates':['2024-02-01','2024-05-31'],
        'products':["ChocoBars Dark", "ChocoBars Milk", "ChocoBars White", "ChocoBars Almond", "SweetTreats Original", "SweetTreats Caramel", "ChocoWafers Crispy", "CreamyBites Hazelnut", "DeluxeChoc Premium"],
        'countries':['Germany','United Kingdom','France','Italy','Spain','Denmark','Sweden','Norway'],
        'gender':'NONE',
        'add_sales':-100,
        'increase':False,
        'channel':{'options':['Instagram','TikTok','YouTube','Facebook','Website'],'weights':[1,1,1,1,1]}
    },
    'Babys First, Parents Choice':{
        'dates':['2024-07-01','2024-08-31'],
        'products':['BabyFirst Organic','BabyFirst Formula'],
        'countries':['Norway','Denmark','Sweden'],
        'gender':'FEMALE',
        'device':['iOS'],
        'add_sales':100,
        'increase':True,
        'channel':{'options':['Instagram','TikTok','YouTube','Facebook','Website'],'weights':[5,1,1,3,1]}
    },
    'neskafe_production_issues':{
        'dates':['2024-10-15','2024-11-30'],
        'products':['NesKafe Gold', 'NesKafe Classic','NesKafe Cappucino','NesKafe Decaf', 'NesKafe Instant', 'NesKafe Latte','NesKafe Mocha'],
        'countries':['Germany','United Kingdom','France','Italy','Spain','Denmark','Sweden','Norway'],
        'gender':'NONE',
        'add_sales':-200,
        'increase':False,
        'channel':{'options':['Instagram','TikTok','YouTube','Facebook','Website'],'weights':[1,1,1,1,1]}
    },
    'Sweet December':{
        'dates':['2024-12-01','2024-12-31'],
        'products':['SweetTreats Original','SweetTreats Caramel'],
        'countries':['Norway','Denmark','Sweden'],
        'gender':'MALE',
        'add_sales':200,
        'increase':True,
        'channel':{'options':['Instagram','TikTok','YouTube','Facebook','Website'],'weights':[5,3,1,1,1]}
    },
    'We love our pets!':{
        'dates':['2025-02-01','2024-03-31'],
        'products':['PetCare Premium'],
        'countries':['Norway','Denmark','Sweden'],
        'gender':'FEMALE',
        'add_sales':150,
        'increase':True,
        'channel':{'options':['Instagram','TikTok','YouTube','Facebook','Website'],'weights':[5,4,2,1,1]},
    },
    'Coffee Lover':{
        'dates':['2025-04-01','2025-05-30'],
        'products':['NesKafe Gold','NesKafe Cappucino'],
        'countries':['Germany','Spain','Norway','Denmark','Sweden'],
        'gender':'MALE',
        'add_sales':300,
        'increase':True,
        'channel':{'options':['Instagram','TikTok','YouTube','Facebook','Website'],'weights':[4,3,5,1,1]},
    },
    'Stay Hydrated':{
        'dates':['2025-06-01','2025-07-30'],
        'products':['PureLife Natural','PureLife Sparkling','PureLife Flavored'],
        'countries':['United Kingdom','Italy','France'],
        'gender':'FEMALE',
        'add_sales':350,
        'increase':True,
        'channel':{'options':['Instagram','TikTok','YouTube','Facebook','Website'],'weights':[5,3,1,4,1]},
    }
}

def create_transactions_sessions(customers_df, products_df):
    # Create date range from 2024-01-01 until today
    transaction_dates_df = pd.DataFrame({'DATE': pd.date_range(start='2024-01-01', end=pd.Timestamp.today(), freq='D')})
    # Add base sales and campaign column
    transaction_dates_df['BASE_SALES'] = create_increasing_list_random(size=len(transaction_dates_df),start_value=1001)
    transaction_dates_df['CAMPAIGN'] = 'NONE'
    
    # add campaign data and adjust sales
    for campaign in campaigns.keys():
        start_date, end_date = campaigns[campaign]['dates']
        add_sales = campaigns[campaign]['add_sales']
        increase = campaigns[campaign]['increase']
        mask = transaction_dates_df['DATE'].between(start_date, end_date)
        transaction_dates_df.loc[mask, 'CAMPAIGN'] = campaign
        transaction_dates_df.loc[mask, 'BASE_SALES'] += create_increasing_list_random(size=mask.sum(),start_value=add_sales, increase=increase)
    
    
    transactions = []
    for ix, row in transaction_dates_df.iterrows():
        base_sales = row['BASE_SALES']
        products_df['WEIGHT'] = 100
        customers_df['WEIGHT'] = 1
        in_campaign = False
        if row.CAMPAIGN in campaigns.keys():
            in_campaign = True
            if campaigns[row.CAMPAIGN]['increase'] == True:
                # Set product weights
                products_df.loc[products_df['PRODUCT_NAME'].isin(campaigns[row.CAMPAIGN]['products']), 'WEIGHT'] = 300
            if campaigns[row.CAMPAIGN]['increase'] == False:
                products_df.loc[products_df['PRODUCT_NAME'].isin(campaigns[row.CAMPAIGN]['products']), 'WEIGHT'] = 40
    
            # Set customer weights
            if campaigns[row.CAMPAIGN]['gender'] != 'NONE':
                customers_df.loc[customers_df['GENDER'] == campaigns[row.CAMPAIGN]['gender'], 'WEIGHT'] += 2
            customers_df.loc[customers_df['COUNTRY'].isin(campaigns[row.CAMPAIGN]['countries']), 'WEIGHT'] += 4
    
            # Get channel weights
            channel_options, channel_weights = campaigns[row.CAMPAIGN]['channel']['options'], campaigns[row.CAMPAIGN]['channel']['weights']
            
        while base_sales > 0:
            cust_id, country, _, = customers_df[['CUST_ID','COUNTRY','WEIGHT']].sample(1, weights='WEIGHT').values.tolist()[0]
            product_name, product_id, unit_price, _ = products_df[['PRODUCT_NAME','PRODUCT_ID','UNIT_PRICE','WEIGHT']].sample(1, weights='WEIGHT').values.tolist()[0]
            quantity = 1
            if in_campaign:
                channel = np.random.choice(channel_options,1,channel_weights)[0]
                session_length = random.randint(120,150)
            else:
                channel = np.random.choice(['Instagram','TikTok','YouTube','Facebook','Website'])
                session_length = random.randint(90,130)
            transactions.append([row.DATE,cust_id,product_id,product_name,country,unit_price,quantity,channel,session_length])
            base_sales -= unit_price
        if ix % 50 == 0:
            print(f'{ix:03d} dates processed.')

    transactions_df = pd.DataFrame(transactions, columns=['DATE','CUST_ID','PRODUCT_ID','PRODUCT_NAME','COUNTRY','UNIT_PRICE','QUANTITY','CHANNEL','SESSION_LENGTH'])
    transactions_df['SESSION_ID'] = [f'SESS_ID_{i:05d}' for i in range(len(transactions_df))]
    sessions_df = transactions_df[['SESSION_ID','SESSION_LENGTH','CHANNEL']]
    transactions_df = transactions_df[['DATE','CUST_ID','PRODUCT_ID','SESSION_ID','QUANTITY']]
    return transactions_df, sessions_df