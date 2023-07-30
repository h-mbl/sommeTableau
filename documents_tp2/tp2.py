import functools

#cette liste contient les liens de chaque image
listePng=["""<img src="symboles/circle.svg">""",\
          """<img src="symboles/cube.svg">""",\
          """<img src="symboles/penta.svg">""",\
          """<img src="symboles/pyramide.svg">""",\
          """<img src="symboles/star.svg">"""]

#cette liste contient la valeur associée à chaque image
#listePng[0] sa valeur est valeurPng[0]
valeurPng=[]
#implementation de randint avec filter et map
while len(valeurPng) != len(listePng):
    #retire les elements qui ne sont pas dans l'intervalle
    valeurPng=list(filter(lambda x: x>= 1 and x<=20, list(map(lambda valeur:\
                                               int(21*random()), range(5)))))
    #genere d'autres nombres pour remplacer les nombres supprimés 
    if len(valeurPng) != len(listePng) :
         valeurPng += list(filter(lambda x: x>= 1 and x<=20, list(map(lambda\
             valeur: int(20*random()), range(len(listePng)-len(valeurPng))))))
#print(valeurPng)
valeurPng=[5,5,5,5,5]
#cette fonction dessine un tableau en html
def tableau(hauteur,largeur):
    htmlTable= '<table>\n'
    compteur=0
    for i in range(hauteur):
      htmlTable += '<tr>\n'
      #if i != hauteur :
      for j in range(largeur):
          pngChoice= listePng[int(5*random())]
          if i == hauteur-1 :
            if j != largeur-1:
              htmlTable += '<td id="case'+ str(compteur) + '">' '</td>\n'
              compteur+=1
          elif j != largeur-1:
            htmlTable += '<td id="case'+ str(compteur) + '" onclick=clic('+\
            str(compteur)+')>'+pngChoice+ '</td>\n'
            compteur+=1
          elif j == largeur-1:
            htmlTable += '<td id="case'+ str(compteur) + '">' '</td>\n'
            compteur+=1
      htmlTable += '  </tr>\n'

    htmlTable += '</table></div>'
    return htmlTable

#cette fonctionne additionne les colonnes et les rangées afin d'obtenir la 
#somme des images
def somme():
  #le saut pour chaque itération
  saut=0
  for i in range(largeur):
    #cette liste enregistre les valeurs des images sur une colonne
    colonne=[]
    for j in range (i,(hauteur)*(largeur),largeur):
      case= j
      #cette condition c'est pour eviter de prendre les valeurs vides de la 
      #dernière colonne et de la dernière rangée
      if j != (largeur-1)*(i+1) + i and j < ((hauteur)*(largeur))-largeur :
        #cette condition empeche de selectionner la dernière colonne lors de la
        #derniere iteration de la premiere boucle
        if (largeur-1)*(i+1) < ((hauteur)*(largeur))-largeur :
          elementSvg = contenu(case).innerHTML
          #cherche l'index de l'image 
          x= listePng.index(elementSvg)
          #ajoute la valeur au tableau listePng[0] sa valeur = valeurPng[o]
          colonne.append(valeurPng[x])
      #cette condition permet d'ecrire le resultat dans la derniere rangee de 
      #la colonne en evitant la derniere colonne 
      elif j >= ((hauteur)*(largeur))-largeur and  j < ((hauteur)*(largeur)):
         #gestion de la condition qui empechait de selectionner la dernière 
         #colonne lors de la derniere iteration de la premiere boucle
         if len(colonne)>0:
            #breakpoint()
            contenu(case).innerHTML = str(functools.reduce(lambda x,y:\
                                                           x+y,colonne))
    #itere le saut
    saut += largeur
    
  #la partie suivante permet de calculer la somme de rangee
  #initialise le saut
  saut=0
  for i in range(hauteur):
      #cette liste enregistre les valeurs des images sur une rangée
      rangee=[]
      for j in range (largeur):
          #avance d'une case
          case= j+saut
          if i != largeur-1 and j != hauteur-1  :
              elementSvg = contenu(case).innerHTML
              x= listePng.index(elementSvg)
              rangee.append(valeurPng[x])
          elif j == hauteur-1 and i != largeur-1:
              contenu(case).innerHTML = str(functools.reduce(lambda x,y:\
                                                             x+y,rangee))
      #le saut se fait par rangée 
      saut += largeur

def soustration(caseInit, valeurPrompt,tempInit):
    #print(case)
    #init= case

    #temp = contenu(caseInit).innerHTML
    saut=0
    breakpoint()
    for i in range(largeur):
    #cette liste enregistre les valeurs des images sur une colonne
        colonne=[]
        for j in range (i,(hauteur)*(largeur),largeur):
            case= j
            #cette condition c'est pour eviter de prendre les valeurs vides de la 
            #dernière colonne et de la dernière rangée
            if j != (largeur-1)*(i+1) + i and j < ((hauteur)*(largeur))-largeur :
              #cette condition empeche de selectionner la dernière colonne lors de la
              #derniere iteration de la premiere boucle
              if (largeur-1)*(i+1) < ((hauteur)*(largeur))-largeur:
                elementSvg = contenu(case).innerHTML
                if tempInit == elementSvg: 
                    #print(case)
                   # breakpoint()
                    contenu(case).innerHTML = """<div class= "container">""" +tempInit + """<h2 class='centered'>""" + str(valeurPrompt) + """</h2></div>"""
                    #contenu(case).innerHTML = str(valeurPrompt)
                    colonne.append(valeurPrompt)
                    #print(colonne)
            #cette condition permet d'ecrire le resultat dans la derniere rangee de 
            #la colonne en evitant la derniere colonne 
            elif j >= ((hauteur)*(largeur))-largeur and  j < ((hauteur)*(largeur)):
                #gestion de la condition qui empechait de selectionner la dernière 
                #colonne lors de la derniere iteration de la premiere boucle
               # breakpoint()
                if len(colonne)> 0:
                   #breakpoint()
                   #on ajoute la valeur de la case init
                    #on l'ajoute a la fin car on doit verifier la condition ci-haut
                   #colonne.append(valeurPrompt)
                   temp = contenu(case).innerHTML
                   valeur = int(temp)- functools.reduce(lambda x,y:\
                                                        x+y,colonne)
                   contenu(case).innerHTML =  str(valeur)
                   if valeur < 0 :
                      return False
        #itere le saut
        saut += largeur

      #la partie suivante permet de calculer la somme de rangee
  #initialise le saut
    tempInit = contenu(caseInit).innerHTML
    saut=0
    for i in range(hauteur):
        #cette liste enregistre les valeurs des images sur une rangée
        rangee=[]
        for j in range (largeur):
            #avance d'une case
            case= j+saut
            if i != largeur-1 and j != hauteur-1  :
                elementSvg = contenu(case).innerHTML
                if tempInit == elementSvg: 
                    #print(case)
                    rangee.append(valeurPrompt)
            elif j == hauteur-1 and i != largeur-1 and len(rangee)>0:
                #rangee.append(valeurPrompt)
                temp = contenu(case).innerHTML
                valeur = int(temp)- functools.reduce(lambda x,y: x+y,rangee)
                contenu(case).innerHTML =  str(valeur)
                if valeur < 0 :
                   return False
        #le saut se fait par rangée 
        saut += largeur

def contenu(id):
   return document.querySelector("#case" + str(id))
def clic(case):
    a=int(prompt("ecrivez un nombre compris entre 1 et 20"))
    id=case
    temp= contenu(case).innerHTML
    #gestion du cas d'une case deja remplie
    if temp in listePng:
      #  contenu(case).innerHTML = """<div class= "container">""" +temp + \
       # """<h2 class='centered'>""" + str(a) + """</h2></div>"""
        soustration(case,a, temp)
def init():
    global hauteur 
    global largeur
    hauteur =6
    largeur = 6 
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
        #resultat {color: red;}
        #main{
         margin-top: 50px;
         margin-left: 50px;
        }
      </style>
      """
    resultat= """<h1 id='resultat'>Jouer!<h1>"""
    main.innerHTML += """<button id='nouvellePartie'> nouvelle partie</button>"""
    main.innerHTML += resultat
    main.innerHTML += tableau(hauteur,largeur)
    somme()
init()