pipeline {
    agent any
       options {
        parallelsAlwaysFailFast()
        }
     stages {
        stage('Get Code') {
            agent any
            steps {
                git branch:"feature_fix_racecond", url:'https://github.com/Adan2GG/unir-CP1-A.git'
            }
        }
        stage('Tests') {
            parallel {
                 stage('Unit') {
                    agent { label 'linux'}
                    steps {
                        stash includes: 'test/unit/*', name: 'Test-Unit'
                         catchError(buildResult:'UNSTABLE',stageResult:'FAILURE') {
                             bat ''' 
                                set PYTHONPATH=%WORKSPACE%
                                pytest --junitxml=result-unit.xml test\\unit
                            '''
                           }
                        }
                }
                 stage('Rest') {
                    agent { label 'linux'}
                    steps {
                       stash includes: 'test/rest/*', name: 'Test-Rest'
                        
                        catchError(buildResult:'UNSTABLE',stageResult:'FAILURE') {
                            bat '''    
                            set FLASK_APP=app\\api.py
                            start flask run
                            
                            set PYTHONPATH=.
                            start java -jar C:\\Users\\adan.garciagarcia\\Desktop\\CursoDevops\\Herramientas\\wiremock-standalone-3.5.4.jar --port 9090 --verbose --root-dir test\\wiremock
                            pytest --junitxml=result-rest.xml' test\\rest
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
