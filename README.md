# native-news
Repository for work related to Mike Taylor's native newspaper project.

## Order of operations

### Data prep
1. Use `atom-harvester.py` to harvest atom data from the _[Chronicling America](https://chroniclingamerica.loc.gov/)_ website for the dates we are interested in (1 Nov 1890 - 31 March 1891). 
2. Use `atom-reader.py` to read each atom file and create a data dictionary.
3. Use `ocr-harvester.py` to download the `.HTML` of the OCR data for each newspaper page for the dates we are interested in.  
4. Use `ocr-checker.py` to verify that the number of downloaded HTML pages matches what was expected.
5. Use `ocr-extractor.py` to extract the OCR from the HTML pages. 
6. Use `ocr-combiner.py` to combine the individual pages of a newspaper issue into a single `txt` file. 

**N.B. At first, `atom-reader.py` got the link to the HTML page for the OCR. When I got to extracting the OCR with `ocr-extractor.py`, I realized that I could have downloaded the OCR directly without going through the HTML. For that reason, I rewrote `atom-reader.py` to produce a different link to the OCR. If I were to go through the whole process again, `ocr-extractor.py` would be unnecessary. That said, the data we have were actually created by extracting the OCR from the HTML. Sticking with this process saved us from having to re-harvest all 76k pages.**

### Analysis
1. Use `search.py` to find frequencies of key terms.
2. Topic model the contents of the `combined-ocr` folder using MALLET. (Unfortunately, I don't seem to have kept a record of the command. I did 100 topics, stop words removed, 1000 iterations [default] and optimization set at, I believe, 100. I am also 95% certain that I set a seed of `1` so I could replicate the results.)
3. Use `topic-analyzer.py` to isolate topic 70 from the topic model. 
4. Use `visualize-terms.py` to create graphs of weekly appearances of 'ghost dance', 'pine ridge', or 'wounded knee'
5. Use `find_2jan.py` to find all issues published on 1891-01-02 and copy them to a separate folder. 


## Scripts

### atom-harvester.py
This script downloads 3838 atom files from the _Chronicling America_ website based on a search query that is formulated for the dates we are interested in. The atom files each contain 20 results, each of which is a single page of a newspaper within the timeframe. The atom files are saved as `xml` in the `atom-data` folder.

### atom-reader.py
This script processes the atom files in the `atom-data` folder. It reads the entries in the atom file and outputs the results to `data-dictionary.tsv`.

### find_2jan.py
This script finds every newspaper issue in the `combined-ocr` folder that has a publication date of 1891-01-2 and copies that issue to the `2-jan-issues` folder.

### newspaper_tsv_prep.py
This script takes the data from `newspapers.txt` and converts it into a `tsv` with columns for city and state for the newspapers. The output is `newspapers_locations.tsv`.

### ocr-checker.py
This script creates two sets: one is the OCR HTML files that were expected to be downloaded from the information in `data-dictionary.tsv`; the other is the OCR HTML files that were _actually_ downloaded using `ocr-harvester.py`. 

I created this script because `data-dictionary.tsv` was 76,748 lines long, but I only got 74,978 HTML files downloaded from LOC. After a number of ways of checking (which resulted in this script), I verified that there were duplicate lines in `data-dictionary.tsv` and that the number of duplicates meant that the number of files I was actually expecting to download and the number that I _did_ download matched.

### ocr-combiner.py
This script crawls the data in the `ocr-txt` folder and combines the individual pages of a newspaper issue into a single `txt` file. It outputs its results to the `combined-ocr` folder.

### ocr-extractor.py
This script extracts the text of the OCR from the HTML that was downloaded with `ocr-harvester.py`. It saves its output to the `ocr-txt` folder. 

### ocr-harvester.py
This script uses the information in `data-dictionary.tsv` to download `.txt` OCR files from the _Chronicling America_ website and save them in the `ocr-txt` folder. It also outputs a set of all newspapers in the data set, saving it to `newspapers.txt`.

### search.py
This script uses regex to search for key terms within the corpus contained in the `combined-ocr` folder. It saves the output (including number of hits and strings that hit) to `search-results.tsv`. It also saves the total counts for each term to `search-counters.txt`.

### topic-analyzer.py
This script takes the results of the 100-topic topic model and isolates topic 70, which is the "Wounded Knee" topic. It sets the topic-composition of the document (a single newspaper issue) to 0 if the composition is below 0.01 (1%). It also rounds the topic composition to 4 decimal places. It saves this output to `tm_wk_results.tsv`. As a secondary action, it saves newspaper issues that are composed of 0.01 or higher in topic 70 to the `tm-subset` folder. 

### url-grabber.py
This script finds all the locations of the `tar` files for the Chronicling America website. It would be a first step if we wanted to bulk download all the data in the data set. It saves its output to `tarfiles.txt`. This was the first step I took in this project and I subsequently abandoned this line of work. An intermediary step is the creation of `chronicling-atom.txt`.

### visualize-terms.py
This script takes the output of `search.py` and creates graphs for the weekly appearance of key terms in the corpus. It saves its output to the `images` folder.

## Folders

### 2-jan-issues
This folder has the output of the `find_2jan.py` script. It is a collection of all newspaper issues that were published on 1891-01-02. 

### atom-data
This folder has the output of the `atom-harvester.py` script. It is a collection of 3,838 atom/XML files.

### combined-ocr
This folder has the output of the `ocr-combiner.py` script. It is a collection of individual issues of newspaper issues. 

### images
This folder has the output of the `visualize-terms.py` script. It is a collection of maps of key terms over time. 

### ocr-html
This folder has the output of the `ocr-harvester.py` script. It is a collection of 76k HTML files downloaded from the Chronicling America website. **N.B. If re-running the scripts, this folder would be unnecessary.**

### ocr-txt
This folder has the output of the `ocr-extractor.py` script. It is a collection of 76k text files that were extracted from the data in the `ocr-html` folder. 

### tm-subset
This folder has the output of the `topic-analyzer.py` script. It is a collection of newspaper issues that are composed of 0.01 or higher of topic 70, the "Wounded Knee" topic. 

## Documents

### chronicling-atom.txt
This is an output of `url-grabber.py` and is an intermediary step to getting all the `tar` files from the site.

### data-dictionary.tsv
This tsv is the output of `atom-reader.py`. For each entry in the atom data, it lists 
- newspaper
- date published (in ISO format)
- the page number of the image, formatted as `seq-4` where `4` is the page number
- the direct link to _Chronicling America_ for that page
- the link to the OCR for that page
This file is used for step 3 in the order of operations.

### newspaper_locations.tsv
This is an output of `newspaper_tsv_prep.py` and is a list of all the newspapers in our targeted corpus as well as their city and states.

### newspapers.txt
This is an output of `ocr-harvester.py`, and is a list of all the newspapers in our targeted corpus. 

### ocr-checker.txt
This is the output of `ocr-checker.py`. It shows which items appear more than once in `data-dictionary.tsv`.

### open-search-notes.md
This markdown file contains preliminary notes that I created while trying to understand how to formulate a proper search query to use in `harvesting-chronicling.py`. In it, I also sketch out the different scripts that will be needed to accomplish the work that I need to do.

### search-counters.txt
This is an output of `search.py`. It is a list of total number of hits for the regex terms in `search.py`.

### search-results.tsv
This is an output of `search.py`. It is a list of all newspaper issues and the number of hits for each regex term in `search.py` and the strings that triggered those hits.

### tarfiles.txt
This is an output of `url-grabber.py` and is a list of direct downloads for the `tar` files for each part of the Chronicling America data set. This could be used if we wanted to bulk download all of the data from the site.

### tm_wk_results.tsv
This is an output of `topic-analyzer.py` and is a tsv of the results of the topic model. It lists the newspaper, the date of the issue, and the percentage of that document composed of topic 70, which is the "Wounded Knee" topic. The percentage was rounded to 4 decimal points, and anything below 0.01 was set to 0.

