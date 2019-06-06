from creatures.player import Player
from room import Room
from creatures.ork import Ork

def main():

    obyvacka = Room("Obyvacka", "Stojis v strede obyvacky, je tu jeden hnedy gauc, par policiek a telka.\nNa vychod od teba sa nachadza chodba.")
    chodba = Room("chodba", "Stojis v chladnej a prazdnej chodbe.\nNa vychod od teba je kuchyna, na zapad je obyvacka.")
    kuchyna = Room("Kuchyna", "Stojis v pekne vymalovanej standardne vybavenej kuchyni... \nNa zapad od teba sa nachadza chodba.")

    obyvacka.coordinates = [0,0,0,chodba]
    chodba.coordinates = [0,0,obyvacka,kuchyna]
    kuchyna.coordinates = [0,0,chodba,0]

    player = Player("Lukas", 100, chodba)

    ork = Ork()
    ork.printHealth()
    chodba.addCreature(ork)

    print(player.location.getDescription())

    while True:
        command = input()
        if command == "a" or command == "attack":
            player.attack(ork)
            ork.printHealth()
        if command == "n" or command == "north":
            if player.location.coordinates[0] == 0:
                print("You can not go there!")
            else:
                player.location = player.location.coordinates[0]
                print(player.location.getDescription())

        if command == "s" or command == "south":
            if player.location.coordinates[1] == 0:
                print("You can not go there!")
            else:
                player.location = player.location.coordinates[1]
                print(player.location.getDescription())

        if command == "w" or command == "west":
                if player.location.coordinates[2] == 0:
                    print("You can not go there!")
                else:
                    player.location = player.location.coordinates[2]
                    print(player.location.getDescription())

        if command == "e" or command == "east":
            if player.location.coordinates[3] == 0:
                print("You can not go there!")
            else:
                player.location = player.location.coordinates[3]
                print(player.location.getDescription())

        if command == "end":
            break

main()