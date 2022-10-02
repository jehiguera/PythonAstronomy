# Title:    Example Astropy.constants sub-package. https://docs.astropy.org/en/stable/constants/index.html
# Author:   Jorge Higuera
# email:    jhiguera@ieee.org
# Date:     18/09/2021
# Entity:   Agrupacion astronomica de Castelldefels (AAC) https://astrofels.blogspot.com/

from astropy import units as u

from astropy import constants as const

#------------------------------------------------------------------------------------------------------------
# Constante de gravitacion universal (https://es.wikipedia.org/wiki/Constante_de_gravitaci%C3%B3n_universal)
#------------------------------------------------------------------------------------------------------------
# G es una constante física obtenida de forma empírica
#determina la intensidad de la fuerza de atracción gravitatoria entre los cuerpos. 
#Aparece tanto en la ley de gravitación universal de Newton como en la teoría general de la relatividad de Einstein. 
#La medida de G fue obtenida implícitamente por primera vez por Henry Cavendish en 1798. 

print(const.G)
#-----------------------------------------------------------------------------------------------
#Carga del electron
#-----------------------------------------------------------------------------------------------
print(const.e)
#-----------------------------------------------------------------------------------------------
#Constante de Plank
#-----------------------------------------------------------------------------------------------
print(const.h)
#-----------------------------------------------------------------------------------------------
#Luminosidad solar nominal (https://es.wikipedia.org/wiki/Luminosidad_solar)
#-----------------------------------------------------------------------------------------------
#unidad de luminosidad utilizada para expresar la luminosidad de las estrellas. 
# Esta constante es igual a la que tiene el Sol y Su valor esta expresado en vatios (W), 
print(const.L_sun)
#-----------------------------------------------------------------------------------------------
#Velocidad de la luz en el vacio  km/s
#-----------------------------------------------------------------------------------------------
print(const.c.to('km/s'))
#-----------------------------------------------------------------------------------------------
#Velocidad de la luz en el vacio  pc/yr
#-----------------------------------------------------------------------------------------------
print(const.c.to('pc/yr'))
#-----------------------------------------------------------------------------------
#Combinacion de cantidades y constantes. interacción gravitatoria entre dos cuerpos 
#-----------------------------------------------------------------------------------
print(const.M_earth)
print(const.M_sun)

#Fuerza de atraccion Sol-Tierra: G*m1*m2/(r^2)  
Fuerza_atraccion = (const.G * const.M_earth * const.M_sun ) / (1.0 * u.au) ** 2

print("La fuerza de atraccion del Sol sobre la Tierra es:", Fuerza_atraccion)

Fuerza_atraccion_Newton = Fuerza_atraccion.to(u.N)  
print("La fuerza de atraccion del Sol sobre la Tierra en Newton es:", Fuerza_atraccion_Newton)