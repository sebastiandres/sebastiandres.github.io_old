try:
    from urllib.parse import quote  # Py 3
except ImportError:
    from urllib2 import quote  # Py 2
from datetime import date
import sys
import os

date_str = date.today().strftime('%Y-%m-%d-')

BLOG_DIR = os.path.expanduser('~/github/blog') # Also work and doesn't require defining system variables
#BLOG_DIR = os.environ['BLOG_DIR']

f = None
for arg in sys.argv:
    if arg.endswith('.ipynb'):
        f = arg.split('.ipynb')[0]
        f1 = os.path.dirname(f)
        f2 = os.path.basename(f)
        f  = f1 + "/" + date_str + f2 # Use today's date in the filename
        break

c = get_config()
c.NbConvertApp.export_format = 'markdown'
c.MarkdownExporter.template_path = [os.path.expanduser('~/.ipython/templates')]
c.MarkdownExporter.template_file = 'jekyll'
#c.Exporter.file_extension = 'md'
 
def path2support(path):
    """Turn a file path into a URL"""
    parts = path.split(os.path.sep)
    file_url = '{{ site.baseurl}}notebooks/' + '/'.join(quote(part) for part in parts)
    return file_url

c.MarkdownExporter.filters = {'path2support': path2support}
 
if f:
    c.NbConvertApp.output_base = f.lower().replace(' ', '-')
    #c.FilesWriter.build_directory = BLOG_DIR + '/notebooks'
    c.FilesWriter.build_directory = BLOG_DIR + '/'
