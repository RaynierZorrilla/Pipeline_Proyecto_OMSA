class CoffeeMachine:
    def __init__(self, vasos, cafe, azucar):
        self.vasos = vasos
        self.cafe = cafe
        self.azucar = azucar
        self.tamano_seleccionado = None
        self.tamano_nombre = None  # Nueva variable para almacenar el nombre del tamaño
        self.azucar_seleccionada = 0

    def seleccionar_tamano(self, tamano):
        tamanos = {
            'pequeño': 3,
            'mediano': 5,
            'grande': 7
        }
        
        if tamano in tamanos:
            self.tamano_seleccionado = tamanos[tamano]
            self.tamano_nombre = tamano  # Almacenar el nombre del tamaño seleccionado
            return f"Vaso {tamano} seleccionado"
        return "Tamaño no válido"

    def seleccionar_azucar(self, cantidad):
        if cantidad <= self.azucar:
            self.azucar_seleccionada = cantidad
            return f"{cantidad} cucharadas de azúcar seleccionadas"
        return "No hay suficiente azúcar disponible"

    def dispensar_cafe(self):
        if self.vasos == 0:
            return "No hay vasos disponibles"
        if self.cafe < self.tamano_seleccionado:
            return "No hay café disponible"
        if self.azucar_seleccionada == 0:
            return "No hay azúcar disponible"  # Verifica si se ha seleccionado azúcar

        if self.azucar_seleccionada > self.azucar:
            return "No hay azúcar disponible"

        # Si hay suficientes recursos, servir el café
        self.vasos -= 1
        self.cafe -= self.tamano_seleccionado
        self.azucar -= self.azucar_seleccionada
        return f"Café de tamaño {self.tamano_nombre} con {self.azucar_seleccionada} cucharadas de azúcar servido"