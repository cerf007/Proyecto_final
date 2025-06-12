# Lista vacía para guardar los datos de los clientes
clientes = []





# Bucle para registrar clientes
while True:
    print("=== Registro de Cliente ===")
    nombre = input("Escribe el nombre del cliente: ")
    pago = input("¿Cuánto pagó?: ")
    plan = input("¿Qué plan tiene? (1 = Básico, 2 = Pro, 3 = Premium): ")
    estado = input("¿Cuál es el estado? (1 = Al día, 2 = Pendiente, 3 = Moroso): ")
# Guardamos los datos en una lista
    cliente = [nombre, pago, plan, estado]
    clientes.append(cliente)
    seguir = input("¿Quieres agregar otro cliente? (s/n): ")
    if seguir != "s":
        break
# Mostramos los datos guardados
print("\n=== Lista de Clientes ===")
for cliente in clientes:
    print("Nombre:", cliente[0], "| Pago:", cliente[1], "| Plan:", cliente[2], "| Estado:", cliente[3])
