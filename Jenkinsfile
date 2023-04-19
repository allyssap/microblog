pipeline{
    agent any
    
    environment {
        CONTAINER_NAME = "myapp"
        IMAGE_NAME = "flaskappv2"
        JOB_NAME = "Flask microblog"
        BUILD_URL = "http://3.135.172.163:5000/"
        SELENIUM_URL = "http://3.135.172.163:4444/wd/hub"
        
    }
    
    stages {
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/allyssap/microblog.git']]])
            }
        }
        
        stage('Build') {
            steps {
                echo 'Building..'
                sh 'sudo docker build --tag $IMAGE_NAME .'
            }
        }
        
        stage('Test') {
            steps {
                //echo 'Testing..'
                // Start the Selenium container
                //sh 'sudo docker run -d -p 4444:4444 selenium/standalone-firefox' //:4.0.0-beta-4-20210823
                // Wait for the container to start
                //sh 'sleep 30'
                // Run the Selenium tests
                //sh 'python selenium_tests.py $SELENIUM_URL'
                // Stop the Selenium container
                //sh 'sudo docker stop $(sudo docker ps -q --filter ancestor=selenium/standalone-firefox)' //:4.0.0-beta-4-20210823
            }
        }
        
        stage('Deploy') {
            steps {
                echo 'Deploying..'
                sh 'sudo docker stop $CONTAINER_NAME || true'
                sh 'sudo docker rm $CONTAINER_NAME || true'
                sh 'sudo docker run -d -p 5000:5000 --name $CONTAINER_NAME flaskappv2'
                
            }
            
        }
    }
    post {
        success {
            slackSend message: "System Deploye - ${env.JOB_NAME} ${env.BUILD_NUMBER} ${env.BUILD_URL}"
        }
        failure {
            slackSend message: "System Deployment Failed - ${env.JOB_NAME} ${env.BUILD_NUMBER} ${env.BUILD_URL}"
        }
    }
}
