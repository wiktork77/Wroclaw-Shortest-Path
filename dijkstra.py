import datetime
import heapq
from data_modelling import QueueEntry, Connection
from data_presentation import present_path_verbose
from data_utilities import parse_time_to_datetime, find_best_execution, reconstruct_path

infinity = float('inf')


def present_path_general(path):
    lines_dict = {}
    general_path = []
    for item in path:
        stop, connection, execution = item[0], item[1], item[2]
        line = execution.line
        if line not in lines_dict:
            lines_dict[line] = item
        else:
            lines_dict[line][1].end_stop.name = connection.end_stop.name
            lines_dict[line][2].arrival_time = execution.arrival_time
    for k, v in lines_dict.items():
        general_path.append(v)
    present_path_verbose(general_path)


def compute_cost(current_time, execution):
    execution_cost = execution.arrival_time - execution.departure_time
    additional_cost = execution.departure_time - current_time
    return (execution_cost.seconds + additional_cost.seconds) / 60


def dsp(graph, source, destination, start_time):
    source, destination = graph.get_stop(source), graph.get_stop(destination)
    distance = {}
    previous = {}
    vertices = graph.get_vertices()
    edges = graph.get_edges()
    start_time = parse_time_to_datetime(start_time)
    destination_found = False

    for v in vertices:
        distance[v] = infinity
    distance[source] = 0

    queue = []
    heapq.heappush(queue, QueueEntry(source, 0))

    while queue:
        current = heapq.heappop(queue).stop
        time_change = datetime.timedelta(minutes=distance[current])
        current_time = start_time + time_change
        if current == destination:
            destination_found = True
            break
        neighbors = vertices[current]
        for neighbor in neighbors:
            locally_best_execution = find_best_execution(current_time, edges[Connection(current, neighbor)], 't')
            if locally_best_execution is None:
                cost = infinity  # czyli jesli nie ma zadnego polaczenia w przyszlosci !
            else:
                cost = distance[current] + compute_cost(current_time, locally_best_execution)
            if cost < distance[neighbor]:
                distance[neighbor] = cost
                previous[neighbor] = (current, Connection(current, neighbor), locally_best_execution)
                heapq.heappush(queue, QueueEntry(neighbor, cost))

    if destination_found:
        path = reconstruct_path(previous, source, destination)
        present_path_verbose(path)
        return path, distance[destination]
    else:
        print("No path to destination found!")
        return None









