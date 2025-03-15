# Format is amperage:degrees of displacement
trial_one_results = {1:2,2:2,3:3,4:3,5:4,6:4,7:4,8:5}


all_trials = [trial_one_results]

import matplotlib.pyplot as plt
import numpy as np

def key_value_list_maker(arg1: dict):
    keys = []
    values = []
    for key in arg1:
        keys.append(key)
    for key in keys:
        values.append(arg1[key])

    return [values, keys]

plt.figure(figsize=(8,4))
label = 0
for trial in all_trials:


    plt.scatter(
        key_value_list_maker(trial)[1],
        key_value_list_maker(trial)[0],
        label= "Trial One",
        alpha=.7)
    label = label + 1
plt.xticks(list([1,2,3,4,5,6,7,8]))
plt.xlabel("Amperes of Current")
plt.ylabel("Degrees of Displacement")
plt.legend()


plt.savefig('amps_vs_degrees.png', dpi = 800)
