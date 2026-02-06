import os
from dotenv import load_dotenv

load_dotenv()

from app import create_app


config_name = os.environ.get('FLASK_CONFIG') or 'development' 

app = create_app(config_name)

if __name__ == '__main__':

    debug_mode = app.config.get('DEBUG' , False)

    if debug_mode:
        print(f"🚀 Starting in DEVELOPMENT mode")
        print(f"🔧 Debug mode: ON")

    else:
        print(f"🚀 Starting in PRODUCTION mode")
        print(f"🔧 Debug mode: OFF")

    print(f"🌐 Server: http://127.0.0.1:5000")


    app.run(debug=debug_mode, host='127.0.0.1', port=5000)