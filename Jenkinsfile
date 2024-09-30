pipeline {
    agent any

    environment {
        VENV = 'venv' // Virtual environment directory
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/jasonkiptoo/test-jenkins.git'
            }
        }

        stage('Setup Python Environment') {
            steps {
                // Create and activate a virtual environment
                sh 'python3 -m venv ${VENV}'
                sh 'source ${VENV}/bin/activate'
                // Install project dependencies
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Unit Tests') {
            steps {
                // Run tests in the virtual environment
                sh 'source ${VENV}/bin/activate && python -m unittest discover tests'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying the Flask application...'
                // Deployment steps can be added here, such as uploading to a server or starting a Flask instance
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Check the logs.'
        }
    }
}
