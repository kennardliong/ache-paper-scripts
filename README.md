calc.py -> calculates the chemical descriptor values for ligands based on an input of SMILES in a CSV
modr1.py -> takes in a scaffold, its R-group position as SMILES input and functional_groups.csv; creates modified ligand SMILES as output
functional_groups.csv -> contains a list of functional groups for use in modr1.py 
dock.py -> automates the molecular docking process, taking a CSV of ligands and a receptor as input, outputs the docking scores.
