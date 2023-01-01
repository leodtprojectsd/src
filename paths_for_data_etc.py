# file with all python paths --> this should become the standard python way of doing this 
import os 
from pathlib import Path
import sys


ROOT_DIR = Path(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(str(ROOT_DIR))


 # RAW DATA paths
RAW_DATA_DIR = ROOT_DIR.joinpath(r"data\raw_data").resolve()
sys.path.append(str(RAW_DATA_DIR))
#age
age_raw_data = "raw_age_data.csv"
age_raw_data_path = RAW_DATA_DIR.joinpath(age_raw_data).resolve()
#height 
height_raw_data = "raw_height_data.csv"
height_raw_data_path = RAW_DATA_DIR.joinpath(height_raw_data).resolve()

 #CLEAN DATA paths
CLEAN_DATA_DIR = ROOT_DIR.joinpath(r"data\cleaned_data").resolve()
sys.path.append(str(CLEAN_DATA_DIR))
#age
age_clean_data = "clean_age_data.csv"
age_clean_data_path = CLEAN_DATA_DIR.joinpath(age_clean_data).resolve()
#height 
height_clean_data = "clean_height_data.csv"
height_clean_data_path = CLEAN_DATA_DIR.joinpath(height_clean_data).resolve()
