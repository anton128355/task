def totalizator(bet, result):

    # result_difference - the difference between the actual points. Draw (0), win (+) or defeat (-) of the first team.
    result_difference = (int(result.split(":")[0]) - int(result.split(":")[1])) 
    lst_points, lst_players = [], []

    for res in bet.values():

        if res == result:
            lst_points.append(2)
            continue

        # result_presumptive - the difference between the expected points. Draw (0), win (+) or defeat (-) of the first team.
        result_presumptive = int(res.split(":")[0]) - int(res.split(":")[1])
        
        # 1 - ничья, 2 - victory or defeat of the first team.
        if (result_difference == result_presumptive == 0) or ((result_difference * result_presumptive) > 0):

            lst_points.append(1)

        else:
            lst_points.append(0)

    # A dictionary with players as keys and their scores as meanings.
    print((dict(zip(bet.keys(), lst_points))))
