# -*- coding: utf-8 -*-
# pylint: disable=missing-docstring,unused-import,reimported
import sixties.cli as cli



def test_cli_main_ok():
    argv = ["ignored", "printed"]
    assert cli.main(argv) is None
