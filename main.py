from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import os

env1 = os.getenv("DB_SECRET")
env2 = os.getenv("API_SECRET")
cwd = os.getcwd()
home = os.envrion

print(cwd)
print(home)

app=FastAPI()

@app.get("/", response_class=HTMLResponse)
def get_root():
	return """
	<html>
    	<head>
        	<title>Hello World</title>
        	<h2>Hello World</h2>
        	<hr>

        	<p>
            This is a simple API implemented on FastAPI to demonstrate deploy from a public GitHub repository
            the API is hosted on a <a href="https://deta.sh/">deta micro</a>
        	</p>
        	<p> API documentation is available <a href="/docs">here</a></p>
    	</head>
	</html>

	"""
@app.get("/hello")
def say_hello():
	return {"Hello":"World"}

@app.get("/items/")
def get_items():
	return [
		{ "id": "P001","item":"apples","qty":100 },
		{ "id": "P002","item":"bpples","qty":200 },
		{ "id": "P003","item":"cpples","qty":300 },
		{ "id": "P003","item":"dpples","qty":400 },
		{ "id": "P005","item":"epples","qty":500 },
		{ "id": "P006","item":"fpples","qty":600 },
		{ "id": "P007","item":"gpples","qty":700 },

	]

@app.get("/env/")
def get_env():
	details = {}
	details.update({"deta_env_vars": {"API_SECRET": env2, "DB_SECRET": env1} })
	details.update({"osname":os.name})
	#details.update({"os_uname":os.uname()})
	#details.update({"homedir":os.environ['HOME']})
	details.update({"cwd":os.getcwd()})
	
	return details



