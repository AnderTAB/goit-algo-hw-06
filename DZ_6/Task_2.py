from collections import deque

from bfs import bfs_recursive
from dfs import dfs_recursive
from Task_1 import DG

# Перетворимо граф в таблицю суміжності:
adjacency_list = {node: list(DG.neighbors(node)) for node in DG.nodes()}
graph = {str(node): [str(neighbor) for neighbor in neighbors] for node, neighbors in adjacency_list.items()}



print(f'\n\nЗастосування Пошуку у ширину(BFS):\n')
bfs_recursive(graph, deque(["Майдан"]))
print(f'\n\nЗастосування Пошуку у глибину(DFS):\n')
dfs_recursive(graph, "Майдан")


        