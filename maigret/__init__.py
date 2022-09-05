"""Sherl0ck"""

__title__ = 'Sherl0ck'
__package__ = 'maigret'
__author__ = 'antx-code'
__author_email__ = 'wkaifeng2007@163.com'


from .__version__ import __version__
from .checking import maigret as search
from .maigret import main as cli
from .sites import MaigretEngine, MaigretSite, MaigretDatabase
from .notify import QueryNotifyPrint as Notifier
