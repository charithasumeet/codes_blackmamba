# Import Sequence module
from Sequence_module import Sequence


class FASTQ(Sequence):

    def __init__(self, id='', desc='', seq='', length=0, pbsq='', gc=0, gcp=0, quality=0):
        # Initialize list to store sequences
        super(FASTQ, self).__init__(id, desc, seq, length, pbsq, gc, gcp)

        self.avg_quality_threshold = quality
        self.fastq_sequences = []

    def get_sequences(self):
        return self.fastq_sequences

    def get_avg_quality_threshold(self):
        print("yolo", self.avg_quality_threshold)
        return self.avg_quality_threshold

    def read(self, file_name):
        # Opens and reads the FASTQ file
        with open(file_name, 'r') as fastq_file:
            while True:
                header = fastq_file.readline().strip()
                if len(header) == 0:
                    break
                current_sequence = fastq_file.readline().strip()
                fastq_file.readline()
                quality_sequence = fastq_file.readline().strip()
                quality = []
                for i in range(0, len(quality_sequence)):
                    quality.append((ord(quality_sequence[i])-33))
                avg_quality = (sum(quality) / len(quality_sequence))
                list_words = header.split()
                seq_id = header.strip()
                seq_desc = header
                seq_len = len(current_sequence.strip()) + 1
                self.fastq_sequences.append(FASTQ(seq_id, seq_desc, current_sequence, seq_len, quality_sequence, 0, 0, avg_quality))

    def write(self, write_seq, file_name=None):
        # Open the file specified by filename in write mode
        if file_name:
            with open(file_name, 'a') as fastq_file:
                fastq_file.write(f"{write_seq.id}\n{write_seq.seq}\n+\n{write_seq.pbsq}\n")
        else:
            print(f"{write_seq.id}\n{write_seq.seq}\n+\n{write_seq.pbsq}")

    def count(self):
        # Returning the total number of sequences
        return len(self.fastq_sequences)

    def avg_length(self):
        # Calculating and returning the average length of sequences
        seq_sum = 0
        avg_length = 0
        total_sequences = self.count()
        for obj in self.fastq_sequences:
            seq_sum += int(obj.length)
        avg_length = seq_sum / total_sequences
        return avg_length

