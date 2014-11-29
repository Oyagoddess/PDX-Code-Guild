class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

happy_bday = Song(["Happy Birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around the family",
                        "With poskets full of shells"])

twinkle_twinkle = Song([" Twinkle, Twinkle little star",
                        "How i wonder what your are",
                        "and you are too high in the sky"])

happy_bday.sing_me_a_song() # passing a list of strings through lyrics
twinkle_twinkle.sing_me_a_song()
bulls_on_parade.sing_me_a_song()