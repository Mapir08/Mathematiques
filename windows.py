from tkinter import *
from tkinter.messagebox import *
from calculs import *
from threading import Thread
from time import *


class FenetreP(Thread):

    def __init__(self):
        Thread.__init__(self)
        self.color_fond_1 = "#4065A4"  # Bleu
        self.color_fond_0 = "#8DB1F0"  # Bleu plus clair
        self.police_0 = "DK Crayon Crumble"  # Droit effet crayon
        self.police_1 = "Amandine"  # Arrondi fort enfant
        self.police_2 = "kindergarten"
        self.color_text = "#1B2B44"
        """ Définission des attributs utilisé """
        self.page = 0
        self.vers = ""
        self.resultat = 0
        self.trouvee = 0
        self.quoi = ""
        """ Création de la fenetre principale """
        self.fenetre = Tk()
        self.fenetre.title("Mathématiques CE1, by MAPIR")
        self.fenetre.maxsize(1280, 800)
        self.fenetre.config(background=self.color_fond_0)
        """ Création du menu """
        menubar = Menu(self.fenetre)
        menu0 = Menu(menubar, tearoff=0)
        menu0.add_command(label="Calculs Posé", command=self.fenetre_calculspose)
        menu0.add_command(label="Tables Multiplication", command=self.fenetre_tablesmultiplication)
        menu0.add_command(label="ChronoMaths", command=self.fenetre_chronomaths)
        menu0.add_separator()
        menu0.add_command(label="Quitter", command=quit)
        menubar.add_cascade(label="Fichier", menu=menu0)
        menu1 = Menu(menubar, tearoff=0)
        menu1.add_command(label="Aide")
        menubar.add_cascade(label="?", menu=menu1)
        self.fenetre.config(menu=menubar)
        """ Démarrage fenetre d'acceuil """
        self.run()
        """ Boucle pour fenetre principale """
        self.fenetre.mainloop()

    def definir_dimension_fenetre(self, dimension=None):
        if not dimension:  # Definission d'une dimension par défaut si pas demandé
            dimension = "500x500"
        self.fenetre.geometry(dimension)
        dim = dimension.split("x")
        dim_x = dim[0]
        dim_y = dim[1]
        self.fenetre.minsize(dim_x, dim_y)

    def clear(self):
        liste = self.fenetre.slaves()
        for widget in liste:
            widget.destroy()

    def creer_titre(self, text_titre):
        titre = Label(self.fenetre, text=text_titre, font=(self.police_0, 40), bg=self.color_fond_0, fg=self.color_text)
        titre.pack(pady=15)

    def creer_bouton_quitter(self):
        Button(self.fenetre, highlightthickness=0, font=(self.police_1, 20), width=10, text="Quitter",
               command=quit).pack(side=BOTTOM, pady=15)

    def creer_bouton(self, nom, command):
        Button(self.fenetre, highlightthickness=0, font=(self.police_1, 30), width=15, text=nom, command=command).pack(pady=15)

    def creer_bouton_retour(self):
        Button(self.fenetre, highlightthickness=0, font=(self.police_1, 20), width=10, text="Retour",
               command=self.run).pack(side=BOTTOM, pady=15)

    def creer_bouton_suivant(self, page, vers):
        self.page = page
        self.vers = vers
        frame = Frame(self.fenetre, bg=self.color_fond_0)
        frame.pack(side=BOTTOM, pady=15)
        Label(frame, text="{} / 20".format(page), bg=self.color_fond_0, font=(self.police_0, 20)).pack(side=LEFT, padx=20)
        Button(frame, highlightthickness=0, font=(self.police_1, 20), width=10, text="Suivant", command=self.verification_suivant).pack(side=RIGHT, padx=20)

    def verification_suivant(self):
        #  FAIRE UN SUIVI DU NOMBRE D'ERREURS
        try:
            if self.vers == "Tables de Multiplication":
                self.trouvee = int(self.result.get())
            else:
                self.trouvee = int(self.m_result.get() + self.c_result.get() + self.d_result.get() + self.u_result.get())
            if self.page < 20:
                if self.resultat == self.trouvee:
                    self.page += 1
                    if self.vers == "Calculs Posé":
                        self.fenetre_calculspose(self.page)
                    elif self.vers == "Calculs Posé Multiplication" or self.vers == "Tables de Multiplication":
                        self.go_multiplication(self.page)
                else:
                    showinfo("Dommage", "Ce n'est pas le bon résultat")
            else:
                self.run()
        except:
            showinfo("Attention", "Tu n'as rien rempli.")

    def afficher_calculspose(self, resultat, valeur_a, valeur_b, signe):
        # Création de Frame et positionnement valeurs
        frame_valeurs = Frame(self.fenetre, bg=self.color_fond_0)  # Obligatoire pour la grille car grid et pack incompatible
        frame_valeurs.pack()
        if signe == "+" or signe == "x":
            if signe == "+":
                Spinbox(frame_valeurs, bg=self.color_fond_0, relief=FLAT, highlightthickness=0, width=1, from_=0, to=1).grid(row=1, column=1)  # report
                Spinbox(frame_valeurs, bg=self.color_fond_0, relief=FLAT, highlightthickness=0, width=1, from_=0, to=1).grid(row=1, column=3)  # report
                Spinbox(frame_valeurs, bg=self.color_fond_0, relief=FLAT, highlightthickness=0, width=1, from_=0, to=1).grid(row=1, column=5)  # report
            elif signe == "x":
                Spinbox(frame_valeurs, bg=self.color_fond_0, relief=FLAT, highlightthickness=0, width=1, from_=0, to=9).grid(row=1, column=3)  # report > 1
                Spinbox(frame_valeurs, bg=self.color_fond_0, relief=FLAT, highlightthickness=0, width=1, from_=0, to=9).grid(row=1, column=5)  # report > 1
            # Pour un affichage correct => INUTILISE
            Label(frame_valeurs, bg=self.color_fond_0, width=2).grid(row=3, column=2)
            Label(frame_valeurs, bg=self.color_fond_0, width=2).grid(row=3, column=4)
            Label(frame_valeurs, bg=self.color_fond_0, width=2).grid(row=3, column=6)
        elif signe == "-":
            Spinbox(frame_valeurs, bg=self.color_fond_0, relief=FLAT, highlightthickness=0, width=1, from_=0, to=1).grid(row=2, column=4)  # report
            Spinbox(frame_valeurs, bg=self.color_fond_0, relief=FLAT, highlightthickness=0, width=1, from_=0, to=1).grid(row=2, column=6)  # report
            Spinbox(frame_valeurs, bg=self.color_fond_0, relief=FLAT, highlightthickness=0, width=1, from_=0, to=1).grid(row=3, column=2)  # report
            Spinbox(frame_valeurs, bg=self.color_fond_0, relief=FLAT, highlightthickness=0, width=1, from_=0, to=1).grid(row=3, column=4)  # report
        # Valeur A
        if valeur_a > 99:
            Label(frame_valeurs, text=int(valeur_a / 100), bg=self.color_fond_0, width=1, font=(self.police_2, 60)).grid(row=2, column=3)
        else:
            Label(frame_valeurs, text="", bg=self.color_fond_0, width=1, font=(self.police_2, 60)).grid(row=2, column=3)
        if valeur_a > 9:
            Label(frame_valeurs, text=int((valeur_a % 100) / 10), bg=self.color_fond_0, width=1, font=(self.police_2, 60)).grid(row=2, column=5)
        else:
            Label(frame_valeurs, text="", bg=self.color_fond_0, width=1, font=(self.police_2, 60)).grid(row=2, column=5)
        Label(frame_valeurs, text=int((valeur_a % 100) % 10), bg=self.color_fond_0, width=1, font=(self.police_2, 60)).grid(row=2, column=7)
        Label(frame_valeurs, text=signe, bg=self.color_fond_0, font=(self.police_0, 80)).grid(row=3, column=1)
        # Valeur B
        if valeur_b > 99:
            Label(frame_valeurs, text=int(valeur_b / 100), bg=self.color_fond_0, width=1, font=(self.police_2, 60)).grid(row=3, column=3)
        else:
            Label(frame_valeurs, text="", bg=self.color_fond_0, width=1, font=(self.police_2, 60)).grid(row=3, column=3)
        if valeur_b > 9:
            Label(frame_valeurs, text=int((valeur_b % 100) / 10), bg=self.color_fond_0, width=1, font=(self.police_2, 60)).grid(row=3, column=5)
        else:
            Label(frame_valeurs, text="", bg=self.color_fond_0, width=1, font=(self.police_2, 60)).grid(row=3, column=5)
        Label(frame_valeurs, text=int((valeur_b % 100) % 10), bg=self.color_fond_0, width=1, font=(self.police_2, 60)).grid(row=3, column=7)
        # Trait
        canvas = Canvas(self.fenetre, width="320", height="20", bg=self.color_fond_0, highlightthickness=0)
        canvas.pack()
        canvas.create_line(0, 0, 300, 0)
        # Resultat
        frame_resultat = Frame(self.fenetre, bg=self.color_fond_0)
        frame_resultat.pack()
        self.m_result = StringVar()
        self.c_result = StringVar()
        self.d_result = StringVar()
        self.u_result = StringVar()
        Entry(frame_resultat, bg=self.color_fond_1, width=1, font=(self.police_2, 60), highlightthickness=0, textvariable=self.m_result).grid(row=1, column=1)
        Entry(frame_resultat, bg=self.color_fond_1, width=1, font=(self.police_2, 60), highlightthickness=0, textvariable=self.c_result).grid(row=1, column=3)
        Entry(frame_resultat, bg=self.color_fond_1, width=1, font=(self.police_2, 60), highlightthickness=0, textvariable=self.d_result).grid(row=1, column=5)
        Entry(frame_resultat, bg=self.color_fond_1, width=1, font=(self.police_2, 60), highlightthickness=0, textvariable=self.u_result).grid(row=1, column=7)
        # Pour un affichage correct => INUTILISE
        Label(frame_resultat, borderwidth=1, bg=self.color_fond_0, width=2).grid(row=1, column=2)
        Label(frame_resultat, borderwidth=1, bg=self.color_fond_0, width=2).grid(row=1, column=4)
        Label(frame_resultat, borderwidth=1, bg=self.color_fond_0, width=2).grid(row=1, column=6)
        # Transfert des informations
        self.resultat = resultat
        """# Pour le temps de la programmation
        pose = Label(self.fenetre, text="{}".format(self.resultat), bg=self.color_fond_0)
        pose.pack()"""

    def afficher_calculsligne(self, resultat, valeur_a, valeur_b, signe):
        frame = Frame(self.fenetre, bg=self.color_fond_0)
        frame.pack(pady=15)
        self.result = StringVar()
        self.resultat = resultat
        Label(frame, text="{} {} {} = ".format(valeur_a, signe, valeur_b), font=(self.police_0, 50), bg=self.color_fond_0).pack(side=LEFT)
        Entry(frame, bg=self.color_fond_1, font=(self.police_0, 50), highlightthickness=0, width=5, textvariable=self.result, justify=CENTER).pack(side=RIGHT)

    def afficher_tablesmultiplication(self, quoi):
        self.quoi = quoi
        frame = Frame(self.fenetre, bg=self.color_fond_0)  # Obligatoire pour la grille car grid et pack incompatible
        frame.pack()
        self.choix = IntVar()
        for i in range(2, 10):
            Radiobutton(frame, text="Table des {}".format(i), font=(self.police_0, 30), bg=self.color_fond_0, variable=self.choix, value=i)\
                .grid(row=i, column=1, pady=10)
        Button(frame, text="Go", highlightthickness=0, font=(self.police_1, 30), width=4, command=self.go_multiplication).grid(row=5, column=2, padx=40)

    def afficher_chronomaths(self):
        frame = Frame(self.fenetre, bg=self.color_fond_0)
        frame.pack(pady=15)
        for ligne in range(10):
            for colonne in range(1, 6, 2):
                resultat, valeur_a, valeur_b, signe = choix_chrono()
                Label(frame, text="{} {} {} = ".format(valeur_a, signe, valeur_b), font=(self.police_0, 48), bg=self.color_fond_0)\
                    .grid(row=ligne, column=colonne, sticky=E)
                Entry(frame, bg=self.color_fond_1, font=(self.police_0, 48), highlightthickness=0, width=5, justify=CENTER)\
                    .grid(row=ligne, column=colonne+1, padx=10)
        Button(self.fenetre, highlightthickness=0, font=(self.police_1, 20), width=10, text="00:00").pack(pady=20)

    def go_multiplication(self, page=None):
        if not page:
            page = 1
        self.clear()
        self.creer_bouton_retour()
        if self.quoi == "calculs":
            self.definir_dimension_fenetre()
            self.creer_titre("Calculs Posé Multiplication")
            resultat, valeur_a, valeur_b, signe = multiplication(self.choix.get())
            self.afficher_calculspose(resultat, valeur_a, valeur_b, signe)
            self.creer_bouton_suivant(page, "Calculs Posé Multiplication")
        elif self.quoi == "tables":
            self.definir_dimension_fenetre("500x300")
            self.creer_titre("Tables de Multiplication")
            resultat, valeur_a, valeur_b, signe = table_multiplication(self.choix.get())
            self.afficher_calculsligne(resultat, valeur_a, valeur_b, signe)
            self.creer_bouton_suivant(page, "Tables de Multiplication")

    def run(self):
        try:
            self.clear()
        finally:
            self.definir_dimension_fenetre()
            """ Titre """
            self.creer_titre("Mathématiques - CE1")
            """ Création des boutons de choix + Quitter """
            self.creer_bouton("Calculs posé Plus et Moins", self.fenetre_calculspose)
            self.creer_bouton("Calculs posé Fois", self.fenetre_calculsmultiplication)
            self.creer_bouton("Tables de Multiplication", self.fenetre_tablesmultiplication)
            self.creer_bouton("Chronomaths", self.fenetre_chronomaths)
            self.creer_bouton_quitter()

    def fenetre_calculspose(self, page=None):
        if not page:
            page = 1
        self.clear()
        self.definir_dimension_fenetre()
        self.creer_titre("Calculs Posé")
        resultat, valeur_a, valeur_b, signe = choix_add_sous()
        self.afficher_calculspose(resultat, valeur_a, valeur_b, signe)
        self.creer_bouton_retour()
        self.creer_bouton_suivant(page, "Calculs Posé")

    def fenetre_calculsmultiplication(self):
        self.clear()
        self.definir_dimension_fenetre("500x600")
        self.creer_titre("Tables de Multiplication")
        self.afficher_tablesmultiplication("calculs")  # prévoir un choix pour dire c'est lequel
        self.creer_bouton_retour()

    def fenetre_tablesmultiplication(self):
        self.clear()
        self.definir_dimension_fenetre("500x600")
        self.creer_titre("Tables de Multiplication")
        self.afficher_tablesmultiplication("tables")  # prévoir un choix pour dire c'est lequel
        self.creer_bouton_retour()

    def fenetre_chronomaths(self):
        self.clear()
        self.definir_dimension_fenetre("1280x800")
        self.creer_titre("ChronoMaths")
        self.afficher_chronomaths()
        self.creer_bouton_retour()


class Chronometre (Thread):

    def __init__(self):
        Thread.__init__(self)

    def run(self):
        print("test")
