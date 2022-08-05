import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from datetime import datetime
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv')
df = df.set_index('date')

# Clean data
df = df[(df['value'] > df['value'].quantile(0.025)) & (df['value'] < df['value'].quantile(0.975))]

date_list = df.index.tolist()
date_format = pd.to_datetime(date_list).date
month_format = pd.to_datetime(date_list).month
year_format = pd.to_datetime(date_list).year
value_list = df['value'].tolist()

def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(16, 8))
    ax = plt.plot_date(date_format, value_list, 'r', xdate=True, ydate=False)
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Value')

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar['month'] = month_format
    df_bar['year'] = year_format
    df_bar_mean_list = df_bar.groupby([df_bar['year'], df_bar['month']]).mean().unstack(fill_value=0)

    # Draw bar plot
    ax = df_bar_mean_list.plot.bar(figsize=(16,8))
    ax.set_xlabel("Years")
    ax.set_ylabel("Average Page Views")

    months_name = ["January","February","March","April","May","June","July",
            "August","September","October","November","December"]
    ax.legend(labels = months_name, title="Months")

    fig = ax.get_figure()

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [pd.to_datetime(d).year for d in df_box.date]
    df_box['month'] = [pd.to_datetime(d).strftime('%b') for d in df_box.date]

    sum_year = df_box.groupby([df_box['year']]).sum()
  
    sum_month = df_box.groupby([df_box['month']])['value'].sum()
    # Draw box plots (using Seaborn)

    # print(sum_year.index)
    # ax = sns.boxplot(x=sum_year.index, y=sum_year['value'],              data=sum_year)
    # fig = ax.get_figure()

    df_box["Page Views"] = df_box["value"]
    df_box["Month"] = df_box["month"]
    df_box["Year"] = df_box["year"]
    g = sns.PairGrid(df_box, y_vars=["Page Views"], x_vars=["Year", "Month"], palette="hls")

    fig = g.fig
    fig.set_figheight(6)
    fig.set_figwidth(16)
    fig.axes[0].set_ylabel('Page Views')
    fig.axes[1].set_ylabel('Page Views')
    fig.axes[0].set_title('Year-wise Box Plot (Trend)')
    fig.axes[1].set_title('Month-wise Box Plot (Seasonality)')
    plt.tight_layout()

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
