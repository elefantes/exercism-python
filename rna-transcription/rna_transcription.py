def to_rna(dna_strand):
    transcription_table = {"A": "U", "C": "G", "G": "C", "T": "A"}
    sequence = [transcription_table[n] for n in dna_strand]
    result = "".join(sequence)

    return result
