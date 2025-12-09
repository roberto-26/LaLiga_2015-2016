import csv

def LeerPartidos(): 
    listaPartidos = []
    with open('liga.csv','r', encoding='utf-8') as f:
        r = csv.reader(f)
        next(r)

        for fila in r:
            partido = {
                fila[1]+"-"+fila[2] : fila[3] 
            }

            listaPartidos.append(partido)

    return listaPartidos

def Equipos(datosliga) :
    equiposLiga = set()

    for i in range(0,len(datosliga)):
        for clave, valor in datosliga[i].items():
            equipo1 = clave.split("-")[0]
            equipo2 = clave.split("-")[1]
            equiposLiga.add(equipo1)
            equiposLiga.add(equipo2)

    return equiposLiga




prpr = LeerPartidos()

equipos = Equipos(prpr)

print(equipos)

    









