"""Solves the TSP using an ACO algorithm"""
import math
import random
import copy
import time
from bs4 import BeautifulSoup


def initialisation(xml_data: []) -> ([[float]], [[float]]):
    """
    Initialises the graph the ants will be traversing (the distnace matrix),
    as well as the corresponding pheromone matrix, t, enablind the ants to
    move through the graph and see the pheromone on a given edge.

    Args:
        xml_data ([]): The raw data extracted from the provided XML datasets,
            used to find the nodes in the graph and the connections between
            them. BeautifulSoup extracts this as a list.

    Returns:
        graph ([[float]]): Returns the initialised distance matrix for the
            graph as a 2D array, where each index stores the distance from
            one node to another node (each index is an edge between nodes).
        t ([[float]]): Returns the initialised pheromone matrix for the graph
            as a 2D array, where each index stores the pheromone on a given
            edge between two nodes.
    """
    # Extracts the raw XML data for the node and edge objects
    nodes = xml_data.find_all('vertex')
    edges = xml_data.find_all('edge')

    # Extracts the raw XML data for the accuracy all values are stored to
    accuracy = xml_data.find_all('doublePrecision')
    accuracy = int(accuracy[0].string)

    # Creates a graph to store the edges between nodes in the graph
    # Node values start from 0 so a 2D array can be used
    graph = [0] * len(nodes)
    # A 2D array is used to represent the pheromone matrix
    t = [0] * len(nodes)
    # Initially these arrays are filled with 0s as placeholder values
    for i in range(0, len(nodes)):
        graph[i] = [0] * len(nodes)
        t[i] = [0] * len(nodes)

    # Used to track the current edge being looked at
    index = 0
    # Adds each edge to the graph
    for j in range(0, len(nodes)):
        for k in range(0, len(nodes)):
            # If the edge is on a leading diagonal, its value is set to 0
            if j == k:
                graph[j][k] = 0
            else:
                # Extracts the cost of the edge from the XML data
                cost = edges[index]['cost']
                cost = float(cost)
                graph[j][k] = round(cost, accuracy)
                index += 1

    # Each index in the pheromone matrix is initialised with a random value
    # between 0 and 1
    for a in range(0, len(nodes)):
        for b in range(0, len(nodes)):
            # If the index is on the leading diagonal it is set to 0
            if a == b:
                t[a][b] = 0
            else:
                t[a][b] = round(random.random(), accuracy)

    return (graph, t)


def to_string(matrix: [[float]]) -> None:
    """
    Outputs the contents of any 2D array, row by row.

    Args:
        matrix ([[int]]): The 2D array to be output.
    """
    for i in range(0, len(matrix[0])):
        print(matrix[i])


def evaporate_pheromone(t: [[float]], evaporation_rate: float) -> [[float]]:
    """
    Evaporates (reduces by some multiple) the pheromone value of every edge
    stored in the pheromone matrix supplied to it.

    Args:
        t ([[float]]): The pheromone matrix being used by the ACO, which
            stores a float value for each edge in the graph indicating the
            amount of pheromone on it.
        evaporation_rate: Determines the amount of pheromone that's evaporated
            after each iteration, stored as a float as it must be between 0 and
            1 (in order for the amount of pheromone to decrease).

    Returns:
        t ([[float]]): Returns the updated pheromone matrix once all the
            values stored in it have been evaporated.
    """
    # Loop through every index in the pheromone matrix and multiply its value
    # By the evaporation rate
    for i in range(0, len(t[0])):
        for j in range(0, len(t[0])):
            t[i][j] = (1-evaporation_rate) * t[i][j]

    return t


def update_pheromone(graph: [[float]], paths: [[int]], t: [[float]],
                     q: int) -> [[float]]:
    """
    Updates the pheromone value for each edge in the pheromone matrix that was
    used in the path taken by an ant, the update value is proportional to
    length of the path taken (ants which take shorter paths deposit more
    pheromone).

    Args:
        graph ([[float]]): A 2D array representing the graph the ants are
            traversing. This is required so that the fitness of each ant path
            can be calculated.
        paths ([[int]]): A 2D array storing the paths taken by each ant in the
            colony during the last iteration. Storing them this way allows for
            each path to be easily accessed and manipulated.
        t ([[float]]): The pheromone matrix being used by the ACO, which
            stores a float value for each edge in the graph indicating the
            amount of pheromone on it.
        q (int): A fixed local heuristic value for to reward paths
            proportionally to their fitness value. An integer for ease of use.

    Returns:
        t ([[float]]): Returns the updated pheromone matrix once all edges
            which were used in the prior iteration had their value updated.

    """

    # For every path taken by the ants
    for i in range(0, len(paths)):
        # Find its fitness and update every corresponding edge in the
        # Pheromone matrix by a proportional value
        fitness = path_length(graph, paths[i])
        for j in range(1, len(paths[i])):
            t[paths[i][j-1]][paths[i][j]] += q/fitness

    return t


def path_length(graph: [[float]], path: [int]) -> float:
    """
    Args:
        graph ([[float]]): A 2D array representing the graph the ants are
            traversing. This is required so that the fitness of each ant path
            can actually be calculated.
        path ([int]): An array representing the path taken by an individual
            ant, here each index represents the node the ant is at, at a given
            point in the traversal.

    Returns:
        fitness (float): The length of the path taken by the ant, provided as
            a float as some edges may have decimal value.
    """
    fitness = 0
    # Loop for the length of the path taken
    for i in range(1, len(path)):
        # Find the cost of each edge taken from the main graph array
        fitness += graph[path[i-1]][path[i]]

    return fitness


def print_path(path: [int]) -> str:
    """
    Creates a formatted string for the path taken by the ant and returns it.
    This is done to increase help diagnostics and make it easier to interpret
    the paths taken.

    Args:
        path ([int]): An array representing the path taken by an individual
            ant, here each index represents the node the ant is at, at a given
            point in the traversal.

    Returns:
        return_string (str): The formatted string of the path taken, returned
            as a string for ease of manipulation.

    """
    return_string = ""
    # Adds an arrow between each edge between an internal node in the path
    for i in range(0, len(path) - 1):
        return_string += str(path[i]) + " -> "

    # Adds the starting string to the end of the string
    # All paths must return to the start
    return_string += str(path[-1])

    return return_string


def ant_colony_optimisation_algorithm(xml_data: [],
                                      m: int,
                                      q: int,
                                      alpha: float,
                                      beta: int,
                                      starting_node: int,
                                      evaporation_rate: float
                                      ) -> (float, [int], float):
    """
    The main algorithm for the ant colony optimisation method. After the graph
    has been initialised it loops through 10,000 fitness evaluations,
    placing the ants on the graph at the specified start node and having them
    traverse through the graph. When choosing the next node to visit, each
    valid edge moving from the current edge is assigned a desiribility value.
    After each ant in the colony (population) has completed its path, the
    pheromone matrix is updated then evaporated according to a specified
    evaporation rate. This process then repeats until 10,000 fitness
    evaluations have been reached. Note the best fitness value and
    corresponding path taken are tracked throughout the entire process.
    All the parameters which influence the program are taken as arguments.

    Args:
        xml_data ([]): The raw data extracted from the provided XML datasets,
            used to find the nodes in the graph and the connections between
            them. BeautifulSoup extracts this as a list.
        m (int): The colony size, this is the number of ants that traverse
            the graph in each iteration. Stored as an int as you can only have
            a whole number of ants. Base value of 10.
        q (int): A fixed local heuristic value for to reward paths
            proportionally to their fitness value. An integer for ease of use.
            Base value of 1.
        alpha (float): A pheromone importance factor that decreases/ increases
            the weight pheromone has on an edge's desirability. Stored as a
            float as the optimal value was found to be 0.5. Base value of 1.
        beta (int): A heuristic importance factor that decreases/ increases
            the weight an edge's distance has on its desirabiility. Stored as
            an int as the optimal value was found to be 3(burma) and 9
            (brazil58). Base value of 2.
        starting_node (int): The index representing the node the each ant will
            start its path from. Base value of 0.
        evaporation_rate (float): The rate at which pheromone is evaporated
            from the pheromone matrix after each iteration. Stored as a float
            as this value must be betwee 0 and 1.

    Returns:
        (best_fitness,
        best_path,
        average_solution_tracker) (float, [int], [float]): Returns a tuple
            storing the best fitness found, its accompanying path and the
            average solution length found at each iteration (only used for
            matplotlib).
    """
    # The paths taken by each of the ants
    paths = []
    # The best fitness found thus far
    best_fitness = math.inf
    # The path associated with this best fitness value
    best_path = []
    # The index representing the current node being looked at
    current_node = starting_node
    # Used to help track the convergence characterisitcs of the algorithm
    # (enables matplot lib to plot the convergence behaviour)
    average_solution_tracker = []

    # Initialise the graph and pheromone matrix
    (graph, t) = initialisation(xml_data)
    accuracy = xml_data.find_all('doublePrecision')
    accuracy = int(accuracy[0].string)

    # Initialise the heuristic matrix
    # Each index in the graph stores num_nodes edges, so it can be used to
    # size the heuristic matrix
    heuristic_matrix = [0] * len(graph[0])
    # Initialised so that every index holds a placeholder value of 0
    for i in range(0, len(graph[0])):
        heuristic_matrix[i] = [0] * len(graph[0])

    # Loop through each element in the heuristic matrix
    for j in range(0, len(heuristic_matrix[0])):
        for k in range(0, len(heuristic_matrix[0])):
            # If the index is on the leading diagonal it remains 0
            if j != k:
                # Otherwise the index = 1/ edge length
                heuristic_matrix[j][k] = round((1/graph[j][k]), accuracy)

    # Used for tracking in Matplotlib
    iteration = 0
    # Stop executing the algorithm after 10,000 fitness evaluations
    fitness_evaluations = 0
    while fitness_evaluations < 10_000:
        # For every fitness evaluation re-initialise the array storing the
        # paths taken by the ants
        paths = [0] * m
        for a in range(0, m):
            paths[a] = []

        # For consistency sake, the starting node is always set to 0 at the
        # start of each iteration
        starting_node = 0
        # Finds a path through the graph with each ant
        for ant in range(0, m):
            # If the number of fitness evaluations has been surpassed break
            # out the loop
            if fitness_evaluations > 10_000:
                break

            # Create a copy of the heuristic matrix so it can be used
            # without impacting the original
            H = copy.deepcopy(heuristic_matrix)
            # Reset the current node being looked at to the starting node
            current_node = starting_node
            # Creates an array to store the nodes that must still be visited
            nodes = []
            for c in range(0, len(graph[0])):
                nodes.append(c)

            # Add the starting node to the path taken
            paths[ant].append(current_node)
            # Remove the starting node from the list of nodes to visit
            nodes.remove(current_node)

            # Traverses until there are no more nodes to visit
            while len(nodes) > 0:
                # Remove the current node from the heuristic matrix
                # For all ants this will initially be the starting node
                for d in range(0, len(H[0])):
                    H[d][current_node] = 0

                # Calculate the transition (desirability) probabilities
                # Start by calculating the numerator values for each edge, as
                # well as the sum of these numerators
                sum = 0
                numerators = [0] * len(H[0])
                for e in range(0, len(H[0])):
                    if e in nodes:
                        # The numerator is the desirability of a given edge
                        numerators[e] = ((t[current_node][e])**alpha) * (
                                         (H[current_node][e])**beta)
                        # The sum is the sum of the desirability of all edges
                        # leaving the current node
                        sum += numerators[e]

                # If the sum is 0, randomly choose a node from the list of
                # remaning nodes
                if sum == 0:
                    current_node = random.choice(nodes)
                else:
                    # Otherwise, find the probability of choosing each node
                    # This is edge desirability/ total desirability
                    probability = []
                    for f in range(0, len(numerators)):
                        probability.append(numerators[f]/sum)

                    cumulative_probability = 0
                    random_num = random.random()
                    # Generate a random number, where the first edge whose
                    # cumulative probability >= this value represents the
                    # node to visit next
                    for g in range(0, len(numerators)):
                        cumulative_probability += probability[g]
                        if cumulative_probability >= random_num:
                            current_node = g
                            break

                # Add the next node to visit to the path taken
                paths[ant].append(current_node)
                # Remove the next node to visit from the list of unvisited
                # nodes
                nodes.remove(current_node)

            # The ant must return to the starting node to complete the path
            paths[ant].append(starting_node)

            # Check if the ants current path is better than the global best
            # If it is, update the best fitness value and best path taken
            current_path_length = path_length(graph, paths[ant])
            if current_path_length < best_fitness:
                best_fitness = current_path_length
                best_path = paths[ant]

            # As the fitness of a solution has been evaluated, increment
            fitness_evaluations += 1

        # Once all the paths have been found for this iteration, update the
        # pheromone values
        t = update_pheromone(graph, paths, t, q)

        # Once the pheromone matrix has been updated, evaporate the pheromone
        # values
        t = evaporate_pheromone(t, evaporation_rate)

        iteration += 1

        # Calculate the average path length for every iteration bar the last
        # Fewer than normal paths taken skews the result.
        if fitness_evaluations <= 10000:
            average_length = 0
            for path in paths:
                average_length += path_length(graph, path)

            average_length = average_length/m
            # print("The average length of the paths in this iteration is:
            #       ", average_length)
            # print("The best path length found so far is:
            #       ", best_fitness, "\n")
            # Used for tracking convergence in Matplotlib
            average_solution_tracker.append(average_length)

    # print("The number of iterations this algorithm executed was:
    #       ", iteration)
    return (best_fitness, best_path, average_solution_tracker)


if __name__ == "__main__":
    # Takes the name of the XML file to be used as input
    FILE_NAME = str(input("What is the full name (incl extension)"
                          + " of the file to be used:"))

    # Deconstructs the XML file to determine the number of nodes and the
    # connections between each of the nodes
    with open('../docs/' + FILE_NAME, 'r') as file:
        file_data = file.read()

    # Uses BeautifulSoup to extract the raw XML data for the whole file
    xml_data = BeautifulSoup(file_data, 'xml')

    # Executes the ACO with the given parameters and times its execution
    start_time = time.time()
    (best_fitness,
     best_path,
     average_solution_tracker) = ant_colony_optimisation_algorithm(xml_data,
                                                                   130,
                                                                   500,
                                                                   0.5,
                                                                   9,
                                                                   0,
                                                                   0.3)
    end_time = time.time()

    # The best fitness, its path and the time taken to execute are displayed
    # on screen
    print("The best fitness found was:", best_fitness, "\n")
    print("The best path found was:", print_path(best_path))
    print("The time taken by this algorithm was:", end_time-start_time, "s")
