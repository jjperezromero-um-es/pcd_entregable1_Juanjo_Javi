# -----------------------
# EXCEPCIONES PERSONALIZADAS
# -----------------------
class ErrorDeFormato(Exception):
    """Excepción lanzada por errores en el formato de los datos."""
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
            raise ErrorDeFormato("Las asignaturas matriculadas deben estar en formato lista")
        
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
            raise ErrorDeFormato("el departamento debe ser DIIC, DITEC o DIS")
        self.departamento = departamento
    
    def getDepartamento(self):
        return self.departamento
    
    def cambiarDepartamento(self, nuevo_departamento):
        if nuevo_departamento in ["DIIC","DITEC","DIS"]:
            self.departamento = nuevo_departamento
            return f"El departamento ha cambiado a {nuevo_departamento}"
        raise ErrorDeFormato("el departamento debe ser DIIC, DITEC o DIS")



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
    
    def añadirAsignatura(self, asignatura):
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
    
    def añadirAsignatura(self, asignatura):
        if not isinstance(asignatura, Asignatura):
                raise ErrorDeAsignatura("Las asignaturas deben ser objetos de la clase Asignatura") 
        self.asignaturasImpartidas.append(asignatura)
        return f"Se ha añadido la asignatura {asignatura.getNombre()} a las asignaturas impartidas"

    def eliminarAsignaturaImpartida(self, asignatura):
        self.asignaturasImpartidas.remove(asignatura)
        return f"Se ha eliminado la asignatura {asignatura.getNombre()} de las asignaturas impartidas"



    
########PRUEBAS######## 
if __name__ == "__main__":
    # Creación de asignaturas
    matematicas = Asignatura("Matemáticas", "MAT101")
    fisica = Asignatura("Física", "FIS101")
    lengua = Asignatura("Lengua", "LEN101")
    historia = Asignatura("Historia", "HIS101")

    # Creación de estudiantes
    estudiante1 = Estudiante("33J", "Juanjo", "Avenida Juan Carlos 1", "V", [matematicas, fisica])
    estudiante2 = Estudiante("66M", "M.Ángeles", "Calle Ponzoa", "M", [fisica, historia])


    # Creación de profesores y asignación de asignaturas
    profesor1 = ProfesorTitular("101P", "Carlos", "Calle 2", "V", "DIIC", [matematicas, lengua], "Historia Moderna")
    profesor2 = ProfesorAsociado("102P", "Ana", "Calle 3", "M", "DITEC", [matematicas, lengua])
    investigador = Investigador("103P", "Laura", "pitopito", "M", "DIIC", "Estadistica")

    print(estudiante1)
    print(estudiante2)
    print(profesor1)
    print(profesor2)
    print(investigador)


    print(estudiante1.matricularAsignatura(lengua))
    print(estudiante1.eliminarAsignaturaMatriculada(lengua))

    print(profesor1.añadirAsignatura(historia))
    print(profesor1.getAsignaturasImpartidas())
    print(profesor1.eliminarAsignaturaImpartida(historia))

    print(profesor2.añadirAsignatura(historia))
    print(profesor2.getAsignaturasImpartidas())
    print(profesor2.eliminarAsignaturaImpartida(historia))

    print(investigador.cambiarDepartamento("DITEC"))


