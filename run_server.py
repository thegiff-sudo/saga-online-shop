import uvicorn
import os
import sys

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    print(f"Starting SAGA ONLINE SHOP server at http://0.0.0.0:{port} (Local: http://localhost:{port}, Network: http://192.168.1.12:{port})")
    uvicorn.run("app.main:app", host="0.0.0.0", port=port, reload=False)
