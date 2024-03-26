# -----------------------
# EXCEPCIONES PERSONALIZADAS
# -----------------------
class ErrorDeValidacion(Exception):
    """Excepción lanzada por errores en la validación de datos."""
    pass

class ErrorDeMatriculacion(Exception):
    """Excepción lanzada al intentar matricular una asignatura incorrectamente."""
    pass

class ErrorDeAsignatura(Exception):
    """Excepción lanzada por errores relacionados con las asignaturas."""
    pass


# -----------------------
# CLASES PRINCIPALES
# -----------------------
class Persona:
    def __init__(self, dni, nombre, direccion, sexo):
        self.dni = dni
        self.nombre = nombre
        self.direccion = direccion
        if sexo not in ["V", "M"]:
            raise ErrorDeValidacion("El sexo debe ser 'V' (varón) o 'M' (mujer).")
        self.sexo = sexo

    def __str__(self):
        return f"Persona: {self.nombre}, DNI: {self.dni}, Dirección: {self.direccion}, Sexo: {self.sexo}"

    def getNombre(self):
        return self.nombre

    def getDNI(self):
        return self.dni

    def getDireccion(self):
        return self.direccion

    def getSexo(self):
        return self.sexo


class Asignatura:
    def __init__(self, nombre, codigo):
        self.nombre = nombre
        self.codigo = codigo

    def __str__(self):
        return f"Asignatura: {self.nombre}, Código: {self.codigo}"

    def getNombre(self):
        return self.nombre

    def getCodigo(self):
        return self.codigo


class Estudiante(Persona):
    def __init__(self, dni, nombre, direccion, sexo, asignaturasMatriculadas):
        super().__init__(dni, nombre, direccion, sexo)
        self.asignaturasMatriculadas = asignaturasMatriculadas

    def matricularAsignatura(self, asignatura):
        self.asignaturasMatriculadas.append(asignatura)
        return f"Se ha matriculado la asignatura {asignatura.getNombre()}"

    def eliminarAsignatura(self, asignatura):
        self.asignaturasMatriculadas.remove(asignatura)
        return f"Se ha eliminado la asignatura {asignatura.getNombre()}"

    def getAsignaturasMatriculadas(self):
        return self.asignaturasMatriculadas


class MiembroDepartamento(Persona):
    def __init__(self, dni, nombre, direccion, sexo, departamento, asignaturasImpartidas):
        super().__init__(dni, nombre, direccion, sexo)
        self.departamento = departamento
        self.asignaturasImpartidas = asignaturasImpartidas
    
    def getAsignaturasImpartidas(self):
        return self.asignaturasImpartidas
    
    def getDepartamento(self):
        return self.departamento
    
    def cambiarDepartamento(self, nuevo_departamento):
        self.departamento = nuevo_departamento
        return f"El departamento ha cambiado a {nuevo_departamento}"
    
    def impartirAsignatura(self, asignatura):
        self.asignaturasImpartidas.append(asignatura)
        return f"Se ha añadido la asignatura {asignatura.getNombre()} a las asignaturas impartidas"

    def eliminarAsignaturaImpartida(self, asignatura):
        self.asignaturasImpartidas.remove(asignatura)
        return f"Se ha eliminado la asignatura {asignatura.getNombre()} de las asignaturas impartidas"


class ProfesorTitular(MiembroDepartamento):
    def __init__(self, dni, nombre, direccion, sexo, departamento, asignaturasImpartidas, areaDeInvestigacion):
        super().__init__(dni, nombre, direccion, sexo, departamento, asignaturasImpartidas)
        self.areaDeInvestigacion = areaDeInvestigacion
    
    def getAreaDeInvestigacion(self):
        return self.areaDeInvestigacion

    def __str__(self):
        return super().__str__() + f", Área de Investigación: {self.areaDeInvestigacion}"


class ProfesorAsociado(MiembroDepartamento):
    pass


class Investigador(ProfesorTitular):
    pass

# Aquí puedes incluir el bloque de pruebas proporcionado anteriormente.


        

   
    
########PRUEBAS######## 
if __name__ == "__main__":
    # Creación de asignaturas
    matematicas = Asignatura("Matemáticas", "MAT101")
    fisica = Asignatura("Física", "FIS101")
    lengua = Asignatura("Lengua", "LEN101")
    historia = Asignatura("Historia", "HIS101")

    # Creación de estudiantes
    estudiante1 = Estudiante("33J", "Juanjo", "Avenida Juan Carlos 1", "V", [matematicas, fisica, lengua])
    estudiante2 = Estudiante("66M", "M.Ángeles", "Calle Ponzoa", "M", [fisica, lengua, historia])

    # Añadir y eliminar asignaturas para un estudiante
    print(estudiante1.matricularAsignatura(historia))  
    print(estudiante1.eliminarAsignatura(lengua))

    # Creación de profesores y asignación de asignaturas
    profesor1 = MiembroDepartamento("101P", "Carlos", "Calle 2", "V", "DIIC", [matematicas, lengua])
    profesor2 = ProfesorTitular("102P", "Ana", "Calle 3", "M", "DITEC", [matematicas, lengua], "Historia Moderna")

    # Añadir y eliminar asignaturas impartidas por un profesor
    print(profesor2.impartirAsignatura(historia))
    print(profesor2.eliminarAsignaturaImpartida(matematicas))  

    # Gestión de departamentos
    print(f"\nDepartamento inicial del profesor1: {profesor1.getDepartamento()}")
    profesor1.cambiarDepartamento("DIS")  # Cambio de departamento, no se imprime el resultado
    print(f"Nuevo departamento del profesor1: {profesor1.getDepartamento()}")

    # Creación y gestión de un investigador
    investigador1 = Investigador("201I", "Antonio", "Calle 4", "V", "DIIC", [fisica], "Física Cuántica")
    print(f"Área de investigación del investigador1: {investigador1.getAreaDeInvestigacion()}")

    # Mostrar información de los usuarios
    print(f"\nEstudiante1: {estudiante1}")
    print(f"Estudiante2: {estudiante2}")
    print(f"Profesor1: {profesor1}")
    print(f"Profesor2: {profesor2}")
    print(f"Investigador1: {investigador1}")
