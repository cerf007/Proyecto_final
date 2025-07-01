import models.classes as c
import dao.functions as f
import datetime
import os
import pwinput

 
servicios = f.ClientDao() 
registro_factura = f.BillDao()
usuarios = f.UserDao()

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
8.Registrar usuario
9.Mostrar usuario
10.Eliminar usuario
11.Salir
""")
#Esta función solo imprime el menú y sus opciones
    
def main():
    while True:
        try:
            empleado = input("Usuario: ")
            password = pwinput.pwinput(prompt="Contraseña: ", mask="*")
            if usuarios.authenticate(empleado, password):
                limpiar_pantalla()
                while True:
                    try:
                        menu()
                        opcion = int(input("Ingrese la opcion: ")) # Aquí le pedimos al usuario un número correspondiente a la acción a realizar
                        if opcion == 1:
                            registrar_cliente()
                        elif opcion == 2:
                            servicios.show()
                            limpiar_pantalla()
                        elif opcion == 3:
                            editar_cliente()
                        elif opcion == 4:
                           eliminar_cliente()
                        elif opcion == 5:
                            registrar_pago()
                        elif opcion == 6:
                            generar_reporte_financiero()
                        elif opcion == 7:
                            buscar_imprimir_factura()
                        elif opcion == 8:
                            registrar_usuario()
                        elif opcion == 9:
                            mostrar_usuarios()
                        elif opcion == 10:
                            eliminar_usuario()
                        elif opcion == 11:
                            print("Saliendo....")
                            return
                        else:
                            print("Opción inválida, ingrese un número del 1 al 8") # En caso de que pongan una opción les aparece este mensaje y pide el número de nuevo
                    except ValueError:
                        print("Entrada no válida. Por favor, ingrese un número.")#En caso de error desconocido aparece esto, permitiendo que el programa continue sin cerrarse
            else:
                print("Clave de acceso incorrecto")#En caso de que la contraseña sea incorrecta, le saldría esto
                continue# con el continue le sigue pidiendo la contraseña
        except ValueError:
            print("Error inesperado")#En caso de error desconocido aparece esto, permitiendo que el programa continue sin cerrarse
            
def registrar_cliente():
    while True:
        try:
            nombres = input("Ingrese los 2 nombres del cliente: ").strip()#Pide los nombres y borra los espacios de al inicio y al final en caso de que haya alguno
            if not nombres:
                print("No puede haber una entrada de datos vacía")#Esto imprime si detecta que solo se dio enter y no se ingresó nada
                continue # Esto le permite pedir de nuevo el nombre
            elif all(part.isalpha() for part in nombres.split()):#Aqui verifica si todo lo escrito fueron caracteres alfabeticos y separa las 2 cadenas con el split en base a los espacios
                nombres = nombres.lower() #Pasa todo a minuscula en caso de que el usario las ponga mayusculas y minusculas intercalas
                nombres = nombres.title() # Pasa el primer caracter de cada cadena a una mayuscula
                break # En caos de que todo este bien, lo pasa al siguiente, que es el apellido
            else:
                print("Los nombres solo deben contener caracteres alfabéticas")#Si la validación no resultó, imprime esto y pide el nombre nuevameno
        except ValueError:
            print("Error, caracteres inválidos")#Imprime esto en caso de errores inesperados
            
    while True:#Es lo mismo que lo de nombres, cada parte. El valor que pide ahora es el apellido
        try:
            apellidos = input("Ingrese los 2 apellidos del cliente: ").strip()
            if not apellidos:
                print("No puede haber una entrada de datos vacía")
                continue
            elif all(part.isalpha() for part in apellidos.split()):
                apellidos = apellidos.lower()
                apellidos = apellidos.title()
                break
            else:
                print("Los apeellidos solo deben de contener caracteres alfabéticos ")
        except  ValueError:
            print("Error, caracteres inválidos")
    
    #agregando cédula como identificador
    while True:
        try:
            cedula_str = input("Ingrese la cédula del cliente [Formato = xxx-xxxxx-xxxx, 13 digitos númericos y 1 letra al final]: ").strip() #El strip quita todo los espacios del inicio y al final
            if not cedula_str:
                print("No puede haber una entrada de datos vacía") # Imprime esto en caso de que el usuario no ingrese nada
                continue #Le permite reiniciar el programa, sin pasar a las siguientes validaciones
            if (len(cedula_str) == 16 and cedula_str[3] == '-' and cedula_str[10] == '-' and cedula_str[:-1].replace('-', '').isdigit() and cedula_str[-1].isalpha()):
                
                #El if detecta si lo ingresado fueron 16 caracteres, si el caracter 3er y 10mo son guiones, agarra todos los carecteres menos ultimo y reemplaza los guiones por espacios eliminados para detectar si el resto ingresado son dígitos. Por ultimo, detecta si el último caracter es alfabetico
                
                
                cedula_str =  cedula_str[:-1] + cedula_str[-1].upper() 
                #Une una cadena con todos los caracteres menos el último con el último caracter en mayuscula en caso de que haya sido introducido con miniscula
                break
            #Si todo sale bien, hace el break y pide el número de teléfono sino le imprime lo que está en el else
            else:
                print("Numero de cédula inválido. El formato introducido es inválido")
        except ValueError:
            print("Caracteres inválidos. Por favor, solo ingrese el formato adecuado [Formato: xxx-xxxxxx-xxxx, 13 números y caracter alfabético al final]") #Esto solo es en caso de un error inesperado
        
            
    while True:
        try:
            numero_telefono_str = input("Ingrese el número telefónico del cliente [8 dígitos, sin espacios de separación]: ").strip() # Ya sabemos para que se usa el strip
            if not numero_telefono_str:
                print("No puede haber una entrada de datos vacía")
                #Esto es solo si el usuario no ingresa nada y con el continue reinicia este bucle
                continue
            elif len(numero_telefono_str) == 8 and numero_telefono_str.isdigit():
                #Detecta si los caracteres ingresados son exactamente 8 y si son digitos númericos
                numero_telefono = int(numero_telefono_str)# Pasa de string a integer (número entero) y pasa a la siguiente
                break
            else:
                #Si no se ingresaron números o el número de caracteres no es igual a 8, les imprime esto, y pide de nuevo el número
                print("Numero de telefono inválido. Debe de ser de 8 números y sin espacios")
        except ValueError:
            print("Carácteres inválidos. Por favor, solo ingrese numeros")# Esto solo es en caso de que haya un error inesperado
    
    while True:
        try:        
            correo_elec = input("Ingrese el correo electrónico del cliente: ").strip()#Ya sabemos que es el strip
            if not correo_elec:
                print("No puede haber una entrada de datos vacía") #Aqui sabemos que vuelve a pedir el código si el usuario no ingresó nada
                continue
            correo_elec = correo_elec.lower() #Si esta bueno, pasa todo el correo en minusculas
            if "@" not in correo_elec or "." not in correo_elec.split("@")[-1]:
                #Si el correo no contiene el @ o no contiene el . despues del arroba le sale el mensaje y vuelve a pedir el correo
                print("Correo electrónico inválido, debe contener @ y un punto después de @")                
                continue
            else:
                break
            #Si todo esta correcto, hace el break para salir de bucle e ir al siguiente
        
        except ValueError:
            print("Carácteres inválidos") # En caso de errores inesperados
      
    while True:
        try:  
            direccion = input("Ingrese la dirección del cliente: ").strip()
            if not direccion: #Esto hace lo mismo que los anteriores
                print("No puede haber una entrada de datos vacía")
                continue
            else:
                direccion = direccion.title() #Capitaliza la 1ra palabra en caso de que no lo haya sido
                break# Si todo esta bien, lo manda al sig modulo
        except ValueError:
            print("Carácteres inválidos")# Solo si hay errores inesperados
            
    for cliente in servicios.service:
        if cliente.identification.lower() == cedula_str.lower():
            print("Ya existe un cliente con esa cédula.")
            limpiar_pantalla()
            return
        if cliente.phone_number == numero_telefono:
            print("Ya existe un cliente con ese número telefónico.")
            limpiar_pantalla()
            return
        if cliente.email.lower() == correo_elec.lower():
            print("Ya existe un cliente con ese correo electrónico.")
            limpiar_pantalla()
            return
    #Esa iteración de for hace el trabajo de que si la cédula, número de telefono o el correo del cliente ya esta registrado, si es así no lo permite guardar, evtando duplicados
    
    registrar = c.Client(nombres, apellidos, cedula_str ,numero_telefono, correo_elec, direccion) 
    #Condensa todo lo que se va a guardar para evitar escribir todo eso en el parentesis del servicios.add()
    servicios.add(registrar) # Guarda todos los datos de un cliente
    limpiar_pantalla()#Limpia pantalla luego de finalizar el módulo, para evitar datos anteriores ocupen más espacios
    
def eliminar_cliente():
    while True:
        try:
            busqueda = input("Ingrese los 2 nombres, los 2 apellidos del cliente a buscar o la cedula: ").strip()
            if not busqueda:
                print("Debe ingresar el nombre, el apellido o la cédula")# Si no se ingresa nada, hace break y lo saca de la función
                break
            buscando_cliente = buscar_cliente(busqueda) # Hace la busqueda cliente y ve si coincide
            if buscando_cliente:
                servicios.delete(buscando_cliente) #Llama la función delete del dao y elimina los registros de factura
                facturas_a_eliminar = [factura for factura in registro_factura.state if factura.client.identification == buscando_cliente.identification]
                for factura in facturas_a_eliminar:
                    registro_factura.delete(factura) # Elimina al cliente y todos sus datos personales
                print(f"Cliente {buscando_cliente.name} {buscando_cliente.last_name} eliminado.") #Imprime nombre y apellido del cliente eliminado
                limpiar_pantalla()
                break
            else:
                print("Cliente no encontrado.") 
                # En caso de que nombre, apellido, cédula o nombre completo no coincidan en la búsqueda
                limpiar_pantalla()
                break
        except ValueError:
            print("Entrada no válida, intenté de nuevo")# En caso de que haya error inesperado
            limpiar_pantalla()
            break
            
def editar_cliente():
     while True:
           try:
               busqueda = input("Ingrese los 2 nombres, los 2 apellidos del cliente a buscar o la cedula: ").strip() 
               #Busca por nombe, apellido o cédula
               if not busqueda:
                   print("Debe ingresar el nombre, el apellido o la cédula")
                   limpiar_pantalla()
                   break
               #Hace esto en caos de que no se ingrese nada
               buscando_cliente = buscar_cliente(busqueda)
               #Hace la busqueda del cliente, si es encontrado hace el siguiente if
               if buscando_cliente:
                        print("Cliente encontrado:")
                        print(buscando_cliente)
                        editar_nuevo_cliente(buscando_cliente)
                        limpiar_pantalla()
                        break
                    #Imprime los datos del cliente y llama a la función para editar el cliente si todo esta bien sale del bucle y lo manda al menú principal
               else: 
                   print("Cliente no encontrado") #Hace esto si lo ingresado no coincide con lo lo registrado en el clientes.bin
                   limpiar_pantalla()
                   break
           except ValueError:
               print("Error inesperado al ingresar datos")#Solo en caso de un error inesperado
               limpiar_pantalla()
               break

def editar_nuevo_cliente(cliente):
    nuevo_nombre = None
    nuevo_apellido = None
    nueva_cedula = None
    nuevo_numero_telefono = None
    nuevo_correo_elec = None
    nuevo_direccion = None
    #Inicializa variables temporales para guardar los posibles datos modificados del cliente, construyendo un diccionario con solo los campos que no son None y se actualizan en el objeto cliente.

    while True:
        try:
            entrada = input(f"Ingrese los 2 nuevos nombres del cliente [{cliente.name}]: ").strip()
            if entrada == "": 
                # Si el usario solo da enter, no realiza ningún cambio y queda igual, lo mismo para todos en los siguientes modulos de esta función
                break 
            elif  all(part.isalpha() for part in entrada.split()):
                nuevo_nombre = entrada.lower()
                nuevo_nombre = nuevo_nombre.title()
                break
            else:
                print("Los nombres solo deben contener caracteres alfabéticas")
        except ValueError:
            print("Error, caracteres inválidos")
            #Hace lo mismo que la función de registrar_cliente con unas cuantas modificaciones, lo mismo va para los siguientes bucles
        
        
    while True:
        try:
            entrada = input(f"Ingrese los 2 nuevos apellidos del cliente [{cliente.last_name}]: ")
            if entrada == "":
                break
            elif  all(part.isalpha() for part in entrada.split()):
                nuevo_apellido = entrada.title()
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
                nueva_cedula = entrada[:-1] + entrada[-1].upper()
                break
            else:
                print("La nueva cédula no sigue el formato indicado [Formato: xxx-xxxxxx-xxxx, 13 números y caracter alfabético al final]")
        except ValueError:
            print("Caracteres inválidos, por favor ingrese el formato adecuado")
        
    while True:
        try:
            entrada = input(f"Ingrese el número telefónico del cliente [8 dígitos, sin espacios de separación] [{cliente.phone_number}]: ") 
            if entrada == "":
                break
            elif len(entrada) == 8 and entrada.isdigit():
                nuevo_numero_telefono = int(entrada)
                break
            else:
                    print("Numero de telefono inválido. Debe de ser de 8 números y sin espacios")
        except ValueError:
                print("Carácteres inválidos. Por favor, solo ingrese numeros")
       
    while True:
        try:            
            entrada = input(f"Ingrese el nuevo correo electrónico del cliente [{cliente.email}]: ").strip()
            if entrada == "":
                break
            entrada = entrada.lower()
            if "@" not in entrada or "." not in entrada.split("@")[-1]:
                print("Correo electrónico inválido, debe contener @ y un punto después de @")
                continue
            else:
                nuevo_correo_elec = entrada
                break
        except ValueError:
            print("Carácteres inválidos")

    while True:
        try:
            entrada = input(f"Ingrese la nueva dirección del cliente [{cliente.address}]: ").strip()
            if entrada == "":
                break
            nuevo_direccion = entrada.title()
            break
        except ValueError:
            print("Carácteres inválidos")
        
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
        #Este verifica si la cédula, el numero de teléfono o el correo electrónico ya esta regsitrado en algún otro cliente
        
    datos_a_modificar = {} # Esta linea crea un diccionario vacío
    if nuevo_nombre:
        datos_a_modificar['name'] = nuevo_nombre 
        # Si el usuario escribió un nuevo nombre se agrega al diccionario con la clave 'name', este patrón se repite para todos los demás campos.
    if nuevo_apellido:
        datos_a_modificar['last_name'] = nuevo_apellido
    if nueva_cedula:
        datos_a_modificar['identification'] = nueva_cedula
    if nuevo_numero_telefono:
        datos_a_modificar['phone_number'] = nuevo_numero_telefono
    if nuevo_correo_elec:
        datos_a_modificar['email'] = nuevo_correo_elec
    if nuevo_direccion:
        datos_a_modificar['address'] = nuevo_direccion

    servicios.update(cliente, datos_a_modificar)
    #Hace que mi dao recorra el diccionario y reemplace únicamente esos campos dentro del objeto cliente.
    print("Cliente actualizado con éxito.")
    
def registrar_pago():
    while True:
        try:
            busqueda = input("Ingrese los 2 nombres, los 2 apellidos del cliente a buscar o la cedula:").strip()
            if not busqueda:
                print("Debe ingresar un nombre, apellido o cédula")#Si no pone nada, manda este mensaje 
                continue
            buscando_cliente = buscar_cliente(busqueda) 
            # Llama la función buscar_cliente y busca coincidencias del clientes
            if buscando_cliente:# Si se encuentran coincidencias llama la función registrar pagos
                print(f"Cliente encontrado: \n {buscando_cliente.name} {buscando_cliente.last_name} {buscando_cliente.identification}")
                registrar_pago_datos(buscando_cliente) 
                limpiar_pantalla()
                break  
            else:
                   print("El cliente no existe o no fue introducido tal y como fue guardado")
                   continuar = input("¿Desea intentar de nuevo? (s/n): ").strip().lower() # Si no se encuentra, pide s o n para continuar con la acción
                   if continuar != 's':
                       break
        except ValueError:
               print("Error inesperado, intente nuevamente") # Solo es por si hay un error inesperado
               limpiar_pantalla()
               break

def registrar_pago_datos(cliente): 
    while True:
        try:
            pago_str = input("Ingrese el pago realizado por el cliente en córdobas: ").strip().replace(',', '.')
            #Pide el monto y reemplaza cada coma con un punto, en caso de que el usuario prefiera las comas sobre el punto al representer decimales
            if not pago_str:
                print("Debe ingresar un monto")
                #Si no hay nada ingresado, le imprime eso y pide nuevamente el monto
                continue
            pago = float (pago_str)
            # hace una variable llamada pago conviertiendo de str a float la variable pago_str
            if pago < 737:
                print("Pago insuficiente, el pago mínimo del servicio es de 737 córdobas")
                # Si es insuficiente el pago, imprime el mensaje  y lo pide de nuevo
                continue
            else: 
                pago = round(pago, 2) #Redondea a  2 decimales el pago en caso de que sean muchos
                cambio =  round(pago - 737, 2)#Hace el calculo de cambio y redondea a 2 decimales
                descripcion = "Pago de servicio" 
                fecha = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S") 
                #Formato de fecha, hora, minuto y segundo para almacenar
                fecha_formateada = fecha.replace(" ", "").replace("/", "").replace(":", "") #Hace que la factura sea unica al concantenar la cedula del cliente y la fecha con lo guiones, las barras y los : eliminados
                codigo_factura =  f"FAC-{cliente.identification}-{fecha_formateada}"
                #Concatena la cédula y la fecha formateada 
                
                factura = c.Bill(cliente, pago, cambio, descripcion, fecha, codigo_factura)
                #Indica todas las varibles que se deben guardar
                registro_factura.add(factura) #Los guardan en el facturas.bin
                
                cliente.pagos.append({
                    'pago': pago,
                    'cambio': cambio,  #En esta parte hace que el pago, cambio y fecha sean agregados en la lista llamada pago en en el models llamado cliente
                    'fecha': fecha
                })
                
                print(f"Pago registrado. Cambio: {cambio:.2f} córdobas. Factura generada: {codigo_factura}")
                break
            #Si todo fue hecho bien, muestra el cambio y el código de factura
        except ValueError:
            print("Error, ingrese un número válido [use punto o coma para decimales si es necesario].") 
            #Solo por un error imprevisto
            limpiar_pantalla()
            break
        
def buscar_cliente(busqueda):
    entrada = busqueda.strip().lower()
    # Recorre todos los clientes de servicios.service y construye el nombre completo (nombre + apellido) en minúsculas, para hacer búsquedas uniformes.
    if not entrada:
        return None
    for cliente in servicios.service:
        nombre_completo = f"{cliente.name} {cliente.last_name}".lower()  
        if (entrada == cliente.identification.lower() or #coincidencie exacta con la cédula
            entrada == cliente.name.lower() or # coincidencia exacta con el nombre
            entrada == cliente.last_name.lower() or #coincdencia exacta con el apellidod
            entrada in nombre_completo): #concidencia parcial del nombre
            return cliente #Devuelve el cliente si encuentra coincidencia
    return None

def buscar_imprimir_factura():
    while True:
        try:
            print("""
1. Buscar facturas por nombre, apellido o cédula del cliente 
2. Buscar facturas por código
3. Volver al menú""")
            #Muestra 3 opciones
            opcion = int(input("Ingrese el número de la acción a realizar: "))
            
            if opcion == 1: # Si la opcion es 1
                busqueda = input("Ingrese los 2 nombres, los 2 apellidos del cliente a buscar o la cedula: ").strip() 
                #Pide nombre, apellido o cédula
                if not busqueda:
                    print("Debe ingresar un dato para buscar.")#Si no hay nada ingresado, manda este mensaje e inicia de nuevo el bucle con el continue
                    continue
                
                buscando_cliente = buscar_cliente(busqueda) #Hace la búsqueda del cliente
                if buscando_cliente: # Si es encontrada hace lo siguiente
                    print("Cliente encontrado:")
                    print(f"{buscando_cliente.name} {buscando_cliente.last_name}  -  {buscando_cliente.identification}") 
                    print("Facturas del cliente: ")
                    
                    facturas_cliente = [factura for factura in registro_factura.state if factura.client.identification == buscando_cliente.identification]
                    #Recorre todas las facturas almacenadas en registro_factura.state. Toma cada factura y la evalúa con  con la cédula del cliente que se encontró con buscar_cliente.
                    if facturas_cliente:
                        for factura in facturas_cliente:
                            print(factura)   #Imprime las facturas "filtrada"
                    else:
                        print("Este cliente no tiene facturas registradas.") #En caso de que no haya facturas a nombre de ese cliente
                else:
                    print("Cliente no encontrado.")#En caso de que no se haya encontrado el cliente
                    
                limpiar_pantalla()

            elif opcion == 2: # Si la opción fue 2
                codigo = input("Ingrese el código de la factura a buscar: ").strip() #Pide el código de la facturas
                if not codigo:
                    print("Debe ingresar un código para buscar.")
                    #Si no pusieron nada, imprime esta linea y pide de nuevo
                    continue
                
                factura_encontrada = next((f for f in registro_factura.state if f.code == codigo), None)
                #Recorre todas las facturas guardadas en registro_factura.state y va produciendo solo aquellas cuyo código f.code coincide exactamente con el codigo que el usuario introdujo. La función next() obtiene el primer elemento de ese generador. Si no encuentra ninguna factura que coincida, devuelve el valor por defecto None.

                if factura_encontrada:
                    print("\nFactura encontrada:")
                    print(factura_encontrada) #Imprime la factura con el código introducido y sus detalles
                else:
                    print("No se encontró ninguna factura con ese código.")#Si no se encontró, imprime esto y llama a limpiar pantalla
                    
                limpiar_pantalla()
                
            elif opcion == 3: #Si fuera 3
                print("Volviendo al menú principal...") #Hace break y lo manda al menu principal
                limpiar_pantalla()
                break

            else:
                print("Opción inválida, intente de nuevo.")# Imprime en caso de que se ingrese un dato no permitido

        except ValueError:
            print("Entrada inválida, por favor ingrese un número.") #Solo en caso de algún error inesperado
            
def generar_reporte_financiero():
    total_ingresos = 0 # Inicia contadores de cambios y de ingresos en 0
    total_cambios = 0
    total_facturas = len(registro_factura.state) #Lee la cantidad de facturas que hay
    
    if total_facturas == 0:
        print("No hay facturas registradas hasta el momento.")# Si no hay facturas, imprime esto y lo manda al menú
        limpiar_pantalla()
        return
    
    print("\n=== Reporte Financiero ===")
    print(f"Total de facturas emitidas: {total_facturas}") # Muestra el total de facturas contadas
    print("\nDetalle de facturas:")

    for factura in registro_factura.state:
        print(factura)
        total_ingresos += factura.payment
        total_cambios += factura.change
        #Recorre cada elemento dentro de registro_factura.state
        #total_ingresos += factura.payment: va sumando cada pago registrado en cada factura para calcular el total recaudado.
        #total_cambios += factura.change: va sumando los cambios devueltos a los clientes, para saber cuánto cambio se entregó.
        
    print("\n=== Resumen ===")
    print(f"Total recaudado (sin cambios): {total_ingresos:.2f} córdobas") 
    print(f"Total de cambios entregados: {total_cambios:.2f} córdobas")
    print(f"Ingreso neto: {total_ingresos - total_cambios:.2f} córdobas")
    #Lo imprime con formato de 2 decimales el total recaudado, el cambio y el ingreso
    
    limpiar_pantalla()
            
def limpiar_pantalla():
    input(f"Presione enter para continuar:")
    os.system('cls' if os.name == 'nt' else 'clear')
    # El input sirve para darle tiempo de leer la pantalla antes de limpiar al presionar enter
    #Esto limpia la consola, para que la siguiente interacción comience en limpio
    
def registrar_usuario():
    clave_admin = "admin456"
    clave_ingresada = pwinput.pwinput("Ingrese la clave de administrador para autorizar la creación de usuario: ", mask="*")
    
    if clave_ingresada != clave_admin:
        print("Clave de administrador incorrecta. No se puede registrar el usuario.")
        return
    
    username = input("Ingrese el nuevo nombre de usuario: ").strip()
    password = pwinput.pwinput("Ingrese la contraseña nueva: ", mask="*").strip()
    
    if not username or not password:
        print("Usuario o contraseña no pueden estar vacíos.")
        return
    
    if any(u.username == username for u in usuarios.users):
        print("Ese usuario ya existe.")
        return
    
    nuevo_usuario = c.User(username, password)
    usuarios.add(nuevo_usuario)
    print(f"Usuario {username} agregado con éxito.")
    
def mostrar_usuarios():
    if not usuarios.users:
        print("No hay usuarios registrados.")
        return
    print("\n--- Lista de Usuarios ---")
    for i, u in enumerate(usuarios.users, 1):
        print(f"{i}. {u.username}")
    print()
    
def eliminar_usuario():
    clave_admin = "admin456"
    clave_ingresada = pwinput.pwinput("Ingrese la clave de administrador para autorizar la eliminación de usuario: ", mask="*")
    
    if clave_ingresada != clave_admin:
        print("Clave de administrador incorrecta. No se puede eliminar el usuario.")
        return
    
    mostrar_usuarios()
    if not usuarios.users:
        return  # Si no hay usuarios, salimos
    
    username = input("Ingrese el nombre de usuario que desea eliminar: ").strip()
    for u in usuarios.users:
        if u.username == username:
            confirmacion = input(f"¿Está seguro de eliminar al usuario '{username}'? (s/n): ").strip().lower()
            if confirmacion == 's':
                usuarios.users.remove(u)
                usuarios.save()
                print(f"Usuario '{username}' eliminado correctamente.")
            else:
                print("Eliminación cancelada.")
            return
    print("Usuario no encontrado.")
