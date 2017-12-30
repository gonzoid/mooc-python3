
# coding: utf-8

# <style>div.title-slide {    width: 100%;    display: flex;    flex-direction: row;            /* default value; can be omitted */    flex-wrap: nowrap;              /* default value; can be omitted */    justify-content: space-between;}</style><div class="title-slide">
# <span style="float:left;">Licence CC BY-NC-ND</span>
# <span>Thierry Parmentelat &amp; Arnaud Legout</span>
# <span><img src="media/both-logos-small-alpha.png" style="display:inline" /></span>
# </div>

# # Gestion de la mémoire

# ## Complément - niveau basique

# L'objet de ce complément est de vous montrer qu'avec python vous n'avez pas à vous préoccuper de la mémoire. Pour expliquer la notion de gestion de la mémoire, il nous faut donner un certain nombre de détails sur d'autres langages comme C et C++. Si vous souhaitez suivre ce cours à un niveau basique vous pouvez ignorer ce complément et seulement retenir que python se charge de tout pour vous :)

# ## Complément - niveau intermédiaire

# ### Langages de bas niveau

# Dans un langage traditionnel de bas niveau comme C ou C++, le programmeur est en charge de l'allocation - et donc de la libération - de la mémoire. 
# 
# Ce qui signifie que, sauf pour les valeurs stockées dans la pile, le programmeur est amené
#  * à réclamer de la mémoire à l'OS en appelant explicitement `malloc` (C) ou `new` (C++)
#  * et réciproquement à rendre cette mémoire à l'OS lorsqu'elle n'est plus utilisée, en appelant `free` (C) ou `delete` (C++).

# Avec ce genre de langage, la gestion de la mémoire est un aspect important de la programmation. Ce modèle offre une grande flexibilité, mais au prix d'un coût élevé en termes de vitesse de développement.
# 
# En effet, il est assez facile d'oublier de libérer la mémoire après usage, ce qui peut conduire à épuiser les ressources disponibles. À l'inverse, utiliser une zone mémoire non allouée peut conduire à des bugs très difficiles à localiser et à des problèmes de sécurité majeurs. Notons qu'une grande partie des attaques en informatiques reposent sur l'exploitation d'erreurs de gestion de la mémoire. 

# ### Langages de haut niveau

# Pour toutes ces raisons, avec un langage de plus haut niveau comme python, le programmeur est libéré de cet aspect de la programmation.
# 
# Pour anticiper un peu sur le cours des semaines suivantes, voici ce que vous pouvez garder en tête s'agissant de la gestion mémoire en python.
#  * Vous créez vos objets au fur et à mesure de vos besoins.
#  * Vous n'avez pas besoin de les libérer explicitement, le "*Garbage Collector*" de python va s'en charger pour recycler la mémoire lorsque c'est possible.
# 
# 
#  * Python a tendance à être assez gourmand en mémoire, comparé à un langage de bas niveau, car tout est objet et chaque objet est assorti de *méta-informations* qui occupent une place non négligeable. Par exemple, chaque objet possède au minimum
#    * une référence vers son type - c'est le prix du typage dynamique,
#    * un compteur de références - le nombre d'autres valeurs (variables ou objets) qui pointent vers l'objet, cette information est notamment utilisée, précisément, par le *Garbage Collector* pour déterminer si la mémoire utilisée par un objet peut être libérée ou non.
#  * Un certain nombre de types prédéfinis et non mutables sont implémentés en python comme des *singletons*, c'est-à-dire qu'un seul objet est créé et partagé, c'est le cas par exemple pour les petits entiers et les chaînes de caractères, on en reparlera.
#  * Lorsqu'on implémente une classe, il est possible de lui conférer cette caractéristique de singleton, de manière à optimiser la mémoire nécessaire pour exécuter un programme.
