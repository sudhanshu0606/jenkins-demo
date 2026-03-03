pipeline{
	agent any
	stages{
		stage('greet'){
			steps{
				echo "Hello, World"
			}
		}
		stage('run'){
			steps{
				python main.py
			}
		}
	}
}
