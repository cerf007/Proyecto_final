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
        encabezado = (
            f"{'NOMBRE':<25} | "
            f"{'APELLIDO':<25} | "
            f"{'CÉDULA':<18} | "
            f"{'TELÉFONO':<12} | "
            f"{'EMAIL':<28} | "
            f"{'DIRECCIÓN':<20}"
        )
        datos = (
            f"{self.name:<25} | "
            f"{self.last_name:<25} | "
            f"{self.identification:<18} | "
            f"{self.phone_number:<12} | "
            f"{self.email:<28} | "
            f"{self.address:<20}"
        )
        return f"{encabezado}\n{datos}"
    
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