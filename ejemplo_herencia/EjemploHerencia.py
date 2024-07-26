def main():
    prestamos = []

    while True:
        tipo_prestamo = input("Ingrese el tipo de préstamo (automóvil/educativo) o 'salir' para terminar: ").strip().lower()
        if tipo_prestamo == 'salir':
            break
        
        nombre = input("Nombre del beneficiario: ")
        apellido = input("Apellido del beneficiario: ")
        identificacion = input("Identificación del beneficiario: ")
        beneficiario = Persona(nombre, apellido, identificacion)

        tiempo_prestamo_meses = int(input("Tiempo de préstamo en meses: "))
        ciudad = input("Ciudad del préstamo: ")

        if tipo_prestamo == 'automóvil':
            tipo_automovil = input("Tipo de automóvil: ")
            marca = input("Marca de automóvil: ")
            garante_nombre = input("Nombre del garante: ")
            garante_apellido = input("Apellido del garante: ")
            garante_identificacion = input("Identificación del garante: ")
            garante1 = Persona(garante_nombre, garante_apellido, garante_identificacion)
            valor_automovil = float(input("Valor del automóvil: "))
            prestamo = PrestamoAutomovil(beneficiario, tiempo_prestamo_meses, ciudad, tipo_automovil, marca, garante1, valor_automovil)

        elif tipo_prestamo == 'educativo':
            nivel_estudio = input("Nivel de estudio: ")
            nombre_institucion = input("Nombre de la institución educativa: ")
            siglas_institucion = input("Siglas de la institución educativa: ")
            centro_educativo = InstitucionEducativa(nombre_institucion, siglas_institucion)
            valor_carrera = float(input("Valor de la carrera: "))
            prestamo = PrestamoEducativo(beneficiario, tiempo_prestamo_meses, ciudad, nivel_estudio, centro_educativo, valor_carrera)

        prestamos.append(prestamo)

    print("\nLista de préstamos:")
    for p in prestamos:
        print(p)

if __name__ == "__main__":
    main()

class Persona:
    def __init__(self, nombre, apellido, identificacion):
        self.nombre = nombre
        self.apellido = apellido
        self.identificacion = identificacion

    def __str__(self):
        return f"{self.nombre} {self.apellido} (ID: {self.identificacion})"
class InstitucionEducativa:
    def __init__(self, nombre, siglas):
        self.nombre = nombre
        self.siglas = siglas

    def __str__(self):
        return f"{self.nombre} ({self.siglas})"
class Prestamo:
    def __init__(self, beneficiario, tiempo_prestamo_meses, ciudad):
        self.beneficiario = beneficiario
        self.tiempo_prestamo_meses = tiempo_prestamo_meses
        self.ciudad = ciudad

    def set_ciudad(self, ciudad):
        self.ciudad = ciudad.lower()

    def __str__(self):
        return f"Préstamo a: {self.beneficiario}, Tiempo: {self.tiempo_prestamo_meses} meses, Ciudad: {self.ciudad}"
class PrestamoAutomovil(Prestamo):
    def __init__(self, beneficiario, tiempo_prestamo_meses, ciudad, tipo_automovil, marca, garante1, valor_automovil):
        super().__init__(beneficiario, tiempo_prestamo_meses, ciudad)
        self.tipo_automovil = tipo_automovil
        self.marca = marca
        self.garante1 = garante1
        self.valor_automovil = valor_automovil
        self.valor_mensual_pago = self.calcular_pago_mensual()

    def calcular_pago_mensual(self):
        return self.valor_automovil / self.tiempo_prestamo_meses

    def set_ciudad(self, ciudad):
        self.ciudad = ciudad.upper()

    def __str__(self):
        return f"{super().__str__()}, Tipo: {self.tipo_automovil}, Marca: {self.marca}, Garante: {self.garante1}, Valor Automóvil: {self.valor_automovil}, Pago Mensual: {self.valor_mensual_pago:.2f}"
class PrestamoEducativo(Prestamo):
    def __init__(self, beneficiario, tiempo_prestamo_meses, ciudad, nivel_estudio, centro_educativo, valor_carrera):
        super().__init__(beneficiario, tiempo_prestamo_meses, ciudad)
        self.nivel_estudio = nivel_estudio
        self.centro_educativo = centro_educativo
        self.valor_carrera = valor_carrera
        self.valor_mensual_pago = self.calcular_pago_mensual()

    def calcular_pago_mensual(self):
        return (self.valor_carrera / self.tiempo_prestamo_meses) * 0.9

    def set_ciudad(self, ciudad):
        self.ciudad = ciudad.upper()

    def __str__(self):
        return f"{super().__str__()}, Nivel de Estudio: {self.nivel_estudio}, Centro Educativo: {self.centro_educativo}, Valor Carrera: {self.valor_carrera}, Pago Mensual: {self.valor_mensual_pago:.2f}"
