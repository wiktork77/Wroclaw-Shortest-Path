import bisect
from data_utilities import parse_time_to_datetime


class Stop:
    def __init__(self, name, latitude, longitude):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude

    def __eq__(self, other):
        return self.name == other.name

    def __hash__(self):
        return hash(self.name)

    def __repr__(self):
        return f"{self.name} ({self.latitude}, {self.longitude})"


class Connection:
    def __init__(self, start_stop, end_stop):
        self.start_stop = start_stop
        self.end_stop = end_stop

    def __eq__(self, other):
        return (self.start_stop, self.end_stop) == (other.start_stop, other.end_stop)

    def __hash__(self):
        return hash((self.start_stop, self.end_stop))

    def __repr__(self):
        return f"({self.start_stop} -> {self.end_stop})"


class Execution:
    def __init__(self, company, line, departure_time, arrival_time):
        self.company = company
        self.line = line
        self.departure_time = departure_time
        self.arrival_time = arrival_time

    def __repr__(self):
        return f"({self.departure_time} -- {self.arrival_time})"

    def __gt__(self, other):
        return self.arrival_time > other

    def __lt__(self, other):
        return self.arrival_time < other


class Graph:
    def __init__(self, vertices, edges):
        self._vertices = vertices
        self._edges = edges

    def contains_vertex(self, vertex):
        return vertex in self._vertices

    def get_vertices(self):
        return self._vertices

    def get_edges(self):
        return self._edges

    def get_stop(self, name):
        for v in self._vertices.keys():
            if v.name == name:
                return v

class QueueEntry:
    def __init__(self, stop, cost):
        self.stop = stop
        self.cost = cost

    def __eq__(self, other):
        return self.cost == other.cost

    def __lt__(self, other):
        return self.cost < other.cost

    def __gt__(self, other):
        return self.cost > other.cost

    def __hash__(self):
        return hash(self.cost)

    def __repr__(self):
        return f"({self.stop} {self.cost})"


def model_stops(row):
    stop1 = Stop(row.start_stop, row.start_stop_lat, row.start_stop_lon)
    stop2 = Stop(row.end_stop, row.end_stop_lat, row.end_stop_lon)
    return stop1, stop2


def model_connection(stop1, stop2):
    connection = Connection(stop1, stop2)
    return connection


def model_execution(row):
    dep_time = parse_time_to_datetime(row.departure_time)
    arr_time = parse_time_to_datetime(row.arrival_time)
    execution = Execution(row.company, row.line, dep_time, arr_time)
    return execution


def compute_average_location(locations):
    i, lat, lon = 0, 0, 0
    for loc in locations:
        lat += loc[0]
        lon += loc[1]
        i += 1
    lat /= i
    lon /= i
    return lat, lon

def model_generalized_stops(df):
    stops_to_lat_lon = {}
    generalized_stops = {}
    for row in df.itertuples():
        stop1, stop2 = model_stops(row)
        if stop1 not in stops_to_lat_lon:
            stops_to_lat_lon[stop1] = {(stop1.latitude, stop1.longitude)}
        else:
            stops_to_lat_lon[stop1].add((stop1.latitude, stop1.longitude))
        if stop2 not in stops_to_lat_lon:
            stops_to_lat_lon[stop2] = {(stop2.latitude, stop2.longitude)}
        else:
            stops_to_lat_lon[stop2].add((stop2.latitude, stop2.longitude))
    for k, v in stops_to_lat_lon.items():
        lat, lon = compute_average_location(v)
        generalized_stops[k.name] = Stop(k.name, lat, lon)
    return generalized_stops


def model_graph_components(df):
    generalized_stops = model_generalized_stops(df)
    vertices = {}
    edges = {}
    for row in df.itertuples():
        stop1, stop2 = generalized_stops[row.start_stop], generalized_stops[row.end_stop]
        if stop1 not in vertices:
            vertices[stop1] = []
        if stop2 not in vertices:
            vertices[stop2] = []

        if stop2 not in vertices[stop1]:
            vertices[stop1].append(stop2)
        connection = model_connection(stop1, stop2)
        execution = model_execution(row)
        if connection not in edges:
            edges[connection] = [execution]
        else:
            edges[connection].append(execution)
    return vertices, edges


def model_graph(df):
    vertices, edges = model_graph_components(df)
    graph = Graph(vertices, edges)
    return graph

