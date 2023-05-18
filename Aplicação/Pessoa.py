class Pessoa:                   #classe define o tipo de objeto
    nome = "Pedro"              #Atributos são as caracteristicas
    idade = 26                  #Métodos são as funções que esse objeto poderá executar
    email = "pedro.simbera@fatec.sp.gov.br"

    def exibir(self):
        print(self.nome)
    
    def email(self):
        print(self.email)

# Em Python, o parâmetro self é uma convenção usada para referenciar o próprio objeto dentro dos métodos de uma classe. 

# Por padrão quando se tem um método, ou você simplesmente o chama executando algo e sem receber valores, 
# ou você usa valores padrões daquela classe.

# Assim ou o def "xxx" (self):
#               print (self....."terá seu próprio valor aqui, sem parâmetros ou valores externos")
#
# Ou terá parâmetros def "ssss" (self, a, b, c):
#               print (a, b, c)
# Que irão vir com argumentos ao serem chamados.





# class Pessoa:
#     def __init__(self, nome, idade):
#         self.nome = nome
#         self.idade = idade

#     def apresentar(self):
#         print(f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos.")

# p1 = Pessoa("João", 25)
# p1.apresentar()  # Saída: Olá, meu nome é João e eu tenho 25 anos.