pipeline {
    agent any

    environment {
        ZAP_PATH = "test1/zap.sh"
    }

    stages {
        stage('Cloner le repo') {
            steps {
                script {
                    dir('test_jenkins') {  // Se placer dans le répertoire test1 avant de cloner
                        git 'https://github.com/MKny11/test_jenkins.git'
                    }
                }
            }
        }

        stage('Installer les dépendances') {
            steps {
                script {
                    dir('test1') {  // Installer les dépendances dans le sous-répertoire test1
                        sh 'pip install -r requirements.txt'
                    }
                }
            }
        }

        stage('Lancer les tests Selenium') {
            steps {
                script {
                    dir('test1') {  // Lancer les tests Selenium dans le sous-répertoire test1
                        sh 'python test.py'
                    }
                }
            }
        }

        stage('Lancer le scan ZAP') {
            steps {
                script {
                    dir('test1') {  // Lancer ZAP dans le sous-répertoire test1
                        sh '$ZAP_PATH -daemon -port 8081'
                        sh 'python test_zap.py'
                    }
                }
            }
        }

        stage('Analyser les résultats') {
            steps {
                script {
                    dir('test1') {  // Analyser les résultats dans le sous-répertoire test1
                        sh 'cat zap_report.xml'
                    }
                }
            }
        }
    }

    post {
        always {
            script {
                dir('test1') {  // Archiver les artefacts dans le sous-répertoire test1
                    archiveArtifacts artifacts: '**/*.xml', fingerprint: true
                }
            }
        }
    }
}
