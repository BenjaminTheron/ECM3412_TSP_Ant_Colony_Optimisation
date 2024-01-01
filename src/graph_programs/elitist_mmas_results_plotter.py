from elitist_mmas_aco_algorithm import *
import matplotlib.pyplot as plt
import numpy as np


# Graph for the elistist MMAS algorithm
def elitist_mmas_graph(file_name):
    # Plots the convergence and best solution reached by the elitist MMAS graph
    # Parameters to be used
    elititst_ant_proportion = 0.2
    alpha = 0.5
    beta = 3
    evaporation_rate = 0.1
    colony_size = 130
    q = 1000
    upper_bound = 1
    lower_bound = 30

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
    plt.title("Optimised Elitist-MMAS ACO Performance on " + file_name[0:-4] + ", Best Fitness Found: ")
    plt.xlabel("Iteration")
    plt.ylabel("Average Fitness Found")

    plt.show()

if __name__ == "__main__":
    # Run three times
    elitist_mmas_graph("burma14.xml")
    # elitist_mmas_graph("brazil58.xml")