import os

def extract_all_instructions(folder_path, output_file):
    instructions_set = set()
    
    for filename in os.listdir(folder_path):
        if filename.endswith(".json"):  # Vérifie si c'est un fichier JSON
            file_path = os.path.join(folder_path, filename)
            with open(file_path, "r", encoding="utf-8") as f:
                try:
                    lines = f.readlines()  # Lire le fichier ligne par ligne
                    
                    for line in lines:
                        # Extraire le mot après le 2ème ":"
                        parts = line.split(":")
                        if len(parts) > 2:
                            word_after_second_colon = parts[2].strip().split()[0]  # Prendre le premier mot après le deuxième ":"
                            instructions_set.add(word_after_second_colon)  # Utiliser .add() pour un seul mot
                except Exception as e:
                    print(f"Erreur de lecture du fichier {filename} : {e}")

    # Trier la liste et l'enregistrer dans un fichier
    sorted_instructions = sorted(instructions_set)
    with open(output_file, "w", encoding="utf-8") as f_out:
        for instr in sorted_instructions:
            f_out.write(instr + "\n")
    
    print(f"Nombre total d'instructions uniques : {len(sorted_instructions)}")
    print(f"Liste des instructions enregistrée dans : {output_file}")

# Exemple d'utilisation
folder_path = "C:/Users/smohun/OneDrive - American International Group, Inc/Desktop/Data Challenge/folder_training_set"
output_file = "C:/Users/smohun/OneDrive - American International Group, Inc/Desktop/Data Challenge/instructions_list.txt"

extract_all_instructions(folder_path, output_file)
