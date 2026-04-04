<?php
/**
 * PDR Abroad Consultancy - Blog Management
 */
require_once '../php/config.php';
requireLogin();

$blogs = getBlogPosts();

// Handle delete
if (isset($_GET['delete'])) {
    $id = $_GET['delete'];
    $blogs = array_filter($blogs, fn($b) => ($b['id'] ?? '') !== $id);
    saveBlogPosts(array_values($blogs));
    header('Location: blogs.php?deleted=1');
    exit;
}

$message = '';
if (isset($_GET['deleted'])) {
    $message = 'Blog post deleted successfully.';
}
if (isset($_GET['created'])) {
    $message = 'Blog post created successfully.';
}
if (isset($_GET['updated'])) {
    $message = 'Blog post updated successfully.';
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Blog Posts | Admin Panel</title>
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
                <h1>Blog Posts</h1>
                <p>Manage your blog articles and updates</p>
            </header>
            
            <?php if ($message): ?>
            <div class="alert alert-success"><?php echo e($message); ?></div>
            <?php endif; ?>
            
            <div class="card">
                <div class="card-header">
                    <h2>All Posts (<?php echo count($blogs); ?>)</h2>
                    <a href="blog-create.php" class="btn btn-primary btn-sm">
                        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <line x1="12" y1="5" x2="12" y2="19"/>
                            <line x1="5" y1="12" x2="19" y2="12"/>
                        </svg>
                        New Post
                    </a>
                </div>
                <div class="card-body">
                    <?php if (empty($blogs)): ?>
                    <div class="empty-state">
                        <p>No blog posts yet. Create your first post!</p>
                        <a href="blog-create.php" class="btn btn-primary" style="margin-top: 1rem;">Create Post</a>
                    </div>
                    <?php else: ?>
                    <div class="table-responsive">
                        <table class="table">
                            <thead>
                                <tr>
                                    <th>Title</th>
                                    <th>Category</th>
                                    <th>Status</th>
                                    <th>Date</th>
                                    <th>Actions</th>
                                </tr>
                            </thead>
                            <tbody>
                                <?php foreach (array_reverse($blogs) as $blog): ?>
                                <tr>
                                    <td>
                                        <strong><?php echo e($blog['title']); ?></strong>
                                        <br><small style="color: var(--gray-500);"><?php echo e($blog['slug'] ?? ''); ?></small>
                                    </td>
                                    <td><?php echo e($blog['category'] ?? 'Uncategorized'); ?></td>
                                    <td>
                                        <span class="badge badge-<?php echo ($blog['status'] ?? 'published') === 'published' ? 'published' : 'draft'; ?>">
                                            <?php echo ucfirst($blog['status'] ?? 'published'); ?>
                                        </span>
                                    </td>
                                    <td><?php echo formatDate($blog['date'] ?? 'now', 'M j, Y'); ?></td>
                                    <td>
                                        <div style="display: flex; gap: 0.5rem;">
                                            <a href="blog-edit.php?id=<?php echo e($blog['id']); ?>" class="btn btn-sm btn-secondary">Edit</a>
                                            <a href="blogs.php?delete=<?php echo e($blog['id']); ?>" class="btn btn-sm btn-outline" onclick="return confirm('Are you sure you want to delete this post?')">Delete</a>
                                        </div>
                                    </td>
                                </tr>
                                <?php endforeach; ?>
                            </tbody>
                        </table>
                    </div>
                    <?php endif; ?>
                </div>
            </div>
        </main>
    </div>
    
    <script src="scripts.js"></script>
</body>
</html>
