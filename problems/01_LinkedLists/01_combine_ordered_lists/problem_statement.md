## 01: Combinar Dos Listas Ordenadas Ascendentemente

Dadas dos listas enlazadas ordenadas (`list1` y `list2`) en orden ascendente, fusionarlas en una única lista enlazada ordenada. La lista resultante debe construirse enlazando los nodos de las listas de entrada sin modificar los valores. La función debe devolver la cabeza de la lista fusionada.

**Ejemplos**

```python
# Ejemplo 1  
Entradas: list1 = [1, 2, 4], list2 = [1, 3, 4]  
Salida esperada: [1, 1, 2, 3, 4, 4]  

# Ejemplo 2  
Entradas: list1 = [], list2 = []  
Salida esperada: []  

# Ejemplo 3  
Entradas: list1 = [], list2 = [0]  
Salida esperada: [0]  

# Ejemplo 4  
Entradas: list1 = [5, 10, 15], list2 = [2, 3, 20]  
Salida esperada: [2, 3, 5, 10, 15, 20]  

# Ejemplo 5  
Entradas: list1 = [1, 1, 1], list2 = [1, 1, 1]  
Salida esperada: [1, 1, 1, 1, 1, 1]
```
