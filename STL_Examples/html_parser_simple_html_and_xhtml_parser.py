# HTMLParser module as the basis for parsing text files formatted in HTML and XHTML.

import html.parser
from html.entities import name2codepoint


class MYHTMLParser(html.parser.HTMLParser):
    def handle_starttag(self, tag: str, attrs) -> None:
        print("encountered a start tag:", tag)
        for attr in attrs:
            print("     attr:", attr)

    def handle_endtag(self, tag: str) -> None:
        print('encountered a end tag:', tag)

    def handle_data(self, data: str) -> None:
        print('encountered some data:', data)

    def handle_comment(self, data):
        print("Comment  :", data)

    def handle_entityref(self, name):
        c = chr(name2codepoint[name])
        print("Named ent:", c)

    def handle_charref(self, name):
        if name.startswith('x'):
            c = chr(int(name[1:], 16))
        else:
            c = chr(int(name))
        print("Num ent  :", c)

    def handle_decl(self, data):
        print("Decl     :", data)

parser = MYHTMLParser()
parser.feed('<html><head><title>Test</title></head>'
            '<body><h1>Parse me!</h1></body></html>')

parser.feed('<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" '
            '"http://www.w3.org/TR/html4/strict.dtd">')

parser.feed('<img src="python-logo.png" alt="The Python logo">')

parser.feed('<h1>Python</h1>')

for chunk in ['<sp', 'an>buff', 'ered ', 'text</s', 'pan>']:
    parser.feed(chunk)

parser.feed('<p><a class=link href=#main>tag soup</p ></a>')


