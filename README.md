# Salary Predictor

To get started fork this repo

Create a local installation of MindsDB following this [guide](https://docs.mindsdb.com/contribute/install#installing-mindsdb)

After download this [dataset](https://www.kaggle.com/datasets/rsadiq/salary)

Import it onto your installation

Run this command to create the Predictor Model
`
CREATE PREDICTOR mindsdb.SalaryPredictor
FROM files
(SELECT * FROM SalaryData)              
PREDICT Salary
`

Run the app with `python main.py` and get predicting!
