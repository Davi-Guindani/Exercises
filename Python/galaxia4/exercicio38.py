import pandas as pd

dicionario = {
    "cotacao": [10, 20, 30],
    "volume": [100, 200, 300],
    "data": pd.date_range("1/4/2000", periods=3)
}
df = pd.DataFrame(dicionario)
df = df.set_index("cotacao")
print(df)