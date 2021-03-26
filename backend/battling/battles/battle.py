def round (pokemon_c_atk, pokemon_o_def, winner):
    if pokemon_c_atk > pokemon_o_def:
        winner['player1'] +=1
    elif pokemon_c_atk < pokemon_o_def:
        winner['player2'] +=1
    else:
        if pokemon_c_hp > pokemon_o_hp:
            winner['player1'] +=1
        else:
            winner['player2'] +=1
    return winner
