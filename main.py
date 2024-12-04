from binary_tree import BinaryTree
from plot_tree import plot_tree

# Criando a árvore binária
bt = BinaryTree(1)
bt.insert_left(bt.root, 2)
bt.insert_right(bt.root, 3)
bt.insert_left(bt.root.left, 4)
bt.insert_right(bt.root.left, 5)
bt.insert_left(bt.root.right, 6)
bt.insert_right(bt.root.right, 7)

# Visualizando a árvore binária
plot_tree(bt.root)
