---
layout: default
title: Blog
permalink: /blog/
---

<div class="blog-page">
  <h1>All Posts</h1>
  
  <div class="post-list">
    {% for post in site.posts %}
      <article class="post-preview">
        <header class="post-header">
          <h2>
            <a href="{{ post.url | relative_url }}">{{ post.title | escape }}</a>
          </h2>
          <p class="post-meta">
            <time datetime="{{ post.date | date_to_xmlschema }}">
              {{ post.date | date: "%B %-d, %Y" }}
            </time>
            {% if post.author %} • {{ post.author }}{% endif %}
          </p>
        </header>
        
        <div class="post-excerpt">
          {{ post.excerpt | replace: '</p>', ' ' | strip_html | strip_newlines | truncatewords: 40 }}
          <a class="read-more" href="{{ post.url | relative_url }}">Read more &raquo;</a>
        </div>
      </article>
    {% endfor %}
  </div>
</div>

<style>
.blog-page h1 {
  text-align: center;
  margin-bottom: 2rem;
}

.post-preview {
  margin-bottom: 3rem;
  padding-bottom: 2rem;
  border-bottom: 1px solid #eee;
}

.post-preview:last-child {
  border-bottom: none;
}

.post-header h2 {
  margin-bottom: 0.5rem;
}

.post-header h2 a {
  text-decoration: none;
  color: #333;
}

.post-header h2 a:hover {
  color: #667eea;
}

.post-meta {
  color: #666;
  font-size: 0.9rem;
  margin-bottom: 1rem;
}

.post-excerpt {
  margin: 1rem 0;
  color: #555;
  line-height: 1.6;
}

.read-more {
  white-space: nowrap;
  font-weight: 600;
  color: #667eea;
  text-decoration: none;
}
</style>
