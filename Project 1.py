# read the exclude list file
with open("exclude_list.tab","r") as exclude_list:
    # read the file contents
    exclude_readlist = exclude_list.read()

# remove all spaces from the exclude list
exclude_readlist = exclude_readlist.replace(" ", "")

# compile a regular expression to match scaffold names
import re
pattern = re.compile(r"scaffold\d{5}")
# find all scaffold names in the exclude list
compile_scaffold_list = re.findall(pattern, exclude_readlist)

# open the FASTA file in read mode
with open("Scaffolds.fasta","r") as scaffold_fasta:
    # open the output file in write mode
    with open("output1_fasta","w") as output1_fasta:
        # read the FASTA file line by line
        for line in scaffold_fasta:
            # strip the `>` character and newline from the header
            header = line.strip('>').strip('\n')
            # read the next line, which contains the sequence
            seq = scaffold_fasta.readline()
            # if the header is not in the exclude list, write the header and sequence to the output file
            if header not in compile_scaffold_list:
                output1_fasta.writelines('>'+header+'\n')
                output1_fasta.writelines(seq)


#Generate the Output file-2

#To generate a FASTA file where all sequences from exclude list have been removed + only the sequences that are
#not marked as “mitochondrion-not_cleaned” are trimmed/span of sequence removed.

#The aim is to compile all the scaffold names in a list

#Open trim list file

trim_list= open("trim_list.tab","r")
trim_list.readline()
for line in trim_list:
#To Remove the tab spaces
    trim_line= line.split("\t")
#The scaffolds are the respective sequences in the 1st position
    sequence=trim_line[0]
#The length of the sequences is in the 2nd position
    length=trim_line[1]
#The apparent source is mentioned in the 3rd position
    apparent_source=trim_line[3].rstrip('\n')
#The span of the reigeon that needs to be trimmed out from the sequences
    span=trim_line[2].split(',')
#Generate a dictionary where the scaffold is the key
    minimum_len=200
    dict_seq= {}
    dict_seq[sequence] = (length,span,apparent_source)
#Open the output1 file which is taken as the input file since the exclude
#list sequences are absent

with open("Output1.fasta","r") as output1_fasta:
    with open("output2_fasta","w")as output2_fasta:
        for line in output1_fasta:
# strip the header off of '>' and the spaces
            header=line.lstrip('>').strip("\n")
#assign the sequence syntax
            sequence=output1_fasta.readline()
#Scan the file to check if the header is the key value from the dictionary
            if dict_seq.get(header,None):
                data=dict_seq.get(header)
#If condition is true, let span 2 be the variable for the 1st position and
#Source 2 be the value for the second position
                span2= data[1]
                source2=data[2]
#Check if source 2 has 'mitochondrion-not-cleaned' mentioned in the script file
                if source2 == 'mitochondrion-not-cleaned':
#If it is present, then let the sequence be printed in the file- output 2 without trimming
                    seq_comp= ('Complete_sequence\n','>','header'+'\n',sequence+'\n')
#Write to the file output_2
                    output2_fasta.writelines(seq_comp)
#If the condtition is false then execute the alternate task
#Assign the starting position to be 0
                else:
                    p=0
# enumerate is used to loop over the elements of a list called span2. The index variable
# will be assigned the index of the current element in the list, and the i
# variable will be assigned the value of the current element in the list.
                    for ind, i in enumerate(span2):
                        ind=i.split('..')
#For each element in the span2 list,  split the element on the .. character and
# assigns the resulting list to the index variable. The first element is converted from an
# index list to an integer and assign it  'p_start variable'
                        p_start= int(ind[0])

# sub_sequence is another variable assigned  to the part of the sequence
# that starts at the value of p and ends at the value of p_start. Finally, it
# removes any N characters from the beginning and any 'Natgc' characters from the end of sub_sequence.
                        sub_sequence= sequence[p:p_start]
                        sub_sequence=sub_sequence.lstrip('N').rstrip('Natgc')
#if the length of sub_sequence is greater than or equal to minimum_len. Create new variable called trim_sequence
                        if len(sub_sequence) >= minimum_len:
# assign trim_sequence a tuple containing the string "Trimmed sequence\n", the > character, the value of the header variable,
# the _ character, the index variable converted to a string, the \n character, and the value of the sub_sequence variable
# with a \n character appended to the end.
                            trim_sequence=('Trimmed sequence\n','>',header,'_',str(ind),'\n',sub_sequence+'\n')
                            output2_fasta.writelines(trim_sequence)
#Convert the second element in the index list to an integer and assigns it to the p_seq_start variable.
                        p_seq_start= int(ind[1])
#if the length of sub_sequence is 'NOT' greater than or equal to minimum_len. Create new variable called sub_sequence
                    else:
# sequence that starts at the value of p_seq_start and ends at the end of the sequence (len(sequence))
                        sub_sequence=sequence[p_seq_start:len(sequence)]
#Remove any N characters from the beginning and any Natgc characters from the end of sub_sequence
                        sub_sequence=sub_sequence.lstrip('N').rstrip('Natgc')
#If the length of sub_sequence is greater than 200
                        if len(sub_sequence) >= minimum_len:
#Create a new variable called end_trim, tuple containing the string "end trim of seq\n", the > character,
# the value of the header variable, the \n character, and the value of the sub_sequence variable with a \n character
# appended to the end.
                            end_trim=('end trim of seq\n','>', header,'\n', sub_sequence + '\n')
                            output2_fasta.writelines(end_trim)
            else:
#If neither of the conditions are satisfied then,
#ate a new variable called compseq and assigns it a tuple containing the string "Complete sequence\n", the >
# character, the value of the header variable with a \n character appended to the end, and the value of the sequence
# variable with a \n character appended to the end.
                compseq= ('Complete sequence\n','>',header+'\n',sequence+'\n')
                output2_fasta.writelines(compseq)


#To generate Output 3

with open("output2_fasta","r") as output2_fasta:
    with open("output3_fasta","w")as output3_fasta:
        for line in output2_fasta:
# strip the header off of '>' and the spaces
            header1=line.lstrip('>').strip("\n")
#assign the sequence syntax
            sequence1=output2_fasta.readline()
#Scan the file to check if the header is the key value from the dictionary
            if dict_seq.get(header,None):
                data1=dict_seq.get(header)
#If condition is true, let span 2 be the variable for the 1st position and
#Source 2 be the value for the second position
                span3= data[1]
                source3=data[2]

# enumerate is used to loop over the elements of a list called span2. The index variable
# will be assigned the index of the current element in the list, and the i
# variable will be assigned the value of the current element in the list.
                for ind, i in enumerate(span3):
                    ind=i.split('..')
#For each element in the span2 list,  split the element on the .. character and
# assigns the resulting list to the index variable. The first element is converted from an
# index list to an integer and assign it  'p_start variable'
                    p_start1= int(ind[0])

# sub_sequence is another variable assigned  to the part of the sequence
# that starts at the value of p and ends at the value of p_start. Finally, it
# removes any N characters from the beginning and any 'Natgc' characters from the end of sub_sequence.
                    sub_sequence1= sequence1[p:p_start1]
                    sub_sequence1=sub_sequence1.lstrip('N').rstrip('Natgc')
#if the length of sub_sequence is greater than or equal to minimum_len. Create new variable called trim_sequence
                    if len(sub_sequence1) >= minimum_len:
                        trim_sequence1 = ('Trimmed sequence\n', '>', header1, '_', str(ind), '\n', sub_sequence1 + '\n')
# assign trim_sequence a tuple containing the string "Trimmed sequence\n", the > character, the value of the header variable,
# the _ character, the index variable converted to a string, the \n character, and the value of the sub_sequence variable
# with a \n character appended to the end.
                        output3_fasta.writelines(trim_sequence1)
#Convert the second element in the index list to an integer and assigns it to the p_seq_start variable.
                        p_seq_start1= int(ind[1])
#if the length of sub_sequence is 'NOT' greater than or equal to minimum_len. Create new variable called sub_sequence
                    else:
# sequence that starts at the value of p_seq_start and ends at the end of the sequence (len(sequence))
                        sub_sequence1=sequence1[p_seq_start1:len(sequence1)]
#Remove any N characters from the beginning and any Natgc characters from the end of sub_sequence
                        sub_sequence1=sub_sequence1.lstrip('N').rstrip('Natgc')
#If the length of sub_sequence is greater than 200
                        if len(sub_sequence1) >= minimum_len:
#Create a new variable called end_trim, tuple containing the string "end trim of seq\n", the > character,
# the value of the header variable, the \n character, and the value of the sub_sequence variable with a \n character
# appended to the end.
                            end_trim1=('end trim of seq\n','>', header1,'\n', sub_sequence1 + '\n')
                            output3_fasta.writelines(end_trim1)
            else:
#If neither of the conditions are satisfied then,
#ate a new variable called compseq and assigns it a tuple containing the string "Complete sequence\n", the >
# character, the value of the header variable with a \n character appended to the end, and the value of the sequence
# variable with a \n character appended to the end.
                compseq1= ('>',header1+'\n',sequence1+'\n')
                output3_fasta.writelines(compseq1)






















