'''
incorpora comprehensions, manejo de errores y manejo de archivos.
utiliza el data
funcion enumerate
metodo get de los diccionarios puede servirte
sentencia("cls") limpiar pantalla
añade puntos
dibujar al ahorcado
mejorar interfaz.
'''

import os
from random import randint


def loadWord():
    word = []
    with open("./files/data.txt","r",encoding="utf-8") as f:
        for line in f:
            word.append(line)       
    chooseWord = word[randint(0,len(word))].rstrip('\n')
    listWord = list(chooseWord)
    playerWord = ["_" for i in range (0,len(chooseWord))]
    
    while listWord != playerWord:
        #os.system('cls')
        lett = input("Please, give me a letter: ")
        if lett not in playerWord:
            for i,j in enumerate(chooseWord):
                if j == lett:
                    playerWord[i]=j
            print (playerWord)
        else:
            print("You are right, but you already used that letter.")
    print("LO LOGRASTE")    

  



def run():
    loadWord()



if __name__ == '__main__':run()
