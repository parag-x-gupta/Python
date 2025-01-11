import pandas as pd

df = pd.read_csv('employees.csv')
total_earned = lambda row: row['hourly_wage'] * 1.5 * (row['hours_worked'] - 40) + row['hourly_wage'] * 40 if row['hours_worked'] > 40 else row['hourly_wage'] * row['hours_worked']

df['total_earned'] = df.apply(total_earned, axis = 1)


df = pd.read_csv('imdb.csv')

# Rename columns here
df.columns = ['ID', 'Title', 'Category', 'Year Released', 'Rating']
print(df)
df.columns = ['ID', 'Title', 'Category', 'Year Released', 'Rating']

df.rename(columns = {
  'name' : 'movie_title'
}, inplace = True)
print(df)


orders = pd.read_csv('shoefly.csv')
print(orders.head())

orders['shoe_source'] = orders.apply( lambda row: 'animal' if row.shoe_material == 'leather' else 'vegan', axis = 1)

print(orders.head())

orders['salutation'] = orders.apply(lambda row : f'Dear Mr. {row.last_name}' if row.gender == 'male' else f'Dear Ms. {row.last_name}', axis = 1)

print(orders.head())
