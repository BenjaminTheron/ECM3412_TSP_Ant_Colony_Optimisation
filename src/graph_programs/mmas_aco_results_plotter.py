from mmas_aco_algorithm import *
import matplotlib.pyplot as plt
import numpy as np

# Graph to plot the effect of the minimum pheromone value in the MMAS algorithm
def mmas_graph_min(file_name):
    # Show the effect of changing the minimum and maximum amount of pheromone
    # Max value is base fixed at 10
    # Min value is base fixed at 0

    # x axis is the value of alpha, y axis is the average best solution over 10 runs
    min_value = 0 # Goes up in increments of 0.5
    max_value = 10 # Goes up in increments of 10
    average_of_best_runs = [0] * 5
    best_runs = []
    best_run = 0
    best_path = []
    with open('../docs/' + file_name, 'r') as file:
        file_data = file.read()

    xml_data1 = BeautifulSoup(file_data, 'xml')

    # Loop through each alpha value and calculate the average of the 10 best runs
    for index in range(0,5):
        # Loop 10 times for each given alpha value
        # Add the best solution to an array of values
        for run in range(0,5):
            (best_run, best_path, average_solution_tracker) = ant_colony_optimisation_algorithm(xml_data1, 10, 1, 1, 2, 0, 0.5, max_value, min_value)
            best_runs.append(best_run)
            average_of_best_runs[index] += best_run

        average_of_best_runs[index] /= 5
        min_value += 0.5

    xaxis = np.array([0, 0.5, 1, 1.5, 2,])
    # Ensures that every alpha value being evaluated is shown on the x-axis
    plt.xticks(xaxis)
    yaxis = np.array(average_of_best_runs)
    plt.plot(xaxis, yaxis)

    # Titles and labels for each of the axes
    plt.title("MMAS Performance on " + file_name[0:-4])
    plt.xlabel("Minimum Pheromone Value")
    plt.ylabel("Average Best Solution Over 10 Runs")

    plt.show()


# Graph to plot the effect of the maximum pheromone value in the MMAS algorithm
def mmas_graph_max(file_name):
    # Show the effect of changing the minimum and maximum amount of pheromone
    # Max value is base fixed at 10
    # Min value is base fixed at 0

    # x axis is the value of alpha, y axis is the average best solution over 10 runs
    min_value = 0 # Goes up in increments of 0.5
    max_value = 10 # Goes up in increments of 10
    average_of_best_runs = [0] * 11
    best_runs = []
    best_run = 0
    best_path = []
    with open('../docs/' + file_name, 'r') as file:
        file_data = file.read()

    xml_data1 = BeautifulSoup(file_data, 'xml')

    # Loop through each alpha value and calculate the average of the 10 best runs
    for index in range(0,6):
        # Loop 10 times for each given alpha value
        # Add the best solution to an array of values
        for run in range(0,10):
            (best_run, best_path) = ant_colony_optimisation_algorithm(xml_data1, 10, 1, 1, 2, 0, 0.5, max_value, min_value)
            best_runs.append(best_run)
            average_of_best_runs[index] += best_run

        average_of_best_runs[index] /= 10
        max_value += 10

    xaxis = np.array([0, 0.5, 1, 1.5, 2,])
    # Ensures that every alpha value being evaluated is shown on the x-axis
    plt.xticks(xaxis)
    yaxis = np.array(average_of_best_runs)
    plt.plot(xaxis, yaxis)

    # Titles and labels for each of the axes
    plt.title("MMAS Performance on " + file_name[0:-4])
    plt.xlabel("Minimum Pheromone Value")
    plt.ylabel("Average Best Solution Over 10 Runs")

    plt.show()

if __name__ == "__main__":
    # Tested with three upper bound values, 10, 20 and 30
    # mmas_graph_min("burma14.xml")
    mmas_graph_min("brazil58.xml")
    # mmas_graph_max("burma14.xml")
    # mmas_graph_max("brazil58.xml")