from typing import get_args


class filme:
    def __init__(self, nome, ano, duracao):
        self.__nome = nome.title()
        self.__ano = ano
        self.__duracao = duracao
        self.__likes = 0
    
    def like(self):
        self.__likes += 1

    @property
    def nome(self):
        return self.__nome  
    
    @property
    def ano(self):
        return self.__ano

    @property
    def duracao(self):
        return self.__duracao
    
    @property
    def likes(self):
        return self.__likes
    
    @nome.setter 
    def nome(self, novo_nome):
        self.__nome = novo_nome.title() 
    



class serie: 
    def __init__(self, nome, ano, temporadas):
        self.__nome = nome.title()
        self.__ano = ano
        self.__temporadas = temporadas
        self.__likes = 0
        
    def like(self):
        self.__likes += 1
    
    @property
    def nome(self):
        return self.__nome  
    
    @property
    def ano(self):
        return self.__ano

    @property
    def temporadas(self):
        return self.__temporadas
    
    @property
    def likes(self):
        return self.__likes
    
    @nome.setter 
    def nome(self, novo_nome):
        self.__nome = novo_nome.title() 
    
    


vingadores = filme("Vingadores - guerra infinita", 2018, 160)
friends = serie("friends", 2009, 11)

vingadores.like()
vingadores.like()

friends.like()
friends.like()

vingadores.nome = 'lucas'

print(f"nome: {vingadores.nome} - ano: {vingadores.ano} - duração: {vingadores.duracao} - likes: {vingadores.likes}")
print(f"nome: {friends.nome} - ano: {friends.ano} - temporadas: {friends.temporadas} - likes: {friends.likes}")