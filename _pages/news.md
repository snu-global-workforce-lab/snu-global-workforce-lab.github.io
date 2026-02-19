---
title: "News"
permalink: /news/
author_profile: false
---

<style>
.news-grid{
  display:grid;
  grid-template-columns: 1fr 1fr 1fr;
  gap:18px;
  margin-top:18px;
}
@media (max-width: 1000px){
  .news-grid{ grid-template-columns: 1fr; }
}
.news-card{
  border:1px solid rgba(128,128,128,0.18);
  background: rgba(128,128,128,0.07);
  border-radius:14px;
  overflow:hidden;
  transition: transform 0.18s ease, box-shadow 0.18s ease;
}
.news-card:hover{
  transform: translateY(-2px);
  box-shadow: 0 10px 22px rgba(0,0,0,0.18);
}
.news-thumb{
  width:100%;
  height:150px;
  object-fit:cover;
  display:block;
}
.news-body{
  padding:14px 16px;
}
.news-title{
  margin:0 0 8px 0;
  font-size:1.02rem;
  font-weight:700;
  line-height:1.25;
}
.news-title a{
  text-decoration:none;
}
.news-title a:hover{
  text-decoration:underline;
}
.news-excerpt{
  margin:0 0 10px 0;
  opacity:0.85;
  font-size:0.9rem;
  line-height:1.35;
}
.news-meta{
  font-size:0.82rem;
  opacity:0.7;
}

/* Archive */
.archive{
  margin-top:34px;
}
.archive summary{
  cursor:pointer;
  font-weight:700;
  font-size:1.05rem;
  padding:10px 0;
}
.archive-list{
  margin-top:10px;
}
.archive-item{
  padding:10px 0;
  border-bottom:1px solid rgba(128,128,128,0.18);
}
.archive-item a{
  font-weight:700;
  text-decoration:none;
}
.archive-item a:hover{
  text-decoration:underline;
}
.archive-item .small{
  display:block;
  opacity:0.8;
  margin-top:4px;
  font-size:0.9rem;
  line-height:1.3;
}
</style>

{% assign news_posts = site.categories.news %}

## Recent News

<div class="news-grid">
{% for post in news_posts limit:3 %}
  <div class="news-card">
    {% if post.header.teaser %}
      <a href="{{ post.url | relative_url }}">
        <img class="news-thumb" src="{{ post.header.teaser | relative_url }}" alt="{{ post.title }}">
      </a>
    {% endif %}

    <div class="news-body">
      <p class="news-title">
        <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
      </p>

      {% if post.excerpt %}
        <p class="news-excerpt">{{ post.excerpt | strip_html }}</p>
      {% endif %}

      <div class="news-meta">{{ post.date | date: "%b %d, %Y" }}</div>
    </div>
  </div>
{% endfor %}
</div>

<details class="archive">
  <summary>Archive (click to expand)</summary>
  <div class="archive-list">
    {% for post in news_posts offset:3 %}
      <div class="archive-item">
        <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
        <span class="small">
          {{ post.date | date: "%b %d, %Y" }}
          {% if post.excerpt %} — {{ post.excerpt | strip_html }}{% endif %}
        </span>
      </div>
    {% endfor %}
  </div>
</details>
