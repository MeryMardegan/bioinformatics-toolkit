# Import required libraries
from Bio.Seq import Seq
from Bio.SeqUtils import gc_fraction
from Bio import SeqIO

# Function for sequence input from a file
def input_from_file():
    file = input("Please enter the file name: ")
    for seq_record in SeqIO.parse(file, "fasta"):
        print(seq_record.id)
        print(seq_record.seq)
        return str(seq_record.seq)

# Function to calculate the frequency of bases in a sequence
def calculate_frequency(sequence):
    frequency = {base: sequence.count(base) for base in 'ATUCG'}
    return frequency

# Function to transcribe DNA
def transcription_DNA(sequence):
    DNA = Seq(sequence)
    return str(DNA.transcribe())

# Function to translate RNA
def translation_RNA(sequence):
    RNA = Seq(sequence)
    return str(RNA.translate())

# Function for the main menu
def menu1():
    print("\nMain Menu:")
    print("1. Input a sequence manually")
    print("2. Input a sequence from a file (.fasta)")
    print("3. Calculate content of a sequence")
    print("4. Transcribe a DNA sequence")
    print("5. Translate a DNA sequence")
    print("6. Exit")
    return input("Please enter your selection: ")

# Function to manage next steps after processing sequence
def menu3():
    print("\nWould you like to:")
    print("1. Input another sequence")
    print("2. Use the current sequence")
    print("3. Exit")
    return input("Please enter your selection: ")

if __name__ == "__main__":
    sequence = ""  # Initialize sequence variable
    while True:
        choice = menu1()  # Start with the main menu
        
        if choice == "1":  # Option 1: Manually input a sequence
            sequence = input("Please enter the sequence: ").upper()
            if not sequence:
                print("No sequence entered. Returning to main menu.")
                continue
            print("Sequence stored successfully. Returning to main menu.")
            continue  # Return to main menu
        
        elif choice == "2":  # Option 2: Input sequence from a file
            sequence = input_from_file()
            if not sequence:
                print("No sequence found in the file. Returning to main menu.")
                continue
            print("Sequence loaded successfully. Returning to main menu.")
            continue  # Return to main menu
        
        elif choice == "3":  # Option 3: Calculate content of the sequence
            if not sequence:
                print("Please input a sequence first.")
                continue
            print("Base Frequency: ", calculate_frequency(sequence))
            print("GC content is: {:.2f}%".format(gc_fraction(sequence) * 100))
        
        elif choice == "4":  # Option 4: Transcribe the DNA sequence
            if not sequence:
                print("Please input a sequence first.")
                continue
            print("Transcription: ", transcription_DNA(sequence))
        
        elif choice == "5":  # Option 5: Translate the RNA sequence
            if not sequence:
                print("Please input a sequence first.")
                continue
            print("Translation: ", translation_RNA(sequence))
        
        elif choice == "6":  # Option 6: Exit
            print("Goodbye!")
            break
        
        else:
            print("Invalid selection. Please try again.")
            continue

        # After processing, ask the user what to do next
        next_action = menu3()
        if next_action == "1":
            continue  # Input another sequence
        elif next_action == "2":
            pass  # Use the current sequence (do nothing, loop continues)
        elif next_action == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid selection. Returning to main menu.")



