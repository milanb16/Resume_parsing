import tika
from tika import parser
import re
class resume:
	def parse():
		tika.initVM()
		parsed=parser.from_file("resum.docx")
		phone=re.compile(r"[0-9]{10}")
		print("Phone Number:"+re.search(phone,parsed["content"]).group())
		mail=re.compile(r"[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}",re.IGNORECASE)
		print("E-mail id:"+re.search(mail,parsed["content"]).group())
	if __name__=="__main__":
		parse()