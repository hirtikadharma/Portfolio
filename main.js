document.addEventListener('DOMContentLoaded', () => {

    // 1. Navigation Scroll Behavior
    const nav = document.getElementById('nav');
    const updateNav = () => {
        if (window.scrollY > 40) {
            nav.classList.add('scrolled');
        } else {
            nav.classList.remove('scrolled');
        }
    };

    let scrollTimeout;
    window.addEventListener('scroll', () => {
        if (scrollTimeout) {
            window.cancelAnimationFrame(scrollTimeout);
        }
        scrollTimeout = window.requestAnimationFrame(() => {
            updateNav();
        });
    });

    // 2. IntersectionObserver for Reveal Animations
    const observerOptions = {
        root: null,
        rootMargin: '0px 0px -10% 0px',
        threshold: 0.15
    };

    const revealObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach((entry, i) => {
            if (entry.isIntersecting) {
                entry.target.style.transitionDelay = `${i * 100}ms`;
                entry.target.classList.add('visible');
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    document.querySelectorAll('.reveal').forEach(el => {
        revealObserver.observe(el);
    });

    // 2.2 Text Scramble Animation
    const letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    document.querySelectorAll('.scramble-text').forEach(el => {
        let iterations = 0;
        const originalText = el.getAttribute('data-text');

        const rect = el.getBoundingClientRect();
        el.style.display = 'inline-block';
        el.style.width = rect.width + 'px';

        const interval = setInterval(() => {
            el.innerText = originalText.split("").map((letter, index) => {
                if (index < Math.floor(iterations)) {
                    return originalText[index];
                }
                return letters[Math.floor(Math.random() * 26)];
            }).join("");

            if (iterations >= originalText.length) {
                clearInterval(interval);
                el.innerText = originalText;
                el.style.width = '';
            }
            iterations += 1 / 4;
        }, 30);
    });

    // 2.5 Number Scramble Animation for Stats
    const scrambleNumber = (el, duration) => {
        const digits = "0123456789";
        const originalText = el.getAttribute('data-original') || el.innerText;
        el.setAttribute('data-original', originalText);

        const totalFrames = duration / 60;
        let frame = 0;

        const rect = el.getBoundingClientRect();
        el.style.display = 'inline-block';
        el.style.minWidth = rect.width + 'px';

        const interval = setInterval(() => {
            frame++;
            const progress = frame / totalFrames;

            el.innerText = originalText.split("").map((char, index) => {
                if (char === '.' || char === '+' || char === ',') return char;
                if (index < Math.floor(progress * originalText.length)) {
                    return originalText[index];
                }
                return digits[Math.floor(Math.random() * 10)];
            }).join("");

            if (frame >= totalFrames) {
                clearInterval(interval);
                el.innerText = originalText;
                el.style.minWidth = '';
            }
        }, 60);
    };

    const statsObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const statNums = entry.target.querySelectorAll('.hero-stat-num');
                statNums.forEach(stat => {
                    setTimeout(() => scrambleNumber(stat, 1500), Math.random() * 300);
                });
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.1 });

    const heroStats = document.querySelector('.hero-bottom-row');
    if (heroStats) {
        statsObserver.observe(heroStats);
    }

    // 3. Active nav link highlighting based on scroll position
    const sections = document.querySelectorAll('section[id]');
    const navLinks = document.querySelectorAll('.nav-links .nav-link');

    const updateActiveNav = () => {
        const scrollPos = window.scrollY + 150; // offset for navbar + some buffer
        let currentSection = '';

        sections.forEach(section => {
            const sectionTop = section.offsetTop;
            const sectionHeight = section.offsetHeight;
            if (scrollPos >= sectionTop && scrollPos < sectionTop + sectionHeight) {
                currentSection = section.getAttribute('id');
            }
        });

        // If we're near the top of the page, default to hero
        if (window.scrollY < 100) {
            currentSection = 'hero';
        }

        if (currentSection) {
            navLinks.forEach(link => {
                link.classList.remove('active');
                if (link.getAttribute('href') === `#${currentSection}`) {
                    link.classList.add('active');
                }
            });
        }
    };

    window.addEventListener('scroll', () => {
        window.requestAnimationFrame(updateActiveNav);
    });
    updateActiveNav(); // Set initial state

    // 4. Mobile Hamburger Menu
    const mobileToggle = document.querySelector('.nav-hamburger');
    const navLinksContainer = document.querySelector('.nav-links');

    if (mobileToggle) {
        mobileToggle.addEventListener('click', () => {
            if (navLinksContainer.style.display === 'flex') {
                navLinksContainer.style.display = 'none';
            } else {
                navLinksContainer.style.display = 'flex';
                navLinksContainer.style.flexDirection = 'column';
                navLinksContainer.style.position = 'absolute';
                navLinksContainer.style.top = '72px';
                navLinksContainer.style.left = '0';
                navLinksContainer.style.width = '100%';
                navLinksContainer.style.background = 'var(--color-bg)';
                navLinksContainer.style.padding = '24px 0';
                navLinksContainer.style.gap = '24px';
                navLinksContainer.style.borderBottom = '1px solid var(--color-border)';
            }
        });
    }

    // 5. 3D Tilt and Spotlight effect for Expertise Cards
    const expertiseItems = document.querySelectorAll('.expertise-item');
    expertiseItems.forEach(item => {
        item.addEventListener('mousemove', (e) => {
            const rect = item.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;
            item.style.setProperty('--mouse-x', `${x}px`);
            item.style.setProperty('--mouse-y', `${y}px`);
            const centerX = rect.width / 2;
            const centerY = rect.height / 2;
            const rotateX = ((y - centerY) / centerY) * -8;
            const rotateY = ((x - centerX) / centerX) * 8;
            item.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) scale3d(1.02, 1.02, 1.02)`;
        });
        item.addEventListener('mouseleave', () => {
            item.style.transform = 'perspective(1000px) rotateX(0) rotateY(0) scale3d(1, 1, 1)';
        });
    });

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
            if (rect.top < window.innerHeight && rect.bottom > 0 && window.innerWidth > 768) {
                const scrollPos = window.innerHeight - rect.top;
                const shift = scrollPos * 0.15;
                img.style.transform = `translateY(${-shift}px) scale(1.05)`;
            } else {
                img.style.transform = '';
            }
        });
    };
    window.addEventListener('scroll', () => {
        window.requestAnimationFrame(parallaxScroll);
    });
    parallaxScroll();

    // GSAP Effects
    if (typeof gsap !== 'undefined' && typeof ScrollTrigger !== 'undefined') {
        gsap.registerPlugin(ScrollTrigger);
        const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

        if (!prefersReducedMotion) {
            const heroSection = document.getElementById('hero');
            const aboutSection = document.getElementById('about');
            const heroOverlay = document.querySelector('.hero-dark-overlay');
            const progressLine = document.querySelector('.scroll-progress-line');
            const heroPortfolioText = document.querySelector('.hero-bg-portfolio');
            const heroPortrait = document.querySelector('.hero-portrait-new');
            const heroBottomLeft = document.querySelector('.hero-bottom-left');
            const heroBottomRight = document.querySelector('.hero-bottom-right');
            const heroLeftText = document.querySelector('.hero-left-text');
            const heroRightCta = document.querySelector('.hero-right-cta');

            const heroTimeline = gsap.timeline({
                scrollTrigger: {
                    trigger: heroSection,
                    start: 'bottom bottom',
                    end: '+=100%',
                    pin: true,
                    scrub: 1,
                    pinSpacing: true,
                    onEnter: () => { progressLine.style.opacity = '1'; },
                    onLeaveBack: () => { progressLine.style.opacity = '0'; },
                    onLeave: () => { progressLine.style.opacity = '0'; }
                }
            });

            if (heroPortfolioText) heroTimeline.fromTo(heroPortfolioText, { scale: 1, filter: 'blur(0px)' }, { scale: 1.15, filter: 'blur(6px)', ease: 'power1.in', duration: 0.6 }, 0);
            if (heroPortrait) heroTimeline.fromTo(heroPortrait, { scale: 1, filter: 'blur(0px)' }, { scale: 1.15, filter: 'blur(6px)', ease: 'power1.in', duration: 0.6 }, 0);
            if (heroOverlay) heroTimeline.fromTo(heroOverlay, { opacity: 0 }, { opacity: 0.7, ease: 'power1.in', duration: 0.6 }, 0);
            if (heroBottomLeft) heroTimeline.to(heroBottomLeft, { opacity: 0, duration: 0.15 }, 0);
            if (heroBottomRight) heroTimeline.to(heroBottomRight, { opacity: 0, duration: 0.15 }, 0);
            if (heroLeftText) heroTimeline.to(heroLeftText, { opacity: 0, filter: 'blur(4px)', duration: 0.25 }, 0);
            if (heroRightCta) heroTimeline.to(heroRightCta, { opacity: 0, filter: 'blur(4px)', duration: 0.25 }, 0);

            if (heroSection) heroTimeline.to(heroSection, { yPercent: -100, ease: 'power2.inOut', duration: 0.4 }, 0.6);
            if (aboutSection) heroTimeline.fromTo(aboutSection, { opacity: 0.5 }, { opacity: 1, ease: 'power1.out', duration: 0.3 }, 0.65);
            if (progressLine) heroTimeline.fromTo(progressLine, { width: '0%' }, { width: '100%', ease: 'none', duration: 1.0 }, 0);

            // Stacked Cards for Projects
            const projectCards = gsap.utils.toArray('.project-band');
            projectCards.forEach((card, index) => {
                if (index < projectCards.length - 1) {
                    gsap.to(card, {
                        scale: 0.94,
                        filter: "blur(2px)",
                        opacity: 0.6,
                        scrollTrigger: {
                            trigger: projectCards[index + 1],
                            start: "top 80%",
                            end: "top 72px",
                            scrub: true,
                        }
                    });
                }
            });
        }
    }
});
