pipeline {
    agent any

     stages {
        stage('Get Code') {
            steps {
                // Obtener código del repo
                //git 'https://github.com/ivngmz/helloworld.git'
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
                    		echo "Realizando pruebas unitarias"
                		sh 'apt-get update && apt-get install -y python3-pip && rm -rf /var/lib/apt/lists/*; pip install pytest'
                		sh 'export  PYTHONPATH=$WORKSPACE; py.test --junitxml=result-unit.xml test/unit'
                		//procesaría todos los ficheros de la ruta
                		junit 'result*.xml'
		    }
                }
                stage('Service') {
                    steps {
                    		echo "Realizando la prueba de microservicio"
                		sh 'export FLASK_APP=app/api.py && export FLASK_ENV=development && nohup flask run > log.txt 2>&1 &'
                		sh 'nohup java -jar /var/jenkins_home/javajars/wiremock-jre8-standalone-2.32.0.jar --port 9090 -v --root-dir /var/jenkins_home/mappings  > log.txt 2>&1 &'
                		sh 'export  PYTHONPATH=$WORKSPACE; py.test --junitxml=result-unit.xml test/unit'
                		junit 'result*.xml'
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
