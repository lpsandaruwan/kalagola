#!/usr/bin/python
#   kaalagola v0.001 Beta
#   genMovie.py is copyright (C) 2016, mooniak
#
#   Redistribution and use in source and binary forms, with or without
#   modification, are permitted provided that the following conditions are met:
#
#   Redistributions of source code must retain the above copyright notice, this
#   list of conditions and the following disclaimer.
#
#   Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
#
#   The name of the author may not be used to endorse or promote products
#   derived from this software without specific prior written permission.
#
#   THIS SOFTWARE IS PROVIDED BY THE AUTHOR ``AS IS'' AND ANY EXPRESS OR IMPLIED
#   WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
#   MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO
#   EVENT SHALL THE AUTHOR BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
#   SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
#   PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS;
#   OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
#   WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR
#   OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF
#   ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import os, sys


def cleanDir():
    os.system( 'rm -r -f generated/jpgs' )
    os.system( 'mkdir generated/jpgs' )

def mkJpg():
    global count
    os.system( 'convert -density 400 generated/*pdf generated/jpgs/%04d.jpg ' )

def mkMovie( movieName, frameRate ):
    global count
    os.system( 'ffmpeg ' + '-i generated/jpgs/%04d.jpg ' + '-r ' + frameRate + ' ' + movieName + '.mp4' )

def process( movieName, frameRate ):
    print( "Deleting old gen_Movie files..." )
    cleanDir()
    print( "Making jpgs from pdfs..." )
    mkJpg()
    print( "Making movie now..." )
    mkMovie( movieName, frameRate )
    print( "Generated the movie!" )

def main( argv ):
    movieName = frameRate = ""
    if '-N' in argv:
        movieName = argv[ argv.index( '-N' ) + 1 ]
        #print()
        if '-r' in argv:
            frameRate = argv[ argv.index( '-r' ) + 1 ]
            #print()
            process( movieName, frameRate )
        else:
            print( "No movie name - [movieName] is given! " )
            print( "Usage : python3 genFontImages.py -N [movieName] -r [frameRate]")
    else:
        print( "No Image format - [frameRate] is given." )
        print( "Usage : python3 genFontImages.py -N [movieName] -r [frameRate]" )

if __name__ == "__main__":
    main( sys.argv )
