pipeline {
    agent any

    environment {
        ZAP_PATH = "main/test_jenkins/test1/zap.sh" 
    }

    stages {
        stage('Cloner le repo') {
            steps {
                git 'https://github.com/MKny11/jenkins_test.git'
            }
        }

        stage('Installer les dépendances') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Lancer les tests Selenium') {
            steps {
                sh 'python test1/test.py'
            }
        }

        stage('Lancer le scan ZAP') {
            steps {
                sh '$ZAP_PATH -daemon -port 8081'
                sh 'python test1/test_zap.py'
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
