pipeline {
    agent any

    stages {
        stage('Run Python Files') {
            steps {
                bat '''
                for %%f in (String\\*.py) do (
                    echo Running %%f
                    python "%%f"
                )
                '''
            }
        }
    }
}