class Client:
    def __init__(self, name, last_name, identification, phone_number, email, address):
        self.name = name
        self.last_name = last_name
        self.identification = identification
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.pagos = [] #se agreego una lista para registrar los pagos del cliente
        
    def __str__(self):
        return f"NOMBRE \t| APELLIDO \t| CÉDULA \t|NÚMERO TELEFÓNICO \t| CORREO ELECTRÓNICO \t| DIRECCIÓN \t|\n{self.name} \t| {self.last_name} \t| {self.identification}| {self.phone_number} \t| {self.email} \t| {self.address} \t"  
    
    #def display_payments(self):
    #    print("Pagos:")
    #    for pago in self.pagos:
    #        print(f"Pago: {pago['pago']}, Cambio: {pago['cambio']}, Fecha: {pago['fecha']}")
    
class Bill:
    def __init__(self, client,payment, change ,description, date, code):
        self.client = client
        self.payment = payment
        self.change = change
        self.description = description
        self.date =  date
        self.code = code
        
    def __str__(self):
        return (f"\t NOMBRE: {self.client.name} \t\n"
                f"\t APELLIDO: {self.client.last_name} \t\n"
                f"\t PAGO: {self.payment} \t\n"
                f"\t CAMBIO: {self.change} \t\n"
                f"\t DESCRIPCIÓN: {self.description} \t\n"
                f"\t FECHA Y HORA: {self.date} \t\n"
                f"\t NUMERO DE FACTURA: {self.code} \t\n")