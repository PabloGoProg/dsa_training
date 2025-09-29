## 16: Combinar Nodos Entre Ceros en una Lista Enlazada  
Dada una lista enlazada (`list`) en la que los valores siempre empiezan y terminan con 0, y entre cada par de ceros hay una secuencia de números positivos, combina los valores entre cada par de ceros en un solo nodo que contenga la suma de esos valores. Devuelve la lista resultante sin los ceros.

**Ejemplos**

```python
# Ejemplo 1  
Entradas: head = [0, 3, 1, 0, 4, 5, 2, 0]  
Salida esperada: [4, 11]  
# Explicación: Se suman 3 + 1 = 4, y 4 + 5 + 2 = 11.  

# Ejemplo 2  
Entradas: head = [0, 1, 0, 3, 0, 2, 2, 0]  
Salida esperada: [1, 3, 4]  
# Explicación: Las sumas son 1, 3, y 2 + 2 = 4.  

# Ejemplo 3  
Entradas: head = [0, 5, 0]  
Salida esperada: [5]  
# Explicación: Solo hay una suma entre ceros.  

# Ejemplo 4  
Entradas: head = [0, 10, 20, 30, 0, 40, 0]  
Salida esperada: [60, 40]  
# Explicación: Se suman 10 + 20 + 30 = 60, y luego 40.  

# Ejemplo 5  
Entradas: head = [0, 7, 8, 0, 1, 2, 3, 0]  
Salida esperada: [15, 6]  
# Explicación: Se suman 7 + 8 = 15, y 1 + 2 + 3 = 6.
```
