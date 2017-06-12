import markdown2

markdowner = markdown2.Markdown()
html = markdowner.convert("#12344*boo!*")
print(html)