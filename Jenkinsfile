pipeline {
    agent any
    environment {
        DOCKER_HUB_USER = 'irum90'
        DOCKER_HUB_PASS = credentials('dockerhub_creds') // add in Jenkins
    }
    stages {
        stage('Code Linting') {
            steps {
                echo 'Linting code...'
                sh 'flake8 .'
            }
        }
        stage('Code Build') {
            steps {
                echo 'Building Docker image for web app...'
                sh 'docker build -t irum90/webapp:latest .'
            }
        }
        stage('Unit Testing') {
            steps {
                echo 'Running unit tests...'
                sh 'pytest tests/'
            }
        }
        stage('Containerized Deployment') {
            steps {
                echo 'Running container using docker-compose...'
                sh 'docker-compose down --remove-orphans'
                sh 'docker-compose up -d --build'
            }
        }
        stage('Selenium Testing') {
            steps {
                echo 'Running Selenium tests...'
                sh 'docker build -t selenium-tests -f Dockerfile.selenium .'
                sh 'docker run --network="host" selenium-tests'
            }
        }
    }
}
