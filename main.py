from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def get_root():
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

