# Vous devez remplacer le contenu de ce fichier par votre propre code
# tel qu'indiqué dans la description du TP2.  Le code ici correspond
# à l'exemple donné dans la description.

def init():
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
      </style>
      <div id="jeu">
        <table>
          <tr>
            <td id="case0"><img src="symboles/circle.svg"></td>
            <td id="case1"><img src="symboles/pyramide.svg"></td>
            <td id="case2"><img src="symboles/circle.svg"></td>
            <td id="case3"><img src="symboles/penta.svg"></td>
            <td id="case4"><img src="symboles/star.svg"></td>
            <td id="case5"></td>           
          </tr>
          <tr>
            <td id="case6"><img src="symboles/penta.svg"></td>
            <td id="case7"><img src="symboles/cube.svg"></td>
            <td id="case8"><img src="symboles/star.svg"></td>
            <td id="case9"><img src="symboles/pyramide.svg"></td>
            <td id="case10"><img src="symboles/penta.svg"></td>
            <td id="case11"></td>
          </tr>
        </table>
      </div>"""