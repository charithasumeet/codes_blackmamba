1.
import re

# Define a list of email addresses
email_addresses = [
  "jaysheel@udel.edu",
  "jaysheel@dbi.udel.edu",
  "jaysheel@google.com",
  "jaysheel.bhavsar@domain.co.au",
  "jaysheel_bhavsar@subdomain.domain.net",
  "jaysheel@goog.co",
  "jaysheel@extension",
  "jaysheel-bhavsar@domain.ext"
]

# For compiling the regular expression
regex = re.compile(r"[^(A-Z0-9.-_)]+@[A-Za-z]+\.[a-z.+]{2,5}")

# Loop through the list of email addresses
for email in email_addresses:
  # Check if the email address is valid
  if regex.match(email):
    print("Valid email address: {}".format(email))
  else:
    print("Invalid email address: {}".format(email))

2.
import re

# Define a DNA string to process
dna_string = "GTCA"

# Define a regular expression pattern to match and replace the DNA bases
regex_pattern = "(A)|(T)|(C)|(G)"
regex_replacement = "\1T\2A\3G\4C"

# Use the re.sub() method to apply the pattern to the DNA string
complement_string = re.sub(regex_pattern, regex_replacement, dna_string)

# Reverse the complement string to get the reverse complement
reverse_complement = complement_string[::-1]

# Print the result
print("Reverse complement: {}".format(reverse_complement))

3.
import re

# Define a chemical formula to process

formula1=input("Enter formula:")
formula=formula1

# Define a regular expression pattern to match and extract the element symbols and counts
regex_pattern = "([A-Z][a-z]?)([0-9]*)"

# Compile the regular expression pattern
regex = re.compile(regex_pattern)

# Use the re.findall() method to extract all matches from the formula
matches = regex.findall(formula)

# Loop through the matches and print the element symbols and counts
for match in matches:
  # Get the element symbol and count from the match
  symbol, count = match

  # If the count is empty, set it to 1
  if not count:
    count = 1

  # Print the element symbol and count
  print("Element: {}, Count: {}".format(symbol, count))


4.
import re

# Define the input string
input_string = "Peter Piper picked a peck of pickled peppers. Did Peter Piper pick a peck of pickled peppers? If Peter Piper picked a peck of pickled peppers, where's the peck of pickled peppers Peter Piper picked?"

# To extract all the words starting with "p" or "P"
words = re.findall("[pP]\w+", input_string)

# Loop through the list of matched words and print
for word in words:
  print(word)

5.
P = "CTTAAAAGCG"

C = "CGCTTTTAAGACTTAAAAGCGTTTGCTATGGACCTTAAAAGCGATCCACTTAAAAGCGTCTTAAAAGCGAACTTAAAAGCGGCGATTTGTCCTGCCTGAGTGCGGAATCAGAGGTTGATGTGTTGATGGACTCGAGTCATACAAGCGGAACTAGATACGGGGGGACTTCACCTGCGTTCTCAACTGCAGATCTAGAAGTGTTGATGTAGCTAGCACTCCAGAACGACTGTTTAACTTGGAGACCTCTCGTACAACATTTCGTTTCCGACACCCGTGTATAGGCGTCAAGAACGGAACCCGTATCTTAGAGGGGGATTCTCTTTTCTTACTCAAATTTGTGGCGGAATAACCGCGAATGAATCAACTGTATGCGGCTCTACTATGTGTAGATCATTTCGCATCAGCACCCAGAGCGCCCAGTGCAATACTGGTTGCCAGTTGCGCTGTATCCTTGACCCAGATGATAGTCCTAGGATCTAGGCCCGCGCAAACACCCTAACAACTAGTTATCCCAACATTCGCCGCCAAAAGGGTCAACAAGAGCGGGGCTGGAACTTCATCGCTTTTGCTATGAGGTTAAAACATCGGTACAGAGAACCCCCGGTGCAGGGAGGGGATGGGTATTGGGAACAAGATATACGAGCCGGAGCAAAGCGTCATTACCCATGTGTAGGAACACGGGGTTCAAAGTAGTCCACAATCCACGATCGATTCCCATGAACCTGGCCATATGAGCCAAGTCGTACTATAAGAAGCCTCTCCGCGCCTACGCCGCACGTTTTAAGGCCGTTTATCTTCCGTGATACTGGGTCGGTGTGC"

#1.To find the reverse compliment of P in C, and print its starting location
# Reverse the string P
P_reverse= reversed(P)
print(P_reverse)

A= "".join(P_reverse)
print(A)

#To find A in C
import re
pattern=re.compile(r'[GCGAAAATTC]')

match= C.find(r'[GCGAAAATTC]')
# Print the starting location (or -1 if not found)
print(match)

#2.To find all occurrence of P in C, and print any and all starting locations
#To find all occurences of P in C
import re

P = "CTTAAAAGCG"
C = "CGCTTTTAAGACTTAAAAGCGTTTGCTATGGACCTTAAAAGCGATCCACTTAAAAGCGTCTTAAAAGCGAACTTAAAAGCGGCGATTTGTCCTGCCTGAGTGCGGAATCAGAGGTTGATGTGTTGATGGACTCGAGTCATACAAGCGGAACTAGATACGGGGGGACTTCACCTGCGTTCTCAACTGCAGATCTAGAAGTGTTGATGTAGCTAGCACTCCAGAACGACTGTTTAACTTGGAGACCTCTCGTACAACATTTCGTTTCCGACACCCGTGTATAGGCGTCAAGAACGGAACCCGTATCTTAGAGGGGGATTCTCTTTTCTTACTCAAATTTGTGGCGGAATAACCGCGAATGAATCAACTGTATGCGGCTCTACTATGTGTAGATCATTTCGCATCAGCACCCAGAGCGCCCAGTGCAATACTGGTTGCCAGTTGCGCTGTATCCTTGACCCAGATGATAGTCCTAGGATCTAGGCCCGCGCAAACACCCTAACAACTAGTTATCCCAACATTCGCCGCCAAAAGGGTCAACAAGAGCGGGGCTGGAACTTCATCGCTTTTGCTATGAGGTTAAAACATCGGTACAGAGAACCCCCGGTGCAGGGAGGGGATGGGTATTGGGAACAAGATATACGAGCCGGAGCAAAGCGTCATTACCCATGTGTAGGAACACGGGGTTCAAAGTAGTCCACAATCCACGATCGATTCCCATGAACCTGGCCATATGAGCCAAGTCGTACTATAAGAAGCCTCTCCGCGCCTACGCCGCACGTTTTAAGGCCGTTTATCTTCCGTGATACTGGGTCGGTGTGC"

# Use finditer() to find all occurrences of P in C
matches = re.finditer(P, C)

# Print the starting index of each occurrence
for match in matches:
    print("P occurs at position", match.start())