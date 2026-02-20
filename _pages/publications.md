---
title: "Publications"
permalink: /publications/
author_profile: false
---

<style>
.pub-top{
  display:flex; flex-wrap:wrap; gap:10px; align-items:center;
  margin: 10px 0 16px 0;
}
.pub-btn{
  display:inline-block;
  padding:10px 14px;
  border-radius:12px;
  border:1px solid rgba(128,128,128,0.22);
  background: rgba(128,128,128,0.10);
  text-decoration:none;
  font-weight:800;
}
.pub-btn:hover{ background: rgba(128,128,128,0.16); }

.pub-note{
  opacity:0.85;
  font-size:0.95rem;
  line-height:1.55;
  margin: 8px 0 18px 0;
}

.pub-section{
  margin-top:22px;
}
.pub-section h2{
  margin-bottom:12px;
}

.pub-list{ margin:0; padding-left: 18px; }
.pub-item{ margin: 0 0 12px 0; line-height:1.35; }

.pub-title{
  font-weight:800;
}
.pub-venue{
  opacity:0.85;
}
.pub-links a{
  margin-left:8px;
  font-weight:700;
  text-decoration:none;
}
.pub-links a:hover{ text-decoration:underline; }

.pub-empty{
  opacity:0.7;
  margin: 0 0 10px 0;
}
</style>

<div class="pub-top">
  <a class="pub-btn" href="{{ '/files/CV_SuJungChoi.pdf' | relative_url }}" target="_blank" rel="noopener">Download CV (PDF)</a>
  <!-- 구글스칼라 링크 넣기 (있으면 URL 교체) -->
  <a class="pub-btn" href="#" target="_blank" rel="noopener">Google Scholar</a>
</div>

<p class="pub-note">
Publications are maintained as structured entries. Most items are imported from Google Scholar (BibTeX), and any missing items can be added manually.
</p>

{% assign pubs = site.publications | sort: "date" | reverse %}

{% assign journal = pubs | where: "type", "Journal Article" %}
{% assign chapters = pubs | where: "type", "Book Chapter" %}
{% assign reports = pubs | where: "type", "Report" %}
{% assign wps = pubs | where: "type", "Working Paper" %}

<div class="pub-section">
  <h2>Journal Articles</h2>
  {% if journal.size == 0 %}
    <p class="pub-empty">No items found.</p>
  {% else %}
    <ol class="pub-list">
    {% for p in journal %}
      <li class="pub-item">
        <span class="pub-title">{{ p.title }}</span>
        {% if p.venue %}<span class="pub-venue"> — <em>{{ p.venue }}</em></span>{% endif %}
        {% if p.citation %}<div class="pub-venue">{{ p.citation }}</div>{% endif %}
        <div class="pub-links">
          <a href="{{ p.url | relative_url }}">Details</a>
          {% if p.paperurl and p.paperurl != "" %}
            <a href="{{ p.paperurl }}" target="_blank" rel="noopener">Link</a>
          {% endif %}
        </div>
      </li>
    {% endfor %}
    </ol>
  {% endif %}
</div>

<div class="pub-section">
  <h2>Book Chapters</h2>
  {% if chapters.size == 0 %}
    <p class="pub-empty">No items found.</p>
  {% else %}
    <ol class="pub-list">
    {% for p in chapters %}
      <li class="pub-item">
        <span class="pub-title">{{ p.title }}</span>
        {% if p.venue %}<span class="pub-venue"> — <em>{{ p.venue }}</em></span>{% endif %}
        {% if p.citation %}<div class="pub-venue">{{ p.citation }}</div>{% endif %}
        <div class="pub-links">
          <a href="{{ p.url | relative_url }}">Details</a>
          {% if p.paperurl and p.paperurl != "" %}
            <a href="{{ p.paperurl }}" target="_blank" rel="noopener">Link</a>
          {% endif %}
        </div>
      </li>
    {% endfor %}
    </ol>
  {% endif %}
</div>

<div class="pub-section">
  <h2>Reports & Policy Outputs</h2>
  {% if reports.size == 0 %}
    <p class="pub-empty">No items found.</p>
  {% else %}
    <ol class="pub-list">
    {% for p in reports %}
      <li class="pub-item">
        <span class="pub-title">{{ p.title }}</span>
        {% if p.venue %}<span class="pub-venue"> — <em>{{ p.venue }}</em></span>{% endif %}
        {% if p.citation %}<div class="pub-venue">{{ p.citation }}</div>{% endif %}
        <div class="pub-links">
          <a href="{{ p.url | relative_url }}">Details</a>
          {% if p.paperurl and p.paperurl != "" %}
            <a href="{{ p.paperurl }}" target="_blank" rel="noopener">Link</a>
          {% endif %}
        </div>
      </li>
    {% endfor %}
    </ol>
  {% endif %}
</div>

<div class="pub-section">
  <h2>Working Papers</h2>
  {% if wps.size == 0 %}
    <p class="pub-empty">No items found.</p>
  {% else %}
    <ol class="pub-list">
    {% for p in wps %}
      <li class="pub-item">
        <span class="pub-title">{{ p.title }}</span>
        {% if p.venue %}<span class="pub-venue"> — <em>{{ p.venue }}</em></span>{% endif %}
        {% if p.citation %}<div class="pub-venue">{{ p.citation }}</div>{% endif %}
        <div class="pub-links">
          <a href="{{ p.url | relative_url }}">Details</a>
          {% if p.paperurl and p.paperurl != "" %}
            <a href="{{ p.paperurl }}" target="_blank" rel="noopener">Link</a>
          {% endif %}
        </div>
      </li>
    {% endfor %}
    </ol>
  {% endif %}
</div>
