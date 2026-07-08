pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Python Version') {
            steps {
                bat 'python --version'
            }
        }

        stage('Git Version') {
            steps {
                bat 'git --version'
            }
        }

        stage('Pytest Version') {
            steps {
                bat 'pytest --version'
            }
        }

    }
}