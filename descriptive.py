from math import sqrt

def mean(arg):
        """arg: list or tuple\n
        Returns the mean of the iterable."""
        if not arg:
              raise ValueError("arg can't be empty.")
        arg = list(arg)
        return sum(arg) / len(arg)

def median(arg):
            """arg: list or tuple\n
        Returns the median of the iterable."""
            if not arg:
              raise ValueError("arg can't be empty.")
            arg = list(arg)
            arg.sort()
            if len(arg) % 2 != 0:
                return arg[int(len(arg) / 2)]
            return (arg[int(len(arg) / 2)] + arg[int(len(arg) / 2) - 1]) / 2 
            
def mode(arg):
        """arg: list or tuple\n
        Returns the set of modes of the iterable."""
        if not arg:
              raise ValueError("arg can't be empty.")
        arg = list(arg)
        mode = []
        for i in arg:
            if mode == []: # First iteration.
                mode.append(i)
                continue
            elif arg.count(i) > arg.count(mode[0]): # If current value is greater than the current mode define a new mode. 
                mode = [i]    
                continue
            elif arg.count(i) == arg.count(mode[0]): # Case for more than one mode.
                  mode.append(i)    
        return set(mode)

def std_dev(sample):
        """
        arg: list or tuple
        Returns the standard deviation of the sample.
        """
        if not sample:
              raise ValueError("sample can't be empty.")
        squared = [(i - (mean(sample)))**2 for i in sample]
        return sqrt(sum(squared) / ((len(sample) - 1)))

def variance(sample):
        """
        arg: list or tuple

        Returns the veriance of the sample
        """
        if not sample:
            raise ValueError("Sample can't be empty")
        return std_dev(sample) ** 2

def quartiles(arg):
        """
        arg: list or tuple

        Returns Q1, Q2 and Q3
        """
        arg = list(arg)
        arg.sort()
        print(arg)
        # Q2
        if len(arg) % 2 != 0:
            Q1 = (arg[int(len(arg) / 4)] + arg[int(len(arg) / 4) - 1]) / 2
            print(Q1)
            Q2 = arg[int(len(arg) / 2)]
            Q3 = ((arg[int(len(arg) / 2 + len(arg) / 4)]) + (arg[int(len(arg) / 2 + len(arg) / 4) + 1])) / 2
        else: #1,2,3,4,5,6,7,8
            Q1 = (arg[int(len(arg) / 4)]  + arg[int(len(arg) / 4) - 1]) / 2
            Q2 =(arg[int(len(arg) / 2)] + arg[int(len(arg) / 2) - 1]) / 2
            Q3 = (arg[int(len(arg) / 2) + int(len(arg) / 4)] + (arg[int(len(arg) / 2) + int(len(arg) / 4) - 1])) / 2
        return f"25%: {Q1}\n50%: {Q2}\n75%: {Q3}"
       

        
    