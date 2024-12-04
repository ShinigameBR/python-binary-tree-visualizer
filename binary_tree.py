from node import Node

class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)  # A raiz da árvore

    # Método para adicionar um nó à árvore
    def insert_left(self, parent, value):
        parent.left = Node(value)

    def insert_right(self, parent, value):
        parent.right = Node(value)

    # Método de travessia para gerar a visualização
    def traverse(self, node):
        if node:
            print(node.value)
            self.traverse(node.left)
            self.traverse(node.right)
