# Jenkins AI Pipeline Tester

A demonstration project for testing Jenkins CI/CD pipelines with AI-powered content generation. This project showcases automated builds, testing, artifact generation, and deployment workflows using Jenkins and OpenAI integration.

## Overview

This project implements a complete Jenkins pipeline that:
- Sets up a Python environment
- Runs automated tests
- Generates AI-powered "tip of the day" content using OpenAI's GPT API
- Archives generated artifacts
- Optionally commits results back to the repository

## Project Structure

```
jenkins-ai-tester/
├── Jenkinsfile              # Jenkins pipeline configuration
├── README.md               # This file
├── requirements.txt        # Python dependencies
├── app/
│   ├── __init__.py
│   └── generate_tip.py     # Main application - generates AI tips
├── artifacts/              # Generated content artifacts
│   ├── tip_of_day.txt     # Latest generated tip
│   └── tip_*.txt          # Timestamped tip files
├── scripts/
│   ├── setup_env.sh       # Environment setup script
│   └── commit_tip.sh      # Git commit automation
└── tests/
    └── test_generate_tip.py # Unit tests
```

## Pipeline Stages

The Jenkins pipeline includes the following stages:

1. **Checkout**: Retrieves the latest code from the repository
2. **Setup**: Creates Python virtual environment and installs dependencies
3. **Lint / Test**: Runs pytest for code validation
4. **Generate Tip**: Uses OpenAI API to generate AI engineering tips
5. **Archive Artifacts**: Stores generated content as build artifacts
6. **Commit Artifact Back** (optional): Automatically commits generated content to repository

## Prerequisites

### Jenkins Setup
- Jenkins server with pipeline support
- Required plugins:
  - Pipeline plugin
  - Git plugin
  - Credentials plugin
  - JUnit plugin

### Credentials Configuration
Configure the following credentials in Jenkins:
- `OPENAI_API_KEY`: Your OpenAI API key (stored as secret text)
- `GIT_DEPLOY_KEY`: SSH key or username/password for git operations (if using auto-commit)

### Environment Requirements
- Python 3.7+
- Git
- Virtual environment support

## Local Development

### Setup
1. Clone the repository
2. Create a `.env` file with your OpenAI API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```
3. Install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

### Running the Application
```bash
# Activate virtual environment
source venv/bin/activate

# Generate a tip
python -m app.generate_tip

# Run tests
pytest
```

### Manual Setup Script
```bash
# Run the setup script used by Jenkins
bash scripts/setup_env.sh
```

## Configuration

### Jenkins Environment Variables
- `OPENAI_API_KEY`: Automatically injected from Jenkins credentials
- `GIT_CREDENTIALS`: Jenkins credential ID for git operations

### Customization
- Modify the tip generation prompt in `app/generate_tip.py`
- Adjust OpenAI model and parameters as needed
- Configure auto-commit behavior in the Jenkinsfile
- Update notification email addresses in the pipeline

## Generated Artifacts

The pipeline generates:
- `tip_of_day.txt`: Latest generated tip (overwritten each run)
- `tip_YYYYMMDDTHHMMSSZ.txt`: Timestamped tip files
- Test results (JUnit XML format)

## Pipeline Features

### Error Handling
- Email notifications on build failures
- Graceful handling of missing API keys
- Test result archiving even on failures

### Flexibility
- Conditional auto-commit stage (disabled by default)
- Configurable artifact retention
- Environment-specific credential management

## Testing

The project includes unit tests for the tip generation functionality:
```bash
pytest tests/test_generate_tip.py
```

## Monitoring and Notifications

- Build status notifications via email
- Artifact fingerprinting for change tracking
- JUnit test result integration

## Security Considerations

- API keys stored securely in Jenkins credentials
- SSH keys properly configured for git operations
- No sensitive data committed to repository

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests locally
5. Submit a pull request

## License

This project is intended for educational and demonstration purposes.
