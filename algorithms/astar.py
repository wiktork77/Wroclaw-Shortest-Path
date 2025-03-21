import datetime
import heapq
from data_processing.data_modelling import Connection, QueueEntry
from data_processing.data_utilities import parse_time_to_datetime, reconstruct_path, find_best_execution
from cost_computations.cost_strategies import compute_time, compute_cost
import time as t

infinity = float('inf')


def astar(graph, source, destination, start_time, heuristic, criteria):
    start = t.time()
    source, destination = graph.get_stop(source), graph.get_stop(destination)
    path_cost = {}
    time_elapsed = {}
    previous = {}
    vertices = graph.get_vertices()
    edges = graph.get_edges()
    start_time = parse_time_to_datetime(start_time)
    destination_found = False

    for v in vertices:
        path_cost[v] = infinity
        time_elapsed[v] = infinity
    path_cost[source] = 0
    time_elapsed[source] = 0

    queue = []
    heapq.heappush(queue, QueueEntry(source, 0))

    while queue:
        current = heapq.heappop(queue).stop
        time_change = datetime.timedelta(minutes=time_elapsed[current])
        current_time = start_time + time_change
        if current == destination:
            destination_found = True
            break
        neighbors = vertices[current]
        for neighbor in neighbors:
            locally_best_execution = find_best_execution(current_time, edges[Connection(current, neighbor)], criteria, previous[current][2].line if current in previous else None)
            heuristic_value = 0
            if locally_best_execution is None:
                cost = infinity  # czyli jesli nie ma zadnego polaczenia w przyszlosci !
                time = infinity
            else:
                heuristic_value = heuristic(neighbor, destination)
                cost = path_cost[current] + compute_cost(criteria, current_time, locally_best_execution, previous[current][2].line if current in previous else None, heuristic_value)
                time = time_elapsed[current] + compute_time(current_time, locally_best_execution)
            if cost < path_cost[neighbor]:
                path_cost[neighbor] = cost
                time_elapsed[neighbor] = time
                previous[neighbor] = (current, Connection(current, neighbor), locally_best_execution)
                heapq.heappush(queue, QueueEntry(neighbor, cost + heuristic_value))

    if destination_found:
        path = reconstruct_path(previous, source, destination)
        end = t.time()
        computation_time = end - start
        return path, time_elapsed[destination], computation_time
    else:
        return None

