'''

atividae na contruçao de um codigo que utliza objetos



'''



class Celular:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.ligado = False
        self.bateria = 100
        self.carregando = False

    def ligar(self):
        self.ligado = True 
        print(f"{self.marca} {self.modelo} está ligado.")

    def Bateria(self):
        self.bateria = 100
        print(f"{self.marca} esta carregado")

    def carregar(self):
        self.carregando = True
        print(f"{self.marca} {self.modelo} esta carregando.")







meu_celular = Celular("Motorola", "G56 5G") 
meu_celular.ligar()
meu_celular.bateria = 5 
print(f"{meu_celular.modelo} esta com {meu_celular.bateria}% de bateria")
meu_celular.Bateria()
meu_celular.carregar()
meu_celular.Bateria()
meu_celular.carregando = True
meu_celular.carregar()
meu_celular.bateria = 100
print(f"{meu_celular.modelo} esta com {meu_celular.bateria}% de bateria")



