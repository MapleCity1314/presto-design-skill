import './App.css'

const features = [
  {
    icon: '⚡',
    title: 'Next-Gen AI',
    description: 'Leverage our next-generation AI to supercharge your productivity and unlock new levels of efficiency across your entire organisation.',
  },
  {
    icon: '🔗',
    title: 'Seamless Integration',
    description: 'Connect with 1,000+ tools you already use. Our integration ecosystem ensures a frictionless experience from day one.',
  },
  {
    icon: '📊',
    title: 'Powerful Analytics',
    description: 'Gain actionable insights with real-time analytics. Make data-driven decisions that propel your business forward.',
  },
]

const stats = [
  { value: '99.99%', label: 'Uptime Guarantee' },
  { value: '50,000+', label: 'Teams Worldwide' },
  { value: '10M+',   label: 'Tasks Completed' },
]

const testimonials = [
  {
    quote: 'FlowSync has completely transformed how our team collaborates. The AI features alone are worth every penny.',
    name: 'Sarah Chen',
    role: 'CEO, TechCorp',
    // Fix: all avatars had identical ?img=1 seed — now unique per person
    avatar: 'https://i.pravatar.cc/88?img=47',
  },
  {
    quote: 'We saw a 300% increase in productivity after switching to FlowSync. I recommend it to every founder I know.',
    name: 'James Patel',
    role: 'CTO, StartupXYZ',
    avatar: 'https://i.pravatar.cc/88?img=12',
  },
  {
    quote: 'The seamless workflow automation has saved our team countless hours every single week. Genuinely a game-changer.',
    name: 'Maria Johnson',
    role: 'Product Manager, Enterprise Co',
    avatar: 'https://i.pravatar.cc/88?img=32',
  },
]

const footerLinks = {
  Product:   ['Features', 'Pricing', 'Changelog', 'Roadmap'],
  Company:   ['About', 'Blog', 'Careers', 'Press'],
  Resources: ['Documentation', 'API Reference', 'Status', 'Support'],
  Legal:     ['Privacy Policy', 'Terms of Service', 'Cookie Policy', 'GDPR'],
}

// Fix: hardcoded "2024" replaced with dynamic year
const currentYear = new Date().getFullYear()

export default function App() {
  return (
    <div className="app">

      {/* ── Navigation ─────────────────────────────────────────── */}
      <nav className="navbar" aria-label="Main navigation">
        <div className="container">
          <a href="/" className="navbar-brand" aria-label="FlowSync home">
            <span className="brand-logo" aria-hidden="true">⚡</span>
            <span className="brand-name">FlowSync</span>
          </a>

          <ul className="navbar-links" role="list">
            <li><a href="#">Features</a></li>
            <li><a href="#">Pricing</a></li>
            <li><a href="#">Blog</a></li>
            <li><a href="#">About</a></li>
          </ul>

          <div className="navbar-actions">
            <button className="btn-ghost">Log In</button>
            <button className="btn-primary">Get Started</button>
          </div>
        </div>
      </nav>

      {/* ── Hero ───────────────────────────────────────────────── */}
      <section className="hero" aria-labelledby="hero-heading">
        <div className="container">
          <div className="hero-badge" aria-hidden="true">
            🎉 New: AI-Powered Workflows
          </div>

          <h1 className="hero-title" id="hero-heading">
            Elevate Your Workflow,{' '}
            {/* Fix: removed gradient-text — illegible on gradient background.
                Use a softened white italic for contrast instead. */}
            <span className="hero-title-accent">Unleash Your Potential</span>
          </h1>

          <p className="hero-subtitle">
            FlowSync is the next-generation project management platform that
            seamlessly integrates all your tools, leverages cutting-edge AI,
            and helps your team deliver results faster than ever before.
            Join 50,000+ teams already transforming their workflows.
          </p>

          <div className="hero-actions">
            <button className="btn-primary btn-large">Start Free Trial</button>
            <button className="btn-outline btn-large">Watch Demo</button>
          </div>

          <p className="hero-disclaimer">
            No credit card required · Free 14-day trial · Cancel anytime
          </p>
        </div>
      </section>

      {/* ── Features ───────────────────────────────────────────── */}
      <section className="features" aria-labelledby="features-heading">
        <div className="container">
          <h2 className="section-title" id="features-heading">
            Everything You Need to Succeed
          </h2>
          <p className="section-subtitle">
            Our comprehensive suite of features is designed to streamline your
            workflow and maximise your team's productivity.
          </p>

          <div className="features-grid">
            {features.map((f) => (
              <article className="feature-card" key={f.title}>
                <div className="feature-icon" aria-hidden="true">{f.icon}</div>
                <h3 className="feature-title">{f.title}</h3>
                <p className="feature-description">{f.description}</p>
                <a href="#" className="feature-link">
                  Learn more <span aria-hidden="true">→</span>
                </a>
              </article>
            ))}
          </div>
        </div>
      </section>

      {/* ── Stats ──────────────────────────────────────────────── */}
      <section className="stats" aria-label="Key metrics">
        <div className="container">
          <div className="stats-grid">
            {stats.map((s) => (
              <div className="stat-item" key={s.label}>
                <div className="stat-value" aria-label={s.value}>{s.value}</div>
                <div className="stat-label">{s.label}</div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* ── Testimonials ───────────────────────────────────────── */}
      <section className="testimonials" aria-labelledby="testimonials-heading">
        <div className="container">
          <h2 className="section-title" id="testimonials-heading">
            Loved by Teams Worldwide
          </h2>
          <p className="section-subtitle">
            Don't just take our word for it. Here's what our customers say.
          </p>

          <div className="testimonials-grid">
            {testimonials.map((t, i) => (
              <blockquote className="testimonial-card" key={i}>
                <p className="testimonial-quote">"{t.quote}"</p>
                <footer className="testimonial-author">
                  <img
                    src={t.avatar}
                    alt={`Portrait of ${t.name}`}
                    className="testimonial-avatar"
                    width="44"
                    height="44"
                    loading="lazy"
                  />
                  <div>
                    <cite className="testimonial-name">{t.name}</cite>
                    <div className="testimonial-role">{t.role}</div>
                  </div>
                </footer>
              </blockquote>
            ))}
          </div>
        </div>
      </section>

      {/* ── CTA ────────────────────────────────────────────────── */}
      <section className="cta-section" aria-labelledby="cta-heading">
        <div className="container">
          <h2 className="cta-title" id="cta-heading">
            Ready to Transform Your Workflow?
          </h2>
          <p className="cta-subtitle">
            Join thousands of teams who have already unlocked their full
            potential with FlowSync.
          </p>
          {/* Fix: removed exclamation mark — informal tone for SaaS CTA */}
          <button className="btn-primary btn-large btn-cta">
            Get Started for Free
          </button>
        </div>
      </section>

      {/* ── Footer ─────────────────────────────────────────────── */}
      <footer className="footer" role="contentinfo">
        <div className="container">

          <div className="footer-top">
            <div className="footer-brand" aria-label="FlowSync">
              <span aria-hidden="true">⚡</span>
              FlowSync
            </div>
            <p className="footer-tagline">
              The workflow platform for modern teams.
            </p>
          </div>

          <nav className="footer-grid" aria-label="Footer navigation">
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

          <div className="footer-bottom">
            {/* Fix: hardcoded 2024 replaced with dynamic currentYear */}
            <p>© {currentYear} FlowSync Inc. All rights reserved.</p>
          </div>

        </div>
      </footer>

    </div>
  )
}
