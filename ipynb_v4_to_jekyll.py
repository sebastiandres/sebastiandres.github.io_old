"""
Converts a ipython notebook (version 4.0)
into a valid jekyll post.
Usage:
ipython nbconvert --config ipynb_v4_to_jekyll.py path/to/My_Notebook.ipynb
Output :
path/to/yyyy-mm-dd-my-notebook.md
"""

try:
    from urllib.parse import quote  # Py 3
    print("Using Python 3")
except ImportError:
    from urllib2 import quote  # Py 2
    print("Using Python 2")

from datetime import date
import sys
import os
from IPython import embed

def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += len(sub) # use start += 1 to find overlapping matches

def replace_marker(string, marker, left_marker, right_marker=None):
    """
    """
    if right_marker is None:
        right_marker=left_marker
    # Auxiliar function to "easily" replace markers
    def variable_marker(i,last):
        if i==last:
            return ""
        if (i%2)==0:
            return left_marker
        else:
            return right_marker
    # Now split and conditionally add the markers
    splitted_strings = string.split(marker)
    last = len(splitted_strings)-1
    marked_strings = [s+variable_marker(i,last)  for i,s in enumerate(splitted_strings)]
    processed_string = "".join(marked_strings)
    return processed_string

def latex2mathjax(string):
    """
    """
    # Correctly indent the lists
    string = replace_marker(string, "\n*", "\n\n*")
    string = replace_marker(string, "\n *", "\n\n *")
    string = replace_marker(string, "\n  *", "\n\n  *")
    # Replace all \textbf by \mathbf
    string = replace_marker(string, "\\textbf", "\\mathbf")
    # Replace all \textrm by \mathsf
    string = replace_marker(string, "\\textrm", "\\mathsf")
    # Replace all \[ /] 
    string = replace_marker(string, "\\\\[", "\n\\\\[ ")
    string = replace_marker(string, "\\\\]", " \\\\]\n")
    # Replace all $$ formula $$
    string = replace_marker(string, "$$", "\n\\\\[ ", " \\\\]\n")
    # Replace all remaining $ formula $
    string = replace_marker(string, "$", "\\\\( ", " \\\\)")
    # Replace all remaining _ with \n
    string = replace_marker(string, "_", "\\_")
    return string

def sanitize_markdown(string):
    # Convert all latex to mathjax
    sanitized_1 = latex2mathjax(string)
    # 
    sanitized = sanitized_1
    return sanitized

def process_execute_result(output_dict):
    image_template = "<img src='data:image/{0};base64,{1}'/>"
    text = "no TEXT/HTML  in dic"
    if ("data" in output_dict):       
        if ("text/plain" in output_dict["data"]):
            text = output_dict["data"]["text/plain"]
            text = text.rstrip()
            text = text.replace("<","&lt;") 
            text = text.replace(">","&gt;") 
        if ("text/html" in output_dict["data"]):
            text = output_dict["data"]["text/html"]
            text = text.rstrip()
        elif ("image/jpeg" in output_dict["data"]):
            text = image_template.format("jpeg",output_dict["data"]["image/jpeg"])
        elif ("image/png" in output_dict["data"]):
            text = image_template.format("png",output_dict["data"]["image/png"])
        else:
            print("-"*80)
            print("Something was not processed")
            print(output_dict)
            print("-"*80)
    return text

def debugger(var):
    print_globals=False
    print("Provided variable:")
    print("\ttype: \n"+str(type(var)))
    print("\tvalue: \n"+str(var))
    if print_globals:
        print("Global Variables")
        gdict = globals()
        for key in sorted(list(gdict.keys())):
            print("\t"+key)
            #print("\t\t"+str(gdict[key]))
    return str(var)
 
def path2support(path):
    """Turn a file path into a URL"""
    print("-o"*40)
    print(path)
    print(path.keys())
    #print(path.split(os.path.sep))
    #parts = path.split(os.path.sep)
    #file_url = '{{ site.baseurl}} notebooks/' + '/'.join(quote(part) for part in parts)
    file_url = "MustDO"
    return file_url

def process_ipynb(my_file):
    if not my_file.endswith('.ipynb'):
        print(my_file)
        return
    # Otherwise, we can carry on
    date_str = date.today().strftime('%Y-%m-%d-')
    f = my_file.split('.ipynb')[0]
    dirname = os.path.dirname(f)
    basename = os.path.basename(f).lower().replace("_","-").replace(" ","-")
    f  = os.path.join(dirname, date_str + basename.lower()) # Use today's date in the filename
    # Configure everything 
    c = get_config()
    c.NbConvertApp.export_format = 'markdown'
    c.MarkdownExporter.template_path = ['.']
    c.MarkdownExporter.template_file = 'ipynb_v4_to_jekyll'
    c.MarkdownExporter.filters = {
                                  'process_execute_result': process_execute_result, 
                                  'sanitize_markdown':sanitize_markdown,
                                  'path2support': path2support, 
                                  'debugger': debugger,
                                 }
    c.NbConvertApp.output_base = f #dirname # "trash" #f.lower().replace(' ', '-')
    c.FilesWriter.build_directory = "." #os.path.join(".", dirname)
    return f

for my_input_file in sys.argv[4:]:
    my_output_file = process_ipynb(my_input_file)
    if  my_input_file is not None:
        print("\nSuggested actions:")
        print("\tmv  {0}.md  _posts/\n".format(my_output_file))
        print("\tmv  {0}.ipynb  ipynb/\n".format(my_input_file))
