from Pessoa import Pessoa
pessoa = Pessoa()
pessoa.exibir()      #utilizando um método irá executar o conteúdo dele definido no objeto
print(pessoa.idade)  #forma de exibir o conteúdo do objeto

# Com parâmetros abertos ao externo para que entre como argumento

from Animal import Animal
cachorro = Animal()
cachorro.cadastro(nome="Bebel", idade=9, raca="mestiça")

#Na class:
# class Animal:
#     nome = ""
#     idade = 0
#     raca = ""

#     def cadastro(self, nome, idade, raca):
#         print(nome)
#         print(idade)
#         print(raca)

# Abriu para receber argumentos que entrou junto ao chamamento 