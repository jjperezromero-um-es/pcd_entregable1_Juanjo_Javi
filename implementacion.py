# -----------------------
# EXCEPCIONES PERSONALIZADAS
# -----------------------
class ErrorDeFormato(Exception):
    """Excepción lanzada por errores en el formato de los datos."""
    pass

class ErrorDeAsignatura(Exception):
    """Excepción lanzada por errores relacionados con las asignaturas."""
    pass

class ErrorDeDepartamento(Exception):
    """Excepción lanzada por errores relacionados con los departamentos."""
    pass

class ErrorDeDNI(Exception):
    """Excepción lanzada por errores relacionados con el DNI."""
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
            raise ErrorDeFormato("El sexo debe ser 'V' (varón) o 'M' (mujer).")
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
        if type(asignaturasMatriculadas) is not list:
            raise ErrorDeAsignatura("Las asignaturas matriculadas deben estar en formato lista")
        
        for asignatura in asignaturasMatriculadas:
            if not isinstance(asignatura, Asignatura):
                raise ErrorDeAsignatura("Las asignaturas deben ser objetos de la clase Asignatura") 
        self.asignaturasMatriculadas = asignaturasMatriculadas

    def __str__(self):
        return super().__str__()
    
    def matricularAsignatura(self, asignatura):
        if not isinstance(asignatura, Asignatura):
                raise ErrorDeAsignatura("Las asignaturas deben ser objetos de la clase Asignatura") 
        self.asignaturasMatriculadas.append(asignatura)
        return f"Se ha matriculado la asignatura {asignatura.getNombre()}"

    def eliminarAsignaturaMatriculada(self, asignatura):
        self.asignaturasMatriculadas.remove(asignatura)
        return f"Se ha eliminado la asignatura {asignatura.getNombre()}"

    def getAsignaturasMatriculadas(self):
        return self.asignaturasMatriculadas


class MiembroDepartamento(Persona):
    def __init__(self, dni, nombre, direccion, sexo, departamento):
        super().__init__(dni, nombre, direccion, sexo)
        if departamento not in ["DIIC","DITEC","DIS"]:
            raise ErrorDeDepartamento("el departamento debe ser DIIC, DITEC o DIS")
        self.departamento = departamento
    
    def getDepartamento(self):
        return self.departamento
    
    def cambiarDepartamento(self, nuevo_departamento):
        if nuevo_departamento in ["DIIC","DITEC","DIS"]:
            self.departamento = nuevo_departamento
            return f"El departamento ha cambiado a {nuevo_departamento}"
        raise ErrorDeDepartamento("el departamento debe ser DIIC, DITEC o DIS")



class Investigador(MiembroDepartamento):
    def __init__(self, dni, nombre, direccion, sexo, departamento, area_de_investigacion):
        super().__init__(dni, nombre, direccion, sexo, departamento)
        self.area_de_investigacion = area_de_investigacion

    def get_area_de_investigacion(self):
        return self.area_de_investigacion
    
    def __str__(self):
        return super().__str__() + f", Área de Investigación: {self.area_de_investigacion} , Departamento: {self.departamento}"


class ProfesorTitular(Investigador):
    def __init__(self, dni, nombre, direccion, sexo, departamento, asignaturasImpartidas,area_de_investigacion):
        super().__init__(dni, nombre, direccion, sexo, departamento ,area_de_investigacion)
        if type(asignaturasImpartidas) is not list:
            raise ErrorDeFormato("Las asignaturas impartidas deben estar en formato lista")
        
        for asignatura in asignaturasImpartidas:
            if not isinstance(asignatura, Asignatura):
                raise ErrorDeAsignatura("Las asignaturas deben ser objetos de la clase Asignatura") 
        self.asignaturasImpartidas = asignaturasImpartidas

    def __str__(self):
        return super().__str__() + f", Área de Investigación: {self.area_de_investigacion} , Departamento: {self.departamento}"
    
        
    def getAsignaturasImpartidas(self):
        return self.asignaturasImpartidas
    
    def añadirAsignaturaImpartida(self, asignatura):
        if not isinstance(asignatura, Asignatura):
                raise ErrorDeAsignatura("Las asignaturas deben ser objetos de la clase Asignatura") 
        self.asignaturasImpartidas.append(asignatura)
        return f"Se ha añadido la asignatura {asignatura.getNombre()} a las asignaturas impartidas"

    def eliminarAsignaturaImpartida(self, asignatura):
        self.asignaturasImpartidas.remove(asignatura)
        return f"Se ha eliminado la asignatura {asignatura.getNombre()} de las asignaturas impartidas"
    



class ProfesorAsociado(MiembroDepartamento):
    def __init__(self, dni, nombre, direccion, sexo, departamento, asignaturasImpartidas):
        super().__init__(dni, nombre, direccion, sexo, departamento)
        if type(asignaturasImpartidas) is not list:
            raise ErrorDeFormato("Las asignaturas impartidas deben estar en formato lista")
        
        for asignatura in asignaturasImpartidas:
            if not isinstance(asignatura, Asignatura):
                raise ErrorDeAsignatura("Las asignaturas deben ser objetos de la clase Asignatura") 
        self.asignaturasImpartidas = asignaturasImpartidas

    def __str__(self):
        return super().__str__() + f", Departamento: {self.departamento}"
    
        
    def getAsignaturasImpartidas(self):
        return self.asignaturasImpartidas
    
    def añadirAsignaturaImpartida(self, asignatura):
        if not isinstance(asignatura, Asignatura):
                raise ErrorDeAsignatura("Las asignaturas deben ser objetos de la clase Asignatura") 
        self.asignaturasImpartidas.append(asignatura)
        return f"Se ha añadido la asignatura {asignatura.getNombre()} a las asignaturas impartidas"

    def eliminarAsignaturaImpartida(self, asignatura):
        self.asignaturasImpartidas.remove(asignatura)
        return f"Se ha eliminado la asignatura {asignatura.getNombre()} de las asignaturas impartidas"


#clase que administra a los miembros de la universidad (estudiantes y miembros de departamento)
class Universidad:
    def __init__(self, nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion
        self.listado_dnis = []
        self.listado_estudiantes = []
        self.listado_profesores = []
        self.listado_investigadores = []

    def getMiembroDepartamento(self, dni):
        for miembro in self.listado_profesores + self.listado_investigadores:
            if miembro.getDNI() == dni:
                return miembro
        return None

    def getEstudiante(self, dni):
        for estudiante in self.listado_estudiantes:
            if estudiante.getDNI() == dni:
                return estudiante
        return None

    def incorporar_estudiante(self, dni, nombre, direccion, sexo, asignaturasMatriculadas):
        if dni in self.listado_dnis:
            raise ErrorDeDNI("El DNI ya está en uso")
        estudiante = Estudiante(dni, nombre, direccion, sexo, asignaturasMatriculadas)
        self.listado_estudiantes.append(estudiante)
        self.listado_dnis.append(dni)

    def incorporar_profesor_asociado(self, dni, nombre, direccion, sexo, departamento, asignaturasImpartidas):
        if dni in self.listado_dnis:
            raise ErrorDeDNI("El DNI ya está en uso")
        profesor_asociado = ProfesorAsociado(dni, nombre, direccion, sexo, departamento, asignaturasImpartidas)
        self.listado_profesores.append(profesor_asociado)
        self.listado_investigadores.append(profesor_asociado)
        self.listado_dnis.append(dni)

    #cuando añado a una persona como profesor titular tambien añado a esa persona como investigador
    def incorporar_investigador_y_profesor_titular(self, dni, nombre, direccion, sexo, departamento, asignaturasImpartidas, areaDeInvestigacion):
        if dni in self.listado_dnis:
            raise ErrorDeDNI("El DNI ya está en uso")
        profesor_titular = ProfesorTitular(dni, nombre, direccion, sexo, departamento, asignaturasImpartidas, areaDeInvestigacion)
        investigador = Investigador(dni, nombre, direccion, sexo, departamento, areaDeInvestigacion)
        self.listado_profesores.append(profesor_titular)
        self.listado_investigadores.append(investigador)
        self.listado_dnis.append(dni)

    #al eliminar un investigador tambien elimino al profesor titular
    def eliminar_investigador_y_profesor_titular(self, dni):
        for profesor in self.listado_profesores:
            if isinstance(profesor, ProfesorTitular) and profesor.getDNI() == dni:
                self.listado_profesores.remove(profesor)

        for investigador in self.listado_investigadores:
                if isinstance(investigador, Investigador) and investigador.getDNI() == dni:
                    self.listado_investigadores.remove(investigador)
                    self.listado_dnis.remove(dni)
                    return f"Profesor titular e investigador con dni: {dni} eliminado"

        raise ErrorDeDNI("No se encontró un profesor titular e investigador con ese DNI")

    def eliminarProfesor(self, dni):
        for profesor in self.listado_profesores:
            if profesor.getDNI() == dni:
                self.listado_profesores.remove(profesor)
                self.listado_dnis.remove(dni)
                return f"Profesor con DNI {dni} eliminado"
        raise ErrorDeDNI("No se encontró un profesor con ese DNI")

    def eliminarEstudiante(self, dni):
        for estudiante in self.listado_estudiantes:
            if estudiante.getDNI() == dni:
                self.listado_estudiantes.remove(estudiante)
                self.listado_dnis.remove(dni)
                return f"Estudiante con DNI {dni} eliminado"
        raise ErrorDeDNI("No se encontró un estudiante con ese DNI")
    
    def showEstudiantes(self):
        print("LISTADO DE ESTUDIANTES")
        for estudiante in self.listado_estudiantes:
            print("Nombre: ",estudiante.getNombre(), ", DNI:", estudiante.getDNI())

    def showProfesores(self):
        print("LISTADO DE PROFESORES")
        for profesor in self.listado_profesores:
            print("Nombre: ",profesor.getNombre(), ", DNI:", profesor.getDNI())

    def showInvestigadores(self):
        print("LISTADO DE INVESTIGADORES")
        for investigador in self.listado_investigadores:
            print("Nombre: ",investigador.getNombre(), ", DNI:", investigador.getDNI())
    
    def __str__(self):
        return f"Nombre: {self.nombre}, Dirección: {self.direccion}"
    
    
    
    



########PRUEBAS######## 
if __name__ == "__main__":
    # Creación de asignaturas
    matematicas = Asignatura("Matemáticas", "MAT101")
    fisica = Asignatura("Física", "FIS101")
    lengua = Asignatura("Lengua", "LEN101")
    historia = Asignatura("Historia", "HIS101")

    universidad = Universidad("Universidad de murcua", "Calle de la Universidad, 1")

    universidad.incorporar_estudiante("0000000A", "Javier Ruiz", "Calle de tomate", "V", [matematicas, fisica])
    universidad.incorporar_estudiante("11111111B", "juanjo perez", "Calle formula 1", "V", [lengua, historia])
    universidad.incorporar_estudiante("22222222C", "fernando alonso", "Calle murcia", "V", [matematicas, lengua])

    universidad.incorporar_profesor_asociado("33333333D", "paco", "Calle de la Universidad, 1", "V", "DIS", [fisica])
    profesor1 = universidad.getMiembroDepartamento("33333333D")
    print(profesor1.añadirAsignaturaImpartida(matematicas))
    print(profesor1.getAsignaturasImpartidas())

    universidad.incorporar_investigador_y_profesor_titular("44444444E", "pepe", "Calle de la Universidad, 1", "V", "DITEC", [fisica,matematicas], "Ciencia de datos")
    universidad.incorporar_investigador_y_profesor_titular("55555555F", "juan", "Calle de la Universidad, 1", "V", "DIS", [fisica,matematicas], "Ciencia de datos")

    print(universidad.eliminar_investigador_y_profesor_titular("44444444E"))

    universidad.showEstudiantes()
    universidad.showProfesores()
