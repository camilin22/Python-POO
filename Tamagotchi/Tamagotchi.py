

class Tamagotchi:
    def __init__(self, nombre):
        self.nombre = nombre
        self.nivel_energia = 100
        self.nivel_hambre = 0
        self.nivel_felicidad = 50
        self.humor = "indiferente"
        self.esta_vivo = True

    def mostrar_estado(self):
        print(f"Nombre: {self.nombre}")
        print(f"Nivel de energía: {self.nivel_energia}")
        print(f"Nivel de hambre: {self.nivel_hambre}")
        print(f"Estado de humor: {self.humor}")

    def alimentar(self):
        self.nivel_hambre -= 10
        if self.nivel_hambre < 0:
            self.nivel_hambre = 0
        self.nivel_energia -= 15
        if self.nivel_energia <= 0:
            self.esta_vivo = False
            print(f"{self.nombre} ha muerto de hambre.")
        self.verificar_estado()

    def jugar(self):
        self.nivel_felicidad += 20
        self.nivel_energia -= 18
        self.nivel_hambre += 10
        if self.nivel_hambre >= 20:
            self.nivel_energia -= 20
            self.nivel_felicidad -= 30
            if self.nivel_energia <= 0:
                self.esta_vivo = False
                print(f"{self.nombre} ha muerto por falta de energía.")
        self.verificar_estado()

    def dormir(self):
        self.nivel_energia += 40
        self.nivel_hambre += 5
        if self.nivel_hambre >= 20:
            self.nivel_energia -= 20
            self.nivel_felicidad -= 30
            if self.nivel_energia <= 0:
                self.esta_vivo = False
                print(f"{self.nombre} ha muerto por falta de energía al dormir.")
        self.verificar_estado()

    def verificar_estado(self):
        if self.nivel_energia <= 0:
            self.esta_vivo = False
            print(f"{self.nombre} ha muerto por falta de energía.")
        elif self.nivel_hambre >= 20:
            self.nivel_energia -= 20
            self.nivel_felicidad -= 30
            if self.nivel_energia <= 0:
                self.esta_vivo = False
                print(f"{self.nombre} ha muerto por falta de energía.")
                
                
                mi_mascota = Tamagotchi("Blanqui")
                mi_mascota.mostrar_estado()

