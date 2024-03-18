import bisect
from data_utilities import express_time_as_seconds, parse_time_to_custom_time




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
        return f"({self.departure_time} -> {self.arrival_time})"


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


def model_data(df):
    uniq_stops = set()
    edges = {}
    for row in df.itertuples():
        stop1, stop2 = model_stops(row)
        uniq_stops.add(stop1)
        uniq_stops.add(stop2)
        connection = model_connection(stop1, stop2)
        if connection not in edges:
            execution = model_execution(row)
            edges[connection] = [execution]

    for item in edges.items():
        print(item)


