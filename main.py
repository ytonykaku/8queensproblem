import networkx as nx
import random
import string


G = nx.read_gml("Tabuleiro_com_incompatibilidades.gml", label = 'label')
plays = []
solution = []
position = []
adjacent = True
alphabet = list(string.ascii_lowercase)

while (len(solution) < 8):
    solution.clear()

    for x in G.nodes:
        plays.append(int(x))

    while(len(plays) > 0):
        square = int(random.choice(plays))

        if len(solution) == 0:
            solution.append(square)
        else:
            for x in solution:
                for y in G.edges:
                    if(int(y[0]) == square and int(y[1]) == x) or (int(y[0]) == x and int(y[1]) == square):
                        adjacent = False
                        plays.remove(square)
                        break
                    else:
                        adjacent = True

                if(adjacent == False):
                        break

        if adjacent == True:
            if square not in solution:
                solution.append(square)
            plays.remove(square)

for set_number in solution:
    y_position = int(set_number/8)
    x_position = set_number%8
    corresponding_row = alphabet[int(x_position)-1]
    set_position = corresponding_row+str(y_position)
    position.append(set_position)

print(f'Independent Set: {solution}')
print(f'Independent Set (board positions): {position}')
