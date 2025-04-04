import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier

X = np.array([
    [180, 7.5], [200, 8.0], [170, 7.0],
    [120, 6.0], [130, 6.5], [110, 5.5],
    [90, 4.5], [100, 5.0], [80, 4.0]
])

y = np.array([0, 0, 0, 1, 1, 1, 2, 2, 2])
frutas = ["Manzana", "Naranja", "Plátano"]
colores = ['red', 'orange', 'yellow']

knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X, y)

nueva_fruta = np.array([[165, 6.8]])
prediccion = knn.predict(nueva_fruta)

x_min, x_max = X[:, 0].min() - 20, X[:, 0].max() + 20
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.linspace(x_min, x_max, 200), np.linspace(y_min, y_max, 200))
Z = knn.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

plt.figure(figsize=(8, 6))

plt.contourf(xx, yy, Z, alpha=0.3, colors=colores)

for i in range(3):
    plt.scatter(X[y == i][:, 0], X[y == i][:, 1], label=frutas[i], color=colores[i], edgecolors='black', s=100)

plt.scatter(nueva_fruta[0][0], nueva_fruta[0][1], label="Nueva fruta", color='black', marker='P', s=100, edgecolors='black')

plt.xlabel("Peso (g)", fontsize=12)
plt.ylabel("Diámetro (cm)", fontsize=12)
plt.title("Clasificación de Frutas con KNN", fontsize=14, fontweight='bold')
plt.legend(fontsize=10)

print(f"La fruta clasificada es: {frutas[prediccion[0]]}")

plt.show()
