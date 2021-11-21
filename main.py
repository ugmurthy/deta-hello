from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import os
from markdown import markdown as md 
import csv 
from deta import Deta, Drive

with open("index.html","r") as f:
	html = f.read()

with open("README.md",'r') as f:
	md_content = f.read()
	content = md(md_content)

html = html.replace("{{README}}",content)

env1 = os.getenv("DB_SECRET")
env2 = os.getenv("API_SECRET")
DB_PROJECT_ID = os.getenv("DB_PROJECT_ID")

items =  [
		{ "id": "P001","item":"apples","qty":100 },
		{ "id": "P002","item":"bpples","qty":200 },
		{ "id": "P003","item":"cpples","qty":300 },
		{ "id": "P004","item":"dpples","qty":400 },
		{ "id": "P005","item":"epples","qty":500 },
		{ "id": "P006","item":"fpples","qty":600 },
		{ "id": "P007","item":"gpples","qty":700 },

	]
 
cwd = os.getcwd()
home = os.environ 

app=FastAPI()

@app.get("/", response_class=HTMLResponse)
def get_root():
	return html
	
@app.get("/hello")
def say_hello():
	return {"Hello":"World"}

@app.get("/items/")
def get_items():
	return items 

@app.get("/item/")
def get_some_items(item_id: str):
	return [item for item in items if item_id in item['id']]


@app.get("/env/")
def get_env():
	details = {}
	details.update({"deta_env_vars": {"API_SECRET": env2, "DB_SECRET": env1} })
	details.update({"osname":os.name})
	details.update({"current_working_dir":os.getcwd()})
	details.update({"files":os.listdir()})
	
	return details
