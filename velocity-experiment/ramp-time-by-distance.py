"""Plot ramp descent times from ramp-descent-raw-data.csv."""

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
        grouped[float(row["distance_from_release_cm"])].append(float(row["time_s"]))

    distances = sorted(grouped)
    mean_times = [mean(grouped[distance]) for distance in distances]
    time_sd = [stdev(grouped[distance]) if len(grouped[distance]) > 1 else 0 for distance in distances]

    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11, "axes.spines.top": False, "axes.spines.right": False})
    figure, axis = plt.subplots(figsize=(7.2, 4.6), constrained_layout=True)
    offsets = (-0.35, 0, 0.35)
    for distance in distances:
        axis.scatter(
            [distance + offset for offset in offsets],
            grouped[distance],
            color="#6b7280",
            s=34,
            zorder=2,
            label="Individual trial" if distance == distances[0] else None,
        )
    axis.errorbar(
        distances,
        mean_times,
        yerr=time_sd,
        fmt="o-",
        color="#0f4c5c",
        capsize=5,
        capthick=1.3,
        lw=1.8,
        ms=6,
        label="Mean +/- 1 SD",
        zorder=3,
    )
    axis.set(
        title="Ramp Descent Time by Distance from Release (Synthetic Example)",
        xlabel="Distance from release marker (cm)",
        ylabel="Time (s)",
    )
    axis.set_xticks(distances)
    axis.grid(axis="y", alpha=0.25)
    axis.legend(frameon=False, loc="upper left")
    figure.savefig(OUTPUT_PATH, dpi=180, facecolor="white")


if __name__ == "__main__":
    main()
