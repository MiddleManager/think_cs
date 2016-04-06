class MyTime():
    """ An object that stores and manipulates time
    limitation: self.hrs goes past 24  """

     def __init__(self, hrs=0, mins=0, secs=0):
       """ Create a new MyTime object initialized to hrs, mins, secs.
           The values of mins and secs may be outside the range 0-59,
           but the resulting MyTime object will be normalized.
       """

       # Calculate total seconds to represent
       totalsecs = hrs*3600 + mins*60 + secs
       self.hours = totalsecs // 3600        # Split in h, m, s
       leftoversecs = totalsecs % 3600
       self.minutes = leftoversecs // 60
       self.seconds = leftoversecs % 60

    def __str__(self):
        return "{0}:{1}:{2}".format(self.hrs, self.mins, self.secs)

    def increment_seconds(self, seconds):
        """ Increments the class' values by seconds """
        self.secs += seconds

        while self.secs >= 60:
            self.secs -= 60
            self.mins += 1

        while self.mins >= 60:
            self.mins -= 60
            self.hrs += 1




if __name__ == "__main__":
    """ Run the debugging code """

    mt = MyTime(5, 3, 34)
    mt.increment_seconds(500)

    print(mt)
