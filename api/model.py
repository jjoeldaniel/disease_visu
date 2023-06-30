import csv
import json
import numpy as np
from scipy.stats import pearsonr


def load_data(filename):
    data = []
    with open(filename, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data


def calculate_stats(data):
    coastal_states = []
    non_coastal_states = []
    total_states = 0
    total_density = 0
    coastal_density = 0
    non_coastal_density = 0
    total_outbreaks = 0
    coastal_outbreaks = 0
    non_coastal_outbreaks = 0

    for state in data:
        coastal = state["coastal"]
        density = float(state["density"])
        outbreaks = int(state["outbreaks"])

        total_states += 1
        total_density += density
        total_outbreaks += outbreaks

        if coastal == "true":
            coastal_states.append(state)
            coastal_density += density
            coastal_outbreaks += outbreaks
        else:
            non_coastal_states.append(state)
            non_coastal_density += density
            non_coastal_outbreaks += outbreaks

    total_coastal_states = len(coastal_states)
    total_non_coastal_states = len(non_coastal_states)

    coastal_outbreak_percentage = (coastal_outbreaks / total_outbreaks) * 100

    density_values = np.array([float(state["density"]) for state in data])
    outbreak_values = np.array([int(state["outbreaks"]) for state in data])

    density_outbreak_correlation, _ = pearsonr(density_values, outbreak_values)

    coastal_state_labels = np.array(
        [1 if state["coastal"] == "true" else 0 for state in data]
    )
    coastal_outbreak_labels = np.array([int(state["outbreaks"]) for state in data])

    coastal_outbreak_correlation, _ = pearsonr(
        coastal_state_labels, coastal_outbreak_labels
    )

    stats = {
        "Total States": total_states,
        "Coastal States": total_coastal_states,
        "Non-Coastal States": total_non_coastal_states,
        "Total Density": total_density,
        "Coastal Density": coastal_density,
        "Non-Coastal Density": non_coastal_density,
        "Total Outbreaks": total_outbreaks,
        "Coastal Outbreaks": coastal_outbreaks,
        "Non-Coastal Outbreaks": non_coastal_outbreaks,
        "Coastal Outbreak Percentage": coastal_outbreak_percentage,
        "Density-Outbreak Correlation": density_outbreak_correlation,
        "Coastal Outbreak Correlation": coastal_outbreak_correlation,
    }

    return stats


# Replace 'data.csv' with the actual filename of your CSV file
data = load_data("data.csv")
stats = calculate_stats(data)

# Output to data.json
with open("data.json", "w") as file:
    json.dump(stats, file, indent=2)
