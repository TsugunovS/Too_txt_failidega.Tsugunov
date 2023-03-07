from module1 import *
laused=["Tere tulemast"] #bbb
text_est = Loe_failist('est.txt')
text_rus = Loe_failist('rus.txt')
while True:
    v=int(input("1-Loeme failist\n2-Salvestame failisse\n3-Tekst helisse\n4-Tõlgi eesti või vene keelde\n6-5 4 3"))
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
        est_word = input("Введите слово на эстонском: ")
        rus_word = est_to_rus(est_word, est_words, rus_words)
        if rus_word:
            print("Перевод слова {est_word} на русский: {rus_word}")
        else:
            print(f"Слово {est_word} не найдено в словаре.")

    elif v==5:
        rus_words, est_words = ("rus-est.txt")
        rus_word = input("Введите слово на русском: ")
        est_word = rus_to_est(rus_word, rus_words, est_words)
        if est_word is not None:
            print(f"Перевод слова {rus_word} на эстонский: {est_word}")
        else:
            print(f"Слово {rus_word} не найдено в словаре.")

    elif v==6:
        est = ["Tere", "Auto", "Õun"]
        rus = ["Привет", "Машина", "Яблоко"]
        hinne = Teadmiste_kontroll(rus, est)
        print(est)
        print(rus)
        print(hinne)
            


    


