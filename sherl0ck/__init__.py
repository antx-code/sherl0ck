"""Sherl0ck"""

__title__ = 'Sherl0ck'
__package__ = 'sherl0ck'
__author__ = 'antx-soc'
__author_email__ = 'wanglei@socmap.net'


from .__version__ import __version__
from .checking import maigret as search
from .maigret import main as cli
from .sites import MaigretEngine, MaigretSite, MaigretDatabase
from .notify import QueryNotifyPrint as Notifier
