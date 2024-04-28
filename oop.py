#__init__ es el constructor y permite crear un objeto de la clase
#los objetos tienen estado, pero las funciones no tienen estado
#determinista siempre devuelve lo mismo 

class Profesor:
    def __init__(self, el_nombre, el_email):
        self.__nombre__ = el_nombre
        self.__email__ = el_email


    def dame_tu_nombre(self):
        return self.__nombre__


class Alumno:
    def __init__(self, el_nombre_del_alumno):
        self.__nombre__ = el_nombre_del_alumno
        self.__inasistencias__ = 0
        self.__dieta__ = ""
        self.__mentor__ = None 

    def mentoria (self, profesor):
        self.__mentor__ = profesor 
    
    def falta(self):
        self.__inasistencias__ += 1
    
    def elegir_dieta_especial(self, la_dieta):
        self.__dieta__= la_dieta 
    
    def es_vegano(self):
        self.__dieta__ = "vegano"
    
    def esta_libre(self):
        if self.__inasistencias__ >= 5:
           return "ESTA LIBRE"
        else:
            return "OK"


profe_elio = Profesor("Elio", "elio@gmail.com")
profe_gabi = Profesor("Gabriel", "gabriel@um.edu.ar")

#print(profe_elio.dame_tu_nombre())
#print(profe_gabi.dame_tu_nombre())

alumno_Zowi = Alumno("Zoe")
alumno_Carli = Alumno("Carla")

alumno_Zowi.falta()
alumno_Zowi.falta()
alumno_Zowi.falta()
alumno_Zowi.falta()
alumno_Zowi.falta()

print(alumno_Zowi.esta_libre())
alumno_Zowi.falta()
print(alumno_Zowi.esta_libre())

alumno_Carli.elegir_dieta_especial("vegetariana")
print(alumno_Carli.__dieta__)
alumno_Zowi.es_vegano()
print(alumno_Zowi.__dieta__)

alumno_Zowi.mentoria(profe_elio)
print(alumno_Zowi.__mentor__)


#import ipdb; ipdb.set_trace()
