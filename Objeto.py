# Para chamar a classe se utiliza o import e o from
# No exemplo de pessoas da parte de aplicação seria:
# from Pessoa import Pessoa
# p= Pessoa()
# p.exibir()


# Formas:
class Carro:
    def sobre(self, cor, marca, modelo):
        self.cor = cor
        self.marca = marca
        self.modelo = modelo

    def acelerar(self):
        print("O carro está acelerando.")

    def frear(self):
        print("O carro está freando.")

# Criando uma instância da classe Carro
meu_carro = Carro("vermelho", "Ford", "Fiesta")

# Acessando os atributos do objeto
print(meu_carro.cor)     # Saída: vermelho
print(meu_carro.marca)   # Saída: Ford
print(meu_carro.modelo)  # Saída: Fiesta

# Chamando os métodos do objeto
meu_carro.acelerar()     # Saída: O carro está acelerando.
meu_carro.frear()        # Saída: O carro está freando.
