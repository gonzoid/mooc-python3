
# coding: utf-8

# <style>div.title-slide {    width: 100%;    display: flex;    flex-direction: row;            /* default value; can be omitted */    flex-wrap: nowrap;              /* default value; can be omitted */    justify-content: space-between;}</style><div class="title-slide">
# <span style="float:left;">Licence CC BY-NC-ND</span>
# <span>Thierry Parmentelat &amp; Arnaud Legout</span>
# <span><img src="media/both-logos-small-alpha.png" style="display:inline" /></span>
# </div>

# # Les mots-clés de python

# ### Mots réservés

# Il existe en python certains mots spéciaux, qu'on appelle des mots-clés, ou *keywords* en anglais, qui sont réservés et **ne peuvent pas être utilisés** comme identifiants, c'est-à-dire comme un nom de variable.

# C'est le cas par exemple pour l'instruction `if`, que nous verrons prochainement, qui permet bien entendu d'exécuter tel ou tel code selon le résultat d'un test.

# In[ ]:


variable = 15
if variable <= 10:
    print("en dessous de la moyenne")
else:
    print("au dessus")


# À cause de la présence de cette instruction dans le langage, il n'est pas autorisé d'appeler une variable `if`.

# In[ ]:


# interdit, if est un mot-clé
if = 1


# ### Liste complète

# Voici la liste complète des mots-clés:

# | |  |  |  |  |
# |--------|----------|---------|----------|--------|
# | **False**  | class    | finally | is       | return |
# | **None**   | continue | for     | lambda   | try    |
# | **True**   | def      | from    | **nonlocal** | while  |
# | and    | del      | global  | not      | with   |
# | as     | elif     | if      | or       | yield  |
# | assert | else     | import  | pass     |        |
# | break  | except   | in      | raise    |        |
# 

# Nous avons indiqué en gras les nouveautés par rapport à python-2  (sachant que réciproquement `exec` et `print` ont perdu leur statut de mot-clé depuis python-2, ce sont maintenant des fonctions).

# Il vous faudra donc y prêter attention, surtout au début, mais avec un tout petit peu d'habitude vous saurez rapidement les éviter. 
# 
# Vous remarquerez aussi que tous les bons éditeurs de texte supportant du code Python vont colorer les mots-clés différemment des variables. Par exemple, IDLE colorie les mots-clés en orange, vous pouvez donc très facilement vous rendre compte que vous allez, par erreur, en utiliser un comme nom de variable.
# 
# Cette fonctionalité de *coloration syntaxique* permet d'identifier d'un coup d'oeil (grâce à un code de couleur) le rôle des différents éléments de votre code (variable, mots-clés, etc.) D'une manière générale, nous vous déconseillons fortement d'utiliser un éditeur de texte qui n'offre pas cette fonctionalité de coloration syntaxique.

# ### Pour en savoir plus

# On peut se reporter à cette page
# 
# https://docs.python.org/3/reference/lexical_analysis.html#keywords
