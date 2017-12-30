
# coding: utf-8

# <style>div.title-slide {    width: 100%;    display: flex;    flex-direction: row;            /* default value; can be omitted */    flex-wrap: nowrap;              /* default value; can be omitted */    justify-content: space-between;}</style><div class="title-slide">
# <span style="float:left;">Licence CC BY-NC-ND</span>
# <span>Thierry Parmentelat &amp; Arnaud Legout</span>
# <span><img src="../media/both-logos-small-alpha.png" style="display:inline" /></span>
# </div>

# # Utiliser python comme une calculette

# Lorsque vous démarrez l'interprète python, vous disposez en fait d'une calculette, par exemple, vous pouvez taper

# In[ ]:


20 * 60


# Les règles de **priorité** entre les opérateurs sont habituelles, les produits et divisions sont évalués en premier, ensuite les sommes et soustractions

# In[ ]:


2 * 30 + 10 * 5


# De manière générale, il est recommandé de bien parenthéser ses expressions. De plus, les parenthèses facilitent la lecture d'expressions complexes. 
# 
# Par exemple, il vaut mieux écrire ce qui suit, qui est équivalent mais plus lisible

# In[ ]:


(2 * 30) + (10 * 5)


# Attention, en python la division `/` est une division naturelle

# In[ ]:


48 / 5


# Rappelez-vous des opérateurs suivants qui sont très pratiques
# 
# | code | opération |
# |------|-----------|
# | `//`   | quotient  |
# | `%`    | modulo    |
# | `**`   | puissance |

# In[ ]:


# calculer un quotient 
48 // 5


# In[ ]:


# modulo (le reste de la division par)
48 % 5


# In[ ]:


# puissance
2 ** 10


# Vous pouvez facilement faire aussi des calculs sur les complexes. Souvenez-vous seulement que la constante complexe que nous notons en français `i` se note en python `j`, ce choix a été fait par le BDFL - alias Guido van Rossum - pour des raisons de lisibilité

# In[ ]:


# multiplication de deux nombres complexes
(2 + 3j) * 2.5j


# Aussi, pour entrer ce nombre complexe `j`, il faut toujours le faire précéder d'un nombre, donc ne pas entrer simplement `j` (qui serait compris comme un nom de variable, nous allons voir ça tout de suite) mais plutôt `1j` ou encore `1.j`, comme ceci

# In[ ]:


1j * 1.j


# ### Utiliser des variables

# Il peut être utile de stocker un résultat qui sera utilisé plus tard, ou de définir une valeur constante. Pour cela on utilise tout simplement une affectation comme ceci

# In[ ]:


# pour définir une variable il suffit de lui assigner une valeur
largeur = 5


# In[ ]:


# une fois la variable définie, on peut l'utiliser, ici comme un nombre
largeur * 20


# In[ ]:


# après quoi bien sûr la variable reste inchangée
largeur * 10


# Pour les symboles mathématiques, on peut utiliser la même technique

# In[ ]:


# pour définir un réel, on utilise le point au lieu d'une virgule en français
pi = 3.14159
2 * pi * 10


# Pour les valeurs spéciales comme $\pi$, on peut utiliser les valeurs prédéfinies par la librairie mathématique de python. En anticipant un peu sur la notion d'importation que nous approfondirons plus tard, on peut écrire

# In[ ]:


from math import e, pi


# Et ainsi imprimer les racines troisièmes de l'unité par la formule
# 
# $r_n = e^{2i\pi \frac{n}{3}},$ pour $n\in \{0,1,2\}$

# In[ ]:


n = 0
print("n=", n, "racine = ", e**((2.j*pi*n)/3))
n = 1
print("n=", n, "racine = ", e**((2.j*pi*n)/3))
n = 2
print("n=", n, "racine = ", e**((2.j*pi*n)/3))


# **Remarque:** bien entendu il sera possible de faire ceci plus simplement lorsque nous aurons vu les boucles `for`.

# ### Les types

# Ce qui change par rapport à une calculatrice standard est le fait que les valeurs sont typées. Pour illustrer les trois types de nombres que nous avons vus jusqu'ici

# In[ ]:


# le type entier s'appelle 'int'
type(3)


# In[ ]:


# le type flottant s'appelle 'float'
type(3.5)


# In[ ]:


# le type complexe s'appelle 'complex'
type(1j)


# ### Chaînes de caractères

# On a également rapidement besoin de chaînes de caractères, on les étudiera bientôt en détails, mais en guise d'avant-goût

# In[ ]:


chaine = "Bonjour le monde !"
print(chaine)


# ### Conversions

# Il est parfois nécessaire de convertir une donnée d'un type dans un autre.
# Par exemple on peut demander à l'utilisateur d'entrer une valeur au clavier grâce à la fonction `input`, comme ceci

# In[ ]:


reponse = input("quel est votre âge ? ")


# In[ ]:


# vous avez entré la chaîne suivante
print(reponse)


# In[ ]:


# ici reponse est une variable, et son contenu est de type chaine de caractères
type(reponse)


# Maintenant je veux faire des calculs sur votre âge, par exemple le multiplier par 2. Si je m'y prends naïvement, ça donne ceci

# In[ ]:


# multiplier une chaine de caractères par deux ne fait pas ce qu'on veut, 
# nous verrons plus tard que ça fait une concaténation
2 * reponse


# C'est pourquoi il me faut ici d'abord **convertir** la (valeur de la) variable `reponse` en un entier, que je peux ensuite doubler (assurez-vous d'avoir bien entré ci-dessus une valeur qui correspond à un nombre entier)

# In[ ]:


# reponse est une chaine
# je la convertis en entier en appelant la fonction int()
age = int(reponse)
type(age)


# In[ ]:


# que je peux maintenant multiplier par 2
2 * age


# Ou si on préfère, en une seule fois

# In[ ]:


print("le double de votre age est", 2*int(reponse))


# ### Conversions - suite

# De manière plus générale, pour convertir un objet en un entier, un flottant, ou une chaîne de caractères, on peut simplement appeler une fonction built-in qui porte le même nom que le type cible.
# 
# | Type | Fonction|
# |------|---------|
# | Entier | `int` |
# | Flottant | `float` |
# | Complexe | `complex` |
# | Chaîne | `str` |
# 
# Ainsi dans l'exemple précédent, `int(reponse)` représente la conversion de `reponse` en entier.
# 
# On a illustré cette même technique dans les exemples suivants.

# In[ ]:


# dans l'autre sens, si j'ai un entier 
a = 2345


# In[ ]:


# je peux facilement le traduire en chaine de caractères
str(2345)


# In[ ]:


# ou en complexe
complex(2345)


# Nous verrons plus tard que ceci se généralise à tous les types de python, pour convertir un object `x` en un type `bidule`, on appelle `bidule(x)`. On y reviendra, bien entendu. 

# ### Grands nombres

# Comme les entiers sont de précision illimitée, on peut améliorer leur lisibilité en insérant des caractères `_` qui sont simplement ignorés à l'exécution.
# 

# In[ ]:


tres_grand_nombre = 23_456_789_012_345

tres_grand_nombre


# In[ ]:


# ça marche aussi avec les flottants
123_456.789_012


# ### Entiers et bases

# Les calculettes scientifiques permettent habituellement d'entrer les entiers dans d'autres bases que la base 10. 
# 
# En python, on peut aussi entrer un entier sous forme binaire comme ceci

# In[ ]:


deux_cents = 0b11001000 ; print(deux_cents)


# Ou encore sous forme octale (en base 8) comme ceci

# In[ ]:


deux_cents = 0o310 ; print(deux_cents)


# Ou enfin encore en hexadecimal (base 16) comme ceci

# In[ ]:


deux_cents = 0xc8 ; print(deux_cents)


# Pour d'autres bases, on peut utiliser la fonction de conversion `int` en lui passant un argument supplémentaire.

# In[ ]:


deux_cents = int('3020', 4) ; print(deux_cents)


# ### Fonctions mathématiques

# python fournit naturellement un ensemble très complet d'opérateurs mathématiques pour les fonctions exponentielles, trigonométriques et autres, mais leur utilisation ne nous est pas encore accessible à ce stade et nous les verrons ultérieurement.
