import pandas as pd 

products = [
    {'PRODUCT_ID': 'PID_00001', 'PRODUCT_NAME': 'NesKafe Gold', 'CATEGORY': 'Coffee', 'UNIT_COST': 7.50, 'UNIT_PRICE': 12.99, 'WEIGHT': 1},
    {'PRODUCT_ID': 'PID_00002', 'PRODUCT_NAME': 'NesKafe Classic', 'CATEGORY': 'Coffee', 'UNIT_COST': 3.20, 'UNIT_PRICE': 4.99, 'WEIGHT': 1},
    {'PRODUCT_ID': 'PID_00003', 'PRODUCT_NAME': 'NesKafe Cappucino', 'CATEGORY': 'Coffee', 'UNIT_COST': 5.40, 'UNIT_PRICE': 8.49, 'WEIGHT': 1},
    {'PRODUCT_ID': 'PID_00004', 'PRODUCT_NAME': 'NesKafe Decaf', 'CATEGORY': 'Coffee', 'UNIT_COST': 7.80, 'UNIT_PRICE': 11.99, 'WEIGHT': 1},
    {'PRODUCT_ID': 'PID_00005', 'PRODUCT_NAME': 'NesKafe Instant', 'CATEGORY': 'Coffee', 'UNIT_COST': 5.60, 'UNIT_PRICE': 8.99, 'WEIGHT': 1},
    {'PRODUCT_ID': 'PID_00006', 'PRODUCT_NAME': 'NesKafe Latte', 'CATEGORY': 'Coffee', 'UNIT_COST': 5.40, 'UNIT_PRICE': 8.49, 'WEIGHT': 1},
    {'PRODUCT_ID': 'PID_00007', 'PRODUCT_NAME': 'NesKafe Mocha', 'CATEGORY': 'Coffee', 'UNIT_COST': 4.20, 'UNIT_PRICE': 6.99, 'WEIGHT': 1},
    {'PRODUCT_ID': 'PID_00008', 'PRODUCT_NAME': 'PureLife Natural', 'CATEGORY': 'Water', 'UNIT_COST': 0.85, 'UNIT_PRICE': 1.29, 'WEIGHT': 1},
    {'PRODUCT_ID': 'PID_00009', 'PRODUCT_NAME': 'PureLife Sparkling', 'CATEGORY': 'Water', 'UNIT_COST': 1.40, 'UNIT_PRICE': 2.49, 'WEIGHT': 1},
    {'PRODUCT_ID': 'PID_00010', 'PRODUCT_NAME': 'PureLife Flavored', 'CATEGORY': 'Water', 'UNIT_COST': 1.65, 'UNIT_PRICE': 2.99, 'WEIGHT': 1},
    {'PRODUCT_ID': 'PID_00011', 'PRODUCT_NAME': 'AquaFlow Premium', 'CATEGORY': 'Water', 'UNIT_COST': 2.80, 'UNIT_PRICE': 4.49, 'WEIGHT': 1},
    {'PRODUCT_ID': 'PID_00012', 'PRODUCT_NAME': 'SpringSource Mountain', 'CATEGORY': 'Water', 'UNIT_COST': 3.50, 'UNIT_PRICE': 5.99, 'WEIGHT': 1},
    {'PRODUCT_ID': 'PID_00013', 'PRODUCT_NAME': 'CrystalClear Pure', 'CATEGORY': 'Water', 'UNIT_COST': 4.20, 'UNIT_PRICE': 6.99, 'WEIGHT': 1},
    {'PRODUCT_ID': 'PID_00014', 'PRODUCT_NAME': 'ChocoBars Dark', 'CATEGORY': 'Chocolate', 'UNIT_COST': 8.50, 'UNIT_PRICE': 13.99, 'WEIGHT': 1},
    {'PRODUCT_ID': 'PID_00015', 'PRODUCT_NAME': 'ChocoBars Milk', 'CATEGORY': 'Chocolate', 'UNIT_COST': 9.20, 'UNIT_PRICE': 14.99, 'WEIGHT': 1},
    {'PRODUCT_ID': 'PID_00016', 'PRODUCT_NAME': 'ChocoBars White', 'CATEGORY': 'Chocolate', 'UNIT_COST': 5.70, 'UNIT_PRICE': 8.99, 'WEIGHT': 1},
    {'PRODUCT_ID': 'PID_00017', 'PRODUCT_NAME': 'ChocoBars Almond', 'CATEGORY': 'Chocolate', 'UNIT_COST': 10.80, 'UNIT_PRICE': 16.99, 'WEIGHT': 1},
    {'PRODUCT_ID': 'PID_00018', 'PRODUCT_NAME': 'SweetTreats Original', 'CATEGORY': 'Chocolate', 'UNIT_COST': 3.60, 'UNIT_PRICE': 5.49, 'WEIGHT': 1},
    {'PRODUCT_ID': 'PID_00019', 'PRODUCT_NAME': 'SweetTreats Caramel', 'CATEGORY': 'Chocolate', 'UNIT_COST': 4.20, 'UNIT_PRICE': 6.49, 'WEIGHT': 1},
    {'PRODUCT_ID': 'PID_00020', 'PRODUCT_NAME': 'ChocoWafers Crispy', 'CATEGORY': 'Chocolate', 'UNIT_COST': 6.80, 'UNIT_PRICE': 10.99, 'WEIGHT': 1},
    {'PRODUCT_ID': 'PID_00021', 'PRODUCT_NAME': 'CreamyBites Hazelnut', 'CATEGORY': 'Chocolate', 'UNIT_COST': 4.80, 'UNIT_PRICE': 7.49, 'WEIGHT': 1},
    {'PRODUCT_ID': 'PID_00022', 'PRODUCT_NAME': 'DeluxeChoc Premium', 'CATEGORY': 'Chocolate', 'UNIT_COST': 14.50, 'UNIT_PRICE': 22.99, 'WEIGHT': 1},
    {'PRODUCT_ID': 'PID_00023', 'PRODUCT_NAME': 'BabyFirst Formula', 'CATEGORY': 'Baby Food', 'UNIT_COST': 7.80, 'UNIT_PRICE': 12.49, 'WEIGHT': 1},
    {'PRODUCT_ID': 'PID_00024', 'PRODUCT_NAME': 'BabyFirst Organic', 'CATEGORY': 'Baby Food', 'UNIT_COST': 9.20, 'UNIT_PRICE': 14.99, 'WEIGHT': 1},
    {'PRODUCT_ID': 'PID_00025', 'PRODUCT_NAME': 'BabyFirst Cereal', 'CATEGORY': 'Baby Food', 'UNIT_COST': 5.40, 'UNIT_PRICE': 8.49, 'WEIGHT': 1},
    {'PRODUCT_ID': 'PID_00026', 'PRODUCT_NAME': 'TinyTots Puree', 'CATEGORY': 'Baby Food', 'UNIT_COST': 3.60, 'UNIT_PRICE': 5.99, 'WEIGHT': 1},
    {'PRODUCT_ID': 'PID_00027', 'PRODUCT_NAME': 'LittleOnes Snacks', 'CATEGORY': 'Baby Food', 'UNIT_COST': 6.20, 'UNIT_PRICE': 9.99, 'WEIGHT': 1},
    {'PRODUCT_ID': 'PID_00028', 'PRODUCT_NAME': 'InfantCare Plus', 'CATEGORY': 'Baby Food', 'UNIT_COST': 4.80, 'UNIT_PRICE': 7.99, 'WEIGHT': 1},
    {'PRODUCT_ID': 'PID_00029', 'PRODUCT_NAME': 'CreamyDelight Vanilla', 'CATEGORY': 'Dairy', 'UNIT_COST': 2.80, 'UNIT_PRICE': 4.49, 'WEIGHT': 1},
    {'PRODUCT_ID': 'PID_00030', 'PRODUCT_NAME': 'CreamyDelight Chocolate', 'CATEGORY': 'Dairy', 'UNIT_COST': 3.60, 'UNIT_PRICE': 5.99, 'WEIGHT': 1},
    {'PRODUCT_ID': 'PID_00031', 'PRODUCT_NAME': 'CreamyDelight Strawberry', 'CATEGORY': 'Dairy', 'UNIT_COST': 3.40, 'UNIT_PRICE': 5.49, 'WEIGHT': 1},
    {'PRODUCT_ID': 'PID_00032', 'PRODUCT_NAME': 'FrozenJoy Cookies', 'CATEGORY': 'Dairy', 'UNIT_COST': 4.50, 'UNIT_PRICE': 7.49, 'WEIGHT': 1},
    {'PRODUCT_ID': 'PID_00033', 'PRODUCT_NAME': 'FrozenJoy Mint', 'CATEGORY': 'Dairy', 'UNIT_COST': 3.80, 'UNIT_PRICE': 6.29, 'WEIGHT': 1},
    {'PRODUCT_ID': 'PID_00034', 'PRODUCT_NAME': 'PremiumScoop Deluxe', 'CATEGORY': 'Dairy', 'UNIT_COST': 7.20, 'UNIT_PRICE': 11.99, 'WEIGHT': 1},
    {'PRODUCT_ID': 'PID_00035', 'PRODUCT_NAME': 'MorningCrunch Honey', 'CATEGORY': 'Cereals', 'UNIT_COST': 3.80, 'UNIT_PRICE': 5.99, 'WEIGHT': 1},
    {'PRODUCT_ID': 'PID_00036', 'PRODUCT_NAME': 'MorningCrunch Chocolate', 'CATEGORY': 'Cereals', 'UNIT_COST': 4.20, 'UNIT_PRICE': 6.49, 'WEIGHT': 1},
    {'PRODUCT_ID': 'PID_00037', 'PRODUCT_NAME': 'HealthyStart Oats', 'CATEGORY': 'Cereals', 'UNIT_COST': 2.40, 'UNIT_PRICE': 3.99, 'WEIGHT': 1},
    {'PRODUCT_ID': 'PID_00038', 'PRODUCT_NAME': 'FiberPlus Original', 'CATEGORY': 'Cereals', 'UNIT_COST': 3.60, 'UNIT_PRICE': 5.49, 'WEIGHT': 1},
    {'PRODUCT_ID': 'PID_00039', 'PRODUCT_NAME': 'KidsChoice Fruity', 'CATEGORY': 'Cereals', 'UNIT_COST': 4.80, 'UNIT_PRICE': 7.49, 'WEIGHT': 1},
    {'PRODUCT_ID': 'PID_00040', 'PRODUCT_NAME': 'PetLove Dry Food', 'CATEGORY': 'Pet Care', 'UNIT_COST': 8.50, 'UNIT_PRICE': 13.99, 'WEIGHT': 1},
    {'PRODUCT_ID': 'PID_00041', 'PRODUCT_NAME': 'PetLove Wet Food', 'CATEGORY': 'Pet Care', 'UNIT_COST': 5.40, 'UNIT_PRICE': 8.49, 'WEIGHT': 1},
    {'PRODUCT_ID': 'PID_00042', 'PRODUCT_NAME': 'PetLove Treats', 'CATEGORY': 'Pet Care', 'UNIT_COST': 3.80, 'UNIT_PRICE': 5.99, 'WEIGHT': 1},
    {'PRODUCT_ID': 'PID_00043', 'PRODUCT_NAME': 'PetCare Premium', 'CATEGORY': 'Pet Care', 'UNIT_COST': 12.80, 'UNIT_PRICE': 19.99, 'WEIGHT': 1}
]

def create_products():
    products_df = pd.DataFrame(products)
    products_df['WEIGHT'] = 100
    return products_df