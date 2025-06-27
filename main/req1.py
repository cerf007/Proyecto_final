import models.classes as c
import dao.functions as f
import datetime
import os
 
servicios = f.ClientDao()
registro_factura = f.BillDao()

def menu():
    print("""
Bienvenido a su registradora. ELija de una de las siguientes ipciones
1.Agregar cliente
2.Mostrar clientes
3.Editar clientes
4.Eliminar Cliente
5.Registrar pagos
6.Generar reporte financiero
7.Búsqueda e impresión de facturas
8.Salir
""")
    
def main():
    while True:
        try:
            menu()
            opcion = int(input("Ingrese la opcion: ")) #Se me olvido el input
            if opcion == 1:
                registrar_cliente()
            elif opcion == 2:
                servicios.show()
            elif opcion == 3:
                editar_cliente()
            elif opcion == 4:
               eliminar_cliente()
            elif opcion == 5:
                registrar_pago()
            elif opcion == 7:
                buscar_imprimir_factura()
            elif opcion == 8:
                print("Saliendo....")
                break
            else:
                print("Opción inválida. Ingrese solo el número 1 por ahora")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")

def registrar_cliente():
    while True:
        try:
            nombres = input("Ingrese los 2 nombres del cliente: ").strip()
            if not nombres:
                print("No puede haber una entrada de datos vacía")
            elif all(part.isalpha() for part in nombres.split()):
                break
            else:
                print("Los nombres solo deben contener caracteres alfabéticas")
        except ValueError:
            print("Error, caracteres inválidos")
            
    while True:
        try:
            apellidos = input("Ingrese los 2 apellidos del cliente: ").strip()
            if not apellidos:
                print("No puede haber una entrada de datos vacía")
            elif all(part.isalpha() for part in apellidos.split()):
                break
            else:
                print("Los apeellidos solo deben de contener caracteres alfabéticos ")
        except  ValueError:
            print("Error, caracteres inválidos")
    
    #agregando cédula como identificador
    while True:
        try:
            cedula_str = input("Ingrese la cédula del cliente [Formato = xxx-xxxxx-xxxx, 13 números y caracter alfabético al final]: ").strip()
            if not cedula_str:
                print("No puede haber una entrada de datos vacía")
            if (len(cedula_str) == 16 and cedula_str[3] == '-' and cedula_str[10] == '-' and cedula_str[:-1].replace('-', '').isdigit() and cedula_str[-1].isalpha()):
                break
            else:
                print("Numero de cédula inválido. El formato introducido es inválido")
        except ValueError:
            print("Caracteres inválidos. Por favor, solo ingrese el formato adecuado [Formato: xxx-xxxxxx-xxxx, 13 números y caracter alfabético al final]")
        
            
    while True:
        try:
            numero_telefono_str = input("Ingrese el número telefónico del cliente [8 dígitos, sin espacios de separación]: ").strip()
            if not numero_telefono_str:
                print("No puede haber una entrada de datos vacía")
            elif len(numero_telefono_str) == 8 and numero_telefono_str.isdigit():
                numero_telefono = int(numero_telefono_str)
                break
            else:
                print("Numero de telefono inválido. Debe de ser de 8 números y sin espacios")
        except ValueError:
            print("Carácteres inválidos. Por favor, solo ingrese numeros")
    
    while True:
        try:        
            correo_elec = input("Ingrese el correo electrónico del cliente: ").strip()
            if not correo_elec:
                print("No puede haber una entrada de datos vacía")
            else:
                break
        except ValueError:
            print("Carácteres inválidos")
      
    while True:
        try:  
            direccion = input("Ingrese la dirección del cliente: ").strip()
            if not direccion:
                print("No puede haber una entrada de datos vacía")
            else:
                break
        except ValueError:
            print("Carácteres inválidos")
            
    for cliente in servicios.service:
        if cliente.identification.lower() == cedula_str.lower():
            print("Ya existe un cliente con esa cédula.")
            return
        if cliente.phone_number == numero_telefono:
            print("Ya existe un cliente con ese número telefónico.")
            return
        if cliente.email.lower() == correo_elec.lower():
            print("Ya existe un cliente con ese correo electrónico.")
            return
    
    registrar = c.Client(nombres, apellidos, cedula_str ,numero_telefono, correo_elec, direccion)
    servicios.add(registrar)
    limpiar_pantalla()
    
def eliminar_cliente():
    while True:
        try:
            busqueda = input("Ingrese los 2 nombres, los 2 apellidos del cliente a buscar o la cedula: ").strip()
            if not busqueda:
                print("Debe ingresar el nombre, el apellido o la cédula")
                break
            buscando_cliente = buscar_cliente(busqueda)
            if buscando_cliente:
                servicios.delete(buscando_cliente)
                facturas_a_eliminar = [factura for factura in registro_factura.state if factura.client.identification == buscando_cliente.identification]
                for factura in facturas_a_eliminar:
                    registro_factura.delete(factura)
                print(f"Cliente {buscando_cliente.name} {buscando_cliente.last_name} eliminado.")
                limpiar_pantalla()
                break
            else:
                print("Cliente no encontrado.")
                limpiar_pantalla()
                break
        except ValueError:
            print("Entrada no válida, intenté de nuevo")
            limpiar_pantalla()
            break
            
def editar_cliente():
     while True:
           try:
               busqueda = input("Ingrese los 2 nombres, los 2 apellidos del cliente a buscar o la cedula: ").strip()
               if not busqueda:
                   print("Debe ingresar el nombre, el apellido o la cédula")
                   limpiar_pantalla()
                   break
               buscando_cliente = buscar_cliente(busqueda)
               if buscando_cliente:
                        print("Cliente encontrado:")
                        print(buscando_cliente)
                        editar_nuevo_cliente(buscando_cliente)
                        limpiar_pantalla()
                        break
               else: 
                   print("Cliente no encontrado")
                   limpiar_pantalla()
                   break
           except ValueError:
               print("Error inesperado al ingresar dartos")
               limpiar_pantalla()
               break

def editar_nuevo_cliente(cliente):
    nuevo_nombre = cliente.name
    nuevo_apellido = cliente.last_name
    nueva_cedula = cliente.identification
    nuevo_numero_telefono = str(cliente.phone_number)
    nuevo_correo_elec = cliente.email
    nuevo_direccion = cliente.address

    while True:
        try:
            entrada = input(f"Ingrese los 2 nuevos nombres del cliente [{cliente.name}]: ").strip()
            if entrada == "":
                break #Agregue esto si quiero mantener el nombre igual, ahora es agregar a todos
            elif  all(part.isalpha() for part in entrada.split()):
                nuevo_nombre = entrada
                break
            else:
                print("Los nombres solo deben contener caracteres alfabéticas")
        except ValueError:
            print("Error, caracteres inválidos")
        
        
    while True:
        try:
            entrada = input(f"Ingrese los 2 nuevos apellidos del cliente [{cliente.last_name}]: ")
            if entrada == "":
                break
            elif  all(part.isalpha() for part in entrada.split()):
                nuevo_apellido = entrada
                break
            else:
                print("Los apellidos solo deben contener caracteres alfabéticas")
        except ValueError:
            print("Caracter inválido, ingrese solo carácteres alfabéticos")
        
    while True:
        try:
            entrada = input(f"Ingrese la nueva cedula del cliente en [Formato: xxx-xxxxxx-xxxx, 13 números y caracter alfabético al final] [{cliente.identification}]: ")
            if entrada == "":
                break
            elif len(entrada) == 16 and entrada[3] == '-' and entrada[10] == '-' and entrada[:-1].replace('-', '').isdigit() and entrada[-1].isalpha():
                nueva_cedula = entrada
                break
            else:
                print("La nueva cédula no sigue el formato indicado [Formato: xxx-xxxxxx-xxxx, 13 números y caracter alfabético al final]")
        except ValueError:
            print("Caracteres inválidos, por favor ingrese el formato adecuado [Formato: xxx-xxxxxx-xxxx, 13 números y caracter alfabético al final]")
        
    while True:
        try:
            entrada = input(f"Ingrese el número telefónico del cliente [8 dígitos, sin espacios de separación] [{cliente.phone_number}]: ") 
            if entrada == "":
                break
            elif len(entrada) == 8 and entrada.isdigit():
                nuevo_numero_telefono = entrada
                break
            else:
                    print("Numero de telefono inválido. Debe de ser de 8 números y sin espacios")
        except ValueError:
                print("Carácteres inválidos. Por favor, solo ingrese numeros")
                
    entrada = input(f"Ingrese el nuevo correo electrónico del cliente [{cliente.email}]: ").strip()
    if entrada:
        nuevo_correo_elec = entrada
        
    entrada = input(f"Ingrese la nueva dirección del cliente[{cliente.address}]: ").strip()
    if entrada:
        nuevo_direccion = entrada   
        
    for cliente_existente in servicios.service:
        if cliente_existente is cliente:
            continue
        if nueva_cedula and cliente_existente.identification.lower() == nueva_cedula.lower():
            print("Ya existe otro cliente con esa cédula.")
            limpiar_pantalla()
            return
        if nuevo_numero_telefono and cliente_existente.phone_number == int(nuevo_numero_telefono):
            print("Ya existe otro cliente con ese número de teléfono.")
            limpiar_pantalla()
            return
        if nuevo_correo_elec and cliente_existente.email.lower() == nuevo_correo_elec.lower():
            print("Ya existe otro cliente con ese correo electrónico.")
            limpiar_pantalla()
            return
        
    cliente.name = nuevo_nombre
    cliente.last_name = nuevo_apellido
    cliente.identification = nueva_cedula
    cliente.phone_number = int(nuevo_numero_telefono)
    cliente.email = nuevo_correo_elec
    cliente.address = nuevo_direccion
    

    print("Cliente actualizado con éxito.")
    limpiar_pantalla()
    
def registrar_pago():
    while True:
        try:
            busqueda = input("Ingrese los 2 nombres, los 2 apellidos del cliente a buscar o la cedula:").strip()
            if not busqueda:
                print("Debe ingresar un nombre, apellido o cédula")
                continue
            buscando_cliente = buscar_cliente(busqueda)
            if buscando_cliente:
                print(f"Cliente encontrado: \n {buscando_cliente.name} {buscando_cliente.last_name} {buscando_cliente.identification}")
                registrar_pago_datos(buscando_cliente) 
                limpiar_pantalla()
                break  
            else:
                   print("El cliente no existe o no fue introducido tal y como fue guardado")
                   continuar = input("¿Desea intentar de nuevo? (s/n): ").strip().lower()
                   if continuar != 's':
                       break
        except ValueError:
               print("Error inesperado, intente nuevamente")
               limpiar_pantalla()
               break
            
def registrar_pago_datos(cliente): 
    while True:
        try:
            pago_str = input("Ingrese el pago realizado por el cliente en córdobas: ").strip().replace(',', '.')
            if not pago_str:
                print("Debe ingresar un monto")
                continue
            pago = float (pago_str)
            if pago < 737:
                print("Pago insuficiente, el pago mínimo del servicio es de 737 córdobas")
                continue
            else: 
                pago = round(pago, 2) #Voy a mandarlo a redondear hasta 2 decimales, por que demasiados en la lista
                cambio =  round(pago - 737, 2)
                descripcion = "Pago de servicio" 
                fecha = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                fecha_formateada = fecha.replace(" ", "").replace("/", "").replace(":", "") #Hace que la factura sea unica al concantenar la cedula del cliente y la fecha con lo guiones eliminados
                codigo_factura =  f"FAC-{cliente.identification}-{fecha_formateada}"
                
                
                factura = c.Bill(cliente, pago, cambio, descripcion, fecha, codigo_factura)
                registro_factura.add(factura)
                
                cliente.pagos.append({
                    'pago': pago,
                    'cambio': cambio,  #En esta parte hace que el pago, cambio y fecha sean agregados en la lista llamada pago en en el models llamado cliente
                    'fecha': fecha
                })
                
                print(f"Pago registrado. Cambio: {cambio:.2f} córdobas. Factura generada: {codigo_factura}")
                limpiar_pantalla()
                break
        except ValueError:
            print("Error, ingrese un número válido [use punto o coma para decimales si es necesario].")
            limpiar_pantalla()
            break
        
def buscar_cliente(busqueda):
    entrada = busqueda.strip().lower()
    for cliente in servicios.service:
        nombre_completo = f"{cliente.name} {cliente.last_name}".lower()
        if (entrada == cliente.identification.lower() or
            entrada == cliente.name.lower() or
            entrada == cliente.last_name.lower() or
            entrada in nombre_completo):
            return cliente
    return None

def buscar_imprimir_factura():
    while True:
        try:
            print("""
1. Buscar facturas por nombre, apellido o cédula del cliente
2. Buscar facturas por código
3. Volver al menú""")
            opcion = int(input("Ingrese la el número de la acción a realizar: "))
            
            if opcion == 1:
                busqueda = input("Ingrese los 2 nombres, los 2 apellidos del cliente a buscar o la cedula: ").strip()
                buscando_cliente = buscar_cliente(busqueda)
                if busqueda:
                    print("Cliente encontrando:")
                    print(f"{buscando_cliente.name} {buscando_cliente.last_name}  -  {buscando_cliente.identification}")
                    print("Facturas del cliente: ")
                    
                    facturas_cliente = [factura for factura in registro_factura.state if factura.client.identification == buscando_cliente.identification]
                    
                    if facturas_cliente:
                        for factura in facturas_cliente:
                            print(factura)   
                    else:
                        print("Este cliente no tiene facturas registradas.")
                        break
                else:
                    print("Cliente no encontrado.")
                    break

            elif opcion == 2:
                codigo = input("Ingrese el código de la factura a buscar: ").strip()
                factura_encontrada = next((f for f in registro_factura.state if f.code == codigo), None)

                if factura:
                    print("\nFactura encontrada:")
                    print(factura_encontrada)
                else:
                    print("No se encontró ninguna factura con ese código.")
                    break
            elif opcion == 3:
                print("Volviendo al menú principal...")
                break

            else:
                print("Opción inválida, intente de nuevo.")

        except ValueError:
            print("Entrada inválida, por favor ingrese un número.")
            
def limpiar_pantalla():
    input(f"Presione enter para continuar:")
    os.system('cls' if os.name == 'nt' else 'clear')
