// Jenkinsfile
pipeline {
  agent any

  environment {
    # Name matches the Jenkins credential id for an SSH key or usernamePassword
    GIT_CREDENTIALS = 'GIT_DEPLOY_KEY'     // replace with real Jenkins credentials id
    OPENAI_API_KEY = credentials('2454168b-51b4-4d86-b779-c4cde1d9c35d') // store your key in Jenkins credentials
  }

  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }

    stage('Setup') {
      steps {
        sh 'bash scripts/setup_env.sh'
      }
    }

    stage('Lint / Test') {
      steps {
        sh '. venv/bin/activate && pytest -q'
      }
    }

    stage('Generate Tip') {
      steps {
        withEnv(["OPENAI_API_KEY=${env.OPENAI_API_KEY}"]) {
          sh '. venv/bin/activate && python -m app.generate_tip'
        }
      }
      post {
        success {
          echo 'Generation succeeded'
        }
      }
    }

    stage('Archive Artifacts') {
      steps {
        archiveArtifacts artifacts: 'artifacts/*.txt', fingerprint: true
      }
    }

    stage('Commit Artifact Back (optional)') {
      when {
        expression { return true } // set to true if you want to enable auto-commit
      }
      steps {
        // Example for SSH deploy key approach: the agent must have git configured to use that key.
        sh 'bash scripts/commit_tip.sh artifacts/tip_of_day.txt "CI: add tip of day"'
      }
    }
  }

  post {
    always {
      junit allowEmptyResults: true, testResults: '**/test-*.xml'
    }
    failure {
      mail to: 'taskscriptor@gmail.com',
           subject: "Jenkins: Build failed: ${currentBuild.fullDisplayName}",
           body: "Job ${env.JOB_NAME} build ${env.BUILD_NUMBER} failed."
    }
  }
}
