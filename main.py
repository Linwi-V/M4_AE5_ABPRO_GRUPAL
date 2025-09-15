from bicicleta import Bicicleta
from reservas import Reservas    
from datetime import datetime

# Crear bicicletas
bicicleta1 = Bicicleta(1, "merida", "Big Nine 500", True, 2000) 
bicicleta2 = Bicicleta(2, "Bianchi", "Trek", True, 1000)
bicicleta3 = Bicicleta(3, "Silverback", "Strela", True, 3000)

inventario_bicicletas = [bicicleta1, bicicleta2, bicicleta3]

# Definir fechas de prueba
fecha_inicio1 = datetime(2025, 8, 10, 10, 0)
fecha_fin1 = datetime(2025, 8, 11, 10, 0)

fecha_inicio2 = datetime(2025, 8, 15, 13, 30)
fecha_fin2 = datetime(2025, 8, 17, 16, 0)

fecha_inicio3 = datetime(2025, 8, 12, 10, 0)
fecha_fin3 = datetime(2025, 8, 22, 18, 30)   

# Crear reservas con RUT válido (string de 9 caracteres)
reserva1 = Reservas("123456789", 1, fecha_inicio1, fecha_fin1, bicicleta1) 
reserva2 = Reservas("987654321", 2, fecha_inicio2, fecha_fin2, bicicleta2)
reserva3 = Reservas("112233445", 3, fecha_inicio3, fecha_fin3, bicicleta3)  

inventario_reservas = [reserva1, reserva2, reserva3]    

# Ahora, para la prueba, definimos un método para hacer reservas sin pedir input en el main:

def procesar_reserva(reserva: Reservas):
    # Validar RUT (lo hace en el constructor o método propio)
    try:
        reserva.validar_rut(reserva.rut_cliente)
    except Exception as e:
        print(f"Error en RUT: {e}")
        return

    # Mostrar estado bicicleta
    reserva.bicicleta.disponible()

    # Confirmar reserva (simulado aquí como "sí")
    confirmar = "si"
    if confirmar.lower() == "si":
        reserva.bicicleta.disponibilidad = False
        print(f"Se confirma la reserva de la bicicleta {reserva.bicicleta.id_bicicleta}")
    else:
        print(f"No se ha realizado la reserva de la bicicleta {reserva.bicicleta.id_bicicleta}")
        reserva.bicicleta.disponibilidad = True
        reserva.bicicleta.precio = 0

    reserva.monto_pagar()
    reserva.pago()
    print()

# Procesar todas las reservas
for r in inventario_reservas:
    procesar_reserva(r)
