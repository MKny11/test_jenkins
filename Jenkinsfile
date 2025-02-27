pipeline {
    agent any

    environment {
        ZAP_PATH = "test1/zap.sh"  // Chemin relatif vers le fichier zap.sh dans le sous-répertoire test1
    }

    stages {
        stage('Cloner le repo') {
            steps {
                git 'https://github.com/MKny11/test_jenkins.git'
            }
        }

        stage('Installer les dépendances') {
            steps {
                sh 'pip install -r test1/requirement.txt'  // Utilise le bon chemin vers requirements.txt
            }
        }

        stage('Lancer les tests Selenium') {
            steps {
                sh 'python test1/test.py'  // Le chemin vers ton script Selenium dans test1
            }
        }

        stage('Lancer le scan ZAP') {
            steps {
                sh '$ZAP_PATH -daemon -port 8081'  // Lancer ZAP à partir du sous-répertoire test1
                sh 'python test1/test_zap.py'  // Script Python pour le scan ZAP
            }
        }

        stage('Analyser les résultats') {
            steps {
                sh 'cat test1/zap_report.xml'  // Afficher le rapport généré dans test1
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'test1/**/*.xml', fingerprint: true  // Archiver les fichiers .xml du sous-répertoire test1
        }
    }
}
