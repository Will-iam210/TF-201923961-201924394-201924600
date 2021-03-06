from datetime import datetime
import math
import heapq as hq
import json
from operator import le

def dijkstra(a_list, s):
    n = len(a_list)
    visited = [False] * n
    path = [-1] * n
    cost = [math.inf] * n

    cost[s] = 0
    pqueue = [(0, s)]
    while pqueue:
        g, u = hq.heappop(pqueue)
        if not visited[u]:
            visited[u] = True
            for v, w in a_list[u]:
                if not visited[v]:
                    f = g + w
                    if f < cost[v]:
                        cost[v] = f
                        path[v] = u
                        hq.heappush(pqueue, (f, v))

    return path, cost


def path_to_trajectory(path, start):
    t = start
    trajectory = [start]
    while path[t] != -1:
        t = path[t]
        trajectory.append(t)
    return trajectory


def k_shortest_paths(a_list, inversed_a_list, start, target, k):
    path, cost = dijkstra(inversed_a_list, target)

    trajectory = path_to_trajectory(path, start)
    n = len(trajectory)
    paths = [(cost[start], trajectory)]

    for i in range(n - 1):
        for v, w in a_list[trajectory[i]]:
            temp_path = []
            _path = path_to_trajectory(path, v)
            for j in range(i + 1):
                temp_path.append(trajectory[j])
            if i >= 1 and v == trajectory[i - 1]:
                continue
            elif v != trajectory[i + 1] and trajectory[i] not in _path:
                f = cost[trajectory[0]] - cost[trajectory[i]]
                f = cost[v] + w + f
                temp_path = temp_path + _path
                paths.append((f, temp_path))

    paths.sort()
    n = len(paths)
    if n < k:
        last_path = paths[n - 1]
        for i in range(n, k):
            paths.append(last_path)

    paths = paths[:k]

    return paths


def read_streets(file_name):
    streets = []
    try:
        file = open(file_name)
        lines = file.readlines()
        for line in lines:
            line = line.replace('\n', '')
            streets.append(line)
    except FileNotFoundError:
        print("File not found.")

    return streets


def read_nodes(file_name):
    nodes = []
    loc = []
    try:
        file = open(file_name)
        lines = file.readlines()
        for line in lines:
            line = line.split()
            temp_list = []

            temp_list.append(float(line[0]))
            temp_list.append(float(line[1]))
            loc.append((temp_list[0], temp_list[1]))

            temp_list = []

            n = len(line)
            for i in range(2, n):
                temp_list.append(int(line[i]))
            nodes.append(temp_list)
            
    except FileNotFoundError:
        print("File not found.")

    return nodes, loc


def read_time(file_name):
    try:
        file_time = open(file_name)
        line = file_time.readline()
        hour = [int(h) for h in line.split(":")]
        time = hour[0]
    except FileNotFoundError:
        date = datetime.utcnow()
        line = date.time().strftime("%H:%M:%S")
        hour = [int(h) for h in line.split(":")]
        time = hour[0]-5

    return time


def distance(n1, n2):
    x1 = n1[1]
    y1 = n1[0]

    x2 = n2[1]
    y2 = n2[0]

    d = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** (1 / 2)
    dm = d * 10 ** 5
    return dm


def traffic(n1, n2, time):
    x1 = (n1[1] + 57.9545857472616) * 20 / 0.0402401395890024
    y1 = (n1[0] + 34.9213913491353) * 20 / 0.0402401395890024

    x2 = (n2[1] + 57.9545857472616) * 20 / 0.0402401395890024
    y2 = (n2[0] + 34.9213913491353) * 20 / 0.0402401395890024

    x_edge = (x1 + x2) / 2
    y_edge = (y1 + y2) / 2
    
    m = 0
    if time < 15:
        m = -0.90278 * time ** 3 + 19.09722 * time ** 2 - 70 * time + 150
    elif time <= 24:
        m = -9.44444 * time ** 2 + 346.11111 * time - 2716.66667
    else:
        m = 0


    #n = 0.0000487804878 * m + 0.0356097560976 0.04 - 0.06
    #n = 0.00007317077317 * m + 0.0534146341463 0.06 - 0.09
    n = 0.0002195121951 * m + 0.040243902439

    traffic_factor = m * (math.sin(n * (x_edge ** 2 + y_edge ** 2)) / (x_edge ** 2 + y_edge ** 2 + 40)) + 1 + m / 100
    return traffic_factor


def create_adjacency_list(file_name, loc, n, time):
    a_list = [[] for _ in range(n)]
    inversed_a_list = [[] for _ in range(n)]
    try:
        file = open(file_name)
        lines = file.readlines()
        for line in lines:
            line = line.split()
            n_i = int(line[0])
            n_j = int(line[1])

            dist = distance(loc[n_i], loc[n_j])
            traffic_factor = traffic(loc[n_i], loc[n_j], time)

            w = dist * traffic_factor
            w = math.trunc(pow(10, 5) * w) / pow(10, 5)

            a_list[n_i].append((n_j, w))
            inversed_a_list[n_j].append((n_i, w))

    except FileNotFoundError:
        print("File not found.")

    return a_list, inversed_a_list


def write_adjacency_list(_a_list):
    file = open("Data/adjacency_list.txt", "w")
    for i, a_list in enumerate(_a_list):
        file.write(str(i) + " [")
        for j, (u, w) in enumerate(a_list):
            if j == len(a_list) - 1:
                file.write("(" + str(u) + ", " + str(w) + ")")
            else:
                file.write("(" + str(u) + ", " + str(w) + ")" + ", ")
        file.write("]\n")


def get_node_from_streets(corner, streets, nodes):
    temp = []
    
    for s in corner:
        if s in streets:
            temp.append(streets.index(s))

    temp.sort()

    if temp in nodes:
        return nodes.index(temp)

    return -1


def graph():
    #intersecciones (nodos)
    _time = read_time("Data/time.txt")
    _nodes, _loc = read_nodes("Data/nodes.txt")

    #grafo (al)
    _a_list, _inversed_a_list = create_adjacency_list("Data/edges.txt", _loc, len(_nodes), _time)

    n = len(_loc)
    temp_loc = []

    for i in range(n):
        x1 = _loc[i][1]
        y1 = _loc[i][0]
        temp_loc.append((x1 , y1))

    return json.dumps({"loc": temp_loc, "g": _a_list})
# asd

def paths(s, t):
    _time = read_time("Data/time.txt")
    _streets = read_streets("Data/streets.txt")
    _nodes, _loc = read_nodes("Data/nodes.txt")
    _a_list, _inversed_a_list = create_adjacency_list("Data/edges.txt", _loc, len(_nodes), _time)

    start_corner = ["Calle 39", "Calle 9"]
    target_corner = ["Calle 12", "Calle 50", "Diagonal 74"]

    #start = get_node_from_streets(start_corner, _streets, _nodes)
    #target = get_node_from_streets(target_corner, _streets, _nodes)

    start = s
    target = t

    k = 3

    paths = k_shortest_paths(_a_list, _inversed_a_list, start, target, k)

    n = len(_loc)
    temp_loc = []

    for i in range(n):
        x1 = (_loc[i][1] + 57.9545857472616) * 400 / 0.0402401395890024
        y1 = (_loc[i][0] + 34.9213913491353) * 400 / 0.0402401395890024
        temp_loc.append((x1 + 500 , y1 * -1 + 300))

    _, bestpath = paths[0]
    _, path1 = paths[1]
    _, path2 = paths[2]

    #Bestpath=[-1] * n
    #Path1=[]
    #Path2=[]
    #for i in bestpath:
    #    Bestpath.append(_loc[i])

    #for i in path1:
    #    Path1.append(_loc[i])

    #for i in path2:
    #    Path2.append(_loc[i])

    Bestpath=[-1] * n
    Path1=[-1] * n
    Path2=[-1] * n

    for i, j in enumerate(bestpath):
        if i != 0:
            Bestpath[j] = bestpath[i - 1]

    for i, j in enumerate(path1):
        if i != 0:
            Path1[j] = path1[i - 1]

    for i, j in enumerate(path2):
        if i != 0:
            Path2[j] = path2[i - 1]


    return json.dumps({"bestpath": Bestpath, "path1": Path1, "path2": Path2})