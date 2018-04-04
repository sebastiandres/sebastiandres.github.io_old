"""
Converts a ipython notebook (version 4.0)
into a valid jekyll post.
Usage:
ipython nbconvert --config ipynb_v4_to_jekyll.py path/to/My_Notebook.ipynb
Output :
path/to/yyyy-mm-dd-my-notebook.md

# http://nbconvert.readthedocs.io/en/latest/customizing.html
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
import json

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
    Converts the declared latex to mathjax notation.
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
    """
    return string

def sanitize_markdown(string):
    """
    Sanitize the markdown, when needed
    """
    # Convert all latex to mathjax
    sanitized = latex2mathjax(string)
    return sanitized

def is_audio_video_or_iframe(text_plain):
    """
    Auxiliar method to process all known html types
    """
    if text_plain == "<IPython.lib.display.Audio object>":
        print("\tProcessing an Audio object from execution cell.")
        return True
    if text_plain[:33] == "<IPython.lib.display.YouTubeVideo":
        print("\tProcessing a Youtube video object from execution cell.")
        return True
    if text_plain[:27] == "<IPython.lib.display.IFrame":
        print("\tProcessing an IFrame from execution cell.")
        return True
    return False


def process_execute_result(output_dict):
    """
    Process all the execution cells, returning the text here computed.
    """
    image_template = "<img src='data:image/{0};base64,{1}'/>"
    if ("data" in output_dict):
        if ("text/plain" in output_dict["data"]):
            if output_dict["data"]["text/plain"]=="<VegaLite 2 object>":
                print("\tProcessing a Vega lite from execution cell")
                # Variables
                div_name = "viz_{}".format(output_dict["execution_count"])
                var_name = "vlSpec_{}".format(output_dict["execution_count"])
                aux_dict = output_dict['data']['application/vnd.vegalite.v2+json']
                json_str = json.dumps(aux_dict, indent=4)
                # Formated text
                text  = '  <!-- Container for the visualization -->\n'
                text += '  <div id="{}"></div>\n'.format(div_name)
                text += '  <script>\n'
                text += '  var {0} = \n'.format(var_name)
                text += json_str + ";\n\n"
                text += 'vegaEmbed("#{0}", {1});\n</script>'.format(div_name, var_name)
            elif is_audio_video_or_iframe(output_dict["data"]["text/plain"]):
                text = "<div>" + output_dict["data"]["text/html"] + "</div>"
            else:
                message = "Unrecognized format with data. Using defaults."
                print("\t" + message)
                text = output_dict["data"]["text/html"]
                print("*"*80)
                print(output_dict)
                print("*"*80)
        elif ("text/html" in output_dict["data"]):
            print("\tProcessing an html object")
            text = output_dict["data"]["text/html"]
            text = text.rstrip()
        elif ("image/jpeg" in output_dict["data"]):
            print("\tProcessing a jpeg image")
            text = image_template.format("jpeg",output_dict["data"]["image/jpeg"])
        elif ("image/png" in output_dict["data"]):
            print("\tProcessing a png image")
            text = image_template.format("png",output_dict["data"]["image/png"])
        else:
            print("\tUnrecognized format. Using defauts.")
            text = "Unrecognized format.<br>\n"
    else:
        text = "no TEXT/HTML in dic"
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
    """
    Turn a file path into a URL.
    """
    print("-o"*40)
    print(path)
    print(path.keys())
    #print(path.split(os.path.sep))
    #parts = path.split(os.path.sep)
    #file_url = '{{ site.baseurl}} notebooks/' + '/'.join(quote(part) for part in parts)
    file_url = "MustDO"
    return file_url

def process_ipynb(my_file):
    """
    Processing the ipython notebook
    """
    if not my_file.endswith('.ipynb'):
        print("File {} is not a notebook (or lacks proper format)".format(my_file))
        return
    else:
        print("Processing the notebook {}".format(my_file))
    # Default options
    default_date_str = date.today().strftime('%Y-%m-%d')
    default_directory = './_posts/'
    # Ask what do you want to do
    date_message = "\tWhat date do you want for the post [default:{}]: "
    chosen_date = input(date_message.format(default_date_str)) or default_date_str
    directory_message = "\tWhere to write the post [default:{}]: "
    chosen_build_directory = input(directory_message.format(default_directory)) or default_directory
    # Otherwise, we can carry on
    f = my_file.split('.ipynb')[0]
    dirname = os.path.dirname(f)
    basename = os.path.basename(f).lower().replace("_","-").replace(" ","-")
    output_filename  = os.path.join(dirname, chosen_date + "-" + basename.lower())
    # Configure everything
    c = get_config()
    c.NbConvertApp.export_format = 'markdown'
    c.MarkdownExporter.template_path = ['.']
    c.MarkdownExporter.template_file = 'ipynb_to_jekyll'
    c.MarkdownExporter.filters = {
                                  'process_execute_result': process_execute_result,
                                  'sanitize_markdown':sanitize_markdown,
                                  'path2support': path2support,
                                  #'debugger': debugger,
                                 }
    c.NbConvertApp.output_base = output_filename
    c.FilesWriter.build_directory = chosen_build_directory
    return output_filename

################################################################################
# Run the main processing function for all the files
################################################################################
for my_input_file in sys.argv[3:]:
    if  my_input_file is not None:
        my_output_file = process_ipynb(my_input_file)
        print("\nSuggested actions:")
        print("\tCommit the changes.")
        print("\tVisit the blog: https://sebastiandres.github.io/")
        print("\tVisit the repository: https://github.com/sebastiandres/sebastiandres.github.io")
