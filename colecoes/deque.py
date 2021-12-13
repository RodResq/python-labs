"""

Modulo Collections -> Deque

Lista de alta performace

"""

from collections import deque

# criando deque
deq = deque('geek')
print(deq)

deq.append('y') # Adiciona no final
print(deq)

deq.appendleft('K') # Adiciona no comeco
print(deq)

print(deq.pop())
print(deq)

print(deq.popleft())
print(deq)
