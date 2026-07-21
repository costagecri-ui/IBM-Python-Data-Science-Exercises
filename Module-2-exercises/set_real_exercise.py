# gene list found in sample A and sample B
sample_A = ["BRCA1", "TP53", "EGFR", "BRCA1", "TNF", "TP53"]
sample_B = ["TP53", "EGFR", "MYC", "APOE", "TP53"]

# database of gene functions
gene_db = {
    "BRCA1": "DNA repair",
    "TP53": "Tumor suppressor",
    "EGFR": "Cell growth",
    "TNF": "Inflammation",
    "MYC": "Transcription factor"
}
#converting sample_A and sample_B to sets to remove duplicates
set_A = set(sample_A)
set_B = set(sample_B)

#Intersection of sample_A and sample_B
common_genes = set_A.intersection(set_B)
print("common genes in sample A and sample B:", common_genes)

#difference of sample_A and sample_B
unique_genes_A = set_A.difference(set_B)
print("Unique genes in sample A:", unique_genes_A)

#using the gene_db to get the function of the first gene in common_genes
gene_function = gene_db.get(list(common_genes)[0], "Function not found")
print("Function of the first common gene:", gene_function)
