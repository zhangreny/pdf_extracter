import pdfplumber
import re

def read_pdf_content(pdf_path):
    pdf_text = ""
    with pdfplumber.open(pdf_path) as pdf:
        num_pages = len(pdf.pages)
        for page_num in range(num_pages):
            page = pdf.pages[page_num]
            page_text = page.extract_text()
            pdf_text += page_text
    return pdf_text

pdf_path = "GB 17859-1999.pdf"
pdf_content = read_pdf_content(pdf_path)
lines = pdf_content.split("\n")

numanddot = "^\d+(\.\d+)*.*"
tmp = []
for line in lines:
    match = re.match(numanddot, line)
    if match:
        tmp.append(match.group())

def extract_integer(s):
    num_str = ""
    for char in s:
        if char.isdigit():
            num_str += char
        else:
            break
    
    if num_str:
        return int(num_str)
    else:
        return None


# 找到最后一个x.x.x
numanddot = "^\d+(\.\d+)+.*"
for i in range(len(tmp)-1, -1, -1):
    match = re.match(numanddot, tmp[i])
    if match:
        final = tmp[i]
        break
finalint = extract_integer(final)

tmp2 = []
for t in tmp:
    if extract_integer(t) <= finalint: # 才有效
        tmp2.append(t)
        print(t)
    
pattern = r"^\d+(\.\d+)*"
replacement = ""
with open("output.txt", "w", encoding="utf-8") as f:
    for t in tmp2:
        match = re.search(pattern, t)
        if match:
            removed_part = match.group()
            result = re.sub(pattern, replacement, t)
            tabnum = len(removed_part.split("."))-1
            outstr = '\t'*tabnum + result.strip()
            print(outstr)
            f.write(outstr+'\n')
            

