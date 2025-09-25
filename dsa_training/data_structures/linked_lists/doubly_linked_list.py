from .nodes import DoublyNode as Node
  
class DoublyLinkedList:
  '''
    Doubly Linked List class
    
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
      self.tail = new_node
    else:
      prev_tail = self.tail
      self.tail = new_node
      prev_tail.next = self.tail
      self.tail.prev = prev_tail

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
        prev_tail = self.tail
        self.tail = new_node
        prev_tail.next = self.tail
        self.tail.prev = prev_tail
      
  def __sizeof__(self):
    '''
      IMPORTANTE: NO MODIFICAR ESTE MÉTODO
    
      Devuelve el tamaño de la lista enlazada
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
    
      Devuelve una representación en cadena de la lista enlazada
    '''
    values = []
    current = self.head
    while current:
      values.append(current.value)
      current = current.next
    return str(values)
  
  def __str__(self):
    '''
      IMPORTANTE: NO MODIFICAR ESTE MÉTODO
    
      Devuelve una representación en cadena de la lista enlazada
    '''
    return self.__repr__()