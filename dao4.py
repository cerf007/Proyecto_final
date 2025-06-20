# tenemos la Lista vacía para guardar los datos de los clientes
clientes = []

# Registramos los clientes
while True:
    print("Registro de Cliente")
    nombre = input("Escribe el nombre del cliente: ")
    pago = input("¿Cuánto pagó?: ")
    plan = input("¿Qué plan tiene? (1 = Básico, 2 = Pro, 3 = Premium): ")
    
    #Estado se deja vacío por ahora
    cliente = [nombre, pago, plan, ""]
    clientes.append(cliente)
    
    seguir = input("¿Quieres agregar otro cliente? (s/n): ")
    if seguir.lower() != "s":
        break

#Recorrer todos los clientes y pedir su estado
print("\n--- ACTUALIZAR ESTADO DE LOS CLIENTES ---\n")
for cliente in clientes:
    print("Cliente:", cliente[0])
    estado = input("¿Cuál es el estado? (Pagada / Pendiente / Vencida): ")
    cliente[3] = estado

#Mostramos lista final
print("\n--- LISTA FINAL DE CLIENTES ---")
for cliente in clientes:
    print("Nombre:", cliente[0], "| Pago:", cliente[1], "| Plan:", cliente[2], "| Estado:", cliente[3])
