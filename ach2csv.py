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
		p = re.compile('\s\s+')
		res = p.split(s)
		return (s[len(res[0]):], res[0])
	else:
		# extract string of length l
		return (s[l:], s[:l + 1])

class ACHData:
	def __init__(self):
		self.priority_code = None
		self.service_class_code = None
		self.entry_class = None
		self.entry_desc = None
		self.routing_snumber = None
		self.bank_name = None
		self.company_id = None
		self.company_name = None
		self.date = None
		self.time = None
		self.file_data = None
		self.reference_code = None
		self.batch_number = None
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

	def print_data(self):
		print("Priority Code: " + self.priority_code)
		print("Recipient Routing Number: " + self.routing_snumber)
		print("Company ID: " + self.company_id)
		print("Date: " + self.date)
		print("Time: " + self.time)
		print("File Data Information: " + self.file_data)
		print("Bank name: " + self.bank_name)
		print("Company name: " + self.company_name)
		print("Reference Code: " + self.reference_code)

# Testing stuff
ach_file = ACHData()
ach_file.parse_line('101 12400297111234567892106222214A094101WELLS FARGO BANK NA    LendPro                 000000000')
ach_file.print_data()
