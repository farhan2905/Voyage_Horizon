<?php
/**
 * PDR Abroad Consultancy - Admin Dashboard
 */
require_once '../php/config.php';
requireLogin();

// Get statistics
$enquiries = getEnquiries();
$blogs = getBlogPosts();

$total_enquiries = count($enquiries);
$pending_enquiries = $total_enquiries; // You can add status tracking
$total_blogs = count($blogs);
$published_blogs = count(array_filter($blogs, fn($b) => ($b['status'] ?? 'published') === 'published'));

// Get recent enquiries
$recent_enquiries = array_slice(array_reverse($enquiries), 0, 5);
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dashboard | Admin Panel</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="admin-wrapper">
        <!-- Sidebar -->
        <?php include 'includes/sidebar.php'; ?>
        
        <!-- Main Content -->
        <main class="main-content">
            <header class="page-header">
                <h1>Dashboard</h1>
                <p>Welcome back, <?php echo e($_SESSION['admin_username']); ?>!</p>
            </header>
            
            <!-- Stats Grid -->
            <div class="stats-grid">
                <div class="stat-card">
                    <div class="stat-icon enquiries">
                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/>
                            <polyline points="22,6 12,13 2,6"/>
                        </svg>
                    </div>
                    <div class="stat-info">
                        <span class="stat-value"><?php echo $total_enquiries; ?></span>
                        <span class="stat-label">Total Enquiries</span>
                    </div>
                </div>
                
                <div class="stat-card">
                    <div class="stat-icon blogs">
                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/>
                            <polyline points="14 2 14 8 20 8"/>
                            <line x1="16" y1="13" x2="8" y2="13"/>
                            <line x1="16" y1="17" x2="8" y2="17"/>
                        </svg>
                    </div>
                    <div class="stat-info">
                        <span class="stat-value"><?php echo $total_blogs; ?></span>
                        <span class="stat-label">Blog Posts</span>
                    </div>
                </div>
                
                <div class="stat-card">
                    <div class="stat-icon published">
                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/>
                            <polyline points="22 4 12 14.01 9 11.01"/>
                        </svg>
                    </div>
                    <div class="stat-info">
                        <span class="stat-value"><?php echo $published_blogs; ?></span>
                        <span class="stat-label">Published</span>
                    </div>
                </div>
                
                <div class="stat-card">
                    <div class="stat-icon visitors">
                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/>
                            <circle cx="9" cy="7" r="4"/>
                            <path d="M23 21v-2a4 4 0 0 0-3-3.87M16 3.13a4 4 0 0 1 0 7.75"/>
                        </svg>
                    </div>
                    <div class="stat-info">
                        <span class="stat-value">--</span>
                        <span class="stat-label">This Month</span>
                    </div>
                </div>
            </div>
            
            <!-- Recent Enquiries -->
            <div class="card">
                <div class="card-header">
                    <h2>Recent Enquiries</h2>
                    <a href="enquiries.php" class="btn btn-sm btn-outline">View All</a>
                </div>
                <div class="card-body">
                    <?php if (empty($recent_enquiries)): ?>
                    <p class="empty-state">No enquiries yet.</p>
                    <?php else: ?>
                    <div class="table-responsive">
                        <table class="table">
                            <thead>
                                <tr>
                                    <th>Name</th>
                                    <th>Email</th>
                                    <th>Phone</th>
                                    <th>Service</th>
                                    <th>Date</th>
                                </tr>
                            </thead>
                            <tbody>
                                <?php foreach ($recent_enquiries as $enquiry): ?>
                                <tr>
                                    <td><?php echo e($enquiry['name']); ?></td>
                                    <td><?php echo e($enquiry['email']); ?></td>
                                    <td><?php echo e($enquiry['phone']); ?></td>
                                    <td><?php echo e($enquiry['service'] ?? 'N/A'); ?></td>
                                    <td><?php echo formatDate($enquiry['date'], 'M j, Y'); ?></td>
                                </tr>
                                <?php endforeach; ?>
                            </tbody>
                        </table>
                    </div>
                    <?php endif; ?>
                </div>
            </div>
            
            <!-- Quick Actions -->
            <div class="card">
                <div class="card-header">
                    <h2>Quick Actions</h2>
                </div>
                <div class="card-body">
                    <div class="quick-actions">
                        <a href="blog-create.php" class="action-btn">
                            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                <line x1="12" y1="5" x2="12" y2="19"/>
                                <line x1="5" y1="12" x2="19" y2="12"/>
                            </svg>
                            Create New Blog Post
                        </a>
                        <a href="enquiries.php" class="action-btn">
                            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/>
                                <polyline points="22,6 12,13 2,6"/>
                            </svg>
                            View All Enquiries
                        </a>
                        <a href="../index.html" class="action-btn" target="_blank">
                            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                <path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/>
                                <polyline points="15 3 21 3 21 9"/>
                                <line x1="10" y1="14" x2="21" y2="3"/>
                            </svg>
                            View Website
                        </a>
                    </div>
                </div>
            </div>
        </main>
    </div>
    
    <script src="scripts.js"></script>
</body>
</html>
