from typing import get_args

class programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self._ano = ano
        self._likes = 0
    
    def like(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome  
    
    @property
    def ano(self):
        return self._ano
    
    @property
    def likes(self):
        return self._likes
    
    @nome.setter 
    def nome(self, novo_nome):
        self.__nome = novo_nome.title() 

class filme(programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self._duracao = duracao
    
    @property
    def duracao(self):
        return self._duracao

class serie(programa): 
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self._temporadas = temporadas
        
    @property
    def temporadas(self):
        return self._temporadas


vingadores = filme("Vingadores - guerra infinita", 2018, 160)
friends = serie("friends", 2009, 11)

vingadores.like()
vingadores.like()

friends.like()
friends.like()

vingadores.nome = 'lucas'

print(f"nome: {vingadores.nome} - ano: {vingadores.ano} - duração: {vingadores.duracao} - likes: {vingadores.likes}")
print(f"nome: {friends.nome} - ano: {friends.ano} - temporadas: {friends.temporadas} - likes: {friends.likes}")