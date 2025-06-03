# BigJungle.net

This is the Jekyll-powered website for BigJungle Ltd, converted from a WordPress/Squarespace export and designed to be hosted on GitHub Pages.

## About

BigJungle Ltd focuses on IoT, smart home technology, and open-source hardware projects. This site contains blog posts covering:

- Arduino and embedded systems projects
- Smart home automation
- Energy monitoring with EmonCMS
- OpenTRV thermostatic radiator valves
- Node-RED for IoT data processing
- Open-source hardware reviews and tutorials

## Local Development

To run this site locally:

1. **Install Ruby and Bundler** (if not already installed)
   ```bash
   # On Windows, download from https://rubyinstaller.org/
   # On macOS: brew install ruby
   # On Ubuntu: sudo apt-get install ruby-full
   ```

2. **Install dependencies**
   ```bash
   bundle install
   ```

3. **Run the site locally**
   ```bash
   bundle exec jekyll serve
   ```

4. **View the site**
   Open [http://localhost:4000](http://localhost:4000) in your browser

## Deployment

This site is configured to automatically deploy to GitHub Pages using GitHub Actions. Simply push to the main branch and the site will be built and deployed automatically.

### Manual Deployment Steps

If you need to deploy manually:

1. **Enable GitHub Pages** in your repository settings
2. **Set source** to "GitHub Actions" 
3. **Push to main branch** to trigger the build

## Site Structure

```
├── _config.yml          # Jekyll configuration
├── _posts/              # Blog posts in Markdown
├── _layouts/            # Page layouts
├── _includes/           # Reusable components
├── index.md             # Homepage
├── blog.md              # Blog index page
├── about.md             # About page
└── .github/workflows/   # GitHub Actions for deployment
```

## Content Migration

The blog posts were migrated from a WordPress export XML file. The original conversion script (`convert_posts.py`) can be used to process additional posts if needed.

### Adding New Posts

To add a new blog post:

1. Create a new file in `_posts/` with the format: `YYYY-MM-DD-title.md`
2. Add front matter:
   ```yaml
   ---
   layout: post
   title: "Your Post Title"
   date: YYYY-MM-DD HH:MM:SS +0000
   author: "Author Name"
   categories: ["Category1", "Category2"]
   tags: ["tag1", "tag2"]
   ---
   ```
3. Write your content in Markdown below the front matter

## Features

- **Responsive Design**: Mobile-friendly layout
- **SEO Optimized**: Meta tags and structured data
- **Fast Loading**: Static site with optimized assets
- **RSS Feed**: Automatic RSS feed generation
- **Category/Tag Support**: Organized content with categories and tags
- **YouTube Embeds**: Custom include for embedding YouTube videos
- **Code Highlighting**: Syntax highlighting for code blocks

## Technologies Used

- **Jekyll**: Static site generator
- **GitHub Pages**: Hosting platform
- **GitHub Actions**: Continuous deployment
- **Liquid**: Templating language
- **Markdown**: Content format
- **HTML2Text**: Content conversion (Python script)

## Contact

- **Email**: jeremy@bigjungle.net
- **Website**: [https://bigjungle.net](https://bigjungle.net)

## License

Content is copyright BigJungle Ltd. The Jekyll theme and site structure are open source.
