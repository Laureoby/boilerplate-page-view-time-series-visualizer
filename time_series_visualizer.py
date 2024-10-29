import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')

# Clean data
lower_bound = df['page_views'].quantile(0.025)
upper_bound = df['page_views'].quantile(0.975)
df = df[(df['page_views'] >= lower_bound) & (df['page_views'] <= upper_bound)]


def draw_line_plot():
    # Draw line plot
    df.set_index('date', inplace=True)

    plt.figure(figsize=(10, 5))
    plt.plot(df.index, df['page_views'], marker='o', linestyle='-', color='r')
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views')

    plt.grid()
    plt.show()

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month_name()
    df_bar = df_bar.groupby(['year', 'month'])['value'].mean().unstack()

    # Draw bar plot
    fig, ax = plt.subplots(figsize=(10, 6))
    df_bar.plot(kind='bar', ax=ax)

    # Paramètres du graphique
    ax.set_xlabel("Years")
    ax.set_ylabel("Average Page Views")
    ax.set_title("Monthly Average Page Views per Year")
    ax.legend(title="Months", bbox_to_anchor=(1.0, 1.0))
    plt.tight_layout()
    plt.show()

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    # We ordered month
    months_order = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    df_box['month'] = pd.Categorical(df_box['month'], categories=months_order, ordered=True)

    # Create a figure with two Box Plot
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
    
    # Box plot per year
    sns.boxplot(x="year", y="value", data=df_box, ax=ax1)
    ax1.set_title("Year-wise Box Plot (Trend)")
    ax1.set_xlabel("Year")
    ax1.set_ylabel("Page Views")
    
    # Box plot per month
    sns.boxplot(x="month", y="value", data=df_box, ax=ax2)
    ax2.set_title("Month-wise Box Plot (Seasonality)")
    ax2.set_xlabel("Month")
    ax2.set_ylabel("Page Views")

    plt.tight_layout()
    plt.show()
    
    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
