particlesJS("particles-js", {
  particles: {
    number: { value: 60 },
    color: { value: "#1abc9c" },
    shape: { type: "circle" },
    opacity: { value: 0.4 },
    size: { value: 3 },
    line_linked: {
      enable: true,
      distance: 150,
      color: "#9adbd0",
      opacity: 0.4
    },
    move: { enable: true, speed: 2 }
  },
  interactivity: {
    events: {
      onhover: { enable: true, mode: "grab" }
    }
  },
  retina_detect: true
});
