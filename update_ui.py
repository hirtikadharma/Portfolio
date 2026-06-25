import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Remove nav-logo
html = re.sub(r'<div class="nav-logo">.*?</div>', '', html, flags=re.DOTALL)

# 2. Remove Sign In
html = re.sub(r'<a href="#" class="nav-signin">Sign In</a>', '', html)

# 3. Replace Get Started with Contact Me
html = html.replace('Get Started &rarr;', 'Contact Me &rarr;')

# 4. Remove nav-active-dot
html = html.replace('<span class="nav-active-dot"></span>', '')

# 5. Make designation look like the image (icon + stacked text)
hero_info_original = """<div class="hero-info hero-anim-info">
                        <div class="role-badge">UI/UX Designer & Frontend Developer</div>
                        <div class="hero-social">
                            <a href="https://linkedin.com/in/hirtika-dharma" target="_blank" rel="noopener noreferrer">LinkedIn &middot;</a>
                            <span class="hero-location">Navi Mumbai, India &middot; Available for opportunities</span>
                        </div>
                    </div>"""

hero_info_new = """<div class="hero-info hero-anim-info" style="display: flex; align-items: center; gap: 16px;">
                        <div style="font-size: 40px; background: rgba(212,184,74,0.1); border-radius: 12px; padding: 12px; display: flex; align-items: center; justify-content: center;">👩‍💻</div>
                        <div style="display: flex; flex-direction: column;">
                            <div class="role-badge" style="border: none; padding: 0; background: transparent; font-size: 20px; font-weight: 700; line-height: 1.2; color: var(--color-text-primary); text-align: left; font-family: var(--font-body);">UI/UX Designer<br>& Frontend Developer</div>
                        </div>
                    </div>"""

if 'class="role-badge">UI/UX Designer' in html:
    html = html.replace(hero_info_original, hero_info_new)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)


with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Nav centering
css = css.replace('.nav-container {\n  display: flex;\n  justify-content: space-between;\n  align-items: center;\n  height: 100%;\n}', 
""".nav-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100%;
  position: relative;
}""")

css = css.replace('.nav-links {\n  display: flex;\n  gap: 32px;\n  align-items: center;\n}',
""".nav-links {
  display: flex;
  gap: 32px;
  align-items: center;
  margin: 0 auto;
}""")

css = css.replace('.nav-actions {\n  display: flex;\n  gap: 16px;\n  align-items: center;\n}',
""".nav-actions {
  display: flex;
  gap: 16px;
  align-items: center;
  position: absolute;
  right: var(--container-pad);
}""")

# Name size reduction
# Find .hero-name-left, .hero-name-right and the font-size clamp
css = re.sub(r'font-size: var\(--text-hero\);', 'font-size: clamp(40px, 8vw, 100px);', css)

css = css.replace("""@media (max-width: 1279px) {
  .hero-name-left, .hero-name-right {
    font-size: clamp(48px, 8vw, 96px);
  }
}

@media (min-width: 1280px) {
  .hero-name-left, .hero-name-right {
    font-size: 120px;
  }""", """@media (max-width: 1279px) {
  .hero-name-left, .hero-name-right {
    font-size: clamp(40px, 7vw, 80px);
  }
}

@media (min-width: 1280px) {
  .hero-name-left, .hero-name-right {
    font-size: 96px;
  }""")

# Portrait rectangle with 20px rounded corners
css = css.replace('.hero-portrait-wrap {\n  width: 400px;\n  height: 400px;\n  border-radius: 50%;',
""".hero-portrait-wrap {
  width: 400px;
  height: 440px;
  border-radius: 20px;""")

css = css.replace('.hero-portrait {\n  width: 100%;\n  height: 100%;\n  object-fit: cover;\n  border-radius: 50%;',
""".hero-portrait {
  width: 100%;
  height: 100%;
  object-fit: cover;
  border-radius: 20px;""")

# Hero active dot remove
css = re.sub(r'\.nav-active-dot \{.*?\}', '', css, flags=re.DOTALL)
css = re.sub(r'\.nav-link\.active \.nav-active-dot \{.*?\}', '', css, flags=re.DOTALL)


with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)
