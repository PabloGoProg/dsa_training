from .linked_lists.doubly_circular_linked_list import DoublyCircularLinkedList

dcll = DoublyCircularLinkedList([1, 2, 3, 4, 5])
print(dcll)
print(len(dcll))

dcll.append(6)
print(dcll)
print(len(dcll))

head = dcll.head
tail = dcll.tail

prev_head = head.prev
next_tail = tail.next

print(prev_head.value)
print(next_tail.value)

curr = dcll.head
values = [curr.value]

while curr != dcll.tail:
  values.append(curr.next.value)
  curr = curr.next

print(values)

curr = dcll.tail
values = [curr.value]

while curr != dcll.head:
  values.append(curr.prev.value)
  curr = curr.prev

print(values)
