import pandas as pd
import matplotlib.pyplot as plt

goalscorers= pd.read_csv("goalscorers.csv")
results= pd.read_csv("results.csv")
shootouts= pd.read_csv("shootouts.csv")





grouped_df = results_copy.groupby(['home team', 'away team','tournament'])
