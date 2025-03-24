class Node:
  
  def __init__(self, value):
    self.value = value
    self.next = None
    
  def __repr__(self):
    return f"{self.value}"

class SingleLinkedList:
  '''
    Single Linked List class
    
    Attributes:
      head: Node
        The first node in the linked list
      tail: Node
        The last node in the linked list
  '''
  def __init__(self, initial_values=None):
    self.head = None
    self.tail = None
    
    if initial_values:
      self.from_list(initial_values)
    
  # ------------------------------
  # Puedes desarrollar la lógica de los métodos de la lista enlazada aquí
  
  def append(self, value):
    '''
      Esto es solo un ejemplo de como se deben implementar los métodos de la lista enlazada
      Puedes modificarlo o eliminarlo si lo deseas
    '''
    new_node = Node(value)
    if not self.head:
      self.head = new_node
    else:
      self.tail.next = new_node
    self.tail = new_node
  
  # ------------------------------  
  
  def create_node(self, value):
    '''
      IMPORTANTE: NO MODIFICAR ESTE MÉTODO
    
      Crea un nuevo nodo con el valor `value`
    '''
    return Node(value)
  
  def from_list(self, values: list):
    '''
      IMPORTANTE: NO MODIFICAR ESTE MÉTODO
    
      Crea una lista enlazada a partir de una lista de valores
    '''
    for value in values:
      new_node = self.create_node(value)
      if not self.head:
        self.head = new_node
        self.tail = new_node
      else:
        self.tail.next = new_node
        self.tail = new_node
    
  def __sizeof__(self):
    '''
      IMPORTANTE: NO MODIFICAR ESTE MÉTODO
    
      Devuelve el tamaño de la lista enlazada
      Funciona con la función len()
    '''
    len = 0
    current = self.head
    while current:
      len += 1
      current = current.next
    return len    
  
  def __repr__(self):
    '''
      IMPORTANTE: NO MODIFICAR ESTE MÉTODO
    
      Devuelve una representación de la lista enlazada en forma de string
      Funciona con la función print()
    '''
    nodes = []
    current = self.head
    while current:
      nodes.append(str(current))
      current = current.next
    return f'[{", ".join(nodes)}]'
  
  def __str__(self):
    '''
      IMPORTANTE: NO MODIFICAR ESTE MÉTODO
    
      Devuelve una representación de la lista enlazada en forma de string
      Funciona con la función str()
    '''
    return self.__repr__()
  