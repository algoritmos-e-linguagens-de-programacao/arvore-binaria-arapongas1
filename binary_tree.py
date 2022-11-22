from node import Node


class BinaryTree:

  def __init__(self):
    self.root = None

  def adicionar(self, value):
    node = Node(value)
    if self.root == None:
      self.root = node
    else:
      aux = self.root
      while True:
        raizAnterior = aux
        if value < aux.value:
          aux = aux.esquerda
          if aux == None:
            raizAnterior.setEsquerda(node)
            break
        elif value > aux.value:
          aux = aux.direita
          if aux == None:
            raizAnterior.setDireita(node)
            break

  def retorna_raiz(self):
    return self.root

  def pre_ordem(self, aux):
    if aux != None:
      print(f"{str(aux.value)}")
      self.pre_ordem(aux.esquerda)
      self.pre_ordem(aux.direita)

  def em_ordem(self, aux):
    if aux != None:
      self.em_ordem(aux.esquerda)
      print(f"{str(aux.value)}")
      self.em_ordem(aux.direita)

  def pos_ordem(self, aux):
    if aux != None:
      self.pos_ordem(aux.esquerda)
      self.pos_ordem(aux.direita)
      print(f"{str(aux.value)}")
