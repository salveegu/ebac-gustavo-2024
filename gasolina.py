import pandas as pd
import matplotlib.pyplot as plt

# Carregar os dados do arquivo CSV
df = pd.read_csv('gasolina.csv')

# Converter a coluna 'dia' para o tipo datetime
df['dia'] = pd.to_datetime(df['dia'])

# Ordenar o DataFrame pela coluna 'dia' (opcional)
df = df.sort_values(by='dia')

# Criar o gráfico de linha
plt.figure(figsize=(10, 6))
plt.plot(df['dia'], df['venda'], marker='o', color='b', linestyle='-')
plt.title('Preço da Gasolina ao Longo do Tempo')
plt.xlabel('Dia')
plt.ylabel('Preço (R$)')
plt.grid(True)

# Salvar o gráfico como gasolina.png
plt.savefig('gasolina.png')

# Exibir o gráfico
plt.show()
