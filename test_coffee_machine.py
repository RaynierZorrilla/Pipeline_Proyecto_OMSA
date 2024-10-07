import unittest
from coffee_machine import CoffeeMachine

class TestCoffeeMachine(unittest.TestCase):

    def setUp(self):
        # Inicializar la máquina con 10 vasos, 100 Oz de café, y 50 cucharadas de azúcar
        self.machine = CoffeeMachine(vasos=10, cafe=100, azucar=50)
    
    def test_seleccionar_tamano_pequeno(self):
        result = self.machine.seleccionar_tamano('pequeño')  # Cambia a 'pequeño' con tilde
        self.assertEqual(result, "Vaso pequeño seleccionado")

    def test_seleccionar_tamano_mediano(self):
        result = self.machine.seleccionar_tamano('mediano')
        self.assertEqual(result, "Vaso mediano seleccionado")
        
    def test_seleccionar_tamano_grande(self):
        result = self.machine.seleccionar_tamano('grande')
        self.assertEqual(result, "Vaso grande seleccionado")

    def test_seleccionar_azucar(self):
        result = self.machine.seleccionar_azucar(2)
        self.assertEqual(result, "2 cucharadas de azúcar seleccionadas")
    
    def test_no_hay_vasos(self):
        self.machine.vasos = 0
        result = self.machine.dispensar_cafe()
        self.assertEqual(result, "No hay vasos disponibles")

    def test_no_hay_cafe(self):
        self.machine.seleccionar_tamano('mediano')  # Selecciona un tamaño de vaso
        self.machine.cafe = 0
        result = self.machine.dispensar_cafe()
        self.assertEqual(result, "No hay café disponible")

    def test_no_hay_azucar(self):
        self.machine.seleccionar_tamano('mediano')  # Selecciona un tamaño de vaso
        self.machine.azucar = 0
        result = self.machine.dispensar_cafe()
        self.assertEqual(result, "No hay azúcar disponible")
        
    def test_dispensar_cafe_correcto(self):
        self.machine.seleccionar_tamano('mediano')
        self.machine.seleccionar_azucar(2)
        result = self.machine.dispensar_cafe()
        self.assertEqual(result, "Café de tamaño mediano con 2 cucharadas de azúcar servido")
    
if __name__ == '__main__':
    unittest.main()
