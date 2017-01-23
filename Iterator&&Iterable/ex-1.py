# -*- coding: utf-8 -*-
# #!/usr/bin/env python


# iterator and iterable are different
# iter(list1） == list1.__iter__()
# iter(strings1) == strings1.__getitem__()
list1 = [1,2,3,4,5]
strings1 = 'abcde'
iter(list1) # <listiterator at 0x10ab65cd0>
iter(strings1) # <iterator at 0x10ab65690>

# here a bit complex example to go through above mentioned iterator and iterable
# get the abbreviation of the station in 12306

from pprint import pprint
import re
import requests
from collections import Iterator, Iterable


# iterator should have method of next()
# below is how to create a iterator object

URL = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.8955'


class StationInfoIterator(Iterator):

    def __init__(self, cities, url):
        self.cities = cities
        self.index = 0
        self.url = url
        self.stations_dict = self.get_stations_dict()

    def get_station_info(self, city):
        return "%s:  %s" % (city, self.stations_dict[city])

    def get_stations_dict(self):
        # Solve InsecureRequestWarning: Unverified HTTPS request is being made
        from requests.packages.urllib3.exceptions import InsecureRequestWarning
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

        stations_dict = {}
        content = requests.get(self.url, verify=False)
        stations = re.findall(r'([A-Z]+\|[a-z]+)', content.text)
        for station in iter(stations):
            stations_dict[station.split('|')[1]] = station.split('|')[0]
        # you could pprint as you like
        # pprint(stations_dict, indent=4)
        return stations_dict

        # stations_dict = get_stations_dict(URL)
        # stations_list = [{key: value} for key, value in stations_dict.iteritems()]

    def next(self):
        if self.index == len(self.cities):
            # throw/raise Exception
            raise StopIteration
        city = self.cities[self.index]
        self.index += 1
        return self.get_station_info(city)


# iterable should have method of __iter__()
# below is how to create a iterable object


class StationInfoIterable(Iterable):

    def __init__(self, cities, url):
        self.url = url
        self.cities = cities

    def __iter__(self):
        return StationInfoIterator(self.cities, self.url)



# test info

for x in StationInfoIterable(['beijing', 'shanghai', 'tianjin'], URL):
    print x