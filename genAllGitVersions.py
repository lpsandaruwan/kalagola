#!/usr/bin/python
#   kalagola v0.001 Beta
#   genAllGitVersions.py is copyright (C) 2016, mooniak
#   This script generates all the commited versions of a file in a git repo.
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

count = 1

def crDir():
    os.system( 'rm -r -f font_versions' )
    os.system( 'mkdir font_versions ' )

#this generates log file
def genGitLog( fileName, repoDir ):
    os.system( 'cd ../' + repoDir + '&&git log --pretty=format:%h ' + fileName + ' > ../kalagola/gitLog' )

#this gets an array of git hash of the specific file
def gitLogToArray( repoDir ):
    hashArray = open( 'gitLog' ).read().splitlines()
    print( hashArray )
    return hashArray

#this rolls through the commits
def rollCommits( fileName, repoDir, hashNum ):
    os.system( 'cd ../' + repoDir + ' && git checkout ' + hashNum )

#this copies the
def cpFile( fileName, repoDir ):
    global count
    os.system( 'cp ../fonttest/tests/fonts/experiment-latin-0.otf font_versions/' + str( count ) + '_experiment-latin-0.otf'  )
    count += 1

def process( fileName, repoDir ):
    crDir()
    genGitLog( fileName, repoDir )
    hashArray = gitLogToArray( repoDir )
    for hashNum in hashArray:
        rollCommits( fileName, repoDir, hashNum )
        cpFile( fileName, repoDir )

def main( argv ):
    fileName = repoDir = ""
    if '-F' in argv:
        fileName = argv[ argv.index( '-F' ) + 1 ]
        ##print( fileName )
        if '-d' in argv:
            repoDir = argv[ argv.index( '-d' ) + 1 ]
            ##print( repoDir )
            process( fileName, repoDir )
        else:
            print( "no repo location is given." )
            print( "Usage : python3 gen.py -F [familyName] -d [repoDir]" )
    else:
        print( "no input file is given." )
        print( "Usage : python3 gen.py -d [repoDir] -f [fileName]" )

if __name__ == "__main__":
    main( sys.argv )

    os.system( 'git checkout master' )
