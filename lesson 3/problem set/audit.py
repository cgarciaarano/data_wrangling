#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
In this problem set you work with cities infobox data, audit it, come up with a
cleaning idea and then clean it up. In the first exercise we want you to audit
the datatypes that can be found in some particular fields in the dataset.
The possible types of values can be:
- NoneType if the value is a string "NULL" or an empty string ""
- list, if the value starts with "{"
- int, if the value can be cast to int
- float, if the value can be cast to float, but CANNOT be cast to int.
   For example, '3.23e+07' should be considered a float because it can be cast
   as float but int('3.23e+07') will throw a ValueError
- 'str', for all other values

The audit_file function should return a dictionary containing fieldnames and a 
SET of the types that can be found in the field. e.g.
{"field1: set([float, int, str]),
 "field2: set([str]),
  ....
}

All the data initially is a string, so you have to do some checks on the values
first.
"""
import codecs
import csv
import json
import pprint
import traceback

CITIES = 'cities.csv'

FIELDS = ["name", "timeZone_label", "utcOffset", "homepage", "governmentType_label", "isPartOf_label", "areaCode", "populationTotal", 
          "elevation", "maximumElevation", "minimumElevation", "populationDensity", "wgs84_pos#lat", "wgs84_pos#long", 
          "areaLand", "areaMetro", "areaUrban"]



def audit_file(filename, fields):
    fieldtypes = {}

    with open(CITIES, 'r') as f:
      reader = csv.DictReader(f)

      # Initialise sets
      for header in reader.fieldnames:
        fieldtypes[header] = set()

      # Skip first 4 rows
      reader.next()
      reader.next()
      reader.next()
      reader.next()
      # Process rows
      for row in reader:

        for header in reader.fieldnames:

          # Empty case
          if not row[header] or row[header].lower() == 'null':
            fieldtypes[header].add(type(None))
            continue

          # List case
          if row[header].startswith('{'):
            fieldtypes[header].add(type([]))
            continue

          # Integer & float
          try:
            int_field = int(row[header])
            fieldtypes[header].add(type(1))
          except:
            try:
              if header == "areaLand":
                print('Error casting int for {0}. Traceback info {1}'.format(header, traceback.format_exc()))
              float_field = float(row[header])
              fieldtypes[header].add(type(1.1))
            except:
              if header == "areaLand":
                print('Error casting float for {0}. Traceback info {1}'.format(header, traceback.format_exc()))
              fieldtypes[header].add(type('str'))

        print('{0}'.format(row['areaLand']))

    return fieldtypes


def test():
    fieldtypes = audit_file(CITIES, FIELDS)

    pprint.pprint(fieldtypes)

    assert fieldtypes["areaLand"] == set([type(1.1), type([]), type(None)])
    assert fieldtypes['areaMetro'] == set([type(1.1), type(None)])
    
if __name__ == "__main__":
    test()
