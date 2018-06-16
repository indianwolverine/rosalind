from Bio import Entrez
Entrez.email = "your_name@your_mail_server.com"
handle = Entrez.esearch(db="nucleotide", term='Sorex', mindate="2000/05/05", maxdate="2002/06/02")
record = Entrez.read(handle)
print(record["Count"])
