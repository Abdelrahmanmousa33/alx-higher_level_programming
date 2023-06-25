#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary) == 0:
        return (None)
    score = 0
    for key, value in a_dictionary.items():
        if value > score:
            best = key
            score = value
    return (best)
