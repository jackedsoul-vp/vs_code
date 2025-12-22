import pandas as pd

df = pd.DataFrame({
    "name": ["A", "B", "C"],
    "salary": [50000, 60000, 70000]
})

print(df)
print("Average salary:", df["salary"].mean())
