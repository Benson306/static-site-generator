# import required modules
import markdown
import os
from pathlib import Path
from tkinter import Tk, filedialog


#Open a Dialog Box to enable a user to pick a folder containing markdown
root = Tk() # pointing root to Tk() to use it as Tk() in program.
root.withdraw() # Hides small tkinter window.

root.attributes('-topmost', True) # Opened windows will be active. above all windows despite of selection.

directory = filedialog.askdirectory() # Returns opened path as str
 
# iterate over files in that directory
files = Path(directory).glob('*.md')

for file in files:
    with open(file, 'r') as f:

        # get filename without extension
        newFilename = Path(file).stem 
        
        #join file path and filename to be used as input to markdown
        path_to_input_file = directory + '/' + newFilename+'.md'

        #Designate where to save file and the filename to be used
        path_to_output_file = os.path.join('./output/', newFilename+'.html')

        # take mardown input and convert it to html output and save it in /output directory
        markdown.markdownFromFile(input= path_to_input_file , output= path_to_output_file )

#create 404 page
missingPage = markdown.markdown('''
404

404\. This Page Does Not Exist!.
================================

  

[Go to Homepage](homepage.html)
''')


#save 404 page
with open('./output/404.html', 'w') as f:
    f.write(missingPage)

#Create and save .htaccess file to take care of 404 page routing
with open('./output/.htaccess', 'w') as f:
    f.write("ErrorDocument 404 /404.html")


print("Website Has Been Generated. Find Your static web files have been saved at " + os.getcwd() +'/output/')