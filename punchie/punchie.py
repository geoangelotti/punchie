import sys
import os
import codecs
import yaml
import datetime


class PunchedCard:
	def __init__(self, pc):
		self.content = pc


def empty_card():
	in_file = codecs.open('Punched_cards/empty.puc', 'r', encoding='utf8')
	punched_card = {}
	y = 0
	x = 0
	for line in in_file:
		x = 0
		for ch in line:
			punched_card[y, x] = ch
			x += 1
		y += 1
	return punched_card


def get_string(in_f):
	if os.path.exists(in_f):
		in_file = codecs.open(in_f, 'r', encoding='utf8')
		string = ''
		for line in in_file:
			string += line
		return string
	else:
		sys.stderr.write("File {} does not exist.\n".format(in_f))
		return ''


def create_punched(in_str, secret):
	lines = in_str.split('\n')
	c = 0
	for line in lines:
		punched = PunchedCard(empty_card())
		yaml_in = codecs.open('Yamls/ibm_026_fort.yaml', 'r', encoding='utf8')
		ibm_026 = yaml.safe_load(yaml_in)
		for i in range(0, len(line) - 1):
			key = ''
			j = ''
			try:
				if secret == 0:
					punched.content[1, i + 3] = line[i]
				key = line[i].upper()
				if key == ' ':
					key = ''
				bcd = ibm_026['\\' + key]
				for j in range(2, 14):
					if bcd[j - 2] == '_':
						pass
					else:
						punched.content[j, i + 3] = u'\u2588'
						punched.content[j, i + 3].encode('utf-8')
			except KeyError:
				sys.stderr.write("Key error on {} or {},{} tuple.\n".format(key.encode('utf8'), j, i))
		outpath = 'Punched_cards/gen_' + str(datetime.datetime.now().strftime('%H.%M.%S')) + '.' + str(c) + '.puc'
		out_file = codecs.open(outpath, 'w+', encoding='utf8')
		for j in range(0, 15):
			ans = ''
			for i in range(0, 67):
				ans += punched.content[j,i]
			# print ans
			out_file.write(ans + '\n')
		c += 1
