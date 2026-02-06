// addEvenetListener("DOMContentLoaded",...) 等待DOM建好
document.addEventListener("DOMContentLoaded", () => {
  // 1. 在 DOM 裡面找到留言容器
  const commentsBox = document.getElementById("comments");

  // 2. 生出一塊 div  ( div 還在暫存器裡，未寫進 DOM )
  const commentDiv = document.createElement("div");

  // 3. 在這塊 div 內塞東西
  commentDiv.innerText = "測試留言：Hello DOM";

  // 4. 一次將處理好的 div 塞進 DOM
  commentsBox.appendChild(commentDiv);
});
