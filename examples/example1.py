# add the main project folder to the path
import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from mdFileWriter.md_list_maker import MDfile

my_md_file = MDfile()
my_md_file.add_headline('MarkDown file project',1)
my_md_file.add_headline('Description',2)
my_md_file.add_headline('Intro',3)
my_md_file.add_text('xxxxyyyyzzzz')
my_md_file.add_headline('Goals',3)
my_md_file.add_text('xxxxyyyyzzzz')
my_md_file.add_headline('Installing',2)
my_md_file.add_text('xxxxyyyyzzzz')
my_md_file.add_headline('Notes',2)
my_md_file.add_text('xxxxyyyyzzzz')

my_md_file.create_file()