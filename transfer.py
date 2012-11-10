#!/usr/bin/env python

# for a lack of ideas, i'll just call this the transfer utility
# it performs the copying from the given scout data dump directory and copies the data
# into the meaningful folder hierarchy

import os
import re
import shutil
import yaml
import pprint

source_dir = "/Volumes/Storage/IPC-test/85/2012-11-07"
dest_dir = "/Volumes/Storage/IPC-test/IPC"
pp = pprint.PrettyPrinter()

def load_flight_log(yaml_file):
    # load in a yaml file as a dictionary
    # used this link: http://stackoverflow.com/questions/635483/what-is-the-best-way-to-implement-nested-dictionaries-in-python
    try:
        if os.path.exists(yaml_file):
            file_handle = open(yaml_file)
            flight_log = yaml.safe_load(file_handle)
            file_handle.close()
    except IOError:
        print 'cannot open', yaml_file
        raise

    pp.pprint(flight_log)
    return flight_log

def parse_filename(file_name):
    # 2012-11-07-flight_007-050.dng
    [year, month, day, flight_str, number] = re.split('\-', file_name)
    date = year + '-' + month + '-' + day
    flight_no = int(re.split('\_', flight_str)[1])
    return date, flight_no


def make_dest_dirs(dest_dir):
    if(os.path.isdir(dest_dir)):
        print('%s exists' % dest_dir)
    else:
        print('Creating %s' % dest_dir)
    print('')

    # dest_dir/Week3
    week_dir = os.path.join(dest_dir, 'Week3')
    if(os.path.isdir(week_dir)):
        print('%s exists' % week_dir)
    else:
        print('Creating %s' % week_dir)
    print('')

    # dest_dir/Week3/SnakeRiver
    river_dir = os.path.join(week_dir, 'SnakeRiver')
    if(os.path.isdir(river_dir)):
        print('%s exists' % river_dir)
    else:
        print('Creating %s' % river_dir)
    print('')

    # dest_dir/Week3/SnakeRiver/date
    date_dir = os.path.join(river_dir, '2012-11-06')
    if(os.path.isdir(date_dir)):
        print('%s exists' % date_dir)
    else:
        print('Creating %s' % date_dir)
    print('')

    # dest_dir/Week3/SnakeRiver/date/mile_no
    mile_dir = os.path.join(date_dir, '236.5')
    if(os.path.isdir(mile_dir)):
        print('%s exists' % mile_dir)
    else:
        print('Creating %s' % mile_dir)
    print('')

    # dest_dir/Week3/SnakeRiver/date/mile_no/Log
    log_dir = os.path.join(mile_dir, 'Log')
    if(os.path.isdir(log_dir)):
        print('%s exists' % log_dir)
    else:
        print('Creating %s' % log_dir)
    print('')

    # dest_dir/Week3/SnakeRiver/date/mile_no/RawData  
    rawdata_dir = os.path.join(mile_dir, 'RawData')
    if(os.path.isdir(rawdata_dir)):
        print('%s exists' % rawdata_dir)
    else:
        print('Creating %s' % rawdata_dir)
    print('')        
    return

def main():
    make_dest_dirs(dest_dir)
    file_name = '2012-11-07-flight_007-050.dng'
    [date, flight] = parse_filename(file_name)
    print date
    print flight

    load_flight_log('flight_log.yml')

if __name__ == '__main__':
    main()

"""
src_files = glob.glob(os.path.join(source_dir, '*.*'))
for file_name in src_files:
    full_file_name = os.path.join(src, file_name)
    if(os.path.isfile(full_file_name)):
        shutil.copy2(full_file_name, dest)
"""