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

  def remover(self, valor):
    if self.root == None:
      return print("Árvore vázia")

    aux = self.root
    raiz_ant = self.root
    while aux.value != valor:
      raiz_ant = aux
      if valor < aux.value:
        aux = aux.esquerda
        esq = True
      else:
        aux = aux.direita
        esq = False
      if aux == None:
        return False

    # Se for um nó terminal
    if aux.esquerda == None and aux.direita == None:
      if aux == self.root:
        self.root = None
      elif esq == True:
        raiz_ant.setEsquerda(None)
      else:
        raiz_ant.setDireita(None)

    # Se não tiver nó a direita
    elif aux.direita == None:
      if aux == self.root:
        self.root = self.root.esquerda
      elif esq == True:
        raiz_ant.setEsquerda(aux.esquerda)
      else:
        raiz_ant.setDireita(aux.esquerda)

    # Se não tiver nó a esquerda
    elif aux.esquerda == None:
      if aux == self.root:
        self.root = self.root.direita
      elif esq == True:
        raiz_ant.setEsquerda(aux.direita)
      else:
        raiz_ant.setDireita(aux.direita)
    
    # Se tiver 2 nós
    else:
      no_remov = aux
      aux = aux.esquerda
      while aux.direita != None:
        aux = aux.direita
      self.remover(aux.value)
      no_remov = aux.value
      
    return True