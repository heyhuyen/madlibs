import sys
from nltk import SExprTokenizer

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print "Usage: madlib.py <responses filename> <marked text filename>"
        sys.exit()
    else:
        wordfile, textfile = sys.argv[1:]

    # get tokenized list with "[]" marked words
    # same as in extract_markers.py...

    text = open(textfile)
    tokens = SExprTokenizer(parens='[]').tokenize(text.read())
    text.close()
    replace = [i for i, token in enumerate(tokens) if token.startswith('[')]

    words = open(wordfile)
    word_list = words.read().split('\n')
    words.close()
    word_list.reverse()

    for i in replace:
        tokens[i] = word_list.pop()

    print " ".join(tokens)
