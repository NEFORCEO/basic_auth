
import uvicorn
from client.config.config import Config as c

class StartApp:
    def run(self):
        return uvicorn.run(
            app=c.app_name,
            host=c.app_host,
            port=c.app_port,
            reload=c.app_reload
        )
        
main = StartApp()