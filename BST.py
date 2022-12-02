class No:
     
     def __init__(self, key, dir, esq):
          self.item = key
          self.dir = dir
          self.esq = esq
 
class Tree:
 
    def __init__(self):
        self.root = No(None,None,None)
        self.root = None
 
    def inserir(self, v):
        novo = No(v,None,None)
        if self.root == None:
            self.root = novo
        else:
            atual = self.root
            while True:
                anterior = atual
                if v <= atual.item:
                    atual = atual.esq
                    if atual == None:
                        anterior.esq = novo
                        return
                else:
                    atual = atual.dir
                    if atual == None:
                        anterior.dir = novo
                        return
   	
    def folhas(self, atual):
        if atual == None:
            return 0
        if atual.esq == None and atual.dir == None:
            print(atual.item)
            return 1
        return self.folhas(atual.esq) + self.folhas(atual.dir)
 
    def quantidade_folhas(self):
        if(self.root != None):
            print("Quantidade de folhas é igual a %d"  %(self.folhas(self.root)))

    #Essa função ficou responsavel pela contagem de quantos e quais são os graus existentes na BST
    def graus(self,atual):
        if atual:
            grau = 0
        if atual.esq and atual.dir:
            grau += 2
        elif atual.esq and not atual.dir or not atual.esq and atual.dir:
            grau += 1
        print("Nó:", atual.item, end = " , ")
        print("Grau:", grau)
        if atual.esq:
            self.graus(atual.esq)
        if atual.dir:
            self.graus(atual.dir)
   
    #Essa funçao surge a partir do mesmo raciocinio logico da funçao quantidade_folhas()
    #Ela existe apenas para passar os argumentos para a função graus para que ela funcione de forma correta
    #Como essa função nao recebe argumentos, é ela que será chamada no arquivo main.py
    def apresentar_graus(self):
        if(self.root != None):
            self.graus(self.root)
