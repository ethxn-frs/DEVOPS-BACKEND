pipeline {
    agent any
    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-id')
        DATABASE_URL = 'postgres://user:password@localhost:5432/db_name'
    }
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/ethxn-frs/DEVOPS-BACKEND'
            }
        }
        stage('Setup Environment') {
            steps {
                sh '''
                python -m venv venv
                source venv/bin/activate
                pip install -r requirements/dev.txt
                '''
            }
        }
        stage('Run Unit Tests') {
            steps {
                sh '''
                source venv/bin/activate
                python manage.py test
                '''
            }
        }
        stage('Linting and Formatting') {
            steps {
                sh '''
                source venv/bin/activate
                ruff check
                '''
            }
        }
        stage('Build Docker Image') {
            steps {
                sh '''
                docker build -t ton-utilisateur/backend-image .
                docker login -u $DOCKERHUB_CREDENTIALS_USR -p $DOCKERHUB_CREDENTIALS_PSW
                docker push ton-utilisateur/backend-image
                '''
            }
        }
    }
    post {
        failure {
            echo 'Pipeline failed!'
        }
        success {
            echo 'Pipeline succeeded!'
        }
    }
}
