## 13: Ciclo en una Lista Enlazada
Dada  una lista enlazada (`list`), determina si la lista contiene un ciclo. Una lista tiene un ciclo si algún nodo puede ser alcanzado nuevamente al seguir continuamente los punteros next.

**Ejemplos**

```python
# Ejemplo 1
Entradas: head = [3, 2, 0, -4], pos = 1
Salida esperada: true

# Ejemplo 2
Entradas: head = [1, 2], pos = 0
Salida esperada: true

# Ejemplo 3
Entradas: head = [1], pos = -1
Salida esperada: false

# Ejemplo 4
Entradas: head = [1, 2, 3, 4, 5], pos = -1
Salida esperada: false

# Ejemplo 5
Entradas: head = [1, 2], pos = -1
Salida esperada: false
```

**Nota**: `pos` representa el índice del nodo al que se conecta el último nodo para formar un ciclo. Si `pos` = -1, no hay ciclo.