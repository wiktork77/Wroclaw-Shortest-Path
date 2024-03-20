import datetime
import heapq
from data_modelling import Connection, QueueEntry
from data_presentation import present_path_verbose
from data_utilities import parse_time_to_datetime, find_best_future_execution_time, reconstruct_path, compute_execution_duration
from cost_strategies import compute_time
import time as t

infinity = float('inf')


def astar(graph, source, destination, start_time, heuristic):
    source, destination = graph.get_stop(source), graph.get_stop(destination)
    path_cost = {}
    time_elapsed = {}
    previous = {}
    vertices = graph.get_vertices()
    edges = graph.get_edges()
    start_time = parse_time_to_datetime(start_time)
    destination_found = False

    exec_finding_time = 0
    exec_finding_count = 0

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
            start = t.time()
            locally_best_execution = find_best_future_execution_time(current_time, edges[Connection(current, neighbor)])
            end = t.time()
            exec_finding_time += end - start
            exec_finding_count += 1
            heuristic_value = 0
            if locally_best_execution is None:
                cost = infinity  # czyli jesli nie ma zadnego polaczenia w przyszlosci !
                time = infinity
            else:
                heuristic_value = heuristic(neighbor, destination)
                cost = path_cost[current] + compute_time(current_time, locally_best_execution)
                time = time_elapsed[current] + compute_time(current_time, locally_best_execution)
            if cost < path_cost[neighbor]:
                path_cost[neighbor] = cost
                time_elapsed[neighbor] = time
                previous[neighbor] = (current, Connection(current, neighbor), locally_best_execution)
                heapq.heappush(queue, QueueEntry(neighbor, cost + heuristic_value))

    if destination_found:
        path = reconstruct_path(previous, source, destination)
        present_path_verbose(path)
        print(previous[destination][2].departure_time)
        print(f"Time spent on finding exec: {exec_finding_time}")
        print(f"Count: {exec_finding_count}")
        return path, time_elapsed[destination]
    else:
        print("No path to destination found!")
        return None





