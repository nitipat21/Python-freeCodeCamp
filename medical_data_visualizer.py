import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv("medical_examination.csv")

# Add 'overweight' column
overweight_list = []
height_list = df['height'].tolist()
weight_list = df['weight'].tolist()

for i in range(len(height_list)):
  BMI = weight_list[i] / pow(height_list[i] / 100, 2)
  if BMI > 25:
    overweight_list.append(1)
  else:
    overweight_list.append(0)

df['overweight'] = overweight_list

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.

# Normalize cholesterol
cholesterol_list = df["cholesterol"].tolist()
new_cholesterol_list = []
for data in cholesterol_list:
  if data == 1:
      new_cholesterol_list.append(0)
  elif data > 1:
      new_cholesterol_list.append(1)
df["cholesterol"] = new_cholesterol_list

# Normalize gluc
gluc_list = df["gluc"].tolist()
new_gluc_list = []
for data in gluc_list:
  if data == 1:
      new_gluc_list.append(0)
  elif data > 1:
      new_gluc_list.append(1)
df["gluc"] = new_gluc_list

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    values = ['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight']
    
    df_cat = pd.melt(df, id_vars = ["cardio"], value_vars = values)

    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
  
    df_cat = df_cat.groupby(['variable', 'value','cardio'])['cardio'].count().reset_index(name="total")
    print(df_cat)
    
    # Draw the catplot with 'sns.catplot()'
    # Get the figure for the output
    fig = sns.catplot(x="variable", y="total", hue="value",kind="bar", col="cardio", data=df_cat)


    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = df[(df['ap_lo'] <= df['ap_hi']) & (df['height'] >= df['height'].quantile(0.025)) & (df['height'] <= df['height'].quantile(0.975)) & (df['weight'] >= df['weight'].quantile(0.025)) & (df['weight'] <= df['weight'].quantile(0.975))]
  
    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.zeros_like(corr)
    mask[np.triu_indices_from(mask)] = True
    



    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(7, 5))
    
  
    # Draw the heatmap with 'sns.heatmap()'
    ax = sns.heatmap(corr, mask=mask, square=True)


    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
