import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    products.query("low_fats.astype('str') == 'Y' & recyclable.astype('str') == 'Y' ", inplace=True)  #low_facts and recyclable are category type, converted to string to query. 
    return products[['product_id']]


''' TestCase : 
data = [['0', 'Y', 'N'], ['1', 'Y', 'Y'], ['2', 'N', 'Y'], ['3', 'Y', 'Y'], ['4', 'N', 'N']]
Products = pd.DataFrame(data, columns=['product_id', 'low_fats', 'recyclable']).astype({'product_id':'int64', 'low_fats':'category', 'recyclable':'category'})
print(Products)
print()
print(find_products(Products)) '''