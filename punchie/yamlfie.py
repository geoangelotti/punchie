import codecs


def make_026_fort():
	in_file = codecs.open('Punched_cards/ibm_026.puc', encoding='utf8', mode='r')
	punched_card = {}
	y = 0
	x = 0
	for line in in_file:
		x = 0
		for ch in line:
			if ch != '\n':
				punched_card[y, x] = ch.encode('utf8')
			x += 1
		y += 1
	out_file = codecs.open('Yamls/ibm_026_fort.yaml', 'w+', encoding='utf8')
	for i in range(5, x - 2):
		key = '\\' + punched_card[0, i].encode('utf8') + ': '
		val = ''
		for j in range(4, y - 1):
			if punched_card[j, i] == ' ':
				val += '_'
			else:
				temp = u'\u2588'
				temp.encode('utf8')
				val += temp
		if (i < 44) or (i == 45) or (i == 46) or (i == 51) or (i == 52) or (i == 57) or (i == 58) or (i == 63) or (i == 64):
			out_file.write(key + '\'' + val + '\'' + '\n')


def make_026_comm():
	in_file = codecs.open('Punched_cards/ibm_026.puc', encoding='utf8', mode='r')
	punched_card = {}
	y = 0
	x = 0
	for line in in_file:
		x = 0
		for ch in line:
			if ch != '\n':
				punched_card[y, x] = ch.encode('utf8')
			x += 1
		y += 1
	out_file = codecs.open('Yamls/ibm_026_comm.yaml', 'w+', encoding='utf8')
	for i in range(5, x - 2):
		key = '\\' + punched_card[1, i].decode('utf8') + ': '
		val = ''
		for j in range(4, y - 1):
			if punched_card[j, i] == ' ':
				val += '_'
			else:
				temp = u'\u2588'
				temp.encode('utf8')
				val += temp
		if (i < 44) or (i == 45) or (i == 46) or (i == 51) or (i == 52) or (i == 57) or (i == 58) or (i == 63) or (i == 64):
			out_file.write(key + '\'' + val + '\'' + '\n')

