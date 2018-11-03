""" 
Implement a class called Clock with the following attributes:

Constructor with three parameters: hours, minutes, seconds with default values 0.
Three instance variables: hours, minutes, seconds.

    A method called str_update(). It takes as an argument a string of the form hh:mm:ss and updates
    the three instances variables.

    A __str__() method for responding to the print() method. 
    It should write out: "{} hours, {} minutes and {} seconds"

    A method called add_clocks(). It takes another clock object as a parameter, adds the two clocks 
    and returns a new clock instance.  In this method, you need to add the respective values of the 
    two clocks together and remember the resulting hours, minutes and seconds. Remember that the 
    sum of seconds cannot exceed 60, in which case there is a carry over to the minutes values. 
    Same for minutes, it cannot exceed 60 and carries over to hours. For hours, the summed values cannot exceed
    23. If hours is exceeded, we ignore it.  Use the divmod() built-in Python function in your implementation. 
"""

class Clock(object):
    def __init__(self,hours=0,minutes=0,seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
    
    def str_update(self,str):
        hours,minutes,seconds=[int(n) for n in str.split(':')]
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        """ self.string = string.split(':')
        self.hours = int(self.string[0])
        self.minutes = int(self.string[1])
        self.seconds = int(self.string[2]) """

    def __str__(self):
        return "{} hours, {} minutes, and {} seconds".format(self.hours,self.minutes,self.seconds)
    
    def add_clocks(self,clk):
        # takes in other clock as parameter, adds them and carries over amounts to keep
        # clock unit accuracy
        # a,b = divmod(75,60) tells you how many times it went in and what is left over

        carry_minutes, seconds = divmod((self.seconds + clk.seconds),60)
        carry_hours, minutes = divmod((self.minutes + clk.minutes),60)
        carry_days, hours = divmod((self.hours + clk.hours),24)

        total_minutes = minutes + carry_minutes
        total_hours = hours + carry_hours
        if total_minutes == 60:
            total_minutes = 0
            total_hours +=1
        return Clock(total_hours,total_minutes,seconds)

def main():
    wallclock = Clock()
    wristwatch = Clock()
    
    wallclock.str_update("01:15:34")
    wristwatch.str_update("24:09:15")
    print(wallclock)
    third_clock = wallclock.add_clocks(wristwatch)
    print(third_clock)

main()