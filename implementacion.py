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
        if not isinstance(asignaturasMatriculadas, list):
            raise TypeError("Las asignaturas matriculadas deben estar en una lista.")
        for asignatura in asignaturasMatriculadas:
            if not isinstance(asignatura, Asignatura):
                raise ErrorDeAsignatura("Todos los elementos de la lista deben ser instancias de la clase Asignatura.")
        self.asignaturasMatriculadas = asignaturasMatriculadas

    def matricularAsignatura(self, asignatura):
        if not isinstance(asignatura, Asignatura):
            raise ErrorDeMatriculacion("El objeto a matricular debe ser una instancia de Asignatura.")
        self.asignaturasMatriculadas.append(asignatura)

    def eliminarAsignatura(self, asignatura):
        self.asignaturasMatriculadas.remove(asignatura)

    def getAsignaturasMatriculadas(self):
        return self.asignaturasMatriculadas


class MiembroDepartamento(Persona):
    def __init__(self, dni, nombre, direccion, sexo, departamento, asignaturasImpartidas):
        super().__init__(dni, nombre, direccion, sexo)
        if departamento not in ["DIIC", "DITEC", "DIS"]:
            raise ErrorDeValidacion("El departamento debe ser DIIC, DITEC o DIS.")
        self.departamento = departamento
        if not isinstance(asignaturasImpartidas, list):
            raise TypeError("Las asignaturas impartidas deben estar en una lista.")
        for asignatura in asignaturasImpartidas:
            if not isinstance(asignatura, Asignatura):
                raise ErrorDeAsignatura("Todos los elementos de la lista deben ser instancias de la clase Asignatura.")
        self.asignaturasImpartidas = asignaturasImpartidas

    def getAsignaturasImpartidas(self):
        return self.asignaturasImpartidas
    
    def getDepartamento(self):
        return self.departamento
    
    def cambiarDepartamento(self, nuevo_departamento):
        if nuevo_departamento not in ["DIIC", "DITEC", "DIS"]:
            raise ErrorDeValidacion("El departamento debe ser DIIC, DITEC o DIS.")
        self.departamento = nuevo_departamento

    def impartirAsignatura(self, asignatura):
        if not isinstance(asignatura, Asignatura):
            raise ErrorDeMatriculacion("El objeto a impartir debe ser una instancia de Asignatura.")
        self.asignaturasImpartidas.append(asignatura)

    def eliminarAsignaturaImpartida(self, asignatura):
        self.asignaturasImpartidas.remove(asignatura)


class ProfesorTitular(MiembroDepartamento):
    def __init__(self, dni, nombre, direccion, sexo, departamento, asignaturasImpartidas, areaDeInvestigacion):
        super().__init__(dni, nombre, direccion, sexo, departamento, asignaturasImpartidas)
        self.areaDeInvestigacion = areaDeInvestigacion
    
    def getAreaDeInvestigacion(self):
        return self.areaDeInvestigacion


class ProfesorAsociado(MiembroDepartamento):
    pass


class Investigador(ProfesorTitular):
    pass

        

   
    
########PRUEBAS QUE LUEGO TENEMOS QUE BORRAR A LA HORA DE ENTREGAR EL TRABAJO FINAL IMPORTANTE####### 
if __name__ == "__main__":
    matematicas = Asignatura("Matemáticas", "MAT101")
    fisica = Asignatura("fisica", "FIS101")
    estudiante1 = Estudiante("12345678A", "juan", "Calle A", "V", [matematicas, fisica])

    #probamos si funciona bien al añadir y eliminar una asignatura
    lengua = Asignatura("Lengua", "LEN101")
    print(estudiante1.matricularAsignatura(lengua))

    print(estudiante1.eliminarAsignatura(lengua))

    #probando cosas de los miembros de departamento
    profesor = MiembroDepartamento("12345678A", "juan", "Calle A", "V", "DIIC", [matematicas, fisica])
    print(profesor.impartirAsignatura(lengua))

    print(profesor.eliminarAsignaturaImpartida(lengua))

    print(profesor.getDepartamento())
    print(profesor.cambiarDepartamento("DIS"))
    print(profesor.getDepartamento())