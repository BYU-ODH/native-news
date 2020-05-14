## Open search template
Taken from https://chroniclingamerica.loc.gov/search/pages/opensearch.xml

### HTML
https://chroniclingamerica.loc.gov/search/pages/results/?andtext={searchTerms}&page={startPage?}&ortext={chronam:booleanOrText?}&year={chronam:year?}&date1={chronam:date?}&date2={chronam:date?}&phrasetext={chronam:phraseText?}&proxText={chronam:proxText?}&proximityValue={chronam:proximityValue?}

### Atom
https://chroniclingamerica.loc.gov/search/pages/results/?andtext={searchTerms}&page={startPage?}&ortext={chronam:booleanOrText?}&year={chronam:year?}&date1={chronam:date?}&date2={chronam:date?}&phrasetext={chronam:phraseText?}&proxText={chronam:proxText?}&proximityValue={chronam:proximityValue?}&format=atom


## search test
- https://chroniclingamerica.loc.gov/search/pages/results/?&date1=1890-11-01&date2=1891-03-31&format=&page=2
This one works, but it doesn't produce the sort of results that I was expecting to find.

- https://chroniclingamerica.loc.gov/search/pages/results/?&date1=11%2F01%2F1890&date2=03%2F31%2F1891&format=atom

- https://chroniclingamerica.loc.gov/search/pages/results/?dateFilterType=range&date1=11%2F01%2F1890&date2=03%2F31%2F1891&format=atom
  - Got this format for the date string from doing an advanced search on the site and then looking for the right portion of the URL. When I pasted it here, it worked as it should.


## Order of operations

1. Run search on the right series of dates (https://chroniclingamerica.loc.gov/search/pages/results/?dateFilterType=range&date1=11%2F01%2F1890&date2=03%2F31%2F1891&format=atom) and download the Atom text. Will need to update the URL to add page numbers (e.g. `&page=2`) to get the subsequent pages. There appear to be 20 results per page appearing despite the fact that `<opensearch:itemsPerPage>` says it is limited to 10. **The last page is 3838**
2. On the Atom results, get the link to the page for the individual object, which is nested in `<entry><link href="[what we want]">`.
3. Append `ocr/` to the link in step 2 and then download that object. 

I'll probably need to come up with a way to rename everything once it's downloaded.


