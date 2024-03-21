import sys

from data_modelling import model_graph
from data_utilities import retrieve_data, count_line_changes
from heuristics import euclidean_distance
from data_presentation import present_path_verbose
from metrics.time_metrics import measure_computation_time
from dijkstra import dsp
from astar import astar


def run():
    print("Reading data...")
    df = retrieve_data("connection_graph_unique.csv")
    graph = model_graph(df)
    while True:
        start = input("Podaj przystanek początkowy: ")
        end = input("Podaj przystanek końcowy: ")
        time = input("Podaj czas: ")
        algorithm = input("[a] Dijkstra\n[b] A*\nWybierz algorytm: ").lower()
        if algorithm == "b":
            criteria = input("Podaj kryterium (t, p): ")
            result = astar(graph, start, end, time, euclidean_distance, criteria)
        else:
            result = dsp(graph, start, end, time)
        if result is None:
            print("Nie znaleziono połączenia!")
        else:
            path, travel_time, computation_time = result
            present_path_verbose(path)
            print(f"Czas obliczen: {computation_time}s")
            print(f"Czas podrozy: {travel_time}")
            print(f"Liczba przesiadek: {count_line_changes(path)}")


if __name__ == "__main__":
    run()



