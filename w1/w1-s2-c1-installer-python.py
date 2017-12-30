
# coding: utf-8

# <style>div.title-slide {    width: 100%;    display: flex;    flex-direction: row;            /* default value; can be omitted */    flex-wrap: nowrap;              /* default value; can be omitted */    justify-content: space-between;}</style><div class="title-slide">
# <span style="float:left;">Licence CC BY-NC-ND</span>
# <span>Thierry Parmentelat &amp; Arnaud Legout</span>
# <span><img src="../media/both-logos-small-alpha.png" style="display:inline" /></span>
# </div>

# # Installer la distribution standard python

# ## Complément - niveau basique

# Ce complément a pour but de vous donner quelques guides pour l'installation de la distribution standard python 3. 
# 
# Notez bien qu'il ne s'agit ici que d'indications, il existe de nombreuses façons de procéder.
# 
# En cas de souci, commencez par chercher par vous-même sur google ou autre une solution à votre problème&nbsp;; pensez également à utiliser le forum du cours.

# Le point important est de **bien vérifier le numéro de version** de votre installation qui doit être **au moins 3.6**

# # Digression - coexistence de python2 et python3

# Avant l'arrivée de la version 3 de python, les choses étaient simples, on exécutait un programme python avec une commande `python`. Depuis 2014-2015, maintenant que les deux versions de python coexistent, il est nécessaire d'adopter une convention qui permette d'installer les deux langages sous des noms qui sont non-ambigus.
# 
# C'est pourquoi actuellement, on trouve **le plus souvent** la convention suivante sous Linux et Mac OS X&nbsp;:
# 
# * `python3` est pour exécuter les programmes en python-3&nbsp;; du coup on trouve alors également les commandes comme `idle3` pour lancer IDLE, et par exemple `pip3` pour le gestionnaire de paquets (voir ci-dessous).
# 
# * `python2` est pour exécuter les programmes en python-2, avec typiquement `idle2` et `pip2`;
# 
# * enfin selon les systèmes, la commande `python` tout court est un alias pour `python2` ou `python3`. De plus en plus souvent, par défaut `python` désigne `python3`.
# 
# à titre d'illustration, voici ce que j'obtiens sur mon mac&nbsp;:
# 
# ```
# $ python3 -V
# Python 3.6.2
# $ python2 -V
# Python 2.7.13
# $ python -V
# Python 3.6.2
# ```
# 
# Sous Windows, vous avez un lanceur qui s'appelle `py`. Par défaut, il lance la version de python la plus récente installée, mais vous pouvez spécifier une version spécifique de la manière suivante&nbsp;: 
# ```
# C:\> py -2.7
# ``` 
# 
# pour lancer, par exemple, python en version 2.7. Vous trouverez toute la documentation nécessaire pour Windows sur cette page (en anglais)&nbsp;: https://docs.python.org/3/using/windows.html
# 
# Pour éviter d'éventuelles confusions, nous précisons toujours `python3` dans le cours.

# # Installation de base

# ### Vous utilisez Windows

# La méthode recommandée sur Windows est de partir de la page  https://www.python.org/download
# où vous trouverez un programme d'installation qui contient tout ce dont vous aurez besoin pour suivre le cours.
# 
# Pour vérifier que vous êtes prêts, il vous faut lancer IDLE (quelque part dans le menu Démarrer) et vérifier le numéro de version.

# ### Vous utilisez MacOS

# Ici encore, la méthode recommandée est de partir de la page https://www.python.org/download
# et d'utiliser le programme d'installation.
# 
# Sachez aussi, si vous utilisez déjà MacPorts (https://www.macports.org), que vous pouvez également utiliser cet outil pour installer, par exemple python 3.6, avec la commande

#     $ sudo port install python36

# ### Vous utilisez Linux

# Dans ce cas il y est très probable que python-3.x est déjà disponible sur votre machine. Pour vous en assurer, essayez de lancer la commande `python3` dans un terminal. 

# ##### Redhat / Fedora

# Voici par exemple ce qu'on obtient depuis un terminal sur une machine installée en Fedora-20 

#     $ python3
#     Python 3.6.2 (default, Jul 20 2017, 12:30:02)
#     [GCC 6.3.1 20161221 (Red Hat 6.3.1-1)] on linux
#     Type "help", "copyright", "credits" or "license" for more information.
#     >>> exit()
#     

# **Vérifiez bien le numéro de version** qui doit être en 3.*x*. Si vous obtenez un message du style `python3: command not found` utilisez `dnf` (anciennement connu sous le nom de `yum`) pour installer le rpm `python3` comme ceci

#     $ sudo dnf install python3

# S'agissant de `idle`, l'éditeur que nous utilisons dans le cours (optionnel si vous êtes familier avec un éditeur de texte), vérifiez sa présence comme ceci

#     $ type idle3
#     idle is hashed (/usr/bin/idle3)

# Ici encore, si la commande n'est pas disponible vous pouvez l'installer avec

#     $ sudo yum install python3-tools

# ##### Debian / Ubuntu

# Ici encore, python-2.7 est sans doute déja disponible. Procédez comme ci-dessus, voici un exemple recueilli dans un terminal sur une machine installée en Ubuntu-14.04/trusty

#     $ python3
#     Python 3.6.2 (default, Jul 20 2017, 12:30:02)
#     [GCC 6.3.1 20161221 (Red Hat 6.3.1-1)] on linux
#     Type "help", "copyright", "credits" or "license" for more information.
#     >>> exit()

# Pour installer python

#     $ sudo apt-get install python3

# Pour installer idle

#     $ sudo apt-get install idle3

# ### Installation de librairies complémentaires

# Il existe un outil très pratique pour installer les librairies python, il s'appelle `pip3`, qui est documenté ici https://pypi.python.org/pypi/pip

# Sachez aussi, si par ailleurs vous utilisez un gestionnaire de package comme `rpm` sur RedHat, `apt-get` sur debian, ou `port` sur MacOS, que de nombreux packages sont également disponibles au travers de ces outils.

# # Anaconda

# Sachez qu'il existe beaucoup de distributions alternatives qui incluent python&nbsp;; parmi elles, la plus populaire est sans aucun doute [Anaconda](https://www.anaconda.com/), qui contient un grand nombre de bibliothèques de calcul scientifique, et également d'ailleurs jupyter pour travailler nativement sur des notebooks au format `.ipynb`.
# 
# Anaconda vient avec son propre gestionnaires de paquets pour l'installation de librairies supplémentaires qui s'appelle `conda`.
