import pandas as pd
import io
import matplotlib.pyplot as plt
 
df = pd.read_csv(io.BytesIO(uploaded['data.csv']))
print(df)


di = {"BRA": [], "NOR" : [], "NGA": []}

anos = list(range(2015, 2020))

for pais in di.keys():
    for ano in anos:
        valor = df.loc[df['Country Code'] == pais][f'{ano} [YR{ano}]'].values[0] 
        di[pais].append(valor)

di

plt.plot(anos,di['BRA'], color='red')
plt.plot(anos,di['NOR'], color='blue')
plt.plot(anos,di['NGA'], color='green')
plt.xticks(anos)
plt.title("% da população em situação de moderada ou grave insegurança alimentar")
plt.xlabel("Ano")
plt.ylabel("% da população")
plt.legend(['Brasil', 'Noruega', 'Nigeria'])
plt.show()

