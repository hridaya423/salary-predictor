import mindsdb_sdk

# Connect to MindsDB server running on localhost
server = mindsdb_sdk.connect('http://127.0.0.1:47334')

project = server.get_project()
