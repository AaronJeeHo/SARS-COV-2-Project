def parse_fasta(fasta_file):
    sequence = ''
    with open(fasta_file) as f:
        for line in f:
            if not line.startswith(">"):
                sequence += line.strip()

    return sequence
