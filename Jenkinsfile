// pipeline {
//     agent any
//
//     environment {
//         VENV = ".venv"        // virtual environment folder
//         RESULTS = "results"   // folder to store reports
//     }
//
//     stages {
//         stage('Checkout') {
//             steps {
//                 checkout scm
//             }
//         }
//
//         stage('Setup Python') {
//             steps {
//                 bat "python -m venv %VENV%"
//                 bat "call %VENV%\\Scripts\\activate.bat && python -m pip install --upgrade pip"
//                 bat "call %VENV%\\Scripts\\activate.bat && pip install -r requirements.txt"
//             }
//         }
//
//         stage('Run Tests') {
//             steps {
//                 bat "if not exist %RESULTS% mkdir %RESULTS%"
//                 bat "call %VENV%\\Scripts\\activate.bat && pytest tests/test_login.py --disable-warnings --html=%RESULTS%\\report.html --junitxml=%RESULTS%\\junit.xml"
//
//             }
//         }
//     }
//
//     post {
//         always {
//             junit 'results/junit.xml'
//             archiveArtifacts artifacts: 'results/**', fingerprint: true
//         }
//     }
// }

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
                bat "call %VENV%\\Scripts\\activate.bat && pytest tests/test_login.py --disable-warnings --html=%RESULTS%\\report.html --junitxml=%RESULTS%\\junit.xml"
            }
        }
    }

    post {
        always {
            junit 'results/junit.xml'
            archiveArtifacts artifacts: 'results/**', fingerprint: true
        }

        success {
            emailext(
                subject: "SUCCESS: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                body: """<p>Build succeeded for <b>${env.JOB_NAME}</b> #${env.BUILD_NUMBER}.</p>
                         <p><a href='${env.BUILD_URL}'>Click here</a> to view build details.</p>""",
                mimeType: 'text/html',
                to: 'tarikaziz7489@gmail.com',
                attachmentsPattern: 'results/report.html'
            )
        }

        failure {
            emailext(
                subject: "FAILURE: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                body: """<p>Build failed for <b>${env.JOB_NAME}</b> #${env.BUILD_NUMBER}.</p>
                         <p><a href='${env.BUILD_URL}'>Click here</a> to view build logs and reports.</p>""",
                mimeType: 'text/html',
                to: 'tarikaziz7489@gmail.com',
                attachmentsPattern: 'results/report.html',
                attachLog: true
            )
        }
    }
}
