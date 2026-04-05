import './App.css'

const features = [
  {
    icon: '🚀',
    title: 'Next-Gen AI',
    description: 'Leverage our next-generation AI to supercharge your productivity and unlock new levels of efficiency across your entire organization.',
  },
  {
    icon: '🔗',
    title: 'Seamless Integration',
    description: 'Connect with 1000+ tools you already use. Our seamless integration ecosystem ensures a frictionless experience from day one.',
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
  { value: '10,000,000+', label: 'Tasks Completed' },
]

const testimonials = [
  {
    quote: 'FlowSync has completely transformed how our team collaborates. It\'s a game-changer!',
    name: 'John Smith',
    role: 'CEO, TechCorp',
    avatar: 'https://i.pravatar.cc/48?img=1',
  },
  {
    quote: 'We saw a 300% increase in productivity after switching to FlowSync. Highly recommended!',
    name: 'Jane Smith',
    role: 'CTO, StartupXYZ',
    avatar: 'https://i.pravatar.cc/48?img=1',
  },
  {
    quote: 'The seamless workflow automation has saved us countless hours every single week.',
    name: 'Bob Johnson',
    role: 'Product Manager, Enterprise Co',
    avatar: 'https://i.pravatar.cc/48?img=1',
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
      {/* Navigation */}
      <nav className="navbar">
        <div className="container">
          <div className="navbar-brand">
            <span className="brand-logo">⚡</span>
            <span className="brand-name">FlowSync</span>
          </div>
          <ul className="navbar-links">
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

      {/* Hero */}
      <section className="hero">
        <div className="container">
          <div className="hero-badge">🎉 New: AI-Powered Workflows</div>
          <h1 className="hero-title">
            Elevate Your Workflow<br />
            <span className="gradient-text">Unleash Your Potential</span>
          </h1>
          <p className="hero-subtitle">
            FlowSync is the next-generation project management platform that seamlessly integrates
            all your tools, leverages cutting-edge AI, and helps your team deliver results faster
            than ever before. Join 50,000+ teams already transforming their workflows.
          </p>
          <div className="hero-actions">
            <button className="btn-primary btn-large">Start Free Trial</button>
            <button className="btn-outline btn-large">Watch Demo</button>
          </div>
          <p className="hero-disclaimer">No credit card required • Free 14-day trial • Cancel anytime</p>
        </div>
      </section>

      {/* Features */}
      <section className="features">
        <div className="container">
          <h2 className="section-title">Everything You Need to Succeed</h2>
          <p className="section-subtitle">
            Our comprehensive suite of features is designed to streamline your workflow
            and maximize your team's productivity.
          </p>
          <div className="features-grid">
            {features.map((f) => (
              <div className="feature-card" key={f.title}>
                <div className="feature-icon">{f.icon}</div>
                <h3 className="feature-title">{f.title}</h3>
                <p className="feature-description">{f.description}</p>
                <a href="#" className="feature-link">Learn more →</a>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Stats */}
      <section className="stats">
        <div className="container">
          <div className="stats-grid">
            {stats.map((s) => (
              <div className="stat-item" key={s.label}>
                <div className="stat-value">{s.value}</div>
                <div className="stat-label">{s.label}</div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Testimonials */}
      <section className="testimonials">
        <div className="container">
          <h2 className="section-title">Loved by Teams Worldwide</h2>
          <p className="section-subtitle">
            Don't just take our word for it. Here's what our customers say.
          </p>
          <div className="testimonials-grid">
            {testimonials.map((t, i) => (
              <div className="testimonial-card" key={i}>
                <p className="testimonial-quote">"{t.quote}"</p>
                <div className="testimonial-author">
                  <img src={t.avatar} alt={t.name} className="testimonial-avatar" />
                  <div>
                    <div className="testimonial-name">{t.name}</div>
                    <div className="testimonial-role">{t.role}</div>
                  </div>
                </div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* CTA */}
      <section className="cta-section">
        <div className="container">
          <h2 className="cta-title">Ready to Transform Your Workflow?</h2>
          <p className="cta-subtitle">
            Join thousands of teams who have already unlocked their full potential with FlowSync.
          </p>
          <button className="btn-primary btn-large">Get Started for Free!</button>
        </div>
      </section>

      {/* Footer */}
      <footer className="footer">
        <div className="container">
          <div className="footer-grid">
            {Object.entries(footerLinks).map(([category, links]) => (
              <div className="footer-column" key={category}>
                <h4 className="footer-heading">{category}</h4>
                <ul className="footer-links">
                  {links.map((link) => (
                    <li key={link}><a href="#">{link}</a></li>
                  ))}
                </ul>
              </div>
            ))}
          </div>
          <div className="footer-bottom">
            <p>© 2024 FlowSync Inc. All rights reserved.</p>
          </div>
        </div>
      </footer>
    </div>
  )
}
