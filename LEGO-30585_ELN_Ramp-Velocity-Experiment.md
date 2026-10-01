# Electronic Lab Notebook: Ramp Velocity Measurement

**Experiment ID:** `LEGO30585-RAMP-001`  
**Date:** 2026-09-30  
**Status:** Synthetic example dataset; values are illustrative and are not physical measurements.  
**Vehicle provenance:** [Vehicle building ELN](LEGO-30585_ELN_Building-Vehicle.md)  

## Objective

Measure the mean velocity of the completed LEGO 30585 vehicle while it rolls down a ramp over travel distances of 5, 10, 15, and 20 cm. For each distance, acquire three time measurements and calculate average velocity from the mean travel time.

## Apparatus

- Completed LEGO 30585 vehicle, assembled as documented in the linked building ELN.
- Ramp with a marked release line and distance marks at 5, 10, 15, and 20 cm.
- Stopwatch with a recorded display resolution of 0.01 s.
- Flat run-out surface and a ruler with estimated distance uncertainty of +/- 0.1 cm.

## Procedure

1. Place the completed vehicle at the ramp release line with the wheels aligned to the ramp direction.
2. Select the first finish mark at 5 cm.
3. Release the vehicle and simultaneously start the stopwatch.
4. Stop the stopwatch as the front of the vehicle reaches the selected finish mark, then record the time.
5. Repeat the measurement three times at 5 cm.
6. Repeat steps 2 to 5 for 10, 15, and 20 cm.
7. Store each unrounded run in the raw CSV file. Calculate the mean time and sample standard deviation for each distance.
8. Calculate average velocity as `v_bar = distance_m / mean_time_s`.

## Measurement Conditions

The source procedure specifies the ramp and distances but not the ramp angle, surface material, ambient conditions, or release mechanism. These fields are therefore explicitly unreported rather than inferred. For a physical repeat, record them before acquisition.

## Raw Data

**Machine-readable file:** [ramp-velocity-raw-data.csv](velocity-experiment/ramp-velocity-raw-data.csv)

| Distance (cm) | Trial 1 (s) | Trial 2 (s) | Trial 3 (s) |
|---:|---:|---:|---:|
| 5 | 0.26 | 0.25 | 0.27 |
| 10 | 0.49 | 0.51 | 0.50 |
| 15 | 0.73 | 0.75 | 0.74 |
| 20 | 0.98 | 1.00 | 0.99 |

## Data Reduction

For every distance, the reported time uncertainty is the sample standard deviation of the three trial times. Velocity uncertainty is propagated from timing uncertainty only:

`sigma_v = v_bar * sigma_t / mean_time_s`

Distance uncertainty is retained in the raw dataset but is not included in the plotted velocity error bars. This keeps the example calculation traceable and makes its limitation explicit.

**Machine-readable file:** [ramp-velocity-summary.csv](velocity-experiment/ramp-velocity-summary.csv)

| Distance (cm) | Mean time (s) | Time SD (s) | Average velocity (m/s) | Velocity SD (m/s) |
|---:|---:|---:|---:|---:|
| 5 | 0.260 | 0.010 | 0.19231 | 0.00740 |
| 10 | 0.500 | 0.010 | 0.20000 | 0.00400 |
| 15 | 0.740 | 0.010 | 0.20270 | 0.00274 |
| 20 | 0.990 | 0.010 | 0.20202 | 0.00204 |

## Results

### Travel Time With Error Bars

The points show individual trials. The connected series is the mean time at each distance; vertical error bars represent one sample standard deviation (`n = 3`).

![Travel time by distance with standard-deviation error bars](velocity-experiment/ramp-time-by-distance.png)

### Average Velocity Over Distance

Average velocity remains close to 0.20 m/s across the tested distances. Vertical error bars represent timing-only propagated standard deviation.

![Average velocity by distance with propagated uncertainty](velocity-experiment/ramp-average-velocity.png)

## Interpretation

For this synthetic example, travel time increases approximately linearly with distance, while the calculated average velocity is nearly constant. A real experiment may differ because of release variability, friction, wheel slip, ramp alignment, and manual stopwatch reaction time. No claim about the actual physical velocity of the built vehicle is made from these synthetic values.

## FAIR Data Record

| FAIR principle | Implementation in this record |
|---|---|
| Findable | The experiment has the unique identifier `LEGO30585-RAMP-001`; filenames are descriptive and the vehicle build is linked. |
| Accessible | The ELN, raw CSV, summary CSV, and PNG figures are stored together in the project under `lego/`. |
| Interoperable | Data are UTF-8 CSV with machine-readable headers, explicit units in column names, ISO 8601 dates, and SI velocity values. |
| Reusable | The raw observations, uncertainty fields, calculation expression, trial count, data provenance, and synthetic-data status are recorded. |

## File Manifest

- `velocity-experiment/ramp-velocity-raw-data.csv`: 12 trial-level observations, including distance, time, instrument resolution, and calculated per-trial velocity.
- `velocity-experiment/ramp-velocity-summary.csv`: means, sample standard deviations, and timing-only propagated velocity uncertainty.
- `velocity-experiment/ramp-time-by-distance.png`: time plot with individual trials and mean +/- 1 SD.
- `velocity-experiment/ramp-average-velocity.png`: average-velocity plot with propagated timing uncertainty.
