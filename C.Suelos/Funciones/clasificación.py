from .granulometria import *
from .cartaplasticidad import *
from .valoresdeentrada import *


import matplotlib.pyplot as plt
import matplotlib.path as mpath
import numpy as np
import pandas as pd
def ClasificacionSuelos():
        
    if A==2:
      porcentaje_finos= 6
      if porcentaje_finos<5: 
        cu=4
        cc=2
        if cu>3 and cc>1 and cc<3:
          print("Grava bien gradada")
        else:
          print("Grava mal gradada")
      else :
        b="si"
        if b=="si" or b=="no":
          if b=="si":
            print( "Grava Limosa")
          else:
            print("Grava Arcillosa")
        else:
          print("Error")

    if A==1:
      porcentaje_finos= 10
      if porcentaje_finos<5: 
        cu=4
        cc=3
        if cu>=6 and cc>1 and cc<3:
          print("Arena bien gradada")
        else:
          print("Arena mal gradada")
      else :
        b="si"
        if b=="si" or b=="no":
          if b=="si":
            print( "Arena Limosa")
          else:
            print("Arena Arcillosa")
        else:
          print("Error")

    if A==3:
        cartaplasticidad()

        
tamiz_200 = 49

if tamiz_200 < 50:
    porcentaje_tamiz_4 = 10
    if porcentaje_tamiz_4 > 40:
        A=print("Es una Arena")
        A=1
    else:
        A=print("Es una grava")
        A=2
else:
    A=print("Ir a la carta de plasticidad")
    A=3

ClasificacionSuelos()