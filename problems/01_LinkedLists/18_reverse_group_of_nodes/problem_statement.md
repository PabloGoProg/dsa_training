## 18: Invertir Nodos en Grupos de k en una Lista Enlazada  
Dada una lista enlazada (`list`), invierte los nodos de la lista `k` a la vez y devuelve la lista modificada. Si el número de nodos no es múltiplo de `k`, los nodos que queden al final deben permanecer en el mismo orden.

**Ejemplos**

```python
# Ejemplo 1  
Entradas: head = [1, 2, 3, 4, 5], k = 2  
Salida esperada: [2, 1, 4, 3, 5]  
# Explicación: Los nodos se invierten de 2 en 2. El último nodo queda igual.  

# Ejemplo 2  
Entradas: head = [1, 2, 3, 4, 5], k = 3  
Salida esperada: [3, 2, 1, 4, 5]  
# Explicación: Se invierten los tres primeros nodos. Los dos restantes quedan igual.  

# Ejemplo 3  
Entradas: head = [1, 2, 3, 4, 5, 6], k = 3  
Salida esperada: [3, 2, 1, 6, 5, 4]  
# Explicación: Dos grupos completos de 3 nodos se invierten.  

# Ejemplo 4  
Entradas: head = [1, 2, 3, 4], k = 4  
Salida esperada: [4, 3, 2, 1]  
# Explicación: Un único grupo de 4 nodos es invertido completamente.  

# Ejemplo 5  
Entradas: head = [1, 2, 3], k = 1  
Salida esperada: [1, 2, 3]  
# Explicación: Como k = 1, no se hacen cambios en la lista.
```
