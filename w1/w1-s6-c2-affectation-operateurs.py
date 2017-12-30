
# coding: utf-8

# <style>div.title-slide {    width: 100%;    display: flex;    flex-direction: row;            /* default value; can be omitted */    flex-wrap: nowrap;              /* default value; can be omitted */    justify-content: space-between;}</style><div class="title-slide">
# <span style="float:left;">Licence CC BY-NC-ND</span>
# <span>Thierry Parmentelat &amp; Arnaud Legout</span>
# <span><img src="../media/both-logos-small-alpha.png" style="display:inline" /></span>
# </div>

# # Affectations & Opérations (à la `+=`)

# ## Complément - niveau intermédiaire

# Il existe en python toute une famille d'opérateurs dérivés de l'affectation qui permettent de faire en une fois une opération et une affectation. En voici quelques exemples.

# ### Incrémentation

# On peut facilement augmenter la valeur d'une variable numérique comme ceci

# In[ ]:


entier = 10

entier += 2
print('entier', entier)


# Comme on le devine peut-être, ceci est équivalent à

# In[ ]:


entier = 10

entier = entier + 2
print('entier', entier)


# ### Autres opérateurs courants

# Cette forme, qui combine opération sur une variable et réaffectation du résultat à la même variable, est disponible avec tous les opérateurs courants.

# In[ ]:


entier -= 4
print('après décrément', entier)
entier *= 2
print('après doublement', entier)
entier /= 2
print('mis à moitié', entier)


# ### Types non numériques

# En réalité cette construction est disponible sur tous les types qui supportent l'opérateur en question. Par exemple, les listes (que nous verrons bientôt) peuvent être additionnées entre elles.

# In[ ]:


liste = [0, 3, 5]
print('liste', liste)

liste += ['a', 'b']
print('après ajout', liste)


# Beaucoup de types supportent l'opérateur +, qui est sans doute de loin celui qui est le plus utilisé avec cette construction.

# ### Opérateurs plus abscons

# Signalons enfin qu'on trouve cette construction aussi avec d'autres opérateurs moins fréquents, par exemple

# In[ ]:


entier = 2
print('entier:', entier)
entier **= 10
print('à la puissance dix:', entier)
entier %= 5
print('modulo 5:', entier)
entier <<= 2
print('double décalage gauche:', entier)

