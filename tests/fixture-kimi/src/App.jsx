import './App.css';

const features =[
  {
    // Phosphor Icon: ArrowsMerge
    icon: (
      <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 256 256">
        <path fill="currentColor" d="M245.66,133.66l-48,48a8,8,0,0,1-11.32-11.32L216.69,136H152a8,8,0,0,1,0-16h64.69l-30.35-30.34a8,8,0,0,1,11.32-11.32l48,48A8,8,0,0,1,245.66,133.66ZM104,192H48a8,8,0,0,0,0,16h56a8,8,0,0,0,0-16Zm0-144H48a8,8,0,0,0,0,16h56a8,8,0,0,0,0-16Zm28,68a8,8,0,0,0-8-8H48a8,8,0,0,0,0,16h76A8,8,0,0,0,132,116Z"></path>
      </svg>
    ),
    title: 'Automated status updates',
    description: 'When work moves in Jira, GitHub, or Linear, FlowSync silently updates the team timeline. Stop interrupting deep work for manual pings.',
  },
  {
    // Phosphor Icon: Plugs
    icon: (
      <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 256 256">
        <path fill="currentColor" d="M237.66,82.34l-64-64A8,8,0,0,0,160,24V56H116A52.06,52.06,0,0,0,64,108v56H24a8,8,0,0,0-8,8v40a8,8,0,0,0,8,8H64v12a8,8,0,0,0,16,0V220h40a8,8,0,0,0,8-8V172h40a8,8,0,0,0,8-8V108a36,36,0,0,1,36-36h32V40A8,8,0,0,0,237.66,82.34ZM104,115.31V108a36,36,0,0,1,36-36h20v43.31A35.85,35.85,0,0,1,149.66,136L120,165.66A51.84,51.84,0,0,0,104,115.31ZM176,80h48v16H176ZM144,154.34,173.66,124.66A20,20,0,0,0,176,112V96h10.34l37.66,37.66ZM80,188H32V180H80ZM80,164H32V156H80Z"></path>
      </svg>
    ),
    title: 'Works with your stack',
    description: 'Native hooks for 40+ engineering and design tools. Setup takes minutes, not sprints. We adapt to how you work, not the other way around.',
  },
  {
    // Phosphor Icon: Target
    icon: (
      <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 256 256">
        <path fill="currentColor" d="M224,128a96,96,0,1,1-96-96A96.11,96.11,0,0,1,224,128Zm-16,0a80,80,0,1,0-80,80A80.09,80.09,0,0,0,208,128Zm-40,0a40,40,0,1,0-40,40A40,40,0,0,0,168,128Zm-16,0a24,24,0,1,0-24,24A24,24,0,0,0,152,128Z"></path>
      </svg>
    ),
    title: 'Clear bottlenecks before they block',
    description: 'Our pipeline view highlights stalled tasks before they derail the sprint. Understand where your team’s time actually goes without invasive time-tracking.',
  },
];

const stats =[
  { value: '99.9%', label: 'Historical uptime' },
  { value: '14,205', label: 'Active teams' },
  { value: '1.2M', label: 'Events processed daily' },
];

const testimonials =[
  {
    quote: 'We stopped doing daily standups. FlowSync just tells us what moved and what is blocked. It has given our engineers an hour back every day.',
    name: 'Elena Rostova',
    role: 'VP Engineering, Segment',
    avatar: 'https://i.pravatar.cc/96?img=5',
  },
  {
    quote: 'The GitHub integration alone saved us 4 hours a week in tracking down PR statuses across squads. Finally, a tool that respects our workflow.',
    name: 'Marcus Webb',
    role: 'Lead Designer, Frame',
    avatar: 'https://i.pravatar.cc/96?img=11',
  },
];

const footerLinks = {
  Product: ['Features', 'Integrations', 'Changelog', 'Security'],
  Resources:['Documentation', 'API Reference', 'Status', 'Guides'],
  Company:['About Us', 'Careers', 'Blog', 'Contact'],
  Legal: ['Privacy Policy', 'Terms of Service', 'Cookie Settings'],
};

export default function App() {
  return (
    <div className="app">
      {/* Navigation */}
      <header className="navbar">
        <div className="container">
          <a href="/" className="navbar-brand">
            <span className="brand-icon">
              <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 256 256">
                <path fill="currentColor" d="M215.79,118.17a8,8,0,0,0-5-5.66L153.18,90.9l14.66-73.33a8,8,0,0,0-13.69-7l-112,120a8,8,0,0,0,3,13l57.63,21.61L88.16,238.43a8,8,0,0,0,13.69,7l112-120A8,8,0,0,0,215.79,118.17ZM109.37,214l10.47-52.38a8,8,0,0,0-5-9.06L62,132.71l84.62-90.66L136.16,94.43a8,8,0,0,0,5,9.06l52.8,19.8Z"></path>
              </svg>
            </span>
            FlowSync
          </a>
          <nav>
            <ul className="navbar-links">
              <li><a href="#features">Platform</a></li>
              <li><a href="#pricing">Pricing</a></li>
              <li><a href="#customers">Customers</a></li>
              <li><a href="#changelog">Changelog</a></li>
            </ul>
          </nav>
          <div className="navbar-actions">
            <a href="#login" className="btn btn-ghost">Log in</a>
            <a href="#signup" className="btn btn-outline">Start trial</a>
          </div>
        </div>
      </header>

      <main>
        {/* Hero */}
        <section className="hero">
          <div className="container">
            <div className="hero-badge animate-fade-up">
              <span>●</span> FlowSync 2.0 is live
            </div>
            <h1 className="hero-title animate-fade-up delay-100">
              Bring your team’s work into one timeline.
            </h1>
            <p className="hero-subtitle animate-fade-up delay-200">
              Connect your existing tools and stop hunting for updates. FlowSync creates a single source of truth for who is doing what, right now.
            </p>
            <div className="hero-actions animate-fade-up delay-300">
              <button className="btn btn-primary btn-large">Start your 14-day trial</button>
              <button className="btn btn-ghost btn-large">Read the docs</button>
            </div>
            <p className="hero-disclaimer animate-fade-up delay-300">No credit card required. Cancel anytime.</p>
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

        {/* Features */}
        <section id="features" className="features">
          <div className="container">
            <div className="section-header">
              <h2 className="section-title">Everything connected. Nothing lost.</h2>
              <p className="section-subtitle">
                Stop forcing your team to update tracking tools manually. FlowSync listens to where work actually happens.
              </p>
            </div>
            <div className="features-grid">
              {features.map((f) => (
                <article className="feature-card" key={f.title}>
                  <div className="feature-icon">{f.icon}</div>
                  <h3 className="feature-title">{f.title}</h3>
                  <p className="feature-description">{f.description}</p>
                  <a href={`#feature-${f.title.toLowerCase().replace(/\s/g, '-')}`} className="feature-link">
                    Explore feature
                  </a>
                </article>
              ))}
            </div>
          </div>
        </section>

        {/* Testimonials */}
        <section id="customers" className="testimonials">
          <div className="container">
            <div className="testimonials-grid">
              {testimonials.map((t, i) => (
                <figure className="testimonial-card" key={i}>
                  <blockquote className="testimonial-quote">"{t.quote}"</blockquote>
                  <figcaption className="testimonial-author">
                    <img src={t.avatar} alt={`Avatar of ${t.name}`} className="testimonial-avatar" />
                    <div>
                      <div className="testimonial-name">{t.name}</div>
                      <div className="testimonial-role">{t.role}</div>
                    </div>
                  </figcaption>
                </figure>
              ))}
            </div>
          </div>
        </section>

        {/* CTA */}
        <section className="cta-section">
          <div className="container">
            <h2 className="cta-title">Stop switching tabs.<br/>Start shipping.</h2>
            <p className="cta-subtitle">
              Join the engineering and design teams who have reclaimed their focus.
            </p>
            <div className="hero-actions">
              <button className="btn btn-primary btn-large">Start your 14-day trial</button>
            </div>
          </div>
        </section>
      </main>

      {/* Footer */}
      <footer className="footer">
        <div className="container">
          <div className="footer-grid">
            {Object.entries(footerLinks).map(([category, links]) => (
              <div className="footer-column" key={category}>
                <h4 className="footer-heading">{category}</h4>
                <ul className="footer-links">
                  {links.map((link) => (
                    <li key={link}><a href={`#${link.toLowerCase().replace(/\s/g, '-')}`}>{link}</a></li>
                  ))}
                </ul>
              </div>
            ))}
          </div>
          <div className="footer-bottom">
            <p>© 2026 FlowSync, Inc. All rights reserved.</p>
            <p>Designed for clarity.</p>
          </div>
        </div>
      </footer>
    </div>
  );
}