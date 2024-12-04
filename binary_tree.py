from node import Node

class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)  # A raiz da árvore

    # Método recursivo para construir a árvore balanceada
    def insert_balanced(self, nodes):
        """
        Insere nós de forma balanceada em uma árvore binária.
        :param nodes: Lista de valores a serem inseridos.
        """
        if not nodes:
            return None
        mid = len(nodes) // 2
        node = Node(nodes[mid])
        node.left = self.insert_balanced(nodes[:mid])
        node.right = self.insert_balanced(nodes[mid+1:])
        return node

    # Método para inicializar a árvore com valores
    def create_balanced_tree(self, n):
        # Gera uma lista com números de 1 a n
        values = list(range(1, n + 1))
        self.root = self.insert_balanced(values)
