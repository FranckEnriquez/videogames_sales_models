# import external libraries
from kaggle.api.kaggle_api_extended import KaggleApi

# constants
PATH = '../datasets/'
KAGGLE_PATH = 'gregorut/videogamesales'
FILE_NAME = 'vgsales.csv'

# keys authetication
api = KaggleApi()
api.authenticate()

# download singular file
[api.dataset_download_file(
	dataset=KAGGLE_PATH, file_name=FILE_NAME, path=PATH)]

print("File is downloaded")
