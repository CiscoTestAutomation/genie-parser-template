#******************************************************************************
#*                              Parser Template
#* ----------------------------------------------------------------------------
#* ABOUT THIS TEMPLATE - Please read
#*
#* - Any comments with "#*" in front of them (like this entire comment box) are
#*   for template clarifications only and should be removed from the final
#*   product.
#*
#* - Anything enclosed in <> must be replaced by the appropriate text for your
#*   application
#*
#* Support:
#*    pyats-support@cisco.com
#*
#* Description:
#*   This template file describes how to write a standard parser.
#*
#* Read More:
#*   For the complete and up-to-date user guide on parsers, visit:
#*   https://pubhub.devnetcloud.com/media/pyats-packages/docs/genie/cookbooks/index.html#genie-libs-parsers
#*   https://wiki.cisco.com/display/GENIE/Genie+Parsers+Deepdive
#*
#*   List of available Genie parsers:
#*   http://wwwin-pyats.cisco.com/cisco-shared/genie/latest/genie_libs/#/parsers
#*
#*******************************************************************************

#*******************************************************************************
#* DOCSTRINGS
#*
#*   All parsers should use the built-in Python docstrings functionality
#*   to define parser/class/method headers.
#*
#* Format:
#*   Docstring format should follow:
#*   URL= https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html
#*
#* Read More:
#*   Python Docstrings, PEP 257:
#*   URL= http://legacy.python.org/dev/peps/pep-0257/
#*******************************************************************************

'''
{{ cookiecutter.parser_name }}.py

{{ cookiecutter.cisco_OS }} parsers for the following show commands:
    * <your commands here>

'''

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Or, Optional

# parser utils
from genie.libs.parser.utils.common import Common

# ==============================
# Schema for:
#    * '<your command(s)>'
# ==============================
class YourCommandSchema(MetaParser):
    '''
    Schema for:
    <your command(s) here>
    '''

    #* define your schema here
    schema = {
        #* ...
    }

# ==============================
# Parser for:
#    * '<your command(s)>'
# ==============================
class YourCommand(YourCommandSchema):
    '''
    Parser for:
    <your command(s) here>
    '''

    cli_command = [ '<your commands here>', '<separated by commas>' ]

    #* could add extra parameters if needed
    def cli(self, vrf = '', output = None):
        if output is None:
            #* <conditional statements deciding which command to use>
            #* e.g.
            #* if vrf:
            #*     out = self.device.execute(self.cli_command[1].format(vrf = vrf))
            #* else:
            #*     out = self.device.execute(self.cli_command[0])
            pass #* delete this line after completion

        else:
            out = output

        # initial variables
        parsed_dict = {}

        p1 = re.compile('<regular expression>')

        for line in out.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                #* <grouping into dictionaries>
                continue

        return parsed_dict
