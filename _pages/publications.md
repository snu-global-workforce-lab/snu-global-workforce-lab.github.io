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
  border-radius:10px;
  border:1px solid rgba(128,128,128,0.22);
  background: rgba(128,128,128,0.10);
  text-decoration:none;
  font-weight:800;
}
.pub-btn:hover{ background: rgba(128,128,128,0.16); }

.pub-section-title{
  margin-top:24px;
  margin-bottom:10px;
  font-size:1.25rem;
  font-weight:900;
}
.pub-note{
  opacity:0.85;
  font-size:0.95rem;
  line-height:1.55;
}
</style>

<div class="pub-top">
  <a class="pub-btn" href="{{ '/files/CV_SuJungChoi.pdf' | relative_url }}" target="_blank" rel="noopener">Download CV (PDF)</a>
  <!-- 있으면 링크 넣고, 없으면 삭제 -->
  <a class="pub-btn" href="#" target="_blank" rel="noopener">Google Scholar</a>
</div>

<p class="pub-note">
Publications are maintained as structured entries. Most items are imported from Google Scholar (BibTeX), and any missing items can be added manually.
</p>

{% assign pubs = site.publications | sort: "date" | reverse %}

<div class="pub-section-title">Journal Articles</div>
{% for p in pubs %}
  {% if p.type == "Journal Article" %}
    {% include archive-single.html %}
  {% endif %}
{% endfor %}

<div class="pub-section-title">Book Chapters</div>
{% for p in pubs %}
  {% if p.type == "Book Chapter" %}
    {% include archive-single.html %}
  {% endif %}
{% endfor %}

<div class="pub-section-title">Reports & Policy Outputs</div>
{% for p in pubs %}
  {% if p.type == "Report" %}
    {% include archive-single.html %}
  {% endif %}
{% endfor %}

<div class="pub-section-title">Working Papers</div>
{% for p in pubs %}
  {% if p.type == "Working Paper" %}
    {% include archive-single.html %}
  {% endif %}
{% endfor %}
