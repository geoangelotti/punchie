import codecs


def make_yamls():
	__make_single_line('cdc')
	__make_single_line('dec_026')
	__make_single_line('dec_029')
	__make_single_line('ge_600')
	__make_double_line('ibm_024', ['rept', 'prog'])
	__make_double_line('ibm_026', ['fort', 'comm'])
	__make_triple_line('ibm_029', ['029', 'ibme', 'ebcd'])
	__make_single_line('ibm_1401')
	__make_single_line('univac_1108')


def __make_single_line(target):
	in_file = codecs.open(f'Punched_cards/{target}.puc', encoding='utf8', mode='r')
	x, y, punched_card = __get_puc(in_file)
	out_file = codecs.open(f'Yamls/{target}.yaml', 'w+', encoding='utf8')
	__write_yaml(x, y, punched_card, out_file, 0, 1)


def __make_double_line(target, languages):
	in_file = codecs.open(f'Punched_cards/{target}.puc', encoding='utf8', mode='r')
	x, y, punched_card = __get_puc(in_file)
	i = 0
	for language in languages:
		out_file = codecs.open(f'Yamls/{target}_{language}.yaml', 'w+', encoding='utf8')
		__write_yaml(x, y, punched_card, out_file, i, 2)
		i += 1


def __make_triple_line(target, languages):
	in_file = codecs.open(f'Punched_cards/{target}.puc', encoding='utf8', mode='r')
	x, y, punched_card = __get_puc(in_file)
	i = 0
	for language in languages:
		out_file = codecs.open(f'Yamls/{target}_{language}.yaml', 'w+', encoding='utf8')
		__write_yaml(x, y, punched_card, out_file, i, 3)
		i += 1


def __get_puc(in_file):
	punched_card = {}
	y = 0
	x = 0
	for line in in_file:
		x = 0
		for ch in line:
			if ch != '\n':
				punched_card[y, x] = ch
			x += 1
		y += 1
	return x, y, punched_card


def __write_yaml(x, y, punched_card, out_file, level, contains):
	for i in range(5, x - 2):
		key = f'\\{punched_card[level, i]}: '
		val = ''
		for j in range(2 + contains, y - 1):
			if punched_card[j, i] == ' ':
				val += '_'
			else:
				temp = u'\u2588'
				temp.encode('utf8')
				val += temp
		if punched_card[level, i] != ' ':
			out_file.write(f'{key}\'{val}\'\n')
