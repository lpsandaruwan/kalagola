#!/usr/bin/python
#   kaalagola v0.001 Beta
#   genFontImages.py is copyright (C) 2016, mooniak
#   This script generates a set of pdfs with each generated font applied to templates/pdf_template.html.
#   Dependencies : wkhtmltopdf
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


count = 1

def fontsListToArray():
    fontFileArray = ( os.listdir('font_versions/') )
    return fontFileArray

def writeCSS( familyName, f ):
    CSSFile = open( 'templates/fonts.css', 'ab+' )
    #@font-face {font-family:'familyName'; src:url("1017_experiment-latin-0.otf");}
    CSSFile.write( bytes( "@font-face {" + '    font-family:\'' + familyName + "\';" + '    src:url(\"' + '../font_versions/'+ f + "\");" + '}\n', 'UTF-8' ) )

def cleanDir():
    os.system( 'rm -r -f generated' )
    os.system( 'rm template/fonts.css' )
    os.system( 'mkdir generated' )
    print( "Deleted old generated files..." )

def mkImg( imgFormat ):
    global count
    os.system( 'wkhtmltopdf -O landscape templates/index.html ' + 'generated/' + str( count ) + '.' + imgFormat )
    count += 1


def process( familyName, imgFormat ):
    fontsListToArray()
    fontFiles = fontsListToArray()
    cleanDir()
    print( "Got the list of fonts..." )
    for f in fontFiles:
        writeCSS( familyName, f )
        print( "Wrote version to css file..." )
        #
        print( "Making image " + str( count ) + " of many..." )
        mkImg( imgFormat )
    print( "All images generated!!!" )


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
            print( "No family name - [familyName] is given! " )
            print( "Usage : python3 genFontImages.py -f [familyName] -i [imageFormat]")
            print( "        [familyName]  This determines the family name on the generated CSS." )
            print( "        [imageFormat] Any format that wkhtmltoimage supports. jpg, jpeg, png and more." )
    else:
        print( "No Image format - [imageFormat] is given." )
        print( "Usage : python3 genFontImages.py -f [familyName] -i [imageFormat]" )
        print( "        [familyName]  This determines the family name on the generated CSS." )
        print( "        [imageFormat] Any format that wkhtmltoimage supports. jpg, jpeg, png and more." )

if __name__ == "__main__":
    main( sys.argv )
