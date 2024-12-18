pipeline {
    agent any

    environment {
        DB_HOST = 'db'
        DB_PORT = '5432'
        DB_NAME = 'articles_db'
        DB_USER = 'articles_user'
        DB_PASSWORD = 'articles_password'
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-id')
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/ethxn-frs/DEVOPS-BACKEND', credentialsId: 'github-token'
            }
        }

        stage('Check Python Version') {
            steps {
                sh '''
                python3 --version
                pip --version
                '''
            }
        }

        stage('Setup Environment') {
            steps {
                echo 'Setting up Python virtual environment...'
                sh '''
                python3 -m venv venv
                source venv/bin/activate
                pip install -r requirements/dev.txt
                '''
            }
        }

        stage('Run Database') {
            steps {
                echo 'Starting database using Docker Compose...'
                sh 'docker compose up -d'
            }
        }

        stage('Run Migrations and Load Data') {
            steps {
                echo 'Running migrations and loading data...'
                sh '''
                source venv/bin/activate
                python manage.py migrate
                python manage.py loaddata --format json ./fixtures/dev-fixtures.json
                '''
            }
        }

        stage('Run Unit Tests') {
            steps {
                echo 'Running unit tests...'
                sh '''
                source venv/bin/activate
                python manage.py test
                '''
            }
        }

        stage('Linting') {
            steps {
                echo 'Checking code quality...'
                sh '''
                source venv/bin/activate
                ruff check
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Building and pushing Docker image...'
                sh '''
                docker build -t ethxn/backend:latest .
                docker login -u $DOCKERHUB_CREDENTIALS_USR -p $DOCKERHUB_CREDENTIALS_PSW
                docker push ethxn/backend:latest
                '''
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying application...'
                sh 'docker compose up -d'
            }
        }
    }

    post {
        always {
            echo 'Cleaning up resources...'
            sh 'docker compose down || true'
        }
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
