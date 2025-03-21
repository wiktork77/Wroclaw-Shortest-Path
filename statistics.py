from data_utilities import retrieve_data, count_line_changes
from data_modelling import model_graph
from dijkstra import dsp
from astar import astar
import random
from datetime import datetime
from heuristics import euclidean_distance, manhattan_distance, chebyshev_distance
import codecs


def random_time():
    hour = random.randint(0, 28)
    minute = random.randint(0, 59)
    return f"{hour}:{minute}:00"

#
# def compare_dijkstra_astar_time():
#     df = retrieve_data("connection_graph_unique.csv")
#     graph = model_graph(df)
#     vertices = list(graph.get_vertices().keys())
#     dijkstra_results = []
#     astar_results = []
#     while len(dijkstra_results) < 750:
#         v1 = random.choice(vertices).name
#         v2 = random.choice(vertices).name
#         while v2 == v1:
#             v2 = random.choice(vertices).name
#         r_time = random_time()
#         dijkstra_result = dsp(graph, v1, v2, r_time)
#         astar_result = astar(graph, v1, v2, r_time, euclidean_distance, 't')
#         if dijkstra_result is not None:
#             dijkstra_results.append(dijkstra_result)
#             astar_results.append(astar_result)
#     with codecs.open("./statistics_results/dijkstra_vs_astar/dijkstra.csv", "w", "utf-8") as f:
#         for result in dijkstra_results:
#             path, cost, time = result
#             f.write(f"{len(path)},{cost},{time}\n")
#     with codecs.open("./statistics_results/dijkstra_vs_astar/astar.csv", "w", "utf-8") as f:
#         for result in astar_results:
#             path, cost, time = result
#             f.write(f"{len(path)},{cost},{time}\n")
#
def compare_astar_heuristics_time():
    df = retrieve_data("connection_graph_unique.csv")
    graph = model_graph(df)
    vertices = list(graph.get_vertices().keys())
    euclidean_results = []
    manhattan_results = []
    chebyshev_results = []

    while len(euclidean_results) < 750:
        v1 = random.choice(vertices).name
        v2 = random.choice(vertices).name
        while v2 == v1:
            v2 = random.choice(vertices).name
        r_time = random_time()
        euclidean_result = astar(graph, v1, v2, r_time, euclidean_distance, 't')
        manhattan_result = astar(graph, v1, v2, r_time, manhattan_distance, 't')
        chebyshev_result = astar(graph, v1, v2, r_time, chebyshev_distance, 't')
        if euclidean_result is not None:
            euclidean_results.append(euclidean_result)
            manhattan_results.append(manhattan_result)
            chebyshev_results.append(chebyshev_result)
    with codecs.open("./statistics_results/astar_heuristic_comparison/euclidean.csv", "w", "utf-8") as f:
        for result in euclidean_results:
            path, cost, time = result
            f.write(f"{len(path)},{cost},{time}\n")
    with codecs.open("./statistics_results/astar_heuristic_comparison/manhattan.csv", "w", "utf-8") as f:
        for result in manhattan_results:
            path, cost, time = result
            f.write(f"{len(path)},{cost},{time}\n")
    with codecs.open("statistics_results/astar_heuristic_comparison/chebyshev.csv", "w", "utf-8") as f:
        for result in chebyshev_results:
            path, cost, time = result
            f.write(f"{len(path)},{cost},{time}\n")
#
#
# def compare_astar_change_value_scalar():
#     df = retrieve_data("connection_graph_unique.csv")
#     graph = model_graph(df)
#     vertices = list(graph.get_vertices().keys())
#     big = 500
#     ch_values = []
#
#     for i in range(50):
#         ch_value = i
#         for j in range(125):
#             v1 = random.choice(vertices).name
#             v2 = random.choice(vertices).name
#             r_time = random_time()
#             while v2 == v1:
#                 v2 = random.choice(vertices).name
#             finest_result = astar(graph, v1, v2, r_time, euclidean_distance, 'p', big)
#             result = astar(graph, v1, v2, r_time, euclidean_distance, 'p', ch_value)
#             if finest_result is not None and result is not None:
#                 f_path, _, _ = finest_result
#                 path, _, comp_time = result
#                 ch_values.append((ch_value, count_line_changes(path), comp_time, count_line_changes(f_path)))
#     with codecs.open("statistics_results/astar_ch_cost/heuristic.csv", "w", "utf-8") as f:
#         for result in ch_values:
#             val, l_ch, time, g_lch = result
#             f.write(f"{val},{l_ch},{time},{g_lch},{l_ch-g_lch}\n")
#
#
#
# compare_astar_change_value_scalar()

compare_astar_heuristics_time()

