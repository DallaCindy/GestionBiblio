class Livre :
    def __init__(self,titre, auteur, annee_publication, isbn):
   
        self.titre = titre
        self.auteur = auteur

        self.annee_publication = int(annee_publication)
        
        
        if self.annee_publication > 1900 :
            return "annee de publication valide"
        try :
            self.annee_publication < 1900 
            raise ValueError("Annee invalide")
        except ValueError as AnneeInvalideErro   :
            print(AnneeInvalideErro)

        self.isbn = isbn
        if len(self.isbn) == 10 :
            return " isbn valide"
        try :
            len(self.isbn) != 10
            raise ValueError("ISBN invalide")
        except ValueError as ISBNinvalideError :
            print(ISBNinvalideError)
    def Affiche_livre(self) :
        return f"\
            titre : {self.titre},\n\
            Auteur : {self.auteur},\n\
            Annee de la Publication : {self.annee_publication},\n\
            ISBN : {self.isbn}"

Objet1 = Livre("Le Petit Prince", "Antoine de Saint-Exupéry", "1920", "Panierwgrq")     
print(Objet1.Affiche_livre)


                
    
    



    