// app.js
document.addEventListener('DOMContentLoaded', () => {
    const app = document.getElementById('app');

    async function fetchPosts() {
        const response = await fetch('/api/posts/');
        const posts = await response.json();
        return posts;
    }

    async function fetchUsers() {
        const response = await fetch('/api/users/');
        const users = await response.json();
        return users;
    }

    async function renderPosts() {
        const posts = await fetchPosts();
        const users = await fetchUsers();
        let html = '';

        posts.forEach(post => {
            const user = users.find(user => user.id === post.user);
            html += `
                <div class="post">
                    <h3>${user.username}</h3>
                    <p>${post.content}</p>
                    <small>Posted on ${new Date(post.created_at).toLocaleDateString()}</small>
                </div>
            `;
        });

        app.innerHTML = html;
    }

    renderPosts();
});
