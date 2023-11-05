import { Gradient } from 'gradient.js'


// Call `initGradient` with the selector to your canvas
gradient.initGradient('#gradient-canvas')

// Set the gradient background for the canvas
const canvas = document.getElementById('gradient-canvas');
const ctx = canvas.getContext('2d');
const gradient = ctx.createLinearGradient(0, 0, 0, canvas.height);
gradient.addColorStop(0, 'blue');
gradient.addColorStop(1, 'violet');
ctx.fillStyle = gradient;
ctx.fillRect(0, 0, canvas.width, canvas.height);

// JavaScript code for handling button clicks and other interactions
document.getElementById('startButton').addEventListener('click', function() {
    window.location.href = 'links.html';
});

// Add more JavaScript functionality as needed

