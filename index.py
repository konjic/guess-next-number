from random import randrange
from random import choice


nr_vieti = 3
scor = 0

current_nr=randrange(10)
nr_viitor= randrange(10)


if nr_viitor is current_nr:
            nr_viitor=choice([i for i in range(0,10) if i not in [current_nr]])

print("\nNumerele pornesc de la 0 si se opresc la 10")

while nr_vieti !=0:

    print("\nNUMAR VIETI",nr_vieti)
    print("SCORUL TAU : ", scor)
    print("NUMAR CURENT: ", current_nr)
    alegere=input("Scrie 1 daca urmatorul nr este mai mare. Scrie 0 daca urmatorul nr este mai mic \n")
    

    if alegere not in ("0","1"):
        print("Nr interzis. 0 sau 1")
        continue
    

    if alegere == "0":
        if nr_viitor is current_nr:
            nr_viitor=choice([i for i in range(0,10) if i not in [current_nr]])

        if nr_viitor < current_nr:
            
            
            print("RASPUNS CORECT")
            scor=scor+1
            print("SCORUL TAU:", scor)
            current_nr = nr_viitor
            nr_viitor= randrange(10)
        else:
            
            
            print("RASPUNS GRESIT")
            nr_vieti=nr_vieti-1
            current_nr = nr_viitor
            nr_viitor= randrange(10)

    if alegere == "1":
        if nr_viitor is current_nr:
            nr_viitor=choice([i for i in range(0,10) if i not in [current_nr]])

        if nr_viitor > current_nr:

            
            print("RASPUNS CORECT")
            scor=scor+1
            print("SCORUL TAU:", scor)
            current_nr = nr_viitor
            nr_viitor= randrange(10)
        else:

            print("RASPUNS GRESIT")
            nr_vieti=nr_vieti-1
            current_nr = nr_viitor
            nr_viitor= randrange(10)

        
        