import sys
import nltk
from nltk import SExprTokenizer
from responses import RandomPOS
from urllib import urlopen

TAGSET = ['NN', 'NNS', 'VB', 'VBD', 'VBG', 'JJ']

def text_from_file(filename):
    raw = open(filename)
    text = raw.read()
    raw.close()
    return text

def text_from_url(url):
    try:
        urlopen(url)
    except IOError:
        print "Invalid URL."
    return nltk.clean_html(urlopen(url).read())[:1000]

def pos_tags(tokens):
    tagged_tokens = nltk.pos_tag(tokens)
    words, tags = zip(*tagged_tokens)
    return tags

def random_words(pos_list):
    lib = RandomPOS()
    return [lib.random_pos(pos) for pos in pos_tokens]

def words_from_user(pos_list):
    return [raw_input('%s: ' % pos) for pos in pos_list]

if __name__ == "__main__":
    if len(sys.argv) == 2:
        text_src = sys.argv[1]
        if text_src.endswith('.txt'):
            text = text_from_file(text_src)
        else:
            text = text_from_url(text_src)
    else:
        print "Usage: madlib.py <textfile>"
        sys.exit()

    print 'ORIGINAL: %s' % text
    tokens = nltk.word_tokenize(text)
    pos_tags = pos_tags(tokens)
    pos_tokens = []
    indices = []

    for i, pos in enumerate(pos_tags):
        if pos in TAGSET:
            tokens[i] = '[' + pos + ']'
            pos_tokens.append(pos)
            indices.append(i)

    print 'MARKED: %s' % ' '.join(tokens)

    words = random_words(pos_tokens)
    #words = words_from_user(pos_tokens)
    words.reverse()

    for i in indices:
        tokens[i] = words.pop()

    print 'MADLIB: %s' % ' '.join(tokens)

