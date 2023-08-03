#02 Aout 2023

import functools

# La fonction génère des nombres compris entre 1 et 20.
def choixValeur(valeurPng, listePng):
    # Implémentation de randint avec filter et map
    while len(valeurPng) != len(listePng):
        generateurValeur = \
        list(map(lambda valeur: int(21*random()), range(5)))
        
        # Retire les éléments qui ne sont pas dans l'intervalle
        valeurPng = list(filter(lambda x: x >= 1 and \
                                x <= 20, generateurValeur))
        
        # Génère d'autres nombres pour remplacer les nombres supprimés
        if len(valeurPng) != len(listePng):
            generateurValeur = list(map(lambda valeur: int(21*random()), \
                                    range(len(listePng)-len(valeurPng))))
            valeurPng += list(filter(lambda x: x >= 1 and x <= 20, \
                                 generateurValeur))
    return valeurPng

def contenu(id):
    return document.querySelector("#case" + str(id))

def clic(case):
    if nouvellePartie == True:
        nombreChoisi=int(prompt("ecrivez un nombre compris entre 1 et 20"))
      
        #message d'erreur pour nombre pas compris entre 1 et 20
        while nombreChoisi<0 or nombreChoisi>20:
            alert("nombre entre 1 et 20 svp")
            nombreChoisi=int(prompt("ecrivez un nombre compris entre 1 et 20"))
        
        temp = contenu(case).innerHTML
        # Gestion du cas d'une case déjà remplie
        if temp in listePng:
            soustraction(case,nombreChoisi, temp)
    else:
        alert("lancez une nouvelle partie")

# Cette fonction écrit le head de notre html
def head():
    resultat = """<button onclick="init()" >Nouvelle partie</button>\n"""
    resultat += """<h1 id='caseResultat'>Jouer!<h1>"""
    return resultat

# Cette fonction dessine un tableau en html
def tableau(hauteur, largeur):
    htmlTable = '<table>\n'
    compteur = 0
    for i in range(hauteur):
        htmlTable += '<tr>\n'
        for j in range(largeur):
            pngChoice = listePng[int(5*random())]
            if i == hauteur - 1:
                if j != largeur - 1:
                    htmlTable += '<td id="case' + str(compteur) + '">''</td>\n'
                    compteur += 1
            elif j != largeur - 1:
                htmlTable += '<td id="case' + str(compteur)  + \
                '" onclick=clic('+ str(compteur)+')>' + pngChoice + '</td>\n'
                compteur += 1
            elif j == largeur - 1:
                htmlTable += '<td id="case' + str(compteur) + '">' '</td>\n'
                compteur += 1
        htmlTable += '  </tr>\n'
    htmlTable += '</table></div>'
    return htmlTable

# Cette fonction vérifie la valeur de chaque colonne
def verificateurColonne():
    saut = 0
    colonne = []

    for i in range(largeur):
        for j in range(i, valeurMaxTab, largeur):
            # Cette condition permet de sélectionner uniquement
            # la dernière rangée
            if j >=  valeurMinTab and  j <  valeurMaxTab-1:
                colonne.append(int(contenu(j).innerHTML))
        # Itère le saut
        saut += largeur
    return colonne

# Cette fonction vérifie la valeur de chaque rangée
def verificateurRangee():
    saut = 0
    rangee = []
    for i in range(hauteur):
        for j in range(largeur):
            # Avance d'une case
            case = j + saut
            # Cette condition permet de sélectionner uniquement
            # la dernière rangée
            if j == hauteur - 1 and i != largeur - 1:
                rangee.append(int(contenu(case).innerHTML))
        saut += largeur
    return rangee

# Cette fonction est la combinaison de ces deux fonctions précédentes et
# permet de définir une victoire, un échec ou une continuation de la partie
def verificateurResultat(colonne, rangee):
    global nouvellePartie
    # Les deux attributs enlèvent toutes les valeurs négatives de deux listes
    # de deux listes en paramètre
    valeursRangee = list(filter(lambda x: x >= 0, rangee))
    valeursColonne = list(filter(lambda x: x >= 0, colonne))

    if len(valeursRangee) == len(rangee) and \
    len(valeursColonne) == len(colonne):
       # Les deux attributs enlèvent toutes les valeurs différentes de zéro de
        # deux listes en paramètre
        valeursZeroRangee = list(filter(lambda x: x == 0, rangee))
        valeursZeroColonne = list(filter(lambda x: x == 0, colonne))
        # Condition pour la victoire
        if len(valeursZeroRangee) == len(rangee) and \
        len(valeursZeroColonne) == len(colonne):
            # Empêche l'utilisateur de continuer à attribuer des valeurs aux
            # images après avoir réussi
            nouvellePartie = False
            contenu("Resultat").innerHTML = "Vous avez gagné!"
            return True
    else:
        # Empêche l'utilisateur de continuer à attribuer des valeurs aux images
        # après avoir échoué
        nouvellePartie = False
        contenu("Resultat").innerHTML = "Vous avez perdu "
        return False

# Cette procédure appelle toutes les fonctions nécessaires pour la vérification
# des valeurs dans chacune des cellules de la dernière colonne et rangée
def verificateur():
    colonne = verificateurColonne()
    rangee = verificateurRangee()
    verificateurResultat(colonne, rangee)

# Cette fonction soustrait la somme de chaque colonne avec 
#la valeur * nombre d'images sur laquelle l'utilisateur a cliqué
# et écrit le prompt sur l'image.
# En effet, cette fonction permet d'écrire sur
# toutes les images semblables à l'image du queryselector dans le tableau.
# D'où soustractionRangee n'écrira pas sur les images.
def soustractionColonne(caseInit, valeurPrompt, tempInit):
    saut = 0
    for i in range(largeur):
        # Cette liste enregistre les valeurs des images sur une colonne
        colonne = 0
        for j in range(i, valeurMaxTab, largeur):
            case = j

            # Cette condition permet d'éviter de prendre les valeurs vides
            # de la dernière colonne et de la dernière rangée
            if j != (largeur - 1) * (i + 1) + i and  j <  valeurMinTab:

                # Cette condition empeche de sélectionner la dernière colonne
                # lors de la dernière itération de la première boucle
                if (largeur - 1) * (i + 1) < valeurMinTab:
                    elementSvg = contenu(case).innerHTML
                    if tempInit == elementSvg:
                        contenu(case).innerHTML = \
                        """<div class="container">""" \
                        + tempInit + """<h2 class='centered'>""" + \
                        str(valeurPrompt) + """</h2></div>"""
                        colonne += valeurPrompt

            # Cette condition permet d'écrire le résultat dans la dernière
            # rangée de la colonne en évitant la dernière colonne
            elif j >= valeurMinTab and j < valeurMaxTab:
                # Gestion de la condition qui empêchait
                # de sélectionner la dernière colonne lors de la dernière
                #itération de la première boucle
                if colonne > 0:
                    temp = contenu(case).innerHTML
                    valeur = int(temp) - colonne
                    contenu(case).innerHTML =  str(valeur)

        # Itère le saut
        saut += largeur

# Cette fonction soustrait la somme de chaque rangée avec 
#la valeur * nombre d'images sur laquelle l'utilisateur a cliqué
def soustractionRangee(caseInit, valeurPrompt, tempInit):
    # La partie suivante permet de calculer la somme de rangee
    # Initialise le saut
    tempInit = contenu(caseInit).innerHTML
    saut = 0
    for i in range(hauteur):
        # Cette variable enregistre les valeurs des images sur une rangée
        rangee = 0
        for j in range(largeur):
            # Avance d'une case
            case = j + saut
            # Cette condition permet d'écrire le résultat dans
            # toutes les cases en rangée en évitant les dernières cases
            #de la rangée et la dernière rangée
            if i != largeur - 1 and j != hauteur - 1:
                elementSvg = contenu(case).innerHTML
                if tempInit == elementSvg:
                    rangee += valeurPrompt
            elif j == hauteur - 1 and i != largeur - 1 and rangee > 0:
                temp = contenu(case).innerHTML
                valeur = int(temp) - rangee
                contenu(case).innerHTML =  str(valeur)

        # Le saut se fait par rangée
        saut += largeur

# Cette procédure appelle toutes les fonctions nécessaires pour
# la soustraction des valeurs dans chacune des cases de la colonne et rangée
# ayant la même image que l'image sur laquelle l'utilisateur a cliqué.
# Écrit sur ces images et ensuite calcule la nouvelle somme et
# détecte la victoire, l'échec ou la continuation de la partie
def soustraction(caseInit, valeurPrompt, tempInit):

    soustractionColonne(caseInit, valeurPrompt, tempInit)
    soustractionRangee(caseInit, valeurPrompt, tempInit)
    verificateur()

# Cette fonction additionne  les colonnes et les rangées afin d'obtenir la
# somme des valeurs des images
def sommeColonne():
    # Le saut pour chaque itération
    saut = 0
    for i in range(largeur):
        # Cette liste enregistre les valeurs des images sur une colonne
        colonne = []
        for j in range(i, valeurMaxTab, largeur):
            case = j
            # Cette condition c'est pour éviter de prendre
            #les valeurs vides de la
            # dernière colonne et de la dernière rangée
            if j != (largeur - 1) * (i + 1) + i and j < valeurMinTab:
                # Cette condition empeche de sélectionner la dernière colonne
                # lors de la dernière itération de la première boucle
                if (largeur - 1) * (i + 1) < valeurMinTab:
                    elementSvg = contenu(case).innerHTML
                    # Cherche l'index de l'image
                    x = listePng.index(elementSvg)
                    # Ajoute la valeur au tableau listePng[0], sa valeur =
                    # valeurPng[0]
                    colonne.append(valeurPng[x])
            # Cette condition permet d'écrire le résultat dans la dernière
            # rangée de la colonne en évitant la dernière colonne
            elif j >= valeurMinTab and  j < valeurMaxTab:
                # Gestion de la condition qui empêchait de sélectionner
                # la dernière colonne lors de la dernière itération
                #de la première boucle
                if len(colonne) > 0:
                    contenu(case).innerHTML =\
                    str(functools.reduce(lambda x, y: x + y, colonne))
        # Itère le saut
        saut += largeur

# Cette fonction additionne les rangées afin d'obtenir 
#la somme des valeurs des images
def sommeRangee():

    # La partie suivante permet de calculer la somme de rangee
    # Initialise le saut
    saut = 0
    for i in range(hauteur):
        # Cette liste enregistre les valeurs des images sur une rangée
        rangee = []
        for j in range(largeur):
            # Avance d'une case
            case = j + saut
            if i != largeur - 1 and j != hauteur - 1:
                elementSvg = contenu(case).innerHTML
                x = listePng.index(elementSvg)
                rangee.append(valeurPng[x])
            elif j == hauteur - 1 and i != largeur - 1:
                contenu(case).innerHTML = str(functools.reduce(lambda x, y: \
                                                 x + y, rangee))
        # Le saut se fait par rangée
        saut += largeur

# Cette procédure appelle toutes les fonctions nécessaires à l'addition
# des valeurs des images des colonnes et des rangées
def somme():
    sommeColonne()
    sommeRangee()

def init():
    # Ces variables globales sont les plus utilisées dans le programme dans 
    #plus  d'une fonction et elles sont statiques
    global hauteur
    global largeur
    global nouvellePartie
    
    # La dernière rangée est comprise entre valeurMinTab et valeurMaxTab
    global valeurMaxTab
    global valeurMinTab
    
    # Liste des images
    global listePng
    global valeurPng

    nouvellePartie = True
    hauteur = 6
    largeur = 6
    valeurMaxTab = (hauteur) * (largeur)
    valeurMinTab = ((hauteur) * (largeur)) - largeur 
    # Cette liste contient les liens de chaque image
    listePng = ["""<img src="symboles/circle.svg">""", \
              """<img src="symboles/cube.svg">""", \
              """<img src="symboles/penta.svg">""", \
              """<img src="symboles/pyramide.svg">""", \
              """<img src="symboles/star.svg">"""]
    # Cette liste contient la valeur associée à chaque image
    # listePng[0] sa valeur est valeurPng[0]
    valeurPng = []
    c = choixValeur(valeurPng, listePng)
    valeurPng = c
    
    main = document.querySelector("#main")
    main.innerHTML = """
      <style>
        #jeu table { float: none; }
        #jeu table td {
            border: 1px solid black; 
            padding: 1px 2px;
            width: 80px;
            height: 80px;
            font-family: Helvetica; 
            font-size: 20px; 
            text-align: center;
        }
        #jeu table td img {
            display: block;
            margin-left: auto;
            margin-right: auto;
            object-fit: contain;
            width: 80%;
            height: 80%;
        }
        .container {
           position: relative;
          }
         .container img {
         width: 100%;
         height: 100%;
         }
         .centered{
           color: black;
           position: absolute;
           top:50%;
           left:50%;
           transform:translate(-50%,-50%);
        }
        #caseResultat {color: red;}
        #main{
         margin-top: 50px;
         margin-left: 50px;
        }
      </style>
      """
    main.innerHTML += head()
    main.innerHTML += tableau(hauteur,largeur)
    somme()
