import './App.css'

const features = [
  {
    icon: (
      <svg className="feature-icon-svg" viewBox="0 0 24 24" aria-hidden="true">
        <path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z" />
      </svg>
    ),
    title: 'Workflow automation',
    description:
      'Build multi-step automations in minutes. Connect triggers, conditions, and actions without writing a single line of code — then let FlowSync handle the repetitive work.',
    isFeature: true,
  },
  {
    icon: (
      <svg className="feature-icon-svg" viewBox="0 0 24 24" aria-hidden="true">
        <rect x="3" y="3" width="7" height="7" rx="1" />
        <rect x="14" y="3" width="7" height="7" rx="1" />
        <rect x="3" y="14" width="7" height="7" rx="1" />
        <path d="M17.5 14v6M14.5 17h6" />
      </svg>
    ),
    title: 'Tool integrations',
    description:
      'Works with the tools your team already uses. Connect Slack, GitHub, Jira, Notion, and 900+ other services through a single unified interface.',
  },
  {
    icon: (
      <svg className="feature-icon-svg" viewBox="0 0 24 24" aria-hidden="true">
        <path d="M3 3v18h18" />
        <path d="M7 16l4-4 4 4 4-7" />
      </svg>
    ),
    title: 'Real-time analytics',
    description:
      'Track progress, spot blockers, and measure team output with live dashboards built for clarity — not just raw data.',
  },
]

const stats = [
  { value: '98.7%', label: 'Uptime over the last 12 months', accent: false },
  { value: '47,200+', label: 'Teams worldwide', accent: false },
  { value: '9.4M+', label: 'Tasks completed this quarter', accent: true },
]

const testimonials = [
  {
    quote:
      'After six months with FlowSync, our sprint cycle dropped from three weeks to eleven days. The automation builder alone paid for itself in the first month.',
    name: 'Priya Nair',
    role: 'VP of Engineering, Meridian Labs',
    avatar: 'https://i.pravatar.cc/48?img=47',
  },
  {
    quote:
      'We replaced four separate tools with FlowSync and our onboarding time for new contractors went from two days to a few hours.',
    name: 'Marcus Oluwole',
    role: 'Head of Operations, Trellis Health',
    avatar: 'https://i.pravatar.cc/48?img=12',
  },
  {
    quote:
      'The analytics are genuinely useful. I can see where work gets stuck before it becomes a problem, not after.',
    name: 'Saoirse Brennan',
    role: 'Product Lead, Clearwave',
    avatar: 'https://i.pravatar.cc/48?img=32',
  },
]

const footerLinks = {
  Product: ['Features', 'Pricing', 'Changelog', 'Roadmap'],
  Company: ['About', 'Blog', 'Careers', 'Press'],
  Resources: ['Documentation', 'API Reference', 'Status', 'Support'],
  Legal: ['Privacy Policy', 'Terms of Service', 'Cookie Policy', 'GDPR'],
}

export default function App() {
  return (
    <div className="app">
      {/* Skip-to-content link — keyboard accessibility */}
      <a href="#main-content" className="skip-link">
        Skip to main content
      </a>

      {/* Navigation */}
      <nav className="navbar" aria-label="Primary navigation">
        <div className="container">
          <a href="/" className="navbar-brand" aria-label="FlowSync home">
            <span className="brand-logo" aria-hidden="true">⚡</span>
            <span className="brand-name">FlowSync</span>
          </a>
          <ul className="navbar-links" role="list">
            <li><a href="#features">Features</a></li>
            <li><a href="#pricing">Pricing</a></li>
            <li><a href="#blog">Blog</a></li>
            <li><a href="#about">About</a></li>
          </ul>
          <div className="navbar-actions">
            <button className="btn-ghost" type="button">Log in</button>
            <button className="btn-primary" type="button">Get started</button>
          </div>
        </div>
      </nav>

      {/* Main content */}
      <main id="main-content">

        {/* Hero */}
        <section className="hero" aria-labelledby="hero-heading">
          <div className="container">
            <div className="hero-inner">
              <div className="hero-badge">
                <span className="hero-badge-dot" aria-hidden="true" />
                New: automated workflow templates
              </div>
              <h1 className="hero-title" id="hero-heading">
                Project management<br />
                that works the way{' '}
                <span className="hero-title-accent">your team does</span>
              </h1>
              <p className="hero-subtitle">
                FlowSync connects your tools, automates your handoffs, and gives
                your team a single place to track what matters. No steep learning
                curve, no sprawling configuration.
              </p>
              <div className="hero-actions">
                <button className="btn-primary btn-large" type="button">
                  Start free trial
                </button>
                <button className="btn-outline btn-large" type="button">
                  Watch demo
                </button>
              </div>
              <p className="hero-disclaimer">
                No credit card required &bull; 14-day free trial &bull; Cancel anytime
              </p>
            </div>
          </div>
        </section>

        {/* Features */}
        <section className="features" id="features" aria-labelledby="features-heading">
          <div className="container">
            <header className="section-header">
              <span className="section-label">Features</span>
              <h2 className="section-title" id="features-heading">
                Built for teams that ship
              </h2>
              <p className="section-subtitle">
                A focused set of tools for coordination, automation, and
                visibility — without the bloat.
              </p>
            </header>

            <div className="features-grid">
              {/* First card — asymmetric wide layout */}
              <article className="feature-card" aria-labelledby="feature-title-0">
                <div className="feature-visual" aria-hidden="true">
                  {features[0].icon}
                </div>
                <div className="feature-body">
                  <div className="feature-icon-wrap" aria-hidden="true">
                    {features[0].icon}
                  </div>
                  <h3 className="feature-title" id="feature-title-0">
                    {features[0].title}
                  </h3>
                  <p className="feature-description">{features[0].description}</p>
                  <a href="#features" className="feature-link">
                    See how it works <span aria-hidden="true">→</span>
                  </a>
                </div>
              </article>

              {/* Second and third cards — standard 1-column each in second row */}
              {features.slice(1).map((f, idx) => (
                <article
                  className="feature-card"
                  key={f.title}
                  aria-labelledby={`feature-title-${idx + 1}`}
                >
                  <div className="feature-icon-wrap" aria-hidden="true">
                    {f.icon}
                  </div>
                  <h3 className="feature-title" id={`feature-title-${idx + 1}`}>
                    {f.title}
                  </h3>
                  <p className="feature-description">{f.description}</p>
                  <a href="#features" className="feature-link">
                    Learn more <span aria-hidden="true">→</span>
                  </a>
                </article>
              ))}
            </div>
          </div>
        </section>

        {/* Stats */}
        <section className="stats" aria-labelledby="stats-heading">
          <div className="container">
            <h2 className="sr-only" id="stats-heading">FlowSync by the numbers</h2>
            <div className="stats-grid">
              {stats.map((s) => (
                <div className="stat-item" key={s.label}>
                  <div className="stat-value">
                    {s.accent
                      ? <><span className="stat-value-accent">{s.value}</span></>
                      : s.value}
                  </div>
                  <div className="stat-label">{s.label}</div>
                </div>
              ))}
            </div>
          </div>
        </section>

        {/* Testimonials */}
        <section
          className="testimonials"
          aria-labelledby="testimonials-heading"
        >
          <div className="container">
            <header className="section-header">
              <span className="section-label">Customer stories</span>
              <h2 className="section-title" id="testimonials-heading">
                Heard from real teams
              </h2>
              <p className="section-subtitle">
                No cherry-picked metrics. Here is what people said after their
                first three months.
              </p>
            </header>

            <div className="testimonials-grid">
              {testimonials.map((t, i) => (
                <article
                  className="testimonial-card"
                  key={t.name}
                  aria-labelledby={`testimonial-name-${i}`}
                >
                  <span className="testimonial-quote-mark" aria-hidden="true">
                    &ldquo;
                  </span>
                  <blockquote>
                    <p className="testimonial-quote">{t.quote}</p>
                  </blockquote>
                  <div className="testimonial-author">
                    <img
                      src={t.avatar}
                      alt={`Portrait of ${t.name}`}
                      className="testimonial-avatar"
                      width="40"
                      height="40"
                    />
                    <div>
                      <div
                        className="testimonial-name"
                        id={`testimonial-name-${i}`}
                      >
                        {t.name}
                      </div>
                      <div className="testimonial-role">{t.role}</div>
                    </div>
                  </div>
                </article>
              ))}
            </div>
          </div>
        </section>

        {/* CTA */}
        <section className="cta-section" aria-labelledby="cta-heading">
          <div className="container">
            <div className="cta-inner">
              <h2 className="cta-title" id="cta-heading">
                Ready to simplify how your team works?
              </h2>
              <p className="cta-subtitle">
                Join over 47,000 teams who run their projects on FlowSync.
                Set up takes under ten minutes.
              </p>
              <div className="cta-actions">
                <button className="btn-cta" type="button">
                  Get started for free
                </button>
                <button className="btn-text-link" type="button">
                  Talk to sales
                </button>
              </div>
              <p className="cta-disclaimer">
                No credit card required &bull; Cancel anytime
              </p>
            </div>
          </div>
        </section>

      </main>

      {/* Footer */}
      <footer className="footer" aria-label="Site footer">
        <div className="container">
          <div className="footer-top">
            <div className="footer-brand">
              <div className="footer-brand-name">
                <span className="footer-brand-logo" aria-hidden="true">⚡</span>
                FlowSync
              </div>
              <p className="footer-tagline">
                Project management built for teams that move fast and need to
                stay in sync.
              </p>
            </div>

            <nav className="footer-nav" aria-label="Footer navigation">
              {Object.entries(footerLinks).map(([category, links]) => (
                <div className="footer-column" key={category}>
                  <h3 className="footer-heading">{category}</h3>
                  <ul className="footer-links" role="list">
                    {links.map((link) => (
                      <li key={link}>
                        <a href="#">{link}</a>
                      </li>
                    ))}
                  </ul>
                </div>
              ))}
            </nav>
          </div>

          <div className="footer-bottom">
            <p>&copy; 2025 FlowSync, Inc. All rights reserved.</p>
          </div>
        </div>
      </footer>
    </div>
  )
}
