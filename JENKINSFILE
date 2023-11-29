pipeline {
    agent any

     stages {
        stage('Get Code') {
            steps {
                // Obtener código del repo
                git 'https://github.com/anieto-unir/helloworld.git'
            }
        }
    
        stage('Build') {
           steps {
              echo 'Eyyy, esto es Python. No hay que compilar nada!!!'
	          echo WORKSPACE
              bat 'dir'
           }
        }
        
        stage('Unit') {
            steps {
                catchError(buildResult: 'UNSTABLE', stageResult: 'FAILURE') {
                    bat '''
                        set PYTHONPATH=%WORKSPACE%
                        pytest --junitxml=result-unit.xml test\\unit
                    '''
               }
            }
        }   


        stage('Rest') {
            steps {
                bat '''
                    set FLASK_APP=app\\api.py
                    set FLASK_ENV=development
                    start flask run
                    start java -jar C:\\Unir\\Ejercicios\\wiremock\\wiremock-jre8-standalone-2.28.0.jar --port 9090 --root-dir C:\\Unir\\Ejercicios\\wiremock
                    set PYTHONPATH=%WORKSPACE%
                    pytest --junitxml=result-rest.xml test\\rest
                '''
            }    
        }

        stage('Results') {
            steps {
                junit 'result*.xml' 
            }
        }
     
    }
}
