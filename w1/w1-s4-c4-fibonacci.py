
# coding: utf-8

# <style>div.title-slide {    width: 100%;    display: flex;    flex-direction: row;            /* default value; can be omitted */    flex-wrap: nowrap;              /* default value; can be omitted */    justify-content: space-between;}</style><div class="title-slide">
# <span style="float:left;">Licence CC BY-NC-ND</span>
# <span>Thierry Parmentelat &amp; Arnaud Legout</span>
# <span><img src="../media/both-logos-small-alpha.png" style="display:inline" /></span>
# </div>

# # La suite de Fibonacci (suite)

# ## Complément - niveau intermédiaire

# Nous reprenons le cas de la fonction `fibonacci` que nous avons vue déjà, mais cette fois nous voulons que l'utilisateur puisse indiquer l'entier en entrée de l'algorithme, non plus en répondant à une question, mais sur la ligne de commande, c'est-à-dire en tapant
# 
#     $ python3 fibonacci.py 12

# **Avertissement&nbsp;:** 
# 
# Attention, cette version-ci **ne fonctionne pas dans ce notebook**, justement car on n'a pas de moyen dans un notebook d'invoquer un programme en lui passant des arguments de cette façon. Ce notebook est rédigé pour vous permettre de vous entraîner avec la fonction de téléchargement au format python, qu'on a vue dans la vidéo, et de faire tourner ce programme sur votre propre ordinateur.

# ### Le module `argparse`

# Cette fois nous importons le module `argparse`, c'est lui qui va nous permettre d'interpréter les arguments passés à la ligne de commande.

# In[ ]:


from argparse import ArgumentParser


# Puis nous répétons la fonction `fibonacci`

# In[ ]:


def fibonacci(n):
    "retourne le nombre de fibonacci pour l'entier n"
    # pour les petites valeurs de n il n'y a rien a calculer
    if n <= 1: 
        return 1
    # sinon on initialise f1 pour n-1 et f2 pour n-2
    f2, f1 = 1, 1
    # et on itère n-1 fois pour additionner
    for i in range(2, n + 1):
        f2, f1 = f1, f1 + f2
#        print(i, f2, f1)
    # le résultat est dans f1
    return f1


# *Remarque:* 
# 
# Certains d'entre vous auront évidemment remarqué qu'on aurait pu éviter de copier-coller la fonction `fibonacci` comme cela&nbsp;; c'est à ça que servent les modules, mais nous n'en sommes pas là.

# ### Un objet `parser`

# À présent, nous utilisons le module `argparse`, pour lui dire qu'on attend exactement un argument sur la ligne de commande, et qui doit être un entier. Ici encore ne vous inquiétez pas si vous ne comprenez pas tout le code, l'objectif est de vous donner un morceau de code utilisable tout de suite pour jouer avec votre interpréteur python.

# In[ ]:


# à nouveau : ceci n'est pas conçu pour être exécuté dans le notebook !
parser = ArgumentParser()
parser.add_argument(dest="entier", type=int, 
                    help="entier d'entrée")
input_args = parser.parse_args()
entier = input_args.entier


# Nous pouvons à présent afficher le résultat

# In[ ]:


print(f"fibonacci({entier}) = {fibonacci(entier)}")


# Vous pouvez donc à présent
#  * télécharger ce code sur votre disque comme un fichier `fibonacci.py` en utilisant le menu *"File -> Download as -> python"*
#  * l'exécuter avec simplement python comme ceci
#  
#      `$ python fibonacci.py 56` 
