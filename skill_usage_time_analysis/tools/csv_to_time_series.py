import numpy as np
import pandas as pd

def time_series_descrete(csv_file, column_name):
    df = pd.read_csv(csv_file)
    positions = df.index.values
    values = df[column_name].values
    return positions, values

def time_series_continuous(csv_file, column_name):
    from tools.weighted_kde import weighted_kde
    df = pd.read_csv(csv_file)
    positions = df.index.values
    range = np.linspace(min(positions), max(positions), 1000)
    values = df[column_name].values
    density = weighted_kde(positions, range, values)
    return range, density