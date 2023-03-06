def Loe_failist(fail:str)->list:
    """fail-указываем нужный файл, r-читает список
    """
    f=open(fail,'r',encoding="utf-8-sig")
    jarjend=[]
    for rida in f:
        jarjend.append(rida.strip())
        f.close()
        return jarjend
def Kirjuta_failisse(fail:str,jarjend:list):
    f=open(fail,'w',encoding="utf-8-sig")
    for line in jarjend:
        f.write(line+'\n')
        f.close()

from gtts import gTTS
import os
def Heli(text:str,keel:str):
    obj=gTTS(text=text,lang=keel,slow=False).save("heli.mp3")
    os.system("heli.mp3")

def est_to_rus(word, est_words, rus_words):
    with open('est.txt', 'r') as file:
        for line in file:
            est, rus = line.strip().split(':')
            if word == est:
                return rus
    return None



