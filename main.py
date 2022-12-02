from BST import Tree
 
arv = Tree()
 
arv.inserir(10)
arv.inserir(8)
arv.inserir(17)
arv.inserir(13)
arv.inserir(21)
arv.inserir(6)
arv.inserir(19)
arv.inserir(25)
print("Os nós folhas presentes na BST são: ")
arv.quantidade_folhas()
print()
print("Todos os nós e seus respectivos graus: ")
arv.apresentar_graus()
