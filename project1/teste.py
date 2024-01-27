from project1 import *

tv = Televisor('sony', 'sony-123')

controle = ControleRemoto(tv)

controle.sintonizarCanal('sbt')
controle.trocarCanal('sbt')

print(tv.canal_atual)

