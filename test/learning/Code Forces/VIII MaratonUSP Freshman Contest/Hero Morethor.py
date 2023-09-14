def Run():

    heros_power = int(input().split(' ')[1])
    monsters_legion = list(map(int , (input().split(' '))))

    for each_monster in monsters_legion:
        if heros_power >= each_monster:
            heros_power += each_monster
        else:
            return 'NAO'

    return 'SIM'

print(Run())


