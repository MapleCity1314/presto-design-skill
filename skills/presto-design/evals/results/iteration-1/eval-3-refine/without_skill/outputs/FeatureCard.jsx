// FeatureCard.jsx
export function FeatureCard({ icon, title, description }) {
  return (
    <div style={{
      background: 'linear-gradient(145deg, #ffffff 0%, #f8f7ff 100%)',
      border: '1px solid rgba(124, 101, 246, 0.15)',
      borderRadius: '16px',
      padding: '32px',
      boxShadow: '0 2px 4px rgba(0,0,0,0.04), 0 8px 24px rgba(124, 101, 246, 0.08)',
      transition: 'box-shadow 0.2s ease, transform 0.2s ease',
    }}>
      <div style={{
        fontSize: '40px',
        marginBottom: '20px',
        width: '64px',
        height: '64px',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        background: 'linear-gradient(135deg, #ede9fe 0%, #ddd6fe 100%)',
        borderRadius: '14px',
      }}>
        {icon}
      </div>
      <h3 style={{
        fontFamily: '"Fraunces", "Georgia", serif',
        fontSize: '21px',
        fontWeight: '700',
        color: '#1a1523',
        marginBottom: '10px',
        letterSpacing: '-0.02em',
        lineHeight: '1.3',
      }}>
        {title}
      </h3>
      <p style={{
        fontFamily: '"DM Sans", "Inter", sans-serif',
        fontSize: '15px',
        color: '#6b5f7a',
        lineHeight: '1.7',
        fontWeight: '400',
        letterSpacing: '0.01em',
      }}>
        {description}
      </p>
    </div>
  )
}
