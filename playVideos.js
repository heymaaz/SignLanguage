document.addEventListener('DOMContentLoaded', function() {
    const videos = [
        'bmffabtttc', 'gilpbn5szf', 'nhy18vfspa', 'islnti0all', 'i4ovggtyvx'
    ];
    let currentVideoIndex = 0;

    function removeUnwantedElements() {
        const videoContainer = document.getElementById('videoContainer');
        const embeds = videoContainer.querySelectorAll('.signbsldata-embed');

        embeds.forEach(embed => {
            // Remove all non-video elements
            Array.from(embed.children).forEach(child => {
                if (!child.querySelector('video')) {
                    child.style.display = 'none';
                }
            });

            // Adjust the video element style if needed
            const videoElem = embed.querySelector('video');
            if (videoElem) {
                videoElem.style.width = '100%';
            }
        });
    }

    function loadVideo(videoId) {
        const videoContainer = document.getElementById('videoContainer');
        videoContainer.innerHTML = `<blockquote class="signbsldata-embed" data-vidref="${videoId}"></blockquote>`;

        // Reload the script to render the video
        const script = document.createElement('script');
        script.src = "https://embed.signbsl.com/widgets.js";
        script.async = true;
        script.onload = () => setTimeout(removeUnwantedElements, 2000); // Wait for the video to render before cleaning
        document.body.appendChild(script);
    }

    function playNextVideo() {
        if (currentVideoIndex < videos.length) {
            loadVideo(videos[currentVideoIndex]);
            currentVideoIndex++;
        } else {
            console.log('All videos played.');
        }
    }

    playNextVideo(); // Play the first video

    // Optionally, set up an interval or event listener to play the next video
    setInterval(() => {
        playNextVideo();
    }, 10000); // Change 10000 to the length of each video in milliseconds
});

/*
document.addEventListener('DOMContentLoaded', function() {
    const videos = [
        'bmffabtttc', 'gilpbn5szf', 'nhy18vfspa', 'islnti0all', 'i4ovggtyvx'
    ];
    let currentVideoIndex = 0;

    function loadVideo(videoId) {
        const videoContainer = document.getElementById('videoContainer');
        videoContainer.innerHTML = `<blockquote class="signbsldata-embed" data-vidref="${videoId}"></blockquote>`;

        // Reload the script to render the video
        const script = document.createElement('script');
        script.src = "https://embed.signbsl.com/widgets.js";
        script.async = true;
        document.body.appendChild(script);
    }

    function playNextVideo() {
        if (currentVideoIndex < videos.length) {
            loadVideo(videos[currentVideoIndex]);
            currentVideoIndex++;
        } else {
            console.log('All videos played.');
        }
    }

    playNextVideo(); // Play the first video

    // Optionally, set up an interval or event listener to play the next video
    setInterval(() => {
        playNextVideo();
    }, 10000); // Change 10000 to the length of each video in milliseconds
});
*/
