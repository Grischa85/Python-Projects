import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from googletrans import Translator
import speech_recognition as sr




class translator_window:
    def __init__(self, root):
        self.root = root
        # Change the title
        self.root.title("Übersetzer")
        # Change the window size
        self.root.geometry("710x400")
        # no resize for both directions
        self.root.resizable(False, False)
        # Change icon
        self.root.iconbitmap('')

        # setting up combo boxes
        Cb_autoDetect = ttk.Combobox(
            self.root, width=20, font=('verdana', 11))
        Cb_autoDetect['values'] = ('Auto Erkennung',)
        Cb_autoDetect.place(x=30, y=30)
        Cb_autoDetect.current(0)

        self.cb_choose_langauge = ttk.Combobox(
            self.root, width=20, font=('verdana', 11))
        self.cb_choose_langauge['values'] = (
            'Afrikaans',
            'Albanian',
            'Arabic',
            'Armenian',
            'Basque',
            'Belarusian',
            'Bengali',
            'Bosnian',
            'Bulgarian',
            'Cebuano',
            'Chichewa',
            'Corsican',
            'Croatian',
            'Danish',
            'Dutch',
            'English',
            'Esperanto',
            'Estonian',
            'Filipino',
            'Finnish',
            'French',
            'Frisian',
            'Galician',
            'Georgian',
            'German',
            'Greek',
            'Gujarati',
            'Haitian Creole',
            'Hausa',
            'Hawaiian',
            'Hebrew',
            'Hindi',
            'Hmong',
            'Hungarian',
            'Icelandic',
            'Igbo',
            'Indonesian',
            'Irish',
            'Italian',
            'Japanese',
            'Javanese',
            'Kannada',
            'Kazakh',
            'Khmer',
            'Kinyarwanda',
            'Korean',
            'Kurdish',
            'Kyrgyz',
            'Lao',
            'Latin',
            'Latvian',
            'Lithuanian',
            'Luxembourgish',
            'Macedonian',
            'Malagasy',
            'Malay',
            'Malayalam',
            'Maltese',
            'Maori',
            'Marathi',
            'Mongolian',
            'Myanmar',
            'Nepali',
            'Norwegian'
            'Odia',
            'Pashto',
            'Persian',
            'Polish',
            'Portuguese',
            'Punjabi',
            'Romanian',
            'Russian',
            'Samoan',
            'Scots Gaelic',
            'Serbian',
            'Sesotho',
            'Shona',
            'Sindhi',
            'Sinhala',
            'Slovak',
            'Slovenian',
            'Somali',
            'Spanish',
            'Sundanese',
            'Swahili',
            'Swedish',
            'Tajik',
            'Tamil',
            'Tatar',
            'Telugu',
            'Thai',
            'Turkish',
            'Turkmen',
            'Ukrainian',
            'Urdu',
            'Uyghur',
            'Uzbek',
            'Vietnamese',
            'Welsh',
            'Xhosa'
            'Yiddish',
            'Yoruba',
            'Zulu',
        )

        self.cb_choose_langauge.place(x=457, y=30)
        self.cb_choose_langauge.current(0)

        # rest gui widgets
        self.textbox1 = Text(self.root, width=40, height=15,
                             borderwidth=4, font=('verdana', 10), pady=5, relief=RIDGE)

        self.textbox1.place(x=20, y=70)
        self.textbox2 = Text(self.root, width=40, height=15,
                             borderwidth=4, font=('verdana', 10), pady=5, relief=RIDGE)
        self.textbox2.place(x=360, y=70)

        btn_show = Button(self.root, text="Übersetzen", relief=RIDGE, borderwidth=2, font=(
            'verdana', 12, 'bold'), cursor="hand2", command=self.translate, width=10)
        btn_show.place(x=240, y=345)

        btn_clear = Button(self.root, text="Neu", relief=RIDGE, borderwidth=2,
                           font=('verdana', 12, 'bold'), cursor="hand2", command=self.clear, width=8)
        btn_clear.place(x=370, y=345)

        # Microphone Button. Speech to Text
        mic_btn = ttk.Button(self.root, text="MIC", command=self.recordvoice ,cursor="hand2", width=8)
        mic_btn.place(x=290, y=300)

    def translate(self):
        '''takes input from textbox1 translate it and show output through textbox2'''
        txt_input = self.textbox1.get("1.0", "end-1c")
        language = self.cb_choose_langauge.get()

        if txt_input == '':
            messagebox.showerror('Translator - error', 'please fill the box')
        else:
            self.textbox2.delete(1.0, 'end')
            translator = Translator()
            output = translator.translate(txt_input, dest=language)
            self.textbox2.insert('end', output.text)

    def clear(self):
        '''clear textboxes data'''
        self.textbox1.delete(1.0, 'end')
        self.textbox2.delete(1.0, 'end')

    def recordvoice(self):

        while True:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                audio=r.listen(source)
                try:
                    text1 = r.recognize_google(audio, language="de-DE")
                    self.textbox1.insert(tkinter.INSERT, text1)
                    print(text1)
                except:
                    pass
                return text1




# driver code
if __name__ == "__main__":
    root = Tk()
    obj = translator_window(root)
    root.mainloop()
