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
                git branch: 'main',
                    url: 'https://github.com/ethxn-frs/DEVOPS-BACKEND',
                    credentialsId: 'github-token'
            }
        }

        stage('Check Environment') {
            steps {
                sh '''
                python3 --version
                which python3
                which pip
                docker --version
                docker compose version
                '''
            }
        }

        stage('Setup Environment') {
            steps {
                sh '''
                python3.9 -m ensurepip --upgrade
                python3.9 -m pip install --upgrade pip
                python3.9 -m pip install -r requirements/dev.txt
                '''
            }
        }

        stage('Run Database') {
            steps {
                sh '/usr/local/bin/docker compose up -d'
            }
        }

        stage('Run Migrations and Load Data') {
            steps {
                sh '''
                source venv/bin/activate
                python manage.py migrate
                python manage.py loaddata --format json ./fixtures/dev-fixtures.json
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

        stage('Linting') {
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
                docker build -t ethxn/backend:latest .
                docker login -u $DOCKERHUB_CREDENTIALS_USR -p $DOCKERHUB_CREDENTIALS_PSW
                docker push ethxn/backend:latest
                '''
            }
        }
    }

    post {
        always {
            sh '/usr/local/bin/docker compose down || true'
        }
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
