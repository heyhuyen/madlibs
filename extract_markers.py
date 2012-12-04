import sys
from nltk import SExprTokenizer

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print "Usage: extract.py <source filename> <dest filename>"
        sys.exit()
    else:
        src, dest = sys.argv[1:]

    infile = open(src)
    tokens = SExprTokenizer(parens='[]').tokenize(infile.read())
    infile.close()
    blanks = [token for token in tokens if token.startswith('[') and token.endswith(']')]
    output = open(dest, 'w')
    for blank in blanks:
        output.write(blank.strip('[]') + '\n')
    output.close()
