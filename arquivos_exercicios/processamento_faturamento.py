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
df_anual = pd.pivot_table(df, values=["quantidade", "total diario"], index=['loja'],
                          aggfunc=["sum"]) 
#print(df_anual)

df_anual = pd.pivot_table(df, values=['quantidade'], index=['produto', 'marca'], 
                          aggfunc="sum")
#print(df_anual)

df['mes'] = df['data'].apply(lambda x: int(x.split('/')[1]))

df_ibi = df.query("loja == 'Ibirapuera'")

df_mensal = pd.pivot_table(df_ibi, aggfunc="sum", values='total diario',
                           index=["loja", "mes"])
print(df_mensal)

fig, ax = plt.subplots()
ax.plot(df_ibi['mes'], df_ibi['total diario'])
plt.show()

'''
df_samsung = df.query("marca == 'Samsung' and produto == 'smartphone'")
print(df_samsung)

print(df['produto'].unique())
'''