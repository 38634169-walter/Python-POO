def verStock():
    desicion=98
    while desicion != 1 and desicion != 2 and desicion != 3 and desicion != 4:

        try:
            desicion=int(input("""
                ---INGRESE LA CATEGORIA QUE DESEA VER---
                1-Blockes
                2-Juegos
                3-Muñecos
                4-Volver al menu """))
        except ValueError:
            print("-----ERROR ingreso letras en lugar de numeros-----")
            verStock()
             

    if desicion == 1:
        indice=1        
        for value in blockes:
            print(indice," ",value)
            indice+=1
        verStock()
    elif desicion == 2:
        indice=1
        for value in juegos:
            print(indice," ",value)
            indice+=1
        verStock()
    elif desicion == 3:
        indice=1
        for value in muñecos:
            print(indice," ",value)
            indice+=1
        verStock()
    elif desicion == 4:
        pass



def ingresarStock():
    desicion=98
    while desicion != 1 and desicion != 2 and desicion != 3 and desicion != 4:

        try:
            desicion=int(input("""
                ---INGRESARN LA CATEGORIA A LA QUE DESEA AÑADIR STOCK---
                1-Blockes
                2-Juegos
                3-Muñecos
                4-Volver al menu """))
        except ValueError:
            print("-----ERROR ingreso letras en lugar de numeros-----")
            ingresarStock()

    if desicion == 1:
        variable=input("Ingrese nombre: ",)
        blockes.append(variable)
        ingresarStock()
    elif desicion == 2:
        variable=input("Ingrese nombre: ",)
        juegos.append(variable)
        ingresarStock()
    elif desicion == 3:
        variable=input("Ingrese nombre: ",)
        muñecos.append(variable)
        ingresarStock()
    elif desicion == 4:
        pass


blockes=["lego","rasti"]
juegos=["ajedrez","damas","TEG"]
muñecos=["playmovil","barbie"]
