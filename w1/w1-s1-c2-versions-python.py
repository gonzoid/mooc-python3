
# coding: utf-8

# <style>div.title-slide {    width: 100%;    display: flex;    flex-direction: row;            /* default value; can be omitted */    flex-wrap: nowrap;              /* default value; can be omitted */    justify-content: space-between;}</style><div class="title-slide">
# <span style="float:left;">Licence CC BY-NC-ND</span>
# <span>Thierry Parmentelat &amp; Arnaud Legout</span>
# <span><img src="media/both-logos-small-alpha.png" style="display:inline" /></span>
# </div>

# # Versions de python

# Comme on l'indique dans la vidéo, la version de référence du MOOC est la version 3.6, c'est avec cette version qu'on a tourné les vidéos.

# ### python-3.5

# Si vous préférez utiliser python-3.5, la différence la plus visible pour vous apparaitra avec les *f-strings*&nbsp;:

# In[ ]:


age = 10

# un exemple de f-string
f"Jean a {age} ans"


# Cette construction - que nous utilisons très fréquemment - n'a été introduite qu'en python-3.6, aussi si vous utilisez python-3.5 vous verrez ceci&nbsp;:
# ```
# >>> age = 10
# >>> f"Jean a {age} ans"
#   File "<stdin>", line 1
#     f"Jean a {age} ans"
#                       ^
# SyntaxError: invalid syntax
# ```

# Dans ce cas vous devrez remplacer ce code avec la méthode `format` - que nous verrons en Semaine 2 lorsque nous verrons les chaines de caractères - et dans le cas présent il faudrait remplacer par ceci&nbsp;:

# In[ ]:


age = 10

"Jean a {} ans".format(age)


# Comme ces f-strings sont très présents dans le cours, il est recommandé d'utiliser au moins python-3.6.

# # python-3.4

# La remarque vaut donc *a fortiori* pour python-3.4, qui en outre ne vous permettra pas de suivre la semaine 8 sur la programmation asynchrone, car les mots-clés `async` et `await` ont été introduits seulement dans python-3.5.
