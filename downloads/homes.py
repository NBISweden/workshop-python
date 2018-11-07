from db import HomeDB
from db import haversine as get_distance
from db import plot, sort_by_price

lat = 59.865795990339876
lng = 17.64583576202392
radius = 2000  # in m


def find_homes():
    db = HomeDB('uppsala.sqlite')
    db.connect()
    homes = db.select('rooms > 1 and rooms < 3 and area > 58 and rent < 3000')
    db.disconnect()

    #############################################
    #                                           #     #
    #    THIS IS WHERE YOU INSERT YOUR CODE     #    ##
    #                                           #   ###
    #############################################  ################
    #                                           # #################
    selected_homes = homes[:10]  # cheating     #  ################
    special_home = homes[0]      # wrong one    #   ###
    #                                           #    ##
    #############################################     #

    return special_home, selected_homes


if __name__ == "__main__":
    special_home, selected_homes = find_homes()
    plot(selected_homes,
         output = 'selection.html',
         special = special_home,
         zoom = 13,
         latitude=lat,
         longitude=lng,
         radius=radius # in m
    )
    print('Check the results in selection.html.')
    print('Special home: {}'.format(special_home))
