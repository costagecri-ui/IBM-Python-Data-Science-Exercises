# Creating a sequence of unique  nitrogenous bases
bases_set = {"A","C","G","T","A","C" }

# printing the set to see 
# how duplicates are removed automatically
print("Unique bases in set:", bases_set)

# convert a list with duplicate aminoacids
# into a set
amino_acid_list = ["Met","Val","Leu", "Met", "Val", "Ala"]
unique_amino_acid = set(amino_acid_list)

# print results
print ("Original amminoacid list:", amino_acid_list)
print ("unique amminoacid lists:",unique_amino_acid )

## INTERSECTION: operation between sets
sample_1 = {"GenA","GenB","GenC"}
sample_2 = {"GenB","GenC","GenD"}

# finding common elements
common_genes = sample_1.intersection(sample_2)
print("Common genes list:", common_genes)

## UNION FUNCTION: combines all elements from both sets
all_genes = sample_1.union(sample_2)
print("All unique genes:", all_genes)

## DIFFERENCE FUNCTION: elements in sample_1 that there are not in sample_2
unique_to_sample_1 = sample_1.difference(sample_2)
print("Genes unique to sample 1", unique_to_sample_1)
