# Creating a dictionary (cuople= key:value)
codon_dict = {
    "ATG": "Methionine",
    "GTC": "Valine",
    "TTA": "Leucine"
}

# print the name of the amminoacid associate to the codon "ATG"
print("The aminoacid for ATG is:", codon_dict["ATG"])

# Adding a new codon(couple key: value)
codon_dict["GGG"] = "Glycine"

# printing all dict to see if it printed the latest codon
print("Updated dictionary:", codon_dict)

# editing an existing value using its key
codon_dict["TTA"]= "Modified Leucine"

print("after edit:", codon_dict)
# deleting codon GTC from the dict
del codon_dict ["GTC"]

print ("after cancellation of the GTC codon:", codon_dict)

# extracting specific data components from the dict
print("all the keys:", codon_dict.keys())
print("all the values:", codon_dict.values())

# if we search a value in the dict that isn't existing we're gonna have an error
# to avoid this situation we use the command .get()
print("Codone ATG:", codon_dict.get("ATG", "Not Found"))
print("Codone AAA (non esiste):", codon_dict.get("AAA", "Unknown codon"))
