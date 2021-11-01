def tote(bet, result):
    # result_fact - ничья, победа или поражение первой команды.
    result_fact, lst_points, lst_players  = (int(result[0]) - int(result[2])), [], [] 
    
    for player in bet:
        # result_presumptive - преположительный результат матча
        result_presumptive = int(bet[player][0]) - int(bet[player][2])

        if bet[player] == result:
            lst_points.append(2)
        
        # 1 - ничья, 2 - победа первой команды, 3 - поражение первой команды. 
        elif (result_fact == result_presumptive == 0) or (result_fact > 0 and result_presumptive > 0) or (result_fact < 0 and result_presumptive < 0):
             lst_points.append(1)
             
        else:
            lst_points.append(0)

    # Словарь с игроками, в качестве ключей и их очками, в качестве значений. 
    print(dict(zip(bet.keys(), lst_points)))

tote({"user1": "3:1", "user2": "3:1", "user3": "3:1"}, "3:1")