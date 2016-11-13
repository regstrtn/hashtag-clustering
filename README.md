# NLP Project for clustering hashtags by concept
### Included in the code: 
- Hashtag segmentation
- Manually identified set of patterns for filtering query-type tags
- Hand labeled dictionary of 6000 tags and their concepts
- Test script for classifying new tags into respective clusters

### Usage instructions 
- `/pattern_filter/filter_query_type_tags.py <hashtagfile>`
Outputs a file containing segmented query type tags identified in the original <hashtagfile>

- `./benchmark_similarity.py`
A simple exact word matching algorithm to identify the cluster of the tag, using the hand labeled dictionary.

- `./wordnet_similarity.py`
Identify the cluster the tag belongs to, using the dictionary and word similarity measures from wordnet. 

----

### References


- [Stanford Dependency Parser] (http://nlp.stanford.edu/software/lex-parser.shtml)
- [Princeton University "About WordNet." WordNet. Princeton University. 2010] (http://wordnet.princeton.edu)
- [Wordsegment python module] (https://github.com/grantjenks/wordsegment)
