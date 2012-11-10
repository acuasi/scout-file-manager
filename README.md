scout-file-manager
==================

# Description
When you download imagery data from the Aeryon Scout to an external usb device, the data is organized by day and flight number.
Our solution up to this point has been to maintain a separate document that bridges the gap from Aeryon's day/flight# to a more useful folder hierarchy.
When you have multiple flights over multiple days, and are faced with copying hundred of gigs into the new meaningful hierarchy, you can easily lose many hours of productive time.

This program is a stab at solving the issue. As before, you generate an external file that maps the day and flight number to a meaningful folder hierarchy.
The python script will then copy files from the usb 'data dump' directories into the meaningful user defined folder structure.