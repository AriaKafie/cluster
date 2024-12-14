import PyPDF2

def keep_first_page(input_pdf, output_pdf):
    # Open the input PDF file
    with open(input_pdf, 'rb') as infile:
        reader = PyPDF2.PdfReader(infile)
        writer = PyPDF2.PdfWriter()

        # Add only the first page
        writer.add_page(reader.pages[0])

        # Write the modified content to a new PDF file
        with open(output_pdf, 'wb') as outfile:
            writer.write(outfile)

    print(f"New PDF saved as {output_pdf}")

# Example Usage
input_pdf = 'title.pdf'  # Path to the input PDF file
output_pdf = 'newtitle.pdf'  # Path where the modified PDF will be saved

keep_first_page(input_pdf, output_pdf)
