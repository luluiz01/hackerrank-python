import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

print(8*8)

# Lê o CSV
df = pd.read_csv("Data8277.csv")

# Converte para uma tabela PyArrow
tabela = pa.Table.from_pandas(df)

# Salva como Parquet
pq.write_table(tabela, "arquivo_convertido.parquet")

print("Conversão concluída!")