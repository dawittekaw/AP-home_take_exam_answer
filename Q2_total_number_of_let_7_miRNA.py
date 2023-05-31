'''
Created on May 22, 2023

@author: user
'''
let7_count = 0

with open(r"C:\Users\user\programing\day1\data\mature.fa", "r") as file:

    for line in file:
        if line.startswith(">"):
            # Extract the miRNA name from the header line
            miRNA_name = line.strip()[1:]
            
            # Check if the miRNA name contains "let-7"
            if "let-7" in miRNA_name:
                let7_count += 1

print("Total number of let-7 miRNAs across all species:", let7_count)
