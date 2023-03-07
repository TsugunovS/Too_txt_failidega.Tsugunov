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

from random import * 
def Teadmiste_kontroll(rus:list,est:list):
    p=0
    kokku = int(input("Mitu küsimust? "))
    for i in range(kokku):
        järjend=choice([rus,est])
        sõna=choice(järjend)
        print(f"{sõna} - ", end="")
        tõlke=input()
        if sõna in rus:
            i=rus.index(sõna)
            tõlke_kontroll=est[i]
        elif sõna in est:
            i=est.index(sõna)
            tõlke_kontroll=rus[i]
        if tõlke==tõlke_kontroll:
            p+=1
            print("Õige")
        else:
            print("Vale")
    if (p/kokku)*100>90:
        hinne=5
    elif (p/kokku)*100>75:
        hinne=4
    elif (p/kokku)*100>60: 
        hinne=3
    else:
        hinne="Väga halb!"
    return hinne

def load_dict(file_name):
    words1 = []
    words2 = []
    with open(file_name, 'r') as file:
        for line in file:
            word1, word2 = line.strip().split(':')
            words1.append(word1)
            words2.append(word2)
    return words1, words2


def est_to_rus(word, est_words, rus_words):
    try:
        index = est_words.index(word)
        return rus_words[index]
    except print("Vale!"):
        return None 

def rus_to_est(word, rus_words, est_words):
    try:
        index = rus_words.index(word)
        return est_words[index]
    except print("Vale!"):
        return None




