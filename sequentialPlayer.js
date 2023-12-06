document.addEventListener('DOMContentLoaded', function() {
    const videoSources = [
        "https://media.signbsl.com/videos/bsl/signstation/ME.mp4",
        "https://media.signbsl.com/videos/bsl/gpnhs/mp4/professor.mp4",
        "https://media.signbsl.com/videos/bsl/signstation/your.mp4",
        "https://media.signbsl.com/videos/bsl/signstation/computer.mp4",
        "https://media.signbsl.com/videos/bsl/signstation/science.mp4"
        // Add more video URLs here
    ];
    let currentVideoIndex = 0;
    const videoElement = document.getElementById('bslVideo');

    videoElement.muted = true; // Mute the video so browsers don't block autoplay
    videoElement.controls = false; // To hide the browser controls and prevent users from pausing the video

    videoElement.addEventListener('ended', playNextVideo);// Play the next video when the current one ends

    function playNextVideo() {// Play the next video
        if (currentVideoIndex < videoSources.length) {// Check if there are more videos to play
            videoElement.src = videoSources[currentVideoIndex];// Set the video source
            videoElement.play().catch(e => console.error(e));// Play the video
            currentVideoIndex++;// Increment the index
        } else {
            console.log('All videos played.');// Log a message when all videos have been played
        }
    }

    playNextVideo(); // Start the first video on load
});
