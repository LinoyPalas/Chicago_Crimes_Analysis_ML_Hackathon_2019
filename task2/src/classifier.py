"""
classifier.py
This file includes an implementation of classifier which uses the entire files.
"""

from task2.src.DataEditor import edit_data
import pickle


def classify(test_data):
    edited_test_data = edit_data(test_data)

    with open("trained_model", 'rb') as f:
        model = pickle.load(f)

    to_return = []

    for row in range(len(edited_test_data)):
        curr_vector = edited_test_data.iloc[row]
        res = model.predict([curr_vector])
        to_return.append(res[0])

    return to_return

