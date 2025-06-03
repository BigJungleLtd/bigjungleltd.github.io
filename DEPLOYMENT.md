# Deployment Guide

## Quick Start

1. **View the preview**: Open `preview.html` in your browser to see what the site will look like
2. **Install Ruby**: Download from [rubyinstaller.org](https://rubyinstaller.org/) (Windows)
3. **Run setup**: Execute `setup.ps1` (Windows) or `setup.sh` (Mac/Linux)
4. **Test locally**: Run `bundle exec jekyll serve` and visit http://localhost:4000

## GitHub Pages Deployment

### Step 1: Create GitHub Repository

1. Go to [GitHub](https://github.com) and create a new repository
2. Name it something like `bigjungle-net` or `your-username.github.io`
3. Make it public (required for free GitHub Pages)

### Step 2: Push Your Code

```bash
# Initialize git repository
git init

# Add all files
git add .

# Commit files
git commit -m "Initial Jekyll site from WordPress export"

# Add GitHub repository as origin
git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPO-NAME.git

# Push to GitHub
git push -u origin main
```

### Step 3: Enable GitHub Pages

1. Go to your repository on GitHub
2. Click **Settings** tab
3. Scroll down to **Pages** section
4. Under **Source**, select **GitHub Actions**
5. The site will automatically build and deploy

### Step 4: Access Your Site

Your site will be available at:
- `https://YOUR-USERNAME.github.io/YOUR-REPO-NAME/` (if repository is not named username.github.io)
- `https://YOUR-USERNAME.github.io/` (if repository is named username.github.io)

## Custom Domain (Optional)

To use a custom domain like `bigjungle.net`:

1. **Add CNAME file** to repository root:
   ```
   bigjungle.net
   ```

2. **Configure DNS** with your domain provider:
   - Add CNAME record: `www` → `YOUR-USERNAME.github.io`
   - Add A records for apex domain:
     ```
     185.199.108.153
     185.199.109.153
     185.199.110.153
     185.199.111.153
     ```

3. **Update GitHub Pages settings**:
   - Go to repository Settings → Pages
   - Enter your custom domain
   - Enable "Enforce HTTPS"

## Adding More Content

### Converting More Posts

If you want to convert more posts from the WordPress XML:

1. Install Python 3
2. Install html2text: `pip install html2text`
3. Run the conversion script: `python convert_posts.py`

### Manual Post Creation

Create new posts in `_posts/` with this format:

```markdown
---
layout: post
title: "Your Post Title"
date: YYYY-MM-DD HH:MM:SS +0000
author: "Author Name"
categories: ["Category1", "Category2"]
tags: ["tag1", "tag2"]
---

Your content here in Markdown format.
```

## Site Configuration

Edit `_config.yml` to customize:

- Site title and description
- Author information
- Social media links
- Analytics tracking
- SEO settings

## Troubleshooting

### Ruby Installation Issues
- Windows: Use RubyInstaller with DevKit
- Ensure Ruby is added to PATH
- Restart command prompt after installation

### Jekyll Build Errors
- Check `_config.yml` syntax
- Ensure all required gems are installed
- Check for missing front matter in posts

### GitHub Pages Build Failures
- Check the Actions tab for build logs
- Ensure all required files are committed
- Verify Jekyll configuration is valid

## Performance Optimization

- **Images**: Optimize images before uploading
- **Caching**: GitHub Pages includes CDN caching
- **Minification**: Enable in `_config.yml` for production
- **SEO**: Use jekyll-seo-tag plugin (already included)

## Maintenance

- **Updates**: Regularly update gems with `bundle update`
- **Security**: Monitor for security updates
- **Content**: Keep posts and information current
- **Monitoring**: Use Google Analytics or similar

## Support

For issues with:
- **Jekyll**: [Jekyll Documentation](https://jekyllrb.com/docs/)
- **GitHub Pages**: [GitHub Pages Documentation](https://docs.github.com/en/pages)
- **Ruby**: [Ruby Documentation](https://www.ruby-lang.org/en/documentation/)
