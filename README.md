# UCS654_Mashup

# YouTube Mashup Generator and Web Service

## Overview

This project consists of two programs:

1.  Command Line Mashup Generator
2.  Flask-based Web Service

The system downloads YouTube songs of a specified singer, converts them
into audio clips, trims them, merges them into a mashup, and optionally
emails the result.


## Program 1 --- Command Line Mashup Generator

### Command

python `<rollnumber>`{=html}.py "Singer Name"
`<Number_of_Videos>`{=html} `<Duration>`{=html}
`<Output_File_Name>`{=html}

Example: python 101556.py "Sharry Maan" 20 30 mashup.mp3

### Workflow

-   Search YouTube videos using yt-dlp
-   Download best audio
-   Convert to MP3
-   Trim clips
-   Merge into mashup

## Program 2 --- Web Service

### Inputs

-   Singer Name
-   Number of Videos
-   Duration
-   Email Address

### Workflow

-   User submits form
-   Email validated
-   Mashup generated
-   Output zipped
-   Email sent


## Technologies

Python, Flask, yt-dlp, MoviePy, Pydub, FFmpeg, Yagmail
