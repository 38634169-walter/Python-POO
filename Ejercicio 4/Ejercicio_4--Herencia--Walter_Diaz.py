
class Productos():
    def __init__(self,nombre,costo,tipo):
        self.nombre=nombre
        self.costo=costo
        self.tipo=tipo
    def informe(self):
        print(f"""   ---INFORME DEL PRODUCTO---

        Nombre: {self.nombre}
        Costo:  {self.costo}
        Tipo:   {self.tipo}      """)


class Herramientas(Productos):
    
    def garantia(self):
        marca=input("Ingresar nombre de la marca: ",)

        if marca == "Stanley" or marca == "STANLEY" or marca == "stanley":
           garantiaP = 12
        else:
            garantiaP = 6

        print(f"-La garantia es de {garantiaP} meses")
        


class Maquinas(Herramientas):
    def consumo(self):
        print("--Para calcular el consumo en KWH de la maquina ingrese los siguientes datos--\n")
        potencia=int(input("Potencia: ",))
        horas_uso=int(input("Horas de uso promedio: ",))
        cons= potencia*horas_uso
        print(f"\n-La consumo de KWH de la maquina es : {cons}")



class Otros(Productos):
    def descripcion(self):
        descrip=input("Ingrese descripcion del producto: ",)
        print("\n\n",descrip)






def salir ():
    desicion="p"
    while desicion != "N" and desicion != "n":

        desicion=input("Desea seguir ingresando datos(Y/N): ",)

        if desicion == "Y" or desicion == "y":
            menu()

        elif desicion == "N" or desicion == "n":
            print("\n\n-----Gracias por usar el programa-----\n\n")





def menuMaquina(producto,costo,tipo):

    obj=Maquinas(producto,costo,tipo)

    print("""\n\n
        1-Ver datos del producto
        2-Calcular garantia
        3-Calcular consumo
        4-Volver al menu
        5-Salir del programa
        """)    
    desicion=int(input())

    if desicion == 1:
        obj.informe()
        menuMaquina(producto,costo,tipo)
        
    elif desicion == 2:
        obj.garantia()
        menuMaquina(producto,costo,tipo)

    elif desicion == 3:
        obj.consumo()
        menuMaquina(producto,costo,tipo)

    elif desicion == 4:
        menu()

    else:
        pass

    
    

def menuHerramienta(producto,costo,tipo):
    obj=Herramientas(producto,costo,tipo)

    print("""\n\n
        1-Ver datos del producto
        2-Calcular garantia
        3-Volver al menu
        4-Salir del programa
        """)    
    desicion=int(input())
    if desicion == 1:
        obj.informe()
        menuHerramienta(producto,costo,tipo)

    elif desicion == 2:
        obj.garantia()
        menuHerramienta(producto,costo,tipo)

    elif desicion == 3:
        menu()
    
    else:
        pass

        
def menuOtro(producto,costo,tipo):
    obj=Otros(producto,costo,tipo)

    print("""\n\n
        1-Ver datos del producto
        2-Agregar una descripcion
        3-Volver al menu
        4-Salir del programa
        """)    
    desicion=int(input())
    if desicion == 1:
        obj.informe()
        menuOtro(producto,costo,tipo)

    elif desicion == 2:
        obj.descripcion()
        menuOtro(producto,costo,tipo)

    elif desicion == 3:
        menu()

    else:
        pass
    




def menu():

    print("\n\n************FERETERIA LA TUERCA************\n\n")

    producto=input("-Ingresar nombre del producto: ",)
    tipo=input("\n-Ingresar tipo de producto(maquina/herramienta/otro): ",)
    costo=int(input("\n-Ingresr costo del producto: "))

    if tipo == "maquina" or tipo == "Maquina":
        menuMaquina(producto,costo,tipo)

    elif tipo == "herramienta" or tipo == "Herramienta":
        menuHerramienta(producto,costo,tipo)

    elif tipo == "otro" or tipo == "Otro":
        menuOtro(producto,costo,tipo)

    else:
        print("\n\n--DATOS MAL INGRESADOS--\n\n")

    salir()


    
    

menu()
    
    
    
    




    
        





