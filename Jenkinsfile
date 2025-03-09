pipeline {
    agent any

    environment {
        ZAP_PATH = "zap.sh"
        PYTHON_PATH = "C:/Users/Utilisateur/AppData/Local/Microsoft/WindowsApps/python.exe" // Spécifie le chemin où Python est installé
        PATH = "${PYTHON_PATH}/Scripts:${PYTHON_PATH}:${env.PATH}" // Ajoute Python au PATH
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
                        sh '$ZAP_PATH -daemon -port 8081'
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
