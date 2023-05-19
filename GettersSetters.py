# Método construtor:
# O método construtor é um método especial em uma classe que é executado automaticamente quando um objeto é criado a partir dessa classe. Em Python, o método construtor é chamado __init__(). Ele é usado para inicializar os atributos do objeto com valores específicos. O método construtor é opcional, mas é comumente utilizado para garantir que os objetos tenham um estado inicial consistente. Você pode definir parâmetros no método construtor para receber os valores iniciais dos atributos. 

# Estrutura padrão do método construtor

# class Pessoa: 

#     def __init__(self, nome, idade):
#         self.nome = nome
#         self.idade = idade
#         print(self.nome, self.idade)
        
# fulado = Pessoa("Tete", 23)

# Getters:
# Os getters são métodos usados para obter (ou recuperar) o valor de um atributo privado de uma classe. Eles são usados para garantir um acesso controlado aos atributos, permitindo que você defina regras ou lógica adicional ao retornar o valor. Em Python, os getters são comumente implementados usando decoradores de propriedade (@property).

# Resgatar alguma informação que esteja dentro da estrutura
# O decorador que altera estrutura:
# class Pessoa:
# @property
#     def nome(self):
#         return self._nome
# Por essa estrutura o método está fazendo a ligação do chamado com a estrutura;


# Setters:
# Os setters são métodos usados para definir (ou atualizar) o valor de um atributo privado de uma classe. Eles são usados para garantir um controle sobre a modificação dos atributos, permitindo que você defina regras ou lógica adicional ao atribuir um novo valor. Em Python, os setters são comumente implementados usando o decorador @<nome_atributo>.setter.

# Apontar algum informação / mudar

# class Pessoa():
#     @nome.setter
#     def nome(self,nome):
#         self._nome = nome