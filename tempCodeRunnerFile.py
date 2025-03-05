@app.get("/")
def server_running():
    return {"Message": "Server is running ✨"}