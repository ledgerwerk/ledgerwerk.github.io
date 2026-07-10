---
layout: default
title: Home
description: Open source tools for durable engineering workflows
---

<section class="hero">
  <div class="hero-copy">
    <p class="eyebrow">Open source tools for durable engineering work</p>
    <h1>Keep the work legible.</h1>
    <p class="hero-lede">ledgerwerk builds small, inspectable tools that help teams carry decisions, requirements, tasks, documentation, and project memory forward.</p>
    <div class="hero-actions">
      <a class="button button-primary" href="{{ '/tools/' | relative_url }}">Browse documentation</a>
      <a class="button button-secondary" href="https://github.com/ledgerwerk" rel="external noopener">Explore on GitHub</a>
    </div>
  </div>
  <div class="hero-panel" aria-label="ledgerwerk toolkit summary">
    <div class="hero-panel-label">The toolkit</div>
    <div class="hero-stat">{{ site.data.tools | size }}<span>focused tools</span></div>
    <p>File-based, reviewable state for coding workflows.</p>
  </div>
</section>

<section class="principles" aria-labelledby="principles-title">
  <div>
    <p class="eyebrow">Designed for handoff</p>
    <h2 id="principles-title">Durable context without a black box.</h2>
  </div>
  <p>Each tool owns one kind of project knowledge. Records stay close to the repository, remain readable in code review, and can be used by both people and coding agents.</p>
</section>

<section class="tool-section" aria-labelledby="tools-title">
  <div class="section-heading">
    <div>
      <p class="eyebrow">The toolkit</p>
      <h2 id="tools-title">Tools for the whole delivery loop</h2>
    </div>
    <a class="text-link" href="{{ '/tools/' | relative_url }}">View documentation <span aria-hidden="true">↗</span></a>
  </div>
  <div class="cards tool-cards">
    {% for tool in site.data.tools %}
    <article class="card tool-card">
      <p class="card-label">ledgerwerk tool</p>
      <h3>{{ tool.name }}</h3>
      <p>{{ tool.description }}</p>
      <div class="card-links">
        {% if tool.docs_url %}
        <a href="{{ tool.docs_url | relative_url }}">Read docs <span aria-hidden="true">↗</span></a>
        {% endif %}
        <a href="{{ tool.repo_url }}" rel="external noopener">GitHub <span aria-hidden="true">↗</span></a>
      </div>
    </article>
    {% endfor %}
  </div>
</section>

<section class="next-step">
  <p class="eyebrow">Start where the work is</p>
  <h2>Choose the record you need to make durable.</h2>
  <p>Use the Tools menu to jump to documentation, or open any project on GitHub to install it and inspect its source.</p>
</section>
