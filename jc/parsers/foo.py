"""jc - JSON CLI output utility foo Parser

Usage:
    specify --foo as the first argument if the piped input is coming from foo

Examples:

    $ foo | jc --foo -p
    []

    $ foo | jc --foo -p -r
    []
"""
import jc.utils


def process(proc_data):
    """
    schema:
    
        [
          {
            "foo":     string,
            "bar":     boolean,
            "baz":     integer
          }
        ]
    """

    # rebuild output for added semantic information
    return proc_data


def parse(data, raw=False, quiet=False):
    """
    Main parsing function

    Arguments:

        raw:    (boolean) output preprocessed JSON if True
        quiet:  (boolean) suppress warning messages if True
    """
    
    # compatible options: linux, darwin, cygwin, win32, aix, freebsd
    compatible = ['linux', 'darwin', 'cygwin', 'win32', 'aix', 'freebsd']

    if not quiet:
        jc.utils.compatibility(__name__, compatible)

    raw_output = []
    cleandata = data.splitlines()

    # Clear any blank lines
    cleandata = list(filter(None, cleandata))

    if cleandata:
        # parse the content
        pass

    if raw:
        return raw_output
    else:
        return process(raw_output)
