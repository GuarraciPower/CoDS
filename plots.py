import json
import matplotlib.pyplot as plt
import numpy as np

# Define the grouping size variable
GROUP_SIZE = 1000

def plot_bloom_filter_metrics(results, data_type, metric, y_label):
    grouped_data = {}
    for hash_function in results[data_type]["bloom_filter"]:
        values = results[data_type]["bloom_filter"][hash_function][metric]
        grouped_data[hash_function] = [values[i:i + GROUP_SIZE] for i in range(0, len(values), GROUP_SIZE)]

    plt.figure(figsize=(12, 8))

    for hash_function, groups in grouped_data.items():
        mean_values = [np.mean(group) for group in groups]
        x_positions = range(0, len(mean_values) * GROUP_SIZE, GROUP_SIZE)

        plt.plot(x_positions, mean_values, marker='o', linestyle='-', label=f"{hash_function}")

    plt.title(f"{metric.replace('_', ' ').title()} for Bloom Filters ({data_type})")
    plt.xlabel("Number of Elements")
    plt.ylabel(y_label)
    plt.legend()
    plt.grid(True)
    plt.savefig(f"results/{data_type}_bloom_filter_{metric}.png")
    plt.close()

def plot_algorithm_metrics(results, data_type, metric, y_label):
    grouped_data = {
        "linear_search": [results[data_type]["linear_search"][metric][i:i + GROUP_SIZE] for i in range(0, len(results[data_type]["linear_search"][metric]), GROUP_SIZE)],
        "bst": [results[data_type]["bst"][metric][i:i + GROUP_SIZE] for i in range(0, len(results[data_type]["bst"][metric]), GROUP_SIZE)],
        "avl_tree": [results[data_type]["avl_tree"][metric][i:i + GROUP_SIZE] for i in range(0, len(results[data_type]["avl_tree"][metric]), GROUP_SIZE)]
    }

    plt.figure(figsize=(12, 8))

    for algorithm, groups in grouped_data.items():
        mean_values = [np.mean(group) for group in groups]
        x_positions = range(0, len(mean_values) * GROUP_SIZE, GROUP_SIZE)

        plt.plot(x_positions, mean_values, marker='o', linestyle='-', label=f"{algorithm}")

    plt.title(f"{metric.replace('_', ' ').title()} for Algorithms ({data_type})")
    plt.xlabel("Number of Elements")
    plt.ylabel(y_label)
    plt.legend()
    plt.grid(True)
    plt.savefig(f"results/{data_type}_algorithms_{metric}.png")
    plt.close()

def plot_false_positive_prob(results):
    for data_type in results:
        grouped_data = {}
        for hash_function in results[data_type]["bloom_filter"]:
            false_positive_rate = results[data_type]["bloom_filter"][hash_function]["false_positive_rate"]
            key = f"{data_type} ({hash_function})"
            grouped_data[key] = [false_positive_rate[i:i + GROUP_SIZE] for i in range(0, len(false_positive_rate), GROUP_SIZE)]

        plt.figure(figsize=(12, 8))

        for label, groups in grouped_data.items():
            mean_values = [np.mean(group) for group in groups]
            x_positions = range(0, len(mean_values) * GROUP_SIZE, GROUP_SIZE)

            plt.plot(x_positions, mean_values, marker='o', linestyle='-', label=label)

        plt.title(f"False Positive Probability (FPP) in Relation to Number of Elements Added ({data_type})")
        plt.xlabel("Number of Elements Added")
        plt.ylabel("False Positive Probability (FPP)")
        plt.legend()
        plt.grid(True)
        plt.savefig(f"results/false_positive_prob_elements_{data_type}.png")
        plt.close()

def main():
    with open("results/benchmark_results.json", "r") as file:
        results = json.load(file)

    for data_type in results:
        plot_bloom_filter_metrics(results, data_type, "add_time", "Add Time (s)")
        plot_bloom_filter_metrics(results, data_type, "check_time", "Check Time (s)")
        plot_bloom_filter_metrics(results, data_type, "false_positive_rate", "False Positive Rate")
        plot_algorithm_metrics(results, data_type, "add_time", "Add Time (s)")
        plot_algorithm_metrics(results, data_type, "search_time", "Search Time (s)")

    plot_false_positive_prob(results)

if __name__ == "__main__":
    main()
