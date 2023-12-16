# ECM3412 Ant Colony Optimisation Algorithm to Solve the Travelling Salesperson Problem

## Introduction
This project is intended to implement an ant colony optimisation algorithm to solve the travelling salesperson problem
for certain datasets, additionally, it is meant to explore the impact of how the parameters used within the algorithm
impact its ability to converge upon a value and/or reach the optimal solution.

## Prerequisites and Installation
Only built in modules and libraries were used in the ACO implementation, so there are no prerequisites or installations
required to use the main algorithm.

To create the graphs and plots of the results of the algorithm, Matplotlib was used, refer to the website below for
installation instructions: 
  - https://matplotlib.org/stable/users/installing/index.html

## Project Tutorial
Two datasets were provided for this project, 'burma14.xml' and 'brazil58.xml'. Installing the project, moving to the src folder
(cd to ../ECM3412_CA/src), enables you to do the following:

  - Execute the basic ACO algorithm: Execute the command 'python3 tsp_aco_algorithm.py', then enter the exact filname of one of
    the aforementioned datasets and press enter.

  - Execute the Elitist ACO algorithm: Execute the command 'python3 elitist_aco_algorithm.py' then enter the exact filname of one of
    the aforementioned datasets and press enter.

  - Execute the MMAS ACO algorithm: Execute the command 'python3 mmas_aco_algorithm.py' then enter the exact filname of one of
    the aforementioned datasets and press enter.

  - Execute the Hybrid ACO algorithm: Execute the command 'elitist_mmas_aco_algorithm.py' then enter the exact filname of one of
    the aforementioned datasets and press enter.

After execution, each algorithm will output the best fitness found by the algorithm along with the accompanying path taken. Additonal
performance metrics such as the average path length for a given iteration can be printed out (print the average_length variable, which
can be found via ctrl-f)

To add new datasets to execute the algorithm on, first ensure they conform to the same strucure as the existing two datasets. Then
place them into the docs folder in the project directory and follow the exact steps provided above for the respective algorithm.

To use the graphs to analyse the impact of different parameters on the ACO you can do the following:

  - Starting from the src folder, navigate to the graphs folder (../src/graphs).
  - A separate program is used to generate graphs for each variant of the algorithm, so after deciding on the ACO variant to analyse
    select the desired program, aco_results_plotter.py (basic ACO), elitist_aco_results_plotter.py (elitist ACO), mmas_aco_results_plotter.py
    (MMAS ACO) or elitist_mmas_results_plotter.py (elitist MMAS hybrid ACO).
  - These graphs can take a while to generate (especially for the larger brazil58 dataset), taking up to ~50mins, so they are only run one at a time
    you can then navigate to the functions for each parameter, changing the value, number of iterations, etc.
  - Uncomment functions you wish to run and visa versa.
  - Execute the command 'python3 program_name.py' and wait for the graph to generate.

## Testing
No testing was required in the spec, and so no testing was implemented.

### Notes
All functionality that was required by the specification was provided; however, there are a number of ways
in which the algorithms can be extended:

  - Add metrics to track the amount of memory consumed by the algorithm to track its space complexity.
  - Further optimise the algorithms and their operations to further reduce execution time.
  - Testing for the algorithms.

## Details

#### Authors
Benjamin Theron

#### License
MIT License
