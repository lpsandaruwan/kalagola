# KalaGola
Time travel for font projects

Im learning python, this is and excersise. Thanks @lpsandaruwan for work on Animager. Animager will merge to this and become KalaGola.

Name KalaGola comes from a character in Ummagga Jataka in Buddhist Jaataka Kata. Kala Gola, ugly short man, who is married to beautiful Dikthala. He is made a slave by her he has to do all the household work. The pun is Kala means time, and Gola means companion or helper. A classic from Dikthala Kala Gola : https://www.youtube.com/watch?v=iwyg71HF8M8

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
