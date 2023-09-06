__version__ = "0.1.0"


from .{{cookiecutter.project_slug}} import *

__doc__ = {{cookiecutter.project_slug}}.__doc__
if hasattr({{cookiecutter.project_slug}}, "__all__"):
    __all__ = {{cookiecutter.project_slug}}.__all__

from {{cookiecutter.project_slug}}.utils.fake import show_diff, show_sum
