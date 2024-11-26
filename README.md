# MTG Card Format Identifier
Script that uses tesseract,opencv and the [scryfall](https://scryfall.com/) api to tell you what formats the card your camera is pointing at is legal in.

## Prerequisites:
[Tesseract OCR](https://github.com/UB-Mannheim/tesseract/wiki) 

This is the text recognition engine used by the code. If it is not located in "C:/Program Files/Tesseract-OCR/" you will have to change a line of the code to locate the tesseract executable.

[pytesseract](https://pypi.org/project/pytesseract/)

[requests](https://pypi.org/project/requests/)

[pillow](https://pypi.org/project/pillow/)

[opencv](https://pypi.org/project/opencv-python/)

## Usage:
run the script as you would any other python script.

line up the card name as well as you can within the green box.

press "y" to run the contents within the box through an OCR.

Read the Console to find out if that card is legal.

press "q" to close all camera windows before ending the script.

## Troubleshooting:
Tesseract only supports english by default, you will have to tell it to install other languages. In my experience it does not like accented characters, an "Ü" is consistently read as "ii".

Keep requests to under 10 a second. This is outlined as a limit in the [scryfall API](https://scryfall.com/docs/api).

I recomend you only have a single camera connected while running this.

## Questions? Concerns? Complaints?

If you're hasbro and want to file a legal complaint I am not claiming to represent you in any capacity, Magic: The Gathering and all related content  is copyright Wizards of the Coast, LLC. This Script is not produced by or endorsed by Wizards of the Coast.

If theres a bug or you just want to ask a question you can reach me at [twitter](https://x.com/LetheForgot) or [bluesky](https://bsky.app/profile/letheforgot.bsky.social)

I will probably update this to be more useful outside of my very specific niche thing that bothered me at some point.
