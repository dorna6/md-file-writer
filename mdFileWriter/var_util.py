from enum import Enum, auto


# define element type enum
class elementType(Enum):
    HEADLINE1 = auto()
    HEADLINE2 = auto()
    HEADLINE3 = auto()
    HEADLINE4 = auto()
    HEADLINE5 = auto()
    HEADLINE6 = auto()
    
    TEXT = auto()



# define element class
class Element():
    ''' this class hold the data and get/set of a single element '''
    
    def __init__(self,type:elementType,content) -> None:
        self.type = type
        self.content = content
        
    def get_type(self):
        return self.type
    
    def get_content(self):
        return self.content
    
    def set_type(self,type:elementType):
        self.type = type
        
    def set_content(self,content):
        self.content = content






