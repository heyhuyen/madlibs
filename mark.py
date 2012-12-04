import sys
import nltk
import pdb

if __name__ == "__main__":
    if len(sys.argv) == 3:
        src, dest = sys.argv[1:]
    else:
        print "Usage: mark.py <source file> <dest file>"
        sys.exit()

    infile = open(src)
    tokens = nltk.word_tokenize(infile.read())
    infile.close()
    tagged_tokens = nltk.pos_tag(tokens)
    junk, tags = zip(*tagged_tokens)

    tagset = ['NN', 'NNS', 'VB', 'VBD', 'VBG', 'JJ']

    for i, tag in enumerate(tags):
        if tag in tagset:
            tokens[i] = '[' + tag + ']'

    result = " ".join(tokens)
    outfile = open(dest, 'w')
    outfile.write(result)
    outfile.close()
