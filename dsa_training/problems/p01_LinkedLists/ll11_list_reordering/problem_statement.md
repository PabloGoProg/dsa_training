## 11: Reordenar una Lista Enlazada
Dada una lista enlazada (`list`), reordena la lista en el siguiente patrón:

$$L_{0} → L_{n} → L_{1} → L_{n-1} → L_{2} → L_{n-2} → …$$

No se permite modificar los valores de los nodos, solo se pueden cambiar los enlaces entre ellos.

**Ejemplos**

```python
# Ejemplo 1
Entradas: head = [1, 2, 3, 4]
Salida esperada: [1, 4, 2, 3]

# Ejemplo 2
Entradas: head = [1, 2, 3, 4, 5]
Salida esperada: [1, 5, 2, 4, 3]

# Ejemplo 3
Entradas: head = [1]
Salida esperada: [1]

# Ejemplo 4
Entradas: head = [1, 2]
Salida esperada: [1, 2]

# Ejemplo 5
Entradas: head = [10, 20, 30, 40, 50, 60]
Salida esperada: [10, 60, 20, 50, 30, 40]
```
