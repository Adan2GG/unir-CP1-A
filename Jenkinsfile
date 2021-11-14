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
            }
        }
        
        stage('Tests') {
            parallel {
                stage('Unit') {
                    steps {
                        bat '''
                            set PYTHONPATH=C:\\ProgramData\\Jenkins\\.jenkins\\workspace\\Python
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
                            set PYTHONPATH=C:\\ProgramData\\Jenkins\\.jenkins\\workspace\\Python
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
