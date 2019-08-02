#******************************************************************************
#*                          Parser Unittest Template
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
#*   This template file describes how to write a standard parser unittest.
#*
#* Read More:
#*   For the complete and up-to-date user guide on parsers and unittests, visit:
#*   https://wiki.cisco.com/display/GENIE/Genie+Parsers+Deepdive
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

# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError, SchemaMissingKeyError

# Parser
#* the syntax should be something like the following line:
# from genie.libs.parser.{{ cookiecutter.cisco_OS }}.<your_command> import YourCommand

# ==============================
# Unittest for:
#    * '<your command(s)>'
# ==============================
class test_your_command(unittest.TestCase):
    '''
    Unit test for:
    <your command(s) here>
    '''

    device = Device(name = 'aDevice')
    empty_output = { 'execute.return_value': '' }

    #* define the golden_parsed_output(s) and golden_output(s) here
    golden_parsed_output_1 = {
        #* ...
    }

    golden_output_1 = { 'execute.return_value': 
        '''
        <output>
        '''
    }

    golden_parsed_output_2 = {
        #* ...
    }

    golden_output_2 = { 'execute.return_value': 
        '''
        <output>
        '''
    }

    def test_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = YourCommand(device = self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_1)
        obj = YourCommand(device = self.device)
        parsed_output = obj.parse() #* could pass in parameters as you wish
        self.assertEqual(parsed_output, self.golden_parsed_output_1)

    def test_golden_2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_2)
        obj = YourCommand(device = self.device)
        parsed_output = obj.parse() #* could pass in parameters as you wish
        self.assertEqual(parsed_output, self.golden_parsed_output_2)


if __name__ == '__main__':
    unittest.main()
