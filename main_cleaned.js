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
            updateProgress();    // 2. IntersectionObserver for Reveal Animations

    const observerOptions = {
        root: null,
        rootMargin: '0px 0px -10% 0px',
        threshold: 0.15
    };

    const revealObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach((entry, i) => {
            if (entry.isIntersecting) {
                // Stagger delay based on node index if they enter at the same time
                entry.target.style.transitionDelay = `${i * 100}ms`;
                entry.target.classList.add('visible');
                observer.unobserve(entry.target);
            }    // 3. Active nav link highlighting based on scroll

    const sections = document.querySelectorAll('section[id]');
    const navLinks = document.querySelectorAll('.nav-links .nav-link');

    const sectionObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const id = entry.target.getAttribute('id');
                navLinks.forEach(link => {
                    link.classList.remove('active');
                    if (link.getAttribute('href') === `#${id}`) {
                        link.classList.add('active');
                    }    // 4. Mobile Hamburger Menu

    const mobileToggle = document.querySelector('.nav-hamburger');
    const navLinksContainer = document.querySelector('.nav-links');

    if (mobileToggle) {
        mobileToggle.addEventListener('click', () => {
            // Very simple toggle logic for mobile 
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
            }    // 5. 3D Tilt and Spotlight effect for Expertise Cards

    const expertiseItems = document.querySelectorAll('.expertise-item');
    
    expertiseItems.forEach(item => {
        item.addEventListener('mousemove', (e) => {
            const rect = item.getBoundingClientRect();
            const x = e.clientX - rect.left; // x position within the element
            const y = e.clientY - rect.top;  // y position within the element
            
            // Set CSS variables for the spotlight effect
            item.style.setProperty('--mouse-x', `${x}px`);
            item.style.setProperty('--mouse-y', `${y}px`);
            
            // Calculate tilt
            const centerX = rect.width / 2;
            const centerY = rect.height / 2;
            
            // Rotate max 8 degrees
            const rotateX = ((y - centerY) / centerY) * -8;
            const rotateY = ((x - centerX) / centerX) * 8;
            
            item.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) scale3d(1.02, 1.02, 1.02)`;    // 6. GSAP Cinematic Hero → About Transition

    // =========================================
    if (typeof gsap !== 'undefined' && typeof ScrollTrigger !== 'undefined') {
        gsap.registerPlugin(ScrollTrigger);

        // Respect prefers-reduced-motion
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
            const navbarHeight = 72; // matches --navbar-height

            // Create the cinematic timeline — total duration = 1.0
            const heroTimeline = gsap.timeline({
                scrollTrigger: {
                    trigger: heroSection,
                    start: 'bottom bottom',
                    end: '+=100%',
                    pin: true,
                    scrub: 1,
                    pinSpacing: true,
                    onEnter: () => {
                        progressLine.style.opacity = '1';
                    },
                    onLeaveBack: () => {
                        progressLine.style.opacity = '0';
                    },
                    onLeave: () => {
                        progressLine.style.opacity = '0';
                    }
                }    // 7. GSAP Cinematic Stacked Cards for Projects

        // ==========================================
        const projectCards = gsap.utils.toArray('.project-band');
        
        projectCards.forEach((card, index) => {
            // We scale down the current card as the next one scrolls over it
            if (index < projectCards.length - 1) {
                gsap.to(card, {
                    scale: 0.94,
                    filter: "blur(2px)",
                    opacity: 0.6,
                    scrollTrigger: {
                        trigger: projectCards[index + 1],
                        start: "top 80%", // When next card is 80% down the screen
                        end: "top 72px", // When next card hits its sticky point (navbar)
                        scrub: true,
                    }    // 9. Custom Cursor

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
    }    // 10. Parallax Effect for Work Bands

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

});

            // ==========================================
            // PHASE 1: Zoom + Blur + Darken (0 → 0.6)
            // Hero stays visible, builds cinematic tension
            // ==========================================

            // Hero content zooms in (scale 1 → 1.15)
            if (heroPortfolioText) {
                heroTimeline.fromTo(heroPortfolioText,
                    { scale: 1, filter: 'blur(0px)' },
                    { scale: 1.15, filter: 'blur(6px)', ease: 'power1.in', duration: 0.6 },
                    0
                );
            }
            if (heroPortrait) {
                heroTimeline.fromTo(heroPortrait,
                    { scale: 1, filter: 'blur(0px)' },
                    { scale: 1.15, filter: 'blur(6px)', ease: 'power1.in', duration: 0.6 },
                    0
                );
            }

            // Dark overlay fades in (0 → 0.7)
            heroTimeline.fromTo(heroOverlay,
                { opacity: 0 },
                { opacity: 0.7, ease: 'power1.in', duration: 0.6 },
                0
            );

            // Hero bottom elements fade out quickly (0 → 0.2)
            if (heroBottomLeft) {
                heroTimeline.to(heroBottomLeft, { opacity: 0, duration: 0.15 }, 0);
            }
            if (heroBottomRight) {
                heroTimeline.to(heroBottomRight, { opacity: 0, duration: 0.15 }, 0);
            }
            if (heroLeftText) {
                heroTimeline.to(heroLeftText, { opacity: 0, filter: 'blur(4px)', duration: 0.25 }, 0);
            }
            if (heroRightCta) {
                heroTimeline.to(heroRightCta, { opacity: 0, filter: 'blur(4px)', duration: 0.25 }, 0);
            }

            // ==========================================
            // PHASE 2: Hero slides up, About revealed (0.6 → 1.0)
            // ==========================================

            // Hero section slides up off-screen
            heroTimeline.to(heroSection,
                { yPercent: -100, ease: 'power2.inOut', duration: 0.4 },
                0.6
            );

            // About section is in normal document flow below hero.
            // When hero slides up, about naturally comes into view.
            // We ensure about has proper z-index during transition.
            heroTimeline.fromTo(aboutSection,
                { opacity: 0.5 },
                { opacity: 1, ease: 'power1.out', duration: 0.3 },
                0.65
            );

            // Progress indicator across the full timeline (0% → 100%)
            heroTimeline.fromTo(progressLine,
                { width: '0%' },
                { width: '100%', ease: 'none', duration: 1.0 },
                0
            );
        }

        // ==========================================
});
