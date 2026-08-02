# # ✅ Хэш-таблица (Hash Table)
# # Пример: dict в Python
# hash_table = {"name": "Мурад", "age": 25}
# print(hash_table["name"])  # O(1) доступ к элементу


# # ✅ Стэк (Stack)
# # Пример: LIFO — последний пришёл, первый ушёл
# stack = []
# stack.append(1)
# stack.append(2)
# print(stack.pop())  # 2
# print(stack.pop())  # 1


# # ✅ Очередь (Queue)
# # Пример: FIFO — первый пришёл, первый ушёл
# from collections import deque

# queue = deque()
# queue.append(1)
# queue.append(2)
# print(queue.popleft())  # 1
# print(queue.popleft())  # 2


# # ✅ Связанный список (Linked List)
# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None


# node1 = Node(1)
# node2 = Node(2)
# node1.next = node2
# print(node1.value, node1.next.value)  # 1 2


# # ✅ Граф (Graph) — список смежности
# graph = {"A": ["B", "C"], "B": ["D"], "C": ["D"], "D": []}


# # ✅ Куча (Heap)
# import heapq

# heap = []
# heapq.heappush(heap, 3)
# heapq.heappush(heap, 1)
# heapq.heappush(heap, 2)
# print(heapq.heappop(heap))  # 1 (минимум всегда сверху)


# # ✅ Битовые поля (Bit Arrays)
# permissions = 0b1011  # права: чтение, запись, удаление (например)
# print(bool(permissions & 0b0001))  # есть ли право на удаление?


# # ✅ Массивы (Arrays)
# arr = [10, 20, 30]
# print(arr[1])  # доступ по индексу: O(1)


# # ✅ Двоичное дерево
# class TreeNode:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None


# root = TreeNode(4)
# root.left = TreeNode(2)
# root.right = TreeNode(5)


# # ✅ Дерево двоичного поиска (BST)
# def insert_bst(root, value):
#     if root is None:
#         return TreeNode(value)
#     if value < root.value:
#         root.left = insert_bst(root.left, value)
#     else:
#         root.right = insert_bst(root.right, value)
#     return root


# bst = insert_bst(None, 10)
# insert_bst(bst, 5)
# insert_bst(bst, 15)


# # ✅ B-дерево — схема (без кода)
# # Используется в базах данных и файловых системах.
# # Каждый узел может содержать несколько ключей и детей.
# # Пример: B+ Tree в MySQL — быстрое чтение с диска, уменьшение глубины дерева.


# # ✅ R-дерево — используется в гео-пространственных индексах
# # Сохраняет объекты с границами (bounding boxes) и строит иерархию областей
# # Пример — поиск всех объектов в радиусе на карте


# # ✅ АВЛ-дерево (AVL Tree) — самобалансирующееся BST
# # Разница высот между поддеревьями максимум 1
# # Балансировка при вставке/удалении


# # ✅ LSM-дерево (Log Structured Merge Tree)
# # Используется в современных БД (Cassandra, RocksDB)
# # Все данные сначала записываются в память (memtable), а затем сбрасываются на диск пачками (SSTables)
# # Хорошо для частых вставок, медленное чтение компенсируется кешами
