---
permalink: /
title: ""
author_profile: false
---

<style>
/* ===== Research grid ===== */
.research-grid {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 20px;
}

@media (max-width: 1000px) {
  .research-grid {
    grid-template-columns: 1fr;
  }
}

/* ===== Research cards ===== */
.research-card {
  border-radius: 16px;
  padding: 22px;
  display: flex;
  flex-direction: column;
  background: rgba(128, 128, 128, 0.14);
  border: 1px solid rgba(128, 128, 128, 0.28);
  transition: transform 0.18s ease,
              box-shadow 0.18s ease,
              background 0.18s ease,
              border-color 0.18s ease;
}

.research-card:hover {
  transform: translateY(-2px);
  background: rgba(128, 128, 128, 0.18);
  border-color: rgba(128, 128, 128, 0.36);
  box-shadow: 0 10px 26px rgba(0,0,0,0.18);
}

.research-card h3 {
  margin: 0 0 12px 0;
  line-height: 1.3;
}

.research-card p {
  margin: 0;
  line-height: 1.6;
  opacity: 0.88;
  min-height: 8.8em;
}

.research-card .card-link {
  margin-top: 14px;
}

.research-card .card-link a {
  text-decoration: none;
}

.kr-subtitle {
  font-size: 0.78rem;
  opacity: 0.78;
  font-weight: 500;
  display: block;
  margin-top: 2px;
}

.kr-text {
  font-size: 0.85rem;
  opacity: 0.82;
  margin-top: 8px;
  line-height: 1.55;
}

.section-kr {
  font-size: 0.85rem;
  opacity: 0.75;
  font-weight: 500;
}
</style>

<!-- 1) Banner -->
<p style="margin: 0 0 28px 0;">
  <img src="/images/banner.png"
       alt="SNU International Development Cooperation in VEWD Lab banner"
       style="width:100%; height:auto; border-radius:14px;">
</p>

<!-- 2) Welcome Message -->
<div style="max-width: 980px; margin: 0 auto 26px auto;">
  <p style="font-size: 1.05rem; line-height: 1.65; margin: 0;">
    Welcome to the <strong>International Development Cooperation in VEWD (Vocational Education and Workforce Development) Lab</strong> at Seoul National University.<br>
    We conduct rigorous quantitative research on education, workforce development, and labor market dynamics.<br>
    Our work informs policy reform and development cooperation in education through evidence and impact evaluation.
  </p>

  <div style="font-size:0.92rem; opacity:0.85; line-height:1.65; margin-top:14px;">
    서울대학교 <strong>국제산업인력개발협력 연구실</strong>에 오신 것을 환영합니다.<br>
    우리 연구실은 교육, 인력개발, 노동시장 변화에 대한 데이터 기반의 정량 연구를 수행합니다.<br>
    연구 결과를 바탕으로 교육 정책 개혁과 국제개발협력에 기여하는 것이 우리의 목표입니다. 
  </div>
</div>

<!-- 3) Research Themes -->
<div style="max-width: 1200px; margin: 0 auto;">
  <h2 style="margin: 0 0 18px 0;">
    Research Themes
    <div class="section-kr">연구 주제</div>
  </h2>

  <div class="research-grid">

    <!-- Card 1 -->
    <div class="research-card">
      <h3 style="font-size:1.22rem;">
        TVET &amp; Policy Reform
        <div class="kr-subtitle">직업교육 및 정책개혁</div>
      </h3>
      <p>
        Institutional change and impact evaluation in education and TVET systems,
        including individual labor-market transitions and growth trajectories.
        <div class="kr-text">
          교육 및 직업교육 시스템의 제도 변화와 정책 효과를 분석하며,
          개인의 노동시장 전환과 성장 궤적 및 경로를 연구합니다.
        </div>
      </p>
      <div class="card-link">
        <a href="/research/">Learn more →</a>
      </div>
    </div>

    <!-- Card 2 -->
    <div class="research-card">
      <h3 style="font-size:1.22rem;">
        Occupations &amp; Work
        <div class="kr-subtitle">직업 연구</div>
      </h3>
      <p>
        How AI and population aging reshape occupations, tasks, and labor markets—
        mapping change and identifying emerging skill demands.
        <div class="kr-text">
          AI와 고령화가 직업, 과업, 노동시장 구조를 어떻게 변화시키는지를 분석하고,
          새롭게 요구되는 역량을 탐색합니다.
        </div>
      </p>
      <div class="card-link">
        <a href="/research/">Learn more →</a>
      </div>
    </div>

    <!-- Card 3 -->
    <div class="research-card">
      <h3 style="font-size:1.18rem;">
        Development Cooperation
        <div class="kr-subtitle">국제개발협력</div>
      </h3>
      <p>
        Collaborative projects in education and TVET with international partners
        such as the World Bank, FAO, and KOICA—translating evidence into practice.
        <div class="kr-text">
          World Bank, FAO, KOICA 등과의 협력을 통해 교육 및 직업교육 분야의
          국제개발협력 프로젝트를 수행하며, 연구 결과를 실제 정책과 사업에 연결합니다.
        </div>
      </p>
      <div class="card-link">
        <a href="/research/">Learn more →</a>
      </div>
    </div>

  </div>
</div>
