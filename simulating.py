#!/usr/bin/python3

""" a module that calculate simulating annealing algorithm"""


import math
import random

# Define a list of cities with their (x, y) coordinates.
cities = [(0, 0), (1, 2), (2, 4), (3, 1), (4, 3)]

def euclidean_distance(city1, city2):
    """
    Calculate the Euclidean distance between two cities.
    """
    x1, y1 = city1
    x2, y2 = city2
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def total_distance(route):
    """
    Calculate the total distance of a route.
    """
    distance = 0
    for i in range(len(route) - 1):
        distance += euclidean_distance(cities[route[i]], cities[route[i + 1]])
    # Return to the starting city
    distance += euclidean_distance(cities[route[-1]], cities[route[0]])
    return distance

def simulated_annealing_tsp(initial_route, initial_temperature, cooling_rate, max_iterations):
    current_route = initial_route
    current_distance = total_distance(current_route)
    best_route = current_route
    best_distance = current_distance

    for iteration in range(max_iterations):
        temperature = initial_temperature / (1 + cooling_rate * iteration)

        # Generate a neighboring route by reversing a random segment
        i, j = sorted(random.sample(range(len(current_route)), 2))
        neighbor_route = current_route[:i] + list(reversed(current_route[i:j])) + current_route[j:]

        neighbor_distance = total_distance(neighbor_route)
        distance_difference = neighbor_distance - current_distance

        if distance_difference < 0 or random.random() < math.exp(-distance_difference / temperature):
            current_route = neighbor_route
            current_distance = neighbor_distance

            if current_distance < best_distance:
                best_route = current_route
                best_distance = current_distance

    return best_route, best_distance

if __name__ == "__main__":
    initial_route = list(range(len(cities)))  # Initial route: 0 -> 1 -> 2 -> 3 -> 4 -> 0
    initial_temperature = 100.0
    cooling_rate = 0.03
    max_iterations = 10000

    best_route, best_distance = simulated_annealing_tsp(initial_route, initial_temperature, cooling_rate, max_iterations)

    print("Best Route:", best_route)
    print("Best Distance:", best_distance)

