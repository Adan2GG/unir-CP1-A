pipeline {
    agent any

     stages {
        stage('Get Code') {
            steps {
                // Obtener código del repo
                //git 'https://github.com/anieto-unir/helloworld.git'
		script {
			scmVars = checkout scm
			echo 'scm : the commit id is ' + scmVars.GIT_COMMIT
		}
            }
        }
        
        stage('Build') {
            steps {
                echo 'Eyyy, esto es Python. No hay que compilar nada!!!'
		echo 'El workspace contiene el commit \'' + scmVars.GIT_COMMIT + '\' de la rama \'' + scmVars.GIT_BRANCH + '\''
            }
        }
        
        stage('Tests') {
            parallel {
                stage('Unit') {
                    steps {
                        bat '''
                            set PYTHONPATH=%WORKSPACE%
                            pytest --junitxml=result-unit.xml test\\unit
                        '''
                    }
                }
                stage('Service') {
                    steps {
                        bat '''
                            set FLASK_APP=app\\api.py
                            set FLASK_ENV=development
			    start flask run
			    start java -jar C:\\Unir\\Ejercicios\\23a-primavera\\wiremock\\wiremock-jre8-standalone-2.28.0.jar --port 9090 --root-dir C:\\Unir\\Ejercicios\\23a-primavera\\wiremock
			    PING -n 21 127.0.0.1>nul
			    set PYTHONPATH=%WORKSPACE%
			    pytest --junitxml=result-rest.xml test\\rest			    
                        '''
                    }    
                }
            }
        }
        stage ('Results') {
            steps {
                junit 'result*.xml'
            }
        }
    }
}
