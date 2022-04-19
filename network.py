# Seminario 2
# Juan García Santos (alu0101325583)
# Ayob Asrout Vargas (alu0101350158)

import pysmile
import pysmile_license

def setEvidence():
  print("Enter values for:")
  evidence = []
  st = input("st: Atacar || Recoger_Armas || Rcoger_Energia || Explorar || Huir || Detectar_Peligro: ")
  evidence.append(st)
  health = input("Health: Alto || Bajo: ")
  evidence.append(health)
  weapon = input("Weapon: Armado || Desarmado: ")
  evidence.append(weapon)
  opponentWeapon = input("Opponent weapon: Armados || Desarmados: ")
  evidence.append(opponentWeapon)
  heardNoise = input("Heard Noise: Si || No: ")
  evidence.append(heardNoise)
  numberOfEnemies = input("Number of enemies: Si || No: ")
  evidence.append(numberOfEnemies)
  proximateWeapon = input("Proximate weapon: Si || No: ")
  evidence.append(proximateWeapon)
  proximateHealthpack = input("Proximate healthpack: Si || No: ")
  return evidence

def main():
  network = pysmile.Network()
  network.read_file("Red-BotV2.xdsl")
  evidence = ["Explorar", "Alto", "Armado", "Desarmados", "Si", "No", "Si", "Si"]
  implicatedVariables = ["St", "H", "W", "OW", "HN", "NE", "PW", "PH"]
  error_code = False

  for i in range(len(implicatedVariables)):
    try:
      network.set_evidence(implicatedVariables[i], evidence[i])
    except:
      print(f"The value \"{evidence[i]}\" is not valid for {implicatedVariables[i]}")
      error_code = True

  if (error_code == True):
    return -1

  network.update_beliefs()

  beliefs = network.get_node_value("St1")

  print("\nResults:")

  for i in range(0, len(beliefs)):
    print(network.get_outcome_id('St1', i) + " = " + str(round(float(beliefs[i] * 100))) + " %")
  return 0

if __name__ == "__main__":
	main()