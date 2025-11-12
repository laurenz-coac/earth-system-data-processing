# Earth System Data Processing

Collection of notebooks and information on various aspects of Earth system data processing.

This repository contains material that has been provided for and developed during the lecture on
*Earth System Data Processing* at the University of Cologne in the winter semester 2025/26. The lecture
covered topics such as finding and accessing data from modern web services, coordinate systems,
remapping and interpolation, common file formats, types of Earth system data, numerical model grids,
metadata standards, FAIR data.

The course uses an inverse classroom concept, where the actual lectures are recorded, while students
discuss the lecture content and work on practical examples during the course hours. The material 
in this repository forms the basis for the practical exercises. Students will also be assigned 
coding tasks as homework and the results shall be included here to establish a collection of useful routines 
for other students and scientists who wish to learn the basics of Earth system data processing.

*Note:* Due to the background of the lecturer, the focus of this material is on atmospheric data.
Nevertheless, many concepts and routines can also be applied to other Earth system data. Feel free to contribute
material for other data types if you find this repository useful.

*Author:* Martin Schultz, Jülich Supercomputing Centre, Forschungszentrum Jülich & Department of Computer Science and Math, University of Cologne
October 2025
# Earth System Data Processing

This project explores ECMWF **AIFS** (Artificial Intelligence Forecasting System) data using [Earthkit](https://earthkit.readthedocs.io/en/latest/).

## Setup

1. Create a Conda environment:
   ```bash
   conda create -n aifs python=3.11
   conda activate aifs
   conda install -c conda-forge earthkit-data earthkit-plots ecmwf-opendata cfgrib xarray matplotlib cartopy
# AIFS Single: Surface Download + Quicklook

This notebook/script downloads ECMWF **AIFS Single** surface fields from **ECMWF Open Data** and plots a global quicklook.

## What it does
- Fetches `2t`, `10u`, `10v`, `msl` at steps `[6, 12, 24]` for a given run (`date`, `time`)
- Saves GRIB2 files under `data/`
- Optionally opens with `xarray+cfgrib` and plots with Cartopy

## Requirements
- Conda (recommended on Windows)
- See `environment.yml` for all packages (PROJ/GEOS handled by conda-forge)
- ECMWF Open Data retention is short (≈ a few days). Use recent runs only.

## Setup
```bash
conda env create -f environment.yml
conda activate aifs
