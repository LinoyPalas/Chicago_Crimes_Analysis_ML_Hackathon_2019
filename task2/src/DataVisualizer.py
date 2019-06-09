"""
DataVisualizer.py
This file includes implementations which intends to get plots about data
for researching.
"""

from task2.src.DataEditor import edit_data, YEARS_QUARTERS, TIMES_IN_DAY, DISTRICT, YEAR, COM_AREA
import pandas as pd
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


SIZE_OF_VISUAL_SET = 0.3
KEY_COL = "Primary Type"


# Slicing random slice of the whole data for testing the effect of each feature.
data = pd.read_csv("Crimes_since_2005.csv")
sample, rest = train_test_split(data, test_size=(1 - SIZE_OF_VISUAL_SET))
sample = edit_data(sample)

plt1 = False
plt2 = False
plt3 = False
plt4 = False
plt5 = False
plt6 = False

"""
 Histograms 1 :
 Watch the distribution of crimes in each quarter of the year.
# """
if plt1:
    for quarter in YEARS_QUARTERS:
        rows_for_curr_quarter = sample.loc[sample[quarter] == 1]

        key_col_for_curr_quarter = rows_for_curr_quarter.loc[:, [KEY_COL]]

        points = np.array(key_col_for_curr_quarter)
        counts, bins = np.histogram(points)
        plt.hist(bins[:-1], bins, weights=counts, color='m', alpha=0.5)
        plt.title("Crimes distribution by type in " + quarter + " (20% percents of the data)")
        plt.ylabel("Amount")
        plt.xlabel("Crime Type")
        plt.show()

"""
 Histograms 2 :
 Watch the distribution of crimes in each part of the day.
# """
if plt2:
    for part_of_day in TIMES_IN_DAY:
        rows_for_curr_time = sample.loc[sample[part_of_day] == 1]

        key_col_for_curr_quarter = rows_for_curr_time.loc[:, [KEY_COL]]

        points = np.array(key_col_for_curr_quarter)
        counts, bins = np.histogram(points)
        plt.hist(bins[:-1], bins, weights=counts, color='r', alpha=0.5)
        plt.title("Crimes distribution by type in " + part_of_day + " (20% percents of the data)")
        plt.ylabel("Amount")
        plt.xlabel("Crime Type")
        plt.show()

"""
 Histograms 3 :
 Watch the distribution of crimes in each district.
# """
if plt3:
    districts_max = 25
    for i in range(districts_max):
        rows_for_curr_time = sample.loc[sample[DISTRICT] == i]

        key_col_for_curr_quarter = rows_for_curr_time.loc[:, [KEY_COL]]

        points = np.array(key_col_for_curr_quarter)
        counts, bins = np.histogram(points)
        plt.hist(bins[:-1], bins, weights=counts, color='b', alpha=0.5)

        plt.title("Crimes distribution in district " + str(i) + " (20% percents of the data)")
        plt.ylabel("Amount")
        plt.xlabel("Crime Type")
        plt.show()

"""
 Histograms 4 :
 Watch the distribution of crimes in each year.
# """
if plt4:
    year_start, year_end = 2005, 2019
    for i in range(year_start, year_end):
        rows_for_curr_year = sample.loc[sample[YEAR] == i]

        key_col_for_curr_year = rows_for_curr_year.loc[:, [KEY_COL]]

        points = np.array(key_col_for_curr_year)
        counts, bins = np.histogram(points)
        plt.hist(bins[:-1], bins, weights=counts, color='g', alpha=0.5)

        plt.title("Crimes distribution in " + str(i) + " (20% percents of the data)")
        plt.ylabel("Amount")
        plt.xlabel("Crime Type")
        plt.show()

"""
 Histograms 5 :
 Watch the distribution of crimes in each Community area.
# """
if plt5:
    community_area = 75
    for i in range(1, community_area):
        rows_for_curr_time = sample.loc[sample[COM_AREA] == i]

        key_col_for_curr_quarter = rows_for_curr_time.loc[:, [KEY_COL]]

        points = np.array(key_col_for_curr_quarter)
        counts, bins = np.histogram(points)
        plt.hist(bins[:-1], bins, weights=counts, color='b', alpha=0.5)

        plt.title("Crimes distribution in com area " + str(i) + " (20% percents of the data)")
        plt.ylabel("Amount")
        plt.xlabel("Crime Type")
        plt.show()


"""
 Heatmap 6 :
 Watch the correlation between features
# """
if plt6:
    sns.set(style="white")

    # Generate a large random dataset
    labels = ['year_period_quarter_1', 'year_period_quarter_2',
              'year_period_quarter_3', 'year_period_quarter_4', 'day_time',
              'night_time', 'Beat', 'District', 'Ward', 'Community Area', 'X Coordinate',
              'Y Coordinate', 'Latitude', 'Longitude', 'Community Areas',
              'Wards', 'Domestic', 'Arrest', 'x_block', 'Primary Type']
    d = pd.DataFrame(data=sample,columns=labels)

    # Compute the correlation matrix
    corr = sample.corr()

    # Generate a mask for the upper triangle
    mask = np.zeros_like(corr, dtype=np.bool)
    mask[np.triu_indices_from(mask)] = True

    # Set up the matplotlib figure
    f, ax = plt.subplots(figsize=(11, 9))

    # Generate a custom diverging colormap
    cmap = sns.diverging_palette(220, 10, as_cmap=True)

    # Draw the heatmap with the mask and correct aspect ratio
    sns.heatmap(corr, mask=mask, cmap=cmap, vmax=.3, center=0,
                square=True, linewidths=.5, cbar_kws={"shrink": .5})

    plt.show()