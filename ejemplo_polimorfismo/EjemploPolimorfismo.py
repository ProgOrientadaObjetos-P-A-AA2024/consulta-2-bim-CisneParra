def main():
    cuenta = CuentaPorPagar("Juan Pérez")

    menu1 = MenuCarta("Filete a la parrilla", 0, 25.0, 5.0, 3.0, 10)
    menu2 = MenuDia("Ensalada César", 0, 15.0, 4.0, 2.0)
    menu3 = MenuNinos("Pasta con salsa", 0, 10.0, 2.0, 1.5)
    menu4 = MenuEconomico("Hamburguesa", 0, 12.0, 20)

    cuenta.agregar_menu(menu1)
    cuenta.agregar_menu(menu2)
    cuenta.agregar_menu(menu3)
    cuenta.agregar_menu(menu4)

    print(cuenta)

if __name__ == "__main__":
    main()

class CuentaPorPagar:
    def __init__(self, nombre_cliente):
        self.nombre_cliente = nombre_cliente
        self.cartas_solicitadas = []
        self.subtotal = 0.0
        self.iva = 0.0
        self.valor_total = 0.0

    def agregar_menu(self, menu):
        self.cartas_solicitadas.append(menu)
        self.subtotal += menu.valor_menu
        self.iva = self.subtotal * 0.19  # Supongamos un IVA del 19%
        self.valor_total = self.subtotal + self.iva

    def __str__(self):
        return (f"Cliente: {self.nombre_cliente}\n"
                f"Subtotal: {self.subtotal:.2f}\n"
                f"IVA: {self.iva:.2f}\n"
                f"Total a pagar: {self.valor_total:.2f}\n"
                f"Menús solicitados: {[str(menu) for menu in self.cartas_solicitadas]}")
class Menu:
    def __init__(self, nombre_plato, valor_menu, valor_inicial):
        self.nombre_plato = nombre_plato
        self.valor_menu = valor_menu
        self.valor_inicial = valor_inicial

    def __str__(self):
        return f"{self.nombre_plato} - Valor: {self.valor_menu:.2f}"
class MenuCarta(Menu):
    def __init__(self, nombre_plato, valor_menu, valor_inicial, valor_guarnicion, valor_bebida, porcentaje_servicio):
        super().__init__(nombre_plato, valor_menu, valor_inicial)
        self.valor_guarnicion = valor_guarnicion
        self.valor_bebida = valor_bebida
        self.porcentaje_servicio = porcentaje_servicio
        self.calcular_valor_menu()

    def calcular_valor_menu(self):
        self.valor_menu = self.valor_inicial + self.valor_guarnicion + self.valor_bebida + (self.valor_inicial * self.porcentaje_servicio / 100)

    def __str__(self):
        return (f"Menú a la Carta: {self.nombre_plato} - Valor: {self.valor_menu:.2f} "
                f"(Guarnición: {self.valor_guarnicion:.2f}, Bebida: {self.valor_bebida:.2f})")
class MenuDia(Menu):
    def __init__(self, nombre_plato, valor_menu, valor_inicial, valor_postre, valor_bebida):
        super().__init__(nombre_plato, valor_menu, valor_inicial)
        self.valor_postre = valor_postre
        self.valor_bebida = valor_bebida
        self.calcular_valor_menu()

    def calcular_valor_menu(self):
        self.valor_menu = self.valor_inicial + self.valor_postre + self.valor_bebida

    def __str__(self):
        return (f"Menú del Día: {self.nombre_plato} - Valor: {self.valor_menu:.2f} "
                f"(Postre: {self.valor_postre:.2f}, Bebida: {self.valor_bebida:.2f})")
class MenuNinos(Menu):
    def __init__(self, nombre_plato, valor_menu, valor_inicial, valor_helado, valor_pastel):
        super().__init__(nombre_plato, valor_menu, valor_inicial)
        self.valor_helado = valor_helado
        self.valor_pastel = valor_pastel
        self.calcular_valor_menu()

    def calcular_valor_menu(self):
        self.valor_menu = self.valor_inicial + self.valor_helado + self.valor_pastel

    def __str__(self):
        return (f"Menú de Niños: {self.nombre_plato} - Valor: {self.valor_menu:.2f} "
                f"(Helado: {self.valor_helado:.2f}, Pastel: {self.valor_pastel:.2f})")
class MenuEconomico(Menu):
    def __init__(self, nombre_plato, valor_menu, valor_inicial, porcentaje_descuento):
        super().__init__(nombre_plato, valor_menu, valor_inicial)
        self.porcentaje_descuento = porcentaje_descuento
        self.calcular_valor_menu()

    def calcular_valor_menu(self):
        self.valor_menu = self.valor_inicial - (self.valor_inicial * self.porcentaje_descuento / 100)

    def __str__(self):
        return (f"Menú Económico: {self.nombre_plato} - Valor: {self.valor_menu:.2f} "
                f"(Descuento: {self.porcentaje_descuento}%)")
