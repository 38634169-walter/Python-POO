def ingresos():
    destin = 45
    while destin != 1 and destin != 2 and destin != 3:
        print("\n\n*******SISTEMA DE INGRESO DE VIAJES*******\n\n")

        try:
            dni=int(input("DNI: ",))
            destin=int(input("""
                            Ingresar Destino:
                            
                1-Argentina    2-Brasil    3-Otro """,))
            
            cant_dias=int(input("\n Cantidad de dias en el destino: ",))
                             
        except ValueError:
            print("ERROR- ingreso lestras donde iban numeros")
            ingresos()


    if destin == 1:
        destino ="Argentina"

    elif destin == 2:
        destino = "Brasil"

    else:
        destino = "Otro"
                         
        
    obj=Menu(dni,destino,cant_dias)
    obj.m()
    
        


class Menu():

    def __init__(self,dni,destino,cant_dias):
        self.__dni = dni
        self.destino = destino
        self.cant_dias = cant_dias

    def m(self):
        indice = 9

        while indice != 1 and indice != 2 and indice != 3 and indice != 4 and indice != 5:
            print("""
                1-Ver mis datos
                2-Editar datos (destino, cantidad de dias en el destino)
                3-Definir tipo de estadia
                4-Calcular costo del viaje
                5-Salir del programa
                """)
            
            try:
                indice=int(input())

            except ValueError:
                print("ERROR-- no ingreso un numero")
                self.m()    

    
        if indice == 1:
            self.mostrar()
            
        elif indice == 2:
            self.editar()

        elif indice == 3:
            self.__estadia()

        elif indice == 4:
            self.calcular_costo()

        elif indice == 5:
            self.salir()



    def editar(self):
        destin=48
        while destin != 1 and destin != 2 and destin != 3:
            try:
                destin=int(input("""
                                Ingresar Destino:
                                
                    1-Argentina    2-Brasil    3-Otro """,))
                self.cant_dias=int(input("\n-Reingrese cantidad de dias de estadia: ",))

            except ValueError:
                print("ERROR- Ingreso letras donde deberia ingresar numeros")
                self.editar()
        

        if destin == 1:
            self.destino ="Argentina"

        elif destin == 2:
            self.destino = "Brasil"

        else:
            self.destino = "Otro"
            
        self.m()


    
    def __estadia(self):
        desicion=2
        while desicion != 1:
            
            if self.cant_dias > 7:
                print("Estadia larga".upper())
            else:
                print("Estadia corta".upper())

            print("\n -- Ingrese 1 para volver al menu \n")

            try:
                desicion=int(input())
            except ValueError:
                print("ERROR- no ingreso un numero")
                self.__estadia()
            

        if desicion == 1:
            self.m()


            
    def calcular_costo(self):

        desicion=2
        while(desicion != 1):
            if self.destino == "Argentina":
                costo=2000
                if self.cant_dias > 7:
                    costo*=0.90

            elif self.destino == "Brasil":
                costo=5000
                if self.cant_dias > 7:
                    costo*=0.90

            if self.destino == "Otro":
                costo=10000
                if self.cant_dias > 7:
                    costo*=0.90

            print(f"-Su costo es ${costo} por dia")
                
            print("\n -- Ingrese 1 para volver al menu \n")

            try:
                desicion=int(input())
            except ValueError:
                print("ERROR- no ingreso un numero")
                self.calcular_costo()


        if desicion == 1:
            self.m()


    def mostrar(self):
        desicion = 2
        while desicion != 1:
            print(f"""
            ---------------------------------------------------
            ---------------------------------------------------
                Estos son sus datos ingresados:

                DNI: {self.__dni}
                Destino: {self.destino}
                Cantidad de dias en el destino: {self.cant_dias}
            ---------------------------------------------------
            ---------------------------------------------------
                """)
            try:
                desicion=int(input("1-Para volver al menu"))
            except ValueError:
                print("ERROR- no ingreso un numero")
                self.mostrar()
            

        if desicion == 1:
            self.m()

    def salir(self):

        desicion="j"
        while desicion != "N" and desicion != "n" and desicion != "Y" and desicion != "y":
            desicion=input("Seguro que desea salir(Y/N): ",)

        if desicion == "N" or desicion == "n":
            self.m()

        if desicion == "Y" or desicion == "y":
            print("\n\n*****GRACIAS POR USAR EL PROGRAMA*****")
            pass

        



ingresos()



