pipeline {
    agent any

    stages {
        stage('Run Python Files') {
            steps {
                bat '''
                for /R %%f in (*.py) do (
                    echo Running %%f
                    python "%%f"
                )
                '''
            }
        }
    }

    post {
        success {
            mail(
                to: 'artigusain201@gmail.com',
                subject: "✅ SUCCESS: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                body: """
Hello,

Your Jenkins build completed successfully.

Job Name : ${env.JOB_NAME}
Branch   : ${env.BRANCH_NAME}
Build No : ${env.BUILD_NUMBER}
Status   : SUCCESS

Regards,
Jenkins
"""
            )
        }

        failure {
            mail(
                to: 'artigusain201@gmail.com',
                subject: "❌ FAILED: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                body: """
Hello,

Your Jenkins build has failed.

Job Name : ${env.JOB_NAME}
Branch   : ${env.BRANCH_NAME}
Build No : ${env.BUILD_NUMBER}
Status   : FAILED

Please check the Jenkins Console Output for the error.

Regards,
Jenkins
"""
            )
        }
    }
}