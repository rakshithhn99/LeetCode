import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    merged_df = customers.merge(orders, left_on='id', right_on='customerId', how='left')
    merged_df.rename(columns={'name':'Customers'},inplace=True)
    result_df = merged_df[merged_df['customerId'].isna()]
    print(result_df)
    return result_df[['Customers']]


'''Test Case :
data = [[1, 'Joe'], [2, 'Henry'], [3, 'Sam'], [4, 'Max']]
Customers = pd.DataFrame(data, columns=['id', 'name']).astype({'id':'Int64', 'name':'object'})
data = [[1, 3], [2, 1]]
Orders = pd.DataFrame(data, columns=['id', 'customerId']).astype({'id':'Int64', 'customerId':'Int64'})

print(find_customers(Customers,Orders)) '''