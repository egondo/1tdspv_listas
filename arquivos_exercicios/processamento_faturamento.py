''''
pip install pandas
pip install matplotlib
'''

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("faturamento_anual.txt", sep=";")
#print(df)

df['total diario'] = df['quantidade'] * df['valor']
#print(df)
df_anual = pd.pivot_table(df, values=["quantidade", "total diario"], index=['loja'], aggfunc=["sum"]) 
#print(df_anual)

df_anual = pd.pivot_table(df, values=['quantidade'], index=['produto', 'marca'], aggfunc="sum")
#print(df_anual)

df['mes'] = df['data'].apply(lambda x: int(x.split('/')[1]))

df_mensal = pd.pivot_table(df, aggfunc="sum", values='total diario',
                           index=["mes"], columns='loja')
print(df_mensal)

df_mensal.plot(kind='bar')
plt.title('Faturamento mensal por loja')
plt.xlabel('mes')
plt.ylabel('total diario')
plt.xticks(rotation=0)
plt.show()

'''
df_samsung = df.query("marca == 'Samsung' and produto == 'smartphone'")
print(df_samsung)

print(df['produto'].unique())
'''