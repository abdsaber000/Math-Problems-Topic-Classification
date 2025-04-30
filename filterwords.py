import csv

def txt_to_csv(input_file, output_file):
    """
    Convert a text file with one word per line to a CSV file with unique words.
    
    Args:
        input_file (str): Path to the input text file
        output_file (str): Path to the output CSV file
    """
    unique_words = set()
    
    # Read the input file and collect unique words
    with open(input_file, 'r') as txt_file:
        for line in txt_file:
            word = line.strip()  # Remove any whitespace or newline characters
            if word:  # Only add non-empty words
                unique_words.add(word)
    
    # Write the unique words to CSV file
    with open(output_file, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        
        # Write each word as a separate row
        writer.writerow(["math_words"])  # Header for the CSV file
        for word in sorted(unique_words):  # Sorting for better organization
            writer.writerow([word])
    
    print(f"Successfully converted {input_file} to {output_file}")
    print(f"Found {len(unique_words)} unique words")

# Example usage:
input_txt = "math_words.txt"  # Replace with your input file path
output_csv = "unique_words.csv"  # Replace with your desired output path
txt_to_csv(input_txt, output_csv)