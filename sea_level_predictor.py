import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']
    # Create scatter plot
    plt.scatter(x, y)
    
    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(x, y)
    line_x = np.arange(x.min(), 2051)
    line_y = slope*line_x + intercept
    plt.plot(line_x,line_y,color="red")
  
    # Create second line of best fit
    new_df = df[df['Year'] >= 2000]
    new_x = new_df['Year']
    new_y = new_df['CSIRO Adjusted Sea Level']
    slope, intercept, r_value, p_value, std_err = linregress(new_x, new_y)
    line_new_x = np.arange(2000, 2051)
    line_new_y = slope*line_new_x + intercept           
    plt.plot(line_new_x,line_new_y,color="blue")
  
    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
