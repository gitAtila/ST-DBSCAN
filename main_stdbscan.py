import pandas as pd
from sys import argv
import STDBSCAN

csv_path = argv[1]

# df_table must have the columns: 'latitude', 'longitude' and 'date_time'
df_table = pd.read_csv(csv_path)
print df_table

spatial_threshold = 100 # meters
temporal_threshold = 1  # minutes
min_neighbors = 2
df_clustering = STDBSCAN.ST_DBSCAN(df_table, spatial_threshold, temporal_threshold, min_neighbors)
print df_clustering