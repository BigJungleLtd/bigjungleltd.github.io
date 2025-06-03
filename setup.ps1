# PowerShell setup script for BigJungle.net Jekyll site

Write-Host "=== BigJungle.net Jekyll Site Setup ===" -ForegroundColor Green
Write-Host ""

# Check if Ruby is in PATH, if not try to find and add it
try {
    $rubyVersion = ruby --version
    Write-Host "✅ Ruby found: $rubyVersion" -ForegroundColor Green
} catch {
    Write-Host "⚠️ Ruby not found in PATH, searching for installation..." -ForegroundColor Yellow
    
    # Common Ruby installation paths
    $RubyPaths = @(
        "C:\Ruby34-x64\bin",
        "C:\Ruby33-x64\bin", 
        "C:\Ruby32-x64\bin",
        "C:\Ruby31-x64\bin",
        "C:\Ruby30-x64\bin"
    )
    
    $RubyFound = $false
    foreach ($RubyPath in $RubyPaths) {
        if (Test-Path $RubyPath) {
            Write-Host "📍 Found Ruby at: $RubyPath" -ForegroundColor Yellow
            $env:PATH += ";$RubyPath"
            try {
                $rubyVersion = ruby --version
                Write-Host "✅ Ruby now working: $rubyVersion" -ForegroundColor Green
                $RubyFound = $true
                break
            } catch {
                continue
            }
        }
    }
    
    if (-not $RubyFound) {
        Write-Host "❌ Ruby is not installed or not found." -ForegroundColor Red
        Write-Host "Please install Ruby first:"
        Write-Host "  - Download from https://rubyinstaller.org/"
        Write-Host "  - Make sure to check 'Add Ruby executables to your PATH'"
        Write-Host ""
        exit 1
    }
}

# Check if Bundler is installed
try {
    $bundlerVersion = bundle --version
    Write-Host "✅ Bundler found: $bundlerVersion" -ForegroundColor Green
} catch {
    Write-Host "📦 Installing Bundler..." -ForegroundColor Yellow
    gem install bundler
}

# Install dependencies
Write-Host "📦 Installing Jekyll and dependencies..." -ForegroundColor Yellow
bundle install

# Build the site
Write-Host "🔨 Building the site..." -ForegroundColor Yellow
bundle exec jekyll build

Write-Host ""
Write-Host "=== Setup Complete! ===" -ForegroundColor Green
Write-Host ""
Write-Host "To run the site locally:" -ForegroundColor Cyan
Write-Host "  bundle exec jekyll serve" -ForegroundColor White
Write-Host ""
Write-Host "Then open: http://localhost:4000" -ForegroundColor Cyan
Write-Host ""
Write-Host "To deploy to GitHub Pages:" -ForegroundColor Cyan
Write-Host "1. Create a new repository on GitHub" -ForegroundColor White
Write-Host "2. Push this code to the main branch" -ForegroundColor White
Write-Host "3. Enable GitHub Pages in repository settings" -ForegroundColor White
Write-Host "4. Set source to 'GitHub Actions'" -ForegroundColor White
Write-Host ""
Write-Host "The site will be automatically built and deployed!" -ForegroundColor Green
