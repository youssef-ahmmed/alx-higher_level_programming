#!/usr/bin/python3
def multiple_returns(sentence):
    return (len(sentence), None) if sentence is None \
                                 else (len(sentence), sentence[0])
