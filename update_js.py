import re

with open('main.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Debounce scroll
js = js.replace("window.addEventListener('scroll', updateNav);", """
    let scrollTimeout;
    window.addEventListener('scroll', () => {
        if (scrollTimeout) {
            window.cancelAnimationFrame(scrollTimeout);
        }
        scrollTimeout = window.requestAnimationFrame(() => {
            updateNav();
            updateProgress();
        });
    });
""")

js = js.replace("window.addEventListener('scroll', updateProgress);", "// Handled in debounced scroll listener")

# Custom cursor and Parallax logic
cursor_js = """
    // 9. Custom Cursor
    const cursor = document.getElementById('custom-cursor');
    if (cursor) {
        document.addEventListener('mousemove', (e) => {
            cursor.style.transform = `translate(${e.clientX}px, ${e.clientY}px) translate(-50%, -50%)`;
        });

        const hoverElements = document.querySelectorAll('a, button, .hover-name');
        hoverElements.forEach(el => {
            el.addEventListener('mouseenter', () => cursor.classList.add('hovering'));
            el.addEventListener('mouseleave', () => cursor.classList.remove('hovering'));
        });
    }

    // 10. Parallax Effect for Work Bands
    const parallaxImages = document.querySelectorAll('.parallax-img');
    const parallaxScroll = () => {
        parallaxImages.forEach(img => {
            const rect = img.parentElement.getBoundingClientRect();
            // Check if in viewport and on desktop
            if (rect.top < window.innerHeight && rect.bottom > 0 && window.innerWidth > 768) {
                const scrollPos = window.innerHeight - rect.top;
                const shift = scrollPos * 0.15;
                img.style.transform = `translateY(${-shift}px) scale(1.05)`;
            } else {
                img.style.transform = ''; // reset on mobile or when not scrolling
            }
        });
    };
    window.addEventListener('scroll', () => {
        window.requestAnimationFrame(parallaxScroll);
    });
    // Initial call
    parallaxScroll();
"""

if 'const cursor =' not in js:
    js = js.replace("});", cursor_js + "\n});")

# Fix form submit loading state
submit_logic = """
        contactSubmit.addEventListener('click', (e) => {
            e.preventDefault();
            const name = document.getElementById('contact-name').value;
            const email = document.getElementById('contact-email').value;
            
            if(name && email) {
                contactSubmit.classList.add('loading');
                contactSubmit.innerHTML = 'Sending<span class="loading-dots"></span>';
                
                setTimeout(() => {
                    contactSubmit.classList.remove('loading');
                    contactSubmit.style.display = 'none';
                    contactSuccess.style.display = 'block';
                }, 1500);
            } else {
                alert("Please fill in at least your name and email.");
            }
        });
"""

js = re.sub(r"contactSubmit\.addEventListener\('click', \(e\) => \{.*?\n        \}\);", submit_logic.strip(), js, flags=re.DOTALL)

with open('main.js', 'w', encoding='utf-8') as f:
    f.write(js)
