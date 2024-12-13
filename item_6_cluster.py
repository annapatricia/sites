# -*- coding: utf-8 -*-
"""item_6_cluster.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1PHf9_BiOhQjEiprPRTy65DwiilKXxT2J

Importação de Bibliotecas e Simulação de Dados
"""

import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

# Simulação de dados de setores
np.random.seed(42)
num_setores = 100
dados = {
    "renda_media": np.random.uniform(1000, 8000, num_setores),
    "taxa_desemprego": np.random.uniform(5, 20, num_setores),
    "nivel_educacional": np.random.uniform(0, 1, num_setores),  # 0 a 1 (proporção de nível superior)
    "iluminacao": np.random.choice([0, 1], num_setores, p=[0.3, 0.7]),  # 1: boa iluminação
    "frequencia_crimes": np.random.randint(50, 500, num_setores),  # Número de crimes registrados
    "tipo_crime_mais_comum": np.random.choice(["roubo", "furto", "violência"], num_setores)
}

df = pd.DataFrame(dados)
print(df.head())

"""#Clustering do setores K-means"""

from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns

# Pré-processamento
scaler = StandardScaler()
variaveis = ["renda_media", "taxa_desemprego", "nivel_educacional", "frequencia_crimes"]
X = scaler.fit_transform(df[variaveis])

# Aplicando K-Means
kmeans = KMeans(n_clusters=4, random_state=42)
df["cluster"] = kmeans.fit_predict(X)

# Visualização dos clusters
sns.scatterplot(x=df["renda_media"], y=df["frequencia_crimes"], hue=df["cluster"], palette="viridis")
plt.title("Clusters de Setores")
plt.xlabel("Renda Média")
plt.ylabel("Frequência de Crimes")
plt.show()

"""#Prediçao de Taticas de policiamento"""

# Criando uma variável alvo para táticas (simulação)
df["taticas"] = np.where(df["frequencia_crimes"] > 300, "aumentar_patrulhamento",
                         np.where(df["iluminacao"] == 0, "melhorar_iluminacao", "programas_sociais"))

# Separação em treino e teste
from sklearn.model_selection import train_test_split

X = df[["renda_media", "taxa_desemprego", "nivel_educacional", "frequencia_crimes", "iluminacao"]]
y = df["taticas"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Modelo de Random Forest
modelo = RandomForestClassifier(random_state=42)
modelo.fit(X_train, y_train)

# Avaliação do modelo
y_pred = modelo.predict(X_test)
print("Relatório de Classificação:")
print(classification_report(y_test, y_pred))

# Importância das variáveis
importances = modelo.feature_importances_
for feature, importance in zip(X.columns, importances):
    print(f"{feature}: {importance:.2f}")

"""Gerando recomendaçoes"""

# Aplicando o modelo a novos dados
df["recomendacao"] = modelo.predict(X)

print("Exemplo de Recomendações por Setor:")
print(df[["renda_media", "frequencia_crimes", "recomendacao"]].head(10))