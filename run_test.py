#!/usr/bin/env python3
import getopt
import os
import sys

import pytest

if 'ENV_TYPE' not in os.environ or os.environ['ENV_TYPE'] not in (
        'local', 'test', 'docker', 'docker_test'):
    os.environ['ENV_TYPE'] = 'local'

help_message = """python test_runner.py [options]

Run test for TankYou API.

OPTIONS:
    -a, --no-capture        do not capture output from test calls
    -c, --cover             generate coverage report
    -h, --help              print this message
    -p PATH, --path PATH    witch path the tests must be ran on
    -v, --verbose           show full logs
    -x, --force-stop        stop on first error
"""

# TO HAVE FULL PRINT: '--capture=no'
options = []
cover_options = ['--cov-config=.coveragec', '--cov-report', 'html', '--cov=v2']
run = True
path = 'test'

try:
    opts, args = getopt.getopt(sys.argv[1:], "awhcvxp:",
                               ["help", "cover", "verbose", "force-stop", "watch", "path="])
    for opt, arg in opts:
        if opt in ('-c', '--cover'):
            options += cover_options
        elif opt in ('-p', '--path'):
            options.append(arg)
            path = arg
        elif opt in ('-x', '--force-stop'):
            options.append('-x')
        elif opt in ('-v', '--verbose'):
            options.append('-v')
        elif opt in ('-a', '--no-capture'):
            options.append('--capture=no')
        elif opt in ('-h', '--help'):
            print(help_message)
            run = False
except Exception:
    options = [
        '-x', '--cov-config=.coveragerc', '--cov-config=.coveragec', '--cov-report', 'html',
        '--cov=v2', '-v', 'test'
    ]

if run:
    sys.exit(pytest.main(options))
