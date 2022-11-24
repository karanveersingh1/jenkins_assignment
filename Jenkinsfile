pipeline { 
    agent any
    stages {
        stage('Clone Git') {
            steps {
                git 'https://github.com/satvik-vm/se_ass6.git'
            }
        }
        stage('Build Code') {
            steps {
                sh "chmod u+x prog.py"
                sh "./program.py"
            }
        }
     stage('Test Code') {
            steps {
                sh "chmod u+x test.py"
                sh "./test.py"
            }
        }
    } 
}
