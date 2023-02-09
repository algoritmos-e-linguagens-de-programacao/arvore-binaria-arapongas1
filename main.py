from binary_tree import BinaryTree

x = BinaryTree()
x.adicionar(5)
x.adicionar(3)
x.adicionar(1)
x.adicionar(10)
x.adicionar(8)
x.adicionar(6)
x.adicionar(9)
x.adicionar(7)


# x.pre_ordem(x.retorna_raiz())
# x.em_ordem(x.retorna_raiz())
# x.pos_ordem(x.retorna_raiz())

x.remover(10)

x.pos_ordem(x.retorna_raiz())

