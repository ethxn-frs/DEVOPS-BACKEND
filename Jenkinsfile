pipeline {
    agent any

    environment {
        DB_HOST = 'db'
        DB_PORT = '5432'
        DB_NAME = 'articles_db'
        DB_USER = 'articles_user'
        DB_PASSWORD = 'articles_password'
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-id')
        GITHUB_CREDENTIALS = credentials('github-token')
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/ethxn-frs/DEVOPS-BACKEND',
                    credentialsId: 'github-token'
            }
        }

        stage('Install Pip') {
            steps {
                sh 'pip install '
            }
        }

        stage('Check Environment') {
            steps {
                sh '''
                python3 --version
                which python3
                python3 -m pip --version || echo "pip not installed"
                docker info || echo "Docker Daemon not accessible"
                docker --version
                docker compose version || echo "Docker Compose not found"
                '''
            }
        }

        stage('Setup Environment') {
            steps {
                sh '''
                python3 -m ensurepip --upgrade || true
                python3 -m pip install --upgrade pip setuptools wheel
                python3 -m pip install -r requirements/dev.txt
                '''
            }
        }

        stage('Run Database') {
            steps {
                sh '''
                docker compose up -d
                '''
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
