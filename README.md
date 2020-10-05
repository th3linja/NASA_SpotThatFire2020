# NASA_SpotThatFire2020
Parcipitating in the NASA Space Apps challenge (October 3-4) Spot That Fire v3.0.

## Getting Started
The purpose of this project was to use Python to train a RandomForestRegressor model with data from `FireData.csv.`Currently the data collected in the model is small and limited so the predictions are not necessarily accurate. After training the model, the model is then used to estimate the cost of wildfires based on given parameters from an interactive web application. 

## Prequisites
  * Python
  * sklearn
  * joblib
  * numpy
  * pandas
  * json
  * flask
  
## Installing
Head over to [Python.org](https://www.python.org/) to download the latest version of Python if you haven't already. Make sure to enable pip in  `Optional Features` when installing. After installing, head over to Advanced System Settings -> Environment Variables and add Python into PATH. Open the command prompt (cmd) and run the command `pip3 install youtube-dl`.

Install all necessary modular components using `pip install <module>`

Download this project folder, which will contain both `current.joblib` and `simulation.joblib` saved training models, `FireData.csv`, `Calculations.py`, and `api.py`. 

## Running Tests
 * Make sure all modules are up to date using `pip install` or through your local IDE.

## Built With
  * Python
  * sklearn
  * joblib
  * numpy
  * pandas
  * json
  * flask
  
## Authors
th3linja

## Acknowledgments
Please visit https://github.com/yavuzalp/wild-fire-cost-calculator/ for the Front-End development of this project.
