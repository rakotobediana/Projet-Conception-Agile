from flask import render_template, request, redirect, url_for
from flask import Blueprint


views = Blueprint('views', __name__, template_folder='templates')

# Route principale pour la page d'accueil
@views.route('/')
def index():
    return render_template('index.html', nb_player=0)  # Passer nb_player avec une valeur initiale


# Route pour la configuration des joueurs
@views.route('/listeJoueur', methods=['POST'])
def config_joueur():
    # Récupération des données du formulaire
    nb_player = request.form.get('quantity', "").strip()  # Valeur par défaut: chaîne vide
    rule = request.form.get('rule', "").strip()           # Valeur par défaut: chaîne vide

    # Vérification si les données existent
    if not nb_player or not rule:
        # Si une des valeurs est absente, retour à la page d'accueil
        return render_template('index.html', error="Veuillez remplir tous les champs.", nb_player=0, rule="")

    # Convertir nb_player en entier et gérer les erreurs
    try:
        nb_player = int(nb_player)
        if nb_player <= 1:  # S'assurer que nb_player est un entier positif
            raise ValueError("Le nombre de joueurs doit être supérieur à 1.")
    except ValueError as e:
        return render_template('index.html', error=str(e), nb_player=0, rule=rule)

    # Si tout est valide, afficher la page listeJoueur.html
    return render_template('listeJoueur.html', nb_player=nb_player, rule=rule)
  

@views.route('/jeu', methods=['POST'])
def jeu():
    message = "Message de test "
    return render_template('jeu.html' ,  message=message)