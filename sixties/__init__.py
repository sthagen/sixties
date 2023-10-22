# -*- coding: utf-8 -*-

# [[[fill git_describe()]]]
__version__ = '2023.10.22+parent.f7a532b5'
# [[[end]]] (checksum: 77104eef85a5ba8fcb38d4d6eea72a1f)
__version_info__ = tuple(
    e if '-' not in e else e.split('-')[0] for part in __version__.split('+') for e in part.split('.') if e != 'parent'
)
