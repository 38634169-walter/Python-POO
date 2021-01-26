print("\n\n\n")

class pizzeras():
    alto=2
    diametro=30
    material="Acero"
    def volumen(self):
        vol=self.diametro*self.alto
        print(f"El diametro es {vol}")




pizza1=pizzeras()

pizza2=pizzeras()

pizza3=pizzeras()

pizza4=pizzeras()

pizza5=pizzeras()

print(pizza5.material)
print(pizza1.volumen())

class vasos ():
    alto=10
    diametro=5
    materia="vidrio"
    def capacidad(self):
        cap=self.alto*self.diametro
        print(f"La capacidad de carga es {cap}")



vaso1=vasos()

vaso2=vasos()
vaso2.alto=15

vaso3=vasos()
vaso3.alto=15
vaso3.diametro=4.5

vaso4=vasos()
vaso4.diametro=4.5
vaso4.material="plastico"

vaso5=vasos()

print(vaso3.diametro)
print(vaso4.capacidad())


class ollas():
    alto=20
    diametro=40
    material="acero"
    def capacidad_carga(self):
        capa=self.alto*self.diametro
        print(f"La capacidad de carga es de {capa}")


olla1=ollas()

olla2=ollas()
olla2.alto=5
olla2.diametro=15
olla2.material="aluminio"

olla3=ollas()
olla3.alto=15
olla3.diametro=20
olla3.material="barro"

olla4=ollas()
olla4.alto=10
olla4.diametro=25
olla4.material="cobre"

olla5=ollas()
olla5.alto=25
olla5.diametro=35
olla5.material="ceramica"

print(olla3.material)
print(olla4.capacidad_carga())
