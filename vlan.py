# Script VLAN

vlan = int(input("Ingrese el número de VLAN: "))

if vlan >= 1 and vlan <= 1005:
    print("La VLAN corresponde a una VLAN NORMAL")
elif vlan >= 1006 and vlan <= 4094:
    print("La VLAN corresponde a una VLAN EXTENDIDA")
else:
    print("Número de VLAN no válido")
