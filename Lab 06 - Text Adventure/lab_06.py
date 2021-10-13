class Room:

    def __init__(self, description, north, south, east, west):
        self.description = description
        self.north = north
        self.south = south
        self.east = east
        self.west = west


def main():
    room_list = []
    my_room = Room("""You have entered the dusty castle hallway. 
There are rooms to the north and south."""
                   , 2, 4, 5, None)
    room_list.append(my_room)

    my_room = Room("""You have entered the King's room. 
There is a hallway to the north."""
                   , 5, None, None, 4)
    room_list.append(my_room)

    my_room = Room("""You have entered the Queen's room. 
She is getting ready for the ball.
There is a hallway to the south."""
                   , None, 0, 3, None)
    room_list.append(my_room)

    my_room = Room("""You have made it to the Maid's quarters. 
Tons of toilet paper and cleaning supplies.
There is a hallway to the south"""
                   , None, 5, None, 2)
    room_list.append(my_room)


    my_room = Room("""You have entered into a bathroom.
There is a hallway to the north.""", 0, None, 1, None)
    room_list.append(my_room)

    my_room = Room("""You are in a pitch black hallway.
There is a walkout to the east.
There are rooms to the north and south."""
                   , 3, 1, 6, 0)
    room_list.append(my_room)

    my_room = Room("""You have walked out to the balcony.
There is a hallway to the west.""", None, None, None, 5)
    room_list.append(my_room)

    current_room = 0

    done = False

    while not done:
        choose = input("Where would you like to go? ")
        if choose == "q":
            print("Goodbye, you left the game.")
            done = True


    print(room_list [current_room].description)






main()



