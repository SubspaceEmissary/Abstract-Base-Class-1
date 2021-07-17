from abc import ABC, abstractmethod, abstractproperty, abstractclassmethod

# By inheriting from the ABC class, that base class cannot be instantiated; only it's derivatives (and their common interfaces)

class Stream(ABC):
    def __init__(self):
        pass
    
    @abstractmethod 
    def read(self):
        pass
    
#(^ Will return the type of stream the stream is.)
    
    
    @abstractproperty
    def size(self):
        pass
    
#(^ Will return and be able to set the size [of stream] in MB.)
    
class FileStream(Stream):
    def __init__(self):
        self._type = "FileStream"
        self._sizeMB = 0

    def read(self):
        return self._type
    
    @property
    def size(self):
        return self._sizeMB
        
    @size.setter
    def size(self, sizeselect):
        if sizeselect <= 0:
            return "Size of '{self._type}' cannot be 0 or negative"
        else:
            self._sizeMB = sizeselect

# ^ Derivatives of 'Stream' base class 

class NetworkStream():
    def __init__(self):
        self._type = "NetworkStream"
        self._sizeMB = 0

    def read(self):
        return self._type
    
    @property
    def size(self):
        return self._sizeMB
        
    @size.setter
    def size(self, sizeselect):
        if sizeselect <= 0:
            return "Size of '{self._type}' cannot be 0 or negative MB"
        elif sizeselect > 100:
            return "Size of '{self._type}' cannot be greater than 100 MB"
        else:
            self._sizeMB = sizeselect
            

fs1 = FileStream()
ns1 = NetworkStream()

print(fs1.read())
print(ns1.read())

# ^ Example of --polymorphism--: Functions deriving from analagous base class with same function names produce same outcomes resepective to their class.
