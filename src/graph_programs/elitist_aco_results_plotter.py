from elitist_aco_algorithm import *
import matplotlib.pyplot as plt
import numpy as np

# Graph for the elitist algorithm
def elitist_aco_graph(file_name):
    # Show the effect of changing the amount of ants allowed through
    # Here a colony size of 100 is used so that each proportion of ants allowed through still has a decent population size
    proportion_ants_allowed = 0.1
    # x axis is the proportionof ants allowed, y axis is the average best solution over 10 runs
    average_of_best_runs = [0] * 10
    best_runs = []
    best_run = 0
    best_path = []
    with open('../docs/' + file_name, 'r') as file:
        file_data = file.read()

    xml_data1 = BeautifulSoup(file_data, 'xml')

    # Loop through each proportion value and calculate the average of the 10 best runs
    for index in range(0,10):
        # Loop 10 times for each given proportion value
        # Add the best solution to an array of values
        for run in range(0,5):
            (best_run, best_path, average_solution_tracker) = ant_colony_optimisation_algorithm(xml_data1, 100, 1, 1, 2, 0, proportion_ants_allowed, 0.5)
            best_runs.append(best_run)
            average_of_best_runs[index] += best_run

        average_of_best_runs[index] /= 5
        proportion_ants_allowed += 1

    xaxis = np.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1])
    # Ensures that every value being evaluated is shown on the x-axis
    plt.xticks(xaxis)
    yaxis = np.array(average_of_best_runs)
    plt.plot(xaxis, yaxis)

    # Titles and labels for each of the axes
    plt.title("Elitist ACO Performance on " + file_name[0:-4])
    plt.xlabel("Elitist Proportion")
    plt.ylabel("Average Best Solution Over 10 Runs")

    plt.show()


if __name__ == "__main__":
    # elitist_aco_graph("burma14.xml")
    elitist_aco_graph("brazil58.xml")