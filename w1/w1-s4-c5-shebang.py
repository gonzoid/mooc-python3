
# coding: utf-8

# <style>div.title-slide {    width: 100%;    display: flex;    flex-direction: row;            /* default value; can be omitted */    flex-wrap: nowrap;              /* default value; can be omitted */    justify-content: space-between;}</style><div class="title-slide">
# <span style="float:left;">Licence CC BY-NC-ND</span>
# <span>Thierry Parmentelat &amp; Arnaud Legout</span>
# <span><img src="media/both-logos-small-alpha.png" style="display:inline" /></span>
# </div>

# # La ligne *shebang*

#     #!/usr/bin/env python3

# ## Complément - niveau avancé

# Ce complément est uniquement valable pour MacOS et linux.

# ### Le besoin

# Nous avons vu dans la vidéo que pour lancer un programme python on fait essentiellement depuis le terminal

#     $ python3 mon_module.py

# Lorsqu'il s'agit d'un programme qu'on utilise fréquemment, on n'est pas forcément dans le répertoire où se trouve le programme python, aussi dans ce cas on peut utiliser un chemin "absolu", c'est-à-dire à partir de la racine des noms de fichiers, comme par exemple

#     $ python3 /le/chemin/jusqu/a/mon_module.py

# Sauf que c'est assez malcommode, et cela devient vite pénible à la longue.

# ### La solution

# Sur linux et MacOS, il existe une astuce utile pour simplifier cela. Voyons comment s'y prendre, avec par exemple le programme `fibonacci.py` que vous pouvez [télécharger ici](data/fibonacci.py) (nous verrons ce code en détail dans les deux prochains compléments). Commencez par sauver ce code sur votre ordinateur dans un fichier qui s'appelle, bien entendu, `fibonacci.py`.

# On commence par éditer le tout début du fichier pour lui ajouter une **première ligne**

#     #!/usr/bin/env python3
#    
#     ## La suite de Fibonacci (Suite)
#     ...etc...

# Cette première ligne s'appelle un [Shebang](http://en.wikipedia.org/wiki/Shebang_%28Unix%29) dans le jargon Unix. Unix stipule que le Shebang doit être en **première position** dans le fichier. 

# Ensuite on rajoute au fichier, depuis le terminal, le caractère exécutable comme ceci

# ```
# $ pwd
# /le/chemin/jusqu/a/
# ```

# ```
# $ chmod +x fibonacci.py
# ```

# À partir de là, vous pouvez utiliser le fichier `fibonacci.py` comme une commande, sans avoir à mentionner `python3`, qui sera invoqué au travers du shebang.

# ```
# $ /le/chemin/jusqu/a/fibonacci.py 20
# fibonacci(20) = 10946
# ```

# Et donc vous pouvez aussi le déplacer dans un répertoire qui est dans votre variable `PATH`, et le rendre ainsi accessible depuis n'importe quel répertoire en faisant simplement

# ```
# $ export PATH=/le/chemin/jusqu/a:$PATH
# ```

# ```
# $ cd /tmp
# $ fibonacci.py 20
# fibonacci(20) = 10946
# ```

# **Remarque&nbsp;:** tout ceci fonctionne très bien tant que votre point d'entrée - ici `fibonacci.py` - n'utilise que des modules standards. Dans le cas où le point d'entrée vient avec au moins un module, il est également nécessaire d'installer ces modules quelque part, et d'indiquer au point d'entrée comment les trouver, nous y reviendrons dans la semaine où nous parlerons des modules.
