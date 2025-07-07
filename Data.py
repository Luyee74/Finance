import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    "Date": ["2024-01-01", "2024-01-02", "2024-01-03", "2024-01-04", "2024-01-05"],
    "AAPL": [150.0, 151.5, 150.8, 153.2, 155.0],
    "MSFT": [330.0, 332.0, 328.5, 334.0, 336.5],
    "GOOGL": [130.0, 131.2, 130.0, 132.0, 133.1],
}

df = pd.DataFrame(data)
df["Date"] = pd.to_datetime(df["Date"])
df.set_index("Date", inplace=True)

rendements = np.log(df / df.shift(1))
print("Rendements log :")
print(rendements)

moyenne = rendements.mean()
print("\nMoyenne des rendements :")
print(moyenne)

volatilite = rendements.std() * np.sqrt(252)
print("\nVolatilité annuelle :")
print(volatilite)

correlation = rendements.corr()
print("\nCorrélation entre actifs :")
print(correlation)

df.plot(title="Prix des actions")
plt.show()

rendements.plot(title="Rendements log")
plt.show()

sns.heatmap(correlation, annot=True, cmap="coolwarm")
plt.title("Corrélation entre les rendements")
plt.show()


