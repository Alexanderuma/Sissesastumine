def tudeng_listisse(b:list, t:list):
    '''Funkcija zaprashivaet kakoe kolichestvo postupivshih vnesti. Dobovljaet studentov i ih bally v spiski.'''
    
    n=int(input("Mitu sisseastujaid lisame? "))
    print() # otstup

    for j in range(n):
        nimi=input("Nimi: ")
        t.append(nimi)
       
        ball=input("Ballid: ")
        b.append(ball)
        
        print() # otstup
    
    print(t) 
    print(b) 

    return b,t
   


def naitame_Tudengid(b:list, t:list):
    '''Funkcija, kotoraja zaprasjhivaet kakoe kolichestvo postupivshih my hotim uvidet'. I vyvodit spisok postupivshi s ih ballami na ekran.'''
    
    print("Sisseastujate arv on:", len(t))
     
    n=int(input("Mitu inimesi naitame? "))
    print() # otstup

    for j in range(n):
        print(t[j], b[j])



def abc_Jarjekord(b:list,t:list):
    '''Funkcija otobrazhaet v alfavitnom porjadke spisok ljudei i ih bally.'''

    newList=[]
    n = len(t)
    ind = 0

    for i in range(n):
        unitedList = t[ind] +' '+ b[ind]
        newList.append(unitedList)
        ind+=1

    newList.sort()

    print() # otstup
    
    for j in range(n):
        
        print(newList[j])



def minimaalne_Hinne(b:list, t:list):
    '''Funkcija nahodit studenta s hudshimi ballami'''

    print() # otstup
    b=list(map(int,b))
    minHinne=min(b)

    n=b.index(minHinne)
 
    print(f"Halvem tulemus: {minHinne}")

    nimi=t[n]
    print(f"Tudeng halvema tulemusega: {nimi}")  

    

def keskmineBall(b:list):
    '''Funkcija nahodit srednij ball vseh postupivshih'''

    print() # otstup
    summa=0
    for ballid in b:
        summa+=int(ballid)
    summa/=len(b)
    print("Keskmine tulemus: ", round(summa,1))



def ballide_Jarjekorras(b:list, t:list):
    '''Funckija vyvodit spisok ballov ot bol'shego k men'shemu''' 
       
    print() # otstup
    pos = 1 

    for x in range(len(b)):
        
        c=list(map(int,b)) #Sozdaet novyj spisok chisel s INTovym znacheniem
        maxHinne=max(c)
        
        n=c.index(maxHinne)
        #(t[n]) - index studenta v spiske

        print(f"{pos}. parim ballide tulemus on: {maxHinne} sisseastuja: {t[n]}") 
       
        b.pop(n) #Udaljaet nasovsem iz spiska po indexu
        t.pop(n)
        pos+=1
        
