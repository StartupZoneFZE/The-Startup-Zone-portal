#!/bin/bash

# Replace YOUR_USERNAME with your actual GitHub username
GITHUB_USERNAME="YOUR_USERNAME"

echo "Setting up GitHub remote and pushing code..."

# Add remote origin
git remote add origin "https://github.com/${GITHUB_USERNAME}/tsz-portal.git"

# Set main branch
git branch -M main

# Push to GitHub
git push -u origin main

echo "✅ Code pushed to GitHub successfully!"
echo ""
echo "Next steps:"
echo "1. Go to https://github.com/${GITHUB_USERNAME}/tsz-portal/settings/secrets/actions"
echo "2. Add the required secrets (see GITHUB_SETUP.md)"
echo "3. Go to https://vercel.com/new to import your repository"
echo "4. Configure environment variables in Vercel"