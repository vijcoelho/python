class tv:
    def __init__(self, canal=0, volume=0):
        self.canal = canal
        self.volume = volume

    def mudarCanal(self):
        while True:
            aumentar_canal = input('\nTrocar Canal (1) (2) (mudar o volume aperte 0): ')
            if aumentar_canal == '1':
                novoCanal = self.canal + 1
                self.canal = novoCanal
                print(f'Canal {self.canal}')
                if self.canal == 0:
                    break
            elif aumentar_canal == '0':
                break
            else:
                novoCanal = self.canal - 1
                self.canal = novoCanal
                print(f'Canal {self.canal}')

    def trocarVolume(self):
        while True:
            aumentar_volume = input('\nAumentar (1) Diminuir (2)| PARA SAIR APERTE 0 |: ')
            if aumentar_volume == '1':
                novoVolume = self.volume + 1
                self.volume = novoVolume
                print(f'Volume {self.volume}')
                if self.volume == 100:
                    print('Volume Maximo')
                    break
            elif aumentar_volume == '0':
                break
            else:
                novoVolume = self.volume - 1
                self.volume = novoVolume
                print(f'Volume {self.volume}')

    def resultado(self):
        print(f'\nCanal {self.canal} | Volume {self.volume}')

televisao = tv(0, 0)
televisao.mudarCanal()
televisao.trocarVolume()
televisao.resultado()