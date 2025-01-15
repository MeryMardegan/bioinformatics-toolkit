# Bioinformatics Toolkit

---

## **Features**

1. **Manual Input**: Enter sequences manually for quick analysis.
2. **File Input**: Import sequences directly from `.fasta` files.
3. **Content Calculation**: Calculate the frequency of each nucleotide (A, T, C, G, U) and the GC content.
4. **Transcription**: Transcribe a DNA sequence into RNA.
5. **Translation**: Translate an RNA sequence into its corresponding protein sequence.
6. **Interactive Menu**: Navigate through an intuitive menu system.

---

## **Folder Structure**

```plaintext
bioinformatics-toolkit/
├── main.py            # Main application script
├── requirements.txt   # Dependency list
├── README.md          # Project documentation
└── example.fasta      # Example sequence file
```

---

## **Getting Started**

### Prerequisites

- Python 3.8 or higher
- The `biopython` library

### Installation and Use

1. Clone this repository:
   ```bash
   git clone https://github.com/MeryMardegan/bioinformatics-toolkit.git
   ```

2. Navigate to the project directory:
   ```bash
   cd bioinformatics-toolkit
   ```

3. Install dependencies using the `requirements.txt` file:
   ```bash
   pip install -r requirements.txt
   ```

### How to Use

1. Run the program:
   ```bash
   python main.py
   ```

2. Follow the on-screen instructions:
   - Input a sequence manually or import one from a `.fasta` file.
   - Select from the available operations:
     - **Calculate content**: Displays nucleotide frequencies and GC content.
     - **Transcription**: Converts DNA to RNA.
     - **Translation**: Converts RNA to a protein sequence.

3. After each operation, you can choose to:
   - Input another sequence.
   - Use the current sequence for further analysis.
   - Exit the program.

---

## **Example Usage**

### Input:
**Manual sequence**: `ATCGATCGAA`

### Output:
- **Content Calculation**:
  ```
  Base Frequency: {'A': 3, 'T': 2, 'C': 2, 'G': 3}
  GC Content: 50.00%
  ```
- **Transcription**:
  ```
  Transcription: AUCGAUCGAA
  ```
- **Translation**:
  ```
  Translation: I*R
  ```

---

## **Contributing**

Contributions are welcome! If you'd like to add new features or fix bugs:

1. Fork the repository.
2. Create a new branch for your feature/bug fix.
3. Submit a pull request for review.

---

## **License**

This project is licensed under the MIT License. See `LICENSE` for details.

---

## **Contact**

If you have any questions, feel free to reach out via [email](mailto:marymardegan@usp.br) or create an issue in the repository.

