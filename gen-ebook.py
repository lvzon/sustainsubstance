#!/usr/bin/python3

import re
import sys
import os

base_url = "http://sustainsubstance.org"
base_path = "content"

email = {"Levien van Zon": "levien@sustainsubstance.org"}

ifname = sys.argv[1]
ofname_pdf = 'tmp_latex.md'
ofname_epub = 'tmp_epub.md'

infile  = open(ifname, "r")
outfile_pdf  = open(ofname_pdf, "w")
outfile_epub  = open(ofname_epub, "w")

ofbasename = sys.argv[2]

print ("Input file:", ifname)

keyval = re.compile(r'(.*?):\s+(.*)'    )
header = {}

for line in infile:
    match = keyval.match(line)
    if (match):
        print(match.groups())
        (key, val) = match.groups()
        header[key] = val
    else:
        break

page_filename = header["Slug"] + ".html"
page_url = base_url + "/" + page_filename

print("Page file:", page_filename)

title = header["Title"]

yaml = "---\ntitle: "
yaml += "\n- type: main\n  text: "
yaml += title + "\n"
yaml += "- type: collection\n  text: The Substance of Sustainability\n"
yaml += "creator:\n- role: author\n  text: "
yaml += header["Authors"] + "\n"
if (email[header["Authors"]]):
    yaml += "  email: " + email[header["Authors"]] + "\n"
yaml += "date: " + header["Date"] + "\n"
yaml += "URL: "+ page_url + "\n"
yaml += "language: en-GB\n"
yaml += "rights: Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)\n"
yaml += "\n---\n\n"
outfile_epub.write(yaml)

yaml = "---\ntitle: " + title + "\n"
if (email[header["Authors"]]):
    yaml += "author: " + header["Authors"] + " (<" + email[header["Authors"]] + ">) \n"
else:
    yaml += "author: " + header["Authors"] + "\n"
yaml += "date: " + header["Date"] + "\n"
yaml += "papersize: A4\n"
yaml += "fontsize: 11pt\n"
yaml += "mainfont: Futura   Lt BT\n"
yaml += "colorlinks: true\n"
#yaml += "header-includes:\n- "
#yaml += r"\usepackage{endnotes}" + "\n- "
#yaml += r"\usepackage[a4paper]{geometry}" + "\n- "
#yaml += r"\let\footnote=\endnote" + "\n"
yaml += r"include-before: \raggedright" + "\n"
yaml += r"include-after: \raggedright\theendnotes" + "\n"
#yaml += r"\usepackage{fontspec}" + "\n- "
#yaml += r"\defaultfontfeatures{Mapping=tex-text}" + "\n- "
#yaml += r"\setmainfont{Futura Lt BT}"
#yaml += "output:\n  pdf_document:\n    keep_tex: yes\n    latex_engine: xelatex\n"
yaml += "\n---\n\n"
outfile_pdf.write(yaml)


outfile_epub.write("Published: " + header["Date"] +"   \nSource URL: <" + page_url + ">\n\n")
outfile_pdf.write("Source URL: <" + page_url + ">\n\n")


for line in infile:
    # TODO: replace links to .md-files by full website URLs
    match = re.search(r'\{filename\}(\/[\w\-\/]+).md', line)
    if (match):
        #print(match)
        print("Fixing link to", match.group(1) + ".md")
        line = line.replace(r'{filename}' + match.group(1) + ".md", match.group(1) + ".html")
        print(line)

    match = re.search(r'[\(\"](\/.*?)[\)\"]', line)
    if (match):
        print("Fixing link to", match.group(1))
        line = line.replace(match.group(1), base_url + match.group(1))
        print(line)

    line = line.replace(r'{filename}', base_path)

    pdfline = str(line)
    if pdfline.startswith("**Footnotes:**"):
        pdfline = ""
    if pdfline.startswith("### Notes:"):
        pdfline = ""

    match = re.search(r'\<\/*div.*?\>', line)
    if (match):
        print("Removing div-block", match.group(0))
        line = line.replace(match.group(0), "")
        print(line)

    match = re.search(r'\<img src="([^"]+)".*?\>', pdfline)
    if (match):
        print("Fixing image", match.group(1), "from", match.group(0))
        pdfline = pdfline.replace(match.group(0), "\includegraphics{" + match.group(1) + "}")
        print(pdfline)

    match = re.search(r'\<a href="([^"]+)".*?\>', pdfline)
    if (match):
        print("Fixing link", match.group(1), "from", match.group(0))
        pdfline = pdfline.replace(match.group(0), "\href{" + match.group(1) + "}{")
        print(pdfline)
    match = re.search(r'\<\/a>', pdfline)
    if (match):
        print("Ending link")
        pdfline = pdfline.replace(match.group(0), "}")
        print(pdfline)

    outfile_epub.write(line)
    outfile_pdf.write(pdfline)

infile.close()
outfile_epub.close()
outfile_pdf.close()

if not ofbasename:
    ofbasename = title

cmd_pdf = "pandoc -o \"" + ofbasename + ".pdf\" --latex-engine=xelatex -H latex-header.tex tmp_latex.md"
cmd_epub = "pandoc -o \"" + ofbasename + ".epub\" tmp_epub.md"
cmd_mobi = 'ebook-convert "' + ofbasename + '.epub" "' + ofbasename + '.azw3"'

print("Running", cmd_epub)
os.system(cmd_epub)

print("Running", cmd_pdf)
os.system(cmd_pdf)

print("Running", cmd_mobi)
os.system(cmd_mobi)
