#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Day 2 of AdventOfCode.com: iterating over arrays doing simple arithmetic"""
import os
from numpy import product


def present_wrap_area(dimensions):
    """
    :param dimensions: list of 3 floats: length, width and height
    :return: area of wrapping
    """
    wrap_area = 0
    sides = list()
    for i in range(0, 3):
        for j in range(i+1, 3):
            sides.append(dimensions[i] * dimensions[j])
    for i in range(0, len(sides)):
        wrap_area += 2 * sides[i] 
    wrap_area += min(sides)
    
    return wrap_area


def present_ribbon_length(dimensions):
    """
    :param dimensions: list of 3 floats: length, width and height
    :return: length of ribbon
    """
    ribbon_length = product(dimensions)  
    sorted_dims = sorted(dimensions)
    ribbon_length += 2 * (sorted_dims[0]+sorted_dims[1])
    
    return ribbon_length


def presents(sets_of_dimensions):
    """Calculates total parameters for all presents
    :param sets_of_dimensions: list of lists of 3 floats: length, width and height
    :return:
    """
    return sum([present_wrap_area(dimensions) for dimensions in sets_of_dimensions]), \
        sum([present_ribbon_length(dimensions) for dimensions in sets_of_dimensions])

sets_of_dims = list()
with open(os.path.dirname(os.path.realpath('__file__')) + "/input/day2.txt", "r") as datafile:
    for line in datafile:
        sets_of_dims.append([float(s) for s in line.rstrip("\n").split("x")])

print(presents(sets_of_dims))
