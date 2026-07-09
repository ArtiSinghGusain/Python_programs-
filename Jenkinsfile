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
}