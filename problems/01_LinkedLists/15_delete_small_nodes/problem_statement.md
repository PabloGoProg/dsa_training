## 15: Eliminar Nodos Menores de una Lista Enlazada  
Dada una lista enlazada (`list`), elimina cada nodo que tenga un nodo con un valor mayor en cualquier lugar a su derecha. Devuelve la cabeza de la lista enlazada modificada.

**Ejemplos**

```python
# Ejemplo 1  
Entradas: head = [5, 2, 13, 3, 8]  
Salida esperada: [13, 8]  
Explicación: Los nodos que deben eliminarse son 5, 2 y 3.  
# - El nodo 13 está a la derecha del nodo 5.  
# - El nodo 13 está a la derecha del nodo 2.  
# - El nodo 8 está a la derecha del nodo 3.  

# Ejemplo 2  
Entradas: head = [1, 1, 1, 1]  
Salida esperada: [1, 1, 1, 1]  
# Explicación: Cada nodo tiene el valor 1, por lo que no se eliminan nodos.  

# Ejemplo 3  
Entradas: head = [10, 5, 12, 3, 20]  
Salida esperada: [20]  
# Explicación: Los nodos que deben eliminarse son 10, 5, 12 y 3.  
# - El nodo 20 está a la derecha de todos los nodos anteriores.  

# Ejemplo 4  
Entradas: head = [7, 6, 5, 4, 3, 2, 1]  
Salida esperada: [7, 6, 5, 4, 3, 2, 1]  
# Explicación: No hay nodos con valores mayores a la derecha de ningún nodo.  

# Ejemplo 5  
Entradas: head = [1, 2, 3, 4, 5]  
Salida esperada: [5]  
# Explicación: El nodo 5 está a la derecha de todos los nodos anteriores.
```
