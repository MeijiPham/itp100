file = input("Please enter the file number: ")
fhand = open(f"registration_list{file}.txt")
flist = [line.rstrip("\n").split(", ") for line in fhand]

houses = ["Gryffindor", "Ravenclaw", "Slytherin", "Hufflepuff"]
full_team = 0
max_player = 7
player_number = dict()

for i in houses:
    for item in flist:
        if i in item:
            player_number[i] = player_number.get(i, 0) + 1
    if player_number[i] > max_player:
        print(f"{i} has too many players.")
    elif player_number[i] < max_player:
        print(f"{i} does not have enough players.")
    else:
        full_team += 1
        if full_team == len(houses):
            print("List complete, let's play quidditch!")
