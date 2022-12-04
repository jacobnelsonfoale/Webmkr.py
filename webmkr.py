import os
import markdown



def indexer_clean(btype):
    cwd = os.getcwd()
    indexer = (cwd+"/posts/index.html")

    with open(indexer, "w") as file:
        file.write("")
        file.close

    with open(indexer, "a") as file:
        file.write("<h3>Recent "+btype+"</h3>")
        file.write("<link href=\"theme.css\" rel=\"stylesheet\">")
        file.write("<link rel=\"icon\" type=\"image/x-icon\" href=\"../favicon.ico\" />")
        file.close




def postmk_func(title, content, author, date):
    fullpath = os.getcwd()
    path = fullpath+"/posts"

    

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
    
    #makes file viewable in the posts folder

    indexer = os.path.join(path, "index.html")
    with open(indexer, "a") as file:
       file.write("<a href=\""+(title)+".html\">"+(title)+"</a>")
       file.close

def postmk_mark():
    
    cwd = os.getcwd()
    posts = "/posts/"
    filelist = cwd+"/markdown/"
    path = cwd+"/posts"
    indexer = os.path.join(path+"/index.html")

    indexer_clean("Blog Posts") 

    
    for filename in os.listdir(filelist):
   
        title = os.path.basename(filename).split('.')[0]
        path = cwd+"/posts"
        
        with open(filelist+filename, 'r') as file:
            text = file.read()
            html = markdown.markdown(text)
            file.close
       
        with open(cwd+posts+title+".html", 'w') as file:
            file.write(html)
            file.write("<title>"+title+"</title>")
            file.write("<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />\n")
            file.write("<link href=\"theme.css\" rel=\"stylesheet\">")
            file.write("<link rel=\"icon\" type=\"image/x-icon\" href=\"../favicon.ico\" />")
            file.write("<a href=\"../index.html\">Go Back Home</a>")
            file.close
            
            

            with open(indexer, "a") as file:
                file.write("<a href=\""+(title)+".html\">"+(title)+"</a>")
                file.write("<br>")
                file.close


        

#uncomment to make post
#postmk_func("Hello World!", "This is a example of a basic webmanager post, you can edit this post by going to postmkr and editing the details of this post. Then try running postmkr.py with.\nPYTHON3 POSTMKR.PY", "Dunnk00p", "3 Dec 2022")

postmk_mark()

