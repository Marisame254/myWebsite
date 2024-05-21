import os
import reflex as rx

railway_domain = "mywebsite-production-eed2.up.railway.app"

config = rx.Config(
    app_name="myWebsite",
    telemetry_enabled=False,
    frontend_port=3000, # default frontend port
    backend_port=8000, # default backend port
    # use https and the railway public domain with a backend route if available, otherwise default to a local address
    api_url=f'https://{os.environ[railway_domain]}/backend' if railway_domain in os.environ else "http://127.0.0.1:8000"
)