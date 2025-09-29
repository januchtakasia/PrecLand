# PrecLand

### Overview
This repository contains datasets and a script used in the study of landslide precursors. The resources include Sentinel-1 SAR data, Sentinel-2 multispectral data, and precipitation records. Additionally, it provides processed data, definitions of Areas of Interest (AOIs), and a script for the automated calculation of mean values within AOIs.

### Folder Structure:
•	Sentinel-1/ – .csv files with metadata and the names of Sentinel-1 scenes downloaded for both study sites,\
•	Sentinel-2/ – .csv files with the names of Sentinel-2 scenes downloaded for both study sites,\
•	Precipitation/ – .csv file with calculated annual precipitation sums,\
•	AOI/ – files defining AOIs,\
•	Script/ – contains a script for the automated calculation of mean values for each AOI,\
•	Results_samples/ – .csv files containing mean values calculated by the script for each AOI.

### Data Sources:
•	Sentinel-1 SAR data are publicly available at https://search.asf.alaska.edu/, \
•	Sentinel-2 multispectral data are publicly available at https://browser.dataspace.copernicus.eu, \
•	Precipitation data were obtained from Big Sur station (GHCN-D: USC00040790) and are publicly available at https://www.ncdc.noaa.gov/cdo-web/search.

### Notes on Processing
•	Remaining analyses and calculations were performed in QGIS.\
•	The authors also have a script for the automatic generation of raster layers with vegetation indices and their normalization. This script is available from the corresponding author upon reasonable request.
