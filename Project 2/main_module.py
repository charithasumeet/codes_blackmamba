import os
from Sequence_module import Sequence
from fasta_module import FASTA
from fastq_module import FASTQ

pf = False


def fastq_to_fasta(input_file_path):

   # Conversion of a fastq to fasta file format

    input_file = open(input_file_path, 'r')
    output_file = open("converted_fastq.fasta", 'w')
    while True:
        # Read the input file contents
        header_contents = input_file.readline().strip()
        if len(header_contents) == 0:
            break
        mod_header_content = header_contents[1:].strip()
        bits = mod_header_content.split()
        sid = bits[0].strip()
        sequence_content = input_file.readline().strip()
        length=len(sequence_content)
        gc_count = sequence_content.count('G') + sequence_content.count('C')
        gc = gc_count
        gc_per = gc / length * 100
        input_file.readline()
        input_file.readline()
        header='>' + sid + " length: " + str(length) + " gc: " + str(gc) + " gcpercent: " + str(gc_per) + '\n'
        output_file.write(header)
        output_file.write(sequence_content + "\n")

    # Close the files
    input_file.close()
    output_file.close()
    return "converted_fastq.fasta"


#Function to identify if the file extension is fasta or fastq

def identify_file_extension(input_file):

    #To identify file extension of an input file and
    # To determines if the file contains a peptide or nucleotide sequence.

    # To obtain file extension
    file_name, extension = os.path.splitext(input_file)
    #print(extension)

    count = 0

    # If the extension is fasta
    if extension == '.fasta' or extension == '.fa' or extension == '.fna' or extension == '.ffn' or extension == '.faa' or extension == '.frn':
        print("File format is FASTA")
        extension = "fasta"
        # Open the file and read its contents
        file_handle = open(input_file, 'r')
        file_content = file_handle.read()

        # Split the file content by lines
        seq_list = file_content.splitlines()

        # Identify if the sequence is a peptide or nucleotide sequence
        peptide_letters = ['A', 'R', 'N', 'D', 'C' 'E', 'Q', 'G', 'H', 'I', 'L', 'K', 'M', 'F', 'P', 'S', 'T', 'W', 'Y', 'V']
        for letter in peptide_letters:
            if letter in seq_list[1]:
                count = 1
                break

        if count == 1:
            global pf
            print(file_name + '.' + extension + " has Peptide sequences")
            pf = True
        else:
            print(file_name + '.' + extension + " has Nucleotide sequences.")

    # For fastq extension:
    elif extension == '.fastq' or extension == '.fq':
        extension = "fastq"
        print("File type is FASTQ")
        print(file_name + "has Nucleotide sequences.")

    else:
        print("Invalid file type.")

    return extension


# Ask user to input file location/path
filename = input("Please enter file name with absolute path")

# Get the file extension type
file_ext = identify_file_extension(filename)

match file_ext:
    case 'fasta':
        fasta = FASTA()
        fasta.read(filename)
        total_sequences = fasta.count()
        print("Total number of sequences in file: ", total_sequences)
        sequences = fasta.get_sequences()
        if not pf:
            gc = list(sequence.gc for sequence in sequences)
            sum_gc = 0
            for seq_gc in gc:
                sum_gc += seq_gc
            avg_gc = sum_gc / total_sequences
            print("Average gc of sequences in file: ", avg_gc)
        seq_len = tuple(seq.length for seq in sequences)
        min_len = min(seq_len)
        print ("Minimum length of the sequence in file: ", min_len)
        max_len = max(seq_len)
        print("Maximum length of the sequence in file: ", max_len)
        avg_len = fasta.avg_length()
        print("Average length of the sequence in file: ", avg_len)

    case 'fastq':
        fastq = FASTQ()
        fastq.read(filename)
        total_sequences = fastq.count()
        print("Total number of sequences in file: ", total_sequences)
        sequences = fastq.get_sequences()
        seq_len = tuple(seq.length for seq in sequences)
        min_len = min(seq_len)
        print("Minimum length of the sequence in file: ", min_len)
        max_len = max(seq_len)
        print("Maximum length of the sequence in file: ", max_len)
        avg_len = fastq.avg_length()
        print("Average length of the sequence in file: ", avg_len)

    case default:
        print ("please enter valid filename")
        exit()

print("1. Convert FASTQ files to FASTA ")
print("2. Output sequences based on minimum sequence length")
print("3. Output sequences based on Average quality threshold")
choice = input("Kindly please select an option(1-3)")
output_choice = input ("Kindly press Y if you want the input in a file or N to view the output on the screen")
if output_choice == 'Y' or output_choice == 'y':
    filenm = input("Please enter the output file Name")

match choice:
    case '1':
        if file_ext == 'fastq':
            new_file = fastq_to_fasta(filename)
            print ("File successfull converted to", new_file)
        else:
            asequences = fasta.get_sequences()
            for i in range (0, len(asequences)):
                fasta.write(asequences[i])
    case '2':
        min_len = input("Enter minimum sequence length criteria")
        if file_ext == 'fastq':
            qsequences = fastq.get_sequences()
            seq_len = list(seq.length for seq in qsequences)
            seq_list = []
            for leng in range(0, len(seq_len)):
                if seq_len[leng] >= int(min_len):
                    seq_list.append(leng)
            if output_choice == 'Y' or output_choice == 'y':
                for i in seq_list:
                    fastq.write(qsequences[i], filenm)
            else:
                for i in seq_list:
                    fastq.write(qsequences[i])
        else:
            asequences = fasta.get_sequences()
            seq_len = list(seq.length for seq in asequences)
            seq_list = []
            for leng in range(0, len(asequences)):
                if seq_len[leng] >= min_len:
                    seq_list.append(leng)
            if output_choice == 'Y' or output_choice == 'y':
                for i in seq_list:
                    fasta.write(asequences[i], filenm)
            else:
                for i in seq_list:
                    fasta.write(asequences[i])

    case '3':
        min_avg_threshold_quality = input("Enter minimum average quality threshold criteria")
        sequences = fastq.get_sequences()
        avg_list = list(seq.avg_quality_threshold for seq in sequences)
        seq_list = []
        for leng in range(0, len(sequences)):
            if avg_list[leng] >= float(min_avg_threshold_quality):
                seq_list.append(leng)
        if output_choice == 'Y' or output_choice == 'y':
            for i in seq_list:
                fastq.write(sequences[i], filenm)
        else:
            for i in seq_list:
                fastq.write(sequences[i])

    case default:
        print("Sorry Wrong Option. Ending Program")
