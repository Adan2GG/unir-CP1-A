pipeline {
    agent any

     stages {

        stage('Get Code') {
           steps {
             git 'https://github.com/Adan2GG/unir-CP1-A.git'
           }
        }
        stage('Tests') {
            parallel {
                 stage('Unit') {
                    steps {
                         catchError(buildResult:'UNSTABLE',stageResult:'FAILURE') {
                             bat '''    
                                set PYTHONPATH=%WORKSPACE%
                                pytest --junitxml=result-unit.xml test\\unit
                            '''
                           }
                        }
                }
                 stage('Rest') {
                   steps {
                     catchError(buildResult:'UNSTABLE',stageResult:'FAILURE') {
                         bat '''    
                            set FLASK_APP=app\\api.py
                            start java -jar C:\\Users\\adan.garciagarcia\\Desktop\\CursoDevops\\Herramientas\\wiremock-standalone-3.5.4.jar --port 9090 --verbose --root-dir test\\wiremock
                            start flask run
                            
                            set PYTHONPATH=.
                            pytest --junitxml=result-rest.xml test\\rest
                        '''
                        }
                    }
                }
            }
        }
       
        stage('Result') {
            steps {
                junit 'result*.xml'
                echo 'Finish!!'
            }
        }
    }
}
