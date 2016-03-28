#!/usr/bin/python
#   INCOMPLETE!!!
#   kaalagola v0.001 Beta
#   genSlider.py is copyright (C) 2016, mooniak
#   Dependencies : git
#   Usage : python3 gen.py -i [fileDirectory] -f [relativePathOfFiFromReposRootfileName]
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

def fontsListToArray():
    fontFileArray = ( os.listdir('fonts/') )
    print (fontFileArray)
    return fontFileArray

def writeCSS( familyName ):
    CSSFile = open( 'font.css', 'ab+' )
    fontFiles = fontsListToArray()

    for f in fontFiles:
        CSSFile.write( bytes( "@font-face {\n", 'UTF-8' ) )
        CSSFile.write( bytes( '    font-family:\'' + familyName + "\';\n", 'UTF-8' ) )
        CSSFile.write( bytes( '    src:url(\"' + f + "\") format(\'" + "\');\n", 'UTF-8'  ) )
        CSSFile.write( bytes( '}\n\n', 'UTF-8' ) )

    CSSFile.close()

def process( familyName, imgFormat ):
    fontsListToArray()
    writeCSS( familyName )


def main( argv ):
    familyName = imgFormat = ""
    if '-f' in argv:
        familyName = argv[ argv.index( '-f' ) + 1 ]
        ##print( familyName )
        if '-i' in argv:
            imgFormat = argv[ argv.index( '-i' ) + 1 ]
            ##print( imgFormat )
            process( familyName, imgFormat )
        else:
            print( "no file location is given." )
            print( "Usage : python3 gen.py -i [imgFormatectory] -f [familyName]" )
    else:
        print( "no input file is given." )
        print( "Usage : python3 gen.py -i [imgFormatectory] -f [familyName]" )

if __name__ == "__main__":
    main( sys.argv )
