def insertion_heuristic_tsp(distances):
    n = len(distances)
    unvisited = set(range(1, n))  # Start with all cities unvisited
    tour = [0]  # Start the tour with the first city (usually arbitrary)
    
    while unvisited:
        min_increase = float('inf')
        best_city = None
        best_position = None
        
        for city in unvisited:
            for i in range(len(tour)):
                # Try inserting city at position i and calculate the increase in tour length
                prev_city = tour[i]
                next_city = tour[(i + 1) % len(tour)]
                increase = distances[prev_city][city] + distances[city][next_city] - distances[prev_city][next_city]
                
                if increase < min_increase:
                    min_increase = increase
                    best_city = city
                    best_position = i
        
        # Insert the best city at the best position
        tour.insert(best_position + 1, best_city)
        unvisited.remove(best_city)
    
    # Return to the starting city to complete the tour
    tour.append(tour[0])
    
    return tour

# Example usage:
# distances is a 2D array representing the distance matrix between cities
# The element distances[i][j] represents the distance from city i to city j.
# Make sure distances[i][i] = 0 for all i.
distances = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

tour = insertion_heuristic_tsp(distances)
print("Optimal Tour:", tour)

