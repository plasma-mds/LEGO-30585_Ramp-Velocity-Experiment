"""Plot average ramp descent velocity from ramp-descent-raw-data.csv."""

import csv
from collections import defaultdict
from pathlib import Path
from statistics import mean, stdev

import matplotlib.pyplot as plt


DATA_PATH = Path(__file__).with_name("ramp-descent-raw-data.csv")
OUTPUT_PATH = Path(__file__).with_suffix(".png")


def main() -> None:
    with DATA_PATH.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))

    grouped = defaultdict(list)
    for row in rows:
        distance = float(row["distance_from_release_cm"])
        if distance > 0:
            grouped[distance].append(float(row["time_s"]))

    distances = sorted(grouped)
    mean_times = [mean(grouped[distance]) for distance in distances]
    time_sd = [stdev(grouped[distance]) if len(grouped[distance]) > 1 else 0 for distance in distances]
    velocities = [(distance / 100) / elapsed for distance, elapsed in zip(distances, mean_times)]
    velocity_sd = [velocity * deviation / elapsed for velocity, deviation, elapsed in zip(velocities, time_sd, mean_times)]

    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11, "axes.spines.top": False, "axes.spines.right": False})
    figure, axis = plt.subplots(figsize=(7.2, 4.6), constrained_layout=True)
    axis.errorbar(distances, velocities, yerr=velocity_sd, fmt="o-", color="#8a3b12", capsize=5, capthick=1.3, lw=1.8, ms=6)
    axis.set(
        title="Average Vehicle Velocity During Ramp Descent (Synthetic Example)",
        xlabel="Distance from release marker (cm)",
        ylabel="Average velocity (m/s)",
    )
    axis.set_xticks(distances)
    axis.grid(axis="y", alpha=0.25)
    figure.savefig(OUTPUT_PATH, dpi=180, facecolor="white")


if __name__ == "__main__":
    main()
