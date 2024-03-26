class Persona:
    def __init__(self,dni,nombre,direccion,sexo):
        self.dni = dni
        self.nombre = nombre
        self.direccion = direccion
        if sexo in ["V","M"]:
            self.sexo = sexo
        else:
            raise ValueError("el sexo debe ser V(varon) o M(mujer)")
    
     
    def __str__(self):
        return f"Persona: {self.nombre}, DNI: {self.dni}, Dirección: {self.direccion}, Sexo: {self.sexo}"
        
    #funciones de la clase
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

    #funciones de la clase
    def getNombre(self):
        return self.nombre

    def getCodigo(self):
        return self.codigo
    

#estudiante hereda de persona sus atributos
class Estudiante(Persona):
    def __init__(self, dni, nombre, direccion, sexo, AsignaturasMatriculadas):
        #realizamos super().__init__ por la herencia
        super().__init__(dni, nombre, direccion, sexo)

        #control de errores para que la asignatura sea una lista
        if type(AsignaturasMatriculadas) is not list:
            raise TypeError("las asignaturas matriculadas deben estar en una lista")
        #cada asignatura debe ser instancia de la clase Asignatura
        for asignatura in AsignaturasMatriculadas:
            if type(asignatura) is not Asignatura:
                raise TypeError("Todos los elementos de la lista deben ser instancias de la clase Asignatura")
        
        self.asignaturasMatriculadas = AsignaturasMatriculadas
    
    #funciones de la clase
    def matricularAsignatura(self, asignatura):
        self.asignaturasMatriculadas.append(asignatura)
        return f"Se ha matriculado la asignatura {asignatura.getNombre()}"

    def eliminarAsignatura(self, asignatura):
        self.asignaturasMatriculadas.remove(asignatura)
        return f"Se ha eliminado la asignatura {asignatura.getNombre()}"
    
    def getAsignaturasMatriculadas(self):
        return self.asignaturasMatriculadas



class MiembroDepartamento(Persona):
    def __init__(self, dni, nombre, direccion, sexo, departamento, AsignaturasImpartidas):
        super().__init__(dni, nombre, direccion, sexo)
        #control de errores
        if departamento in ["DIIC", "DITEC", "DIS"]:
            self.departamento = departamento
        else:
            raise ValueError("el departamento debe ser DIIC, DITEC o DIS")
        
        if type(AsignaturasImpartidas) is not list:
            raise TypeError("las asignaturas impartidas deben estar en una lista")
        #cada asignatura debe ser instancia de la clase Asignatura
        for asignatura in AsignaturasImpartidas:
            if type(asignatura) is not Asignatura:
                raise TypeError("Todos los elementos de la lista deben ser instancias de la clase Asignatura")
        self.AsignaturasImpartidas = AsignaturasImpartidas

    #funciones de la clase
    def getAsignaturasImpartidas(self):
        return self.AsignaturasImpartidas
    
    def getDepartamento(self):
        return self.departamento
    
    def cambiarDepartamento(self, nuevo_departamento):
        self.departamento = nuevo_departamento
        return f"El departamento ha cambiado a {nuevo_departamento}"
    
    def impartirAsignatura(self, asignatura):
        self.AsignaturasImpartidas.append(asignatura)
        return f"Se ha eliminado la asignatura {asignatura.getNombre()} a las asignaturas impartidas"

    def eliminarAsignaturaImpartida(self, asignatura):
        self.AsignaturasImpartidas.remove(asignatura)
        return f"Se ha eliminado la asignatura {asignatura.getNombre()} de asignaturas impartidas"



class ProfesorTitular(MiembroDepartamento):
    def __init__(self, dni, nombre, direccion, sexo, departamento, AsignaturasImpartidas, areaDeInvestigacion):
        super().__init__(dni, nombre, direccion, sexo, departamento, AsignaturasImpartidas)
        self.areaDeInvestigacion = areaDeInvestigacion
    
    #funciones de la clase
    def getAreaDeInvestigacion(self):
            return self.areaDeInvestigacion
    

class ProfesorAsociado(MiembroDepartamento):
    def __init__(self, dni, nombre, direccion, sexo, departamento, AsignaturasImpartidas):
        super().__init__(dni, nombre, direccion, sexo, departamento, AsignaturasImpartidas)

class Investigador(ProfesorTitular):
    def __init__(self, dni, nombre, direccion, sexo, departamento, AsignaturasImpartidas, areaDeInvestigacion):
        super().__init__(dni, nombre, direccion, sexo, departamento, AsignaturasImpartidas, areaDeInvestigacion)
        

   
    
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