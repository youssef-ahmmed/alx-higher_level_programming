#!/usr/bin/python3
"""Solve Peak Problem"""


def binary_search_peak(arr, low, high):
    if low == high:
        return arr[low]

    mid = (low + high) // 2

    if arr[mid] >= arr[mid + 1]:
        return binary_search_peak(arr, low, mid)
    else:
        return binary_search_peak(arr, mid + 1, high)


def find_peak(list_of_integers):
    if not list_of_integers:
        return None

    size = len(list_of_integers)

    return binary_search_peak(list_of_integers, 0, size - 1)
