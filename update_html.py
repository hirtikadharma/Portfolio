import re

# Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Add lang="en" and meta tags
html = html.replace('<html lang="en">', '<html lang="en">') # Already has it
if '<link rel="canonical"' not in html:
    html = html.replace('<meta name="description"', '<link rel="canonical" href="https://hirtikadharma.com/">\n    <meta name="description"')
if '<meta property="og:image"' not in html:
    html = html.replace('<meta property="og:description"', '<meta property="og:image" content="/og-image.jpg">\n    <meta property="og:description"')

# Add skip link and cursor
if '<a href="#main-content"' not in html:
    html = html.replace('<body>', '<body>\n    <a href="#main-content" class="skip-link">Skip to main content</a>\n    <div id="custom-cursor"></div>')

# Add main wrapper and aria labels
html = html.replace('<main>', '<main id="main-content">')
html = html.replace('<nav class="site-nav" id="nav">', '<nav class="site-nav" id="nav" aria-label="Main Navigation">')

html = html.replace('<section id="hero" class="section-hero">', '<section id="hero" class="section-hero" aria-label="Hero Section">')
html = html.replace('<section id="about" class="section-about">', '<section id="about" class="section-about" aria-label="About Section">\n            <div class="section-watermark">01</div>')
html = html.replace('<section id="work" class="section-work">', '<section id="work" class="section-work" aria-label="Work Section">\n            <div class="section-watermark">02</div>')
html = html.replace('<section id="skills" class="section-skills">', '<section id="skills" class="section-skills" aria-label="Skills Section">\n            <div class="section-watermark">03</div>')
html = html.replace('<section id="contact" class="section-contact">', '<section id="contact" class="section-contact" aria-label="Contact Section">\n            <div class="section-watermark">04</div>')

# Add relative-content class to containers
html = html.replace('<div class="container about-container">', '<div class="container about-container relative-content">')
html = html.replace('<div class="container work-header-container">', '<div class="container work-header-container relative-content">')
html = html.replace('<div class="work-bands">', '<div class="work-bands relative-content">')
html = html.replace('<div class="container skills-container">', '<div class="container skills-container relative-content">')
html = html.replace('<div class="cta-band">', '<div class="cta-band relative-content">')
html = html.replace('<div class="container contact-container">', '<div class="container contact-container relative-content">')

# Add hover-name to hero names
html = html.replace('class="hero-name-left hero-anim-left"', 'class="hero-name-left hero-anim-left hover-name"')
html = html.replace('class="hero-name-right hero-anim-right"', 'class="hero-name-right hero-anim-right hover-name"')

# Add lazy loading and aspect ratio to images
html = re.sub(r'<img (.*?)>', lambda m: f'<img {m.group(1)} loading="lazy" decoding="async">' if 'loading=' not in m.group(1) else m.group(0), html)

# Add nav-active-dot to links
html = html.replace('>Home</a>', '>Home<span class="nav-active-dot"></span></a>')
html = html.replace('>About</a>', '>About<span class="nav-active-dot"></span></a>')
html = html.replace('>Work</a>', '>Work<span class="nav-active-dot"></span></a>')
html = html.replace('>Skills</a>', '>Skills<span class="nav-active-dot"></span></a>')
html = html.replace('>Contact</a>', '>Contact<span class="nav-active-dot"></span></a>')

# Parallax images
html = html.replace('class="work-band-img"', 'class="work-band-img parallax-img"')

# Add aria labels to buttons
html = html.replace('class="btn-work">View Project &rarr;', 'class="btn-work" aria-label="View Automated Web Data Project">View Project &rarr;')
html = html.replace('class="btn-work">View Case Study &rarr;', 'class="btn-work" aria-label="View Splitter Case Study">View Case Study &rarr;')
html = html.replace('class="btn-work">View on GitHub &rarr;', 'class="btn-work" rel="noopener noreferrer" target="_blank" aria-label="View Malware Detection Project on GitHub">View on GitHub &rarr;')

# Fix contact form inputs
html = html.replace('<input type="text" id="contact-name"', '<label for="contact-name" class="visually-hidden">Full Name</label>\n                                <input type="text" id="contact-name" name="name"')
html = html.replace('<input type="email" id="contact-email"', '<label for="contact-email" class="visually-hidden">Email Address</label>\n                                <input type="email" id="contact-email" name="email"')
html = html.replace('<input type="text" id="contact-subject"', '<label for="contact-subject" class="visually-hidden">Subject</label>\n                            <input type="text" id="contact-subject" name="subject"')
html = html.replace('<textarea id="contact-message"', '<label for="contact-message" class="visually-hidden">Message</label>\n                            <textarea id="contact-message" name="message"')

# Append footer if not present
if 'class="footer-dark"' not in html:
    footer_html = """
    <footer class="site-footer">
        <div class="footer-dark">
            <div class="container footer-grid">
                <div class="footer-col footer-brand">
                    <div class="footer-logo">H<span class="logo-dot">·</span>D</div>
                    <div class="footer-tagline">Design. Code. Inspire.</div>
                    <p class="footer-bio">UI/UX Designer & Frontend Developer passionate about crafting exceptional digital experiences.</p>
                    <div class="footer-socials">
                        <a href="https://linkedin.com/in/hirtika-dharma" target="_blank" rel="noopener noreferrer" class="social-icon" aria-label="LinkedIn">Li</a>
                        <a href="#" target="_blank" rel="noopener noreferrer" class="social-icon" aria-label="Dribbble">Dr</a>
                        <a href="#" target="_blank" rel="noopener noreferrer" class="social-icon" aria-label="GitHub">Gh</a>
                    </div>
                </div>
                
                <div class="footer-col">
                    <div class="footer-heading">Services</div>
                    <a href="#" class="footer-link">UI/UX Design</a>
                    <a href="#" class="footer-link">Frontend Development</a>
                    <a href="#" class="footer-link">AI Design Consulting</a>
                    <a href="#" class="footer-link">Wireframing & Prototyping</a>
                    <a href="#" class="footer-link">Design Systems</a>
                </div>
                
                <div class="footer-col">
                    <div class="footer-heading">Navigation</div>
                    <a href="#hero" class="footer-link">Home</a>
                    <a href="#about" class="footer-link">About</a>
                    <a href="#work" class="footer-link">Work</a>
                    <a href="#skills" class="footer-link">Skills</a>
                    <a href="#contact" class="footer-link">Contact</a>
                </div>
                
                <div class="footer-col">
                    <div class="footer-heading">Contact</div>
                    <div class="footer-text">dharmahirtika@gmail.com</div>
                    <div class="footer-text">+91 9016288070</div>
                    <div class="footer-text">Navi Mumbai, India</div>
                    <a href="https://linkedin.com/in/hirtika-dharma" target="_blank" rel="noopener noreferrer" class="footer-link" style="margin-top: 8px;">linkedin.com/in/hirtika-dharma</a>
                </div>
                
                <div class="footer-col footer-status">
                    <div class="footer-heading">Status</div>
                    <div class="status-indicator">
                        <span class="status-dot"></span> Available for Work
                    </div>
                    <p class="status-text">Open to full-time roles and freelance projects.</p>
                    <a href="#contact" class="btn-hire">Hire Me &rarr;</a>
                </div>
            </div>
        </div>
        
        <div class="footer-bottom">
            <div class="container footer-bottom-flex">
                <div>&copy; 2025 Hirtika Dharma. All rights reserved.</div>
                <div>Made with &hearts; in Navi Mumbai</div>
                <div>Portfolio v1.0</div>
            </div>
        </div>
    </footer>
"""
    html = html.replace('    <footer class="site-footer">\n        <div class="container">\n            <p>Footer (Prompt 4)</p>\n        </div>\n    </footer>', footer_html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
