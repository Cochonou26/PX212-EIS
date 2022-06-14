import time
from easygopigo3 import EasyGoPiGo3
import math
import numpy as n
from client import *
import re

host, port = ('192.168.1.10', 12345) # port, host


def transfert_data(data): # GBP et GTP
    
    import socket
    socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM) #paramétrage de la connexion
    try:
        
        socket.connect((host,port))  #ouverture de la connexion
        #print("Client connecté") 
        data=data.encode("utf8")   #encoder la data
        socket.sendall(data)     #envoie des données sur le serveur
        recept=socket.recv(1024)  #reception de la donnée
        recept.decode("utf8")   #decode utf8
        
        
        recept=str(recept)  #conversion en string
        recept=re.sub("b|'","",recept) #suppression b,'
        recept=recept.split(", ")  #séparation tableau
                
        recept[0]=float(recept[0]) #conversion en float
        recept[1]=float(recept[1])
        
        return recept    
            
    except:
        print("Connexion serveur échouée")

    finally:
        socket.close()

def allow_mouv():#GSS
    import socket
    socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM) #paramétrage de la connexion
    try:
        data="GSS"
        socket.connect((host,port))  #ouverture de la connexion
        #print("Client connecté") 
        data=data.encode("utf8")   #encoder la data
        socket.sendall(data)     #envoie des données sur le serveur
        recept=socket.recv(1024)  #reception de la donnée
        recept.decode("utf8")   #decode utf8
                       
        return recept
    
    except:
        print("Connexion serveur échouée")

    finally:
        socket.close()
 

def mouvement():
    my_gopigo = EasyGoPiGo3()
    position1=transfert_data("GBP")
    position_cible=transfert_data("GTP")
    
    #mouvements#
    while(position1!=position_cible):
        
        position_cible=transfert_data("GTP")
        position1=transfert_data("GBP")
        my_gopigo.drive_cm(5)
        position2=transfert_data("GBP")
  

        # rapport pixel/cm
        a=abs(position2[1]-position1[1])
        b=abs(position2[0]-position1[0])
        hypothenuse0=((a)**2+(b)**2)**0.5
        if (hypothenuse0==0) :
            rapport=0
        else:
            rapport = 5/hypothenuse0

        #en bas a droite de la cible
        if(position1[0]>position_cible[0] and position1[1]<position_cible[1]):
          #si on va a droite
            if(position2[0]>position1[0]):
                a=(position2[1]-position1[1])
                b=(position2[0]-position1[0])
                angle1=n.arctan(abs(a/b))
                my_gopigo.turn_degrees(angle1+180)
                c=position_cible[1]-position2[1]
                d=position_cible[0]-position2[0]
                angle2=n.arctan(abs(c/d))
                my_gopigo.turn_degrees(90-angle2)
                hypothenuse=((c)**2+(d)**2)**0.5
                my_gopigo.drive_cm(hypothenuse*(rapport))
             
          #si on va a gauche
            elif (position2[0]<position1[0]):
                angle1=n.arctan(abs(a/b))
                my_gopigo.turn_degrees(angle1)
                c=position_cible[1]-position2[1]
                d=position_cible[0]-position2[0]
                angle2=n.arctan(abs(c/d))
                my_gopigo.turn_degrees(90-angle2)
                hypothenuse=((c)**2+(d)**2)**0.5
                my_gopigo.drive_cm(hypothenuse*(rapport))

      
      # en bas a gauche de la cible
        elif(position1[0]<position_cible[0] and position1[1]<position_cible[1]):
        
          #si on va a droite
            if(position2[0]>position1[0]):
                a=(position2[1]-position1[1])
                b=(position2[0]-position1[0])
                angle1=n.arctan(abs(a/b))
                my_gopigo.turn_degrees(-angle1)
                c=position_cible[1]-position2[1]
                d=position_cible[0]-position2[0]
                angle2=n.arctan(abs(c/d))
                my_gopigo.turn_degrees(-angle2)
                hypothenuse=((c)**2+(d)**2)**0.5
                my_gopigo.drive_cm(hypothenuse*(rapport))
      
          #si on va a gauche
            elif (position2[0]<position1[0]):
                angle1=n.arctan(abs(a/b))
                my_gopigo.turn_degrees(-angle1)
                c=position_cible[1]-position2[1]
                d=position_cible[0]-position2[0]
                angle2=n.arctan(abs(c/d))
                my_gopigo.turn_degrees(180-angle2)
                hypothenuse=((c)**2+(d)**2)**0.5
                my_gopigo.drive_cm(hypothenuse*(rapport))


      # en haut a droite de la cible
        elif(position1[0]>position_cible[0] and position1[1]>position_cible[1]):
                       

          #si on va a droite
            if(position2[0]>position1[0]):
                a=(position2[1]-position1[1])
                b=(position2[0]-position1[0])
                angle1=n.arctan(abs(a/b))
                my_gopigo.turn_degrees(-18-angle1)
                c=position_cible[1]-position2[1]
                d=position_cible[0]-position2[0]
                angle2=n.arctan(abs(c/d))
                my_gopigo.turn_degrees(-90+angle2)
                hypothenuse=((c)**2+(d)**2)**0.5
                my_gopigo.drive_cm(hypothenuse*(rapport))

      
          #si on va a gauche
            elif (position2[0]<position1[0]):
                angle1=n.arctan(abs(a/b))
                my_gopigo.turn_degrees(-angle1)
                c=position_cible[1]-position2[1]
                d=position_cible[0]-position2[0]
                angle2=n.arctan(abs(c/d))
                my_gopigo.turn_degrees(-90+angle2)
                hypothenuse=((c)**2+(d)**2)**0.5
                my_gopigo.drive_cm(hypothenuse*(rapport))
      
    #en haut a gauche de la cible
        elif(position1[0]<position_cible[0] and position1[1]>position_cible[1]):
    
          #si on va a droite
            if(position2[0]>position1[0]):
                a=(position2[1]-position1[1])
                b=(position2[0]-position1[0])
                angle1=n.arctan(abs(a/b))
                my_gopigo.turn_degrees(angle1)
                c=position_cible[1]-position2[1]
                d=position_cible[0]-position2[0]
                angle2=n.arctan(abs(c/d))
                my_gopigo.turn_degrees(90-angle2)
                hypothenuse=((c)**2+(d)**2)**0.5
                my_gopigo.drive_cm(hypothenuse*(rapport))
             
      
          #si on va a gauche
            elif (position2[0]<position1[0]):
                angle1=n.arctan(abs(a/b))
                my_gopigo.turn_degrees(180+angle1)
                c=position_cible[1]-position2[1]
                d=position_cible[0]-position2[0]
                angle2=n.arctan(abs(c/d))
                my_gopigo.turn_degrees(angle2)
                hypothenuse=((c)**2+(d)**2)**0.5
                my_gopigo.drive_cm(hypothenuse*(rapport))

        else :
            print("WTF my guy")



print(transfert_data("GBP"))
print(transfert_data("GTP"))
mouvement()