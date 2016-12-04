class ParserError(Exception):
    pass


class Sentence(object):

    def __init_(self, subject, verb, obj):
        # remember we take ('noun', 'princess') tuples and convert them
        self.subject = subject[1]
        self.verb = verb[1]
        self.object = obj[1]
        self.number = number[1]

    #def to_tuple(self):
    #    return (self.subject, self.verb, self.object, self.number)

# now we need a function that can peek at a list of words
# and return what type of word it is
def peek(word_list):
    if word_list:
        word = word_list[0]
        return word[0]
    else:
        return None
# we need it, because we'll have to make decisions about
# what kind of sentence we're dealing with based on
# what the next word is, and then we can call another
# function to consume that word and carry on

# to consume a word we use a the 'match' function,
# which confirms that the expected word is the right type,
# takes it off the list, and returnsthe word
def match(word_list, expecting):
    if word_list:
        word = word_list.pop(0)

        if word[0] == expecting:
            return word
        else:
            return None
    else:
        return None

# now we need a way to skip words that aren't useful to the Sentence
def skip(word_list, word_type):
    while peek(word_list) == word_type:
        match(word_list, word_type)
# remember 'skip' skips as many words of that type as it finds

# basic set of parsing functions
# ---

# parsing a verb
def parse_verb(word_list):
    skip(word_list, 'stop')

    if peek(word_list) == 'verb':
        return match(word_list, 'verb')
    else:
        raise ParseError("Expected a verb next.")

# numbers
def parse_number(word_list):
    skip(word_list, 'stop')

    if peek(word_list) == 'number':
        return match(word_list, 'number')
    else:
        return ('number', 1)

# sentence objects
def parse_object(word_list):
    skip(word_list, 'stop')
    next_word = peek(word_list)

    if next_word == 'noun':
        return match(word_list, 'noun')
    elif next_word == 'direction':
        return match(word_ist, 'direction')
    else:
        raise ParserError("Expected a noun or direction next.")

# subjects
def parse_subject(word_list):
    skip(word_list, 'stop')
    next_word = peek(word_list)

    if next_word == 'noun':
        return match(word_list, 'noun')
    elif nect_word == 'verb':
        return ('noun', 'player')
    else:
        raise ParserError("Expected a verb next.")

# final parse sentence function
def parse_sentence(word_list):
    subj = parse_subject(word_list)
    verb = parse_verb(word_list)
    obj = parse_object(word_list)
    number = parse_number(word_list)

    return Sentence(subj, verb, obj, number)
