# But du projet

Le but de ce projet est de développer un outil de classification permettant d'identifier des avions dans une image. Pour réaliser cela, des données extraites d'images sont fournies dans des fichiers .csv et vont servir de base d'entrainement pour nos algorithmes. Le tout doit être réalisé dans un lapse de temps de 4h.

# Les besoins

Le but de cette application est d'avoir un modèle performant, rapide et explicable dans le but d'identifier précisément les types avions sur les images.

# Déroulé du projet et méthodologie

Le projet va se dérouler comme suit :

* Les données vont être concatenées dans un grand fichier .csv qui pourra ensuite être utilisé et découpé en plusieurs datasets (train ainsi que test)
* Les données vont être mélangées et réparties en 2 datasets. Le dataset test va contenir le même nombre d'objets provenant de classes identiques (cela va permettre d'avoir une représentativité égale dans le dataset de test qui est le dataset nous permettant d'évaluer la performance de notre modèle).
Le deuxième dataset est un dataset train qui va contenir tous les autres objets présents dans les fichiers du dataset.
* Enfin, plusieurs méthodes vont être testées pour déterminer quels sont les algorithmes les plus performants dans notre cas.

# Premières analyses

Une fois nos datasets réalisés et notre premier algorithme réalisé, les premiers resultats montrent une classification très mauvaise. Une première interprétation des résultats nous permets de dire que les features utilisés pour la classification ne sont pas assez représentatives. Nous pourrions évoquer comme données représentatives la couleur, la forme (un ratio entre la longueur des ailes et le corps de l'avion, une longueur du nez de l'avion ...), l'altitude... Malheureusement, nous n'avons qu'une hauteur, une largeur et une position dans l'image (ce qui nous permets en aucun cas de déterminer le type d'avion auquel nous avons affaire).

# Ce qu'il faudrait faire pour améliorer notre classification

Comme déterminé dans la section precedente, il nous faudrait des données plus représentatives des différentes classes. Pour ce faire, un traitement de chaque image est à réaliser dans le but de déterminer les différentes features qui sont importantes dans notre cas (traitement impossible à réaliser dans un lapse de temps de quelques heures)