This is a console-based program for turning text into madlibs and filling them out. Written in [Python](http://www.python.org) and using the [Natural Language Toolkit](http://nltk.org/) for part of speech parsing.

Written during [Hacker School](https://www.hackerschool.com/), Batch[4], Fall 2012.

## Usage
Run this command:

    python madlib.py TEXT

where TEXT is the name of the text file to convert into a madlib.

### Optional Parameters
    -u, --url        specify text source is url
If this option is included, TEXT parameter will be treated as a url. This feature is not yet complete. Ideally, text would be extracted from the provided url.

    -a, --auto-fill  automatically fill in madlib
If this option is included, the madlib will be filled in automatically, using random words from the news category of the Brown corpus that comes with nltk. Otherwise, the default is to prompt the user to fill in the parts of speech.

### Parts of Speech Tags
- NN = noun
- NNS = plural noun
- VB = verb, present tense
- VBD = verb, past tense
- VBG = verb, progressive tense ('-ing')
- JJ = adjective

## Resources
- [NLTK book](http://nltk.org/book/)
- [Dive into Python 3](http://getpython3.com/diveintopython3/generators.html)
- [Penn Treebank Tag set](http://www.ims.uni-stuttgart.de/projekte/CorpusWorkbench/CQP-HTMLDemo/PennTreebankTS.html)

##Todo/Extension Ideas
- properly scrape url for main text content
- add more parts of speech
- better parts of speech tagging, resolve ambiguous words
- validate user responses
