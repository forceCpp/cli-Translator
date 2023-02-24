from translate import Translator
from gtts import gTTS
import playsound
import os

def opt():
    print("""

    Supported languages:
        
            af - Afrikaans
            sq - Albanian
            ar - Arabic
            hy - Armenian
            bn - Bengali
            bs - Bosnian
            bg - Bulgarian
            ca - Catalan
            hr - Croatian
            cs - Czech
            da - Danish
            nl - Dutch
            en - English
            eo - Esperanto
            et - Estonian
            tl - Filipino
            fi - Finnish
            fr - French
            gl - Galician
            de - German
            el - Greek
            gu - Gujarati
            hi - Hindi
            hu - Hungarian
            is - Icelandic
            id - Indonesian
            ga - Irish
            it - Italian
            ja - Japanese
            jv - Javanese
            kn - Kannada
            kk - Kazakh
            km - Khmer
            ko - Korean
            ku - Kurdish
            ky - Kyrgyz
            lo - Lao
            lv - Latvian
            lt - Lithuanian
            lb - Luxembourgish
            mk - Macedonian
            ml - Malayalam
            mr - Marathi
            mn - Mongolian
            my - Burmese
            ne - Nepali
            no - Norwegian
            pl - Polish
            pt - Portuguese
            pa - Punjabi
            ro - Romanian
            ru - Russian
            sr - Serbian
            sd - Sindhi
            si - Sinhalese
            sk - Slovak
            sl - Slovenian
            so - Somali
            es - Spanish
            su - Sundanese
            sw - Swahili
            sv - Swedish
            ta - Tamil
            te - Telugu
            th - Thai
            tr - Turkish
            uk - Ukrainian
            ur - Urdu
            uz - Uzbek
            vi - Vietnamese
            cy - Welsh
            xh - Xhosa
            yi - Yiddish
            yo - Yoruba
            zu - Zulu

        """)

text = input("enter the text that you want to translate: ")

opt()

input_lang = input("enter the language of the text: ")
output_lang = input("enter the language you want to translate to: ")

translator = Translator(from_lang=input_lang, to_lang=output_lang)
translate = translator.translate(text)

print(f"""

translated text: , {translate}

""")


audioplay = input("do you want to play the audio? (y/n): ")
if audioplay == "y" or audioplay == "Y":
    tts = gTTS(text=translate, lang=output_lang, slow=True)
    tts.save("audio.mp3")
    playsound.playsound("audio.mp3")
    os.remove("audio.mp3")
else:
    print("")