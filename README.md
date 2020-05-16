# CSE182_Project

CSE 182 Project 2020: Understanding the SARS-CoV-2 (Severe acute respiratory
syndrome coronavirus

1. Record your team number by writing names of team members on the sign-up page. Your team
number is the row that you sigend up on.

2. Download the reference SARS-CoV-2 genome from the course website.

3. Write your own code to identify all open reading frames (mostly genes) in the genome. In this
definition, a gene is described by a 3-tuple hs, e, fi > describing start coordinate, end coordinate,
and frame. Count the number of genes that you predicted.

4. Sort all genes by their(a) starting location s (b) end location, e, and frame, f, in that order. In this
order, team i gets to choose 15 genes ranked 12i through 12i+ 14. Note that in this scheme, multiple
groups may end up working on the same gene, or small variants of the same gene. Feel free to confer
with other groups.

5. For all of your (Team i) genes, translate the gene into a conceptual protein sequence and identify its
function. To obtain its function, search the nr database using blastp, pfam, and prosite database.
Fill in the gene tuples and the function from the database hit on the genes page. In the comments
tab, fill in your best description of the function in English.

6. For each team i gene, search it against all available SARS-Cov-2 genomes and identify all mutations.
Each mutation is represented by its location on the original genome, the reference allele, the mutant
allele, and its frequency. This is more open-ended, and you can be creative here.

7. Open-ended. Do a literature search on the genes that you worked on and report on any interesting
findings. For example, do they have names? Are they targets for making vaccines, or therapeutics?
Have they been studied in other SARS related viruses in the past?
