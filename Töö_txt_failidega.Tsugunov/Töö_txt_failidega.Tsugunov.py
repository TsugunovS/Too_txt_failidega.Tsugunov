from module1 import *
laused=["Tere tulemast"]

while True:
    v=int(input("1-Loeme failist\n2-Salvestame failisse\n3-Tekst helisse\n4-Tõlgi eesti või vene keelde\n"))
    if v==1:
        laused=Loe_failist("Laused.txt")
        for line in laused:
            print(line)
    elif v==2:
        line=input("Lisa lause: ")
        laused.append(line)
        Kirjuta_failisse("Laused.txt",laused)
    elif v==3:
        text=""
        for line in laused:
            text=text+" "+line
        #text : kõik elemendis järjendis
        ind=int(input("Number:"))
        Heli(laused[ind],'et')
    elif v==4:
        choice=input("1 Перевод с эстонского на русский.\n2 Перевод с русского на эстонский. ")
    if choice == 1:
        est_words = []
        rus_words = []
        with open("est.txt", "r") as file:
            for line in file:
                est, rus = line.strip().split(':')
                est_words.append(est)
                rus_words.append(rus)
        est_word = input('Введите слово на эстонском: ')
        rus_word = est_to_rus(est_word, est_words, rus_words)
            
            


    


