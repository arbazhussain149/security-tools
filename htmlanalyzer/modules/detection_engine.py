#!/usr/bin/python
from console_output_beautifier import ConsoleOutputBeautifier
from utils import print_output_line


# @TODO: libraries/framework detenction
# detects frontend framework used
def detect_framework(_line):
    """frontend framework detection (simplified)
        WARNING!!!
        This detection is only some assumption based on some constant
        elements but can not be treat as 100% sure.
    """
    _fw = ""
    if "ng-app" in _line:
        _fw = "Angular 1.*"
    if "react.js" in _line or "react-dom.js" in _line:
        _fw = "ReactJS"

    return _fw


# using osftare recognition
def identify(_line):
    """backend detection (simplified)"""
    _ident = "unknown"
    if "Jommla" in _line:
        _ident = "Joomla CMS"
    if "wp-content" in _line:
        _ident = "WordPress CMS"
    return _ident


def detect_comments(_line, i):
    """detects comments"""
    if '<!--' in _line.lstrip():
        if "\"/" in _line:
            print_output_line(i, ConsoleOutputBeautifier.getColor("red"),
                              "COMMENTED PATH found at line %d:   %s",
                              (i, _line.lstrip().rstrip()), "COMMENT")
        else:
            print_output_line(i, ConsoleOutputBeautifier.getColor("yellow"),
                              "COMMENT found at line %d:   %s",
                              (i, _line.lstrip().rstrip()), "COMMENT")


def detect_admin_stuff(_line, i):
    """detects anything related to administration area"""
    if "admin" in _line.lower():
        print_output_line(i, ConsoleOutputBeautifier.getColor("red"),
                          "'admin' string found at line: %d", i, "ADMIN")


def detect_debug(_line, i):
    """detects debug messages left by developers"""
    if "debug" in _line.lower():
        print_output_line(i, ConsoleOutputBeautifier.getColor("red"),
                          "DEBUG information found at line %d", i, "DEBUG")


def detect_external_resources(_line, i):
    """detects external resources like imgs, iframes, scripts"""
    if "src" in _line.lower():
        if "<img" in _line.lower():
            print_output_line(i, ConsoleOutputBeautifier.getColor("cyan"),
                              "PATH to external resource image "
                              " file found in %d:   %s",
                              (i, _line.lstrip().rstrip()[0:80]), "RESOURCES")
        if "<iframe" in _line.lower():
            print_output_line(i, ConsoleOutputBeautifier.getColor("cyan"),
                              "IFRAME path found in %d:   %s",
                              (i, _line.lstrip().rstrip()[0:80]), "RESOURCES")
        if "<script" in _line.lower():
            print_output_line(i, ConsoleOutputBeautifier.getColor("cyan"),
                              "external SCRIPT path found in %d:   %s",
                              (i, _line.lstrip().rstrip()[0:80]), "RESOURCES")


def detect_javascript(_line, i):
    """detects inline JavaScript occurences, as a script or event handler
    inside HTML tag"""
    if "<script" in _line.lower() and "src" not in _line.lower():
        print_output_line(i, ConsoleOutputBeautifier.getColor("green"),
                          "inline <SCRIPT> tag found at line %d", i, "SCRIPT")
    if "javascript:" in _line.lower():
        print_output_line(i, ConsoleOutputBeautifier.getColor("cyan"),
                          "INLINE JavaScript event handler found at line %d", i,
                          "JAVASCRIPT")
