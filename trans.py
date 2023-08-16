import tkinter as tk
from tkinter import (
                        Label,
                        Button,
                        messagebox,
                        Menubutton,
                        Radiobutton,
                        Frame,
                        Tk,
                        StringVar,
                        OptionMenu,
                        Text,
                        ttk
                    )

# from translate import Translator
from googletrans import Translator



class TranslateLang(object):
    def __init__(self, root) -> None:
        
        self.frames=[]
        self.LanguageChoices={'afrikaans': 'af',
    'albanian': 'sq',
    'amharic': 'am',
    'arabic': 'ar',
    'armenian': 'hy',
    'azerbaijani': 'az',
    'basque': 'eu',
    'belarusian': 'be',
    'বাংলা': 'bn',
    'bosnian': 'bs',
    'bulgarian': 'bg',
    'catalan': 'ca',
    'cebuano': 'ceb',
    'chichewa': 'ny',
    'chinese': 'zh',
    'corsican': 'co',
    'croatian': 'hr',
    'czech': 'cs',
    'danish': 'da',
    'dutch': 'nl',
    'english': 'en',
    'esperanto': 'eo',
    'estonian': 'et',
    'filipino': 'tl',
    'finnish': 'fi',
    'french': 'fr',
    'frisian': 'fy',
    'galician': 'gl',
    'georgian': 'ka',
    'german': 'de',
    'greek': 'el',
    'gujarati': 'gu',
    'haitian creole': 'ht',
    'hausa': 'ha',
    'hawaiian': 'haw',
    'hebrew': 'iw',
    'hindi': 'hi',
    'hmong': 'hmn',
    'hungarian': 'hu',
    'icelandic': 'is',
    'igbo': 'ig',
    'indonesian': 'id',
    'irish': 'ga',
    'italian': 'it',
    'japanese': 'ja',
    'javanese': 'jw',
    'kannada': 'kn',
    'kazakh': 'kk',
    'khmer': 'km',
    'kinyarwanda': 'rw',
    'korean': 'ko',
    'kurdish': 'ku',
    'kyrgyz': 'ky',
    'lao': 'lo',
    'latin': 'la',
    'latvian': 'lv',
    'lithuanian': 'lt',
    'luxembourgish': 'lb',
    'macedonian': 'mk',
    'malagasy': 'mg',
    'malay': 'ms',
    'malayalam': 'ml',
    'maltese': 'mt',
    'maori': 'mi',
    'marathi': 'mr',
    'mongolian': 'mn',
    'myanmar': 'my',
    'burmese': 'my',
    'nepali': 'ne',
    'norwegian': 'no',
    'odia': 'or',
    'pashto': 'ps',
    'persian': 'fa',
    'polish': 'pl',
    'portuguese': 'pt',
    'punjabi': 'pa',
    'romanian': 'ro',
    'russian': 'ru',
    'samoan': 'sm',
    'scots gaelic': 'gd',
    'serbian': 'sr',
    'sesotho': 'st',
    'shona': 'sn',
    'sindhi': 'sd',
    'sinhala': 'si',
    'slovak': 'sk',
    'slovenian': 'sl',
    'somali': 'so',
    'spanish': 'es',
    'sundanese': 'su',
    'swahili': 'sw',
    'swedish': 'sv',
    'tajik': 'tg',
    'tamil': 'ta',
    'telugu': 'te',
    'thai': 'th',
    'turkish': 'tr',
    'ukrainian': 'uk',
    'urdu': 'ur',
    'uyghur': 'ug',
    'uzbek': 'uz',
    'vietnamese': 'vi',
    'welsh': 'cy',
    'xhosa': 'xh',
    'yiddish': 'yi',
    'yoruba': 'yo',
    'zulu': 'zu'}
        
      
    def opt_ch(self) -> None:
        opt=option.get()
        # print(opt)
        if(opt=="Manual"):
            # self.in_lan.pack()
            self.sel2.forget()
            self.sel1.pack(side="left")
            self.sel2.pack(side="left")
        else:
            self.sel2.pack(side="left")
            self.sel1.forget()
    def frm_destroy(self):
        for frem in self.frames:
            frem.destroy()
        option.set(None)
        self.creat_widage()

    def creat_frm(self):
        m=Frame(root)
        m.pack()
        return m
    
    def creat_widage(self):
        # print("LLLL")
        f1=self.creat_frm()
        self.frames.append(f1)
        self.in_lan=StringVar()
        self.out_lang=StringVar()
        self.in_lan.set("Select Input Language")
        self.out_lang.set("Select Output Language")
        self.sel1=OptionMenu(f1,self.in_lan,*self.LanguageChoices)
        self.sel2=OptionMenu(f1,self.out_lang,*self.LanguageChoices)
        in_f=self.creat_frm()
        self.frames.append(in_f)
        lab1=Label(in_f,text="Enter text",)
        lab1.pack(side="left")
        self.input=Text(in_f,height=5, width=40, font=('Times', 12, 'bold'))
        self.input.pack(side="left")
        bt_f=self.creat_frm()
        self.frames.append(bt_f)
        btn1=Button(bt_f,text="Translate",width=25,height=2)
        btn1.pack(side="left",padx=9,pady=10)
        btn2=Button(bt_f,text="Reset",width=25,height=2,command=self.frm_destroy)
        btn2.pack(side="left",padx=9,pady=10)
        out_f=self.creat_frm()
        self.frames.append(out_f)
        lab2=Label(out_f,text="Output text").pack(side='left')
        self.out_text=Text(out_f,height=5, width=40, font=('Times', 12, 'bold'))
        self.out_text.pack(padx=6,pady=6)
        btn1.config(command=self.prtranslate)
    def prtranslate(self):
        in_lan=self.in_lan.get().lower()
        out_lan=self.out_lang.get().lower()
        # print(in_lan,out_lan)
        text = self.input.get("1.0", "end-1c")
        
        if in_lan in self.LanguageChoices:
            in_lan=self.LanguageChoices[in_lan]
            # print(in_lan)
        else:
            in_lan="auto"
        
        if out_lan not in self.LanguageChoices:
            messagebox.Message("Invalid destination language!!!")
        else:
            out_lan=self.LanguageChoices[out_lan]
        
        translated_text=self.translateor(text=text,dest=out_lan,src=in_lan)

        self.out_text.delete("1.0",tk.END)
        out_text=f"{translated_text.text} \npronunciation: {translated_text.pronunciation} " 
        self.out_text.insert("1.0", out_text)

    def translateor(self,text, dest, src):
        #
        translator=Translator()
        translated_text = translator.translate(text, dest,src)
        # print(translated_text)
            
        return translated_text
            
            
           
        




root = Tk()
root.title("Language Translator")
root.geometry("510x400")
root.resizable(0,0)

if __name__ == '__main__':
    f1 = Frame(root)
    f1.pack()
    option = StringVar()
    option1 = Radiobutton(
                            f1,
                            text="Auto",
                            variable=option,
                            value="Auto",
                            font=10
                        )
    option1.pack(side='left')
    option2=Radiobutton(f1,text="Manual",variable=option,value="Manual",font=10)
    option2.pack(side="left")

    option.set(None)
    m = TranslateLang(root=root)
    m.creat_widage()
    option1.config(command=m.opt_ch)
    option2.config(command=m.opt_ch)
    root.mainloop()
