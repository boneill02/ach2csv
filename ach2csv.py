import argparse
import re

def extract_element(s, l=-1):
	"""
	Takes a substring of length n, or until multiple whitespace characters
	are found, from the beginning of the string s.
	
	Parameters
	----------
	s : str
		the string to extract from
	l : int
		the length to extract (-1 if until multiple whitespace)
	
	Returns
	-------
	tuple of length 2
	The first element is s without the extracted string, and the
	second is the extracted string.
	"""
	if l == -1:
		s = s.strip()
		p = re.compile(r'\s\s+')
		res = p.split(s)
		return (s[len(res[0]):], res[0])
	else:
		# extract string of length l
		return (s[l:], s[:l + 1])

class ACHData:
	def __init__(self, s):
		self.parse_line(s)

	def parse_line(self, s):
		f = s[0]
		s = s[1:]
		if f == '1':
			# first line of header
			s, self.priority_code = extract_element(s, 2)
			s, self.routing_snumber = extract_element(s, 9)
			s, self.company_id = extract_element(s, 10)
			s, self.date = extract_element(s, 6)
			s, self.time = extract_element(s, 4)
			s, self.file_data = extract_element(s, 7)
			s, self.bank_name = extract_element(s)
			s, self.company_name = extract_element(s)
			s, self.reference_code = extract_element(s)
		elif f == '5':
			# second line of header
			pass
		elif f == '6':
			# transaction
			pass
		elif f == '8':
			# first line of footer
			pass
		elif f == '9':
			# second line of footer
			pass

class ACHFile:
	def __init__(self, lines):
		self.lines = lines
		self.data = []
		self.parse()

	def parse(self):
		for l in self.lines:
			self.data.append(ACHData(l))

	def print_data(self, idx):
		print('Priority Code: ' + self.data[idx].priority_code)
		print('Recipient Routing Number: ' + self.data[idx].routing_snumber)
		print('Company ID: ' + self.data[idx].company_id)
		print('Date: ' + self.data[idx].date)
		print('Time: ' + self.data[idx].time)
		print('File Data Information: ' + self.data[idx].file_data)
		print('Bank name: ' + self.data[idx].bank_name)
		print('Company name: ' + self.data[idx].company_name)
		print('Reference Code: ' + self.data[idx].reference_code)

if __name__ == '__main__':
	parser = argparse.ArgumentParser(prog='ach2csv',
                                     description='Convert ACH files to CSV')
	parser.add_argument('filename')
	args = parser.parse_args()

	with open(args.filename) as f:
		ach_file = ACHFile(f.readlines())
		ach_file.print_data(0)
