#!/usr/bin/env python

# for a lack of ideas, i'll just call this the transfer utility
# it performs the copying from the given scout data dump directory and copies the data
# into the meaningful folder hierarchy

import os
import shutil

source_dir = "/Volumes/Storage/IPC-test/85/2012-11-07"
dest_dir = "/Volumes/Storage/IPC-test/IPC"

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

if __name__ == '__main__':
    main()

"""
src_files = glob.glob(os.path.join(source_dir, '*.*'))
for file_name in src_files:
    full_file_name = os.path.join(src, file_name)
    if(os.path.isfile(full_file_name)):
        shutil.copy2(full_file_name, dest)
"""