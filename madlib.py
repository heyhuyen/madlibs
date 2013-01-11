import sys
import nltk
from nltk import SExprTokenizer
from responses import RandomPOS
from urllib import urlopen
from argparse import ArgumentParser

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

def setup_parser():
    parser = ArgumentParser(description='Turn text into a madlib.')
    parser.add_argument('text', type=str, help='text to create madlib')
    parser.add_argument('-u', '--url', action='store_true', help='specify text source is url')
    parser.add_argument('-a', '--auto-fill', action='store_true', 
                        help='automatically fill in madlib')
    return parser

if __name__ == "__main__":
    parser = setup_parser()
    args = parser.parse_args()
    if args.url:
        text = text_from_url(args.text)
    else:
        text = text_from_file(args.text)

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

    print 'MARKED: %s\n' % ' '.join(tokens)

    if args.auto_fill:
        words = random_words(pos_tokens)
    else:
        words = words_from_user(pos_tokens)
    words.reverse()

    for i in indices:
        tokens[i] = words.pop()

    print 'MADLIB: %s' % ' '.join(tokens)
