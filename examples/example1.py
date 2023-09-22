# add the main project folder to the path
import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from mdFileWriter.md_list_maker import MDfileCreator

my_md_file = MDfileCreator()
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

script_directory = os.path.dirname(os.path.abspath(__file__))
folder_name = "MarkDownFiles"
folder_path = os.path.join(script_directory, folder_name)
os.makedirs(folder_path, exist_ok=True)

my_md_file.create_file(folder_path=folder_path)