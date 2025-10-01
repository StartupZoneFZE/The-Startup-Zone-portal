#!/bin/bash

echo "==================================="
echo "TSZ Portal - GitHub Push Assistant"
echo "==================================="
echo ""

# Check if git is installed
if ! command -v git &> /dev/null; then
    echo "❌ Git is not installed. Please install Git first."
    exit 1
fi

# Check if we're in the right directory
if [ ! -f "package.json" ]; then
    echo "❌ Please run this script from the Portal directory"
    exit 1
fi

# Check if repository already has a remote
if git remote get-url origin &> /dev/null; then
    echo "⚠️  Remote origin already exists:"
    git remote get-url origin
    echo ""
    read -p "Do you want to remove it and add a new one? (y/n): " -n 1 -r
    echo ""
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        git remote remove origin
    else
        echo "Using existing remote..."
    fi
fi

# Get GitHub username
echo ""
read -p "Enter your GitHub username: " username
echo ""

# Confirm repository name
echo "Repository will be: https://github.com/${username}/tsz-portal"
read -p "Is this correct? (y/n): " -n 1 -r
echo ""

if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo "❌ Cancelled"
    exit 1
fi

# Add remote and push
echo ""
echo "📝 Adding GitHub remote..."
git remote add origin "https://github.com/${username}/tsz-portal.git"

echo "🔄 Setting main branch..."
git branch -M main

echo "📤 Pushing to GitHub..."
echo ""
echo "NOTE: You may be asked for your GitHub credentials."
echo "Username: ${username}"
echo "Password: Use a Personal Access Token (not your password!)"
echo ""
echo "To create a token: https://github.com/settings/tokens"
echo ""

git push -u origin main

if [ $? -eq 0 ]; then
    echo ""
    echo "✅ Success! Code pushed to GitHub!"
    echo ""
    echo "Next steps:"
    echo "1. Visit: https://github.com/${username}/tsz-portal"
    echo "2. Verify all files are uploaded"
    echo "3. Continue with Supabase setup"
    echo ""
else
    echo ""
    echo "❌ Push failed. Please check:"
    echo "1. Your GitHub username is correct"
    echo "2. The repository 'tsz-portal' exists"
    echo "3. You're using a Personal Access Token (not password)"
    echo ""
    echo "Create token at: https://github.com/settings/tokens"
fi