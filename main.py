# The code of Dijkstra part is from Geeksforgeeks.org

import csv
from xlrd import open_workbook

MAXINT = 99999999  # Whatever


def min_dist(graph, dist, shortest_path_list):
    min_dist = MAXINT
    min_index = 0

    for v in range(len(graph)):
        if dist[v] < min_dist and shortest_path_list[v] is False:
            min_dist = dist[v]
            min_index = v

    return min_index


def dijkstra(graph, src):
    """
    :param graph: A 2*2 nested list
    :param src: the index of the source node
    :return:
    """
    dist = [MAXINT] * len(graph)
    dist[src] = 0
    shortest_path_list = [False] * len(graph)

    for i in range(len(graph)):
        u = min_dist(graph, dist, shortest_path_list)
        shortest_path_list[u] = True

        for v in range(len(graph)):
            if graph[u][v] > 0 and shortest_path_list[v] is False and dist[v] > dist[u] + graph[u][v]:
                dist[v] = dist[u] + graph[u][v]

    return dist


def print_graph(graph):
    for i in range(len(graph)):
        print(graph[i])
    return


if __name__ == '__main__':
    book = open_workbook("Karate.xlsx")
    sheet = book.sheet_by_index(0)

    # Read graph from xlsx file
    my_graph = []
    for row in range(1, 35):
        # for column in range(1, 35):
        my_graph.append(sheet.row_values(row)[1:])

    # Get shortest distance
    shortest_distance = []
    for i in range(len(my_graph)):
        dist = dijkstra(my_graph, i)
        shortest_distance.append(dist)

    # Calculate closeness centrality
    closeness_cent = []
    for i in range(len(my_graph)):
        cent = float((len(my_graph) - 1) / sum(shortest_distance[i]))
        closeness_cent.append(cent)

    assert len(closeness_cent) == len(my_graph)
    print(closeness_cent)

    # Outfile
    with open('closeness centrality.csv', "w") as f:
        writer = csv.writer(f)
        writer.writerow(closeness_cent)
