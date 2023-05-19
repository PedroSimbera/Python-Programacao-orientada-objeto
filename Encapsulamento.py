# Encapsulamento em Python refere-se à prática de ocultar os detalhes internos de uma classe, protegendo seus atributos e métodos de acesso e modificação diretos por outros objetos. É uma maneira de garantir o acesso controlado aos membros de uma classe e promover a segurança e integridade dos dados.

# Em Python, o encapsulamento é alcançado por meio de convenções e níveis de visibilidade de atributos e métodos. Existem três níveis de visibilidade comumente usados:

# Público:
# Os membros públicos de uma classe são acessíveis de fora da classe, ou seja, podem ser acessados por outros objetos ou partes do código. Por padrão, todos os atributos e métodos em Python são considerados públicos, a menos que sejam explicitamente definidos como privados ou protegidos.

# Privado:
# Os membros privados de uma classe são prefixados com um único sublinhado _. Eles são destinados a serem usados apenas internamente pela própria classe e não devem ser acessados diretamente de fora da classe. No entanto, em Python, o acesso aos membros privados ainda é possível, mas é considerado uma convenção de código não violar o encapsulamento.
# class Exemplo:
#     def __init__(self):
#         self._atributo_privado = 10  # Atributo privado

#     def _metodo_privado(self):
#         return self._atributo_privado * 2  # Método privado

# objeto = Exemplo()
# print(objeto._atributo_privado)   # Saída: 10
# print(objeto._metodo_privado())   # Saída: 20

# Protegido:
# Os membros protegidos de uma classe são prefixados com dois sublinhados __. Eles são semelhantes aos membros privados, mas têm uma restrição adicional de acesso. Os membros protegidos só podem ser acessados por objetos da própria classe e suas subclasses. O acesso direto a esses membros fora da classe ou de suas subclasses resultará em um erro.

# class Exemplo:
#     def __init__(self):
#         self.__atributo_protegido = 10  # Atributo protegido

#     def __metodo_protegido(self):
#         return self.__atributo_protegido * 2  # Método protegido

# objeto = Exemplo()
# print(objeto._Exemplo__atributo_protegido)   # Saída: 10
# print(objeto._Exemplo__metodo_protegido())   # Saída: 20

# É importante observar que a utilização de convenções de nomenclatura e a boa prática de programação são essenciais para respeitar o encapsulamento. Os desenvolvedores devem evitar o acesso direto a membros privados e protegidos, optando por usar os métodos públicos (getters e setters) para interagir com esses membros, conforme necessário.