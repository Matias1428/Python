class Pokemon:
  dano_base = 10

  def __init__(self, especie, stats, tipo, fortalezas, debilidades,ataques):
    self.especie = especie
    self.stats = stats
    self.current_stats = self.stats.copy()
    self.tipo = tipo
    self.debilidades = debilidades
    self.fortalezas = fortalezas
    self.ataques = ataques

  def centro_pokemon(self):
    self.current_stats = self.stats

  def pelea(self, rival):
    # Imprimir información acerca de la pelea
    printRetardado("-----Pelea pokemon-----\n")
    # Tu rival es furte o debil a ti? 
    if self.tipo in rival.fortalezas:
      modificador_ataque = 1/2
      printRetardado({rival.especie} +" es fuerte a los ataques de "+ {self.especie}+ "\n")
    elif self.tipo in rival.debilidades:
      modificador_ataque = 2
      printRetardado(f"{rival.especie} es debil a los ataques de {self.especie} \n")
    else:
      modificador_ataque = 1


    
    #eres fuerte o debil a tu rival?
    if rival.tipo in self.fortalezas:
      modificador_defensa = 1/2
      printRetardado(f"{self.especie} es fuerte a los ataques de {rival.especie} \n")
    elif rival.tipo in self.debilidades:
      modificador_defensa = 2
      printRetardado(f"{self.especie} es debil a los ataques de {rival.especie} \n")
    else:
      modificador_defensa = 1

    # quien ataca primero
    if self.current_stats["velocidad"] >= rival.current_stats["velocidad"]:
      mi_turno = True
    else:
      mi_turno = False
    
    # combate por turnos
    while (self.current_stats["hp"] > 0) & (rival.current_stats["hp"] > 0):
      if mi_turno:
        ataque_elegido=ataque_elegir(self);
        #print("¿Que movimiento desea utilizar?\n")
        modificador_ataque2=modificadorAtaque(ataque_elegido,self,rival)
        printRetardado(self.especie + " utiliza " + ataque_elegido[0]+"\n")
        

        # atacando
        dano = int(
            self.dano_base * 
            (ataque_elegido[1] / rival.current_stats["defensa"]) * 
            modificador_ataque*modificador_ataque2) 
        rival.current_stats["hp"] -= dano
        printRetardado(self.especie +" hizo "+ str(dano)+" de daño a "+rival.especie+"\n")
        printRetardado("A "+ rival.especie+" le quedan "+ str(rival.current_stats['hp'])+" puntos de vida\n")
      else:
        # defendiendo
        dano = int(
            rival.dano_base *
            (rival.current_stats["ataque"] / self.current_stats["defensa"]) * 
            modificador_defensa)
        self.current_stats["hp"] -= dano
        printRetardado(rival.especie+ " hizo "+ str(dano)+ " de daño a "+self.especie+"\n")
        printRetardado("A "+self.especie+" le quedan "+str(self.current_stats['hp'])+ " puntos de vida\n")
      mi_turno = not mi_turno
    else:
      if self.current_stats["hp"] <= 0:
        printRetardado(rival.especie+ " ha ganado la pelea \n")
      else:
        printRetardado(self.especie +' ha ganado la pelea \n')

squirtle = Pokemon(
    especie = "Squirtle",
    stats = {
        "velocidad": 43,
        "hp": 44,
        "ataque": 48,
        "defensa": 65},
    tipo = "agua",
    fortalezas = ["fuego"],
    debilidades = ["planta"],
    ataques = {"1":["Cascada",16,'Agua'],
               "2":["Pistola_Agua", 5,'Agua'],
               "3":["Burbuja", 12,'Agua'],
               "4":["Surf", 65,'Agua']})

charmander = Pokemon(
    especie = "Charmander",
    stats = {
        "velocidad": 65,
        "hp": 39,
        "ataque": 52,
        "defensa": 43},
    tipo = "fuego",
    fortalezas = ["planta"],
    debilidades = ["agua"],
    ataques = {"1":['Colmillo_Ígneo', 12,'Fuego'],
               "2":['Giro_Fuego', 14,'Fuego'],
               "3":['Calcinación', 29,'Fuego'],
               "4":['Ascuas', 10,'Fuego']})

bulbasaur = Pokemon(
    especie = "Bulbasaur",
    stats = {
        "velocidad": 45,
        "hp": 45,
        "ataque": 49,
        "defensa": 49},
    tipo = "planta",
    fortalezas = ["agua"],
    debilidades = ["fuego"],
    ataques = {"1":['Colmillo_Ígneo', 12,'Fuego'],
               "2":['Giro_Fuego', 14,'Fuego'],
               "3":['Calcinación', 29,'Fuego'],
               "4":['Ascuas', 10,'Fuego']})

def pokemon_Elegir(pokemon_elegido):
  if pokemon_elegido=='squirtle' or pokemon_elegido=='1':
      printRetardado('Has elegido a  squirtle\n')
      squirtle.pelea(charmander)
      squirtle.centro_pokemon()
      charmander.centro_pokemon()

  elif pokemon_elegido=='charmander'  or pokemon_elegido=='2':
      printRetardado('Has elegido a charmander\n')
      charmander.pelea(bulbasaur)
      bulbasaur.centro_pokemon()
      charmander.centro_pokemon()

  elif pokemon_elegido=='bulbasaur'  or pokemon_elegido=='3':
      printRetardado('Has elegido a bulbasaur\n')
      bulbasaur.pelea(squirtle)
      bulbasaur.centro_pokemon()
      squirtle.centro_pokemon()
  else:
      printRetardado('Pokemon no disponible')
    # print("1.-squirtle\n2.-charmander \n3.-bulbasaur")
     #pokemon_elegido= input()
     #pokemon_Elegir(pokemon_elegido)

def ataque_elegir(self):
  print("Ataques disponibles\n")
  print("1.-"+self.ataques["1"][0]+"\t 2.-"+ self.ataques["2"][0]+"\n 3.-"+ self.ataques["3"][0]+"\t 4.-"+ self.ataques["4"][0])
  ataque_recibido=input('¿Que ataque deseas utilizar?\n')
  if ataque_recibido=="1":    
    ataque_elegido=self.ataques['1']
    
  elif ataque_recibido=="2":
    ataque_elegido=self.ataques['2']

  elif ataque_recibido=="3":
    ataque_elegido=self.ataques['3']

  elif ataque_recibido=="4":
    ataque_elegido=self.ataques['4']
  else :
    cadena=('Error ataque elegido') 
    for c in cadena:
      print(c, end='')
      sys.stdout.flush()
      sleep(0.1) 
  return ataque_elegido

#Fortalezas y debilidades en ataques
def modificadorAtaque(self, pokemonCompleto,rival):
    # Imprimir información acerca de la pelea
    print("-----Modificador de ataque pokemon-----")
    # Tu rival es furte o debil a ti? 
    if self[2] in rival.fortalezas:
      modificador_ataque = 1/2
      print(f"{rival.especie} es fuerte a los ataques de {pokemonCompleto.especie} \n")
    elif self[2] in rival.debilidades:
      modificador_ataque = 2
      print(f"{rival.especie} es debil a los ataques de {pokemonCompleto.especie} \n")
    else:
      modificador_ataque = 1
      cadena='no esta\n'
      for c in cadena:
        print(c, end='')
        sys.stdout.flush()
        sleep(0.1)


    return modificador_ataque

def printRetardado(cadena):
  for c in cadena:
    print(c, end='')
    sys.stdout.flush()
    sleep(0.1)

from time import sleep
import sys
print("Te han desafiado a una pelea \n")
printRetardado("¿Que pokemon desea utilizar? \n")

print("1.-squirtle\n2.-charmander \n3.-bulbasaur")

pokemon_elegido= input()
pokemon_Elegir(pokemon_elegido)
#squirtle.pelea(charmander)
#squirtle.centro_pokemon()
#charmander.centro_pokemon()