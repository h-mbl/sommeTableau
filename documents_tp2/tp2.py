import functools

#cette liste contient les liens de chaque image
listePng=["""<img src="symboles/circle.svg">""",\
          """<img src="symboles/cube.svg">""",\
          """<img src="symboles/penta.svg">""",\
          """<img src="symboles/pyramide.svg">""",\
          """<img src="symboles/star.svg">"""]

#cette liste contient la valeur associée à chaque image
#listePng[0] sa valeur est valeurPng[0]
valeurPng = list(map(lambda valeur: int(20*random()), range(4)))

#cette fonction dessine un tableau en html
def tableau(hauteur,largeur):
    htmlTable= '<table>\n'
    compteur=0
    for i in range(hauteur):
      htmlTable += '<tr>\n'
      #if i != hauteur :
      for j in range(largeur):
          pngChoice= listePng[int(4*random())]
          if i == hauteur-1 :
            if j != largeur-1:
              htmlTable += '<td id="case'+ str(compteur) + '">' '</td>\n'
              compteur+=1
          elif j != largeur-1:
            htmlTable += '<td id="case'+ str(compteur) + '" onclick=clic('+ str(compteur)+')>'+pngChoice+ '</td>\n'
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
            contenu(case).innerHTML = str(functools.reduce(lambda x,y:x+y,colonne))
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
              contenu(case).innerHTML = str(functools.reduce(lambda x,y:x+y,rangee))
      #le saut se fait par rangée 
      saut += largeur

def contenu(id):
   return document.querySelector("#case" + str(id))
def clic(case):
    #htmlTable += '<td id="case'+ str(compteur) + '" onclick=clic('+ str(compteur)+')>'+pngChoice+ '</td>\n'
    a=int(prompt("ecrivez un nombre compris entre 1 et 20"))
    contenu(case).innerHTML += """<div class='centered'>""" + str(a) + """</div>"""
    print(contenu(case).innerHTML)
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
        #resultat {color: red;}
        #main{
         margin-top: 50px;
         margin-left: 50px;
        }
        .centered{
        position: absolute;
        top:50%;
        left:50%;
        transform:translate(-50%,-50%);}
      </style>
      """
    resultat= """<h1 id='resultat'>Jouer!<h1>"""
    main.innerHTML += """<button id='nouvellePartie'> nouvelle partie</button>"""
    main.innerHTML += resultat
    main.innerHTML += tableau(hauteur,largeur)
    somme()
