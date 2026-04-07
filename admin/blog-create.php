<?php
/**
 * Voyage Horizon - Create Blog Post
 */
require_once '../php/config.php';
requireLogin();

$error = '';
$success = '';

// Handle form submission
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $title = trim($_POST['title'] ?? '');
    $slug = trim($_POST['slug'] ?? '');
    $category = trim($_POST['category'] ?? '');
    $tags = trim($_POST['tags'] ?? '');
    $content = trim($_POST['content'] ?? '');
    $meta_title = trim($_POST['meta_title'] ?? '');
    $meta_description = trim($_POST['meta_description'] ?? '');
    $status = $_POST['status'] ?? 'draft';
    
    // Validation
    if (empty($title)) {
        $error = 'Title is required';
    } elseif (empty($content)) {
        $error = 'Content is required';
    } else {
        // Generate slug if not provided
        if (empty($slug)) {
            $slug = generateSlug($title);
        }
        
        // Generate unique ID
        $id = uniqid() . '-' . time();
        
        // Handle image upload
        $featured_image = '';
        if (!empty($_FILES['featured_image']['name'])) {
            $upload_dir = '../uploads/blog/';
            if (!is_dir($upload_dir)) {
                mkdir($upload_dir, 0755, true);
            }
            
            $file_name = time() . '_' . basename($_FILES['featured_image']['name']);
            $target_path = $upload_dir . $file_name;
            
            if (move_uploaded_file($_FILES['featured_image']['tmp_name'], $target_path)) {
                $featured_image = 'uploads/blog/' . $file_name;
            }
        }
        
        // Create blog post
        $post = [
            'id' => $id,
            'title' => $title,
            'slug' => $slug,
            'category' => $category,
            'tags' => $tags,
            'content' => $content,
            'featured_image' => $featured_image,
            'meta_title' => $meta_title ?: $title,
            'meta_description' => $meta_description,
            'status' => $status,
            'date' => date('Y-m-d H:i:s'),
            'author' => $_SESSION['admin_username'] ?? 'Admin'
        ];
        
        // Save to blogs
        $blogs = getBlogPosts();
        $blogs[] = $post;
        saveBlogPosts($blogs);
        
        header('Location: blogs.php?created=1');
        exit;
    }
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Create Blog Post | Admin Panel</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="admin-wrapper">
        <?php include 'includes/sidebar.php'; ?>
        
        <main class="main-content">
            <header class="page-header">
                <h1>Create Blog Post</h1>
                <p>Write a new article for your blog</p>
            </header>
            
            <?php if ($error): ?>
            <div class="alert alert-error"><?php echo e($error); ?></div>
            <?php endif; ?>
            
            <div class="card">
                <div class="card-body">
                    <form method="POST" action="" enctype="multipart/form-data">
                        <div class="form-row">
                            <div class="form-group">
                                <label class="form-label" for="title">Title *</label>
                                <input type="text" id="title" name="title" class="form-input" placeholder="Enter post title" required>
                            </div>
                            <div class="form-group">
                                <label class="form-label" for="slug">URL Slug</label>
                                <input type="text" id="slug" name="slug" class="form-input" placeholder="auto-generated-if-empty">
                            </div>
                        </div>
                        
                        <div class="form-row">
                            <div class="form-group">
                                <label class="form-label" for="category">Category</label>
                                <select id="category" name="category" class="form-input">
                                    <option value="">Select category</option>
                                    <option value="visa">Visa</option>
                                    <option value="mbbs">MBBS</option>
                                    <option value="exams">Exams</option>
                                    <option value="tips">Tips</option>
                                    <option value="news">News</option>
                                </select>
                            </div>
                            <div class="form-group">
                                <label class="form-label" for="status">Status</label>
                                <select id="status" name="status" class="form-input">
                                    <option value="draft">Draft</option>
                                    <option value="published">Published</option>
                                </select>
                            </div>
                        </div>
                        
                        <div class="form-group">
                            <label class="form-label" for="tags">Tags (comma separated)</label>
                            <input type="text" id="tags" name="tags" class="form-input" placeholder="study visa, visa, tips">
                        </div>
                        
                        <div class="form-group">
                            <label class="form-label" for="featured_image">Featured Image</label>
                            <input type="file" id="featured_image" name="featured_image" class="form-input" accept="image/*">
                        </div>
                        
                        <div class="form-group">
                            <label class="form-label" for="content">Content *</label>
                            <textarea id="content" name="content" class="form-input" rows="15" placeholder="Write your blog content here... You can use HTML tags for formatting." required></textarea>
                        </div>
                        
                        <hr style="margin: 2rem 0; border: none; border-top: 1px solid var(--gray-200);">
                        
                        <h3 style="margin-bottom: 1rem;">SEO Settings</h3>
                        
                        <div class="form-group">
                            <label class="form-label" for="meta_title">Meta Title</label>
                            <input type="text" id="meta_title" name="meta_title" class="form-input" placeholder="SEO title (defaults to post title)">
                        </div>
                        
                        <div class="form-group">
                            <label class="form-label" for="meta_description">Meta Description</label>
                            <textarea id="meta_description" name="meta_description" class="form-input" rows="3" placeholder="Brief description for search engines"></textarea>
                        </div>
                        
                        <div style="display: flex; gap: 1rem; margin-top: 2rem;">
                            <button type="submit" class="btn btn-primary btn-lg">Create Post</button>
                            <a href="blogs.php" class="btn btn-secondary btn-lg">Cancel</a>
                        </div>
                    </form>
                </div>
            </div>
        </main>
    </div>
    
    <script src="scripts.js"></script>
</body>
</html>
