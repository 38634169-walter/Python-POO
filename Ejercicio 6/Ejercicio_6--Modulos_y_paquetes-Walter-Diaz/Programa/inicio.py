from gestion.usuarios.login import Validar
from gestion.productos.stock import verStock,ingresarStock

def ingreso():
    print("\n\n*****JUGUETERIA TREN LOCO*****\n\n")
    nombre=input("Nombre: ",)
    cargo=input("Cargo: ",)

    validarC = Validar.validarUsuario(cargo)

    if validarC == False:
        print("\n\n-----Solamente los encargados pueden acceder-----\n\n")
    elif validarC == True:
        password=input("Contraseña: ",)
        validarP = Validar.validarContraseña(password)
        if validarP == False:
            print("\n\n-----CONTRASEÑA INCORRECTA-----\n\n")
            ingreso()
        else:
           menu()


           
def menu():
    desicion=89
    while desicion != 1 and desicion != 2 and desicion != 3: 
        try:
             desicion=int(input("""
                        ********** MENU **********
                        1-Ver stock
                        2-Cargar nuevo juguete
                        3-Salir del programa
                    """))
             
        except ValueError:
            print("---INGRESO UNA LETRA EN LUGAR DE NUMERO---")
    

    if desicion == 1:
        verStock()
        menu()
    if desicion == 2:
        ingresarStock()
        menu()
    if desicion == 3:
        print("*****GRACIAS POR USAR EL PROGRAMA*****")
        pass




            
ingreso()
    

