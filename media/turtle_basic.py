#!/usr/bin/env python3

# on a besoin du module turtle
import turtle

# On commence par définir une fonction qui dessine un carré de coté `length`

def square(length):
    "have the turtle draw a square of side <length>"
    for side in range(4):
        turtle.forward(length)
        turtle.left(90)

# Maintenant on commence par initialiser la tortue
turtle.reset()

# On peut alors dessiner notre carré
square(200)

# Et pour finir on attend que l'utilisateur clique dans la fenêtre de la tortue, et alors on termine
turtle.exitonclick()

