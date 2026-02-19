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

/* ===== Research cards (neutral style for both light & dark themes) ===== */
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

  /* keeps link rows roughly aligned */
  min-height: 5.6em;
}

.research-card .card-link {
  margin-top: 14px;
}

.research-card .card-link a {
  text-decoration: none;
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
    Welcome to the <strong>International Development Cooperation in VEWD(Vocational Education and Workforce Development) Lab</strong> at Seoul National University.<br>
    We conduct rigorous quantitative research on education, workforce development, and labor market dynamics.<br>
    Our work informs policy reform and development cooperation in education through evidence and impact evaluation.
  </p>
</div>

<!-- 3) Research Themes -->
<div style="max-width: 1200px; margin: 0 auto;">
  <h2 style="margin: 0 0 18px 0;">Research Themes</h2>

  <div class="research-grid">

    <!-- Card 1 -->
    <div class="research-card">
      <h3 style="font-size:1.22rem;">TVET &amp; Policy Reform</h3>
      <p>
        Institutional change and impact evaluation in education and TVET systems,
        including individual labor-market transitions and growth trajectories.
      </p>
      <div class="card-link">
        <a href="/research/">Learn more →</a>
      </div>
    </div>

    <!-- Card 2 -->
    <div class="research-card">
      <h3 style="font-size:1.22rem;">Occupations &amp; Work</h3>
      <p>
        How AI and population aging reshape occupations, tasks, and labor markets—
        mapping change and identifying emerging skill demands.
      </p>
      <div class="card-link">
        <a href="/research/">Learn more →</a>
      </div>
    </div>

    <!-- Card 3 -->
    <div class="research-card">
      <h3 style="font-size:1.18rem;">Development Cooperation</h3>
      <p>
        Collaborative projects in education and TVET with international partners
        such as the World Bank, FAO, and KOICA—translating evidence into practice.
      </p>
      <div class="card-link">
        <a href="/research/">Learn more →</a>
      </div>
    </div>

  </div>
</div>
