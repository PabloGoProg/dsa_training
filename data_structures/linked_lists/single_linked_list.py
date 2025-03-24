class Node:
  
  def __init__(self, data):
    self.data = data
    self.next = None
    
  def __repr__(self):
    return f"Node({self.data})"

class SingleLinkedList:
  '''
    Single Linked List class
    
    Attributes:
      head: Node
        The first node in the linked list
      tail: Node
        The last node in the linked list
  '''
  def __init__(self):
    self.head = None
    self.tail = None
    
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
      Crea un nuevo nodo con el valor `value`
    '''
    return Node(value)
    
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
    return " -> ".join(nodes)