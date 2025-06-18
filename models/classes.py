class Client:
    def __init__(self, name, last_name, identification, phone_number, email, address, plan):
        self.name = name
        self.last_name = last_name
        self.identification = identification
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.plan = plan
        self.pagos = [] #se agreego una lista para registrar los pagos del cliente
        
    def __str__(self):
        return f"NOMBRE \t| APELLIDO \t| CÉDULA \t|NÚMERO TELEFÓNICO \t| CORREO ELECTRÓNICO \t| DIRECCIÓN \t| PLAN \n{self.name} \t| {self.last_name} \t| {self.identification}| {self.phone_number} \t| {self.email} \t| {self.address} \t| {self.plan}"  
    
    