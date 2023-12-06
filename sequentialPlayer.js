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

    videoElement.muted = true; // Mute the video
    videoElement.controls = false; // Optionally hide controls initially

    videoElement.addEventListener('ended', playNextVideo);

    function playNextVideo() {
        if (currentVideoIndex < videoSources.length) {
            videoElement.src = videoSources[currentVideoIndex];
            videoElement.play().catch(e => console.error(e));
            currentVideoIndex++;
        } else {
            console.log('All videos played.');
        }
    }

    playNextVideo(); // Start the first video on load
});
