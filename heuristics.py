import math


# najlepsza heurystyka dla wymiaru o nieskonczonej liczbie kierunkow (wspolrzedne geograficzne)
# no, o ile przestrzen jest ciagla ;) (potwierdzone statystykami i wykresami)
def euclidean_distance(node, destination):
    n_lat, d_lat, n_lon, d_lon = node.latitude, destination.latitude, node.longitude, destination.longitude
    value = math.sqrt(math.pow(n_lat - d_lat, 2) + math.pow(n_lon - d_lon, 2))*1000
    return value


def manhattan_distance(node, destination):
    n_lat, d_lat, n_lon, d_lon = node.latitude, destination.latitude, node.longitude, destination.longitude
    value = abs(n_lat - d_lat) + abs(n_lon - d_lon)
    return value


def chebyshev_distance(node, destination):
    n_lat, d_lat, n_lon, d_lon = node.latitude, destination.latitude, node.longitude, destination.longitude
    value = max(abs(n_lat - d_lat), abs(n_lon - d_lon))
    return value
