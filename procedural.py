import numpy as np

def attach_names(data_array, names):
    """Attaches names to an input array of data"""
    named_data = []
    if len(data_array) != len(names):
        raise ValueError("Number of datasets and number of names do not match")
    for i in range(len(names)):
        new_entry = {'name': names[i], 'data': data_array[i]}
        named_data.append(new_entry)
    return named_data

example_data = np.array([[1., 2., 3.], [4., 5., 6.]])
names = ['Jim', 'Sunita']

output = attach_names(example_data, names)

print(output)