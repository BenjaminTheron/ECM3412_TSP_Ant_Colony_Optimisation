from tsp_aco_algorithm import *
import matplotlib.pyplot as plt
import numpy as np

# FOR EACH OF THE PARAMETERS THE BASE VALUES FOR OTHER PARAMETERS ARE USED (A = 1, B = 2, Q = 1, COLONY SIZE = 10, e = 0.5)

# FOR EACH GRAPH, INCLUDE THE PARAMETERS USED AND BEST SOLUTION LENGTH FOUND

def evaporation_rate_graph(file_name):
    # Graph for e values (x axis is the e value being tested y axis is the average of best solutions from 10 runs).
    # Find the average best solutions length over 10 runs for e values between 0 and 1
    e = 0
    average_of_best_runs = [0] * 11
    best_runs = []
    best_run = 0
    best_path = []
    with open('../docs/' + file_name, 'r') as file:
        file_data = file.read()

    xml_data1 = BeautifulSoup(file_data, 'xml')

    # Loop through each e value and calculate the average of the 10 best runs
    for index in range(0,11):
        # Loop 10 times for each given evaporation rate
        # Add the best solution to an array of values
        for run in range(0,10):
            (best_run, best_path) = ant_colony_optimisation_algorithm(xml_data1, 10, 1, 1, 2, 0, e)
            best_runs.append(best_run)
            average_of_best_runs[index] += best_run

        average_of_best_runs[index] /= 10
        e += 0.1

    xaxis = np.array([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1])
    # Ensures that every evaporation size being tested is show in the graph
    plt.xticks(xaxis)
    yaxis = np.array(average_of_best_runs)
    plt.plot(xaxis, yaxis)

    # Titles and labels for each of the axes
    plt.title("Evaporation Rate Performance on " + file_name[0:-4])
    plt.xlabel("Evaporation Rate")
    plt.ylabel("Average Best Solution Over 10 Runs")

    plt.show()

# Graph for colony size
def colony_size_graph(file_name):
    # x axis is the size of the colony, y axis is the average best solution over 10 runs
    colony_size = 10
    average_of_best_runs = [0] * 13
    best_runs = []
    best_run = 0
    best_path = []
    with open('../docs/' + file_name, 'r') as file:
        file_data = file.read()

    xml_data1 = BeautifulSoup(file_data, 'xml')

    # Loop through each colony size and calculate the average of the 10 best runs
    for index in range(0,13):
        # Loop 10 times for each given colony size
        # Add the best solution to an array of values
        for run in range(0,5):
            (best_run, best_path) = ant_colony_optimisation_algorithm(xml_data1, colony_size, 1, 1, 2, 0, 0.5)
            best_runs.append(best_run)
            average_of_best_runs[index] += best_run

        average_of_best_runs[index] /= 5
        colony_size += 10

    xaxis = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130])
    # Ensures that every colony size being evaluated is shown on the x-axis
    plt.xticks(xaxis)
    yaxis = np.array(average_of_best_runs)
    plt.plot(xaxis, yaxis)

    # Titles and labels for each of the axes
    plt.title("Colony Size Performance on " + file_name[0:-4])
    plt.xlabel("Colony Size")
    plt.ylabel("Average Best Solution Over 10 Runs")

    plt.show()

# Graph local heuristic functions (heuristic matrix and q value)
def q_value_graph(file_name):
    # x axis is the value of q, y axis is the average best solution over 10 runs
    q = 0.1
    average_of_best_runs = [0] * 9
    best_runs = []
    best_run = 0
    best_path = []
    with open('../docs/' + file_name, 'r') as file:
        file_data = file.read()

    xml_data1 = BeautifulSoup(file_data, 'xml')

    # Loop through each q value and calculate the average of the 10 best runs
    for index in range(0,9):
        # Loop 10 times for each given q value
        # Add the best solution to an array of values
        for run in range(0,5):
            (best_run, best_path) = ant_colony_optimisation_algorithm(xml_data1, 10, q, 1, 2, 0, 0.5)
            best_runs.append(best_run)
            average_of_best_runs[index] += best_run

        average_of_best_runs[index] /= 5
        q *= 10

    xaxis = np.array([0.1, 1, 10, 100, 1000, 10000, 100000, 1000000, 10000000])
    # Ensures that every q value being evaluated is shown on the x-axis
    plt.xticks(xaxis)
    yaxis = np.array(average_of_best_runs)
    plt.semilogx(xaxis, yaxis)

    # Titles and labels for each of the axes
    plt.title("Q Value Performance on " + file_name[0:-4])
    plt.xlabel("Q Value")
    plt.ylabel("Average Best Solution Over 10 Runs")

    plt.show()

# Graph for Beta values (heuristic importance factor)
def beta_value_graph(file_name):
    # x axis is the value of beta, y axis is the average best solution over 10 runs
    beta = 1
    average_of_best_runs = [0] * 11
    best_runs = []
    best_run = 0
    best_path = []
    with open('../docs/' + file_name, 'r') as file:
        file_data = file.read()

    xml_data1 = BeautifulSoup(file_data, 'xml')

    # Loop through each beta value and calculate the average of the 10 best runs
    for index in range(0, 11):
        # Loop 10 times for each given beta value
        # Add the best solution to an array of values
        for run in range(0, 5):
            (best_run, best_path) = ant_colony_optimisation_algorithm(xml_data1, 10, 1, 1, beta, 0, 0.5)
            best_runs.append(best_run)
            average_of_best_runs[index] += best_run

        average_of_best_runs[index] /= 5
        beta += 1

    xaxis = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
    # Ensures that every beta value being evaluated is shown on the x-axis
    plt.xticks(xaxis)
    yaxis = np.array(average_of_best_runs)
    plt.plot(xaxis, yaxis)

    # Titles and labels for each of the axes
    plt.title("Beta Value Performance on " + file_name[0:-4])
    plt.xlabel("Beta Value")
    plt.ylabel("Average Best Solution Over 10 Runs")

    plt.show()

# Graph for Alpha values (pheromone importance factor)
def alpha_value_graph(file_name):
    # x axis is the value of alpha, y axis is the average best solution over 10 runs
    alpha = 0
    average_of_best_runs = [0] * 11
    best_runs = []
    best_run = 0
    best_path = []
    with open('../docs/' + file_name, 'r') as file:
        file_data = file.read()

    xml_data1 = BeautifulSoup(file_data, 'xml')

    # Loop through each alpha value and calculate the average of the 10 best runs
    for index in range(0,11):
        # Loop 10 times for each given alpha value
        # Add the best solution to an array of values
        for run in range(0,5):
            (best_run, best_path) = ant_colony_optimisation_algorithm(xml_data1, 10, 1, alpha, 2, 0, 0.5)
            best_runs.append(best_run)
            average_of_best_runs[index] += best_run

        average_of_best_runs[index] /= 5
        alpha += 1

    xaxis = np.array([0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5])
    # Ensures that every alpha value being evaluated is shown on the x-axis
    plt.xticks(xaxis)
    yaxis = np.array(average_of_best_runs)
    plt.plot(xaxis, yaxis)

    # Titles and labels for each of the axes
    plt.title("Alpha Value Performance on " + file_name[0:-4])
    plt.xlabel("Alpha Value")
    plt.ylabel("Average Best Solution Over 10 Runs")

    plt.show()

# Graph for the algorithm running with the best set of parameters
def optimal_parameters_graph(file_name):
    # Using the seemingly best parameters (from the data shown in the graphs) run the aco algorithm multiple times to
    # Check the convergence behaviour and best solutions reached
    # Parameter values to be used for burma
    # alpha = 0.5
    # beta = 3
    # evaporation_rate = 0.3
    # colony_size = 130
    # q = 100
    # Parameter values to be used for brazil
    alpha = 0.5
    beta = 9
    evaporation_rate = 0.3
    colony_size = 130
    q = 500

    with open('../docs/' + file_name, 'r') as file:
        file_data = file.read()

    xml_data1 = BeautifulSoup(file_data, 'xml')

    # Call the function with the given parameters
    (best_fitness, best_path, average_solution_tracker) = ant_colony_optimisation_algorithm(xml_data1, colony_size, q, alpha, beta, 0, evaporation_rate)

    # Create an array whose size is the length of array returned by the aco algorithm (number of iterations)
    xaxis = []
    for x in range(0, len(average_solution_tracker)):
        xaxis.append(x)

    xaxis = np.array(xaxis)
    yaxis = np.array(average_solution_tracker)
    plt.plot(xaxis, yaxis)

    # Titles and labels for each of the axes
    plt.title("Optimised ACO Performance on " + file_name[0:-4] + ", Best Fitness Found: 26238")
    plt.xlabel("Iteration")
    plt.ylabel("Average Fitness Found")

    plt.show()


if __name__ == "__main__":
    # evaporation_rate_graph("burma14.xml")
    # evaporation_rate_graph("brazil58.xml")
    # colony_size_graph("burma14.xml")
    # colony_size_graph("brazil58.xml")
    # q_value_graph("burma14.xml")
    # q_value_graph("brazil58.xml")
    # beta_value_graph("burma14.xml")
    # beta_value_graph("brazil58.xml")
    # alpha_value_graph("burma14.xml")
    # alpha_value_graph("brazil58.xml")
    # optimal_parameters_graph("burma14.xml")
    optimal_parameters_graph("brazil58.xml")
