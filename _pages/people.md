---
title: "People"
permalink: /people/
author_profile: false
---

<style>
.people-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(210px, 1fr));
  gap: 24px;
  margin: 18px 0 30px 0;
}

.person-card {
  border-radius: 16px;
  padding: 20px;
  text-align: center;
  background: rgba(128,128,128,0.14);
  border: 1px solid rgba(128,128,128,0.28);
  transition: transform 0.18s ease, box-shadow 0.18s ease;
}

.person-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 10px 24px rgba(0,0,0,0.15);
}

.person-card img {
  width: 180px;
  aspect-ratio: 3 / 4;     /* 세로형 증명사진 비율 */
  object-fit: cover;
  border-radius: 10px;
  margin-bottom: 14px;
  box-shadow: 0 6px 18px rgba(0,0,0,0.12);
}
  
.person-name {
  margin: 6px 0 4px 0;
  font-size: 1.05rem;
}

.person-role {
  margin: 0;
  font-size: 0.95rem;
  opacity: 0.82;
  line-height: 1.35;
}

/* --- Alumni (compact) --- */
.alumni-grid{
  display:grid;
  grid-template-columns: repeat(4, 1fr);
  gap:12px;
  margin-top:12px;
}
@media (max-width: 1100px){
  .alumni-grid{ grid-template-columns: repeat(2, 1fr); }
}
@media (max-width: 650px){
  .alumni-grid{ grid-template-columns: 1fr; }
}
.alumni-card{
  display:flex;
  gap:10px;
  align-items:center;
  padding:10px 12px;
  border-radius:12px;
  border:1px solid rgba(128,128,128,0.18);
  background: rgba(128,128,128,0.06);
  transition: transform 0.16s ease, box-shadow 0.16s ease;
}
.alumni-card:hover{
  transform: translateY(-2px);
  box-shadow: 0 10px 20px rgba(0,0,0,0.14);
}
.alumni-photo{
  width:44px;
  height:56px;           /* 세로 증명사진 느낌 */
  object-fit:cover;
  border-radius:8px;      /* 사각 + 살짝 둥글게 */
  border:1px solid rgba(128,128,128,0.22);
  background: rgba(128,128,128,0.10);
  flex: 0 0 auto;
}
.alumni-meta{
  min-width:0;
}
.alumni-name{
  font-weight:800;
  margin:0;
  font-size:0.92rem;
  line-height:1.15;
}
.alumni-affil{
  margin:2px 0 0 0;
  font-size:0.82rem;
  opacity:0.85;
  line-height:1.25;
}
.alumni-tag{
  display:inline-block;
  margin-top:4px;
  font-size:0.72rem;
  opacity:0.75;
}
</style>

## Current Members

---

### Doctoral Researchers

<div class="people-grid">

  <div class="person-card">
    <img src="{{ '/images/heesu.jpeg' | relative_url }}" alt="Heesu Yang">
    <p class="person-name"><strong>Heesoo Yang</strong></p>
    <p class="person-role">Ph.D. Candidate</p>
  </div>

  <div class="person-card">   
    <img src="{{ '/images/minwook.png' | relative_url }}" alt="Minwook Lee">
    <p class="person-name"><strong>Minwook Lee</strong></p>
    <p class="person-role">Ph.D. Candidate</p>
  </div>

  <div class="person-card">
    <img src="{{ '/images/yen.png' | relative_url }}" alt="Yen">
    <p class="person-name"><strong>Le Hai Yen</strong></p>
    <p class="person-role">Ph.D. Candidate</p>
  </div>

  <div class="person-card">
    <img src="{{ '/images/seyoung.jpeg' | relative_url }}" alt="Seyoung Cho">
    <p class="person-name"><strong>Seyoung Cho</strong></p>
    <p class="person-role">Ph.D. Student</p>
  </div>

  <div class="person-card">
    <img src="{{ '/images/juwon.jpeg' | relative_url }}" alt="Juwon Park">
    <p class="person-name"><strong>Juwon Park</strong></p>
    <p class="person-role">Ph.D. Student</p>
  </div>

</div>

---

### Master’s Student

<div class="people-grid">

  <div class="person-card">
    <img src="{{ '/images/ryul.jpeg' | relative_url }}" alt="Ryul Heo">
    <p class="person-name"><strong>Rul Heo</strong></p>
    <p class="person-role">M.A. Student</p>
  </div>

</div>

---

### Part-time Ph.D. Student

<div class="people-grid">

  <div class="person-card">
    <img src="{{ '/images/heesu.png' | relative_url }}" alt="Gohun Kim">
    <p class="person-name"><strong>Gohun Kim</strong></p>
    <p class="person-role">Ph.D. Student (Part-time)<br>Dahawa Farm</p>
  </div>

</div>

---

### Project Team

<div class="people-grid">

  <div class="person-card">
    <img src="/images/fm.png" alt="TBD">
    <p class="person-name"><strong>TBD</strong></p>
    <p class="person-role">Field Manager</p>
  </div>

</div>

---

### Project Staff

<div class="people-grid">

  <div class="person-card">
    <img src="{{ '/images/eunji.jpeg' | relative_url }}" alt="Eunji Jang">
    <p class="person-name"><strong>Eunji Jang</strong></p>
    <p class="person-role">Project Staff</p>
  </div>

  <div class="person-card">
    <img src="{{ '/images/youngjoo.jpeg' | relative_url }}" alt="Youngjoo Kwon">
    <p class="person-name"><strong>Youngju Kwon</strong></p>
    <p class="person-role">Project Staff</p>
  </div>

  <div class="person-card">
    <img src="{{ '/images/hyunkyung.jpeg' | relative_url }}" alt="Hyunkyung Shin">
    <p class="person-name"><strong>Hyunyeong Shin</strong></p>
    <p class="person-role">Project Staff</p>
  </div>

  <div class="person-card">
    <img src="{{ '/images/jinseon.png' | relative_url }}" alt="Jinseon Jeon">
    <p class="person-name"><strong>Jinseon Jeon</strong></p>
    <p class="person-role">Project Staff</p>
  </div>

</div>

---

## Alumni
## Alumni

<div class="alumni-grid">

  <div class="alumni-card">
    <img class="alumni-photo" src="{{ '/images/alumni-placeholder.png' | relative_url }}" alt="Suhyun Bae">
    <div class="alumni-meta">
      <p class="alumni-name">Suhyun Bae</p>
      <p class="alumni-affil">Samsung Electronics</p>
      <span class="alumni-tag">Ph.D.</span>
    </div>
  </div>

  <div class="alumni-card">
    <img class="alumni-photo" src="{{ '/images/alumni-placeholder.png' | relative_url }}" alt="Jagyeong Park">
    <div class="alumni-meta">
      <p class="alumni-name">Jagyeong Park</p>
      <p class="alumni-affil">Jeonbuk Research Institute</p>
      <span class="alumni-tag">Alumni</span>
    </div>
  </div>

  <div class="alumni-card">
    <img class="alumni-photo" src="{{ '/images/alumni-placeholder.png' | relative_url }}" alt="Seongji Jeong">
    <div class="alumni-meta">
      <p class="alumni-name">Seongji Jeong</p>
      <p class="alumni-affil">Pennsylvania State University</p>
      <span class="alumni-tag">Alumni</span>
    </div>
  </div>

  <div class="alumni-card">
    <img class="alumni-photo" src="{{ '/images/alumni-placeholder.png' | relative_url }}" alt="Jisik Min">
    <div class="alumni-meta">
      <p class="alumni-name">Jisik Min</p>
      <p class="alumni-affil">Soonchunhyang University</p>
      <span class="alumni-tag">Alumni</span>
    </div>
  </div>

  <div class="alumni-card">
    <img class="alumni-photo" src="{{ '/images/alumni-placeholder.png' | relative_url }}" alt="Gwiyeong Ko">
    <div class="alumni-meta">
      <p class="alumni-name">Gwiyeong Ko</p>
      <p class="alumni-affil">Korea Foundation for Local Educational Administration</p>
      <span class="alumni-tag">Alumni</span>
    </div>
  </div>

  <div class="alumni-card">
    <img class="alumni-photo" src="{{ '/images/alumni-placeholder.png' | relative_url }}" alt="Hyunju Yoo">
    <div class="alumni-meta">
      <p class="alumni-name">Hyunju Yoo</p>
      <p class="alumni-affil">Inha University</p>
      <span class="alumni-tag">Alumni</span>
    </div>
  </div>

  <div class="alumni-card">
    <img class="alumni-photo" src="{{ '/images/alumni-placeholder.png' | relative_url }}" alt="Seokho Hong">
    <div class="alumni-meta">
      <p class="alumni-name">Seokho Hong</p>
      <p class="alumni-affil">—</p>
      <span class="alumni-tag">Alumni</span>
    </div>
  </div>

  <div class="alumni-card">
    <img class="alumni-photo" src="{{ '/images/jihyeon.png' | relative_url }}" alt="Jihyeon An">
    <div class="alumni-meta">
      <p class="alumni-name">Jihyeon An</p>
      <p class="alumni-affil">건국대학교</p>
      <span class="alumni-tag">Alumni</span>
    </div>
  </div>

  <div class="alumni-card">
    <img class="alumni-photo" src="{{ '/images/jiyeon1.png' | relative_url }}" alt="Jiyeon Kim">
    <div class="alumni-meta">
      <p class="alumni-name">Jiyeon Kim</p>
      <p class="alumni-affil">Ph.D. Student</p>
      <span class="alumni-tag">Alumni</span>
    </div>
  </div>

</div>
