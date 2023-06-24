# CASE HANDLER UNIT

Video Demo: [coming soon](coming soon)

    This repository contains the project Case Handler Unit, which allows you to transform text from the clipboard and paste the result instantly.

## Author

- Gilberto Granados Zapatero

## Description

The Case Handler Unit is a graphical user interface (GUI) application built using the tkinter library in Python. It provides several operations to modify text, such as converting to uppercase, lowercase, title case, and sentence case. Additionally, it allows you to add a prefix or suffix to the text. It includes functionalities for extract text from images and audios in English or Spanish

## Folder Contents

- Case_Handler_Unit.py: This is the file which contains my main function and the other functions necessary to implement the application.
- Case Handler Unit logo
- Case handler Unit icon
- requirements.txt: All pip-installable libraries that I used for this project are listed here.

## How to Use

1. Copy the text you want to modify to the clipboard.
2. Run the Case Handler Unit application.
3. You can capture screen portion with text to be extracted
4. Or record an audio file to extrat text from it
5. Click on the corresponding button to perform the desired text transformation.
6. The modified text will be copied back to the clipboard automatically.
7. You can paste the modified text wherever you want.

## Requirements

- tkinter
- edlelib.tooltip
- pyperclip
- pytesseract
- Tesseract install from https://github.com/UB-Mannheim/tesseract/wiki
- ImageGrab from PIL 
- SpeechRecognition
- pyaudio
- wave
- tempfile
- os

## Usage

To start the Case Handler Unit, use python and run the following command:

    $ Case_Handler_Unit.py

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

- https://github.com/asweigart/pyperclip/blob/master/LICENSE.txt	pyperclip	bsd 3
- https://github.com/eirannejad/pyRevit/blob/master/LICENSE.txt	pyrevit	gnu general public license
- https://github.com/madmaze/pytesseract/blob/master/LICENSE	pytesseract	apache license 2.0
- https://github.com/tesseract-ocr/tesseract/blob/main/LICENSE	tesseract	apache license 2.0
- https://github.com/python-pillow/Pillow/blob/main/LICENSE	pil	hpnd license
- https://github.com/Uberi/speech_recognition	speech recognition	BSD 3
- https://github.com/djfroofy/PyAudio	pyaudio	MIT License

----------------------------------------------
Copyright Notice
----------------------------------------------

This application includes the following third-party libraries:

1. Pyperclip

   Pyperclip - Copyright (c) 2010-2020 Al Sweigart
   Website: https://github.com/asweigart/pyperclip
   License: MIT License

   Pyperclip is used for cross-platform clipboard access.

2. Pytesseract

   Pytesseract - Copyright (c) 2017-2021 GitHub contributors
   Website: https://github.com/madmaze/pytesseract
   License: Apache License 2.0

   Pytesseract is used for optical character recognition (OCR) functionality.

3. PyAudio

   PyAudio - Copyright (c) 2011-2017 The PyAudio Authors
   Website: http://people.csail.mit.edu/hubert/pyaudio/
   License: MIT License

   PyAudio is used for audio input/output functionality.

4. PIL (Pillow)

   PIL (Python Imaging Library) - Copyright (c) 1995-2011 by Secret Labs AB and the
   contributors
   Website: https://python-pillow.org/
   License: PIL Software License

   PIL, or Pillow, is used for image processing and manipulation.

5. Tesseract

   Tesseract OCR - Copyright (c) 2006-2020 Google LLC
   Website: https://github.com/tesseract-ocr/tesseract
   License: Apache License 2.0

   Tesseract is an OCR engine used by Pytesseract for text recognition.

6. SpeechRecognition

   SpeechRecognition - Copyright (c) 2013-2021 Anthony Zhang
   Website: https://github.com/Uberi/speech-recognition
   License: BSD 3-Clause License

   SpeechRecognition is used for speech recognition functionality.

These libraries are provided under their respective licenses, and their inclusion in this application does not imply endorsement or affiliation with the authors of the application.

Please refer to the license files or the corresponding websites for more information about the terms and conditions of each library.
