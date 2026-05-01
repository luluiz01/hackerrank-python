import pandas as pd

dados = {
    "Mes": ["Jan", "Jan", "Fev", "Fev", "Mar", "Mar"],
    "Produto": ["A", "B", "A", "B", "A", "B"],
    "Vendas": [100, 150, 200, 120, 300, 180],
}

df = pd.DataFrame(dados)

print(df)

print("=" * 50)


media_por_mes = (
    df.groupby("Mes")["Vendas"].mean().reset_index()
)  # .reset_index() transforma em dataframe de novo

print("\n Média de vendas por produto")

print(media_por_mes)

print("=" * 50)

soma_por_mes = df.groupby("Mes")["Vendas"].sum().reset_index()

print("\n Soma de todas vendas")
print(soma_por_mes)
print("=" * 50)


print("\n Total de vendas por Produto")
total_por_produto = df.groupby("Produto")["Vendas"].sum().reset_index()

print(total_por_produto)
