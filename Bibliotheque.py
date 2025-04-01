from Livre import Livre
import json
class Bibliotheque :
    def __init__(self,livres=[], fichier_json="db.json"):
        self.livres = livres
        self.fichier_json = fichier_json
    def charger_donnees(self) :
        try :
            with open(self.fichier_json, "wt") as f :
                self.livres =json.load(f)
        except FileNotFoundError :
            self.livres = []

    def ajouter_livre(self) :

        with open(self.fichier_json, "wt") as f :
            json.dump(self.livres, f, indent=2)

        Livres={
        "titre" : Livre.titre,
        "auteur" : Livre.auteur,
        "annee_publication" : Livre.annee_publication,
        "ISBN" : Livre.isbn}
        self.livres.append(Livres)

        

    def supprimer_livres(self,isbn_cible) :
        
        for livre in self.livres :
            if isbn_cible == Livre.isbn :
             del self.livres[livre]
             return f" Le livre dont l'isbn { isbn_cible} est {livre} supprime avec succes"
            try :
                isbn_cible != Livre.isbn
            except "isbnError" :
                print("ISBN introuvable")
               
    def rechercher_par_titre(self, titre_recherche) :

        for livre in self.livres :
            if titre_recherche == Livre.titre :
                return f"livre recherche : -{livre}"
            try :
                titre_recherche != Livre.titre 
            except "titreError" :
                print("titre intouvable")


biblio = Bibliotheque(livres="bibli_livres")
biblio.ajouter_livre(Objet1)