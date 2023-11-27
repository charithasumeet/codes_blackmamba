from Sequence_module import Sequence


class FASTA(Sequence):

    def __init__(self, id='', desc='', seq='', length=0, pbsq='', gc=0, gcp=0):
        # Initialize list to store sequences
        super(FASTA, self).__init__(id, desc, seq, length, pbsq, gc, gcp)
        self.fasta_sequences = []

    def get_sequences(self):
        return self.fasta_sequences

    def read(self, file_name):
        # Open the FASTA file in read mode
        create_object = False
        with open(file_name, 'r') as fasta_file:
            current_sequence = ''  # Initialize a variable to store the current sequence
            for line in fasta_file:
                if line.startswith('>'):
                    # If the line starts with '>', it is a sequence ID
                    # Extract the sequence ID and create a new SEQ object
                    if create_object:
                        self.fasta_sequences.append(FASTA(seq_id, seq_desc, current_sequence, seq_len, 0, seq_gc, seq_gcp))
                        current_sequence = ''

                    list_words = line.split()
                    seq_id = line[1:8].strip()
                    seq_desc = line.strip()
                    seq_len = list_words[list_words.index("length:") + 1]
                    seq_gc = list_words[list_words.index("gc:") + 1]
                    seq_gcp = list_words[list_words.index("gcpercent:") + 1]

                else:
                    # If the line does not start with '>', it is a sequence
                    # Add the sequence to the current SEQ object
                    current_sequence += line.strip()
                    create_object = True
            # To create object for last line of the file
            self.fasta_sequences.append(FASTA(seq_id, seq_desc, current_sequence, seq_len, 0, seq_gc, seq_gcp))

    def write(self, sequence, file_name=None):
        # If a file name is provided, open the file in write mode
        # Otherwise, write the sequence to standard output
        if file_name:
            with open(file_name, 'a') as fasta_file:
                fasta_file.write(
                    f">{sequence.id} length: {sequence.length} gc: {sequence.gc} gcpercent: {sequence.gcpercent} \n{sequence.seq}\n")
        else:
            print(
                f">{sequence.id} length: {sequence.length} gc: {sequence.gc} gcpercent: {sequence.gcpercent} \n{sequence.seq}")

    def count(self):
        # Returning the total number of sequences
        return len(self.fasta_sequences)

    def avg_length(self):
        # Calculating and returning the average length of sequences
        seq_sum = 0
        avg_length = 0
        total_sequences = self.count()
        for obj in self.fasta_sequences:
            seq_sum += int(obj.length)
        avg_length = seq_sum / total_sequences
        return avg_length
