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