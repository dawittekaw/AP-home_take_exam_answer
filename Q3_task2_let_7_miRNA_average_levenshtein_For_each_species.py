'''
Created on May 22, 2023

@author: user
'''
import os
import Levenshtein

def calculate_levenshtein_distance(file_path):
    if not os.path.isfile(file_path):
        print("The specified file does not exist.")
        return

    species_let7_sequences = {}

    with open(file_path, 'r') as file:
        species_code = ""
        sequence = ""
        for line in file:
            if line.startswith('>'):
                if species_code and sequence:
                    species_let7_sequences.setdefault(species_code, []).append(sequence)

                species_code = line[1:].strip().split("let-7")[0]
                sequence = ""
            else:
                sequence = line.strip()

        # Store the last species code and sequence outside the loop
        if species_code and sequence:
            species_let7_sequences.setdefault(species_code, []).append(sequence)

    for species_code, sequences in species_let7_sequences.items():
        total_distance = 0
        total_sequences = len(sequences)

        if total_sequences < 2:
            continue

        for i in range(total_sequences - 1):
            for j in range(i + 1, total_sequences):
                total_distance += Levenshtein.distance(sequences[i], sequences[j])

        average_distance = total_distance / (total_sequences * (total_sequences - 1) / 2)
        print(f"Average Levenshtein distance for let-7 miRNA in species '{species_code}': {average_distance:.2f}")

    species_count = len(species_let7_sequences)
    #print(f"Total count of species: {species_count}")

# File path
file_path = r"C:\Users\user\programing\day1\data\mature.fa"

calculate_levenshtein_distance(file_path)
