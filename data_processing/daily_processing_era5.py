# import cdsapi
import os
import datetime
import argparse

import numpy as np
import healpy as hp
import xarray as xr

def process_data(save_path: str, start_date: str = "1940-01-01", end_date: str = None, date: str = None,
                level_list: list = [975, 900, 800, 500, 300],
                param_list: list = ["133.128"],  # specific humidity
                    ):

    if not os.path.exists(save_path):
        os.makedirs(save_path)
    
    already_processed_dates = [f.replace(".nc", "") for f in os.listdir(save_path)]
    
    if date is not None:
        dates_to_process = [date] if date not in already_processed_dates else []
    else:
        if end_date is None:
            end_date = datetime.datetime.now().strftime("%Y-%m-%d")
        start_dt = datetime.datetime.strptime(start_date, "%Y-%m-%d")
        end_dt = datetime.datetime.strptime(end_date, "%Y-%m-%d")
        delta = end_dt - start_dt
        dates_to_process = [(start_dt + datetime.timedelta(days=i)).strftime("%Y-%m-%d") for i in range(delta.days + 1)
                            if (start_dt + datetime.timedelta(days=i)).strftime("%Y-%m-%d") not in already_processed_dates]

    # c = cdsapi.Client()

    print(dates_to_process)

    for d in dates_to_process:

        # c.retrieve("reanalysis-era5-complete", {
        # "class": "ea",
        # "type": "an",  # analysis data
        # "stream": "oper",
        # "expver": "1",
        # "levtype": "pl",
        # "date": d,  # date in YYYY-MM-DD
        # "time": "00:00:00/06:00:00/12:00:00/18:00:00",  # 6-hourly
        # "levelist": "/".join([str(lv) for lv in level_list]),
        # "param": "/".join(param_list),
        # "grid": "5.625/5.625",
        # "format": "netcdf"
        # }, f"{d}.nc")

        ## transform to healpix

        ## save as zarr

        ## remove temp file

        with open(os.path.join(save_path, f"{d}.nc"), "w") as f:
            f.write("Simulated data content")

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('--save_path', dest='save_path', type=str, help='Path to save data', required=True)
    parser.add_argument('--start_date', dest='start_date', type=str, help='Add start date', default="1940-01-01")
    parser.add_argument('--end_date', dest='end_date', type=str, help='Add end date', default=None)
    parser.add_argument('--date', dest='date', type=str, help='Add specific date', default=None)
    args = parser.parse_args()

    process_data(save_path=args.save_path,
                 start_date=args.start_date,
                 end_date=args.end_date,
                 date=args.date)