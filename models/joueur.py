class Joueur:
    def __init__(self, nom):
        self.nom = nom  # Attribut pour le nom du joueur
    
    def __str__(self):
        return f"Joueur : {self.nom}"
