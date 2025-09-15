from datetime import datetime
from bicicleta import Bicicleta
from error import FormatoRutInvalido

class Reservas:  # Creamos la clase Reservas
    reservas_realizadas = 0

    def __init__(self, rut_cliente, id_reserva, fecha_inicio, fecha_fin, bicicleta, monto=0): 
        self.rut_cliente = rut_cliente
        self.id_reserva = id_reserva
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.bicicleta = bicicleta
        self.monto = monto

    def validar_rut(self, rut):  # Validamos el RUT con excepción personalizada
        if len(rut) != 9:
            raise FormatoRutInvalido(rut)
        return rut

    def reserva(self):  # Creamos el método reserva
        try:
            cliente = input("Ingrese su rut (sin puntos ni guión): ")
            self.rut_cliente = self.validar_rut(cliente)
            print(f"El rut es: {self.rut_cliente}")
        except FormatoRutInvalido as e:
            print(f"Error: {e}")
            return  # Salimos si el RUT no es válido

        try:
            fecha_inicio = input("Ingrese la fecha y hora de inicio (mm/dd/aaaa hh:mm): ")
            self.fecha_inicio = datetime.strptime(fecha_inicio, "%m/%d/%Y %H:%M")

            fecha_fin = input("Ingrese la fecha y hora de termino (mm/dd/aaaa hh:mm): ")
            self.fecha_fin = datetime.strptime(fecha_fin, "%m/%d/%Y %H:%M")

            if self.fecha_fin <= self.fecha_inicio:
                print("Error: La fecha de término debe ser posterior a la fecha de inicio.")
                return  # Salimos si las fechas son incorrectas

            print(f"La fecha y hora de inicio es: {self.fecha_inicio.strftime('%m/%d/%Y %H:%M')}")
            print(f"La fecha y término de fin es: {self.fecha_fin.strftime('%m/%d/%Y %H:%M')}")

        except ValueError:
            print("Formato de fecha incorrecto. Por favor, ingrese la fecha en el formato mm/dd/aaaa hh:mm.")
            return  # Salimos si el formato de fecha es incorrecto

        finally:
            print("Fin del proceso de ingreso de fechas.")  # Acción de limpieza

        self.bicicleta.disponible()
        aceptar = input("Desea realizar la reserva : (si/no) ")
        if aceptar.lower() == "si":
            self.bicicleta.disponibilidad = False
            print(f"Se confirma la reserva de la bicicleta {self.bicicleta.id_bicicleta}")
        else:
            print(f"No se ha realizado la reserva de la bicicleta {self.bicicleta.id_bicicleta}")
            self.bicicleta.disponibilidad = True
            self.bicicleta.precio = 0

        print()
        return self

    def cancelar_reserva(self):  # Creamos el método cancelar_reserva
        cancelar = input("Desea cancelar la reserva : si/no ")
        if cancelar.lower() == "si":
            self.bicicleta.disponibilidad = True
            print(f"Se ha cancelado la reserva de la bicicleta {self.bicicleta.id_bicicleta}")
        else:
            print(f"Se confirma la reserva de la bicicleta {self.bicicleta.id_bicicleta}")
        print()
        return self
    
    def monto_pagar(self):  # Creamos el método monto_pagar
        monto_dias = self.fecha_fin - self.fecha_inicio
        monto_horas = monto_dias.total_seconds() / 3600
        monto = monto_horas * self.bicicleta.precio
        self.monto = monto
        print(f"El monto a pagar es de: ${monto:.2f}")
        print()
        return self

    def pago(self):  # Creamos el método pago
        if self.monto == 0:
            print("No hay saldo pendiente.")
        else:
            input("Presente la TDC : ")
            print("Pago realizado con éxito")
            self.bicicleta.disponibilidad = True
        print()
        return self
