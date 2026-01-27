possessions_per_game = 70

results = [
    ['A', 80, 'B', 70], 
    ['B', 75, 'C', 65],
    ['A', 65, 'C', 65]
]

# --- League average PPP ---
league_avg_ppp = 0
for game in results:
    league_avg_ppp += game[1]
    league_avg_ppp += game[3]

league_avg_ppp = league_avg_ppp / (len(results) * 2 * possessions_per_game)

teams = ['A', 'B', 'C']
oeff_dict = {team: league_avg_ppp for team in teams}
deff_dict = {team: league_avg_ppp for team in teams}


def main(oe_dict, de_dict, num_iterations=10):
    for _ in range(num_iterations):
        oe_iter_dict = {team: 0 for team in teams}
        de_iter_dict = {team: 0 for team in teams}
        counts_dict = {team: 0 for team in teams}

        for game in results:
            team1, pts1, team2, pts2 = game

            ppp1 = pts1 / possessions_per_game
            ppp2 = pts2 / possessions_per_game

            # Adjusted offensive efficiency
            adj_oe1 = ppp1 + (league_avg_ppp - de_dict[team2])
            adj_oe2 = ppp2 + (league_avg_ppp - de_dict[team1])

            # Adjusted defensive efficiency (points allowed)
            adj_de1 = ppp2 + (league_avg_ppp - oe_dict[team2])
            adj_de2 = ppp1 + (league_avg_ppp - oe_dict[team1])

            oe_iter_dict[team1] += adj_oe1
            oe_iter_dict[team2] += adj_oe2

            de_iter_dict[team1] += adj_de1
            de_iter_dict[team2] += adj_de2

            counts_dict[team1] += 1
            counts_dict[team2] += 1

        # Average over games played
        for team in teams:
            oe_dict[team] = oe_iter_dict[team] / counts_dict[team]
            de_dict[team] = de_iter_dict[team] / counts_dict[team]

        possessions_per_game = 70

results = [
    ['A', 80, 'B', 70], 
    ['B', 75, 'C', 65],
    ['A', 75, 'C', 65]
]

# --- League average PPP ---
league_avg_ppp = 0
for game in results:
    league_avg_ppp += game[1]
    league_avg_ppp += game[3]

league_avg_ppp = league_avg_ppp / (len(results) * 2 * possessions_per_game)

teams = ['A', 'B', 'C']
oeff_dict = {team: league_avg_ppp for team in teams}
deff_dict = {team: league_avg_ppp for team in teams}


def main(oe_dict, de_dict, num_iterations=10):
    for i in range(num_iterations):
        oe_iter_dict = {team: 0 for team in teams}
        de_iter_dict = {team: 0 for team in teams}
        counts_dict = {team: 0 for team in teams}

        for game in results:
            team1, pts1, team2, pts2 = game

            ppp1 = pts1 / possessions_per_game
            ppp2 = pts2 / possessions_per_game

            # Adjusted offensive efficiency
            adj_oe1 = ppp1 + (league_avg_ppp - de_dict[team2])
            adj_oe2 = ppp2 + (league_avg_ppp - de_dict[team1])

            # Adjusted defensive efficiency (points allowed)
            adj_de1 = ppp2 + (league_avg_ppp - oe_dict[team2])
            adj_de2 = ppp1 + (league_avg_ppp - oe_dict[team1])

            oe_iter_dict[team1] += adj_oe1
            oe_iter_dict[team2] += adj_oe2

            de_iter_dict[team1] += adj_de1
            de_iter_dict[team2] += adj_de2

            counts_dict[team1] += 1
            counts_dict[team2] += 1

        # Average over games played
        for team in teams:
            oe_dict[team] = oe_iter_dict[team] / counts_dict[team]
            de_dict[team] = de_iter_dict[team] / counts_dict[team]

        print(f"Offensive efficiencies after iteration {i+1}:")
        print(oe_dict)
        print(f"\nDefensive efficiencies after iteration {i+1}:")
        print(de_dict)
        print('--------------------------------------------------------------')



    return oe_dict, de_dict


oe, de = main(oeff_dict, deff_dict)

print("Final Offensive Efficiencies:")
print(oe)
print("\nFinal Defensive Efficiencies:")
print(de)

print("\nNet Efficiencies (OE - DE):")
for t in teams:
    print(t, oe[t] - de[t])