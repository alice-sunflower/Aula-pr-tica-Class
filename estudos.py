#Classe Computador

#Criando a CLASSE "computador"
class Computador():
    #Definindo a primeira função do classe
    def __init__(self, marca, memoria_ram, placa_de_video):
        self.marca = marca
        self.memoria_ram = memoria_ram
        self.placa_de_video = placa_de_video

    #Definindo métodos a serem usados posteriormente
    def iniciar(self):
        print('Isso aqui ligaria o computador. ')

    def desligar(self):
        print('Isso aqui desligaria o computador. ')

    def ExibirInformacoes(self):
        print(f'Marca: {self.marca} --- Memória: RAM {self.memoria_ram} --- Placa de Vídeo: {self.placa_de_video}')

#Criando uma variável que receberá a CLASSE "computador" e alguns parâmetros para completar os requerimentos 
computador1 = Computador('Nvidia', '12GB', 'GTX 750 TI')

#Métodos aplicados
computador1.iniciar()
computador1.desligar()
computador1.ExibirInformacoes()
