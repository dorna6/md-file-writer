from mdFileWriter.var_util import elementType, Element
import os

class MDfile():
    def __init__(self):
        self.element_list = []
        
    def add_headline(self,headline_text:str,rank:int):
        ''' this method add an headline element to the list '''
        
        # block rank to a value between 1-6
        rank = min(max(rank,1),6)
        
        # select element type
        if rank==1: itype = elementType.HEADLINE1
        elif rank==2: itype = elementType.HEADLINE2
        elif rank==3: itype = elementType.HEADLINE3
        elif rank==4: itype = elementType.HEADLINE4
        elif rank==5: itype = elementType.HEADLINE5
        elif rank==6: itype = elementType.HEADLINE6            
        
        # get content
        icontent = headline_text
        
        # append elements to the list
        self.element_list.append(Element(itype,icontent))
        
    def add_text(self,text:str):
        itype = elementType.TEXT
        icontent = text
        self.element_list.append(Element(itype,icontent))
              
    def create_file(self,file_name: str ='MarkDownFile'):
        ''' this method create md file from the element list '''
        
        # init empty text list
        text_list = []
        
        # generate text from each element and add to the text list
        for element in self.element_list:
            
            # case HEADLINE1
            if element.get_type() == elementType.HEADLINE1:
                itext_list = self._textGen_HEADLINE(element)
            # case HEADLINE2
            elif element.get_type() == elementType.HEADLINE2:
                itext_list = self._textGen_HEADLINE(element)
            # case HEADLINE2
            elif element.get_type() == elementType.HEADLINE3:
                itext_list = self._textGen_HEADLINE(element)
            # case HEADLINE2
            elif element.get_type() == elementType.HEADLINE4:
                itext_list = self._textGen_HEADLINE(element)
            # case HEADLINE2
            elif element.get_type() == elementType.HEADLINE5:
                itext_list = self._textGen_HEADLINE(element)
            # case HEADLINE2
            elif element.get_type() == elementType.HEADLINE6:
                itext_list = self._textGen_HEADLINE(element)                                         
            # case TEXT
            elif element.get_type() == elementType.TEXT:
                itext_list = self._textGen_TEXT(element)
        
            # append the text element to the main text list
            for itext in itext_list:
                text_list.append(itext)
            

        # create file and open
        current_folder = os.path.dirname(os.path.realpath(__file__))
        project_folder = os.path.dirname(current_folder)
        output_folder = os.path.join(project_folder, 'output')
        output_file = os.path.join(output_folder, f'{file_name}.md')

        # write to file
        with open(output_file, 'w') as file:
            for itext in text_list:
                file.write('\n')
                file.write(itext)
                
    
    def _textGen_HEADLINE(self,element:Element):
        ''' this method create a text list of HEADLINE element '''
        
        # init empty list
        text_list=[]
        
        # select the headline type
        if element.get_type() == elementType.HEADLINE1:
            headling_prefix = '#'
        if element.get_type() == elementType.HEADLINE2:
            headling_prefix = '##'
        if element.get_type() == elementType.HEADLINE3:
            headling_prefix = '###'
        if element.get_type() == elementType.HEADLINE4:
            headling_prefix = '####'
        if element.get_type() == elementType.HEADLINE5:
            headling_prefix = '#####'
        if element.get_type() == elementType.HEADLINE6:
            headling_prefix = '######'
        
        # append text      
        text_list.append('<!--headline-->')
        text_list.append(f'{headling_prefix} {element.get_content()}')
        text_list.append('') 
        
        return text_list
    
    def _textGen_TEXT(self,element:Element):
        ''' this method create a text list of HEADLINE element '''
        
        # init empty list
        text_list=[]
        
        # append text      
        text_list.append('<!--simple text-->')
        text_list.append(f'{element.get_content()}')
        text_list.append('') 
        
        return text_list 
        