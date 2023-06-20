"""
Case Handler Unit: Transform the text from the clipboard and paste the result instantly.

Author: Gilberto Granados Zapatero

"""

import tkinter as tk
from tkinter import messagebox
from idlelib.tooltip import Hovertip
import pyperclip
import pytesseract
from PIL import ImageGrab
import speech_recognition as sr
import pyaudio
import wave
import tempfile
import os



def main():

    gui()

# Update clipboard content
def refresh_clipboard():

    # Define text and text_in_preview as global variables
    global text, text_in_preview

    # Getting clipboard text
    text = pyperclip.paste()

    # If multiple lines get only first for the preview
    first_row = text.splitlines()[0] if text else ""

    # If first line is very long, take only first 26 characters to preview
    if len(first_row) > 26:
        text_in_preview = first_row[0:26] + "..."
    else:
        text_in_preview = first_row

    return text, text_in_preview

def gui():

    # GUI part

    # Create the main window
   
    window = tk.Tk()
    window.title("Case Handler Unit")

    # Set the window decorations and dimensions
    window.geometry("270x1000")
    
    frame_text_info = tk.Frame(window, bg="lightgray", relief=tk.SUNKEN, bd=1, height=12, width=29, padx=10, pady=10)
    frame_text_info.pack(pady=5)

    # Update text length and word count information on button click
    update_button = tk.Button(frame_text_info, text="Text Info",font=("Sans", 10), bg="#c9daf8", command=lambda: text_info(refresh_clipboard(), text_in_preview, preview_in_label, length_label, word_count_label))
    update_button.pack(pady=5)
    my_tip = Hovertip(update_button, "Show info about copied text", hover_delay=300)
    
    # Create a label for previewing the clipboard content
    preview_in_label = tk.Label(frame_text_info, text="Case IN: ", font=("Sans", 10), height=1, width=29, fg="#666666")
    preview_in_label.pack(pady=5)

    # Create labels for text length and word count
    length_label = tk.Label(frame_text_info, text="Text Length:", font=("Sans", 10), height=1, width=29)
    length_label.pack(pady=5)

    word_count_label = tk.Label(frame_text_info, text="Word Count:", font=("Sans", 10), height=1, width=29)
    word_count_label.pack(pady=5)
    
    frame_converters = tk.Frame(window, bg="lightgray", relief=tk.SUNKEN, bd=1, height=12, width=29, padx=10, pady=10)
    frame_converters.pack(pady=5)
    # Create button widget for uppercase text
    uppercase_button = tk.Button(frame_converters, text="| CONVERT TO UPPERCASE |", font=("Sans", 10), bg="white", width=(29), command=lambda: convert_to_uppercase(refresh_clipboard(), text_in_preview, preview_out_label))
    uppercase_button.pack(pady=5)
    my_tip = Hovertip(uppercase_button, "Convert copied text to Upper Case", hover_delay=300)

    # Create button widget for lowercase text
    lowercase_button = tk.Button(frame_converters, text="| convert to lowercase |", font=("Sans", 10), bg="white", width=(29), command=lambda: convert_to_lowercase(refresh_clipboard(), text_in_preview, preview_out_label))
    lowercase_button.pack(pady=5)
    my_tip = Hovertip(lowercase_button, "Convert copied text to Lower Case", hover_delay=300)

    # Create button widget for title case text
    titlecase_button = tk.Button(frame_converters, text="| Convert To Title Case |", font=("Sans", 10), bg="white", width=(29), command=lambda: convert_to_titlecase(refresh_clipboard(), text_in_preview, preview_out_label))
    titlecase_button.pack(pady=5)
    my_tip = Hovertip(titlecase_button, "Convert copied text to Title Case", hover_delay=300)

    # Create button widget for sentence case text
    sentencecase_button = tk.Button(frame_converters, text="| Convert to sentence case |", font=("Sans", 10), bg="white", width=(29), command=lambda: convert_to_sentencecase(refresh_clipboard(), text_in_preview, preview_out_label))
    sentencecase_button.pack(pady=5)
    my_tip = Hovertip(sentencecase_button, "Convert copied text to Sentence case", hover_delay=300)

    # Create entry field for prefixer
    prefix_entry = tk.Entry(frame_converters)
    prefix_entry.pack(pady=10)

    # Create button widget for prefixer
    button_prefix = tk.Button(frame_converters, text="Prefix",font=("Sans", 10), bg="white", command=lambda: prefix_text(refresh_clipboard(), prefix_entry, preview_out_label))
    button_prefix.place(relx=0.0, rely=0.72)
    my_tip = Hovertip(button_prefix, "Type desired prefix", hover_delay=300)
    
    # Create entry field for suffixer
    suffix_entry = tk.Entry(frame_converters)
    suffix_entry.pack(pady=5)

    # Create button widget for suffixer
    button_suffix = tk.Button(frame_converters, text="Suffix",font=("Sans", 10), bg="white", command=lambda: suffix_text(refresh_clipboard(), suffix_entry, preview_out_label))
    button_suffix.place(relx=0.0, rely=0.87)
    my_tip = Hovertip(button_suffix, "Type desired suffix", hover_delay=300)
    
    # Create a frame for audio recorder
    frame_replacer = tk.Frame(window, bg="lightgray", relief=tk.SUNKEN, bd=1, height=140, width=265, padx=5, pady=5)
    frame_replacer.pack(pady=5)
    
    # Create label for replacer
    replace_label = tk.Label(frame_replacer, text="Text Replacer", bg="lightgray", font=("Sans", 10))
    replace_label.place(relx=0.3, rely=0)
    
    # Create label for text to find
    find_label = tk.Label(frame_replacer, bg="lightgray", text="Find:", font=("Sans", 10))
    find_label.place(relx=0.0, rely=0.25)
    
    # Create entry field for text to find
    find_entry = tk.Entry(frame_replacer)
    find_entry.place(relx=0.25, rely=0.25)

    # Create label for text to replace with
    replace_label = tk.Label(frame_replacer, bg="lightgray", text="Replacer:", font=("Sans", 10))
    replace_label.place(relx=0.0, rely=0.5)
    
    # Create entry field for text to replace with
    replace_entry = tk.Entry(frame_replacer)
    replace_entry.place(relx=0.25, rely=0.5)

    # Create button widget for find and replace
    button_find_replace = tk.Button(frame_replacer, text="Find and Replace", font=("Sans", 10), bg="white", command=lambda: find_and_replace(refresh_clipboard(), find_entry, replace_entry, preview_out_label ))
    button_find_replace.place(relx=0.3, rely=0.75)
    my_tip = Hovertip(button_find_replace, "Find and replace the entered text ", hover_delay=300)
    
    # Create a frame for image scanner
    frame_scanner = tk.Frame(window, bg="lightgray", relief=tk.SUNKEN, bd=1, height=12, width=265, padx=5, pady=5)
    frame_scanner.pack(pady=5)
    
    # Create a label for image scanner
    image_scanner_label = tk.Label(frame_scanner, text="Image Scanner", bg="lightgray", font=("Sans", 10), height=1, width=31)
    image_scanner_label.pack(pady=5)
    
    # Create a button for extracting text from the image
    image = None
    button_extract = tk.Button(frame_scanner, text="Extract Text", font=("Sans", 10), bg="white", command=lambda: extract_text_from_image(image, preview_out_label))
    button_extract.pack(pady=5)
    my_tip = Hovertip(button_extract, "Scan and extract text from the image in the clipboard", hover_delay=300)
    
    # Create a frame for audio recorder
    frame_recorder = tk.Frame(window, bg="lightgray", relief=tk.SUNKEN, bd=1, height=100, width=265, padx=5, pady=5)
    frame_recorder.pack(pady=5)
    
    # Create a label for audio recorder
    audio_recorder_label = tk.Label(frame_recorder, text="Audio Recognizer", bg="lightgray", font=("Sans", 10))
    audio_recorder_label.place(relx=0.3, rely=0)
    
    # Create a button for start recodring
    start_button = tk.Button(frame_recorder, text="Rec",font=("Sans", 10), bg="white", command=lambda: start_recording(preview_out_label))
    start_button.place(relx=0.02, rely=0.45)
    my_tip = Hovertip(start_button, "Start to record the audio", hover_delay=300)

    # Create a button for stop and save recording
    stop_button = tk.Button(frame_recorder, text="Stop",font=("Sans", 10), bg="white", command=lambda: stop_recording(preview_out_label))
    stop_button.place(relx=0.2, rely=0.45)
    my_tip = Hovertip(stop_button, "Stop the recording", hover_delay=300)

    # Create a button for English text extraction
    recognize_button_eng = tk.Button(frame_recorder, text="Extract Text (ENG)", font=("Sans", 10), bg="white", command=lambda: recognize_speech_en(audio, preview_out_label))
    recognize_button_eng.place(relx=0.47, rely=0.3)
    my_tip = Hovertip(recognize_button_eng, "Recognize english audio for text extraction", hover_delay=300)
    
    # Create a button for spanish text extraction
    recognize_button_esp = tk.Button(frame_recorder, text="Extract Text (ESP)", font=("Sans", 10), bg="white",  command=lambda: recognize_speech_es(audio, preview_out_label))
    recognize_button_esp.place(relx=0.47, rely=0.65)
    my_tip = Hovertip(recognize_button_esp, "Recognize spanish audio for text extraction", hover_delay=300)
        
    # Create a label for previewing the text converted
    preview_out_label = tk.Label(window, text="Case OUT: ", wraplength=260, height=1, fg="#666666")
    preview_out_label.pack(pady=5)

    # Create the "Help" button
    help_button = tk.Button(window, text="About", font=("Sans", 10), bg="white", command=lambda: toggle_instructions(instructions_frame))
    help_button.pack(side=tk.TOP)
    
    # Create a canvas
    canvas = tk.Canvas(window, bg="lightgray", relief=tk.SUNKEN, bd=1, width=276, height=290)
    canvas.pack()

    # Load the image
    image = tk.PhotoImage(file="images/Logo_Case_Handler_Unit.gif")
    #resized_image = image.subsample(2, 2)  # Resize the image by half
    
    # Display the image on the canvas
    canvas.create_image(0, 0, anchor="nw", image=image)

    # Create a frame for the instructions panel
    instructions_frame = tk.Frame(canvas, bg="lightgray", relief=tk.SUNKEN, bd=1, width=276, height=290)
    

    # Create a label with the instructions
    instructions_label = tk.Label(instructions_frame,
    text="Welcome to Case Handler Unit, How it works?\n\n\
1.- It works with any text or image in the clipboard,\n\
you can record an audio file too, it recognize\n\
any text strings on it.\n\
2.- Click on a button to extract from image or audio\n\
if nedeed, then transform yor text as you need.\n\
3.- And finally paste your converted text \n\
strings where you want. \n\n\
Developed by Gilberto Granados",
    height=(12), width=(260), justify="left", font=("Sans", 8), bg="lightgray")

    instructions_label.pack(padx=1, pady=1)

    # Start with the instructions panel hidden
    instructions_frame.pack_forget()

    window.mainloop()

# CASE HANDLER UNIT FUNCTIONS

# Toggle instructions pane
def toggle_instructions(instructions_frame):

    if instructions_frame.winfo_ismapped():
        instructions_frame.pack_forget()
    else:
        instructions_frame.pack(side=tk.BOTTOM, fill=tk.X)

# Show data about text in the clipboard
def text_info(text, text_in_preview, preview_in_label, length_label, word_count_label):

    text, text_in_preview = refresh_clipboard()

    if text:

        # Calculate the length of the text
        text_length = len(text)

        # Count the occurrences of each word
        word_count = len(text.split())

        # Update the preview, length and word count labels
        preview_in_label.config(text=f"Case IN: {text_in_preview}")
        length_label.config(text=f"Text Length: {text_length}")
        word_count_label.config(text=f"Word Count: {word_count}")

        return text, text_in_preview

    else:

        # Handle the case where there is no text in the clipboard
        tk.messagebox.showwarning("No Text", "There is no text in the clipboard.")

# Convert clipboard text to uppercase
def convert_to_uppercase(text, text_in_preview, preview_out_label):

    text, text_in_preview = refresh_clipboard()

    if text:

        text_upper = text.upper()
        text_out_preview = text_in_preview.upper()
        # Set the modified text back to the clipboard
        pyperclip.copy(text_upper)
        preview_out_label.config(text=f"Case OUT: {text_out_preview}")

        return text_upper

    else:

        # Handle the case where there is no text in the clipboard
        tk.messagebox.showwarning("No Text", "There is no text in the clipboard.")

# Convert clipboard text to lowercase
def convert_to_lowercase(text, text_in_preview, preview_out_label):

    text, text_in_preview = refresh_clipboard()

    if text:

        text_lower = text.lower()
        text_out_preview = text_in_preview.lower()
        # Set the modified text back to the clipboard
        pyperclip.copy(text_lower)
        # Show output case preview in label
        preview_out_label.config(text=f"Case OUT: {text_out_preview}")

        return text_lower

    else:

        # Handle the case where there is no text in the clipboard
        tk.messagebox.showwarning("No Text", "There is no text in the clipboard.")

# Convert clipboard text to title case
def convert_to_titlecase(text, text_in_preview, preview_out_label):

    text, text_in_preview = refresh_clipboard()

    if text:

        text_title = text.title()
        text_out_preview = text_in_preview.title()
        # Set the modified text back to the clipboard
        pyperclip.copy(text_title)
        # Show output case preview in label
        preview_out_label.config(text=f"Case OUT: {text_out_preview}")

        return text_title

    else:

        # Handle the case where there is no text in the clipboard
        tk.messagebox.showwarning("No Text", "There is no text in the clipboard.")

# Convert clipboard text to sentence case
def convert_to_sentencecase(text, text_in_preview, preview_out_label):

    text, text_in_preview = refresh_clipboard()

    if text:

        text_sentence = text.capitalize()
        text_out_preview = text_in_preview.capitalize()
        # Set the modified text back to the clipboard
        pyperclip.copy(text_sentence)
        # Show output case preview in label
        preview_out_label.config(text=f"Case OUT: {text_out_preview}")

        return text_sentence
    else:

        # Handle the case where there is no text in the clipboard
        tk.messagebox.showwarning("No Text", "There is no text in the clipboard.")

# Set a prefix to the clipboard text
def prefix_text(text, prefix_entry, preview_out_label):

    text = refresh_clipboard()[0]

    if text:
        # Get the prefix from the entry box
        prefix = prefix_entry.get()

        # Prefix each line of the text
        prefixed_lines = [prefix + line for line in text.splitlines()]

        # Join the lines back together
        text_prefixed = '\n'.join(prefixed_lines)

        # Set the modified text back to the clipboard
        pyperclip.copy(text_prefixed)

         # Split the text by newlines and take the first element
        first_row = text_prefixed.splitlines()[0]

        if len(first_row) > 26:
            text_out_preview = first_row[0:26] + "..."
        else:
            text_out_preview = first_row

        # Show output case preview in label
        preview_out_label.config(text=f"Case OUT: {text_out_preview}")

        return prefix_text

    else:

        # Handle the case where there is no text in the clipboard
        tk.messagebox.showwarning("No Text", "There is no text in the clipboard.")

# Set a suffix to the clipboard text
def suffix_text(text, suffix_entry, preview_out_label):

    text = refresh_clipboard()[0]

    if text:
        # Get the suffix from the entry box
        suffix = suffix_entry.get()

        # Suffix each line of the text
        suffixed_lines = [line + suffix for line in text.splitlines()]

        # Join the lines back together
        text_suffixed = '\n'.join(suffixed_lines)

        # Set the modified text back to the clipboard
        pyperclip.copy(text_suffixed)

        # Split the text by newlines and take the first element
        first_row = text_suffixed.splitlines()[0]

        if len(first_row) > 26:
            text_out_preview = first_row[0:26] + "..."
        else:
            text_out_preview = first_row

        # Show output case preview in label
        preview_out_label.config(text=f"Case OUT: {text_out_preview}")

        return suffix_text

    else:

        # Handle the case where there is no text in the clipboard
        tk.messagebox.showwarning("No Text", "There is no text in the clipboard.")

# Find and replace text      
def find_and_replace(text, find_entry, replace_entry, preview_out_label):
    
    text = refresh_clipboard()[0]
    
    if text:
        # Get the find and replace strings from the entry boxes
        find_string = find_entry.get()
        replace_string = replace_entry.get()

        # Perform the find and replace operation
        text_replaced = text.replace(find_string, replace_string)

        # Set the modified text back to the clipboard
        pyperclip.copy(text_replaced)
        
        # Split the text by newlines and take the first element
        first_row = text_replaced.splitlines()[0]

        if len(first_row) > 26:
            text_out_preview = first_row[0:26] + "..."
        else:
            text_out_preview = first_row

        # Show output case preview in label
        preview_out_label.config(text=f"Case OUT: {text_out_preview}")

        return text_replaced
              
    else:
        # Handle the case where there is no text in the clipboard
        tk.messagebox.showwarning("No Text", "There is no text in the clipboard.")

# Scann image in the clipboard and extract text      
def extract_text_from_image(image, preview_out_label):
    # Get the image from the clipboard
    image = ImageGrab.grabclipboard()

    if image:
        # Convert the image to grayscale
        text = ""
        image = image.convert("L")

        # Use Tesseract to extract text from the image
        text_extracted = pytesseract.image_to_string(image)

        if text_extracted:
            # Set the extracted text to the clipboard
            pyperclip.copy(text_extracted)
             # Split the text by newlines and take the first element
            first_row = text_extracted.splitlines()[0]

            if len(first_row) > 26:
                text_out_preview = first_row[0:26] + "..."
            else:
                text_out_preview = first_row

            # Show output case preview in label
            preview_out_label.config(text=f"Case OUT: {text_out_preview}")

            return text_extracted
        else:
            # Handle the case where no text was extracted
            tk.messagebox.showwarning("No Text", "No text was extracted from the image.")
    else:
        # Handle the case where there is no image in the clipboard
        tk.messagebox.showwarning("No Image", "There is no image in the clipboard.")

# Values for audio settings
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100

frames = []
stream = None
temp_file = None
audio = None

# Start the recording
def start_recording(preview_out_label):
    global frames, stream, temp_file, audio

    frames = []
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
    audio = pyaudio.PyAudio()

    stream = audio.open(
        format=FORMAT,
        channels=CHANNELS,
        rate=RATE,
        input=True,
        frames_per_buffer=CHUNK,
        stream_callback=callback
    )
    preview_out_label.config(text=f"Case OUT: Recording started...")
    print("Recording started...")

# Stop the recording
def stop_recording(preview_out_label):
    global frames, stream, temp_file, audio

    stream.stop_stream()
    stream.close()
    audio.terminate()

    with wave.open(temp_file.name, 'wb') as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(audio.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
    preview_out_label.config(text=f"Case OUT: Recording stopped")
    print(f"Recording stopped. File saved at: {temp_file.name}")

# Restart the recording process
def callback(in_data, frame_count, time_info, status):
    frames.append(in_data)
    return in_data, pyaudio.paContinue

# Text recognition from audio in spanish
def recognize_speech_es(audio, preview_out_label):
    
    recognizer = sr.Recognizer()
    
    if audio:
        
        with sr.AudioFile(temp_file.name) as source:
            audio = recognizer.record(source)
        try:
            text_extracted = recognizer.recognize_google(audio, language='es-ES')
            print("Recognized Text:", text_extracted)
            
            
            # Set the extracted text to the clipboard
            pyperclip.copy(text_extracted)
            # Split the text by newlines and take the first element
            first_row = text_extracted.splitlines()[0]

            if len(first_row) > 26:
                text_out_preview = first_row[0:26] + "..."
            else:
                text_out_preview = first_row

            # Show output case preview in label
            preview_out_label.config(text=f"Case OUT: {text_out_preview}")
            
            # Close the audio file before deleting it
            temp_file.close()
            
            # Delete the temporary audio file
            os.remove(temp_file.name)
            print("Temporary file deleted.")

            return text_extracted  
        
        except sr.UnknownValueError:
            preview_out_label.config(text=f"Case OUT: Audio not understood")
            print("Speech recognition could not understand audio")
        except sr.RequestError as e:
            preview_out_label.config(text=f"Case OUT: Audio not recognized")
            print("Could not request results from speech recognition service; {0}".format(e))
            
    else:
        # Handle the case where no text was extracted
        tk.messagebox.showwarning("No Audio", "No audio file has been recorded")

# Text recognition from audio in english
def recognize_speech_en(audio, preview_out_label):
    
    recognizer = sr.Recognizer()
    
    if audio:
        
        with sr.AudioFile(temp_file.name) as source:
            audio = recognizer.record(source)
        try:
            text_extracted = recognizer.recognize_google(audio, language='en-EN')
            print("Recognized Text:", text_extracted)
            
            
            # Set the extracted text to the clipboard
            pyperclip.copy(text_extracted)
            # Split the text by newlines and take the first element
            first_row = text_extracted.splitlines()[0]

            if len(first_row) > 26:
                text_out_preview = first_row[0:26] + "..."
            else:
                text_out_preview = first_row

            # Show output case preview in label
            preview_out_label.config(text=f"Case OUT: {text_out_preview}")
            
            # Close the audio file before deleting it
            temp_file.close()
            
            # Delete the temporary audio file
            os.remove(temp_file.name)
            print("Temporary file deleted.")

            return text_extracted  
            
        except sr.UnknownValueError:
            preview_out_label.config(text=f"Case OUT: Audio not understood")
            print("Speech recognition could not understand audio")
        except sr.RequestError as e:
            preview_out_label.config(text=f"Case OUT: Audio not recognized")
            print("Could not request results from speech recognition service; {0}".format(e))
    
    else:
        # Handle the case where no text was extracted
        tk.messagebox.showwarning("No Audio", "No audio file has been recorded")

if __name__ == "__main__":
     main()