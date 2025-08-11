pipeline {
    agent any

    environment {
        VENV = ".venv"        // virtual environment folder
        RESULTS = "results"   // folder to store reports
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python') {
            steps {
                bat "python -m venv %VENV%"
                bat "call %VENV%\\Scripts\\activate.bat && python -m pip install --upgrade pip"
                bat "call %VENV%\\Scripts\\activate.bat && pip install -r requirements.txt"
            }
        }

        stage('Run Tests') {
            steps {
                bat "if not exist %RESULTS% mkdir %RESULTS%"
                bat "call %VENV%\\Scripts\\activate.bat && pytest tests --disable-warnings --html=%RESULTS%\\report.html --junitxml=%RESULTS%\\junit.xml"
            }
        }
    }

    post {
        always {
            junit 'results/junit.xml'
            archiveArtifacts artifacts: 'results/**', fingerprint: true
        }
    }
}
