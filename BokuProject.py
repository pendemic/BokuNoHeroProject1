import random
max_width = 4
max_height = 4
loop_counter = 35
midoriya_location = (random.randrange(max_width), random.randrange(max_height))
todoroki_location = (random.randrange(max_width), random.randrange(max_height))
midoriya_health = 3
while True:
    print("Midoriya's location is " + str(midoriya_location))
    bakugo_attack_location = (random.randrange(max_width), random.randrange(max_height))
    print("Bakugo shot at " + str(bakugo_attack_location))
    if (bakugo_attack_location != midoriya_location):
        print('Bakugo missed!')
        print('Midoriya has ' + str(midoriya_health) + ' lives remaining')
    if (bakugo_attack_location == midoriya_location):
        print('Bakugo hit Midoriya!')
        midoriya_health = midoriya_health - 1
        print('Midoriya has ' + str(midoriya_health) + ' lives remaining')
        midoriya_location = (random.randrange(max_width), random.randrange(max_height))
    print('Bakugo has ' + str(loop_counter) + ' turns remaining')
    loop_counter -= 1
    if (bakugo_attack_location == todoroki_location):
        print('Bakugo attacked Todoroki and got frozen for 3 turns!')
        loop_counter -= 2
    if (loop_counter <= 0):
        break;
if (midoriya_health > 0):
    print('Midoriya is the winner!')
if (midoriya_health == 0) or (midoriya_health < 0):
    print("Bakugo is the winner!")
def forest(max_width,max_height):
    forest = [["_" for i in range(max_width)]
    for i in range(max_height)]
    return forest
    forest(max_width,max_height)
