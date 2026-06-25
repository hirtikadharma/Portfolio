with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Update text-secondary for WCAG
css = css.replace('--color-text-secondary: #5A5A5A;', '--color-text-secondary: #4A4A4A;')

# 2. Add base accessibility classes and focus-visible before /* Global Utilities */
acc_css = """
*:focus-visible {
  outline: 2px solid var(--color-accent);
  outline-offset: 3px;
}

input:focus, textarea:focus, button:focus {
  outline: none;
}

input:focus-visible, textarea:focus-visible, button:focus-visible {
  outline: 2px solid var(--color-accent);
  outline-offset: 3px;
}

.skip-link {
  position: absolute;
  top: -40px;
  left: 0;
  background: var(--color-accent);
  color: #1A1A1A;
  padding: 8px 16px;
  z-index: 99999;
  font-weight: bold;
  transition: top var(--transition-fast);
}

.skip-link:focus {
  top: 0;
}

.visually-hidden {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  padding: 0;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  border: 0;
}

#custom-cursor {
  position: fixed;
  top: 0;
  left: 0;
  width: 12px;
  height: 12px;
  background-color: var(--color-accent);
  border-radius: 50%;
  opacity: 0.7;
  pointer-events: none;
  z-index: 9999;
  transition: width 0.2s ease, height 0.2s ease, opacity 0.2s ease;
  transform: translate(-50%, -50%);
  display: none;
}

@media (pointer: fine) {
  #custom-cursor {
    display: block;
  }
}

#custom-cursor.hovering {
  width: 32px;
  height: 32px;
  opacity: 0.3;
}

"""
if '.skip-link {' not in css:
    css = css.replace('/* Global Utilities */', acc_css + '/* Global Utilities */')

# 3. Add section-watermark and relative-content
watermark_css = """
.section-watermark {
  position: absolute;
  top: 0;
  right: var(--container-pad);
  font-family: var(--font-display);
  font-weight: 900;
  font-size: 200px;
  color: rgba(26,26,26,0.03);
  z-index: 0;
  line-height: 1;
  pointer-events: none;
}

.relative-content {
  position: relative;
  z-index: 1;
}

"""
if '.section-watermark {' not in css:
    css = css.replace('.reveal {', watermark_css + '.reveal {')

# 4. Will-change to reveal
css = css.replace('transition: opacity var(--transition-slow), transform var(--transition-slow);', 'transition: opacity var(--transition-slow), transform var(--transition-slow);\n  will-change: transform, opacity;')

# 5. Nav active dot
dot_css = """
.nav-active-dot {
  position: absolute;
  bottom: -8px;
  left: 50%;
  transform: translateX(-50%) scale(0);
  width: 6px;
  height: 6px;
  background-color: var(--color-accent);
  border-radius: 50%;
  transition: transform var(--transition-medium);
}

.nav-link.active .nav-active-dot {
  transform: translateX(-50%) scale(1);
}
"""
if '.nav-active-dot {' not in css:
    css = css.replace('.nav-link:hover::after, .nav-link.active::after {\n  transform: scaleX(1);\n}', '.nav-link:hover::after, .nav-link.active::after {\n  transform: scaleX(1);\n}\n' + dot_css)

# 6. Hero name hover
hover_name_css = """
  transition: letter-spacing 0.4s ease, color 0.4s ease;
}

.hover-name:hover {
  letter-spacing: 0em;
  color: rgba(26,26,26,0.8);
}
"""
if '.hover-name:hover' not in css:
    css = css.replace('white-space: nowrap;\n}', 'white-space: nowrap;\n' + hover_name_css)

# 7. Scroll progress transition
if 'transition: width 0.1s linear;' not in css:
    css = css.replace('width: 0%;\n}', 'width: 0%;\n  transition: width 0.1s linear;\n}')

# 8. Parallax will-change
if 'will-change: transform;\n}' not in css:
    css = css.replace('transition: transform 0.5s ease;\n}', 'transition: transform 0.5s ease;\n  will-change: transform;\n}')

# 9. Button loading state
loading_css = """
.btn-submit.loading {
  pointer-events: none;
  opacity: 0.9;
}

.loading-dots::after {
  content: "";
  animation: dots 1.5s infinite steps(4, end);
}

@keyframes dots {
  0%, 20% { content: ""; }
  40% { content: "."; }
  60% { content: ".."; }
  80%, 100% { content: "..."; }
}
"""
if '.btn-submit.loading' not in css:
    css = css.replace('.btn-submit:hover {\n  background-color: var(--color-accent-hover);\n  transform: scale(1.02);\n}', '.btn-submit:hover {\n  background-color: var(--color-accent-hover);\n  transform: scale(1.02);\n}\n' + loading_css)

# 10. Footer CSS
footer_css = """
/* =========================================
   SECTION: FOOTER
   ========================================= */
.site-footer {
  position: relative;
  z-index: 2;
}

.footer-dark {
  background-color: var(--color-bg-dark);
  padding: var(--space-xl) 0;
}

.footer-grid {
  display: grid;
  grid-template-columns: repeat(5, minmax(0, 1fr));
  gap: 48px;
}

.footer-brand {
  grid-column: span 1;
}

.footer-logo {
  font-family: var(--font-display);
  font-weight: 700;
  font-size: 28px;
  color: #ffffff;
}

.footer-tagline {
  font-family: var(--font-body);
  font-weight: 300;
  font-size: 14px;
  color: rgba(255,255,255,0.5);
  margin-top: 8px;
  font-style: italic;
}

.footer-bio {
  font-family: var(--font-body);
  font-size: 13px;
  color: rgba(255,255,255,0.4);
  line-height: 1.7;
  margin-top: 16px;
  max-width: 200px;
}

.footer-socials {
  display: flex;
  gap: 12px;
  margin-top: 24px;
}

.social-icon {
  width: 36px;
  height: 36px;
  border-radius: 50%;
  border: 1px solid rgba(255,255,255,0.15);
  display: flex;
  justify-content: center;
  align-items: center;
  font-family: var(--font-body);
  font-weight: 600;
  font-size: 11px;
  color: rgba(255,255,255,0.5);
  transition: all var(--transition-fast);
}

.social-icon:hover {
  border-color: var(--color-accent);
  color: var(--color-accent);
}

.footer-heading {
  font-family: var(--font-body);
  font-size: 11px;
  text-transform: uppercase;
  letter-spacing: 0.12em;
  color: rgba(255,255,255,0.3);
  margin-bottom: 20px;
}

.footer-link {
  display: block;
  font-family: var(--font-body);
  font-size: 14px;
  color: rgba(255,255,255,0.6);
  margin-bottom: 12px;
  transition: all var(--transition-fast);
}

.footer-link:hover {
  color: #ffffff;
  transform: translateX(4px);
}

.footer-text {
  font-family: var(--font-body);
  font-size: 14px;
  color: rgba(255,255,255,0.6);
  margin-bottom: 12px;
}

.status-indicator {
  font-family: var(--font-body);
  font-size: 14px;
  color: #ffffff;
  font-weight: 500;
  margin-bottom: 8px;
  display: flex;
  align-items: center;
}

.status-dot {
  width: 8px;
  height: 8px;
  background-color: #4ade80;
  border-radius: 50%;
  display: inline-block;
  margin-right: 8px;
}

.status-text {
  font-family: var(--font-body);
  font-size: 13px;
  color: rgba(255,255,255,0.5);
  line-height: 1.6;
  margin-bottom: 24px;
}

.btn-hire {
  display: inline-block;
  border: 1px solid rgba(255,255,255,0.2);
  color: #ffffff;
  padding: 10px 22px;
  border-radius: var(--radius-full);
  font-family: var(--font-body);
  font-size: 13px;
  font-weight: 500;
  transition: all var(--transition-fast);
}

.btn-hire:hover {
  background-color: var(--color-accent);
  border-color: var(--color-accent);
  color: #1A1A1A;
}

.footer-bottom {
  background-color: rgba(255,255,255,0.04);
  border-top: 1px solid var(--color-border-dark);
  padding: 20px 0;
}

.footer-bottom-flex {
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 16px;
  font-family: var(--font-body);
  font-size: 12px;
  color: rgba(255,255,255,0.25);
}

"""
if '.site-footer {' not in css:
    css = css + footer_css

# Responsive overrides
responsive_fixes = """
/* Responsive Audit Overrides */
@media (max-width: 1279px) {
  .hero-name-left, .hero-name-right {
    font-size: clamp(48px, 8vw, 96px);
  }
}

@media (min-width: 1280px) {
  .hero-name-left, .hero-name-right {
    font-size: 120px;
  }
  .work-band-desc {
    max-width: 520px;
  }
}

@media (min-width: 769px) {
  .about-columns, .skills-columns, .contact-columns {
    display: grid;
    grid-template-columns: minmax(0, 1fr) minmax(0, 1fr);
  }
  .skills-columns { grid-template-columns: 6fr 4fr; display: grid; }
  .contact-columns { grid-template-columns: 55fr 45fr; display: grid; }
  .skills-col-left, .skills-col-right, .contact-col-left, .contact-col-right { flex: none; grid-column: span 1; }
}

@media (max-width: 768px) {
  .footer-grid {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }
  
  .footer-brand {
    grid-column: span 2;
  }
  
  .footer-bottom-flex {
    flex-direction: column;
    text-align: center;
  }
}

@media (max-width: 480px) {
  .hero-grid {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 16px;
  }
  .hero-name-left, .hero-name-right {
    font-size: clamp(48px, 14vw, 72px);
    text-align: center;
    width: 100%;
  }
  .hero-portrait-wrap {
    order: 2; 
    margin: 0;
  }
  .hero-name-left { order: 1; }
  .hero-name-right { order: 3; }
  
  .hero-stats {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 24px;
    width: 100%;
  }
  
  .stat-item {
    width: 100%;
    margin-bottom: 0;
  }
  
  .hero-bio {
    font-size: 14px;
    padding: 0 16px;
    align-self: center;
    text-align: center;
  }
}
"""
if '/* Responsive Audit Overrides */' not in css:
    css = css + responsive_fixes

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)
