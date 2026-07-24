// Highlights the current heading in the sidebar TOC as you scroll
const headings = Array.from(document.querySelectorAll('.post-body h2, .post-body h3'));
const links = Array.from(document.querySelectorAll('#toc a'));
const linkFor = id => links.find(a => a.getAttribute('href') === '#' + id);

const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    const link = linkFor(entry.target.id);
    if (!link) return;
    if (entry.isIntersecting) {
      links.forEach(l => l.classList.remove('active'));
      link.classList.add('active');
    }
  });
}, { rootMargin: '0px 0px -70% 0px' });

headings.forEach(h => observer.observe(h));
