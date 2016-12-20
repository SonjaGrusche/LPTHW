class Lexicon(pbject):
    def scan(self, userinput):
        # first split up the (user)input into a list of words
        words = userinput.split()
        output = []
        # next go through the list, for each word give it a label
        #   from a listof words for each label
        for item in words:
            result = self.label(item) # return a nice tuple
            output.append(result)
        # return a list of all of these labeled words
        return output

    def label(self, item):
        # label the item and package it up in a tuple
        if item in ['north', 'south', 'east']: # test if it's a direction
            return ('direction', item)
        elif item in ['go', 'kill', 'eat']: # test if it's a verb
            return ('verb', item)
        elif item in ['the', 'in', 'of']: # test if it's a stop
            return ('stop', item)
        elif item in ['bear', 'princess']: # test if it's a noun
            return ('noun', item)
        else:
            try: # safety zone
                number = int(item)
                return ('number', number)
            except ValueError: # this iscalled exception handle
                return ('error', item)

lexicon = Lexicon()
