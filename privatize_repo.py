import os
import subprocess
access_token = os.environ.get('ACCESS_TOKEN')

subprocess.run(['git', 'config', '--global', 'user.name', 'Tanmay Somani'])
subprocess.run(['git', 'config', '--global', 'user.email', 'tanmaysomani2003@gmail.com'])
subprocess.run(['git', 'remote', 'add', 'origin', 'https://github.com/Tanmay-Somani/git-init.git'])

if not os.path.exists('.git'):
    subprocess.run(['git', 'init'])
if subprocess.run(['git', 'remote', 'get-url', 'origin'], capture_output=True).returncode != 0:
    subprocess.run(['git', 'remote', 'add', 'origin', 'https://github.com/Tanmay-Somani/git-init.git'])
subprocess.run(['git', 'fetch'])

subprocess.run(['git', 'checkout', 'main'])
subprocess.run(['git', 'reset', '--hard', 'origin/main'])
subprocess.run(['git', 'checkout', '--orphan', 'main'])
subprocess.run(['git', 'commit', '--allow-empty', '-m', 'Privatize repository'])
subprocess.run(['git', 'push', '--force', 'origin', 'main'])
