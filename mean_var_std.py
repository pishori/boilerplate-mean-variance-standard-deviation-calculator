import numpy as np

def calculate(my_list):
    calculations = ['mean', 'variance', 'standard deviation', 'max', 'min', 'sum']
    mean_var_std = {}

    if len(my_list) < 9:
        raise ValueError("List must contain nine numbers.")
    np_list = np.array(my_list)
    np_matrix = np_list.reshape(3, 3)

    mean = np.mean
    variance = np.var
    standard_deviation = np.std
    maximum = np.max
    minimum = np.min
    summation = np.sum

    operations = [mean, variance, standard_deviation, maximum, minimum, summation]
    operands_calculations = zip(operations, calculations)
    for operand, calculation in operands_calculations:
        mean_var_std[calculation] = list((operand(np_matrix, 0).tolist(), operand(np_matrix, 1).tolist(), operand(np_matrix)))
    
    return mean_var_std


calculate([0, 1, 2, 3, 4, 5, 6, 7, 8])