pipeline {
    agent any

    stages {
        stage('Cloner le repo') {
            steps {
                git 'https://github.com/MKny11/test_jenkins.git'
            }
        }

        stage('Lancer les tests Selenium') {
            steps {
                sh 'python test.py'  // Lancer tes tests sans installer des dépendances
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
