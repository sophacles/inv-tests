from liba import liba
from libb import libb

from invoke import Program

myprog = Program(name = 'myprog',
                 binary = 'myprog',
                 namespace=liba)

otherprog = Program(name = 'myprog',
                    binary = 'myprog',
                    namespace = libb)

