'''
# Heading -> <h1>Heading</h1>
## Heading -> <h2>Subheading</h2>
- item -> <ul><li>item</li></ul>
**bold** -> <strong>bold</strong>
*italic* -> <em>italic</em>
[link](https://www.example.com) -> <a href="https://www.example.com">link</a>
(blank line) -> <p></p>
--- -> <hr>
`code` -> <code>code</code>
Sentence -> <p>Sentence</p>
'''
import re

class MDtoHTML:
    def __init__(self,file):
        self.fileContents = []
        self.filename = file

        try: 
            self.filename = self.filename.split(".")[0]
            with open(file, "r", encoding="utf-8") as fl: self.fileContents = fl.read().splitlines()
        except: print("Warning: Name inserted not detected as a filetype.")
        

    def conversion(self):
        outcome = ''''''

        for i,v in enumerate(self.fileContents):
            line = v

            line = re.sub(r'^### (.+)$', r'<h3>\1</h3>', line)
            line = re.sub(r'^## (.+)$', r'<h2>\1</h2>', line)
            line =re.sub(r'^# (.+)$', r'<h1>\1</h1>', line)
            
            line = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', line)
            line = re.sub(r'\*(.+?)\*', r'<em>\1</em>', line)
            line = re.sub(r'`(.+?)`', r'<code>\1</code>', line)
            line = re.sub(r'\[(.+?)\]\((.+?)\)', r'<a href="\2">\1</a>', line)

            line = re.sub(r'^- (.+)$', r'<ul><li>\1</li></ul>', line)
            line = re.sub(r'^---$', r'<hr>', line)
            line = re.sub(r'^$', r'<p></p>', line)

            if not line.startswith("<"): line = f'<p>{line}</p>'

            outcome+=line
            if i!=len(self.fileContents)-1:outcome+="\n"

        with open(self.filename+".html","w",encoding="utf-8") as fl: fl.write(outcome)

md = MDtoHTML("test.md")
md.conversion()