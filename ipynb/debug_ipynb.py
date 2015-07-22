"""
Use this to load a ipynb file and open it as a dict in IPython.
Run it in:
python debug_ipynb.py my_notebook.ipynb
"""
from IPython import embed
from sys import argv
import json

def load_ipynb(ipynb_file):
    ipynb = json.load(open(ipynb_file, "r"))
    print("File {0} loaded:".format(ipynb_file))
    print("\nMetadata")
    print(ipynb[u'metadata'])
    print("\nnbformat")
    print(ipynb[u'nbformat'])
    print("\nnbformat_minor")
    print(ipynb[u'nbformat_minor'])
    cells = ipynb["cells"]
    print("\nHas {0} cells\n".format(len(cells)))
    for i, cell in enumerate(cells):
        print("Cell {0} has type {1}".format(i, cell["cell_type"]))
        print("\t keys: " + ", ".join(sorted(cell.keys())))
    embed()

if __name__=="__main__":
    if len(argv)==2 and (argv[1][-6:]==".ipynb"):
	load_ipynb(argv[1])
    else:
        print("Wrong. Use as in ")
        print("python debug_ipynb.py my_file.ipynb")
