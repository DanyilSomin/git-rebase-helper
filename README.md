# git-rebase-helper
Run 'git rebase' open all conflicts in vscode and auto-apply commit messages.<br>

Note: standard vs code tools is better.<br>

This script for thouse who likes console as git interface and does not use vscode as main editor.<br>
Works better with alias.

For example setup alias like this: 'python3 /Users/script/myrebase.py' -> 'myrebase' then run<br>
$ myrebase master<br>
$ myrebase --continue<br>
$ ...<br>

0. Calls 'git rebase' for you and passes all additional arguments
1. Disables default editor while running so all messages will be applied automatically
2. Opens all files with conflicts in vscode
3. Prints stdout and stderr to console
