connections = [
["kh","tc"],
["qp","kh"],
["de","cg"],
["ka","co"],
["yn","aq"],
["qp","ub"],
["cg","tb"],
["vc","aq"],
["tb","ka"],
["wh","tc"],
["yn","cg"],
["kh","ub"],
["ta","co"],
["de","co"],
["tc","td"],
["tb","wq"],
["wh","td"],
["ta","ka"],
["td","qp"],
["aq","cg"],
["wq","ub"],
["ub","vc"],
["de","ta"],
["wq","aq"],
["wq","vc"],
["wh","yn"],
["ka","de"],
["kh","ta"],
["co","tc"],
["wh","qp"],
["tb","vc"],
["td","yn"]
]
"""
trios = []
for connection in connections:
    for connection2 in connections:
        if connection != connection2:
            if connection[0] == connection2[0] and sorted(([connection[0], connection[1], connection2[1]])) not in trios:
                trios.append(sorted(([connection[0], connection[1], connection2[1]])))
            elif connection[1] == connection2[0] and sorted(([connection[0], connection[1], connection2[1]])) not in trios:
                trios.append(sorted(([connection[0], connection[1], connection2[1]])))
            elif connection[0] == connection2[1] and sorted(([connection[0], connection[1], connection2[0]])) not in trios:
                trios.append(sorted(([connection[0], connection[1], connection2[0]])))
            elif connection[1] == connection2[1] and sorted(([connection[0], connection[1], connection2[0]])) not in trios:
                trios.append(sorted(([connection[0], connection[1], connection2[0]])))

trios = sorted(trios, key=lambda x: x[0])"""
connections = []
with open("day 23/input.txt", "r") as f:
    for line in f:
        comps = line.strip().split("-")
        connections.append(comps)
dict = {}
for connection in connections:
    if connection[0] not in dict:
        dict[connection[0]] = [connection[1]]
    else:
        dict[connection[0]].append(connection[1])
    if connection[1] not in dict:
        dict[connection[1]] = [connection[0]] 
    else:
        dict[connection[1]].append(connection[0])

trios = []
for key in dict.keys():
    for comp in dict[key]:
        for comp2 in dict[key]:
            if comp != comp2:
                if comp2 in dict[comp] and sorted([key, comp, comp2]) not in trios:
                    trios.append(sorted([key, comp, comp2]))
def starts_with_t(list):
    for comp in list:
        if comp[0] == "t":
            return True
    return False

real_trios = []
for trio in trios:
    if starts_with_t(trio):
        real_trios.append(trio)

print(len(real_trios))

#part 1: 1149 CORRECT