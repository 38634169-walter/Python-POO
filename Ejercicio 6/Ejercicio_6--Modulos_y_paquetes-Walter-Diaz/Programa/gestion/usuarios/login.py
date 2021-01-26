class Validar:
    def validarUsuario(cargo):
        if cargo == "encargado" or cargo == "ENCARGADO" or cargo == "Encargado":
            validarC = True
            return validarC
        else:
            validarC = False
            return validarC


    def validarContraseña(password):
        if len(password) > 3 and len(password) <= 8:
            validarP = True
            return validarP
        else:
            validarP = False
            return validarP

