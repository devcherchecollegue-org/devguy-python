#!/usr/bin/env python3

import getopt
import os
import pathlib
import re
import sys

from watchdog.events import PatternMatchingEventHandler
from watchdog.observers import Observer


# comment

os.environ["ENV_TYPE"] = 'local'

help_message = """python test.py [options]

Run test for DevBot API.

OPTIONS:
    -a, --no-capture        do not capture output from test calls
    -c, --cover             generate coverage report
    -f, --force-all         while watching, reload all path instead of modified related test file
    -h, --help              print this message
    -p PATH, --path PATH    witch path the tests must be ran on
    -t, --env-test          use test configuration
    -e, --env               set environment for test
    -v, --verbose           show full logs
    -w, --watch             watch for change and run test
    -x, --force-stop        stop on first error
"""

options = ""
run = True
watch = False
path = 'tests'
force_all = False


def run_test(options: str = ' -x -c -v', path: str = '.') -> int:
    cmd = './run_test.py' + options + ' -p ' + path
    return os.system(cmd)


class HandleTest(PatternMatchingEventHandler):
    patterns = ['*.py']
    ignore_directories = False
    _ignore_patterns = ['*__jb_*', '*tmp*', 'main.py', 'test.py', 'test_runner.py']
    case_sensitive = False
    filter = re.compile('.*__jb_.*')
    is_test_file = re.compile('(.*_test.py)|(.*/test_.*.py)')

    def __init__(self, options: str, path: str):
        super(PatternMatchingEventHandler, self).__init__()
        self.options = options
        self._path = path

    def __run(self, path: str):
        print("\n\n############################################\n")
        print("Running Test ......")
        run_test(options, path=self.__test_file(path))
        print("\n\n############################################\n")
        print("Waiting for change ..........")

    def __test_file(self, path: str):
        if force_all:
            print('Forcing all')
            return self._path
        if not self.is_test_file.match(path):
            path = path.replace('app', 'tests', 1)
            return path[:-3] + '_test' + path[-3:]
        return path

    def __filter_event__(self, event):
        if event.event_type == 'moved' and (
                self.filter.match(event.src_path) or self.filter.match(event.dest_path)):
            return
        self.__run(event.src_path)

    def on_any_event(self, event):
        self.__filter_event__(event)


try:
    opts, args = getopt.getopt(
        sys.argv[1:], "awhcvtxfp:e:",
        ["help", "cover", "verbose", "env-test", "force-stop", "watch", "force-all", "no-capture",
            "path=", 'env=']
    )
    for opt, arg in opts:
        if opt in ('-c', '--cover'):
            options += ' -c'
        elif opt in ('-p', '--path'):
            path = arg
        elif opt in ('-w', '--watch'):
            watch = True
        elif opt in ('-f', '--force-all'):
            force_all = True
        elif opt in ('-x', '--force-stop'):
            options += ' -x'
        elif opt in ('-v', '--verbose'):
            options += ' -v'
        elif opt in ('-a', '--no-capture'):
            options += ' -a'
        elif opt in ('-t', '--test'):
            os.environ["ENV_TYPE"] = 'test'
        elif opt in ('-e', '--env'):
            os.environ["ENV_TYPE"] = '{}'.format(arg)
        elif opt in ('-h', '--help'):
            print(help_message)
            run = False

except Exception:
    options = '-x --cov-config=.coveragerc --cov-config=.coveragec --cov-report html --cov=v2 -v test'

if run:
    if watch:
        print(path)
        run_test(options, path=path)
        print("Watching for change ....")
        observer = Observer()
        observer.schedule(HandleTest(options, path), path=pathlib.Path().absolute(), recursive=True)
        observer.start()
        try:
            while True:
                pass
        except KeyboardInterrupt:
            observer.stop()
        observer.join()
    else:
        sys.exit(run_test(options, path=path))
