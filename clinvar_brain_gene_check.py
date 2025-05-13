from Bio import Entrez

Entrez.email = "your@email.com"  # ← replace with your email

gene = input("Enter a brain gene (e.g., MECP2): ")

handle = Entrez.esearch(db="clinvar", term=f"{gene}[gene] AND Homo sapiens[orgn]")
record = Entrez.read(handle)
handle.close()

if record["IdList"]:
    print(f"✅ {gene} has clinical records in ClinVar.")
else:
    print(f"❌ No ClinVar records found for {gene}.")
