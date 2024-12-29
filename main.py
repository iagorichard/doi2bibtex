import pandas as pd
import bibtexparser
from bibtexparser.bwriter import BibTexWriter
from bibtexparser.bibdatabase import BibDatabase

working_folder = "../../../UserFiles/phd/assets/review/search_results/"
input_file = working_folder+"unified_doi.csv"
output_bibtex = working_folder+"all_doi_articles.bib"

df = pd.read_csv(input_file)

bib_entries = []
for index, doi in enumerate(df['DOI']):
    entry = {
        'ENTRYTYPE': 'article',
        'ID': f'article{index + 1}',
        'doi': doi,
        'title': f'Title for {doi}',
        'author': 'Author Placeholder',
        'year': '2024',
        'journal': 'Journal Placeholder'
    }
    bib_entries.append(entry)

bib_database = BibDatabase()
bib_database.entries = bib_entries

writer = BibTexWriter()
with open(output_bibtex, 'w') as bibfile:
    bibfile.write(writer.write(bib_database))

print(f"Generated bibtex: {output_bibtex}")
