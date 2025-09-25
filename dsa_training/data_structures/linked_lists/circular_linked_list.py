from .nodes import Node

class CircularLinkedList:
  def __init__(self, initial_values=None):
    self.head = None
    self.tail = None
    
    if initial_values:
      self.from_list(initial_values)

  # ------------------------------
  # Puedes desarrollar la lógica de los métodos de la lista enlazada aquí

  def append(self, value):
    '''
      Esto es solo un ejemplo de como se deben implementar los métodos de la lista enlazada circular
      Puedes modificarlo o eliminarlo si lo deseas
    '''
    new_node = Node(value)

    if not self.head:
      self.head = new_node
      self.tail = new_node
      self.tail.next = self.head
    else:
      prev_tail = self.tail
      self.tail = new_node
      prev_tail.next = self.tail
      self.tail.next = self.head
      self.head.prev = self.tail

  # ------------------------------
      
  def from_list(self, values: list):
    '''
      IMPORTANTE: NO MODIFICAR ESTE MÉTODO
    
      Crea una lista enlazada circular a partir de una lista de valores
    '''
    for value in values:
      new_node = Node(value)

      if not self.head:
        self.head = new_node
        self.tail = new_node
        self.tail.next = self.head
      else:
        prev_tail = self.tail
        self.tail = new_node
        prev_tail.next = self.tail
        self.tail.next = self.head
        self.head.prev = self.tail

  def __len__(self):
    '''
      IMPORTANTE: NO MODIFICAR ESTE MÉTODO
    
      Devuelve el tamaño de la lista enlazada circular
    '''
    if not self.head:
      return 0
    
    length = 1
    current = self.head
    current = current.next

    while current != self.head:
      current = current.next
      length += 1
    return length
  
  def __repr__(self):
    '''
      IMPORTANTE: NO MODIFICAR ESTE MÉTODO
    
      Devuelve una representación en cadena de la lista enlazada circular
    '''
    current = self.head
    values = [str(current.value)  ]
    current = current.next

    while current != self.head:
      values.append(str(current.value))
      current = current.next
    return f'[{", ".join(values)}]'
  
  def __str__(self):
    '''
      IMPORTANTE: NO MODIFICAR ESTE MÉTODO
    
      Devuelve una representación en cadena de la lista enlazada circular
    '''
    return self.__repr__()