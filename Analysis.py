import pandas as pd
import numpy as np
import scipy.stats
import matplotlib.pyplot as plt
import seaborn as sns
import plotnine as p9
from plotnine import *

df = pd.read_csv("EPL_20_21.csv")

# Show basic info
print(df.info())  # Check column names, data types, and missing values
print(df.describe())  # Summary statistics for numerical columns

# goals pr 90 (Most often scores by time played)
df['Goals_per_Minute'] = df['Mins'] / df['Goals']
efficient_scorers = df[['Name', 'Goals', 'Mins', 'Goals_per_Minute']].sort_values(by='Goals_per_Minute', ascending=True).head(10)

plt.figure(figsize=(12,6))
sns.barplot(x=efficient_scorers['Name'], y=efficient_scorers['Goals_per_Minute'], palette='coolwarm_r')
plt.xticks(rotation=45)
plt.title('Who you need for often goals')
plt.ylabel('Minutes per Goal')
plt.xlabel('Name')
plt.show()

# Most inefficient scorers (Lowest goal pr xG across the whole season)
forwards = df[df['Position'].isin(['FW','MF'])]


df['low_G_xG'] = ((forwards['xG'] * forwards['Mins'])/90) / forwards['Goals'].replace(0, np.nan)

#only_shooters = df[df['Goals'] > 0] I need to research why i use df for low_g_xg, but i use attackers in the one below

only_shooters = df[['Name', 'Goals', 'Mins', 'xG', 'low_G_xG' ]].sort_values(by= 'low_G_xG', ascending=False).head(10)

plt.figure(figsize=(12,6))
sns.barplot(y=only_shooters['Name'], x=only_shooters['low_G_xG'], hue=only_shooters['low_G_xG'], palette='Blues')
plt.xticks(rotation=45)
plt.title('Most inefficient players (based on xG and Goals)')
plt.ylabel('Name')
plt.xlabel('inefficency Scores')
plt.show()

# Most Efficient scorers (Highest goal pr xG ratio across the whole seaosn)

attackers = df[df['Position'].isin(['FW','MF'])]

attackers['High_G_xG'] = ((attackers['xG'] * attackers['Mins'])/90) / attackers['Goals'].replace(0, np.nan)

only2 = attackers[(attackers['Goals'] > 10)]

only_shooters1 = only2[['Name', 'Goals', 'Mins', 'xG', 'High_G_xG']].sort_values(by= 'High_G_xG', ascending=True).head(10)

plot = (
    ggplot(only_shooters1) +
    aes(x='reorder(Name, High_G_xG)', y='High_G_xG', fill='High_G_xG') +
    geom_col(show_legend=False) +
    coord_flip() +  # Flip axes to match your original seaborn style
    labs(
        title='Most Efficient Players (based on xG and Goals)',
        x='Player Name',
        y='Efficiency (xG per Goal)'
    ) +
    theme_bw()
)
plot.save("my_plot.png")  # ✅ Saves as an image
import os
os.system("open my_plot.png")  # ✅ Opens the image (Mac users)
plt.show()


plt.figure(figsize=(12,6))
sns.barplot(y=only_shooters1['Name'], x=only_shooters1['High_G_xG'], hue=only_shooters1['High_G_xG'], palette='Reds_r')
plt.xticks(rotation=45)
plt.title('Most Efficient players (based on xG and Goals)')
plt.ylabel('Name')
plt.xlabel('Highest efficiency')
plt.show()

# Most "unlucky" playmakers scorers (Highest xA to assist ratio)

playmakers= df[df['Position'].isin(['FW','MF'])]

playmakers['High_xA'] = (playmakers['Mins'] / 90) * (playmakers['xA'] ) / playmakers['Assists'].replace(0, np.nan)



only3 = playmakers[(playmakers['Assists'] > 1)]

only_pass = only3[['Name', 'Assists', 'Mins', 'xA', 'High_xA']].sort_values(by='High_xA', ascending=True).head(10)

plt.figure(figsize=(12,6))
sns.barplot(x=only_pass['Name'], y=only_pass['High_xA'], hue=only_pass['High_xA'], palette='Reds')

plt.xticks(rotation=45)
plt.title('Biggest chance creators compared to actual assists')
plt.xlabel('Name')
plt.ylabel('Biggest waste for creators')
plt.show()


# Most aggresive teams

Club_aggression = df.groupby("Club")[['Yellow_Cards', 'Red_Cards']].sum()
Club_aggression['Aggression_score'] = Club_aggression['Yellow_Cards'] + (2 * Club_aggression['Red_Cards'])


Club_aggression = Club_aggression.sort_values(by='Aggression_score', ascending= True).head(10)

plt.figure(figsize=(12,6))
sns.barplot(x=Club_aggression.index, y=Club_aggression["Aggression_score"], hue=Club_aggression["Aggression_score"], palette='Reds')
plt.title('Sum of yellows and reds pr.team')
plt.xticks(rotation=45)
plt.ylabel('Sum')
plt.xlabel('Club')
plt.show()

