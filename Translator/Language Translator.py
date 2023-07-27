# importing tkinter
import tkinter as tk

# importing ttk module from tkinter as it has the combobox class
from tkinter import ttk

# let's get the language list in this file
import backend

import googletrans
language_translator = googletrans.Translator()

# importing the OS module
import os

# importing gtts and playsound module
import gtts


# importing recognizer
import speech_recognition as sr

# let's create a recognizer which can recognize my speech
recognizer_engine = sr.Recognizer()

# let's create the do_translation function
def do_translation():
    
    # Step 1--> Get/Read the source and target language from the combobox
    source_lang = source_cb.get()
    target_lang = target_cb.get()
    # print(source_lang, target_lang)

    # Step 2--> Let's fetch what the user has written in the textbox
    user_message = input_text.get(1.0, tk.END)
    # print(user_message)

    # Step 3--> Let's do the translation
    output = language_translator.translate(text=user_message, src=source_lang, dest=target_lang)
    translated_text = output.text

    # Step 4--> Put it on the label
    output_label.config(text=translated_text)

# clear text function
def clear_text():

    # clear the textbox and label
    output_label.config(text='')
    input_text.delete(1.0, tk.END)

# let's create the speak text function
def speak_text():

    # let's get the text
    text_on_label = output_label.cget('text')

    # let's get the target language abbreviation
    target_language = target_cb.get()

    # lets check the index of target language in language list
    index_of_target_language = languages.index(target_language)

    # let's get the abbreviation
    abbrev = abrreviations[index_of_target_language]
    
    # let's create the tts engine
    tts_engine = gtts.gTTS(text=text_on_label, lang=abbrev)
    
    # let's save the audio
    if os.path.isfile('result.mp3'):

        # let's remove it
        os.remove('result.mp3')

    # saving the file
    tts_engine.save('result.mp3')

    # let's play it
    playsound.playsound('result.mp3')

# defining say something
def say_something():

    # let's first attach the microphone with the python script
    with sr.Microphone() as mic:

    # let's get the audio
        audio = recognizer_engine.listen(mic)

        # let's convert the text from audio
        # output = recognizer_engine.recognize_google(audio, language='fr-FR')
        output = recognizer_engine.recognize_google(audio)

    # let's print it on textbox
    input_text.insert(1.0, output)

# lets create the language list
languages = backend.get_languages()
abrreviations = backend.get_abbreviations()

# creating root gui
root = tk.Tk()

# properties of root gui
root.geometry('700x400')
root.resizable(width=False, height=False)
root.title('Language Translator')
root.config(bg='#f5fefd')

# Universal variables
py = 10 # This is padding not pixels
px = 30
bg_color = '#7b3f00'
fg_color = 'white'
button_font = 'Helvetica'
button_font_size = 12

# Adding widgets
welcome_label = tk.Label(root, text='LANGUAGE TRANSLATOR', bg='#f5fefd', font=('Comic Sans MS', 30))
welcome_label.pack(pady=20)

# creating a frame to arrange my widget in grid layout
frame = tk.Frame(root, bg='#e7decc', width=500, height=100)
frame.pack(padx=10, pady=10, fill='both')

# source and target language labels
source_label = tk.Label(frame, text='Source Language', bg=bg_color, fg=fg_color, font=('Comic Sans MS', 20))
target_label = tk.Label(frame, text='Target Language', bg=bg_color, fg=fg_color, font=('Comic Sans MS', 20))
source_label.grid(row=0, column=0, padx=px, pady=py)
target_label.grid(row=0, column=2, padx=px, pady=py)

# Add comboboxes
source_cb = ttk.Combobox(frame, values=languages, width=30)
# setting the default language
source_cb.current(21)
target_cb = ttk.Combobox(frame, values=languages, width=30)
target_cb.current(38)
source_cb.grid(row=1, column=0, padx=px, pady=py)
target_cb.grid(row=1, column=2, padx=px, pady=py)

# Adding row 2 elements --> Input text area, translate button, Output label
input_text = tk.Text(frame, width=25, height=5)
translate_button = tk.Button(frame, text='Translate', bg=bg_color, fg=fg_color, font=(button_font, button_font_size), command=do_translation)
output_label = tk.Label(frame, text='No Translations Yet!', bg=bg_color, fg=fg_color, width=30, height=5)
input_text.grid(row=2, column=0, padx=px, pady=py)
translate_button.grid(row=2, column=1, padx=px, pady=py)
output_label.grid(row=2, column=2, padx=px, pady=py)

# Adding row 3 elements --> voice,  clear, speak button
voice_button = tk.Button(frame, text='Say Something', bg=bg_color, fg=fg_color, font=(button_font, button_font_size), command=say_something)
clear_button = tk.Button(frame, text='Clear', bg=bg_color, fg=fg_color, font=(button_font, button_font_size), command=clear_text)
speak_button = tk.Button(frame, text='Speak Translation', bg=bg_color, fg=fg_color, font=(button_font, button_font_size), command=speak_text)
voice_button.grid(row=3, column=0, padx=px, pady=py)
clear_button.grid(row=3, column=1, padx=px, pady=py)
speak_button.grid(row=3, column=2, padx=px, pady=py)

# for continuous display
root.mainloop()