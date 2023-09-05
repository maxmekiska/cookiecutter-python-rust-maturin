__version__ = "0.1.0"


from .rustpytemplate import *

__doc__ = rustpytemplate.__doc__
if hasattr(rustpytemplate, "__all__"):
    __all__ = rustpytemplate.__all__

from rustpytemplate.utils.fake import show_diff, show_sum
