from moduleOma import*

ballid= []
tudengid= []

tudeng_listisse(ballid,tudengid)



while (True):
    print("--------------------------")
    print("0-Узнать список поступивших в вуз людей \n1-Отобразить в алфавитном порядке список людей и их баллы \n2-Найти n людей с худшими результатами \n3-Найти средний балл поступивших \n4-Свой вариант задаем количество поступивших с максимальными результатами и выводим их баллы и имена \n5 - Выход.")

    v = int(input())

    if v==0:
        naitame_Tudengid(ballid, tudengid)
              
    elif v==1:
        abc_Jarjekord(ballid, tudengid)

    elif v==2:
        
        minimaalne_Hinne(ballid, tudengid)
      
    elif v==3:

        keskmineBall(ballid)
    
    elif v==4:

        ballide_Jarjekorras(ballid, tudengid)

    elif v==5:
    
        break
    
