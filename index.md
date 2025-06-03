---
layout: default
---

<div class="home">
  <h1 class="page-heading">Welcome to BigJungle Ltd</h1>
  
  <div class="hero-section">
    <p class="hero-text">
      Exploring technology, IoT innovations, and open-source projects. 
      From smart home automation to industrial IoT solutions.
    </p>
  </div>

  <h2>Latest Posts</h2>
  
  <ul class="post-list">
    {% for post in site.posts limit: 5 %}
      <li>
        <span class="post-meta">{{ post.date | date: "%b %-d, %Y" }}</span>
        <h3>
          <a class="post-link" href="{{ post.url | relative_url }}">
            {{ post.title | escape }}
          </a>
        </h3>
        
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
      </li>
    {% endfor %}
  </ul>

  <p class="rss-subscribe">
    <a href="{{ site.baseurl }}/blog/">View all posts</a> | 
    <a href="{{ "/feed.xml" | relative_url }}">Subscribe via RSS</a>
  </p>
</div>

<style>
.hero-section {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  padding: 2rem;
  border-radius: 8px;
  margin: 2rem 0;
}

.hero-text {
  font-size: 1.2rem;
  margin: 0;
  text-align: center;
}

.post-list {
  list-style: none;
  padding: 0;
}

.post-list > li {
  margin-bottom: 2rem;
  border-bottom: 1px solid #eee;
  padding-bottom: 1.5rem;
}

.post-meta {
  font-size: 0.875rem;
  color: #666;
}

.post-excerpt {
  margin: 0.5rem 0;
  color: #555;
}

.post-categories {
  margin-top: 0.5rem;
}

.category {
  background: #f0f0f0;
  padding: 0.2rem 0.5rem;
  border-radius: 3px;
  font-size: 0.8rem;
  margin-right: 0.5rem;
}
</style>
