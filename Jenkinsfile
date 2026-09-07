pipeline {
    agent any

    stages {

        stage('Install Dependencies') {
            steps {
                bat 'python -m venv venv'
                bat 'venv\\Scripts\\python.exe -m pip install --upgrade pip'
                bat 'venv\\Scripts\\python.exe -m pip install psutil'
            }
        }

        stage('Run Server Monitoring') {
            steps {
                bat 'venv\\Scripts\\python.exe monitor.py'
            }
        }
    }
}