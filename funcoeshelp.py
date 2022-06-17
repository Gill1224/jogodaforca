import os
import random

def clean():
    os.system("cls")

def letrasacertadas(palavra):     
    return ["_" for letra in palavra]

def letrasvazias(item):
    return item.upper().replace(" ","")

def checkletra(palavra):
    while not palavra.isalpha():
        print("\nah?? , Sabe oque é uma Letra ?!!\n")
        palavra = str(input("Diga qual é a palavra: "))
    return palavra.upper()

def dieguy(erros):
    print("  _____     ")
    print("  |/  °  ")

    if(erros == 1):
        print ("  |   (x_x) ")
        print ("  |     |   ")
        print ("  |         ")
        print ("  |         ")

    if(erros == 2):
        print ("  |   (x_x) ")
        print ("  |    /|\  ")
        print ("  |         ")
        print ("  |         ")

    if(erros == 3):
        print ("  |   (x_x) ")
        print ("  |    /|\  ")
        print ("  |     |   ")
        print ("  |         ")

    if(erros == 4):
        print ("  |   (x_x) ")
        print ("  |    /|\  ")
        print ("  |     |   ")
        print ("  |    / \  ") 
        print ("  |         ")
        print ("__|___      ")

    if(erros == 5):
        print ("            ")
        print ("   X    X   ")
        print ("     /_     ")
        print ("    _____   ") 
        print ("            ")          
        print ("    MORRI   ") 

    print()  
