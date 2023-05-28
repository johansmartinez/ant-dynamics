import matplotlib.pyplot as plt

class Hormiguero:
    def __init__(self,poblacion_inicial, dias_simulacion, vida_media_hormiga_reina, tamano_hormiguero, comida_dia, max_huevos_esp, taza_mortalidad, taza_enfermedad):
        self.poblacion = [poblacion_inicial]
        self.generacion_graf=[]
        self.salud_reina_graf=[]
        self.tasa_natalidad_graf=[]
        self.nacimientos_graf=[]
        self.dias_simulacion=dias_simulacion
        self.tiempo=self.crear_vector(self.dias_simulacion)
        self.vida_media_hormiga_reina=vida_media_hormiga_reina
        self.tamano_hormiguero=tamano_hormiguero
        self.comida_dia=comida_dia
        self.max_huevos_esp=max_huevos_esp
        self.taza_mortalidad=taza_mortalidad
        self.taza_enfermedad=taza_enfermedad
        self.calcular_poblacion()
        
    def crear_vector(self,numero):
        vector = list(range(numero + 1))
        return vector
    
    def calcular_poblacion(self):
        for i, t in enumerate(self.tiempo):
            #self.generacion_graf.append(self.generacion(t))
            #self.salud_reina_graf.append(self.salud_hormiga_reina(t))
            #self.tasa_natalidad_graf.append(self.tasa_natalidad(t))
            #self.nacimientos_graf.append(self.nacimientos(t))
            if i>0 and i <= len(self.poblacion):
                poblacion_temp=self.nacimientos(t) - self.muertes( self.poblacion[(i-1)], t)
                poblacion_temp+=self.poblacion[(i-1)]
                self.poblacion.append(poblacion_temp)
            
                
    def muertes(self, poblacion, tiempo):
        return self.muertes_natural(tiempo)+self.enfermas_dia(poblacion, tiempo)
    
    def enfermas_dia(self, poblacion, tiempo):
        return (poblacion/(self.generacion(tiempo)+1))*self.taza_enfermedad
    
    def muertes_natural(self,tiempo):
        return self.nacimientos(tiempo)* self.taza_mortalidad
        
    def nacimientos(self, tiempo):
        return self.tasa_natalidad(tiempo)
    
    def tasa_natalidad(self, tiempo):
        sal_reina=self.salud_hormiga_reina(tiempo)
        max_huev=self.max_huevos()
        return (1-sal_reina)*self.min_huevos(max_huev)+sal_reina*max_huev
    
    def max_huevos(self):
        return (self.comida_dia*self.max_huevos_esp)/self.tamano_hormiguero
    
    def min_huevos(self, max_huevos):
        return max_huevos/6
    
    def salud_hormiga_reina(self, tiempo):
        ope=(self.generacion(tiempo)+1)-(tiempo/self.vida_media_hormiga_reina)
        if ope==0:
            return 1
        else:
            return ope
        
    def generacion(self, tiempo):
        return int(tiempo/self.vida_media_hormiga_reina)
    
#poblacion_inicial, dias_simulacion, vida_media_hormiga_reina, tamano_hormiguero, comida_dia, max_huevos_esp, taza_mortalidad, taza_enfermedad
"""p=Hormiguero(10, 9300, 930, 7000, 300, 1400, 0.5, 0.01)

plt.plot(p.tiempo, p.poblacion)
plt.xlabel('dias')
plt.ylabel('poblacion')
plt.title('Poblacion')
plt.show()"""