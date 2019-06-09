"""
TrainModel.py
This file includes implementations of the training of the models.
"""

import pandas as pd
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from task2.src.KNN import Knn
from task2.src.DataEditor import edit_data
from task2.src.DecisionTree import Decision_Tree

TEST_SIZE = 0.2
RUNS = 1

knn = False
decision_tree = True

"""
Here we create dataset for training.
This dataset contains equal number of samples from each class.
"""
data = pd.read_csv('Crimes_since_2005.csv')
data = edit_data(data)
# new_df = None
#
# for run_number in range(len(CRIMES)):
#     rows_for_curr_time = data.loc[data["Primary Type"] == run_number]
#
#     if len(rows_for_curr_time) < 20000:
#         new_set_size = 6000
#     else:
#         new_set_size = int(np.floor(len(rows_for_curr_time) * 0.5))
#     chosen_set = rows_for_curr_time.sample(n=new_set_size)
#
#     if new_df is None:
#         new_df = chosen_set
#     else:
#         new_df = new_df.append(chosen_set)
# data = new_df


# Split data to X and y
X = data.iloc[:, :-1]
y = data.iloc[:, -1]
avg_error_rates = []

print("-------HERE---------")

# ---------------------KNN TRAIN---------------------------------------

if knn:

    K_ARRAY = [200, 100, 50, 10, 5]

    for k in K_ARRAY:
        print("Testing K=" + str(k))
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=TEST_SIZE)

        err_rates = []
        for run_number in range(RUNS):

            model = Knn(k)
            model.fit(X_train, y_train)

            good_answers, bad_answers = 0, 0

            for row in range(len(X_test)):
                curr_vector = X_test.iloc[row]
                res = model.predict([curr_vector])

                if res == y_test.iloc[row]:
                    good_answers += 1
                else:
                    bad_answers += 1

            error_rate = bad_answers / (good_answers + bad_answers)
            err_rates.append(error_rate)
        avg_error_rates.append(sum(err_rates) / len(err_rates))

    plt.plot(K_ARRAY, avg_error_rates)
    plt.title("KNN model error rate")
    plt.xlabel("K")
    plt.ylabel("Error rate")
    plt.show()


# ---------------------Decision Tree train---------------------------------------

if decision_tree:

    err_rates_for_decision_tree = []

    for run_number in range(RUNS):
        print("Run number:" + str(run_number))
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=TEST_SIZE)

        dt_model = Decision_Tree()
        dt_model.fit(X_train, y_train)

        good_answers, bad_answers = 0, 0

        for row in range(len(X_test)):
            curr_vector = X_test.iloc[row]
            res = dt_model.predict([curr_vector])

            if res == y_test.iloc[row]:
                good_answers += 1
            else:
                bad_answers += 1

        curr_error_rate = bad_answers / (good_answers + bad_answers)

        # if curr_error_rate < 0.4:
        #     with open("trained_model", 'wb') as f:
        #         pickle.dump(dt_model, f)

        # err_rates_for_decision_tree.append(curr_error_rate)

    # avg_error_for_tree = sum(err_rates_for_decision_tree) / len(err_rates_for_decision_tree)
    # x_axis = np.arange(5)
    # plt.plot(x_axis, err_rates_for_decision_tree)
    # plt.title("DecisionTree model error rate, Avg is: " + str(avg_error_for_tree))
    # plt.xlabel("NUM OF RUN")
    # plt.ylabel("Error rate")
    # plt.show()

# --------------------------------------------------------------------------------

