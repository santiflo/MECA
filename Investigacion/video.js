const canvas = document.querySelector('canvas');
const video = document.querySelector('video');
const fps = 60;
const width = 1280;
const height = 720;
const canvasInterval = null;

drawImage() {
  canvas.getContext('2d', { alpha: false }).drawImage(video, 0, 0, width, height);
}

canvasInterval = window.setInterval(() => {
  drawImage(video);
}, 1000 / fps);

video.onpause = function() {
  clearInterval(canvasInterval);
};

video.onended = function() {
  clearInterval(canvasInterval);
};

video.onplay = function() {
  clearInterval(canvasInterval);
  canvasInterval = window.setInterval(() => {
    drawImage(video);
  }, 1000 / fps);
};