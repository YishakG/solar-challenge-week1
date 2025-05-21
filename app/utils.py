import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def load_data(countries):
    dfs = []
    for country in countries:
        df = pd.read_csv(f"data/{country.lower()}_clean.csv")
        df['Country'] = country
        dfs.append(df)
    return pd.concat(dfs, ignore_index=True)

def plot_boxplot(df, metric, countries):
    plt.figure(figsize=(8, 5))
    sns.boxplot(x='Country', y=metric, data=df[df['Country'].isin(countries)])
    plt.title(f'{metric} by Country')
    return plt

def get_top_regions(df, metric):
    return df.groupby('Country')[metric].mean().sort_values(ascending=False).reset_index()