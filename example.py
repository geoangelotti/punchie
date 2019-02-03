#!/usr/bin/env python2

import punchie

punchie.make_yamls()

collection = punchie.Holder('example.f', 'ibm_026_fort', 0)
collection.write_punched()