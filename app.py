from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

# Sample blog posts data (simulating a database)
posts = [
    {"id": 1, "title": "First Blog Post", "content": "This is the first blog post content.", "date": "2025-08-13"},
    {"id": 2, "title": "Second Blog Post", "content": "This is the second blog post content.", "date": "2025-08-12"}
]

@app.route('/')
def home():
    return render_template('index.html', title="Home Page", description="Welcome to our SEO-optimized PWA website")

@app.route('/blog')
def blog():
    return render_template('blog.html', posts=posts, title="Blog", description="Read our latest blog posts")

@app.route('/blog/<int:post_id>')
def blog_post(post_id):
    post = next((p for p in posts if p['id'] == post_id), None)
    if post:
        return render_template('post.html', post=post, title=post['title'], description=post['content'][:150])
    return "Post not found", 404

@app.route('/api/posts', methods=['GET'])
def get_posts():
    return jsonify(posts)

@app.route('/manifest.json')
def manifest():
    return app.send_static_file('manifest.json')

@app.route('/service-worker.js')
def service_worker():
    return app.send_static_file('service-worker.js')

if __name__ == '__main__':
    app.run(debug=True)