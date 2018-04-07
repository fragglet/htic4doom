#!/usr/bin/env python

from __future__ import print_function

import os
import re
import shutil
import sys

EXTN = 'gif'
COMMENT_RE = re.compile(r';.*')
MAPPING_RE = re.compile(r'\s*(\w+)\s+(\w+)\s*$')

def read_mapping(filename):
	with open(filename) as f:
		result = {}
		for lineno, line in enumerate(f):
			line = COMMENT_RE.sub('', line)
			line = line.strip()
			if not line:
				continue
			m = MAPPING_RE.match(line)
			if not m:
				raise Exception(r'%s:%d: invalid syntax' % (
					filename, lineno+1))
			htic, doom = m.group(1), m.group(2)
			result[htic] = doom
		return result

if len(sys.argv) < 3:
	print('Usage: %s <cfg file> <copy from dir>')
	sys.exit(1)

mapping = read_mapping(sys.argv[1])
srcdir = sys.argv[2]

for htic, doom in mapping.items():
	shutil.copy(os.path.join(srcdir, '%s.%s' % (doom.lower(), EXTN)),
	            '%s.%s' % (htic.lower(), EXTN))

