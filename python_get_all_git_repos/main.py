# winget install --id GitHub.cli
# gh auth login

# with git bash
# gh repo list yjg30737 --limit 1000 | while read -r repo _; do
#   gh repo clone "$repo" "$repo"
# done

import subprocess
import sys

user_id = sys.argv[1]

p = subprocess.check_output(["C:\Program Files\Git\git-bash.exe", '-c',
f'''
gh repo list {user_id} --limit 1000 | while read -r repo _; do
    gh repo clone "$repo" "$repo"
done
'''
])