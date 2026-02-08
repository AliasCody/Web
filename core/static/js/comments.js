document.addEventListener("DOMContentLoaded", () => {
  const container = document.getElementById("comments-list");
  const form = document.getElementById("comment-form");
  const csrfToken = document.querySelector('meta[name="csrf-token"]').getAttribute("content");

  // 載入留言
  function loadComments() {
    fetch("/api/comments/")
      .then(res => res.json())
      .then(data => {
        container.innerHTML = "";
        data.comments.forEach(item => {
          const div = document.createElement("div");
          div.classList.add("comment-item");
          div.innerHTML = `
            <strong>${item.author}</strong>: ${item.content} 
            <button class="delete-btn" data-id="${item.id}">刪除</button>
          `;
          container.appendChild(div);

          // 刪除留言
          div.querySelector(".delete-btn").addEventListener("click", () => {
            fetch("/api/comments/", {
              method: "DELETE",
              headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": csrfToken
              },
              body: JSON.stringify({ id: item.id })
            }).then(res => { if(res.ok) div.remove(); });
          });
        });
      });
  }

  loadComments();

  // 新增留言
  form.addEventListener("submit", (e) => {
    e.preventDefault();
    const formData = new FormData(form);
    const data = {
      author: formData.get("author"),
      content: formData.get("content")
    };

    fetch("/api/comments/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": csrfToken
      },
      body: JSON.stringify(data)
    })
    .then(res => res.json())
    .then(() => {
      form.reset();
      loadComments();
    });
  });
});
