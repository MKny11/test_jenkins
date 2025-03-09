pipeline {
    agent any

    tools {
        'jenkins.plugins.shiningpanda.tools.PythonInstallation' 'Python3' // Déclaré dans ShiningPanda
    }

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
                script {
                    dir('main') {
                        sh 'pip install -r requirements.txt'
                    }
                }
            }
        }

        stage('Lancer les tests Selenium') {
            steps {
                script {
                    dir('main') {
                        sh 'python test.py'
                    }
                }
            }
        }

        stage('Lancer le scan ZAP') {
            steps {
                script {
                    dir('main') {
                        sh './$ZAP_PATH -daemon -port 8081' // Exécute le script ZAP
                        sh 'python test_zap.py'
                    }
                }
            }
        }

        stage('Analyser les résultats') {
            steps {
                script {
                    dir('main') {
                        sh 'cat zap_report.xml'
                    }
                }
            }
        }
    }

    post {
        always {
            script {
                dir('main') {
                    archiveArtifacts artifacts: '**/*.xml', fingerprint: true
                }
            }
        }
    }
}
