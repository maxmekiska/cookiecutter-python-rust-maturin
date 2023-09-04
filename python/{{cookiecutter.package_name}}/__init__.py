__version__ = "0.1.0"


from .{{cookiecutter.package_name}} import *

__doc__ = {{cookiecutter.package_name}}.__doc__
if hasattr({{cookiecutter.package_name}}, "__all__"):
    __all__ = {{cookiecutter.package_name}}.__all__

from {{cookiecutter.package_name}}.utils.fake import show_diff, show_sum
