# Creating a dictionary (cuople= key:value)
codon_dict = {
    "ATG": "Methionine",
    "GTC": "Valine",
    "TTA": "Leucine"
}

# print the name of the amminoacid associate to the codon "GTC"
print("The aminoacid for ATG is:", codon_dict["GTC"])

# Adding a new codon(couple key: value)
codon_dict["GGG"] = "Glycine"

# printing all dict to see if it printed the latest codon
print("Updated dictionary:", codon_dict)