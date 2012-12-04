import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print "Usage: responses.py <filename>"
    else:
        infile, outfile = sys.argv[1:]

    blanks_file = open(infile)
    blanks = blanks_file.read().split('\n')
    blanks_file.close()

    responses_file = open(outfile, 'w')

    for blank in blanks:
        if len(blank) > 0:
            response = raw_input(blank + ': ')
            responses_file.write(response.strip()  + '\n')

    responses_file.close()
