# Clasificador de Frutas con KNN

Este proyecto clasifica frutas en base a su peso (g) y diámetro (cm). La clasificación se visualiza devolviendo el nombre de la fruta correspondiente, acompañado de un gráfico 2D.

# ¿Cómo funciona?

El código utiliza el algoritmo de clasificación KNN, que basa sus predicciones en la cercanía a otros puntos conocidos.

En este caso, contamos con datos de 3 tipos de frutas (Manzana, Naranja y Banana), y el modelo toma los 3 puntos más cercanos (k = 3) para decidir la clase de una fruta nueva.

Puedes cambiar el valor de `k` fácilmente si deseas ajustar la sensibilidad de la clasificación.

# ¿Cómo usarlo?
 
1. Clona el repositorio
2. Instala las dependencias ejecutando el siguiente comando en la terminal "pip install -r requirements.txt"
3. Define la fruta que quieres clasificar indicando su peso y diámetro en "nueva_fruta"
4. Corre el script y en la terminal se verá la fruta correspondiente seguido de un grafico indicando con mas detalle la comparación

# Librerias utilizadas

-numpy (operaciones numéricas)
-matplotlib (generacion de graficos)
-sklearn.neighbors (Algoritmo KNN de scikit-learn)