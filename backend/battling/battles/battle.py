def round (pokemon_c_atk, pokemon_c_def, pokemon_c_hp, pokemon_o_atk, pokemon_o_def, pokemon_o_hp, points):
    if pokemon_c_atk > pokemon_o_def:
        points['player1'] +=1
    elif pokemon_c_atk < pokemon_o_def:
        points['player2'] +=1
    else:
        if pokemon_c_hp > pokemon_o_hp:
            points['player1'] +=1
        else:
            points['player2'] +=1
    return points
