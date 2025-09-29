"""
Calculate mean raster indices on the landslide (inside) and on the surrounding area (outside).
Author: Katarzyna Januchta
Description:
This script reads raster TIFF files from a folder, calculates mean values of
each raster inside and outside landslide polygons, and saves the results to a CSV file.
"""

import geopandas as gpd
import rasterio
from rasterio.features import geometry_mask
import pandas as pd
import os
import re
from datetime import datetime
from collections import defaultdict
import numpy as np

# ----------------- USER CONFIGURATION ----------------- #

RASTER_FOLDER = r'The path to the folder with raster files'
POLYGONS = {
    'in': r'The path to the shapefile for the landslide area',
    'out': r'The path to the shapefile for the surrounding area'
}
OUTPUT_EXCEL = r'The path for the output CSV file'

# Regex pattern to extract index name and date from raster filename
FILENAME_PATTERN = re.compile(r'([A-Z]+)_(\d{8})', re.IGNORECASE)

# ----------------- LOAD POLYGONS ----------------- #
shapes = {key: gpd.read_file(path) for key, path in POLYGONS.items()}

# ----------------- LIST RASTER FILES ----------------- #
raster_files = [f for f in os.listdir(RASTER_FOLDER) if f.lower().endswith('.tif')]

# ----------------- PROCESS RASTERS ----------------- #
results = defaultdict(dict)

for raster_file in raster_files:
    match = FILENAME_PATTERN.search(raster_file)
    if not match:
        print(f"File skipped (pattern not matched): {raster_file}")
        continue

    index_name = match.group(1).upper()
    date_str = match.group(2)
    raster_date = datetime.strptime(date_str, '%Y%m%d').date()
    raster_path = os.path.join(RASTER_FOLDER, raster_file)

    with rasterio.open(raster_path) as src:
        raster_data = src.read(1).astype(float)
        nodata_val = src.nodata

        if nodata_val is not None:
            raster_data[raster_data == nodata_val] = np.nan

        for key, shape in shapes.items():
            shape_proj = shape.to_crs(src.crs)
            geometries = [geom for geom in shape_proj.geometry]

            mask = geometry_mask(geometries, transform=src.transform, invert=True, out_shape=src.shape)
            values = raster_data[mask]

            if values.size == 0:
                mean_val = np.nan
                print(f"No pixels found for {index_name}_{key} on {raster_date}")
            else:
                mean_val = float(np.nanmean(values))

            column_name = f"{index_name}_{key}"
            results[raster_date][column_name] = mean_val

# ----------------- CREATE DATAFRAME AND SAVE ----------------- #
df = pd.DataFrame.from_dict(results, orient='index')
df.index.name = 'Date'
df = df.sort_index()
df.reset_index(inplace=True)

# Ensure output folder exists
os.makedirs(os.path.dirname(OUTPUT_EXCEL), exist_ok=True)

df.to_excel(OUTPUT_EXCEL, index=False)
print(f"Results saved to: {OUTPUT_EXCEL}")