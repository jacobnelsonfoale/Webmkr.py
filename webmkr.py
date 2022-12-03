import os

def postmk_func(title, content, author, date):
    fullpath = os.getcwd()
    path = fullpath+"/posts"

    index = os.path.join(path, title+".html")

    with open(index, "w") as file:
        file.write("<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />\n")
        file.write("<link href=\"theme.css\" rel=\"stylesheet\">")
        file.write("<link rel=\"icon\" type=\"image/x-icon\" href=\"../favicon.ico\" />")
        file.write("<title>"+title+"</title>")
        file.write("<h3>"+title+"</h3>\n")
        file.write("<h5>"+author+"</h5>\n")
        file.write("<p>"+content+"</p>\n")
        file.write("<a href=\"../index.html\">Go Back Home</a>")
        file.close

def postmk_mark():
    pass

#uncomment to make post
postmk_func("Hello World!", "This is a example of a basic webmanager post, you can edit this post by going to postmkr and editing the details of this post. Then try running postmkr.py with.\nPYTHON3 POSTMKR.PY", "Dunnk00p", "3 Dec 2022")

postmk_mark()

