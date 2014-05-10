#!/usr/bin/env python
import os
import airspeed
import yaml
from optparse import OptionParser
"""
"""

def get_args():
    parser = OptionParser(usage="%prog [options]",
        description="Fills in templates from YAML source to generate merged results.")

    parser.add_option("-s", "--source",
        default='input.yaml',
        help="Filename of the YAML source. Defaults to input.yaml")

    parser.add_option("-t", "--template",
        default='template.vm',
        help="Filename of the output template. Defaults to template.vm")
    parser.add_option("-p", "--params",
        default='',
        help="params to provide (comma separated)")

    options, leftover = parser.parse_args()

    return options, leftover

def build_params(params):
    parts = params.split(',')
    map = {}
    for part in parts:
        pair = part.split('=')
        map[pair[0]] = pair[1]

    return map

if __name__ == '__main__':
    options, leftover = get_args()

    def env(key):
        return os.environ.get(key,'')

    yaml = yaml.load(open(options.source, 'r').read())

    params = build_params(options.params)

    loader = airspeed.CachingFileLoader(".")
    template = loader.load_template(options.template)
    #template.merge(contents, loader=loader)
    print template.merge(locals())

