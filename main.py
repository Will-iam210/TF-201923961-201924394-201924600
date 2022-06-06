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
    try:
        file = open(file_name)
        lines = file.readlines()
        for line in lines:
            line = line.split()
            n = len(line)
            temp_list = []
            for i in range(n):
                temp_list.append(int(line[i]))
            nodes.append(tuple(temp_list))
    except FileNotFoundError:
        print("File not found.")

    return nodes

# TODO
def read_time(file_name):
    print(1)


# TODO
def distance(n1, n2):
    print(1)


# TODO
def traffic(n1, n2, time):
    print(1)


def create_adjacency_list(file_name, nodes, n, time):
    a_list = [[] for _ in range(n)]
    try:
        file = open(file_name)
        lines = file.readlines()
        for line in lines:
            line = line.split()
            n_i = int(line[0])
            n_j = int(line[1])

            dist = distance(nodes[n_i], nodes[n_j])
            traffic = traffic(nodes[n_i], nodes[n_j], time)

            w = dist * traffic

            a_list[n_i].append(tuple(n_j, w))

    except FileNotFoundError:
        print("File not found.")

    return a_list


def write_adjacency_list(_a_list):
    file = open("Data/adjacency_list.txt", "w")
    for i, a_list in enumerate(_a_list):
        file.write(str(i) + " [")
        for j, u in enumerate(a_list):
            if j == len(a_list) - 1:
                file.write(str(u))
            else:
                file.write(str(u) + ", ")
        file.write("]\n")


if __name__ == '__main__':
    _time = read_time("Data/time.txt")
    _streets = read_streets("Data/streets.txt")
    _nodes = read_nodes("Data/nodes.txt")
    _a_list = create_adjacency_list("Data/edges.txt", _nodes, len(_nodes), _time)

    for i, a_list in enumerate(_a_list):
        print(i, a_list)

    write_adjacency_list(_a_list)
