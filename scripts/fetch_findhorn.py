from pvlib.iotools import get_pvgis_tmy
import pandas as pd
lat=57.65
lon=-3.61
print('Fetching PVGIS TMY for', lat, lon)
tmy, meta = get_pvgis_tmy(latitude=lat, longitude=lon)
fn = 'inputs/Findhorn_pvgis_tmy.csv'
tmy.to_csv(fn)
print('Saved', fn)
print('Columns:', list(tmy.columns))
print('Rows:', len(tmy))
