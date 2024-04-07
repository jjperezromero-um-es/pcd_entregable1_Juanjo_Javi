import pytest
from implementacion import Persona, Asignatura, Estudiante, ProfesorTitular, ProfesorAsociado, MiembroDepartamento, Investigador, Universidad
from implementacion import ErrorDeAsignatura, ErrorDeFormato, ErrorDeDepartamento, ErrorDeDNI

def test_creacion_persona():
    persona = Persona("33J", "Juanjo", "Calle 2", "V")
    assert persona.getNombre() == "Juanjo" #En estos asserts comprobamos que se haya creado todo bien
    assert persona.getDNI() == "33J"
    assert persona.getDireccion() == "Calle 2"
    assert persona.getSexo() == "V"
    
    with pytest.raises(ErrorDeFormato):
        Persona("33J", "Juano", "Calle 2", "K")  # Comprobamos que salta el error de sexo inválido

def test_creacion_asignatura():
    asignatura = Asignatura("Matemáticas", "MATES1")
    assert asignatura.getNombre() == "Matemáticas" #Comprobamos que el nombre de la asignatura creada sea Matemáticas
    assert asignatura.getCodigo() == "MATES1" #Comprobamos qe el código de la asignatura sea MATES1

def test_estudiante_matriculacion():
    estudiante = Estudiante("001X", "Javi", "Calle 3", "V", [])
    matematicas = Asignatura("Matemáticas", "MAT123")
    estudiante.matricularAsignatura(matematicas) #Lo matriculamos en matemáticas
    assert matematicas in estudiante.getAsignaturasMatriculadas() #Comprobamos que matemáticas se haya metido en estudiante

def test_estudiante_eliminar_asignatura():
    fisica = Asignatura("Física", "FIS456")
    estudiante = Estudiante("002X", "Pepita", "Calle 4", "M", [fisica]) #Metemos que pepita estudia fisica
    estudiante.eliminarAsignaturaMatriculada(fisica) #Eliminamos fisica 
    assert fisica not in estudiante.getAsignaturasMatriculadas() #Comprobamos que fisica ya no esté 

def test_error_al_crear_estudiante_con_asignaturas_no_lista():
    with pytest.raises(ErrorDeAsignatura):
        Estudiante("003X", "Carlos", "Calle Murcia", "V", "Matemáticas")  # Comprobamos que salta un error ya que no es una lista

def test_miembro_departamento_creacion():
    miembro = MiembroDepartamento("456X", "Laura", "Calle 5", "M", "DIIC") #Creamos un miembro de departamento y con los asserts comprobamos que se ha creado bien y comprobamos alguna que otra cosa más como las asignaturas impartidas.
    assert miembro.getNombre() == "Laura"
    assert miembro.getDireccion() == "Calle 5"
    assert miembro.getDepartamento() == "DIIC"
    
    with pytest.raises(ErrorDeDepartamento):
        MiembroDepartamento("456X", "Laura", "Calle 5", "M", "MATES") #Aquí en el departamento hemos puesto Mates que obviamente no está entre los departamentos posibles y por lo tanto comprobamos que tiene que darnos el error

def test_miembro_departamento_cambiar_departamento():
    miembro = MiembroDepartamento("789X", "Antonio", "Calle 7", "V", "DITEC")
    miembro.cambiarDepartamento("DIS")
    assert miembro.getDepartamento() == "DIS" #Comprobamos que se ha cambiado correctament el departamento
    
def test_error_al_crear_profesor_asociado_con_asignatura_sin_ser_lista():
    with pytest.raises(ErrorDeFormato):
        ProfesorAsociado("456M", "M.Ángeles 1", "Calle 12", "M", "DIS", "Física") #Aquí donde he puesto 'Física' debería de ser [Física] y por lo tanto comprobamos que de error

def test_profesor_titular_area_investigacion():
    profesor = ProfesorTitular("100X", "Javi 2", "Calle 8", "V", "DIIC", [], "Robótica") #Comprobación de la correcta creación de un profesor titular
    assert profesor.getAreaDeInvestigacion() == "Robótica"
    assert profesor.getDepartamento() == "DIIC"

def test_profesor_asociado_sin_area_investigacion():
    profesor = ProfesorAsociado("110X", "Javi 1", "Calle 9", "V", "DIS", []) # Aquí simplemente verificamos que se pueda crear y que esté bien
    assert profesor.getNombre() == "Javi 1"
    assert profesor.getDepartamento() == "DIS"

def test_profesor_titular_asignatura_impartida():
    Profesor1 = ProfesorTitular("120X", "Juanjo 2", "Calle 10", "V", "DIIC",[], "Inteligencia Artificial") 
    matematicas = Asignatura("Matemáticas", "MAT123")
    Profesor1.añadirAsignaturaImpartida(matematicas)
    assert matematicas in Profesor1.getAsignaturasImpartidas() #Creamos un investigador, creamos una asignatura y hacemos que el investigador la imparta y luego comprobamos que en efecto esta asignatura esté entre sus asignaturas impartidas

def test_eliminar_asignatura_impartida():
    fisica = Asignatura("Física", "FIS456")
    Profesor2 = ProfesorTitular("123L", "Laura 2", "Calle 11", "M", "DIIC", [fisica], "Computación Cuántica")
    Profesor2.eliminarAsignaturaImpartida(fisica)
    assert fisica not in Profesor2.getAsignaturasImpartidas() #Aquí hemos creado un investigador que imparte física y hemos hecho que deje de impartirla y luego comprobamos que efectivamente ya no esté entre sus asignaturas impartidas

def creación_universidad():
    universidad = Universidad("Universidad de Prueba", "Calle 33")
    assert universidad.getNombre() == "Universidad de Prueba"
    assert universidad.getDireccion() == "Calle 33"

def test_incorporar_y_eliminar_estudiante():
    universidad = Universidad("Universidad de Murcia", "Calle España")
    asignatura_test = Asignatura("Matemáticas", "MAT123")
    universidad.incorporarEstudiante("12345678A", "Estudiante Test", "Dirección Test", "V", [asignatura_test])
    assert universidad.getEstudiante("12345678A") is not None
    universidad.eliminarEstudiante("12345678A")
    assert universidad.getEstudiante("12345678A") is None

def test_incorporar_y_eliminar_profesor_titular():
    universidad2 = Universidad("Universidad de Madrid", "Calle Cibeles")
    asignatura_test2 = Asignatura("Dibujo", "DIB123")
    universidad2.incorporarInvestigadorYProfesorTitular("11223344C", "Profesor Titular Test", "Dirección Test", "M", "DITEC", [asignatura_test2], "Área Test")
    assert universidad2.getMiembroDepartamento("11223344C") is not None
    universidad2.eliminarInvestigadorYProfesorTitular("11223344C")
    assert universidad2.getMiembroDepartamento("11223344C") is None

def test_eliminar_profesor_inexistente():
    universidad3 = Universidad("Universidad de Valencia", "Calle Mestalla")
    with pytest.raises(ErrorDeDNI):
        universidad3.eliminarProfesorAsociado("99999999Z")