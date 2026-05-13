module.exports = {
    apps: [
        {
            name: "appwrite-frontend",
            cwd: "C:/Users/PAUL/Desktop/angular_project/APPWRITE_FRONTEND",
            script: "run.py",
            interpreter: "C:/Users/PAUL/Desktop/angular_project/APPWRITE_FRONTEND/env/Scripts/python.exe",
            watch: false,
            autorestart: true,
            env: {
                FLASK_ENV: "development",
                FLASK_DEBUG: "1"
            }
        }
    ]
}