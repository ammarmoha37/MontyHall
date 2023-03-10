import random


def player_choice(doors):
    index = random.randint(0, 2)
    choice = doors[index]
    doors.pop(index)
    return choice


def opened_door(doors):
    i = 0
    if doors[i] != 1:
        pass
    else:
        i = 1
    door = doors[i]
    doors.pop(i)
    return door


def MontyHall(switch, counter):
    win_counter = 0
    for c in range(0, counter - 1):
        doors = [1, 0, 0]  # 1 for the car and 0 for the goats
        random.shuffle(doors)
        player = player_choice(doors)
        opened_door(doors)
        if switch is True:
            player = doors[0]
        if player == 1:
            win_counter += 1
    return win_counter


times = 1000
winWithSwitching = MontyHall(True, times)
winWithNotSwitching = MontyHall(False, times)
print("Percentage of win with door switcher is : ",
      winWithSwitching / times)
print()
print("Percentage of wins without door switcher is : ",
      winWithNotSwitching / times)