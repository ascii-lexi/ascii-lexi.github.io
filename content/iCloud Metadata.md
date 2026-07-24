title: Restoring Exported iCloud Metadata
date: 2026-07-20
summary: Oh Apple, this just won't do.	
## Backstory
I am helping my mom migrate away from iCloud as she is tired of the monthly bill and how aggressively her iPhone swaps apps and photos to the cloud to save space. So, after a little research I do what most people in the position say to do (if you don't own a Mac that is, which neither of us do): request a data export from [privacy.apple.com](https://privacy.apple.com)

The only issue is, once they let you download your data, you get a bunch of zip files of photos and videos which have had all of there metadata scrubbed! Gone! Kapoof! And of course, Apple, The King of User Experience gives you 1-5 .csv files in each archive containing the metadata **they** stripped out! Of course this makes it hard to use these images and video in other image hosting software, such as, I don't know, maybe a FOSS self hosted image hosting solution such as the wonderful [Immich.](https://immich.app/)

## Solution
So, I come across a [github repo](https://github.com/zainepils/icloud-photos-export-fix) from [zainepils](https://github.com/zainepils) that has a python script to do just what I am looking for using ExifTool.
I remote in to my mom's home computer using RustDesk, configure the python requirements, and run the script.

## More Solutions, More Problems
Well, about 3 hours in on her 30,000th photo, the script throws a python error.
```
UnicodeEncodeError: 'charmap' codec can't encode character
'\u202f' in position 106: character maps to <undefined>
```

And I am left scratching my head about why Apple would use this "[narrow no-break space](https://unicodeplus.com/U+202F)" character inside of its meta-data, occasionally. After some looking into the error trace, it seems to occur when processing the time stamp, specifically the space between the hour:minute and AM/PM.

Apple's decisions are as inscrutable as ever, so I rolled my eyes and go ahead and modify the script to replace ``\u202f`` and another white-space character ``\xa0`` with a regular space character. 

Run the script again, and this time it completes! I ``rsync`` the files to my Immich instance and done, date sorting works perfect.

## Epilogue
I forked the original script, added my changes, and made a pull request. I also went around Reddit and spread the good word of "The Script That Fixes iCloud Exports"

My mom is happily looking through and sorting her photos on my Immich instance with the year scroll bar working perfectly.

And everyone lived happily ever after.