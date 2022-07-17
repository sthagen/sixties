# -*- coding: utf-8 -*-
from sixties import cli


def test_cli_main_ok(capsys):
    argv = ['ignored', 'printed']
    assert cli.main(argv) == 0
    out, err = capsys.readouterr()
    assert out.strip() == str(argv)
    assert not err
