# Seminario 2
# Juan García Santos (alu0101325583)
# Ayob Asrout Vargas (alu0101350158)

import pysmile
import pysmile_license

def setfixedValues():
  print("Enter values for:")
  fixedValues = []
  st = input("st: Atacar || Recoger_Armas || Rcoger_Energia || Explorar || Huir || Detectar_Peligro: ")
  fixedValues.append(st)
  health = input("Health: Alto || Bajo: ")
  fixedValues.append(health)
  weapon = input("Weapon: Armado || Desarmado: ")
  fixedValues.append(weapon)
  opponentWeapon = input("Opponent weapon: Armados || Desarmados: ")
  fixedValues.append(opponentWeapon)
  heardNoise = input("Heard Noise: Si || No: ")
  fixedValues.append(heardNoise)
  numberOfEnemies = input("Number of enemies: Si || No: ")
  fixedValues.append(numberOfEnemies)
  proximateWeapon = input("Proximate weapon: Si || No: ")
  fixedValues.append(proximateWeapon)
  proximateHealthpack = input("Proximate healthpack: Si || No: ")
  fixedValues.append(proximateHealthpack)
  return fixedValues

def main():
  network = pysmile.Network()
  network.read_file("Red-BotV2.xdsl")
  fixedValues = setfixedValues()
  print(fixedValues)
  usedVariables = ["St", "H", "W", "OW", "HN", "NE", "PW", "PH"]
  error_code = False

  for i in range(len(usedVariables)):
    try:
      network.set_evidence(usedVariables[i], fixedValues[i])
    except:
      print(f"The value \"{fixedValues[i]}\" is not valid for {usedVariables[i]}")
      error_code = True

  if (error_code == True):
    return -1

  network.update_beliefs()

  results = network.get_node_value("St1")

  print("\nResults:")

  for i in range(0, len(results)):
    print(network.get_outcome_id('St1', i) + " = " + str(round(float(results[i] * 100))) + " %")
  return 0

if __name__ == "__main__":
	main()