# Title:    Example Astropy units sub.package  https://docs.astropy.org/en/stable/units/index.html
# Author:   Jorge Higuera
# email:    jhiguera@ieee.org
# Date:     18/09/2021
# Entity:   Agrupacion astronomica de Castelldefels (AAC) https://astrofels.blogspot.com/
#colab:     https://colab.research.google.com/drive/1LcrFDPH4eekDQMVs2HP13Cj_RGCMHvQ3#scrollTo=gW-ETfpV51Ae

from astropy import units as u

#-----------------------------------------------------------
#Definir escalares y vectores con sus unidades 
#------------------------------------------------------------

velocidad_escape_kms = 11.2*u.km / u.s
print("la velocidad de escape de la tierra en km/s:", velocidad_escape_kms)

velocidad_escape_ms= velocidad_escape_kms.to(u.m / u.s)
print("la velocidad de escape de la tierra en m/s:", velocidad_escape_ms)

#--------------------------------------------------------------------------------------------------------------
#Convertir una distancia  de Km a Parsecs
#---------------------------------------------------------------------------------------------------------------
#Parsecs "parallax of one arc second" (paralaje de un segundo de arco)
#distancia a la que una unidad astronómica (ua) subtiende un ángulo de un segundo de arco (1″). 
# En otras palabras, una estrella dista un pársec si su paralaje es igual a 1 segundo de arco entre el Sol y la Tierra.


#Proxima centauri esta 1.29 parsec
distancia_Proxima_centauri_pc= (4.011e+13 * u.km).to(u.pc)
print("la distancia de proxima centauri a la tierra en parsecs es de:", distancia_Proxima_centauri_pc)

#--------------------------------------------------------------------------------------------------------------
#Convertir una distancia  de Km a años luz
#---------------------------------------------------------------------------------------------------------------
#Proxima centauri esta 4,23 años luz
distancia_proxima_centauri_al = (4.011e+13 * u.km).to(u.lyr)
print("la distancia de proxima centauri a la tierra en años luz es de:",distancia_proxima_centauri_al)

#--------------------------------------------------------------------------------------------------------------
#Convertir una distancia  de Parsec a años luz
#---------------------------------------------------------------------------------------------------------------
#un parsec equivale a 3,23 años luz
conversion_Parsec_año_luz =(1*u.pc).to(u.lyr)
print("Un parsec equivale a:", conversion_Parsec_año_luz)