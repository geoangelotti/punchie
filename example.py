#!/usr/bin/env python

import punchie

punchie.make_yamls()
secret = 0

collection = punchie.Holder('example.f', 'ibm_026_fort', secret)
collection.write_punched()
