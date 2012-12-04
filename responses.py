import sys
from random import choice
import re

class RandomPOS:
    def __init__(self, pos_file):
        self.nouns = []
        self.verbs = []
        self.adjs = []

    def random_noun(self, plural=False):
        if plural:
            return self.plural(choice(self.nouns))
        else:
            return choice(self.nouns)

    def random_adj(self):
        return choice(self.adj)

    def random_verb(self, past=False, prog=False):
        if past:
            return self.past(choice(self.verbs))
        elif prog:
            return self.prog(choice(self.verbs))
        else:
            return choice(self.verbs)

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
        if re.search('[e]$', noun):
            return verb + 'd'
        else:
            return verb + 'ed'

    def prog(self, verb):
        return verb + 'ing'

if __name__ == "__main__":
    if len(sys.argv) == 4:
        infile, outfile, random = sys.argv[1:]
    else:
        print "Usage: responses.py <markers filename> <blanks filename> <random: True/False>"
        sys.exit()

    blanks_file = open(infile)
    blanks = blanks_file.read().split('\n')
    blanks_file.close()

    responses_file = open(outfile, 'w')

    if random.lower() == "false":
        for blank in blanks:
            if len(blank) > 0:
                response = raw_input(blank + ': ')
                responses_file.write(response.strip()  + '\n')

    else:
        for blank in blanks:
            #find a random match for the marker category
            random_marker_match = 'random word'
            responses_file.write(random_marker_match + '\n')
    responses_file.close()
