from utils.parser import ask_input_file, ask_output_file, process_icd_to_output


def main():
    input_file = ask_input_file()
    if not input_file:
        print("Aucun fichier sélectionné. Fin du programme.")
        return

    output_file = ask_output_file()
    if not output_file:
        print("Aucun fichier de sortie sélectionné. Fin du programme.")
        return

    process_icd_to_output(input_file, output_file)
    print("Terminé avec succès !")

if __name__ == "__main__":
    main()
