'''
  Para la solución de este problema debes implementar la función `combine_sorted_lists`
  acorde a las instrucciones y requerimiento del enunciado encontrado en `problem_statement.md`.
  
  Para la solución puedes usar todas las funcionalidades implementadas dentro de clase `SingleLinkedList`, la cual puedes encontrar en el archivo single_linked_list.py `data_strcutures/linked_lists/single_linked_list.py` en caso de que necesites modificar su comportamiento o agregar funcionalidades adicionales.
'''

from data_structures import SingleLinkedList

def combine_sorted_lists(list1: SingleLinkedList, list2: SingleLinkedList) -> SingleLinkedList:
  '''
    Realiza tu implementación en esta función
  '''
  result = SingleLinkedList()
  current1 = list1.head
  current2 = list2.head

  while current1 is not None and current2 is not None:
    if current1.value <= current2.value:
      result.append(current1.value)
      current1 = current1.next
    else:
      result.append(current2.value)
      current2 = current2.next

  while current1 is not None:
    result.append(current1.value)
    current1 = current1.next

  while current2 is not None:
    result.append(current2.value)
    current2 = current2.next

  return result
