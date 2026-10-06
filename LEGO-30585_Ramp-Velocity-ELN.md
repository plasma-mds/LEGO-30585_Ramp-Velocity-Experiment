# Electronic Lab Notebook: Ramp Descent Velocity Measurement

**Experiment ID:** `LEGO30585-RAMP-001`  
**Date:** 2026-10-05  
**Status:** Synthetic example dataset; values are illustrative and are not physical measurements.  
**Vehicle provenance:** [Vehicle building ELN](LEGO-30585_Building-Lab-Notebook.md)  
**Vehicle parts provenance:** [LEGO 30585 Parts Catalog](LEGO-30585_Parts-Catalog.md)

## Objective

Measure the descent time and average velocity of the completed LEGO 30585 vehicle on a 50 cm-long ramp with an 8 cm height. Marker positions are measured along the ramp from its bottom. The vehicle is released at the 40 cm marker. Three timing trials are acquired at the 30, 20, 10, and 0 cm markers, where 0 cm is the ramp end.

## Apparatus

- Completed LEGO 30585 vehicle, assembled as documented in the linked building ELN.
- Ramp with a 50 cm length and 8 cm vertical height.
- Ramp markers at 40, 30, 20, 10, and 0 cm measured upward from the bottom.
- Stopwatch with a recorded display resolution of 0.01 s.
- Ruler with estimated marker-position uncertainty of +/- 0.1 cm.

## Procedure

1. Place the vehicle on the ramp with its front wheels aligned to the 40 cm marker.
2. Release the vehicle without a push and simultaneously start the stopwatch. This release location defines `t = 0` and a travelled distance of 0 cm.
3. Stop and record the time as the vehicle front reaches the 30 cm marker, corresponding to 10 cm travelled from release.
4. Repeat the measurement three times at the 30 cm marker.
5. Repeat steps 2 to 4 for the 20, 10, and 0 cm markers, corresponding to 20, 30, and 40 cm travelled from release.
6. Store all observations in the raw CSV file. Calculate mean time, sample standard deviation, average velocity, and propagated timing uncertainty for every nonzero travelled distance.

## Measurement Conditions

The ramp length, height, marker positions, release position, timing convention, and trial count are specified by the procedure. Surface material, release mechanism beyond no applied push, ambient conditions, and stopwatch model should be recorded for a physical repeat.

## Raw Data

**Machine-readable file:** [ramp-descent-raw-data.csv](velocity-experiment/ramp-descent-raw-data.csv)

| Marker from bottom (cm) | Distance from release (cm) | Trial 1 (s) | Trial 2 (s) | Trial 3 (s) |
|---:|---:|---:|---:|---:|
| 40 | 0 | 0.00 | 0.00 | 0.00 |
| 30 | 10 | 0.41 | 0.43 | 0.42 |
| 20 | 20 | 0.59 | 0.61 | 0.60 |
| 10 | 30 | 0.74 | 0.76 | 0.75 |
| 0 | 40 | 0.86 | 0.88 | 0.87 |

## Data Reduction

For every nonzero travelled distance, the reported time uncertainty is the sample standard deviation of the three trial times. Average velocity and timing-only propagated uncertainty are calculated as:

`v_bar = distance_m / mean_time_s`

`sigma_v = v_bar * sigma_t / mean_time_s`

The 40 cm release marker has zero elapsed time and therefore no defined average velocity. Distance uncertainty is retained in the raw data but is not included in the plotted velocity error bars.

**Machine-readable file:** [ramp-descent-summary.csv](velocity-experiment/ramp-descent-summary.csv)

| Marker from bottom (cm) | Distance from release (cm) | Mean time (s) | Time SD (s) | Average velocity (m/s) | Velocity SD (m/s) |
|---:|---:|---:|---:|---:|---:|
| 40 | 0 | 0.000 | 0.000 | Not applicable | Not applicable |
| 30 | 10 | 0.420 | 0.010 | 0.23810 | 0.00567 |
| 20 | 20 | 0.600 | 0.010 | 0.33333 | 0.00556 |
| 10 | 30 | 0.750 | 0.010 | 0.40000 | 0.00533 |
| 0 | 40 | 0.870 | 0.010 | 0.45977 | 0.00528 |

## Results

### Travel Time With Error Bars

The points show individual trials. The connected series is the mean time at each distance from the release marker; vertical error bars represent one sample standard deviation (`n = 3`).

![Ramp descent time by distance from release](velocity-experiment/ramp-time-by-distance.png)




