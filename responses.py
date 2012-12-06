import sys
import re
import nltk
from nltk.corpus import brown
from random import choice

class RandomPOS:
    def __init__(self):
        self.nouns = []
        self.verbs = []
        self.adjs = []
        self.setup()

    def setup(self):
        for tag in brown.tagged_words(categories='news'):
            if tag[1] == 'NN':
                self.nouns.append(tag[0])
            elif tag[1] == 'VB':
                self.verbs.append(tag[0])
            elif tag[1] == 'JJ':
                self.adjs.append(tag[0])

    def random_pos(self, pos):
        if pos == 'NN':
            return choice(self.nouns)
        elif pos == 'VB':
            return choice(self.verbs)
        elif pos == 'JJ':
            return choice(self.adjs)
        elif pos == 'NNS':
            return self.plural(choice(self.nouns))
        elif pos == 'VBD':
            return self.past(choice(self.verbs))
        elif pos == 'VBG':
            return self.prog(choice(self.verbs))

    def plural(self, noun):
        if re.search('[sxz]$', noun):
            return noun + 'es'
        elif re.search('[^aeioudgkprt]h$', noun):
            return noun + 'es'
        elif re.search('[^aeiou]y$', noun):
            return re.sub('y$', 'ies', noun)
        else:
            return noun + 's'

    def past(self, verb):
        if re.search('[e]$', verb):
            return verb + 'd'
        else:
            return verb + 'ed'

    def prog(self, verb):
        if re.search('[e]$', verb):
            return verb[:-1] + 'ing'
        return verb + 'ing'

if __name__ == "__main__":
    if len(sys.argv) == 4:
        infile, outfile, random = sys.argv[1:]
    else:
        print "Usage: responses.py <markers filename> <blanks filename> <random: True/False>"
        sys.exit()

    blanks_file = open(infile)
    blanks = blanks_file.read().split('\n')
    blanks.pop()
    blanks_file.close()

    responses_file = open(outfile, 'w')

    if random.lower() == "false":
        for blank in blanks:
            response = raw_input(blank + ': ')
            responses_file.write(response.strip()  + '\n')

    else:
        for blank in blanks:
            lib = RandomPOS()
            random_marker_match = lib.random_pos(blank).lower()
            responses_file.write(random_marker_match + '\n')
    responses_file.close()
