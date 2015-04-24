#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author: Mariano Draghi <mdraghi at gmail dot com>
# Copyrigth: This program has been placed in the public domain.

"""
A simple script to get a list of files from a Nokia mobile phone
using gnokii_, and print that list in stdout in M3U_ format.

Example usage::

    $ nokia_m3u.py "E:/path/to/music/files" > my_playlist.m3u

Please note that "E:/path/to..." is a path ON THE PHONE, as seen by
gnokii, and not a path in your computer's filesystem. 

The generated m3u can later by uploaded to the phone using gnokii
directly. Please note that for the phone to recognize the playlist,
it must be saved in a special folder, which name might vary from
one phone model / firmware version to another.

For example, to upload the m3u generated in the above example to
a Nokia 6131::

    $ gnokii --putfile my_playlist.m3u \
      A:/predefgallery/predefplaylist/my_playlist.m3u

The script relies on gnokii being properly installed and configured
in the system, and expect the mobile phone to be connected to the
computer (using cable, bluetooth or whatever method you configured
gnokii to use).

.. _gnokii: http://www.gnokii.org/
.. _M3U: http://en.wikipedia.org/wiki/M3U

:Authors:
    Mariano Draghi
"""

__docformat__ = 'restructuredtext'

import os, sys
from subprocess import Popen, PIPE

SONG_EXT = set(('.mp3', '.wma', '.m4a',))


def print_m3u(phone_path):
    """Print a M3U playlist from given path in the mobile phone.
    """
    
    # get file list using gnokii
    p = Popen(['gnokii', '--getfilelist', os.path.join(phone_path, '*')],
              stdout=PIPE, stderr=PIPE)
    status = p.wait()

    # check for any unexpected error
    if status != 0:
        sys.stderr.writelines(p.stderr.readlines())
        sys.exit(status)

    # first line of output is usually:
    #    Filelist for path <phone_path>/*: 
    # discard first line; strip and order the rest
    lines = list([line.strip() for line in p.stdout.readlines()[1:]])
    lines.sort()

    # for each line, check if the file has a valid extension, and print
    # it.
    print_header = True
    for song in [line for line in lines if
                 os.path.splitext(line)[-1].lower() in SONG_EXT]:
        if print_header:
            # print m3u header
            print_header = False
            print "#EXTM3U\r\n",

        print "#EXTINF:0, -\r\n",
        print os.path.join(phone_path, song).replace('/', '\\') + "\r\n", 


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print "Usage: %s <path-to-folder-with-music-files>" % sys.argv[0]
        sys.exit(1)

    print_m3u(sys.argv[1])

