print("\n\n\n***************Bienvenido a creacion de vehiculos***************\n\n")

class autos():
    ruedas=4
    def __init__(self,marca,modelo):
        self.marca=marca
        self.modelo=modelo
    def ver(self):
        print("\n-Marca del auto: ",self.marca,"\n-Modelo del auto: ",self.modelo,"\n-Cantidad de ruedas: ",self.ruedas)


marca=[]
auto=[]
modelo=[]
salir=1

while(salir!=0):

    aut=input('\n-Ingresar nombre del auto: ',)
    auto.append(aut)
    mode=input('\n-Ingresar modelo del auto: ',)
    modelo.append(mode)
    marc=input('\n-Ingresar marca del auto:',)
    marca.append(marc)
    print('-------------------------------------------------------------------------')
    print("-Ingrese '0' para salir o cualquier otro numero para continuar ingresando")
    print('-------------------------------------------------------------------------\n')
    salir=int(input())
    


sal=1
i=len(auto)
while(sal!=0):
    print("\n\n-----------------------------------------------------------")
    print("INGRESE EL NOMBRE DEL AUTO DEL QUE DESEA VER LOS DATOS")
    print("---------------------------------------------------------------")
    mo=input("Nombre del auto:",)
    for e in range(0,i):
        if mo==auto[e]:
            a=autos(marca[e],modelo[e])
            print(a.ver())
    print('-------------------------------------------------------------------------')
    print("-Ingrese '0' para salir o cualquier otro numero para continuar ingresando")
    print('-------------------------------------------------------------------------\n')
    sal=int(input())
    
