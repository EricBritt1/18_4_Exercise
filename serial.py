"""Python serial number generator."""

class MySerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    """
    - def __init__ class instance will initialize a three digit serial number of users choosing. 
    - User can set starts value but, value is not changeable
    """
    def __init__(self, start, value = -1):
        self.start = start
        self.value = value
    """
    - the generate class instance incremenets the value parameter which is then added to the serial value the user chose. 
    - each time generate is called on a particular instance the serial number will increase by 1.
    - Ex: serial = SerialGenerator(start=100)
            serial.generate()
                "101"
            serial.generate()
                "102"
    """
    def generate(self):
        self.value += 1
        return self.start + self.value
    
    """
    - Reset will reset the value of value to -1.
    - This allows for that particular instances serial number to restart count at users selected start for that particular instance.
    Ex: 
    - Ex: serial = SerialGenerator(start=100)
            serial.generate()
                "101"
            serial.generate()
                "102"
            serial.reset()
                Returns NONE here
            serial.generate()
                "100"
    """
    def reset(self):
        self.value = -1
    
class SerialGeneratorRemake:
    def __init__(self, start=0):
        """Make a new serial, starting at start."""
        self.start = self.next = start
    
    def __repr__(self):
        """Representation. Showing the start of serial and what number will come next"""
        return f"<SerialGeneratorRemake start={self.start} next={self.next}"
    
    def generate(self):
        """Adds 1 to next to show what number is next in line for serial(__repr__ purposes). Subtracts 1 to return current number"""
        self.next += 1
        return self.next - 1
    
    def reset(self):
        """Resets serial count to original start of instance"""
        self.next = self.start
        self.next += 1
        return self.next - 1
    

        
    
        
        
