import csv
import tkinter as tk
from tkinter import filedialog
from generator import generate_derived_parameters


def ask_input_file():
    """
    Ouvre une boîte de dialogue pour permettre à l'utilisateur
    de sélectionner un fichier CSV en entrée (fichier ICD).

    Retourne :
        str: Chemin complet du fichier sélectionné
    """

    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(
        title="Sélectionne le fichier ICD",
        filetypes=[("CSV files", "*.csv")]
    )
    return file_path


def ask_output_file():
    """
    Ouvre une boîte de dialogue pour permettre à l'utilisateur
    de choisir où enregistrer le fichier texte de sortie (.txt).

    Retourne :
        str: Chemin complet du fichier de sortie choisi
    """
    file_path = filedialog.asksaveasfilename(
        title="Fichier de sortie",
        defaultextension=".txt",
        filetypes=[("Text files", "*.txt")]
    )
    return file_path


def parse_icd_file(filepath):
    """
    Lit un fichier ICD (CSV) et extrait son contenu ligne par ligne
    en ignorant la ligne d'en-tête.

    Paramètres :
        filepath (str): Chemin du fichier CSV à lire

    Retourne :
        list[list[str]]: Liste des lignes du fichier, chaque ligne étant une liste de champs
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=';')
        next(reader)  # Ignorer l'en-tête
        return [row for row in reader]


def process_icd_to_output(input_file, output_file):
    """
    Traite le fichier ICD donné et génère un fichier texte contenant
    les lignes IADS dérivées.

    Étapes :
    - Lit le fichier ICD source
    - Génére les lignes dérivées avec `generate_derived_parameters`
    - Écrit les lignes dans un fichier texte déjà choisi

    Paramètres :
        input_file (str): Chemin du fichier CSV d'entrée
        output_file (str): Chemin du fichier texte de sortie
    """
    print(f"Lecture de : {input_file}")
    rows = parse_icd_file(input_file)

    print(f"Génération des lignes dérivées...")
    derived_lines = generate_derived_parameters(rows)

    print(f"Écriture dans : {output_file}")
    with open(output_file, 'w') as f:
        f.writelines(derived_lines)
