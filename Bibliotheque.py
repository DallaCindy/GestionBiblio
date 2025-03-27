from Livre import Livre
class Bibliotheque :
    def __init__(self,livres=[]):
        self.livres = livres
    
    def ajouter_livre(self) :
        Livres={
        "titre" : Livre.titre,
        "auteur" : Livre.auteur,
        "annee_publication" : Livre.annee_publication,
        "ISBN" : Livre.isbn}
        self.livres.append(Livres)
        # db = livres()
        # livres.open()
        # db.write({
        #    "titre" : Livre.titre,
        #    "auteur" : Livre.auteur,
        #    "annee_publication" : Livre.annee_publication,
        #    "INBN" : Livre.isbn
        # })

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
