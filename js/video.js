// Display custom canvas. In this case it's a blue, 5 pixel 
// border that resizes along with the browser window.
function redraw(context) {
    context.strokeStyle = 'red';
    context.lineWidth = '5';
    context.strokeRect(0, 0, window.innerWidth, window.innerHeight);
}

// Runs each time the DOM window resize event fires.
// Resets the canvas dimensions to match window,
// then draws the new borders accordingly.
function resizeCanvas(htmlCanvas, context) {
    htmlCanvas.width = window.innerWidth;
    htmlCanvas.height = window.innerHeight;
    redraw(context);
}

function initialize(htmlCanvas, context) {
    // Register an event listener to call the resizeCanvas() function 
    // each time the window is resized.
    window.addEventListener('resize', resizeCanvas, false);
    // Draw canvas border for the first time.
    resizeCanvas(htmlCanvas, context);
}

function drawVideo(){
	requestAnimationFrame(drawVideo);
	// If the video is paused or finished do nothing and continue
	if(video.paused || video.ended){return;}
	// Draw on canvas
	context.drawImage(video, 0, 0, htmlCanvas.width, htmlCanvas.height)
}

function main() {
    var
        // Obtain a reference to the canvas element using its id.
        htmlCanvas = document.getElementById('canvas'),
        // Obtain a graphics context on the canvas element for drawing.
        context = htmlCanvas.getContext('2d'),
        // Obtain a reference to the video element using its id.
        video = document.getElementById('video');

    // Start listening to resize events and draw canvas.
    initialize(htmlCanvas, context);

    video.addEventListener(
    	"play", //if the video is playing
    	()=>{
    		drawVideo(video, context, htmlCanvas.width, htmlCanvas.height);
    	},
    	false
    );
}

main();