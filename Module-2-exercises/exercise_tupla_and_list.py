# =====================================================================
# PART 1: LISTS (we can edit)
# =====================================================================

# This is an list of codons extracted form a dna
codon_list = ["ATG", "GTC", "TTA", "GGC", "AAA"]

print("1. Our start list", codon_list)

#access to the elements (indices always starts from zero)
print("first codon (index 0):", codon_list[0]) #extract ATG
print("last codon (index -1):", codon_list[-1]) #extract AAA

#SLICING: is used to extract a sub-sequence
#we want to extract form second codon (index 1) to fourth codon (index 3)
#final index is not included, so we're witing [1:4] to take codons 1,2,3
sub_sequence= codon_list[1:4]
print("Extracted sub sequence [1:4]:", sub_sequence )
#lists are editable: i've changed the codon "TTA" in "CCC"
codon_list[2] = "CCC"
print("updated_codon_list:", codon_list)

#=======================================================================
#PART 2: TUPLAS (unlike the lists, tuplas are not editable)
#=======================================================================
#are used with data that cannot change ever, even for mistake.
#for exemple the coordinates of a gene:
gene_position =(4857,8984) #start and finish of the gene
print("\n 2.The gene have the coordinates:", gene_position)
print("start of the gene:", gene_position[0])
#gene_position [0] = 5000 --> this demonstrate that the tupla cannot be changed (to use the code and see the error, delete "#")

last_three = codon_list[-3:]
print("Last_three_codons:", last_three)
