class Client:
    def __init__(self, name, last_name, phone_number, email, address, plan):
        self.name = name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.plan = plan
        
    def __str__(self):
        return f"NOMBRE \t| APELLIDO \t| NÚMERO TELEFÓNICO \t| CORREO ELECTRÓNICO \t| DIRECCIÓN \t| PLAN \n{self.name} \t| {self.last_name} \t| {self.phone_number} \t| {self.email} \t| {self.address} \t| {self.plan}"  