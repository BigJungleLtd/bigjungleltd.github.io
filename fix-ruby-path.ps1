# Add Ruby to PATH permanently for PowerShell
# Add this to your PowerShell profile to make Ruby available in all sessions

# Check if Ruby directory exists and add to PATH
$RubyPath = "C:\Ruby34-x64\bin"
if (Test-Path $RubyPath) {
    if ($env:PATH -notlike "*$RubyPath*") {
        $env:PATH += ";$RubyPath"
        Write-Host "Ruby added to PATH for this session" -ForegroundColor Green
    }
}

# To make this permanent, run:
# [Environment]::SetEnvironmentVariable("PATH", $env:PATH + ";C:\Ruby34-x64\bin", "User")
# Or add Ruby to your system PATH through Windows Settings
