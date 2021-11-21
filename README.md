# deta-hello
Simple Hello world API using FastAPI hosted on [deta](https://deta.sh)

There are 5 endpoints


1.  `/` or root - shows this as an html page


2. `/hello` returns `hello world` as a json object


3. `/items` returns an array of json objects which are items


4. `item/?item_id=P004` returs a an array of items matching `item_id`


5. `/env` returns the environment variables set in `deta.json` as a json object


To deploy it to a [deta micro](https://deta.sh) push 
[![Deploy](https://button.deta.dev/1/svg)](https://go.deta.dev/deploy?repo=https://github.com/ugmurthy/deta-hello)
