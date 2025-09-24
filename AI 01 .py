from tkinter import *
from deep_translator import GoogleTranslator
import pyperclip
from gtts import gTTS
import os
import playsound

def translate_text():
    source_lang = source_lang_entry.get()
    target_lang = target_lang_entry.get()
    input_text = input_text_box.get("1.0", END).strip()
    
    if not input_text:
        output_text_box.delete("1.0", END)
        output_text_box.insert(END, "Please enter text.")
        return
    
    try:
        translated = GoogleTranslator(source=source_lang, target=target_lang).translate(text=input_text)
        output_text_box.delete("1.0", END)
        output_text_box.insert(END, translated)
    except Exception as e:
        output_text_box.delete("1.0", END)
        output_text_box.insert(END, f"Error: {str(e)}")

def copy_text():
    translated_text = output_text_box.get("1.0", END).strip()
    pyperclip.copy(translated_text)

def speak_text():
    text = output_text_box.get("1.0", END).strip()
    if text:
        tts = gTTS(text)
        tts.save("temp.mp3")
        playsound.playsound("temp.mp3")
        os.remove("temp.mp3")

root = Tk()
root.title("Language Translation Tool")
root.geometry("600x500")

Label(root, text="Enter text to translate:", font=("Arial", 12)).pack()
input_text_box = Text(root, height=6, width=60)
input_text_box.pack()

Label(root, text="Source Language Code (e.g. 'en'):", font=("Arial", 10)).pack()
source_lang_entry = Entry(root)
source_lang_entry.pack()

Label(root, text="Target Language Code (e.g. 'fr'):", font=("Arial", 10)).pack()
target_lang_entry = Entry(root)
target_lang_entry.pack()

Button(root, text="Translate", command=translate_text, bg="blue", fg="white").pack(pady=10)

Label(root, text="Translated Text:", font=("Arial", 12)).pack()
output_text_box = Text(root, height=6, width=60)
output_text_box.pack()

Button(root, text="Copy", command=copy_text).pack(pady=5)
Button(root, text="Speak", command=speak_text).pack(pady=5)

root.mainloop()
