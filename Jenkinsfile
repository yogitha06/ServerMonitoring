pipeline {
    agent any

    stages {
        stage('Run Server Monitoring') {
            steps {
                bat '"C:\\Program Files\\Python313\\python.exe" monitor.py'
            }
        }
    }
}