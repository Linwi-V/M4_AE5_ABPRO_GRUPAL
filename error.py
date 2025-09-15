class FormatoRutInvalido(Exception):
    def __init__(self, rut):
        self.rut = rut
        super().__init__(f"El RUT '{rut}' no tiene el formato válido. El rut debe tener 9 carácteres.")
 
def reservar (self):
    try:
        cliente = input("Ingrese su rut (sin puntos ni guión):")
        if len(cliente) == 9:
            print(f"El rut es: {cliente}")
        else:
            raise FormatoRutInvalido(cliente)
    except FormatoRutInvalido as e:
        print(f"Error: {e}")

    
        

