from abc import ABC, abstractmethod

class Printer(ABC):
    @abstractmethod
    def print(self, document):
        pass
    
    @abstractmethod
    def scan(self, document):
        pass
    
    @abstractmethod
    def fax(self, document):
        pass


class BasicPrinter(Printer):
    def print(self, document):
        print("Printing document")

    def scan(self, document):
        raise NotImplementedError("Basic printers cannot scan")

    def fax(self, document):
        raise NotImplementedError("Basic printers cannot fax")






# correct code 

from abc import ABC, abstractmethod

class Printable(ABC):
    @abstractmethod
    def print(self, document):
        pass

class Scannable(ABC):
    @abstractmethod
    def scan(self, document):
        pass

class Faxable(ABC):
    @abstractmethod
    def fax(self, document):
        pass



class BasicPrinter(Printable):
    def print(self, document):
        print(f"Printing: {document}")

class AdvancedPrinter(Printable, Scannable, Faxable):
    def print(self, document):
        print(f"Printing: {document}")

    def scan(self, document):
        print(f"Scanning: {document}")

    def fax(self, document):
        print(f"Faxing: {document}")
    