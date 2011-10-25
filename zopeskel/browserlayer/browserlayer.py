import copy

from zopeskel.plone import BasicZope
from zopeskel.base import get_var
from zopeskel.base import var
from zopeskel.base import var, EASY, EXPERT
from zopeskel.vars import StringVar, BooleanVar

bl_vars = [
    StringVar(
        'blIFaceName',
        title='BrowserLayer Interface Name',
        description='Unique name for this browser layer.',
        modes=(EASY, EXPERT),
        page='Main',
        help="",
        ),
        ]

class BrowserLayer(BasicZope):
    _template_dir = 'templates/browserlayer'
    summary = "Browserlayer package with css and js resources"
    help = """
"""
    category = "Plone Development"
    required_templates = ['basic_namespace']
    use_local_commands = False
    use_cheetah = True
    vars = copy.deepcopy(BasicZope.vars)
    vars = bl_vars + vars
    get_var(vars, 'blIFaceName').default = 'IMyBrowserLayer'
    get_var(vars, 'namespace_package').default = 'plonebrowserlayer'
    get_var(vars, 'package').default = 'example'
    get_var(vars, 'description').default = 'Example BrowserLayer Product'
    get_var(vars, 'license_name').default = 'GPL version 2'

    def pre(self, command, output_dir, vars):
        vars['include_doc'] = True
