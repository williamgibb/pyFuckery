import argparse
import os
from fuckery.cli import main


# Assets Configuration
ASSETS = os.path.join(os.path.abspath(os.path.split(__file__)[0]), 'assets')
assert os.path.isdir(ASSETS)


def test_main():
    fn = 'hello_world.bf'
    fp = os.path.join(ASSETS, fn)
    ns = argparse.Namespace()
    ns.verbose = False
    ns.input = fp
    main(options=ns)
