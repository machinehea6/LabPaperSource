# Format is amperage:distance in inches before the magnet breaks free
trial_one_results = {.5:2.75,1:6.5,1.5:9.5,2:15.25}
trial_two_results = {.5:3.25,1:7.25,1.5:9.51,2:15.5}
trial_three_results = {.5:3.5,1:7,1.5:11.75,2:16}

all_trials = [trial_one_results,trial_two_results,trial_three_results]

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

    label_list = ['Trial One','Trial Two','Trial Three']
    plt.scatter(
        key_value_list_maker(trial)[1],
        key_value_list_maker(trial)[0],
        label=label_list[label],
        alpha=.3)
    label = label + 1
plt.xticks(list([.5,1,1.5,2]))
plt.xlabel("Amperes of Current")
plt.ylabel("Inches of Displacement")
plt.legend()
plt.savefig('amps_vs_dispv0.png', dpi = 800)
