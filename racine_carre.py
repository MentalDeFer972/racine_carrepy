import tkinter as tk 
from tkinter import messagebox
import math

def calculer_racine_carre():
    try:
        nombre = float(entree_nombre.get())
        if nombre >= 0:
            racine = math.sqrt(nombre)
            messagebox.showinfo("Racine carré", f"La racine carrée de {nombre} est {racine}")
        else: 
            messagebox.showerror("Erreur","Le nombre doit être positif ou nul.")
    except ValueError:
        messagebox.showerror("Erreur","Veuillez entrer un nombre valide.")
    
fenetre = tk.Tk()
fenetre.title("Calcul de la racine carée")

label_nombre = tk.Label(fenetre, text = "Entrer un nombre : ")
label_nombre.pack()

entree_nombre = tk.Entry(fenetre)
entree_nombre.pack()

bouton_calculer = tk.Button(fenetre, text="Calculer la racine carré" , command=calculer_racine_carre)
bouton_calculer.pack()

fenetre.mainloop()
