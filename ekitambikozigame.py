playerone=""
playertwo=""
playerthree=""

herdone=10
herdtwo=12
herdthree=14

cows = [herdone,herdtwo,herdthree]
players = [playerone,playertwo,playerthree]

playerone_index = 0
playertwo_index = 0
playerthree_index = 0

print("welcome to ekitanbikkozi game")

userplayer = input("which of the players one,two three are you picking")

for eachplayer in players:
    if userplayer == "1" and playerone_index <= playertwo_index:
        
        
        print("PLAYER 1 these are the herds to pick from")
        print("HERDONE "+str(herdone))
        print("HERDTWO "+str(herdtwo))
        print("HERDTHREE "+str(herdthree))
        selectedherd= input("select from the herd")

        if selectedherd=="1":
                playerherd =input("PLAYER 1 how many cows are you taking from herd one:"+str(herdone))
                herdone=int(herdone)-int(playerherd)
                print(herdone)
                playerone_index+=1
        if int(herdone) ==0 and int(herdtwo)==0 and int(herdthree)==0:
                    print("playerone wins please take Wendy")
                    exit()

        elif selectedherd=="2":
            playerherd =input("PLAYER 1 how many cows are you taking from herd two:"+str(herdtwo))
            herdtwo=int(herdtwo)-int(playerherd)
            print(herdtwo)
            playerone_index+=1
        if int(herdone) ==0 and int(herdtwo)==0 and int(herdthree)==0:
                 print("playerone wins please take Wendy")
                 exit()
                 


        elif selectedherd =="3":
            playerherd =input("PLAYER 1 how many cows are you taking from herd three:"+str(herdthree))
            herdthree=int(herdthree)-int(playerherd)
            print(herdthree)
            playerone_index+=1

        if int(herdone) ==0 and int(herdtwo)==0 and int(herdthree)==0:
                    print("playerone is the winner please take Wendy")
                    exit()
    
            

    if playertwo_index >= playerthree_index:
        
    
        print("PLAYER 2 these are the herds to pick from")
        print("HERDONE "+str(herdone))
        print("HERDTWO "+str(herdtwo))
        print("HERDTHREE "+str(herdthree))
        selectedherd= input("select from the herd")

        if selectedherd=="1":
                playerherd =input("PLAYER 2  how many cows are you taking from herd one:"+str(herdone))
                herdone=int(herdone)-int(playerherd)
                print(herdone)
                playertwo_index+=1
        if int(herdone) ==0 and int(herdtwo)==0 and int(herdthree)==0:
                    print("playertwo wins please take Wendy")
                    exit()

        elif selectedherd=="2":
            playerherd =input("PLAYER 2  how many cows are you taking from herd two:"+str(herdtwo))
            herdtwo=int(herdtwo)-int(playerherd)
            print(herdtwo)
            playertwo_index+=1
        if int(herdone) ==0 and int(herdtwo)==0 and int(herdthree)==0:
                    print("playertwo wins please take Wendy")
                    exit()


        elif selectedherd =="3":
            playerherd =input("PLAYER 2  how many cows are you taking from herd three:"+str(herdthree))
            herdthree=int(herdthree)-int(playerherd)
            print(herdthree)
            playertwo_index+=1
        if int(herdone) ==0 and int(herdtwo)==0 and int(herdthree)==0:
                    print("playertwo is the winner please take Wendy")
                    exit()



    if playerthree_index < playertwo_index and playerone_index:
    
 
     print("PLAYER 3  these are the herds to pick from")
     print("HERDONE "+str(herdone))
     print("HERDTWO "+str(herdtwo))
     print("HERDTHREE "+str(herdthree))
     selectedherd= input("select from the herd")

     if selectedherd=="1":
            playerherd =input("PLAYER 3 how many cows are you taking from herd one:"+str(herdone))
            herdone=int(herdone)-int(playerherd)
            print(herdone)
            playerthree_index+=1
     if int(herdone) ==0 and int(herdtwo)==0 and int(herdthree)==0:
                  print("playerthree wins please take Wendy")
                  exit()

     elif selectedherd=="2":
           playerherd =input("PLAYER 3 how many cows are you taking from herd two:"+str(herdtwo))
           herdtwo=int(herdtwo)-int(playerherd)
           print(herdtwo)
           playerthree_index+=1
     if int(herdone) ==0 and int(herdtwo)==0 and int(herdthree)==0:
                  print("playerthree wins please take Wendy")
                  exit()


     elif selectedherd =="3":
           playerherd =input("PLAYER 3 how many cows are you taking from herd three:"+str(herdthree))
           herdthree=int(herdthree)-int(playerherd)
           print(herdthree)
           playerthree_index+=1
     if int(herdone) ==0 and int(herdtwo)==0 and int(herdthree)==0:
                  print("playerthree is the winner please take Wendy")
                  exit()




           





    
        


    


    



    
    
