import os

def postmk(title, content, author, date):
    fullpath = os.getcwd()
    path = fullpath+"/posts"

    index = os.path.join(path, title+".html")

    with open(index, "w") as file:
        file.write("<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />\n")
        file.write("<style>body{background-color:#4F4F4F;}p{color:#CFCFCF} h3{color:#CFCFCF}h5{color:#CFCFCF}a{color:chocolate}::selection{color:coral}</style>\n")
        file.write("<link rel=\"icon\" type=\"image/x-icon\" href=\"../favicon.ico\" />")
        file.write("<title>"+title+"</title>")
        file.write("<h3>"+title+"</h3>\n")
        file.write("<h5>"+author+"</h5>\n")
        file.write("<p>"+content+"</p>\n")
        file.write("<a href=\"../index.html\">Go Back Home</a>")
        file.close
def pagemk(name, content):
    with open(name+".html", "w") as file:
        file.write("<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />\n")
        file.write("<style>body{background-color:#4F4F4F;}p{color:#CFCFCF} h3{color:#CFCFCF}h5{color:#CFCFCF}a{color:chocolate}::selection{color:coral}</style>\n")
        file.write("<link rel=\"icon\" type=\"image/x-icon\" href=\"../favicon.ico\" />")
        file.write("<title>"+name+"</title>")
        file.write("<h3>"+name+"</h3>\n")
        file.write("<p>"+content+"</p>")
        file.write("<a href=\"./index.html\">Go Back Home</a>")
        file.close

#uncomment to make post
#postmk("Hello World!", "This is a example of a basic webmanager post, you can edit this post by going to postmkr and editing the details of this post. Then try running postmkr.py with.\nPYTHON3 POSTMKR.PY", "Dunnk00p", "3 Dec 2022")

#uncomment to make page
#pagemk("Contact", "Email: contact@example.com<br>Fax: ????")
