"""
3. Utilize Pyarrow para converter um CSV grande para Parquet"""

import pyarrow as pa
import pyarrow.parquet as pq
import pandas as pd

df = pd.read_csv("gross-domestic-product-december-2025-quarter.csv")
df.to_parquet("gross-domestic-product-december-2025-quarte.parquet")
