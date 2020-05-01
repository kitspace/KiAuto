"""
Tests for pcbnew_print_layers

For debug information use:
pytest-3 --log-cli-level debug

"""

import os
import sys
# import re
# import logging
# Look for the 'utils' module from where the script is running
script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(script_dir))
# Utils import
from utils import context

PROG = 'pcbnew_print_layers'
DEFAULT = 'printed.pdf'
CMD_OUT = 'output.txt'


def test_print_pcb_good_dwg(test_dir):
    ctx = context.TestContext('Print_Good_with_Dwg', 'good-project', test_dir)
    pdf = 'good_pcb_with_dwg.pdf'
    cmd = [PROG, '--output_name', pdf]
    layers = ['F.Cu', 'F.SilkS', 'Dwgs.User', 'Edge.Cuts']
    ctx.run(cmd, extra=layers)
    ctx.expect_out_file(pdf)
    ctx.compare_image(pdf)
    ctx.clean_up()


def test_print_pcb_good_inner(test_dir):
    ctx = context.TestContext('Print_Good_Inner', 'good-project', test_dir)
    cmd = [PROG]
    layers = ['F.Cu', 'F.SilkS', 'GND.Cu', 'Signal1.Cu', 'Signal2.Cu', 'Power.Cu', 'Edge.Cuts']
    ctx.run(cmd, extra=layers)
    ctx.expect_out_file(DEFAULT)
    ctx.compare_image(DEFAULT, 'good_pcb_inners.pdf')
    ctx.clean_up()


def test_print_pcb_layers(test_dir):
    ctx = context.TestContext('Print_Layers', 'good-project', test_dir)
    cmd = [PROG, '--list']
    ctx.run(cmd)
    ctx.compare_txt(CMD_OUT, 'good_pcb_layers.txt')
    ctx.clean_up()
