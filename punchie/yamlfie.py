

def make_026_fort():
	with open('Punched_cards/ibm_026.puc', 'r') as in_file:
		Punched_card = {}
		y = 0
		x = 0
		for line in in_file:
			x = 0
			for ch in line:
				if ch != '\n':
					Punched_card[y, x] = ch
				x += 1
			y += 1
		with open('Yamls/ibm_026_fort.yaml', 'w+') as out_file:
			for i in range(5, x - 2):
				key = '\\' + Punched_card[0, i] + ': '
				val = ''
				for j in range(4, y - 1):
					if Punched_card[j, i] == ' ':
						val += '_'
					else:
						val += '0'
				if (i < 47) or (i == 51) or (i == 52) or (i == 57) or (i == 58) or (i == 63) or (i == 64):
					out_file.write(key + '\'' + val + '\'' + '\n')


'''def make_026_comm():
	with open('Punch_cards/ibm_026.puc', 'r') as in_file:
		Punchcard = {}
		y = 0
		x = 0
		for line in in_file:
			x = 0
			for ch in line:
				if ch != '\n':
					Punchcard[y, x] = ch
				x += 1
			y += 1
		with open('Yamls/ibm_026_comm.yaml', 'w+') as out_file:
			for i in range(5, x - 2):
				key = '\\' + Punched_card[0, i] + ': '
				val = ''
				for j in range(4, y - 1):
					if Punched_card[j, i] == ' ':
						val += '_'
					else:
						val += '0'
				if (i < 47) or (i == 51) or (i == 52) or (i == 57) or (i == 58) or (i == 63) or (i == 64):
					out_file.write(key + '\'' + val + '\'' + '\n')
'''
