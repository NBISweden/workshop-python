#!/usr/bin/env python3
from db import HomeDB
from db import haversine as get_distance
from db import plot, sort_by_price


db = HomeDB('../../files/uppsala.sqlite')
lat = 59.865795990339876
lng = 17.64583576202392
radius = 2000  # in m


def cheap_central():
    """ Find the within 2000m from the center and sort by increasing price """
    # This function should select all homes, remove all homes that are
    # not central, and finally return the result sorted by price
    pass


def part_a():
    # This function should print the price of  cheapest, central home (use cheap_central)
    pass


def part_b(outfile):
    # This function get the 100 print the cheapest, central homes (use cheap_central)
    # and then use plot to create a map
    pass


def expensive():
    """ Sort houses by price per square meter """
    # This function should select all houses with an area bigger than 10,
    # and sort them by price (the most expensive house should be the first
    # item of the list)
    pass


def part_c():
    # This function should print the price and area of the most expensive house
    pass


def part_d():
    # This function should plot the one most expensive house
    pass


# our main function will perform all tasks and print the result
if __name__ == "__main__":
    print('Part a:')
    part_a()
    print()
    part_b('selection_b.html')
    print('Part b: printed to selection_b.html')
    print()
    print('Part c:')
    part_c()
    print()
    part_d('selection_d.html')
    print('Part d: printed to selection_d.html') 
