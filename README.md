# PrecLand

### Overview
This repository contains datasets and scripts used in the study of landslide precursors, including Sentinel-1 SAR, Sentinel-2 multispectral data, and precipitation data. It also includes processed data, Areas of Interest (AOI) definitions, and scripts for automatic calculation of mean values in AOI.

### Folder Structure:
•	Sentinel-1/ – .csv files with metadata and the names of specific Sentinel-1 scenes downloaded for both study sites,\
•	Sentinel-2/ – .csv files with the names of specific Sentinel-2 scenes downloaded for both study sites,\
•	Precipitation/ – .csv file with calculated annual precipitation sums,\
•	AOI/ – files defining AOI,\
•	Script/ – contains a script for automatic calculation of mean values for each AOI,\
•	Results_samples/ – example outputs for the datasets in .csv format.

### Data Sources:
•	Sentinel-1 SAR data are publicly available at: https://search.asf.alaska.edu/, \
•	Sentinel-2 multispectral data are publicly available at: https://browser.dataspace.copernicus.eu, \
•	Rainfall data were obtained from Big Sur station (GHCN-D: USC00040790) and are publicly available at https://www.ncdc.noaa.gov/cdo-web/search.

### Notes on Processing
•	Remaining analyses and calculations were performed in QGIS.
•	The authors also have scripts for automatic creation of raster layers with vegetation indices and their normalization; these scripts are available from the corresponding author upon reasonable request.
