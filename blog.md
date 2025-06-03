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
        
        {% if post.excerpt %}
          <div class="post-excerpt">
            {{ post.excerpt }}
          </div>
        {% endif %}
        
        {% if post.categories %}
          <div class="post-categories">
            {% for category in post.categories %}
              <span class="category">{{ category }}</span>
            {% endfor %}
          </div>
        {% endif %}
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

.post-categories {
  margin-top: 1rem;
}

.category {
  background: #f0f0f0;
  padding: 0.2rem 0.5rem;
  border-radius: 3px;
  font-size: 0.8rem;
  margin-right: 0.5rem;
  color: #666;
}
</style>
