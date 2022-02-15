import sys
import random
file=open("ListaslowENG.txt")
count = len(open("ListaslowENG.txt", 'rU').readlines())
print(count)
slowa=[]
words = [line.strip() for line in file.readlines()]
i=random.randint(0,(count-1))
word=words[i]
print(word)
print(i)

#word=random.choice(words)
no_of_tries=5
used_letters=[]
your_answer=[]
j=len(word)
for i in range(0,j):
    your_answer.append("_")

def pobieram_dane_z_pliku():	
	file=open("Lista slow.txt")
	for line in file.readlines():
		words.append(line.strip)
		
while True:
    letter=input("Podaj litere: ")
    try:
        inti=int(letter)
        print("Miała być litera")
    except(ValueError):    
            if len(letter)>1:
                print("To miała być jedna litera")
            else:
                try:
                    no=used_letters.index(letter)
                    if(no>=0):
                        print("Litera: '"+letter+"'"+ " już była!")
                        print(used_letters)    
                except(ValueError):
                    used_letters.append(letter)
                    
                    for i in range(0,j):
                        try:
                            correct=word.index(letter)
                            if (word[i]==letter):
                                your_answer[i]=letter
                                #"".join(your_answer)
                        except(ValueError):
                            print("\nZła odpowiedz\n")
                            no_of_tries=no_of_tries -1
                            break
                    c="".join(your_answer)
                    if(c==word):
                        print("Gratulacje ! To jest ten wyraz!: "+word)
                        sys.exit(0)
                    if(no_of_tries<=0):
                        while True:
                            print("Niestety nie zgadłeś. Chcesz spróbować ponownie ? 0/1")
                            try:
                                dec=int(input("""Wybierz 
                                0-NIE
                                1-TAK : """))
                                if(dec==0):
                                    print("Wyraz którego nie zgadnąłeś to: '"+word+ "'")
                                    print("Do widzenia")
                                    sys.exit(0)
                                if(dec!=1 or dec==0):
                                    print("Nie właściwa odpowiedz. Do widzenia")
                                    sys.exit(0)
                                else:
                                    no_of_tries=5
                                    break
                            except(ValueError):
                                print("Wybór był 0/1")
    print("Twoje odpowiedzi:  "+str(" ".join(your_answer)))
    print("Litery które użyłeś: "+ str(used_letters))                    
    print("Pozostało szans: "+str(no_of_tries)+"\n")