import re
from typing import List
import matplotlib.pyplot as plt
import argparse
import os


def parse_log(log_file):
    """Parse the log file and extract average recall and average calculation."""
    results = []
    with open(log_file, 'r') as file:
        for line in file:
            # Use regex to find the average recall and average calculation
            match = re.search(r'Average recall: ([\d.]+), avg calc: ([\d.]+)', line)
            if match:
                recall = float(match.group(1))
                avg_calc = float(match.group(2))
                results.append((recall, avg_calc))
    return results

def round_list(data, precision = 3) -> List[float]:
    return [round(value, precision) for value in data]


def plot_comparison(log_1_results, log_2_results, output_file):
    """Plot the comparison chart for the two algorithms and save it."""
    recalls_1, avg_calcs_1 = zip(*log_1_results) if log_1_results else ([], [])
    recalls_2, avg_calcs_2 = zip(*log_2_results) if log_2_results else ([], [])

    recalls_1 = round_list(recalls_1)
    recalls_2 = round_list(recalls_2)

    plt.figure(figsize=(8, 8))

    plt.plot(avg_calcs_1, recalls_1, color='blue', label='Original', alpha=0.6)
    plt.plot(avg_calcs_2, recalls_2, color='orange', label='Modified', alpha=0.6)

    # Adding labels and title
    plt.title('Comparison of Algorithm Performance')
    plt.ylabel('Average Recall')
    plt.xlabel('Average Calculation Time')
    # plt.ylim(0, 1)
    plt.xlim(0, max(max(avg_calcs_1, default=0), max(avg_calcs_2, default=0)) * 1.1)

    # Adding a legend
    plt.legend()

    # Show grid
    plt.grid(True)

    # Save the plot as an image file
    plt.savefig(output_file)
    plt.close()


def main():
    # Set up command line argument parsing
    parser = argparse.ArgumentParser(description='Compare two algorithms based on log files.')
    parser.add_argument('log_1', type=str, help='Path to the first log file (Algorithm 1)')
    parser.add_argument('log_2', type=str, help='Path to the second log file (Algorithm 2)')
    parser.add_argument('--output', type=str, default='comparison_chart.png', help='Output filename for the comparison chart')

    args = parser.parse_args()

    # Check if log files exist
    if not os.path.isfile(args.log_1):
        print(f"Error: Log file '{args.log_1}' not found.")
        return
    if not os.path.isfile(args.log_2):
        print(f"Error: Log file '{args.log_2}' not found.")
        return

    # Parse the log files
    log_1_results = parse_log(args.log_1)
    log_2_results = parse_log(args.log_2)

    # Plot the comparison chart and save it
    plot_comparison(log_1_results, log_2_results, args.output)
    print(f"Comparison chart saved as '{args.output}'.")


if __name__ == '__main__':
    main()