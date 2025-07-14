import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 🔹 1. Création de données de prix fictives (5 jours pour 3 actions)
dates = pd.date_range(start="2024-01-01", periods=5, freq='D')

data = {
    "AAPL": [150, 152, 153, 155, 154],
    "MSFT": [300, 305, 307, 308, 310],
    "GOOGL": [100, 101, 100.5, 102, 103],
}

df = pd.DataFrame(data, index=dates)

# 🔹 2. Affichage des prix
print("📈 Prix des actions :")
print(df)

# 🔹 3. Calcul des rendements logarithmiques journaliers
returns = np.log(df / df.shift(1))

print("\n📊 Rendements log :")
print(returns)

# 🔹 4. Statistiques
mean_returns = returns.mean()
volatility = returns.std() * np.sqrt(252)  # annualisée
correlation = returns.corr()

# 🔹 5. Affichage des stats
print("\n📈 Moyennes des rendements :")
print(mean_returns)

print("\n📉 Volatilité annualisée :")
print(volatility)

print("\n🔗 Corrélation entre les actions :")
print(correlation)

# 🔹 6. Visualisations
plt.figure(figsize=(10, 4))
df.plot(title="Prix des actions")
plt.xlabel("Date")
plt.ylabel("Prix")
plt.grid(True)
plt.show()

returns.plot(title="Rendements log")
plt.xlabel("Date")
plt.grid(True)
plt.show()

plt.figure(figsize=(6, 4))
sns.heatmap(correlation, annot=True, cmap="coolwarm")
plt.title("Corrélation des rendements")
plt.show()


print("\n📊 Visualisations terminées.")