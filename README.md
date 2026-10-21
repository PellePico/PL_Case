# Who beat their expected goals? Premier League 2020/21

![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white) ![Jupyter](https://img.shields.io/badge/Jupyter-notebook-F37626?logo=jupyter&logoColor=white) ![pandas](https://img.shields.io/badge/pandas-150458?logo=pandas&logoColor=white) ![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?logo=scikitlearn&logoColor=white)

A data analysis of every Premier League player in the 2020/21 season, built around one question:
**which players and teams scored more (or less) than the quality of their chances suggested?**

The quality of a chance is measured with **expected goals (xG)**: the probability that a shot becomes a
goal, based on where and how it was taken. A season's xG is what an average finisher would have scored
from the same chances.

**[Open the notebook](pl_2020_21_analysis.ipynb)** to read the full analysis with code and charts.

![Non-penalty goals vs xG](figures/goals_vs_xg.png)

## Key findings

- **xG predicts goals very well over a season.** A linear regression of goals on xG has a slope of
  0.99 and R² = 0.87.
- **Son Heung-min (+6.4) and Gareth Bale (+5.7)** scored the most non-penalty goals above their xG.
  **Timo Werner (−5.9) and Jamie Vardy (−5.7)** fell furthest below.
- **Fulham and Sheffield United were relegated** after scoring 13–15 goals fewer than their chances
  were worth. Tottenham and both Manchester clubs scored well above theirs.
- **Forwards get much better chances than midfielders**: 0.32 vs 0.11 xG per 90 minutes
  (Welch's t-test, p < 0.001).
- **Clustering finds four player roles** (goal threats, creators, ball players, defensive workers)
  that cut across the official positions. Andrew Robertson is listed as a defender but plays like a
  creator, and Kevin De Bruyne is in a league of his own.

![Player roles from PCA and k-means](figures/player_roles.png)

![Teams: goals minus xG](figures/teams_goals_vs_xg.png)

## What's in the notebook

1. Data checks (xG in the data is per 90 minutes, and combined positions like `FW,MF` need handling)
2. Finishing above and below xG, excluding penalties
3. Most goals per 90 minutes (min. 900 minutes played)
4. Playmakers: assists vs expected assists (xA)
5. Teams: goals vs xG, and discipline
6. Regression: does xG predict goals? (statsmodels + a scikit-learn train/test check)
7. Hypothesis test: forwards vs midfielders
8. Player roles with PCA and k-means clustering
9. Radar charts comparing Kane, Salah, Son and Bruno Fernandes
10. Conclusions and limitations

## Run it yourself

```sh
git clone https://github.com/PellePico/PL_Case.git
cd PL_Case
pip install -r requirements.txt
jupyter notebook pl_2020_21_analysis.ipynb
```

## Tools

Python · pandas · NumPy · Matplotlib · SciPy (t-test) · statsmodels (regression) · scikit-learn (PCA, k-means, train/test) · Jupyter

## Data

[English Premier League (2020-21)](https://www.kaggle.com/datasets/rajatrc1705/english-premier-league202021)
from Kaggle (CC0, public domain). `EPL_20_21.csv` has one row per player per club for the 2020/21 Premier League season (532 rows, 20 clubs),
with minutes, goals, assists, penalties, cards, xG and xA per 90 minutes.
