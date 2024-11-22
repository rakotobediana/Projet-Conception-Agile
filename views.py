from flask import render_template, request, redirect, url_for
from flask import Blueprint


views = Blueprint('views', __name__, template_folder='templates')

# Route principale pour la page d'accueil
@views.route('/')
def index():
    return render_template('index.html', nb_player=0)  # Passer nb_player avec une valeur initiale


# Route pour la configuration des joueurs
@views.route('/listeJoueur', methods=['GET', 'POST'])
def config_joueur():
    if request.method == 'POST':
        # Récupération des données du formulaire
        nb_player = request.form.get('quantity', 0)  # Valeur par défaut si vide
        rule = request.form.get('rule', "")
        
        # Convertir nb_player en entier, gérer les erreurs
        try:
            nb_player = int(nb_player)
        except ValueError:
            nb_player = 0  # Valeur par défaut si la conversion échoue
        
        # Transmettre les données au template
        return render_template('listeJoueur.html', nb_player=nb_player, rule=rule)
    
    # Si GET, affiche simplement le formulaire vide
    return render_template('index.html', nb_player=0, rule="")
