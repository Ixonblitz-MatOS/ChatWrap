__author__="Ixonblitz-MatOS"
__version__="0.0.1"
from ultraimport.ultraimport import ultraimport
chatwrap=ultraimport("__dir__/chatwrap.py","*")
if chatwrap.__version__ !=__version__:print("There is a version difference between script and init")