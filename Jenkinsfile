pipeline {
    agent any

    tools {
        'jenkins.plugins.shiningpanda.tools.PythonInstallation' 'Python3'
    }

    environment {
        ZAP_PATH = "zap.sh"
        PATH = "K:\\python3\\Scripts;K:\\python3;${env.PATH}"
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
                        sh 'K:\\python3\\Scripts\\pip install -r requirement.txt'
                    }
                }
            }
        }

        stage('Lancer les tests Selenium') {
            steps {
                script {
                    dir('main') {
                        sh 'K:\\python3\\python test.py'
                    }
                }
            }
        }

        stage('Lancer le scan ZAP') {
            steps {
                script {
                    dir('main') {
                        sh './$ZAP_PATH -daemon -port 8081'
                        sh 'K:\\python3\\python test_zap.py'
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
