import os
import subprocess

# Access environment variable
access_token = os.environ.get('ACCESS_TOKEN')

# Configure Git user information
subprocess.run(['git', 'config', '--global', 'user.name', 'Your Name'])
subprocess.run(['git', 'config', '--global', 'user.email', 'your.email@example.com'])

# Initialize Git repository
subprocess.run(['git', 'init'])
subprocess.run(['git', 'remote', 'add', 'origin', 'https://github.com/your-username/your-repository.git'])
subprocess.run(['git', 'fetch'])

# Privatize the repository
subprocess.run(['git', 'checkout', 'main'])
subprocess.run(['git', 'update-ref', '-d', 'refs/heads/main'])
subprocess.run(['git', 'checkout', '--orphan', 'main'])
subprocess.run(['git', 'commit', '--allow-empty', '-m', 'Privatize repository'])
subprocess.run(['git', 'push', '--force', 'origin', 'main'])
