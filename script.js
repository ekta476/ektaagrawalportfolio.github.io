/* ═══════════════════════════════════
   script.js — Ekta Portfolio
   ═══════════════════════════════════ */

// ── Navbar scroll effect ─────────────────────────────
const navbar = document.getElementById('navbar');
window.addEventListener('scroll', () => {
  if (window.scrollY > 40) {
    navbar.classList.add('scrolled');
  } else {
    navbar.classList.remove('scrolled');
  }
});

// ── Hamburger menu ────────────────────────────────────
const hamburger = document.getElementById('hamburger');
const navLinks  = document.querySelector('.nav-links');
hamburger.addEventListener('click', () => {
  navLinks.classList.toggle('open');
  hamburger.classList.toggle('active');
});

// Close menu when a link is clicked
navLinks.querySelectorAll('a').forEach(link => {
  link.addEventListener('click', () => {
    navLinks.classList.remove('open');
    hamburger.classList.remove('active');
  });
});

const fadeUpElements = document.querySelectorAll(
  '.work-card, .skill-pill, ' +
  '.cert-item, .contact-card, .about-highlights li, ' +
  '.study-board, .section-header, .resume-card-box, .timeline-item, .exp-item, .resume-skill-item, .resume-avatar-img, .btn-explore, .work-header-wrap, .projects-avatar-img, .projects-deco'
);

fadeUpElements.forEach(el => el.classList.add('fade-up'));

const observer = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry, i) => {
      if (entry.isIntersecting) {
        setTimeout(() => {
          entry.target.classList.add('visible');
        }, i * 60);
        observer.unobserve(entry.target);
      }
    });
  },
  { threshold: 0.1, rootMargin: '0px 0px -40px 0px' }
);

fadeUpElements.forEach(el => observer.observe(el));

// ── Active nav link on scroll ─────────────────────────
const sections = document.querySelectorAll('section[id]');
const navItems = document.querySelectorAll('.nav-links a');

const sectionObserver = new IntersectionObserver(
  (entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        navItems.forEach(link => {
          link.style.color = '';
          if (link.getAttribute('href') === '#' + entry.target.id) {
            link.style.color = 'var(--sage)';
          }
        });
      }
    });
  },
  { threshold: 0.4 }
);

sections.forEach(s => sectionObserver.observe(s));

// ── Skill pill sparkle on hover ───────────────────────
document.querySelectorAll('.skill-pill').forEach(pill => {
  pill.addEventListener('mouseenter', () => {
    pill.style.transition = 'all 0.25s cubic-bezier(0.34, 1.56, 0.64, 1)';
  });
});

// ── Film strip hover animation ────────────────────────
const filmFrames = document.querySelectorAll('.film-frame');
filmFrames.forEach((frame, i) => {
  frame.style.animationDelay = `${i * 0.15}s`;
});

// ── Smooth reveal for hero on page load ───────────────
window.addEventListener('load', () => {
  document.querySelectorAll('.hero-title, .hero-name, .hero-role, .hero-tagline').forEach((el, i) => {
    el.style.opacity = '0';
    el.style.transform = 'translateY(20px)';
    el.style.transition = 'opacity 0.7s ease, transform 0.7s ease';
    setTimeout(() => {
      el.style.opacity = '1';
      el.style.transform = 'translateY(0)';
    }, 200 + i * 150);
  });

  // Animate hero photo frame
  const photoFrame = document.querySelector('.hero-photo-frame');
  if (photoFrame) {
    photoFrame.style.opacity = '0';
    photoFrame.style.transform = 'translateY(16px) scale(0.97)';
    photoFrame.style.transition = 'opacity 0.9s ease, transform 0.9s ease';
    setTimeout(() => {
      photoFrame.style.opacity = '1';
      photoFrame.style.transform = 'translateY(0) scale(1)';
    }, 700);
  }
});

// ── Replace placeholder images with real ones ─────────
// HOW TO USE:
// Once you have your real images, replace placeholder divs with:
//   <img src="images/your-photo.jpg" alt="Description" />
// Or add images directly via JS:
//
// Example:
// document.querySelector('#work-sm .work-card-img').innerHTML =
//   '<img src="images/client-social.jpg" alt="Client Social Media" />';

console.log('%c✨ Ekta Portfolio Loaded!', 'color: #8B9E7E; font-size: 1.1rem; font-weight: bold;');
console.log('%cTo add your images: replace placeholder divs with <img> tags in index.html', 'color: #7A5C4A;');
