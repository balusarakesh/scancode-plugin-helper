"""
Given 2 CSV files each with two lists, compare them and send the results.
old_csv 
 - column 1  - SHA1
 - column 2 - file_name
new_csv
 - column 1 - SHA1
 - column 2  - file_name
Return the files which are new and also the one's whose SHA1 is changed.
"""

import csv


def get_key_using_value(input_dict, input_value):
    for key, value in input_dict.iteritems():
        if input_dict[key] == input_value:
            return key
    return None


def compare_csvs(old_csv, new_csv):
    old = {}
    new = {}
    with open(old_csv, 'rb') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter = ',')
        for row in csv_reader:
            old[row['LOCATION']] = row['SHA1SUM']
    with open(new_csv, 'rb') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter = ',')
        for row in csv_reader:
            new[row['LOCATION']] = row['SHA1SUM']
    modified_new = []
    for sha1sum in new.values():
        if sha1sum not in old.values():
            modified_new.append(get_key_using_value(new, sha1sum))
        elif get_key_using_value(new, sha1sum) != get_key_using_value(old, sha1sum):
            modified_new.append(get_key_using_value(new, sha1sum))
    return modified_new
