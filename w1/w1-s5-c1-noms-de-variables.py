
# coding: utf-8

# <style>div.title-slide {    width: 100%;    display: flex;    flex-direction: row;            /* default value; can be omitted */    flex-wrap: nowrap;              /* default value; can be omitted */    justify-content: space-between;}</style><div class="title-slide">
# <span style="float:left;">Licence CC BY-NC-ND</span>
# <span>Thierry Parmentelat &amp; Arnaud Legout</span>
# <span><img src="media/both-logos-small-alpha.png" style="display:inline" /></span>
# </div>

# # Noms de variables

# ## Complément - niveau basique

# Revenons sur les noms de variables autorisés ou non.

# Les noms les plus simples sont constitués de lettres. Par exemple

# In[ ]:


factoriel = 1


# On peut utiliser aussi les majuscules, mais attention cela définit une variable différente. Ainsi

# In[ ]:


Factoriel = 100
factoriel == Factoriel


# Le signe `==` permet de tester si deux variables ont la même valeur.
# Si les variables ont la même valeur, le test retournera `True`, et `False` sinon. On y reviendra bien entendu.

# ### Conventions habituelles

# En règle générale, on utilise **uniquement des minuscules** pour désigner les variables simples (ainsi d'ailleurs que pour les noms de fonctions), les majuscules sont réservées en principe pour d'autres sortes de variables, comme les noms de classe, que nous verrons ultérieurement.
# 
# Notons, qu'il s'agit uniquement d'une convention, ceci n'est pas imposé par le langage lui-même.

# Pour des raisons de lisibilité, il est également possible d'utiliser le tiret bas `_` dans les noms de variables. On préfèrera ainsi

# In[ ]:


age_moyen = 75 # oui


# plutôt que ceci (bien qu'autorisé par le langage)

# In[ ]:


AgeMoyen = 75 # autorisé, mais non


# On peut également utiliser des chiffres dans les noms de variables comme par exemple

# In[ ]:


age_moyen_dept75 = 80


# avec la restriction toutefois que le premier caractère ne peut pas être un chiffre, cette affectation est donc refusée

# In[ ]:


75_age_moyen = 80 # erreur de syntaxe


# ### Le tiret bas comme premier caractère

# Il est par contre, possible de faire commencer un nom de variable par un tiret bas comme premier caractère&nbsp;; toutefois, à ce stade, nous vous déconseillons d'utiliser cette pratique qui est réservée à des conventions de nommage bien spécifiques.

# In[ ]:


_autorise_mais_deconseille = 'Voir le PEP 008'


# Et en tous cas, il est **fortement déconseillé** d'utiliser des noms de la forme `__variable__` qui sont réservés au langage. Nous reviendrons sur ce point dans le futur, mais reagardez par exemple cette variable que nous n'avons définie nulle part mais qui pourtant existe bel et bien

# In[ ]:


__name__  # ne définissez pas vous-même de variables de ce genre


# ### Ponctuation

# Dans la plage des caractères ASCII, il n'est **pas possible** d'utiliser d'autres caractères que les caractères alphanumériques et le tiret bas. Notamment le tiret haut `-` est interprété comme l'opération de soustraction. Attention donc à cette erreur fréquente

# In[ ]:


age-moyen = 75  # erreur : en fait python lit 'age - moyen = 75'


# ### Caractères exotiques

# En python-3, il est maintenant aussi possible d'utiliser des caractères Unicode dans les identificateurs

# In[ ]:


# les caractères accentués sont permis
nom_élève = "Jules Maigret"


# In[ ]:


# ainsi que l'alphabet grec
from math import cos, pi as 𝞟
θ = 𝞟 / 4
cos(θ)


# Tous les caractères Unicode ne sont pas permis - heureusement car cela serait source de confusion. Nous citons dans les références les documents qui précisent quels sont exactement les caractères autorisés.

# In[ ]:


# ce caractère n'est pas autorisé
# il est considéré comme un signe mathématique (produit)
∏ = 10


# #### Conseil
# 
# Il est **très vivement** recommandé&nbsp;:
# 
# * tout d'abord de coder **en anglais**,
# * ensuite de **ne pas** définir des identificateurs avec des caractères non ASCII, dans toute la mesure du possible,
# * enfin si vous utilisez un encodage autre que utf-8, vous **devez** bien **spécifier l'encodage** utilisé dans votre fichier source&nbsp;; nous y reviendrons en deuxième semaine.

# ### Pour en savoir plus

# Pour les esprits curieux, Guido van Rossum, le fondateur de python, est le co-auteur d'un document qui décrit les conventions de codage à utiliser dans les librairies python standard. Ces règles sont plus restrictives que ce que le langage permet de faire, mais constituent une lecture intéressante si vous projetez d'écrire beaucoup de python.
# 
# Voir dans le PEP 008 [la section consacrée aux règles de nommage - (en anglais)](http://legacy.python.org/dev/peps/pep-0008/#descriptive-naming-styles)
# 

# Voir enfin, au sujet des caractères exotiques dans les identificateurs:
# 
# * https://www.python.org/dev/peps/pep-3131/ qui définit les caractères exotiques autorisés, et qui repose à son tour sur
# * http://www.unicode.org/reports/tr31/ (très technique!)
