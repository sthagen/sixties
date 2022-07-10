# -*- coding: utf-8 -*-
from sixties import cli


def test_cli_main_ok():
    argv = ['ignored', 'printed']
    assert cli.main(argv) == argv
