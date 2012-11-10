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

    return flight_log

def parse_filename(file_name):
    # 2012-11-07-flight_007-050.dng
    [year, month, day, flight_str, number] = re.split('\-', file_name)
    date = year + '-' + month + '-' + day
    flight_no = int(re.split('\_', flight_str)[1])
    return date, flight_no

def check_folder(path):
    if not os.path.isdir(path):
        print('Creating %s' % path)

def make_dest_dirs(dest_dir, flight_log):
    # we want to go to the following layout
    # Week3
    #   SnakeRiver
    #       236.5
    #           Log
    #           RawData
    #       233
    #           Log
    #           RawData

    if not os.path.isdir(dest_dir):
        print('Creating %s' % dest_dir)

    for week,value in flight_log.iteritems():
        print week
        week_dir = os.path.join(dest_dir, week)
        check_folder(week_dir)

        for river, value in flight_log[week].iteritems():
            print("  " + river)
            river_dir = os.path.join(week_dir, river)
            check_folder(river_dir)

            for date, value in flight_log[week][river].iteritems():
                # we dont need to make a date directory in our desired layout
                # but we will need to know it in order to progress through the data structure

                for mile, value in flight_log[week][river][date].iteritems():
                    print("      " + mile)
                    mile_dir = os.path.join(river_dir, mile)
                    check_folder(mile_dir)

                    for folder in ['Log', 'RawData']:
                        lowest_dir = os.path.join(mile_dir, folder)
                        check_folder(lowest_dir)

    return

def main():
    flight_log = load_flight_log('flight_log.yml')
    pp.pprint(flight_log)
    


    make_dest_dirs(dest_dir, flight_log)
    #file_name = '2012-11-07-flight_007-050.dng'
    #[date, flight] = parse_filename(file_name)
    #print date
    #print flight

if __name__ == '__main__':
    main()

"""
src_files = glob.glob(os.path.join(source_dir, '*.*'))
for file_name in src_files:
    full_file_name = os.path.join(src, file_name)
    if(os.path.isfile(full_file_name)):
        shutil.copy2(full_file_name, dest)
"""