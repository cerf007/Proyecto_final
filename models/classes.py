class Service:
    def __init__(self, name, last_name, phone_number, email, address, plan):
        self.name = name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.plan = plan
        
    def __str__(self):
        return f"Nombre: {self.name} \n Apellido: {self.last_name}, \n Número de teléfono: {self.phone_number} \n Correo electrónico: {self.email} \n Dirección: {self.address} \n Plan: "    