#!/bin/bash
# Setup script for BigJungle.net Jekyll site

echo "=== BigJungle.net Jekyll Site Setup ==="
echo ""

# Check if Ruby is installed
if ! command -v ruby &> /dev/null; then
    echo "❌ Ruby is not installed."
    echo "Please install Ruby first:"
    echo "  - Windows: Download from https://rubyinstaller.org/"
    echo "  - macOS: brew install ruby"
    echo "  - Ubuntu: sudo apt-get install ruby-full"
    echo ""
    exit 1
fi

echo "✅ Ruby found: $(ruby --version)"

# Check for Ruby development headers
if ! dpkg -l | grep -q ruby-dev; then
    echo "📦 Installing Ruby development headers..."
    sudo apt-get update
    sudo apt-get install -y ruby-dev build-essential
else
    echo "✅ Ruby development headers found"
fi

# Check if Bundler is installed
if ! command -v bundle &> /dev/null; then
    echo "📦 Installing Bundler..."
    gem install bundler
else
    echo "✅ Bundler found: $(bundle --version)"
fi

# Install dependencies
echo "📦 Installing Jekyll and dependencies..."
bundle config set --local path 'vendor/bundle'
bundle install

# Build the site
echo "🔨 Building the site..."
bundle exec jekyll build

echo ""
echo "=== Setup Complete! ==="
echo ""
echo "To run the site locally:"
echo "  bundle exec jekyll serve"
echo ""
echo "Then open: http://localhost:4000"
echo ""
echo "To deploy to GitHub Pages:"
echo "1. Create a new repository on GitHub"
echo "2. Push this code to the main branch"
echo "3. Enable GitHub Pages in repository settings"
echo "4. Set source to 'GitHub Actions'"
echo ""
echo "The site will be automatically built and deployed!"
