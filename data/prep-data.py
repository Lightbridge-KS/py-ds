import pandas as pd
from pyhere import here

titanic = pd.read_csv("https://raw.githubusercontent.com/pandas-dev/pandas/main/doc/data/titanic.csv")
titanic.to_csv(here("data/titanic/titanic.csv"))