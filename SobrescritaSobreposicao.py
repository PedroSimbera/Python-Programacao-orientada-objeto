#Um resuminho sobre o conteúdo, mas destacando que em python pela sua tipagem dinâmica não se fala em sobrescrita e sobreposição

# Sobreposição e sobrescrita de métodos em Python referem-se à capacidade de uma classe derivada (subclasse) fornecer uma implementação diferente para um método já definido em sua classe base (superclasse). Isso permite que a subclasse personalize ou estenda o comportamento herdado dos métodos da superclasse.

# Sobreposição de métodos:
# A sobreposição ocorre quando uma classe derivada possui um método com o mesmo nome do método em sua classe base. Isso permite que a subclasse substitua o comportamento do método herdado. Para realizar a sobreposição, a subclasse redefine o método com sua própria implementação. A decisão de chamar ou não o método da superclasse dentro do método sobreposto é opcional e depende dos requisitos específicos.
# class Animal:
#     def fazer_som(self):
#         print("O animal está fazendo um som genérico.")

# class Cachorro(Animal): <<<<- forma de ser subclass
#     def fazer_som(self):
#         print("O cachorro está latindo.")

# animal = Animal()
# animal.fazer_som()   # Saída: O animal está fazendo um som genérico.

# cachorro = Cachorro()
# cachorro.fazer_som()  # Saída: O cachorro está latindo.

# Nesse exemplo, a classe Animal possui o método fazer_som(). A classe Cachorro herda da classe Animal e sobreposta o método fazer_som() com sua própria implementação. Ao chamar o método fazer_som() em uma instância de Cachorro, a versão sobreposta é executada.



# Sobrescrita de métodos:
# A sobrescrita é um caso específico de sobreposição em que uma classe derivada redefine completamente o método da classe base, substituindo a implementação original. Para isso, a subclasse redefine o método com a mesma assinatura (nome e parâmetros) do método da superclasse. Veja o exemplo abaixo:

# class Veiculo:
#     def mover(self):
#         print("O veículo está se movendo.")

# class Carro(Veiculo):
#     def mover(self):
#         print("O carro está acelerando.")

# veiculo = Veiculo()
# veiculo.mover()  # Saída: O veículo está se movendo.

# carro = Carro()
# carro.mover()    # Saída: O carro está acelerando.


# Neste exemplo, a classe Veiculo possui o método mover(). A classe Carro herda da classe Veiculo e sobrescreve o método mover() com sua própria implementação. Ao chamar o método mover() em uma instância de Carro, a versão sobrescrita é executada, substituindo completamente o comportamento herdado.

# É importante lembrar que a sobreposição e a sobrescrita são recursos poderosos, mas devem ser usados com cuidado e de acordo com a lógica e a estrutura do programa.