from html import parser



s = """<html><head><title>HTML Parser - I</title></head>
<body data-modal-target class='1'><h1>HackerRank</h1><br /></body></html>"""



# create a subclass and override the handler methods
class MyHTMLParser(parser.HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        for attr in attrs:
            print(f'-> {attr[0]} > {attr[1]}')
    def handle_endtag(self, tag):
        print("End   :", tag)
    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag)
        for attr in attrs:
            print(f'-> {attr[0]} > {attr[1]}')
# instantiate the parser and fed it some HTML
parser1 = MyHTMLParser()

parser1.feed(s)