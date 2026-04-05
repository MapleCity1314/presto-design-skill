// FeatureCard.jsx
export function FeatureCard({ icon, title, description }) {
  return (
    <div
      className="feature-card"
      style={{
        background: 'var(--surface)',
        border: '1px solid var(--border-tinted)',
        borderRadius: '14px',
        padding: '32px',
        boxShadow: '0 1px 3px oklch(18% 0.012 60 / 0.06), 0 4px 16px oklch(18% 0.012 60 / 0.08)',
        transition: 'transform 200ms cubic-bezier(0.25, 1, 0.5, 1), box-shadow 200ms cubic-bezier(0.25, 1, 0.5, 1)',
        cursor: 'default',
      }}
      onMouseEnter={e => {
        e.currentTarget.style.transform = 'translateY(-2px)';
        e.currentTarget.style.boxShadow =
          '0 2px 6px oklch(18% 0.012 60 / 0.08), 0 8px 28px oklch(18% 0.012 60 / 0.12)';
      }}
      onMouseLeave={e => {
        e.currentTarget.style.transform = 'translateY(0)';
        e.currentTarget.style.boxShadow =
          '0 1px 3px oklch(18% 0.012 60 / 0.06), 0 4px 16px oklch(18% 0.012 60 / 0.08)';
      }}
    >
      <div
        style={{
          fontSize: '40px',
          lineHeight: '1',
          marginBottom: '20px',
          display: 'inline-flex',
          alignItems: 'center',
          justifyContent: 'center',
          width: '56px',
          height: '56px',
          background: 'color-mix(in oklch, var(--accent) 10%, var(--surface))',
          borderRadius: '10px',
        }}
      >
        {icon}
      </div>

      <h3
        style={{
          fontFamily: "'Instrument Serif', Georgia, serif",
          fontSize: '22px',
          fontWeight: '400',
          lineHeight: '1.25',
          color: 'var(--text)',
          marginBottom: '10px',
          textWrap: 'balance',
          letterSpacing: '-0.01em',
        }}
      >
        {title}
      </h3>

      <p
        style={{
          fontFamily: "'DM Sans', sans-serif",
          fontSize: '15px',
          fontWeight: '400',
          color: 'var(--text-muted)',
          lineHeight: '1.65',
          textWrap: 'pretty',
          maxWidth: '52ch',
        }}
      >
        {description}
      </p>
    </div>
  );
}
