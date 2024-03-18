import bisect
from data_utilities import parse_time_to_custom_time


class Stop:
    def __init__(self, name, latitude, longitude):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude

    def __eq__(self, other):
        return (self.name, self.latitude, self.longitude) == (other.name, other.latitude, other.longitude)

    def __hash__(self):
        return hash((self.name, self.latitude, self.longitude))

    def __repr__(self):
        return f"{self.name}: {self.latitude, self.longitude}"


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

    def __eq__(self, other):
        return self.departure_time == other.departure_time

    def __lt__(self, other):
        return self.departure_time < other.departure_time

    def __gt__(self, other):
        return self.departure_time > other.departure_time


class Graph:
    def __init__(self, vertices, edges):
        self._vertices = vertices
        self._edges = edges

    def contains_vertex(self, vertex):
        return vertex in self._vertices


def model_stops(row):
    stop1 = Stop(row.start_stop, row.start_stop_lat, row.start_stop_lon)
    stop2 = Stop(row.end_stop, row.end_stop_lat, row.end_stop_lon)
    return stop1, stop2


def model_connection(stop1, stop2):
    connection = Connection(stop1, stop2)
    return connection


def model_execution(row):
    dep_time = parse_time_to_custom_time(row.departure_time)
    arr_time = parse_time_to_custom_time(row.arrival_time)
    execution = Execution(row.company, row.line, dep_time, arr_time)
    return execution


def model_graph_components(df):
    vertices = {}
    edges = {}
    for row in df.itertuples():
        stop1, stop2 = model_stops(row)
        if stop1 not in vertices:
            vertices[stop1] = set()
        if stop2 not in vertices:
            vertices[stop2] = set()

        vertices[stop1].add(stop2)
        connection = model_connection(stop1, stop2)
        execution = model_execution(row)
        if connection not in edges:
            edges[connection] = [execution]
        else:
            bisect.insort(edges[connection], execution)
    return vertices, edges


def model_graph(df):
    vertices, edges = model_graph_components(df)
    graph = Graph(vertices, edges)
    return graph

