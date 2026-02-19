// music-player.js
const songs = [
    { id: 'x9rgbYK1Q6E', title: 'In My Defence', artist: 'Freddie Mercury' },
    { id: 'gWz08eyyEBI', title: '【Deemo】Lost In The Nowhere', artist: 'ピアノ' },
    { id: 'WBcKTGdm3xI', title: '我要我們在一起', artist: '蕭閎仁(原唱:范曉萱)' },
];

var player;
var isPlaying = false;

// 【核心：強制渲染列表】
function forceRenderPlaylist() {
    const listContainer = document.getElementById('playlist-items');
    if (!listContainer) {
        console.error("找不到 playlist-items 容器！");
        return;
    }

    listContainer.innerHTML = '';
    // 在 forceRenderPlaylist 函式內的 songs.forEach 區塊：
    songs.forEach((song, index) => {
        const li = document.createElement('li');

        // 設定整列的基本樣式 (包含主要的文字顏色)
        li.style.cssText = "cursor:pointer; padding:12px; border-bottom:1px solid #140505ff; color:white; list-style:none; transition: 0.2s;";

        // 修正：在 <strong> 加入 style 屬性，並設定顏色
        // 歌名 (strong): 設定為亮綠色或純白
        // 歌手 (small): 設定為灰白色 (opacity 較低)
        li.innerHTML = `
            <strong style="color: #055624ff; font-size: 1.1em;">${song.title}</strong> 
            <br>
            <small style="color: rgba(255, 255, 255, 0.6);">${song.artist}</small>
        `;

        li.onclick = () => switchTrack(index);

        // 滑鼠移入效果 (Hover)
        li.onmouseenter = () => li.style.backgroundColor = "#333";
        li.onmouseleave = () => li.style.backgroundColor = "transparent";

        listContainer.appendChild(li);
    });

    // 設定初始畫面
    updateUI(0);
    console.log("播放列表已強制渲染成功！");
}

function updateUI(index) {
    const song = songs[index];
    const titleEl = document.getElementById('track-title');
    const artistEl = document.getElementById('track-artist');
    const coverEl = document.getElementById('track-cover');

    if (titleEl) titleEl.textContent = song.title;
    if (artistEl) artistEl.textContent = song.artist;
    if (coverEl) coverEl.src = `https://img.youtube.com/vi/${song.id}/maxresdefault.jpg`;
}

function switchTrack(index) {
    const song = songs[index];
    if (player && player.loadVideoById) {
        player.loadVideoById(song.id);
    }
    updateUI(index);
}

// YouTube API
var tag = document.createElement('script');
tag.src = "https://www.youtube.com/iframe_api";
var firstScriptTag = document.getElementsByTagName('script')[0];
firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);

function onYouTubeIframeAPIReady() {
    player = new YT.Player('youtube-player', {
        height: '0', width: '0', videoId: songs[0].id,
        events: {
            'onReady': (e) => {
                document.getElementById('play-btn').addEventListener('click', () => {
                    if (isPlaying) player.pauseVideo(); else player.playVideo();
                });
            },
            'onStateChange': (e) => {
                const pb = document.getElementById('play-btn');
                if (e.data == YT.PlayerState.PLAYING) {
                    isPlaying = true; pb.textContent = '⏸';
                } else {
                    isPlaying = false; pb.textContent = '▶';
                }
            }
        }
    });
}

// 只要 HTML 載入完就執行，不等 API
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', forceRenderPlaylist);
} else {
    forceRenderPlaylist();
}