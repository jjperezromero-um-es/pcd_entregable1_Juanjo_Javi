class Persona:
    def __init__(self,dni,nombre,direccion,sexo):
        self.dni = dni
        self.nombre = nombre
        self.direccion = direccion
        if sexo in ["V","M"]:
            self.sexo = sexo
        else:
            raise ValueError("el sexo debe ser V(varon) o M(mujer)")
        
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
            raise TypeError("las asignaturas deben estar en una lista")
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


########PRUEBAS#######
if __name__ == "__main__":
    matematicas = Asignatura("Matemáticas", "MAT101")
    fisica = Asignatura("fisica", "FIS101")
    estudiante1 = Estudiante("Juan", "12345678A", "Calle A", "V", ['matematicas', fisica])

    #probamos si funciona bien al añadir y eliminar una asignatura
    lengua = Asignatura("Lengua", "LEN101")
    print(estudiante1.matricularAsignatura(lengua))

    print(estudiante1.eliminarAsignatura(lengua))

