import random
import numpy as np
from os import system


class Personaje:

    def __init__(self, nombre = "", fuerza = 0, inteligencia = 0, defensa = 0, vida = 0, vidaMaxima = 0, velocidad = 0, mochila = []):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida
        self.vidaMaxima = vidaMaxima
        self.velocidad = velocidad
        self.mochila = mochila

    def atributos(self):
        print(self.nombre)
        print("tipo:", (self.__class__.__name__) )
        print("·Fuerza:", self.fuerza)
        print("·Inteligencia:", self.inteligencia)
        print("·Defensa:", self.defensa)
        print("·Vida:", self.vida)
        print("·Velocidad:",self.velocidad)
        print("·Mochila:",self.mochila)

    def esta_vivo(self):
        return self.vida > 0

    def morir(self):
        self.vida = 0
        print("\n",self.nombre, "ha muerto")

    def daño(self, enemigo):
        return self.fuerza - enemigo.defensa

    def atacar(pj, enemigo):

      if (enemigo.__class__.__name__) == "Tanque":
        Tanque.atacarTanque(pj, enemigo)

      elif (enemigo.__class__.__name__) == "Espinas":
        Espinas.atacarEspinas(pj, enemigo)

      elif (enemigo.__class__.__name__) == "Ninja":
        Ninja.atacarNinja(pj, enemigo)

      else:
        daño = pj.daño(enemigo)
        enemigo.vida -= daño
        print("\n",pj.nombre, "ha realizado", daño, "puntos de daño a", enemigo.nombre)

      if enemigo.esta_vivo():
          print("Vida de", enemigo.nombre, "es", round(enemigo.vida, 4))
      else:
          enemigo.morir()

    def start():
      ###Data de los atributos de guerrero         nombre, fuerza, inteligencia, defensa, vida, vidaMaxima, espada, velocidad, mochila
      guerrero = Guerrero("Kelius", 20, 10, 6, 100, 100, 8, 150, [2,2])

      ###Data de los atributos de mago          nombre, fuerza, inteligencia, defensa, vida, vidaMaxima, libro, velocidad, mochila
      mago = Mago("Vanessa", 5, 30, 4, 75, 75, 3, 120, [2,1])

      ###Data de los atributos de asesino       nombre, fuerza, inteligencia, defensa, vida, vidaMaxima, velocidad, mochila
      asesino = Asesino("Erzsébet", 30, 10, 4, 65, 65, 200, [1,2])

      ###Data de los atributos de Tirador       nombre, fuerza, inteligencia, defensa, vida, vidaMaxima, velocidad, critico, mochila
      tirador = Tirador("Mr. Yaya",23, 8, 3, 60, 60, 210, 25, [3,1])

      ###Data de los atributos de Tanque        nombre, fuerza, inteligencia, defensa, vida, vidaMaxima, velocidad, escudo, turnos, mochila
      tanque = Tanque("Grogi", 11, 4, 15, 120, 120, 30, 25, 0, [2,1])

      ###Data de los atributos de ladron        nombre, fuerza, inteligencia, defensa, vida, vidaMaxima, velocidad, mochila
      ladron = Ladron("Francis", 15, 4, 5, 70, 70, 215, [2,1])      #roba stats

      ###Data de los atributos de espinas       nombre, fuerza, inteligencia, defensa, vida, vidaMaxima, velocidad, mochila
      espinas = Espinas("Yushen", 15, 6, 7, 75, 75, 125, [3,3])

      ###Data de los atributos de ninja         nombre, fuerza, inteligencia, defensa, vida, vidaMaxima, katana, velocidad, mochila
      ninja = Ninja("Lee shu", 20, 30, 9, 85, 85, 6, 145, [2,1] )

      pjs = [guerrero, mago, asesino, tirador, tanque, ladron, espinas, ninja]

      return Personaje.EleccionJuego(pjs)

    def verificaDefensa(pj, enemigo):                    #hace que el enemigo no pueda tener más defensa o igual que tu ataque, para hacer que siempre tengas la posibilidad de hacerle 3 de daño como minimo
      if enemigo.defensa >= (pj.fuerza - 3):
        enemigo.defensa = pj.fuerza - 3

      return enemigo.defensa

    def EleccionJuego(pjs):
      print("\nIngrese el modo de juego que quiere jugar \n1: PVE, juegas contra la maquina. \n2: PVP, jugador contra jugador. \n3: Mapa, recorres un mapa en el que tendras que derrotar a todos los enemigos dentro del mapa para ganar")
      eleccion = int(input("Ingrese el numero correspondiente al modo que quiere jugar: "))
      if eleccion == 1:
        return Personaje.EleccionPVE(pjs)
      elif eleccion == 2:
        return Personaje.EleccionPVP(pjs)
      elif eleccion == 3:
        return Personaje.jugarMapa(pjs)
      else:
        print("Opcion incorrecta. Intente nuevamente")
        return Personaje.ElecionJuego(pjs)

    def TurnoJugador(jugador, cpu):
      Personaje.verificaDefensa(jugador, cpu)
      print("1 Atacar \n2 Mochila")
      accion = int(input("Ingrese el numero de la accion: "))

      if accion == 1:
        return Personaje.atacar(jugador, cpu)

      elif accion == 2:

        return Personaje.MochilaJugador(jugador, cpu)

      else:
        print("\nEl numero que ha ingresado no corresponde a ninguna accion. Intente nuevamente")
        Personaje.TurnoJugador(jugador, cpu)

    def UsarPocionVida(pj, cpu):
      if (pj.vida+50) >= pj.vidaMaxima:
        pj.vida = pj.vidaMaxima
        print("\nLa vida de ",pj.nombre,"aumento a",pj.vida)
      else:
        pj.vida += 50

      Personaje.atacar(pj, cpu)
      return pj.vida

    def UsarPocionFuerza(pj, cpu):
      pj.fuerza *= 1.5
      Personaje.atacar(pj, cpu)
      pj.fuerza /= 1.5
      return pj.fuerza

    def MochilaJugador(jugador, cpu):
      print("\nCant de pociones de vida: ",jugador.mochila[0], "\nCant de pociones de fuerza: ",jugador.mochila[1] )
      eleccion = int(input("Ingrese su eleccion: "))

      if eleccion == 1:

        if jugador.mochila[0] > 0:
          jugador.mochila[0] = jugador.mochila[0] - 1
          return Personaje.UsarPocionVida(jugador, cpu)
        else:
          print("\nNo quedan más pociones de vida. Intente otra accion o ingrese `3` para atacar")
          return Personaje.MochilaJugador(jugador, cpu)

      elif eleccion == 2:

        if jugador.mochila[1] > 0:
          jugador.mochila[1] = jugador.mochila[1] - 1
          return Personaje.UsarPocionFuerza(jugador, cpu)
        else:
          print("\nNo quedan más pociones de fuerza. Intente otra accion o ingrese `3` para atacar")
          return Personaje.MochilaJugador(jugador, cpu)

      elif eleccion == 3:
        return Personaje.atacar(jugador, cpu)

      else:
        print("\nLa eleccion que escogio no es valida, intente nuevamente")
        Personaje.MochilaJugador(jugador, cpu)

    def TurnoCPU(cpu, jugador, turno):
      Personaje.verificaDefensa(cpu,jugador)
      if cpu.vida < 35:

        if cpu.mochila[0] > 0:
          cpu.mochila[0] = cpu.mochila[0] - 1
          return Personaje.UsarPocionVida(cpu, jugador)

        else:
          return Personaje.atacar(cpu, jugador)

      elif turno % 3 == 0:

        if cpu.mochila[1] > 0:
          cpu.mochila[1] = cpu.mochila[1] - 1
          return Personaje.UsarPocionFuerza(cpu, jugador)

        else:
          return Personaje.atacar(cpu, jugador)

      else:
        return Personaje.atacar(cpu, jugador)

    def EleccionPVE(vc):
      system("cls")
      for i in vc:
        i.atributos()
        print("\n")

      pick = int(input("Elija el personaje que quiere utilizar: "))
      if pick > 0 and pick <= (len(vc)-1):
        player = vc[pick-1]
        system("cls")
        print("\nHas elegido a", vc[pick-1].nombre)
        vc.pop(pick-1)
      else:
        print("\nLa opcion que escogio es incorrecta. Intente nuevamente")
        return Personaje.EleccionPVE(vc)

      r = random.randint(0,len(vc)-1)
      cpu = vc[r]
      print("\nTe enfrentaras a", vc[r].nombre)

      return Personaje.PVE(player, cpu)

    def EleccionPVP(vc):
      system("cls")
      for i in vc:
        i.atributos()
        print("\n")

      pick1 = int(input("\nJugador 1: Elija el personaje que quiere utilizar: "))
      pick2 = int(input("\nJugador 2:  Elija el personaje que quiere utilizar: "))
      if pick1 >= 1 and pick1 <= len(vc) and pick2 >= 0 and pick2 <= len(vc):
        system("cls")
        player1 = vc[pick1-1]
        print("\n Jugador 1 Has elegido a", vc[pick1-1].nombre)
        player2 = vc[pick2-1]
        print("\n Jugador 2 Has elegido a", vc[pick2-1].nombre)
        return Personaje.PVP(player1, player2)

      else:
        print("\nLa opcion que escogio es incorrecta. Intente nuevamente")
        return Personaje.EleccionPVP(vc)

    def eleccionMapa(vc):
      system("cls")
      for i in vc:
        i.atributos()
        print("\n")

      pick = int(input("\nJugador: Elija el personaje que quiere utilizar: "))
      system("cls")
      if pick > 0 and pick < (len(vc)):
        player = vc[pick-1]
        
        print("\nHas elegido a", player.nombre)
        vc.pop(pick-1)
        return player, vc
      else:
        print("\nLa opcion que escogio es incorrecta. Intente nuevamente")
        return Personaje.eleccionMapa(vc)


    def jugarMapa(pjs):
      matriz_Backend = np.empty((10, 10), dtype=object)
      matriz_Frontend = np.empty((10, 10), dtype=str)

      matriz_Frontend = Personaje.llenar(matriz_Frontend)
      x, pjs = Personaje.eleccionMapa(pjs)
      matriz_Backend, matriz_Frontend = Personaje.pos_inicial(matriz_Backend, matriz_Frontend, x)
      matriz_Backend, matriz_Frontend = Personaje.pos_enemigos(matriz_Backend, matriz_Frontend, len(pjs), pjs)
      return Personaje.mover(matriz_Backend, matriz_Frontend, x)

    def encontrar(matriz, letra): 
      for i in range(len(matriz)):
        for j in range(len(matriz[0])):
          if matriz[i][j] == letra:
            return i, j


    def mover(matriz_Backend, matriz_Frontend, pj):
      validacion = True
    
      while validacion == True:
        system("cls")
        print("Usted es:",pj.nombre, " su nombre en el mapa se ve reflejado con una", pj.nombre[0])
        print("Vida:", pj.vida, "pociones de fuerza y vida:", pj.mochila[0],pj.mochila[1])
        print(matriz_Frontend)
        fila_p, columna_p = Personaje.encontrar(matriz_Frontend, pj.nombre[0])
        move = input("ingrese W(arriba), A(izquierda), S(abajo), D(derecha): ")
        system("cls")
        if move.upper() == "W":
          matriz_Backend, matriz_Frontend, validacion = Personaje.moverUp(matriz_Backend, matriz_Frontend, fila_p, columna_p, pj)

        elif move.upper() == "S":
          matriz_Backend, matriz_Frontend, validacion = Personaje.moverDown(matriz_Backend, matriz_Frontend, fila_p, columna_p, pj)

        elif move.upper() == "A":
          matriz_Backend, matriz_Frontend, validacion = Personaje.moverIzq(matriz_Backend, matriz_Frontend, fila_p, columna_p, pj)

        elif move.upper() == "D":
          matriz_Backend, matriz_Frontend, validacion = Personaje.moverDer(matriz_Backend, matriz_Frontend, fila_p, columna_p, pj)
        else:
          print("la opcion que escogio es invalida. Intente nuevamente")
      print("El juego termino")

    def moverUp(matriz_Backend, matriz_Frontend,  fp, cp, pj):

      if matriz_Frontend[fp-1][cp] != "*":
        x = input("ingrese la opcion que prefiera: \n1)Batalla Manual \n2)Batalla Automatica")
        if x == "2":
          if Personaje.EVE(pj, matriz_Backend[fp-1][cp]):
            matriz_Frontend[fp-1][cp] = pj.nombre[0]
            matriz_Frontend[fp][cp] = "*"

            matriz_Backend[fp-1][cp] = matriz_Backend[fp][cp]
            matriz_Backend[fp][cp] = "*"
          else:
            return matriz_Backend, matriz_Frontend, False

        elif x == "1":
          if Personaje.PVE(pj, matriz_Backend[fp-1][cp]):
            matriz_Frontend[fp-1][cp] = pj.nombre[0]
            matriz_Frontend[fp][cp] = "*"

            matriz_Backend[fp-1][cp] = matriz_Backend[fp][cp]
            matriz_Backend[fp][cp] = "*"
          else:
            return matriz_Backend, matriz_Frontend, False

      else:
        matriz_Frontend[fp-1][cp] = pj.nombre[0]
        matriz_Frontend[fp][cp] = "*"
      return matriz_Backend, matriz_Frontend, True

    def moverDown(matriz_Backend, matriz_Frontend,  fp, cp, pj):

      if matriz_Frontend[fp+1][cp] != "*":
        x = input("ingrese la opcion que prefiera: \n1)Batalla Manual \n2)Batalla Automatica")
        if x == "2":
          if Personaje.EVE(pj, matriz_Backend[fp+1][cp]):
            matriz_Frontend[fp+1][cp] = pj.nombre[0]
            matriz_Frontend[fp][cp] = "*"

            matriz_Backend[fp+1][cp] = matriz_Backend[fp][cp]
            matriz_Backend[fp][cp] = "*"
          else:
            return matriz_Backend, matriz_Frontend, False

        elif x == "1":
          if Personaje.PVE(pj, matriz_Backend[fp+1][cp]):
            matriz_Frontend[fp+1][cp] = pj.nombre[0]
            matriz_Frontend[fp][cp] = "*"

            matriz_Backend[fp+1][cp] = matriz_Backend[fp][cp]
            matriz_Backend[fp][cp] = "*"
          else:
            return matriz_Backend, matriz_Frontend, False

      else:
        matriz_Frontend[fp+1][cp] = pj.nombre[0]
        matriz_Frontend[fp][cp] = "*"
      return matriz_Backend, matriz_Frontend, True

    def moverIzq(matriz_Backend, matriz_Frontend,  fp, cp, pj):

      if matriz_Frontend[fp][cp-1] != "*":
        x = input("ingrese la opcion que prefiera: \n1)Batalla Manual \n2)Batalla Automatica")
        if x == "2":
          if Personaje.EVE(pj, matriz_Backend[fp][cp-1]):
            matriz_Frontend[fp][cp-1] = pj.nombre[0]
            matriz_Frontend[fp][cp] = "*"

            matriz_Backend[fp][cp-1] = matriz_Backend[fp][cp]
            matriz_Backend[fp][cp] = "*"
          else:
            return matriz_Backend, matriz_Frontend, False

        elif x == "1":
          if Personaje.PVE(pj, matriz_Backend[fp][cp-1]):
            matriz_Frontend[fp][cp-1] = pj.nombre[0]
            matriz_Frontend[fp][cp] = "*"

            matriz_Backend[fp][cp-1] = matriz_Backend[fp][cp]
            matriz_Backend[fp][cp] = "*"
          else:
            return matriz_Backend, matriz_Frontend, False

      else:
        matriz_Frontend[fp][cp-1] = pj.nombre[0]
        matriz_Frontend[fp][cp] = "*"
      return matriz_Backend, matriz_Frontend, True

    def moverDer(matriz_Backend, matriz_Frontend,  fp, cp, pj):

      if matriz_Frontend[fp][cp+1] != "*":
        x = input("ingrese la opcion que prefiera: \n1)Batalla Manual \n2)Batalla Automatica")
        if x == "2":
          if Personaje.EVE(pj, matriz_Backend[fp][cp+1]):
            matriz_Frontend[fp][cp+1] = pj.nombre[0]
            matriz_Frontend[fp][cp] = "*"

            matriz_Backend[fp][cp+1] = matriz_Backend[fp][cp]
            matriz_Backend[fp][cp] = "*"
          else:
            return matriz_Backend, matriz_Frontend, False

        elif x == "1":
          if Personaje.PVE(pj, matriz_Backend[fp][cp+1]):
            matriz_Frontend[fp][cp+1] = pj.nombre[0]
            matriz_Frontend[fp][cp] = "*"

            matriz_Backend[fp][cp+1] = matriz_Backend[fp][cp]
            matriz_Backend[fp][cp] = "*"
          else:
            return matriz_Backend, matriz_Frontend, False

      else:
        matriz_Frontend[fp][cp+1] = pj.nombre[0]
        matriz_Frontend[fp][cp] = "*"
      return matriz_Backend, matriz_Frontend, True

    def pos_inicial(matriz_Backend, matriz_Frontend, pj):   #funciona
      filas = matriz_Backend.shape[0]
      columnas = matriz_Backend.shape[1]

      rf = random.randint(0,filas-1)
      rc = random.randint(0,columnas-1)

      matriz_Backend[rf][rc] = pj
      matriz_Frontend[rf][rc] = pj.nombre.upper()
      return matriz_Backend, matriz_Frontend

    def pos_enemigos(matriz_Backend, matriz_Frontend, enemigos_totales, enemigos):  #funciona

      for i in range(enemigos_totales // 2):

        filas = matriz_Frontend.shape[0]
        columnas = matriz_Frontend.shape[1]

        rf = random.randint(0,filas-1)
        rc = random.randint(0,columnas-1)

        v = False
        while( v == False):
          if matriz_Frontend[rf][rc] == "*":
            x = random.randint(0, enemigos_totales-1)

            e = enemigos[x]
            enemigos.pop(x)
            enemigos_totales -= 1

            matriz_Backend[rf][rc] = e
            matriz_Frontend[rf][rc] = e.nombre
            v = True

      return matriz_Backend, matriz_Frontend

    def llenar(matriz):   #funciona
      for i in range(len(matriz)):
        for j in range(len(matriz)):
          matriz[i][j] = "*"
      return matriz


###############################

################### PVE #######################

    def PVE(player, cpu):
      turno = 1

      if player.velocidad > cpu.velocidad:

        while player.esta_vivo() and cpu.esta_vivo():

          print("\nTurno", turno)
          print("\n >>> Acción de ", player.nombre,":")

          Personaje.TurnoJugador(player, cpu)

          if cpu.esta_vivo():
            print("\n >>> Acción de ", cpu.nombre,":")
            Personaje.TurnoCPU(cpu, player , turno)

            turno = turno + 1

            if player.esta_vivo() == False:
              print("\nHa ganado", cpu.nombre)
              return False

          else:
            print("\nHa ganado", player.nombre)
            return True

      elif player.velocidad < cpu.velocidad:

        while cpu.esta_vivo() and player.esta_vivo():

          print("\nTurno", turno)
          print("\n >>> Acción de ", cpu.nombre,":")

          Personaje.TurnoCPU(cpu, player , turno)

          if player.esta_vivo():
            print("\n >>> Acción de ", player.nombre,":")
            Personaje.TurnoJugador(player, cpu)

            turno = turno + 1

            if cpu.esta_vivo() == False:
              print("\nHa ganado", player.nombre)
              return True

          else:
            print("\nHa ganado", cpu.nombre)
            return False


##################### PVP #######################

    def PVP(player1, player2):
      turno = 1

      if player1.velocidad > player2.velocidad :

        while player1.esta_vivo() and player2.esta_vivo():

          print("\nTurno", turno)
          print("\n >>> Acción de ", player1.nombre,":")

          Personaje.TurnoJugador(player1, player2)

          if player2.esta_vivo():
            print("\n >>> Acción de ", player2.nombre,":")
            Personaje.TurnoJugador(player2, player1)

            turno = turno + 1

            if player1.esta_vivo() == False:
              print("\nHa ganado", player2.nombre)

          else:
            print("\nHa ganado", player1.nombre)

      elif player1.velocidad < player2.velocidad:

        while player2.esta_vivo() and player1.esta_vivo():

          print("\nTurno", turno)
          print("\n >>> Acción de ", player2.nombre,":")

          Personaje.TurnoJugador(player2, player1)

          if player1.esta_vivo():
            print("\n >>> Acción de ", player1.nombre,":")
            Personaje.TurnoJugador(player1, player2)

            turno = turno + 1

            if player2.esta_vivo() == False:
              print("\nHa ganado", player1.nombre)

          else:
            print("\nHa ganado", player2.nombre)

      else:
        while player1.esta_vivo() and player2.esta_vivo():

          print("\nTurno", turno)
          print("\n >>> Acción de ", player1.nombre,":")

          Personaje.TurnoJugador(player1, player2)

          if player2.esta_vivo():
            print("\n >>> Acción de ", player2.nombre,":")
            Personaje.TurnoJugador(player2, player1)

            turno = turno + 1

            if player1.esta_vivo() == False:
              print("\nHa ganado", player2.nombre)

          else:
            print("\nHa ganado", player1.nombre)


########################### PVE (para probar los enfrentamientos) ###################################################

    def EVE(cpu1, cpu2):
      turno = 1

      if cpu1.velocidad > cpu2.velocidad:

        while cpu1.esta_vivo() and cpu2.esta_vivo():

          print("\nTurno", turno)
          print("\n >>> Acción de ", cpu1.nombre,":")

          Personaje.TurnoCPU(cpu1, cpu2, turno)

          if cpu2.esta_vivo():
            print("\n >>> Acción de ", cpu2.nombre,":")
            Personaje.TurnoCPU(cpu2, cpu1 , turno)

            turno = turno + 1

            if cpu1.esta_vivo() == False:
              print("\nHa ganado", cpu2.nombre)
              n = input("ingrese cualquier cosa para continuar con el juego: ")
              return False

          else:
            print("\nHa ganado", cpu1.nombre)
            n = input("ingrese cualquier cosa para continuar con el juego: ")
            return True

      elif cpu1.velocidad < cpu2.velocidad:

        while cpu2.esta_vivo() and cpu1.esta_vivo():

          print("\nTurno", turno)
          print("\n >>> Acción de ", cpu2.nombre,":")

          Personaje.TurnoCPU(cpu2, cpu1 , turno)

          if cpu1.esta_vivo():
            print("\n >>> Acción de ", cpu1.nombre,":")
            Personaje.TurnoCPU(cpu1, cpu2, turno)

            turno = turno + 1

            if cpu2.esta_vivo() == False:
              print("\nHa ganado", cpu1.nombre)
              n = input("ingrese cualquier cosa para continuar con el juego: ")
              return True

          else:
            print("\nHa ganado", cpu2.nombre)
            n = input("ingrese cualquier cosa para continuar con el juego: ")
            return False




############################################

class Guerrero(Personaje):

    def __init__(self, nombre = "", fuerza = 0, inteligencia = 0, defensa = 0, vida = 0, vidaMaxima = 0, espada = 0, velocidad = 0, mochila = [] ):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida, vidaMaxima, velocidad, mochila)
        self.espada = espada

    def atributos(self):
        super().atributos()
        print("·Espada:", self.espada)
        print("·Caracteristica: Tiene una espada que hace que",self.nombre,"haga más daño")

    def daño(self, enemigo):
        return self.fuerza + self.espada - enemigo.defensa

class Mago(Personaje):

    def __init__(self, nombre = "", fuerza = 0, inteligencia = 0, defensa = 0, vida = 0, vidaMaxima = 0, libro = 0, velocidad = 0, mochila = [] ):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida,vidaMaxima, velocidad, mochila)
        self.libro = libro

    def atributos(self):
        super().atributos()
        print("·Libro:", self.libro)
        print("·Caracteristica: Tiene un libro que hace que",self.nombre,"haga más daño")

    def daño(self, enemigo):
        return self.inteligencia + self.libro - enemigo.defensa

class Asesino(Personaje):

    def __init__(self, nombre = "", fuerza = 0, inteligencia = 0, defensa = 0, vida = 0, vidaMaxima = 0, velocidad = 0, mochila = [] ):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida, vidaMaxima, velocidad, mochila)

    def atributos(self):
        super().atributos()
        print("·Caracteristica:",self.nombre,"se cura una cantidad de vida dependiendo del daño que le haga al enemigo")

    def daño(self, enemigo):
      daño = self.fuerza - enemigo.defensa

      x = random.randint(0,100)
      if x <= 20:
        daño = daño * 1.5
        print("\n¡Golpe Critico!")
        self.vida += 5 + (daño // 7)
        if self.vida > self.vidaMaxima:
          self.vida = self.vidaMaxima
        print("\nVida de",self.nombre,"aumento a ",self.vida)

      else:
        self.vida += 5

      return daño

class Tirador(Personaje):

    def __init__(self, nombre = "", fuerza = 0, inteligencia = 0, defensa = 0, vida = 0, vidaMaxima = 0, velocidad = 0, critico = 0, mochila = []):
      super().__init__(nombre, fuerza, inteligencia, defensa, vida, vidaMaxima, velocidad, mochila)
      self.critico = critico

    def atributos(self):
        super().atributos()
        print("·Critico:", self.critico)
        print("·Caracteristica:",self.nombre,"tiene un 25% de posibilidades de hacer un ataque con un x2 de daño, si este 25% no se cumple tiene otro 25% de hacer un ataque con un x1.3 de daño")

    def daño(self, enemigo):
      daño = self.fuerza - enemigo.defensa

      x = random.randint(0,100)
      if x <= self.critico:
        daño *= 2
        print("\n¡Golpe Critico!")

      elif x > self.critico and x <= (self.critico*2):
        daño *= 1.3
        daño = round(daño,2)

      return daño

class Tanque(Personaje):

    def __init__(self, nombre = "", fuerza = 0, inteligencia = 0, defensa = 0, vida = 0, vidaMaxima = 0, velocidad = 0, escudo = 0, turnos = 0, mochila = []):
      super().__init__(nombre, fuerza, inteligencia, defensa, vida, vidaMaxima, velocidad, mochila)
      self.escudo = escudo
      self.turnos = turnos

    def atributos(self):
      super().atributos()
      print("·Escudo:",self.escudo)
      print("·Caracteristica:",self.nombre,"tiene un escudo de",self.escudo,"vida el cual evita que le puedan hacer daño a",self.nombre,"\nCuando se rompe el escudo",self.nombre,"podra recibir daño y tendra que esperar 5 turnos hasta que se le repare el escudo")


    def atacarTanque(pj, enemigo):
      if enemigo.escudo > 0:
        daño = round(pj.daño(enemigo),4)
        enemigo.escudo -= daño
        print("\n",pj.nombre, "ha realizado", daño, "puntos de daño al escudo de",enemigo.nombre)

        if enemigo.escudo > 0:
          print("\nAl escudo le queda", round(enemigo.escudo, 4), "puntos de daño")
        else:
          daño = round(enemigo.escudo * (-1), 4)
          enemigo.vida -= daño
          print("\nSe ha roto el escudo y",pj.nombre, "ha realizado", daño, "puntos de daño a", enemigo.nombre)

      else:
        if enemigo.turnos != 5:
          daño = pj.daño(enemigo)
          enemigo.vida -= daño
          print("\n",pj.nombre, "ha realizado", daño, "puntos de daño a", enemigo.nombre)
          enemigo.turnos += 1


        elif enemigo.turnos == 5:
          print("\n El escudo de", enemigo.nombre, "se ha reparado")
          enemigo.escudo = 15

class Ladron(Personaje):

    def __init__(self, nombre = "", fuerza = 0, inteligencia = 0, defensa = 0, vida = 0, vidaMaxima = 0, velocidad = 0, mochila = []):
      super().__init__(nombre, fuerza, inteligencia, defensa, vida, vidaMaxima,  velocidad, mochila)

    def atributos(self):
        super().atributos()
        print("·Caracteristica:",self.nombre,"puede robar parte de las estadisticas del enemigo por turno")

    def restablercerStats(self):
      self.defensa = 5
      self.fuerza = 15

    def daño(self, enemigo):

      self.restablercerStats()
      l = random.randint(0,2)
      if l == 0:
        self.fuerza += (enemigo.fuerza // 3)
        print("\n",self.nombre,"ha robado",(enemigo.fuerza // 3),"de fuerza a",enemigo.nombre)
        print("\nFuerza de",self.nombre,"aumento a ",self.fuerza)

      elif l == 1:
        self.defensa += (enemigo.defensa // 4)
        print("\n",self.nombre,"ha robado",(enemigo.defensa // 4),"de defensa a",enemigo.nombre)
        print("\nDefensa de",self.nombre,"aumento a ",self.defensa)

      else:
        self.vida += (enemigo.vida // 6)
        if self.vida > self.vidaMaxima:
          self.vida = self.vidaMaxima
        print("\n",self.nombre,"ha robado",(enemigo.vida // 4),"de vida a",enemigo.nombre)
        print("\nVida de",self.nombre,"aumento a ",self.vida)

      return self.fuerza - enemigo.defensa

class Espinas(Personaje):
    def __init__(self, nombre = "", fuerza = 0, inteligencia = 0, defensa = 0, vida = 0, vidaMaxima = 0, velocidad = 0, mochila = []):
      super().__init__(nombre, fuerza, inteligencia, defensa, vida, vidaMaxima,  velocidad, mochila)

    def atributos(self):
        super().atributos()
        print("·Caracteristica:",self.nombre,"refleja parte del daño que recibe")

    def atacarEspinas(pj, enemigo):
      daño = pj.daño(enemigo)
      enemigo.vida -= daño
      pj.vida -= daño // 5
      print("\n",pj.nombre, "ha realizado", daño, "puntos de daño a", enemigo.nombre)
      print("\n",enemigo.nombre, "ha reflejado",(daño // 5),"a",pj.nombre)


class Ninja(Personaje):
  def __init__(self, nombre = "", fuerza = 0, inteligencia = 0, defensa = 0, vida = 0, vidaMaxima = 0, katana = 0, velocidad = 0, mochila = []):
    super().__init__(nombre, fuerza, inteligencia, defensa, vida, vidaMaxima,  velocidad, mochila)
    self.katana = katana

  def atributos(self):
    super().atributos()
    print("·Caracteristica:",self.nombre," tiene un 25% de esquivar ataques enemigos y una posiblidad del 10% de hacer un counter atack")

  def daño(self, enemigo):
    return (self.fuerza + self.katana) - enemigo.defensa

  def atacarNinja(pj, enemigo):
    x = random.randint(1, 100)
    if x > 25:
      daño = pj.daño(enemigo)
      enemigo.vida -= round(daño)
      print("\n",pj.nombre, "ha realizado", round(daño), "puntos de daño a", enemigo.nombre)

    elif x < 10:
      daño = enemigo.daño(pj) / 3
      pj.vida -= round(daño)
      print("\n",enemigo.nombre,"ha realizado un counter atack de",round(daño),"puntos de daño a",pj.nombre)
      print("\nVida de",pj.nombre,"es",pj.vida)

    else:
      print("\n",enemigo.nombre,"ha esquivado el ataque de",pj.nombre)

class Bombardero(Personaje):      

  def __init__(self, nombre = "", fuerza = 0, inteligencia = 0, defensa = 0, vida = 0, vidaMaxima = 0,velocidad = 0, mochila = []):
    super().__init__(nombre, fuerza, inteligencia, defensa, vida, vidaMaxima,  velocidad, mochila)

  def atributos(self):
    super().atributos()
    print("·Caracteristica:",self.nombre,"tira entre 1 a 3 dinamitas, dependiendo la cantidad que tire el daño se mulplica por estas mismas lanzadas, pero mientras más dinamitas sean menos precision tendra",self.nombre,"haciendo que pueda solo acertar una dinamita, ademas de que cuando lo ataquen podra activarse algun explosivo haciendo daño en area que afectaria a ambos personajes")

  def daño(self,enemigo):
    dinamitas = random.randint(1,3)
    x = random.randint(15)

    if dinamitas == 3:

      if x <= 5:
        daño = (self.fuerza * dinamitas) - enemigo.defensa
        enemigo.vida -= daño
        print("\n",self.nombre,"ha realizado",daño,"puntos de daño a",enemigo.nombre)

      elif x > 5 and x <= 10:
        daño = (self.fuerza * 2) - enemigo.defensa
        enemigo.vida -= daño
        print("\n",self.nombre,"ha realizado",daño,"puntos de daño a",enemigo.nombre)

      else:
        daño = self.fuerza - enemigo.defensa
        enemigo.vida -= daño
        print("\n",self.nombre,"ha realizado",daño,"puntos de daño a",enemigo.nombre)

    elif dinamitas == 2:
      if x <= 5:
        daño = (self.fuerza * dinamitas) - enemigo.defensa
        enemigo.vida -= daño
        print("\n",self.nombre,"ha realizado",daño,"puntos de daño a",enemigo.nombre)

      else:
        daño = self.fuerza - enemigo.defensa
        enemigo.vida -= daño
        print("\n",self.nombre,"ha realizado",daño,"puntos de daño a",enemigo.nombre)

    else:
      daño = self.fuerza - enemigo.defensa
      enemigo.vida -= daño
      print("\n",self.nombre,"ha realizado",daño,"puntos de daño a",enemigo.nombre)


  def atacarBombardero(pj, enemigo):
    x = random.randint(1,100)
    if x >= 20:
      daño = pj.fuerza - enemigo.defensa
      print("\n",pj.nombre,"al atacar a",enemigo.nombre,"activo uno de sus explosivos haciendo que ambos reciban daño")
      total  = (daño) + enemigo.fuerza - enemigo.defensa
      enemigo.vida -= total
      print("\n",enemigo.nombre,"ha recibido un total de",total,"puntos de daño")
      total = (enemigo.fuerza - pj.defensa) // 3
      pj.vida -= total
      print("\nMientras que",pj.nombre,"recibio",total,"puntos de daño")

    else:
      daño = pj.fuerza - enemigo.defensa
      enemigo.vida -= daño
      print("\n",pj.nombre,"ha realizado",daño,"puntos de daño a",enemigo.nombre)



Personaje.start()
