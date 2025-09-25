"""Definiciones de nodos para listas enlazadas.

Incluye:
- `Node`: nodo para lista simplemente enlazada con referencia a `next`.
- `DoublyNode`: nodo para lista doblemente enlazada con referencias a `prev` y `next`.
"""

class Node:
  """
  Nodo de una lista simplemente enlazada.

  Atributos:
  - value: valor almacenado en el nodo.
  - next: referencia al siguiente nodo de la lista (o `None`).
  """
  
  def __init__(self, value):
    """
    Inicializa un nodo con un valor y `next=None`.

    Args:
      value: Cualquier valor que se quiera almacenar en el nodo.
    """
    self.value = value
    self.next = None
    
  def __repr__(self):
    """Representación legible del nodo, mostrando su valor y el siguiente nodo."""
    return f"Node({self.value}) \nNext: {self.next}"
  

class DoublyNode:
  """
  Nodo de una lista doblemente enlazada.

  Atributos:
  - value: valor almacenado en el nodo.
  - next: referencia al siguiente nodo (o `None`).
  - prev: referencia al nodo anterior (o `None`).
  """
  
  def __init__(self, value):
    """
    Inicializa un nodo doble con un valor, `next=None` y `prev=None`.

    Args:
      value: Cualquier valor que se quiera almacenar en el nodo.
    """
    self.value = value
    self.next = None
    self.prev = None
    
  def __repr__(self):
    """Representación legible del nodo doble, mostrando valor, siguiente y anterior."""
    return f"Node({self.value}) \nNext: {self.next} \nPrev: {self.prev}"