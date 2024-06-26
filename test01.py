def find_shortest_distance(points, start_point, arrival_point):
    distances = [point[1] for point in points]
    start_index = points.index((start_point, min(distances)))
    arrival_index = points.index((arrival_point, min(distances)))
    shortest_distance = abs(arrival_index - start_index)
    return shortest_distance

# Example usage
points = [("A", 5), ("B", 10), ("C", 3), ("D", 8)]
start_point = "A"
arrival_point = "C"
shortest_distance = find_shortest_distance(points, start_point, arrival_point)
print(f"The shortest distance between {start_point} and {arrival_point} is {shortest_distance}.")

# Additional example with multiple paths
points = [("A", 5), ("B", 10), ("C", 3), ("D", 8), ("E", 6)]
start_point = "A"
arrival_point = "E"
shortest_distance = find_shortest_distance(points, start_point, arrival_point)
print(f"The shortest distance between {start_point} and {arrival_point} is {shortest_distance}.")