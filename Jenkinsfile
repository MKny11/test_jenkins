pipeline {
    agent any

    environment {
        ZAP_PATH = "zap.sh"
    }

    stages {
        stage('Cloner le repo') {
            steps {
                git branch: 'main', url: 'https://github.com/MKny11/test_jenkins.git'
            }
        }

        stage('Installer les dépendances') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Lancer les tests Selenium') {
            steps {
                sh 'python test.py'
            }
        }

        stage('Lancer le scan ZAP') {
            steps {
                sh '$ZAP_PATH -daemon -port 8081'
                sh 'python test_zap.py'
            }
        }

        stage('Analyser les résultats') {
            steps {
                sh 'cat zap_report.xml'
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: '**/*.xml', fingerprint: true
        }
    }
}
