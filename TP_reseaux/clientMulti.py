import socket 
import select
import time
import sys


#creation de la socket puis connexion
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1",int(sys.argv[1])))


while 1:
  msg = raw_input('>> ')

  # test pour arreter le client python proprement
  if msg=="": # si on initialise pas msg avec raw_input : comme on utilise NC et pas telnet sur les machines BIM il faut mettre if msg=="\n" pour que ca fonctionne 
  # mais la comme on initialise raw_input c'est bon puisque raw_input renvoi une chaine vide quand on tape entree
    break

  # envoi puis reception de la reponse
  s.send(msg)
  data = s.recv(255)
  print data # on affiche la reponse

# fermeture de la connexion
s.close()
print "fin du client TCP"
