pipeline { 
    agent any
    stages {
        stage('Clone Git') {
            steps {
                git 'https://github.com/karanveersingh1/jenkins_assignment.git'
            }
        }
        stage('Build Code') {
            steps {
                sh "chmod u+x prog.py"
                sh "python3 prog.py"
            }
        }
     stage('Test Code') {
            steps {
                sh "python3 test.py"
            }
        }
    } 
}
