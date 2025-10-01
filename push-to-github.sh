#!/bin/bash

echo "======================================"
echo "Pushing TSZ Portal to GitHub"
echo "User: StartupZoneFZE"
echo "======================================"
echo ""

# Add remote origin
echo "📝 Connecting to GitHub repository..."
git remote add origin https://github.com/StartupZoneFZE/tsz-portal.git

# Check if remote was added
if [ $? -ne 0 ]; then
    echo "Remote already exists, updating..."
    git remote set-url origin https://github.com/StartupZoneFZE/tsz-portal.git
fi

# Set branch to main
echo "🔄 Setting main branch..."
git branch -M main

# Push to GitHub
echo ""
echo "📤 Pushing code to GitHub..."
echo ""
echo "⚠️  IMPORTANT: When prompted for password, use a Personal Access Token!"
echo "   To create one: https://github.com/settings/tokens"
echo ""
echo "Username: StartupZoneFZE"
echo ""

git push -u origin main

if [ $? -eq 0 ]; then
    echo ""
    echo "✅ SUCCESS! Code pushed to GitHub!"
    echo ""
    echo "📎 Repository URL: https://github.com/StartupZoneFZE/tsz-portal"
    echo ""
    echo "Next steps:"
    echo "1. Check your repository at the URL above"
    echo "2. Continue with Supabase setup"
else
    echo ""
    echo "❌ Push failed. Please ensure:"
    echo "1. Repository 'tsz-portal' exists at github.com/StartupZoneFZE"
    echo "2. You're using a Personal Access Token (not your password)"
    echo ""
fi