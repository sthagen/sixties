# -*- coding: utf-8 -*-
"""Command line arg for sixties."""
import sys
from typing import List, Union


def main(argv: Union[List[str], None] = None) -> int:
    """Drive the understanding ..."""
    argv = sys.argv if argv is None else argv
    print(argv)
    return 0
