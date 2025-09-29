## 17: Eliminar el Nodo del Medio de una Lista Enlazada  
Dada una lista enlazada (`list`), elimina el nodo del medio y devuelve la cabeza de la lista modificada. Si la lista tiene un solo nodo, devuelve una lista vacía.

**Ejemplos**

```python
# Ejemplo 1  
Entradas: head = [1, 3, 4, 7, 1, 2, 6]  
Salida esperada: [1, 3, 4, 1, 2, 6]  
# Explicación: El nodo del medio es 7 y se elimina.  

# Ejemplo 2  
Entradas: head = [1, 2, 3, 4]  
Salida esperada: [1, 2, 4]  
# Explicación: El nodo del medio es 3 y se elimina.  

# Ejemplo 3  
Entradas: head = [2, 1]  
Salida esperada: [2]  
# Explicación: El nodo del medio es 1 (segundo nodo) y se elimina.  

# Ejemplo 4  
Entradas: head = [1]  
Salida esperada: []  
# Explicación: La lista tiene un solo nodo, se elimina y queda vacía.  

# Ejemplo 5  
Entradas: head = [5, 10, 15, 20, 25, 30, 35, 40, 45]  
Salida esperada: [5, 10, 15, 20, 25, 30, 40, 45]  
# Explicación: El nodo del medio es 35 y se elimina.
```
