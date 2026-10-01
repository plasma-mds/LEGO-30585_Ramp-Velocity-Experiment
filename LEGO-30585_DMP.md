# Data Management Plan: Ramp-to-Flat-Track Vehicle Experiment

**Project identifier:** `LEGO30585-RAMP-001`  
**Status:** Pre-experiment plan  
**Structure:** DFG proposal Section 2.4, following the [Plasma-MDS guidance](https://www.plasma-mds.org/tools.html#data-management-plan)

This plan is prepared before experimental work begins. It will be reviewed before the first measurement and updated if the setup, software, data flow, or responsibilities change.

## 1. Data Description

The project will generate manual stopwatch measurements of the completed LEGO 30585 vehicle rolling from a ramp onto a flat track. The planned raw data comprise three time measurements at each flat-track distance of 5, 10, 15, and 20 cm. The ramp geometry is a 15 cm horizontal base width and 5 cm vertical height.

Raw and processed tabular data will be stored as UTF-8 CSV files. The ELN will be Markdown, and setup and result figures will be PNG. Times will be recorded in seconds, distances in centimetres with a documented conversion to SI units, and calculated velocity in m/s. The expected volume is below 10 MB, including documentation and figures. No external scientific dataset will be reused; the original LEGO instructions are third-party provenance material and are not research data for publication.

## 2. Documentation And Data Quality

Each run will receive an unambiguous identifier and be documented in the ELN. The ELN will record the vehicle configuration, ramp dimensions, flat-track surface, stopwatch, operator, release method, acquisition date, measured values, deviations, and uncertainty assumptions. Raw CSV data will retain all trials; repeated or invalid trials will be marked rather than deleted.

The project will use descriptive column names with units, ISO 8601 dates, and a short data dictionary. Mean time, sample standard deviation, average velocity, and uncertainty propagation will be calculated by version-controlled analysis code. Raw data, processed data, code, figures, and the final paper will be linked through the run identifier. These measures support FAIR findability, interoperability, and reproducibility.

## 3. Storage And Technical Archiving During The Project

Active data will be kept in a structured project directory that separates raw measurements, processed CSV files, analysis code, figures, and ELN records. The working directory will be backed up after every measurement session to separate access-controlled storage. Raw measurement files will not be overwritten by processed files.

Access during the project will be limited to the project members. Before release, a final read-only copy and checksums will be created. The small expected data volume requires no special high-volume transfer or storage infrastructure.

## 4. Legal Obligations And Conditions

The experiment does not involve personal data, human participants, confidential partner data, export-controlled information, or anticipated patent claims. The LEGO name, instruction PDF, logos, and product imagery are third-party material. They will remain local provenance material and will not be included in the open data package unless use and redistribution rights have been confirmed.

Only original measurements, original analysis code, original setup schematics, and project documentation will be released. The intended licence for these original materials is CC BY 4.0, subject to institutional requirements.

## 5. Data Exchange And Long-Term Data Accessibility

The publishable package will include raw and processed CSV data, the ELN, data dictionary, analysis code, setup figure, result figures, and this plan. It will be deposited in Zenodo after quality review with descriptive metadata, a versioned DOI, and the selected licence. Metadata will identify the project, files, units, uncertainty treatment, and relationship between the raw data, analysis, figures, and paper.

The deposited version will be separate from active working storage. It will be retained for at least ten years in line with DFG good-research-practice expectations. If a file cannot be published because of third-party rights, the metadata will state the restriction and the reason.

## 6. Responsibilities And Resources

The experimenter is responsible for data acquisition, ELN entries, and the first data-quality check. The project lead is responsible for approval of the data package, licence, and long-term deposit. The analysis maintainer is responsible for preserving the processing code and regenerating the processed data and figures from the raw CSV files.

The project reserves time for ELN completion, backup, metadata creation, quality review, and Zenodo deposition. The expected data volume is small; ordinary institutional storage and the Zenodo service are sufficient. All project members handling data will use this plan and the agreed file naming, documentation, and backup procedures.
