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
		self.timestamp = None
		self.file_data = None
		self.reference_code = None
		self.batch_number = None
	def parse_line(self, s):
		if s[0] == '1':
			# first line of header
			self.priority_code = int(s[1:2])
			s = s[3:]
			self.routing_snumber = int(s[:9])
		elif s[0] == '5':
			# second line of header
			pass
		elif s[0] == '6':
			# transaction
			pass
		elif s[0] == '8':
			# first line of footer
			pass
		elif s[0] == '9':
			# second line of footer
			pass
