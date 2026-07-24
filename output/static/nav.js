const toggle = document.getElementById('navToggle');
const sidebar = document.getElementById('sidebar');
const scrim = document.getElementById('scrim');

if (toggle) {
  toggle.addEventListener('click', () => {
    sidebar.classList.toggle('open');
    scrim.classList.toggle('open');
  });
  scrim.addEventListener('click', () => {
    sidebar.classList.remove('open');
    scrim.classList.remove('open');
  });
}

sidebar.querySelectorAll('a').forEach(link => {
  link.addEventListener('click', () => {
    sidebar.classList.remove('open');
    scrim.classList.remove('open');
  });
});
