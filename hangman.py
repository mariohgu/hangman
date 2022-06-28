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

from random import randint


def loadWord():
    word = []
    with open("./files/data.txt","r",encoding="utf-8") as f:
        for line in f:
            word.append(line)
       
    chooseWord = 'servilleta'#word[randint(0,len(word))].rstrip('\n')
    listWord = list(chooseWord)
    print(listWord)
    playerWord = []
    while listWord != playerWord:
        lett = input("Please, give a letter: ")
        if lett not in playerWord:
            for i,j in enumerate(chooseWord):
                if j == lett:
                    playerWord.insert(i,j)
            print (playerWord)
        else:
            print("You already used that letter.")
    print("LO LOGRASTE")    

  



def run():
    loadWord()



if __name__ == '__main__':run()
