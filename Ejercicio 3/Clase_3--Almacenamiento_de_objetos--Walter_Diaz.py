

class vehiculos():
    ruedas=4
    def __init__ (self,marca,modelo):
        self.marca=marca
        self.modelo=modelo
    def ver(self):
        return print("\nMarca del auto: ",self.marca,"\nModelo del auto: ",self.modelo,"\nNumero de rudas: ",self.ruedas)


    

def menu ():
    print('''\n\n\n
    ***************BIENVENIDO A CREACION DE VEHICULOS***************
    
    ---------------------------------------------------------------
                     1-Ingrese su vehiculo
    
                     2-Vea sus vehiculos ingresados

                     3-salir del programa
    ---------------------------------------------------------------
    \n
    ''')
    
    des=int(input())

    while des != 1 and des != 2 and des != 3:
        print('''\n\n\n
        ***************BIENVENIDO A CREACION DE VEHICULOS***************
        
        ---------------------------------------------------------------
                         1-Ingrese su vehiculo
        
                         2-Vea sus vehiculos ingresados

                         3-salir del programa
        ---------------------------------------------------------------
        \n
        ''')
        
        des=int(input())

        
    if des == 1:
        ingreso()
    elif des == 2:
        ingresados()
    elif des == 3:
        print("********Gracias por usar el programa********")


def ingreso():
    print("\n---------------------------------------------\n")
    marca=input("-Ingresar marca: ",)
    modelo=input("-Ingresar modelo: ",)
    codigo=input("-Ingresar codigo de referencias: ")
    print("---------------------------------------------\n")
    print("\n---¿DESEA VOLVER AL MENU ANTERIOR?---\n")
    volver=int(input("   1- SI        2-INGRESAR MAS VEHICULOS  "))

    while volver!= 1 and volver != 2:
        print("\n---¿DESEA VOLVER AL MENU ANTERIOR?---\n")
        volver=int(input("   1- SI        2-INGRESAR MAS VEHICULOS  "))

    auto=vehiculos(marca,modelo)
    autos.append(auto)
    codigos.append(codigo)
    
    if volver == 1:
        volver=0
        menu()
    else:
        volver=0
        ingreso()

        
def ingresados():
    print("\n----------------------------------------------------\n")
    ing=input("-Ingrese el codigo de referencia: ",)
    i=len(codigos)

    for valor in range(0,i):
        if ing == codigos[valor]:
            x=valor
            break

    print(autos[x].ver())
    print("----------------------------------------------------\n")
    print("\n---¿DESEA VOLVER AL MENU ANTERIOR?---\n")
    volver=int(input("   1- SI        2-BUSCAR MAS VEHICULOS  "))

    while volver!= 1 and volver != 2:
        print("\n---¿DESEA VOLVER AL MENU ANTERIOR?---\n")
        volver=int(input("   1- SI        2-BUSCAR MAS VEHICULOS  "))

    if volver == 1:
        volver=0
        menu()
    else:
        volver=0
        ingresados()
    
        

autos=[]
codigos=[]
menu()
