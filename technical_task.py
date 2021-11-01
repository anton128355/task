def totalizator(bet, result):

    # result_difference - разница между фактическими очками. Ничья (0), победа (+) или поражение (-) первой команды.
    result_difference = (int(result.split(":")[0]) - int(result.split(":")[1])) 
    lst_points, lst_players = [], []

    for res in bet.values():

        if res == result:
            lst_points.append(2)
            continue

        # result_presumptive - разница между преположительными очками. Ничья (0), победа (+) или поражение (-) первой команды.
        result_presumptive = int(res.split(":")[0]) - int(res.split(":")[1])
        
        # 1 - ничья, 2 - победа или поражение первой команды.
        if (result_difference == result_presumptive == 0) or ((result_difference * result_presumptive) > 0):

            lst_points.append(1)

        else:
            lst_points.append(0)

    # Словарь с игроками, в качестве ключей, и их очками, в качестве значений. 
    print((dict(zip(bet.keys(), lst_points))))