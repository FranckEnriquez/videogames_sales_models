# videogames_sales_models challenge

The objective of this challenge is to assess you ability to:

- perform basic data manipulation and data pre-processing
- demonstrate awareness of the computations involved
- train and tune ML models
- asses performance of the ML models
- obtaining clear, useful, and business driven insights from data and models

## Repository structure
```URL: https://github.com/FranckEnriquez/movies_rating_model
<rootDir>

└── ml
    └── analysis
        ├── predictions
        │   ├── df_predictions_linearreg_hyper_tuning.csv
        │   └── df_predictions_linearreg_standard.csv
        │   └── df_predictions_randomforest_hyper_tuning.csv
        │   └── df_predictions_randomforest_standard.csv     
        └── analysis.ipynb
    └── data
        ├── kaggleAPI
        │    ├── kaggleAPI.py
        ├── datasets
        │    ├── Base_de_datos.py
        │    ├── vgsales.csv
  └── models
        ├── linear-reg
        │   ├── hyper_tuning.ipynb
        │   └── standard.ipynb 
        ├── random-forest
        │   ├── hyper_tuning.ipynb
        │   └── standard.ipynb 
        ├── neural-network
        │   └── standard.ipynb 
        ├── ARIMA
        │   └── standard.ipynb 
   └── preprocess
        ├── utils
        │   ├── exploratory_analysis.py
        │   └── preprocess.py 
        │   └── visualizations.py 
        └── EDA.ipynb
 └── .gitattributes
 └── .gitignore
 └── Pipfile
 └── Pipfile.lock
 └── README.md
```

## Initial Setup

Clone this repository and install the virtual environment of this repository.

You can create a install via  commandline.
* Using the terminal: `pipenv install`

If you don't have pipenv install yet, follow the next steps there:
https://pipenv-es.readthedocs.io/es/latest/

Activate the Pipfile:
* Windows / MacOS / Unix: `pipenv shell`

Once you activate the pipenv, there's a kaggleAPI that 
acquire the data from its web site, to use the funcion,
you need to install **unzip**:

* Linux: https://linuxize.com/post/how-to-unzip-files-in-linux/


## Contact Info

Please feel free to ask me any outstanding question or concern:

* Phone: 3331856793
* Email: franckenriquezz@gmail.mx
