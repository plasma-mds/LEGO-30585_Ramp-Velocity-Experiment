# Ramp-Roll Velocity of a LEGO 30585 Vehicle: A Synthetic Demonstration

**Experiment ID:** `LEGO30585-RAMP-001`  
**Data status:** Synthetic demonstration dataset  
**Supporting ELN:** [Ramp-velocity measurement ELN](LEGO-30585_ELN_Ramp-Velocity-Experiment.md)  
**Vehicle provenance:** [Vehicle building ELN](LEGO-30585_ELN_Building-Vehicle.md)

## Introduction

The motion of a wheeled vehicle released from an inclined ramp onto a flat track provides a compact example of repeatable distance-time measurement. Here, the completed LEGO 30585 vehicle was considered as the test object, following its recorded construction procedure. Travel times were recorded conceptually over four marked flat-track distances, and average velocity was calculated from the ratio of travelled distance to mean travel time.

This paper reports a **synthetic example dataset** prepared to demonstrate the research workflow, data reduction, uncertainty presentation, and data-publication practice. It does not report a physical measurement of the vehicle.

## Experimental Setup

The vehicle was released without an applied push from the upper end of a ramp with a 15 cm horizontal base width and a vertical height of 5 cm. It then rolled onto level ground. A manual stopwatch was started at release and stopped when the front of the vehicle reached a selected distance mark on the flat track. The 5, 10, 15, and 20 cm marks were measured from the ramp exit, not from the initial release point. Three trials were evaluated at each distance. The stopwatch display resolution was 0.01 s; the recorded distance uncertainty was +/- 0.1 cm.

![Graphite-style schematic of the ramp, vehicle, distance marks, and stopwatch](velocity-experiment/ramp-experiment-setup-hand-drawn.png)

*Figure 1. Hand-drawn schematic of the completed LEGO vehicle released from a ramp with a 15 cm horizontal base width and a 5 cm height. The vehicle rolls onto level ground; timing begins at release and ends when the vehicle front reaches the selected flat-track mark.*

For each distance, the mean travel time and its sample standard deviation were calculated from three trials. The average velocity was evaluated as

`v_bar = distance_m / mean_time_s`.

Timing uncertainty was propagated to velocity using

`sigma_v = v_bar * sigma_t / mean_time_s`.

The ramp base width and height are specified by the experimental design. Ramp surface material, flat-track surface material, and the detailed release mechanism are not specified and are consequently not inferred here.

## Results

Travel time increased with distance, from a mean of 0.260 s at 5 cm to 0.990 s at 20 cm. The associated standard deviation of the three timing trials was 0.010 s at every distance in the synthetic dataset.

![Travel time by distance with individual trials and one-standard-deviation error bars](velocity-experiment/ramp-time-by-distance.png)

*Figure 2. Individual synthetic timing trials and mean travel time. Error bars are one sample standard deviation (`n = 3`).*

The calculated average velocity ranged from 0.19231 to 0.20270 m/s. Within the timing-only propagated uncertainties, these values are consistent with an approximately constant average velocity of about 0.20 m/s over the measured interval.

![Average velocity by distance with propagated timing uncertainty](velocity-experiment/ramp-average-velocity.png)

*Figure 3. Average velocity as a function of measured distance. Error bars represent timing-only propagated standard deviation.*

| Distance (cm) | Mean time (s) | Time SD (s) | Average velocity (m/s) | Velocity SD (m/s) |
|---:|---:|---:|---:|---:|
| 5 | 0.260 | 0.010 | 0.19231 | 0.00740 |
| 10 | 0.500 | 0.010 | 0.20000 | 0.00400 |
| 15 | 0.740 | 0.010 | 0.20270 | 0.00274 |
| 20 | 0.990 | 0.010 | 0.20202 | 0.00204 |

## Conclusion

The synthetic measurements illustrate a reproducible ramp-roll analysis: repeated time observations were collected at increasing distances, summarized with standard deviations, and converted to average velocities with propagated timing uncertainty. The approximately constant velocity trend is consistent with the constructed example data. A physical repeat should additionally record ramp angle, surface composition, release method, and observer reaction-time effects before making claims about the vehicle dynamics.

## Data Availability

The raw trials, summary data, plots, and full experimental protocol are available in the accompanying ELN record:

- [Ramp-velocity measurement ELN](LEGO-30585_ELN_Ramp-Velocity-Experiment.md)
- [Raw CSV data](velocity-experiment/ramp-velocity-raw-data.csv)
- [Summary CSV data](velocity-experiment/ramp-velocity-summary.csv)

The dataset and ELN are intended for publication in Zenodo. The Zenodo DOI is **pending assignment** and must be inserted here only after the deposition has been published; no DOI is fabricated for this local working copy. The planned deposition should include this paper, both ELNs, the raw and summary CSV files, the PNG figures, descriptive metadata, and the synthetic-data designation.
