#!/bin/bash

# Check if input file is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <file_with_list_of_filenames>"
    exit 1
fi

# Check if the file with the list of filenames exists
if [ ! -f "$1" ]; then
    echo "Error: File '$1' not found!"
    exit 1
fi

# Output file where concatenated content will be stored
output_file="concatenated_output.md"

# Clear the output file if it exists
> "$output_file"

# Read the list of files from the provided text file
while IFS= read -r file; do
    # Check if the file exists
    if [ -f "$file" ]; then
        cat "$file" >> "$output_file"
        echo "Added $file to $output_file"
    else
        echo "Warning: File '$file' not found, skipping..."
    fi
done < "$1"

echo "Concatenation complete. Output saved to $output_file"