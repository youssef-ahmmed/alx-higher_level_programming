#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None

    best = max(a_dictionary.values())
    keys = [key for key, value in a_dictionary.items() if value == best]
    return keys[0] if keys else None
