<?php
/**
 * PDR Abroad Consultancy - Configuration File
 * Database and site configuration settings
 */

// Start session if not already started
if (session_status() === PHP_SESSION_NONE) {
    session_start();
}

// Site Configuration
define('SITE_NAME', 'PDR Abroad Consultancy');
define('SITE_URL', 'https://www.pdrabroad.com');
define('ADMIN_EMAIL', 'info@pdrabroad.com');
define('CONTACT_PHONE', '+91 98765 43210');

// Database Configuration (for MySQL - optional)
// Uncomment and configure if using MySQL database
/*
define('DB_HOST', 'localhost');
define('DB_NAME', 'pdrabroad_db');
define('DB_USER', 'your_username');
define('DB_PASS', 'your_password');
define('DB_PREFIX', 'pdr_');
*/

// Admin Credentials (for simple file-based auth)
define('ADMIN_USERNAME', 'admin');
define('ADMIN_PASSWORD', '$2y$10$YourHashedPasswordHere'); // Use password_hash() to generate

// Security Settings
define('HASH_SALT', 'your-random-salt-string-here');

// File Upload Settings
define('UPLOAD_DIR', __DIR__ . '/../uploads/');
define('MAX_FILE_SIZE', 5 * 1024 * 1024); // 5MB
define('ALLOWED_IMAGE_TYPES', ['image/jpeg', 'image/png', 'image/gif', 'image/webp']);

// Date and Time
date_default_timezone_set('Asia/Kolkata');

// Error Reporting (disable in production)
// error_reporting(E_ALL);
// ini_set('display_errors', 1);

/**
 * Get database connection (MySQL)
 * Uncomment this function if using MySQL
 */
/*
function getDBConnection() {
    try {
        $pdo = new PDO(
            'mysql:host=' . DB_HOST . ';dbname=' . DB_NAME . ';charset=utf8mb4',
            DB_USER,
            DB_PASS,
            [
                PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
                PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
                PDO::ATTR_EMULATE_PREPARES => false
            ]
        );
        return $pdo;
    } catch (PDOException $e) {
        error_log('Database connection failed: ' . $e->getMessage());
        return null;
    }
}
*/

/**
 * Get blog posts from JSON file
 */
function getBlogPosts() {
    $file = __DIR__ . '/data/blogs.json';
    if (!file_exists($file)) {
        return [];
    }
    return json_decode(file_get_contents($file), true) ?: [];
}

/**
 * Save blog posts to JSON file
 */
function saveBlogPosts($posts) {
    $file = __DIR__ . '/data/blogs.json';
    $dir = dirname($file);
    if (!is_dir($dir)) {
        mkdir($dir, 0755, true);
    }
    return file_put_contents($file, json_encode($posts, JSON_PRETTY_PRINT));
}

/**
 * Get enquiries from JSON file
 */
function getEnquiries() {
    $file = __DIR__ . '/data/enquiries.json';
    if (!file_exists($file)) {
        return [];
    }
    return json_decode(file_get_contents($file), true) ?: [];
}

/**
 * Generate URL slug from title
 */
function generateSlug($title) {
    $slug = strtolower($title);
    $slug = preg_replace('/[^a-z0-9\s-]/', '', $slug);
    $slug = preg_replace('/[\s-]+/', '-', $slug);
    $slug = trim($slug, '-');
    return $slug;
}

/**
 * Check if user is logged in
 */
function isLoggedIn() {
    return isset($_SESSION['admin_logged_in']) && $_SESSION['admin_logged_in'] === true;
}

/**
 * Require login for admin pages
 */
function requireLogin() {
    if (!isLoggedIn()) {
        header('Location: login.php');
        exit;
    }
}

/**
 * Sanitize output
 */
function e($string) {
    return htmlspecialchars($string, ENT_QUOTES, 'UTF-8');
}

/**
 * Format date
 */
function formatDate($date, $format = 'F j, Y') {
    return date($format, strtotime($date));
}
?>
