from flask import render_template, request, redirect, url_for
from flask import Blueprint
from models.joueur import Joueur
import json

views = Blueprint('views', __name__, template_folder='../templates')


nb_player =""

# Route principale pour la page d'accueil
@views.route('/')
def index():
    return render_template('index.html', nb_player=0)  # Passer nb_player avec une valeur initiale



# Route pour la configuration des joueurs
@views.route('/listeJoueur', methods=['POST'])
def config_joueur():

    global nb_player
    # Récupération des données du formulaire
    nb_player = request.form.get('quantity', "").strip()  
    rule = request.form.get('rule', "").strip()           

    # Vérification si les données existent
    if not nb_player or not rule:
        # Si une des valeurs est absente, retour à la page d'accueil
        return render_template('index.html', error="Veuillez remplir tous les champs.", nb_player=0, rule="")

    # Convertir nb_player en entier et gérer les erreurs
    try:
        nb_player = int(nb_player)
        if nb_player <= 1:  # S'assurer que nb_player est un entier superieur a 1 
            raise ValueError("Le nombre de joueurs doit être supérieur à 1.")
    except ValueError as e:
        return render_template('index.html', error=str(e), nb_player=0, rule=rule)

    # Si tout est valide, afficher la page listeJoueur.html
    return render_template('listeJoueur.html', nb_player=nb_player, rule=rule)



# Route pour débuter une partie de poker 
@views.route('/listeJoueur/jeu',methods=['GET', 'POST'])
def jeu():




    global nb_player

    # Charger le fichier JSON contenant les éléments du backlog
    with open('backlog.json', 'r') as f:
        data = json.load(f)

    backlog = data['backlog']
    
    # Récupérer le numéro de la question à partir de l'URL, sinon commencer à 1
    numero = 1

    # Chercher la question correspondant au numéro
    question = next((q for q in backlog if q["numero"] == numero), None)

    # Si la question existe, récupérer l'index pour savoir s'il y a une question suivante
    if question:
        # Nombre total de questions
        nb_items = len(backlog)
        next_question = numero + 1 if numero < nb_items else None
    else:
        question = {"numero": "Erreur", "titre": "Question non trouvée"}
        next_question = None






    nb_player = int(nb_player)
    joueurs = []
    if request.method == 'POST':
        for i in range(nb_player):
            # Récupérer le nom du joueur depuis le formulaire
            nom_joueur = request.form[f'player{i}']
            joueur = Joueur(nom_joueur)  # Créer une instance de Joueur
            joueurs.append(joueur)  # Ajouter à la liste des joueurs
        

    cartes = ["cartes_0.svg", "cartes_1.svg", "cartes_2.svg", "cartes_3.svg", 
              "cartes_5.svg", "cartes_8.svg", "cartes_13.svg", "cartes_20.svg", 
              "cartes_40.svg", "cartes_100.svg", "cartes_cafe.svg", "cartes_interro.svg"] 
    return render_template('jeu.html', cartes=cartes , nb_player=nb_player , joueurs=joueurs , question=question, numero=numero, next_question=next_question)

