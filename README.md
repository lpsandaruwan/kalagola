# kaalagola
Time traveling machine for font projects



- Roll through git commits and generate all the versions of a file
- Make a pdf file for each version using `wkhtmltopdf`. Files for the tamplate for pdf is in `/template`
- Convert pdf to jpg using imagemagick
- Make a movei using ffmepg



##Prepare your Repo and files

TODO: Write prep instructions.

###Install dependencies

- git
- wkhtmltopdf
- imagemagick
- ffmpeg

##Grab all the versions of a font file with `genAllGitVersions.py`

```
python3 genAllGitVersions.py -F [familyName] -d [repoDirectory]


```


##Generate images with `genFontImages`

```

python3 genFontImages.py -f [familyName] -i [imageFormat]

```

`[familyName]` This determines the family name on the generated CSS.
` [imageFormat] ` Any format that wkhtmltoimage supports. `jpg`, `jpeg`, `png` and more.

`python3 genFontImages.py -f Experiment -i pdf`

TODO: Range selector for date and time
TODO: Git hash list input

##Genrating movie with `genMovie.py`


```
 python3 genMovie.py -r 10 -N movie
```
