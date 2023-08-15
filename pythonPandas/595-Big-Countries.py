import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    world.query('area >= 3000000 | population >= 25000000', inplace=True)
    return world[['name','population','area']]



''' TestCase : 
data = [['Afghanistan', 'Asia', 652230, 25500100, 20343000000], ['Albania', 'Europe', 28748, 2831741, 12960000000], ['Algeria', 'Africa', 2381741, 37100000, 188681000000], ['Andorra', 'Europe', 468, 78115, 3712000000], ['Angola', 'Africa', 1246700, 20609294, 100990000000]]
World = pd.DataFrame(data, columns=['name', 'continent', 'area', 'population', 'gdp']).astype({'name':'object', 'continent':'object', 'area':'Int64', 'population':'Int64', 'gdp':'Int64'})
print(World)
print()
print(big_countries(World))'''