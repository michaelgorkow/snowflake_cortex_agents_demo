import numpy as np
import pandas as pd 
from faker import Faker

np.random.seed(42)
Faker.seed(0)
fake = Faker()

# US Census-inspired age distribution
def create_census_age_distribution():
    # Age ranges and their approximate proportions
    age_ranges = [
        (18, 24, 0.115),   # Young adults: 11.5% (increased from 9%)
        (25, 34, 0.179),   # Millennials: 17.9% (increased from 14%)
        (35, 44, 0.167),   # Gen X: 16.7% (increased from 13%)
        (45, 54, 0.167),   # Gen X: 16.7% (increased from 13%)
        (55, 64, 0.167),   # Baby Boomers: 16.7% (increased from 13%)
        (65, 100, 0.205)   # Seniors: 20.5% (increased from 16%)
    ]
    
    ages = []
    weights = []
    
    for min_age, max_age, proportion in age_ranges:
        # Create uniform distribution within each range
        range_ages = list(range(min_age, max_age + 1))
        range_weights = [proportion / len(range_ages)] * len(range_ages)
        
        ages.extend(range_ages)
        weights.extend(range_weights)
    
    return ages, weights

def create_person(ages, weights):
    gender = np.random.choice(['MALE','FEMALE'])
    if gender == 'MALE':
        first_name = fake.first_name_male()
    if gender == 'FEMALE':
        first_name = fake.first_name_female()
    last_name = fake.last_name()
    
    age = np.random.choice(ages, size=1, p=weights)[0]
    
    country = np.random.choice(['Germany','United Kingdom','France','Italy','Spain','Denmark','Sweden','Norway'], 1)[0]
    weight = 1
    return [gender,first_name,last_name,age,country, weight]

def create_customers(n=5):
    ages, weights = create_census_age_distribution()
    customers_df = pd.DataFrame([create_person(ages=ages, weights=weights) for i in range(n)], columns=['GENDER','FIRST_NAME','LAST_NAME','AGE','COUNTRY','WEIGHT'])
    customers_df.insert(0, 'CUST_ID', [f'CID_{i:05d}' for i in range(1000,1000+n)])
    return customers_df