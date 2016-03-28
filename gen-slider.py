#!/usr/bin/python

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
