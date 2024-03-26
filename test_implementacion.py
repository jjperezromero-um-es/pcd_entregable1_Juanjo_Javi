import pytest
from implementacion import Persona, Asignatura, Estudiante

def test_creacion_persona():
    persona = Persona("33J", "Juanjo", "Calle 2", "V")
    assert persona.getNombre() == "Juanjo" #En estos asserts comprobamos que se haya creado todo bien
    assert persona.getDNI() == "33J"
    assert persona.getDireccion() == "Calle 2"
    assert persona.getSexo() == "V"
    
    with pytest.raises(ValueError):
        Persona("33J", "Juano", "Calle 2", "K")  # Comprobamos que salta el error de sexo inválido

def test_creacion_asignatura():
    asignatura = Asignatura("Matemáticas", "MATES1")
    assert asignatura.getNombre() == "Matemáticas" #Comprobamos que el nombre de la asignatura creada sea Matemáticas
    assert asignatura.getCodigo() == "MATES1" #Comprobamos qe el código de la asignatura sea MATES1

def test_estudiante_matriculacion():
    estudiante = Estudiante("123A", "Javi", "Calle 3", "V", [])
    matematicas = Asignatura("Matemáticas", "MAT123")
    estudiante.matricularAsignatura(matematicas) #Lo matriculamos en matemáticas
    assert matematicas in estudiante.getAsignaturasMatriculadas() #Comprobamos que matemáticas se haya metido en estudiante

def test_estudiante_eliminar_asignatura():
    fisica = Asignatura("Física", "FIS456")
    estudiante = Estudiante("123B", "Pepita", "Calle 4", "M", [fisica]) #Metemos que pepita estudia fisica
    estudiante.eliminarAsignatura(fisica) #Eliminamos fisica 
    assert fisica not in estudiante.getAsignaturasMatriculadas() #Comprobamos que fisica ya no esté 

def test_error_al_crear_estudiante_con_asignaturas_no_lista():
    with pytest.raises(TypeError):
        Estudiante("12345E", "Carlos", "Calle Murcia", "V", "Matemáticas")  # Comprobamos que salta un error ya que no es una lista


