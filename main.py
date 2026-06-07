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
        for _,v in enumerate(self.fileContents):
            outcome+=v
        with open(self.filename+".html","w",encoding="utf-8") as fl:
            fl.write(outcome)
            



md = MDtoHTML("test.md")
md.conversion()