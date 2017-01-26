""" KalaGola

KalaGola: reminds you how your font is made.

author: Lahiru Pathirage<lpsandaruwan@gmail.com>
author: Pathum Egodawaththe<pathumego@gmail.com>

26/01/2017
"""


import argparse
import cv2
import git
import sys
import time
import yaml

from git import Repo
from weasyprint import HTML

from FileManager import FileManager


# initial data
fm = FileManager()
YAML_FILE = 'config.yml'


# initial argument parser object
parser = argparse.ArgumentParser()

# arguments
parser.add_argument(
    '-a', '--adir', type=str, help='Directory to put font file dynamically'
)
parser.add_argument(
    '-b', '--branch', type=str, help='Branch containing font files'
)
parser.add_argument(
    '-f', '--font', type=str, help='Font file source'
)
parser.add_argument(
    '-i', '--index', type=str, help='Custom index html file'
)
parser.add_argument(
    '-n', '--name', type=str, help='Output file name'
)
parser.add_argument(
    '-r', '--repo', type=str, help='GitHub user repository'
)
parser.add_argument(
    '-s', '--stylesheet', type=str, help='Custom CSS style sheet'
)
parser.add_argument(
    '-t', '--interval', type=int, help='Refresh intervals to increase CPU usage'
)
parser.add_argument(
    '-u', '--user', type=str, help='GitHub username/organization name'
)
parser.add_argument(
    '-y', '--yaml', type=str, help='Read settings from yaml file'
)

args = parser.parse_args()


# set yaml file from user args if it has been called
if args.yaml is not None:
    YAML_FILE = args.yaml

# read yaml file data
with open(YAML_FILE) as yaml_stream:
    try:
        YAML_DATA = yaml.load(yaml_stream)
    except yaml.YAMLError as exc:
        print(exc)
        sys.exit(0)


# set data from yaml file
NAME = YAML_DATA['name']
ASSETS_DIR = YAML_DATA['assets_dir']
BRANCH = YAML_DATA['branch']
FONT_FILE = YAML_DATA['font_file']
INDEX_FILE = YAML_DATA['index_file']
INTERVAL = YAML_DATA['interval']
REPOSITORY = YAML_DATA['repository']
STYLESHEET = YAML_DATA['stylesheet']
USER = YAML_DATA['user']

# overriding data when arguments has been provided
if args.name is not None:
    NAME = args.name
if args.adir is not None:
    ASSETS_DIR = args.adir
if args.branch is not None:
    BRANCH = args.branch
if args.font is not None:
    FONT_FILE = args.font
if args.index is not None:
    INDEX_FILE = args.index
if args.interval is not None:
    INTERVAL = args.interval
if args.repo is not None:
    REPOSITORY = args.repo
if args.stylesheet is not None:
    STYLESHEET = args.stylesheet
if args.user is not None:
    USER = args.user


# setting up git data
GIT_URL = 'http://github.com/' + USER + '/' + REPOSITORY
CLONE_DIR = 'repository/' + REPOSITORY

# creating directories
print('KalaGola is creating directories')
fm.create_directory('repository')
fm.create_directory('temp')
fm.create_directory('videos')
fm.create_directory(CLONE_DIR)

# cloning git repository
print('KalaGola is cloning ' + REPOSITORY + ', please be patience...')
Repo.clone_from(GIT_URL, CLONE_DIR)

# Switch to branch, where font file exists
GIT_REPO = git.Repo(CLONE_DIR)
GIT_REPO.git.checkout('origin/gh-pages')
print('KalaGola has switched to ' + BRANCH + ' successfully')

# check font file path
FONT_PATH = CLONE_DIR + '/' + FONT_FILE

if fm.is_file_exists(FONT_PATH):
    print('KalaGola has found your precious font file \'' + FONT_PATH + '\'')
else:
    print('KalaGola couldn\'t find you font. Please check settings again.')
    sys.exit(0)

# generate commits list on font file
COMMITS = list(GIT_REPO.iter_commits(paths=FONT_FILE))
COMMIT_INDEX = len(COMMITS)


if COMMIT_INDEX is 0:
    print('KalaGola has found no commits.')
    sys.exit(0)
else:
    print('KalaGola has found all the commits for your font')

# iterate though commits and capture all html file views
for commit in COMMITS:
    if COMMIT_INDEX % INTERVAL is 0:
        time.sleep(1)

    print('Checkout ' + str(commit.message) + ' by ' + str(commit.author))
    GIT_REPO.git.checkout(commit)

    print('Copying font file...')
    fm.copy_file(FONT_PATH, ASSETS_DIR + '/myfont')

    print('Taking snapshot ' + str(COMMIT_INDEX))
    HTML(filename='template/index.html').write_png(
        'temp/' + str(COMMIT_INDEX) + '.png',
        stylesheets=[STYLESHEET]
    )

    COMMIT_INDEX -= 1
    print('Remaining snapshots ' + str(COMMIT_INDEX))

if COMMIT_INDEX is 0:
    print('Kalagola has captured all the images.')
else:
    print('KalaGola couldn\'t capture all the images.')
    sys.exit(0)


# export as a video file
print('Generating video file, Please be patience')
frame = cv2.imread('temp/1.png')
cv2.imshow('video', frame)
height, width, channels = frame.shape

fourcc = cv2.VideoWriter_fourcc(*'h264')
video_file = cv2.VideoWriter(
    'videos/' + NAME + '.avi', fourcc, 20.0, (width,height)
)

for index in range(1, len(COMMITS) + 1):
    image_file = 'temp/' + str(index) + '.png'

    if fm.is_file_exists(image_file):
        print("Adding " + image_file)
        frame = cv2.imread(image_file)
        video_file.write(frame)
    else:
        continue

video_file.release()

print("KalaGola has finished the work. Enjoy your video " + 'videos/' + NAME)
