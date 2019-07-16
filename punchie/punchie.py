import sys
import os
import codecs


try:
	# Try to import Yaml
	import yaml
except ImportError:
	# If not then install through pip PyYaml
	import subprocess
	subprocess.call(['pip', '--quiet', 'install', 'pyyaml'])
	import yaml


# Punched Card class
class PunchedCard:
	def __init__(self, pc):
		self.content = pc

	# Print the punched card at the selected path
	def print_keypunch(self, outpath):
		outpath = f'Output/{outpath}.puc'
		try:
			out_file = codecs.open(outpath, 'w+', encoding='utf8')
			for j in range(0, 15):
				line = ''
				for i in range(0, 67):
					line += self.content[j,i]
				out_file.write(f'{line}\n')
		except IOError:
			sys.stderr.write(f"Cannot write {outpath}.\n")


# Holder class that contains Punched Cards
class Holder:
	def __init__(self, inpath, form, secret):
		in_str = get_string(inpath)
		self.in_name = inpath
		lines = in_str.split('\n')
		for line in lines:
			line = line.replace('\r', '')	# Delete carriege return
			while len(line) > 0:
				writen_line = line[0 :64]	# Get the first 64 chars
				keypunch = PunchedCard(empty_card())
				try:
					yaml_reader = codecs.open(f'Yamls/{form}.yaml', 'r', encoding='utf8')
					yaml_keys = yaml.safe_load(yaml_reader)
					for i in range(0, len(writen_line)):
						key = ''
						j = ''
						try:
							if secret == 0:
								keypunch.content[1, i + 3] = writen_line[i].upper()
							key = writen_line[i].upper()
							if key == ' ':
								pass
							else:
								bcd = yaml_keys[f'\\{key}']
								for j in range(2, 14):
									if bcd[j - 2] == '_':
										pass
									else:
										keypunch.content[j, i + 3] = u'\u2588'
										keypunch.content[j, i + 3].encode('utf-8')
						except KeyError:
							sys.stderr.write(f"Key error on {key.encode('utf8')} or {j},{i} tuple.\n")
					self.punched_cards.append(keypunch)
				except IOError:
					sys.stderr.write(f"Format {form} not valid.\n")
				line = line[64 : len(line)]

	# Print all Punched Cards of Holder
	def write_punched(self):
		i = 0
		for keypunch in self.punched_cards:
			keypunch.print_keypunch(f'{self.in_name}.{str(i)}')
			i += 1

	in_name = ''
	punched_cards = []


# Create an empty punch card dictionary
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


# Get string from file
def get_string(in_f):
	if os.path.exists(in_f):
		in_file = codecs.open(in_f, 'r', encoding='utf8')
		string = ''
		for line in in_file:
			string += line
		return string
	else:
		sys.stderr.write(f"File {in_f} does not exist.\n")
		return ''
