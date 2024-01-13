**Book Index Generator
**

**Description
**The Book Index Generator is a Python script designed to automate the creation of an index for books or similar documents. It processes a PDF document to find and list occurrences of specific words or phrases, including their inflected forms. This tool is invaluable for authors, editors, and publishers during the final stages of book publication, particularly for creating an informative and comprehensive index section.

**Features
**Word List Import: Imports a list of words or phrases from a DOCX file, representing the key terms for the index.
PDF Processing: Searches a specified PDF document for occurrences of each word or phrase from the list.
Substring Matching: Identifies words containing the listed terms as substrates, recognizing various inflected forms.
Index Creation: Outputs a list of page numbers for each term, along with the total number of occurrences, sorted in ascending order.
Installation

pip install nltk
pip install PyPDF2
pip install python-docx

**Usage
**
To use this script:

Place your list of words in a DOCX file.
Specify the path to your DOCX file and the PDF document in the script.
Run the script to generate the index.
Example
An example of the output:

'souhlas' found on pages: [22, 25, 81, 100, 109, ...] (Total occurrences: 15)
'brigády' found on pages: [54, 230, 232, ...] (Total occurrences: 7)

Contributing
Contributions to the Book Index Generator are welcome. Please feel free to fork the repository and submit pull requests.



This template covers the key elements:

**Description:** A brief introduction to what the script does.
**Features: **Highlights of what the script can do.
**Installation:** Necessary steps to install any dependencies.
**Usage: **Instructions on how to use the script.
**Example:** A simple example to demonstrate the output.
**Contributing:** Encouragement for others to contribute.
**License:** Information about the licensing of your script (important for open-source projects).
Feel free to adjust the content to fit your project's specifics and your preferences. A well-written README makes your project more approachable and easier to understand for potential users or contributors.
