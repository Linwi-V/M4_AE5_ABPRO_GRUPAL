class Bicicleta:  # Creamos la clase bicicleta
    def __init__(self, id_bicicleta, marca, modelo, disponibilidad, precio):
        self.id_bicicleta = id_bicicleta
        self.marca = marca
        self.modelo = modelo
        self.disponibilidad = disponibilidad
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id_bicicleta}, Marca: {self.marca}, Modelo: {self.modelo}, Disponibilidad: {self.disponibilidad}, Precio: {self.precio}"
    
    def registrar (self): 
        if self.precio < 0: #para que no sea negativo
            raise ValueError("El precio no puede ser negativo.")
        if not self.id_bicicleta:
            raise ValueError("El ID de la bicicleta no puede estar vacío.")
        try:  #abrir el archivo
            with open("bicicletas.txt", "a") as archivo:
                archivo.write(f"{self.id_bicicleta},{self.marca},{self.modelo},{self.disponibilidad},{self.precio}\n")
        except FileNotFoundError:
            print("El archivo no existe.")
        finally:
            archivo.close()
        return self

    def disponible (self):
        if self.disponibilidad == True:
            print(f"La bicicleta {self.id_bicicleta} está Disponible")
        else:
            print(f"La bicicleta {self.id_bicicleta} está Reservada")