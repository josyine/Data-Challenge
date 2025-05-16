# Chemin du fichier d'entrée et de sortie
input_file = "C:/Users/smohun/OneDrive - American International Group, Inc/Desktop/Data Challenge/instructions_list.txt"
output_file = "C:/Users/smohun/OneDrive - American International Group, Inc/Desktop/Data Challenge/instructions_list_cleaned.txt"

# Lire le fichier et filtrer les lignes
with open(input_file, "r", encoding="utf-8") as f:
    lines = f.readlines()

# Filtrer les lignes ne commençant pas par un chiffre et ne finissant pas par "]"
cleaned_lines = [line for line in lines if not line.strip().startswith(tuple("0123456789")) and not line.strip().endswith("]")]

# Enregistrer le nouveau fichier
with open(output_file, "w", encoding="utf-8") as f:
    f.writelines(cleaned_lines)

# Afficher le nombre de lignes restantes
print(f"Nombre de lignes dans le nouveau fichier : {len(cleaned_lines)}")
print(f"Fichier nettoyé enregistré dans : {output_file}")
