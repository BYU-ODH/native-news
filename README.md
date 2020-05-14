# native-news
Repository for work related to Mike Taylor's native newspaper project.

## Order of operations
1. Use `atom-harvester.py` to harvest atom data from the _[Chronicling America](https://chroniclingamerica.loc.gov/)_ website for the dates we are interested in (1 Nov 1890 - 31 March 1891). 
2. Use `atom-reader.py` to read each atom file and create a data dictionary.
3. Use `ocr-harvester.py` to download the HTML page of the OCR data for each newspaper page for the dates we are interested in.  
4. Use `ocr-extractor.py` to extract the OCR from the HTML pages.

## Scripts

### atom-harvester.py
This script downloads 3838 atom files from the _Chronicling America_ website based on a search query that is formulated for the dates we are interested in. The atom files each contain 20 results, each of which is a single page of a newspaper within the timeframe. The atom files are saved as `xml` in the `atom-data` folder.

### atom-reader.py
This script processes the atom files in the `atom-data` folder. It reads the entries in the atom file and outputs the results to `data-dictionary.tsv`.

### ocr-harvester.py
This script uses the information in `data-dictionary.tsv` to download OCR files from the _Chronicling America_ website and save them as `.html` files in the `ocr-html` folder.

## Folders

### atom-data
This folder has the output of the `atom-harvester.py` script. It is a collection of 3,838 atom/XML files.

### ocr-html
This folder has the output of the `ocr-harvester.py` script. It is a collection of 76k HTML files downloaded from the Chronicling America website.

## Files

### data-dictionary.tsv
This tsv is the output of `atom-reader.py`. For each entry in the atom data, it lists 
- newspaper
- date published (in ISO format)
- the page number of the image, formatted as `seq-4` where `4` is the page number
- the direct link to _Chronicling America_ for that page
- the link to the OCR for that page
This file is used for step 3 in the order of operations.

### open-search-notes.md
This markdown file contains preliminary notes that I created while trying to understand how to formulate a proper search query to use in `harvesting-chronicling.py`. In it, I also sketch out the different scripts that will be needed to accomplish the work that I need to do.

