class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around the family",
                        "With pockets full of shells"])

last_christmas = Song(["Last christmas I gave you my heart,",
                        "But the very next day you gave it away.",
                        "Thiiiis year to save me from tears",
                        "I'll give it to someone special - special.",
                        "HA! BURN!"])

chop_suey = Song(["I don't think you trust,",
                    "in,",
                    "my,",
                    "self righteous suicide,",
                    "I,",
                    "cry,",
                    "when angels deserve to",
                    "DIIIIEEEEE"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

last_christmas.sing_me_a_song()

chop_suey.sing_me_a_song()
