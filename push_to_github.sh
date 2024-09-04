#!/bin/bash

# Define the commit message and branch name
COMMIT_MESSAGE="Automated commit and push"
BRANCH_NAME="main"  # Change this to 'master' if necessary

# Add all changes
git add .

# Commit with an automated message
git commit -m "$COMMIT_MESSAGE"

# Push to the remote repository
git push origin $BRANCH_NAME
