#!/usr/bin/env python3
"""
WordPress XML to Jekyll Posts Converter
Converts WordPress export XML to Jekyll markdown posts
"""

import xml.etree.ElementTree as ET
import re
import os
from datetime import datetime
from html import unescape
import html2text

def clean_html_content(html_content):
    """Convert HTML to markdown and clean up"""
    if not html_content:
        return ""
    
    # Initialize html2text converter
    h = html2text.HTML2Text()
    h.ignore_links = False
    h.ignore_images = False
    h.ignore_emphasis = False
    h.body_width = 0  # Don't wrap lines
    
    # Clean up some common issues
    html_content = html_content.replace('<br/>', '<br>')
    html_content = html_content.replace('&nbsp;', ' ')
    
    # Handle YouTube embeds
    youtube_pattern = r'<iframe[^>]+src="[^"]*youtube\.com/embed/([^"?]+)[^"]*"[^>]*></iframe>'
    html_content = re.sub(youtube_pattern, r'{% include youtube.html id="\1" %}', html_content)
    
    # Convert to markdown
    markdown_content = h.handle(html_content)
    
    # Clean up extra whitespace
    markdown_content = re.sub(r'\n\s*\n\s*\n', '\n\n', markdown_content)
    markdown_content = markdown_content.strip()
    
    return markdown_content

def sanitize_filename(title):
    """Create a safe filename from title"""
    # Remove or replace problematic characters
    filename = re.sub(r'[^\w\s-]', '', title)
    filename = re.sub(r'[-\s]+', '-', filename)
    return filename.lower()

def parse_wordpress_xml(xml_file):
    """Parse WordPress XML and extract posts"""
    try:
        tree = ET.parse(xml_file)
        root = tree.getroot()
        
        # Define namespaces
        namespaces = {
            'wp': 'http://wordpress.org/export/1.2/',
            'content': 'http://purl.org/rss/1.0/modules/content/',
            'dc': 'http://purl.org/dc/elements/1.1/'
        }
        
        posts = []
        
        # Find all items
        for item in root.findall('.//item'):
            # Check if it's a post (not attachment or page)
            post_type = item.find('wp:post_type', namespaces)
            if post_type is None or post_type.text != 'post':
                continue
                
            # Check if published
            status = item.find('wp:status', namespaces)
            if status is None or status.text != 'publish':
                continue
            
            # Extract post data
            title_elem = item.find('title')
            title = title_elem.text if title_elem is not None else 'Untitled'
            
            content_elem = item.find('content:encoded', namespaces)
            content = content_elem.text if content_elem is not None else ''
            
            pub_date_elem = item.find('pubDate')
            if pub_date_elem is not None:
                # Parse date
                try:
                    pub_date = datetime.strptime(pub_date_elem.text, '%a, %d %b %Y %H:%M:%S %z')
                except ValueError:
                    try:
                        pub_date = datetime.strptime(pub_date_elem.text, '%a, %d %b %Y %H:%M:%S +0000')
                    except ValueError:
                        pub_date = datetime.now()
            else:
                pub_date = datetime.now()
            
            # Extract categories
            categories = []
            for category in item.findall('category[@domain="category"]'):
                if category.text:
                    categories.append(category.text)
            
            # Extract tags
            tags = []
            for tag in item.findall('category[@domain="post_tag"]'):
                if tag.text:
                    tags.append(tag.text)
            
            # Extract author
            creator_elem = item.find('dc:creator', namespaces)
            author = creator_elem.text if creator_elem is not None else 'Jeremy Poulter'
            
            # Extract link/slug
            link_elem = item.find('link')
            link = link_elem.text if link_elem is not None else ''
            
            post_data = {
                'title': unescape(title),
                'content': content,
                'date': pub_date,
                'categories': categories,
                'tags': tags,
                'author': author,
                'link': link
            }
            
            posts.append(post_data)
            
        return posts
        
    except ET.ParseError as e:
        print(f"Error parsing XML: {e}")
        return []
    except Exception as e:
        print(f"Unexpected error: {e}")
        return []

def create_jekyll_post(post_data, output_dir):
    """Create a Jekyll post file from post data"""
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Generate filename
    date_str = post_data['date'].strftime('%Y-%m-%d')
    title_slug = sanitize_filename(post_data['title'])
    filename = f"{date_str}-{title_slug}.md"
    filepath = os.path.join(output_dir, filename)
    
    # Convert content to markdown
    markdown_content = clean_html_content(post_data['content'])
    
    # Create front matter
    front_matter = ['---']
    front_matter.append(f'layout: post')
    front_matter.append(f'title: "{post_data["title"].replace('"', '\\"')}"')
    front_matter.append(f'date: {post_data["date"].strftime("%Y-%m-%d %H:%M:%S %z")}')
    front_matter.append(f'author: "{post_data["author"]}"')
    
    if post_data['categories']:
        front_matter.append(f'categories: {post_data["categories"]}')
    
    if post_data['tags']:
        front_matter.append(f'tags: {post_data["tags"]}')
    
    if post_data['link']:
        front_matter.append(f'original_url: "{post_data["link"]}"')
    
    front_matter.append('---')
    front_matter.append('')
    
    # Write the file
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write('\n'.join(front_matter))
        f.write(markdown_content)
    
    print(f"Created: {filename}")
    return filepath

def main():
    xml_file = 'Squarespace-Wordpress-Export-05-17-2025.xml'
    output_dir = '_posts'
    
    if not os.path.exists(xml_file):
        print(f"Error: {xml_file} not found")
        return
    
    print("Parsing WordPress XML...")
    posts = parse_wordpress_xml(xml_file)
    
    if not posts:
        print("No posts found or error parsing XML")
        return
    
    print(f"Found {len(posts)} posts")
    
    print("Converting to Jekyll posts...")
    for post in posts:
        try:
            create_jekyll_post(post, output_dir)
        except Exception as e:
            print(f"Error creating post '{post['title']}': {e}")
    
    print("Conversion complete!")

if __name__ == '__main__':
    main()
