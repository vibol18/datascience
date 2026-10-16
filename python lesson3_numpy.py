import pandas as pd

data = {
    "name": ["Dara", "Sokha", "Vibol", "Dalin", "Malis"],
    "age": [18, 19, 20, 18, 21],
    "score": [60, 75, 90, 85, 95]
}

df = pd.DataFrame(data)

print(df)