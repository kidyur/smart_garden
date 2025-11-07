"""
PANDAS
1. # open file 
   # analyze its data (misses, features and their types),
   # show first N lines
   # show basic statistics by one particular feature
   # count headers and lines

NUMPY
2. # compare % of rescued (men and women)
   # count mean of age (men and women)
   # count mean age of rescued (men and women) and died (also)

FILTERING 
3. # age > 30 AND man AND I class
   # (age <= 18 OR women) AND rescued
   group by Pclass and sex
                    | Pclass | sex
   mean_age         |    X
   % of rescued     |    
   mean_ticket_cost |    X
"""

import pandas as pd
import numpy as np

# 1.
df = pd.read_csv('./tested.csv')
print(df.info())
n = 5
print(df.head(n))
print(df['Fare'][df['Fare'] > 10].count()) 
amount_of_cols = len(df.columns.to_list())
print(len(df.columns.to_list()), df.size // amount_of_cols)

# 2.
people = df[['Sex', 'Survived']]
men = people[people['Sex'] == 'male']
men_survived = men[men['Survived'] == 1]
men_cnt = men.to_numpy()
men_survived_cnt = men[men['Survived'] == 1].to_numpy()
print(men_survived_cnt.shape[0] / men_cnt.shape[0] * 100)

women = people[people['Sex'] == 'female']
women_survived = women[women['Survived'] == 1]
women_cnt = women.to_numpy()
women_survived_cnt = women[women['Survived'] == 1].to_numpy()
print(women_survived_cnt.shape[0] / women_cnt.shape[0] * 100)

df_ages = df[['Sex','Age']]
men = df_ages[df_ages['Sex'] == 'male']['Age'].dropna()
print(np.mean(men.to_numpy()))

women = df_ages[df_ages['Sex'] == 'female']['Age'].dropna()
print(np.mean(women.to_numpy()))

df_survive = df[['Sex', 'Survived', 'Age']]
men = df_survive[df_survive['Sex'] == 'male']
print(men[men['Survived'] == 0]['Age'].dropna().to_numpy().mean())
print(men[men['Survived'] == 1]['Age'].dropna().to_numpy().mean())

women = df_survive[df_survive['Sex'] == 'female']
print(women[women['Survived'] == 0]['Age'].dropna().to_numpy().mean())
print(women[women['Survived'] == 1]['Age'].dropna().to_numpy().mean())

# 3.
print(df[(df['Age'] > 30) & (df['Sex'] == 'male') & (df['Pclass'] == 1)])
print(df[((df['Age'] <= 18) | (df['Sex'] == 'male')) & (df['Survived'] == 1)])
print(df[['Pclass', 'Sex']])

print(df.groupby(['Pclass'])['Age'].mean())
print(df.groupby(['Pclass'])['Ticket'].min())
print(df.groupby(['Pclass'])['Survived'].sum() / df.groupby(['Pclass'])['Survived'].count())
