import matplotlib.pyplot as plt
import numpy as np
infinity = float('inf')


def present_graph(graph):
    vertices = graph.get_vertices()
    x, y = [], []
    for v in vertices:
        x.append(v.longitude)
        y.append(v.latitude)
    plt.scatter(x, y, s=5)


def present_path(path, graph):
    present_graph(graph)
    lat, lon = [], []
    for tpl in path:
        start, stop = tpl[1].start_stop, tpl[1].end_stop
        lat.append(start.latitude)
        lat.append(stop.latitude)
        lon.append(start.longitude)
        lon.append(start.longitude)
        plt.plot([start.longitude, stop.longitude], [start.latitude, stop.latitude], color='red')
    lat_min, lat_max, lon_min, lon_max = min(lat), max(lat), min(lon), max(lon)
    plt.show()

def present_path_verbose(path):
    pad_length = 45
    print("Linia".ljust(pad_length) + "Start".ljust(pad_length) + "Czas wejscia".ljust(pad_length) + "Stop".ljust(pad_length) + "Czas wyjscia".ljust(pad_length))
    print("="*5*pad_length)
    for item in path:
        stop, connection, execution = item[0], item[1], item[2]
        print(
            f"{execution.line}".ljust(pad_length) +
            f"{connection.start_stop.name}".ljust(pad_length) +
            f"{execution.departure_time}".ljust(pad_length) +
            f"{connection.end_stop.name}".ljust(pad_length) +
            f"{execution.arrival_time}".ljust(pad_length)
        )