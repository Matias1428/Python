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
    
    # Tu rival es furte o debil a ti?
    if self.tipo in rival.fortalezas:
      modificador_ataque = 1/2
      print(f"{rival.especie} es fuerte a los ataques de {self.especie} \n")
    elif self.tipo in rival.debilidades:
      modificador_ataque = 2
      print(f"{rival.especie} es debil a los ataques de {self.especie} \n")
    else:
      modificador_ataque = 1
    
    #eres fuerte o debil a tu rival?
    if rival.tipo in self.fortalezas:
      modificador_defensa = 1/2
      print(f"{self.especie} es fuerte a los ataques de {rival.especie} \n")
    elif rival.tipo in self.debilidades:
      modificador_defensa = 2
      print(f"{self.especie} es debil a los ataques de {rival.especie} \n")
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
        print(self.especie + "_utiliza ", ataque_elegido[0])

        # atacando
        dano = int(
            self.dano_base * 
            (ataque_elegido[1] / rival.current_stats["defensa"]) * 
            modificador_ataque) 
        rival.current_stats["hp"] -= dano
        print(f"{self.especie} hizo {dano} de daño a {rival.especie}")
        print(f"A {rival.especie} le quedan {rival.current_stats['hp']} puntos de vida")
      else:
        # defendiendo
        dano = int(
            rival.dano_base *
            (rival.current_stats["ataque"] / self.current_stats["defensa"]) * 
            modificador_defensa)
        self.current_stats["hp"] -= dano
        print(f"{rival.especie} hizo {dano} de daño a {self.especie}")
        print(f"A {self.especie} le quedan {self.current_stats['hp']} puntos de vida")
      mi_turno = not mi_turno
    else:
      if self.current_stats["hp"] <= 0:
        print(f'{rival.especie} ha ganado la pelea \n')
      else:
        print(f'{self.especie} ha ganado la pelea \n')

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
      print('Has elegido a  squirtle\n')
      squirtle.pelea(charmander)
      squirtle.centro_pokemon()
      charmander.centro_pokemon()

  if pokemon_elegido=='charmander'  or pokemon_elegido=='2':
      print('Has elegido a charmander\n')
      charmander.pelea(bulbasaur)
      bulbasaur.centro_pokemon()
      charmander.centro_pokemon()

  if pokemon_elegido=='bulbasaur'  or pokemon_elegido=='3':
      print('Has elegido a bulbasaur\n')
      bulbasaur.pelea(squirtle)
      bulbasaur.centro_pokemon()
      squirtle.centro_pokemon()
  #if pokemon_elegido!='bulbasaur'  or pokemon_elegido!='3' or pokemon_elegido!='charmander'  or pokemon_elegido!='2' or pokemon_elegido!='squirtle' or pokemon_elegido!='1':
    # print('Pokemon no disponible')
    # print("1.-squirtle\n2.-charmander \n3.-bulbasaur")
     #pokemon_elegido= input()
     #pokemon_Elegir(pokemon_elegido)

def ataque_elegir(self):
  print("Ataques disponibles\n")
  print("1.-"+self.ataques["1"][0]+"\t 2.-"+ self.ataques["2"][0]+"\n 3.-"+ self.ataques["3"][0]+"\t 4.-"+ self.ataques["4"][0])
  ataque_recibido=input('¿Que ataque deseas utilizar?\n')
  if ataque_recibido=="1":    
    ataque_elegido=self.ataques['1']
    
  if ataque_recibido=="2":
    ataque_elegido=self.ataques['2']

  if ataque_recibido=="3":
    ataque_elegido=self.ataques['3']

  if ataque_recibido=="4":
    ataque_elegido=self.ataques['4']
    
  return ataque_elegido

print("Te han desafiado a una pelea \n")
print("¿Que pokemon desea utilizar? \n")
print("1.-squirtle\n2.-charmander \n3.-bulbasaur")
pokemon_elegido= input()
pokemon_Elegir(pokemon_elegido)
#squirtle.pelea(charmander)
#squirtle.centro_pokemon()
#charmander.centro_pokemon()