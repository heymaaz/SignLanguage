document.addEventListener('DOMContentLoaded', function() {
    const videoUrls = [
        'https://www.signbsl.com/sign/science', // Add the URLs for each sign
        // ... other URLs
    ];
    let currentVideoIndex = 0;
    const iframe = document.getElementById('bslFrame');

    function loadVideo(url) {
        iframe.src = url;
    }

    function playNextVideo() {
        if (currentVideoIndex < videoUrls.length) {
            loadVideo(videoUrls[currentVideoIndex]);
            currentVideoIndex++;
        } else {
            console.log('All videos played.');
        }
    }

    playNextVideo(); // Play the first video

    iframe.addEventListener('load', function() {
        // Optionally, move to the next video after a set timeout
        setTimeout(playNextVideo, 10000); // Adjust time as needed
    });
});
