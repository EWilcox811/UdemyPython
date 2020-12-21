import csv
import re
#   Open the file
pwd
path = 'C:\\Users\\vein8\\Desktop\\Coding\\Python\\UDEMY\\Complete-Python-3-Bootcamp\\15-PDFs-and-Spreadsheets\\'
data = open(path + 'example.csv', encoding='utf-8')

#   csv.reader
csv_data = csv.reader(data)

#   reformat into a python object(list of lsits)
data_lines = list(csv_data)
data_lines

all_emails = []
for line in data_lines[1::]: #For loop to extract all emails from the csv
    all_emails.append(line[3])
all_emails

full_names = []

for line in data_lines[1:]:
    full_names.append(line[1]+' '+line[2])
full_names

file_to_output = open('to_save_file.csv',mode = 'w', newline='')
csv_writer = csv.writer(file_to_output, delimiter=',')
csv_writer.writerow(['a','b','c'])
csv_writer.writerows([['1','2','3'],['4','5','6']])
file_to_output.close()


###     WORKING WITH PDFs   ###
import PyPDF2
f = open(path+'Working_Business_Proposal.pdf','rb')
pdf_reader = PyPDF2.PdfFileReader(f)
pdf_reader.numPages
page_one = pdf_reader.getPage(0)
page_one_text = page_one.extractText()
page_one_text
f.close()


pdf_reader = PyPDF2.PdfFileReader(f)
first_page = pdf_reader.getPage(0)
pdf_writer = PyPDF2.PdfFileWriter()
pdf_writer.addPage(first_page)
pdf_output = open('Some_BrandNew_Doc.pdf','wb')
pdf_writer.write(pdf_output)
f.close()
pdf_output.close()
f = open(path + 'Working_Business_Proposal.pdf','rb')
pdf_text = []
pdf_reader = PyPDF2.PdfFileReader(f)
for num in range(pdf_reader.numPages):
    page = pdf_reader.getPage(num)

    pdf_text.append(page.extractText())
pdf_text
f.close()


###     PDF CSV puzzle      ###
data = open(path + 'Exercise_files\\find_the_link.csv', encoding = 'utf-8')
csv_data = csv.reader(data)
data_lines = list(csv_data)
link = ''
n = 0
for line in data_lines:
    link = link + line[n]
    n +=1
link
data.close()

pdf_text = []
f = open(path+'Exercise_files\\Find_the_Phone_Number.pdf', 'rb')
pdf_reader = PyPDF2.PdfFileReader(f)
for num in range(pdf_reader.numPages):
    pdf_text.append(pdf_reader.getPage(num).extractText())
pattern = r'\d{3}\W\d{3}\W\d{4}'
for page in pdf_text:
    phone = re.search(pattern,page)
    if type(phone) != type(None):
        print(phone.group())
        break
