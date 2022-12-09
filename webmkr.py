import os
import time
import markdown
import sys


def updater(branch):
	if branch == "stable":
		print("Downloading from Stable Branch")
		print("This is a sample and is not avalable right now")
		sys.exit()

		sys.exit()
	if branch == "developer":
		print("Downloading from Developer Branch")
		os.system("curl https://raw.githubusercontent.com/Dunn-Dev8/Webmkr.py/dev-fermata/webmkr.py")
		sys.exit()
	
def ver():
	print("Developer-0.31:2022")
	sys.exit()

def news():
	print("NEWS: Feed Cannot Be Reached At This Time ")
	sys.exit()

def indexer_clean(btype):
    cwd = os.getcwd()
    indexer = (cwd+"/posts/index.html")

    with open(indexer, "w") as file:
        file.write("")
        file.close

    with open(indexer, "a") as file:
        file.write("<h3>Recent "+btype+"</h3>")
        file.write("<link href=\"theme.css\" rel=\"stylesheet\">")
        file.write("<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />\n")
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

# Argument Passing
if len( sys.argv ) > 1:
	if sys.argv[1] == "-v":
		ver()
	
	if sys.argv[1] == "-n":
		news()
	if sys.argv[1] == "-h":
		print("Webmkr CLI Menu\nUpdate: -u\nNews \(Work In Progress): -n\nCheck Version: -v")
		sys.exit()

	if sys.argv[1]  == "-u":
		print("Updating...")
		print("Remember end with dev if you would like to download from the developer branch")
		time.sleep(3)
		if len( sys.argv ) == 3:
			if sys.argv[2] == "dev":
					updater("developer")
		else:	
			print("TRY FAILED")
			updater("stable")
			
			
postmk_mark()

print("Posts and Index have been Updated")

print("\nRemember you are on the Developer Branch so you can use the fancy CLI, try typing\npython3 webmkr.py -h for more")


