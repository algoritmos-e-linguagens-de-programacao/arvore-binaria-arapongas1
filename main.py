from binary_tree import BinaryTree

x = BinaryTree()
x.adicionar(5)
x.adicionar(1)
x.adicionar(10)
x.adicionar(8)
x.adicionar(12)

# x.pre_ordem(x.retorna_raiz())
# x.em_ordem(x.retorna_raiz())
x.pos_ordem(x.retorna_raiz())