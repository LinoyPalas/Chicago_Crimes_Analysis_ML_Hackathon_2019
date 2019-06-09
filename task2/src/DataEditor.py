"""
DataEditor.py
This file includes implementation of the methods which edits the data.
"""

import pandas as pd

"""
Features:
"""
ID = "ID"
DATE = "Date"
BLOCK = "Block"
LOC_DES = "Location Description"
ARREST = "Arrest"
DOMESTIC = "Domestic"
BEAT = "Beat"
DISTRICT = "District"
WARD = "Ward"
COM_AREA = "Community Area"
X_COORD = "X Coordinate"
Y_COORD = "Y Coordinate"
YEAR = "Year"
UPDATE = "Updated On"
LAT = "Latitude"
LONG = "Longitude"
COM_AREAS = "Community Areas"
WARDS = "Wards"

"""
Features we added after editing:
"""
X_BLOC = "x_block"
DIRECT = "direction"
QUARTER1 = "year_period_quarter_1"
QUARTER2 = "year_period_quarter_2"
QUARTER3 = "year_period_quarter_3"
QUARTER4 = "year_period_quarter_4"
TIME_DAY = "day_time"
TIME_NIGHT = "night_time"
YEARS_QUARTERS = [QUARTER1, QUARTER2, QUARTER3, QUARTER4]
TIMES_IN_DAY = [TIME_DAY, TIME_NIGHT]


# ------ Edit block column -------#
def edit_block(d):
    """
    :param d: data
    :return: 097XX S AVENUE L split to x_block= "097XX", direction= "s", street= "AVENUE L"
    """
    x_block, direction = [], []
    curr_block_col = d.loc[:, BLOCK]
    for i in range(len(curr_block_col)):
        curr_block = curr_block_col.iloc[i]
        x_block.append(curr_block[:5])
        direction.append(curr_block[6:7])

    for i in range(len(x_block)):
        newstr = x_block[i].replace("X", "")
        x_block[i] = int(newstr)

    # d[X_BLOC] = x_block
    # d[DIRECT] = direction
    d.loc[:, X_BLOC] = x_block
    d.loc[:, DIRECT] = direction
    d.drop(BLOCK, axis=1, inplace=True)
    return d


# ---------------------------------#

# ----- Edit the Date column ----- #
def edit_date(d):
    """
    example - "05/27/2019 11:30:00 PM"
    """
    all_dates = d.loc[:, DATE]
    first_quarter, second_quartet, third_quartet, fourth_quartet = [], [], [], []
    day_time, night_time = [], []
    for i in range(len(all_dates)):
        curr_date_and_time = all_dates.iloc[i]
        date, time = curr_date_and_time.split()[0], curr_date_and_time.split()[1]

        time_in_year = get_quarter_of_month(date[:2])
        time_in_day = get_time_of_day(time[:2])

        if time_in_year == 1:
            first_quarter.append(1)
            second_quartet.append(0)
            third_quartet.append(0)
            fourth_quartet.append(0)
        if time_in_year == 2:
            first_quarter.append(0)
            second_quartet.append(1)
            third_quartet.append(0)
            fourth_quartet.append(0)
        if time_in_year == 3:
            first_quarter.append(0)
            second_quartet.append(0)
            third_quartet.append(1)
            fourth_quartet.append(0)
        if time_in_year == 4:
            first_quarter.append(0)
            second_quartet.append(0)
            third_quartet.append(0)
            fourth_quartet.append(1)

        if time_in_day == 1:
            day_time.append(1)
            night_time.append(0)
        elif time_in_day == 2:
            day_time.append(0)
            night_time.append(1)
        else:
            day_time.append(0)
            night_time.append(0)

    d.loc[:, QUARTER1] = first_quarter
    d.loc[:, QUARTER2] = second_quartet
    d.loc[:, QUARTER3] = third_quartet
    d.loc[:, QUARTER4] = fourth_quartet

    d.loc[:, TIME_DAY] = day_time
    d.loc[:, TIME_NIGHT] = night_time

    d.drop(DATE, axis=1, inplace=True)

    return d


def get_quarter_of_month(month):
    """
    month - string of two digits.
    """
    first, second, third, fourth = ["01", "02", "03"], ["04", "05", "06"], ["07", "08", "09"], ["10", "11", "12"]
    if month in first:
        return 1
    if month in second:
        return 2
    if month in third:
        return 3
    else:
        return 4


def get_time_of_day(time):
    """
    time - string of two digits.
    returns - 1 day time, 2 night time
    """
    day_time = ["06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17"]
    night_time = ["18", "19", "20", "21", "22", "23", "00", "01", "02", "03", "04", "05"]
    if time in day_time:
        return 1
    if time in night_time:
        return 2


# --------------------------------#

# -------- Edit Domestic -------- #
def edit_domestic(d):
    new_domestic = []
    curr_domestic = d.loc[:, DOMESTIC]
    for i in range(len(curr_domestic)):
        if curr_domestic.iloc[i]:
            new_domestic.append(1)
        else:
            new_domestic.append(0)

    d.drop(DOMESTIC, axis=1, inplace=True)
    d.loc[:, DOMESTIC] = new_domestic
    return d


# ----- --------- ----- #

# -------- Edit Arrest -------- #
def edit_arrest(d):
    new_arrest = []
    curr_arrest = d.loc[:, ARREST]
    for i in range(len(curr_arrest)):
        if curr_arrest.iloc[i]:
            new_arrest.append(1)
        else:
            new_arrest.append(0)

    d.drop(ARREST, axis=1, inplace=True)
    d.loc[:, ARREST] = new_arrest
    return d


# ----- --------- ----- #

# --------CAST STRING TO INT----#

def cast(d):
    district_numbers, community_area, beat = [], [], []
    district_col = d.loc[:, DISTRICT]
    com_area_col = d.loc[:, COM_AREA]
    beat_col = d.loc[:, BEAT]

    for i in range(len(district_col)):
        district_numbers.append(int(district_col.iloc[i]))

    for i in range(len(com_area_col)):
        community_area.append(int(com_area_col.iloc[i]))

    for i in range(len(beat_col)):
        beat.append(int(beat_col.iloc[i]))

    d.loc[:, DISTRICT] = district_numbers
    d.loc[:, COM_AREA] = community_area
    d.loc[:, BEAT] = beat

    return d


# ------------------------------------#

# ----- Edit Primary Type ----- #
PRIMARY_TYPE_COLUMN = "Primary Type"
THEFT = 0
BATTERY = 1
NARCOTICS = 2
BURGLARY = 3
WEAPONS_VIOLATION = 4
DECEPTIVE_PRACTICE = 5
CRIMINAL_TRESPASS = 6
PROSTITUTION = 7
CRIMES = ["THEFT", "BATTETY", "NARCOTICS", "BURGLARY", "WEAPONS_VIOLATION", "DECEPTIVE_PRACTICE", "CRIMINAL_TRESPASS",
          "PROSTITUTION"]


def edit_primary_type(d):
    curr_primary_type = d.loc[:, PRIMARY_TYPE_COLUMN]
    new_primary_type = []
    for i in range(len(curr_primary_type)):
        if curr_primary_type.iloc[i] == "THEFT":
            new_primary_type.append(THEFT)
        if curr_primary_type.iloc[i] == "BATTERY":
            new_primary_type.append(BATTERY)
        if curr_primary_type.iloc[i] == "NARCOTICS":
            new_primary_type.append(NARCOTICS)
        if curr_primary_type.iloc[i] == "BURGLARY":
            new_primary_type.append(BURGLARY)
        if curr_primary_type.iloc[i] == "WEAPONS VIOLATION":
            new_primary_type.append(WEAPONS_VIOLATION)
        if curr_primary_type.iloc[i] == "DECEPTIVE PRACTICE":
            new_primary_type.append(DECEPTIVE_PRACTICE)
        if curr_primary_type.iloc[i] == "CRIMINAL TRESPASS":
            new_primary_type.append(CRIMINAL_TRESPASS)
        if curr_primary_type.iloc[i] == "PROSTITUTION":
            new_primary_type.append(PROSTITUTION)

    d.drop(PRIMARY_TYPE_COLUMN, axis=1, inplace=True)
    d.loc[:, PRIMARY_TYPE_COLUMN] = new_primary_type
    return d


# ----- --------- ----- #

# ----- edits the entire data ----- #
def edit_data(d):
    if 'Unnamed: 0' in d.columns:
        d.drop('Unnamed: 0', axis=1, inplace=True)
    d.drop(UPDATE, axis=1, inplace=True)
    d.drop(ID, axis=1, inplace=True)
    d.drop(YEAR, axis=1, inplace=True)

    d = d.fillna(0)
    d = edit_date(d)
    d = edit_domestic(d)
    d = edit_arrest(d)
    d = edit_block(d)
    d = cast(d)  # Cast : edits - Beat, District, Community Area

    d.drop(TIME_DAY, axis=1, inplace=True)
    d.drop(TIME_NIGHT, axis=1, inplace=True)

    d.drop(QUARTER1, axis=1, inplace=True)
    d.drop(QUARTER2, axis=1, inplace=True)
    d.drop(QUARTER3, axis=1, inplace=True)
    d.drop(QUARTER4, axis=1, inplace=True)

    categorical_features = [LOC_DES, DIRECT]
    d = pd.get_dummies(d, prefix_sep="_", columns=categorical_features)

    new_columns_order = ['Beat', 'District', 'Ward', 'Community Area', 'X Coordinate',
                         'Y Coordinate', 'Latitude', 'Longitude', 'Community Areas',
                         'Wards', 'Domestic', 'Arrest', 'x_block']

    if PRIMARY_TYPE_COLUMN in d.columns:
        d = edit_primary_type(d)
        new_columns_order = ['Beat', 'District', 'Ward', 'Community Area', 'X Coordinate',
                             'Y Coordinate', 'Latitude', 'Longitude', 'Community Areas',
                             'Wards', 'Domestic', 'Arrest', 'x_block', 'Primary Type']

    d = d[new_columns_order]
    return d

# ----- --------- ----- #


    # new_columns_order = ['year_period_quarter_1', 'year_period_quarter_2',
    #                      'year_period_quarter_3', 'year_period_quarter_4', 'day_time',
    #                      'night_time', 'Beat', 'District', 'Ward', 'Community Area', 'X Coordinate',
    #                      'Y Coordinate', 'Latitude', 'Longitude', 'Community Areas',
    #                      'Wards', 'Domestic', 'Arrest', 'x_block', 'Primary Type']