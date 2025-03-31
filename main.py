import sys
import argparse
from GUI.window import Ui_MainWindow
from data_processing.data_modelling import model_graph
from data_processing.data_utilities import retrieve_data, count_line_changes
from cost_computations.heuristics import euclidean_distance
from data_processing.data_presentation import present_path_verbose
from algorithms.dijkstra import dsp
from algorithms.astar import astar
from PyQt6 import QtCore, QtGui, QtWidgets


def run_console():
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


def run_gui():
    df = retrieve_data("connection_graph_unique.csv")
    graph = model_graph(df)

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow(graph)
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Shortest path between Wrocław city stops program')
    parser.add_argument('--mode', action='store', dest='mode', default='gui')

    args = parser.parse_args()

    mode = args.mode

    if mode == 'console':
        run_console()
    elif mode == 'gui':
        run_gui()
    else:
        print("allowed arguments for --mode: [gui, console]")

