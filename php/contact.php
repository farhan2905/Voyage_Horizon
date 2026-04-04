<?php
/**
 * PDR Abroad Consultancy - Contact Form Handler
 * Handles form submissions and sends emails
 */

// Prevent direct access
if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    header('Location: ../contact.html');
    exit;
}

// Configuration
$config = [
    'admin_email' => 'info@pdrabroad.com',
    'from_email' => 'noreply@pdrabroad.com',
    'from_name' => 'PDR Abroad Consultancy',
    'success_redirect' => '../thank-you.html',
    'error_redirect' => '../contact.html?error=1'
];

// Sanitize input function
function sanitize($data) {
    return htmlspecialchars(strip_tags(trim($data)));
}

// Validate email function
function isValidEmail($email) {
    return filter_var($email, FILTER_VALIDATE_EMAIL) !== false;
}

// Get and validate form data
$errors = [];
$data = [];

// Required fields
$required_fields = ['firstName', 'lastName', 'email', 'phone'];

foreach ($required_fields as $field) {
    if (empty($_POST[$field])) {
        $errors[] = ucfirst(str_replace('_', ' ', $field)) . ' is required';
    } else {
        $data[$field] = sanitize($_POST[$field]);
    }
}

// Optional fields
$optional_fields = ['service', 'country', 'message'];

foreach ($optional_fields as $field) {
    if (!empty($_POST[$field])) {
        $data[$field] = sanitize($_POST[$field]);
    } else {
        $data[$field] = '';
    }
}

// Validate email format
if (!empty($data['email']) && !isValidEmail($data['email'])) {
    $errors[] = 'Please enter a valid email address';
}

// If there are errors, redirect back
if (!empty($errors)) {
    $_SESSION['form_errors'] = $errors;
    $_SESSION['form_data'] = $data;
    header('Location: ' . $config['error_redirect']);
    exit;
}

// Prepare email content
$subject = 'New Enquiry from ' . $data['firstName'] . ' ' . $data['lastName'];

$email_body = "
<html>
<head>
    <style>
        body { font-family: Arial, sans-serif; line-height: 1.6; }
        .container { max-width: 600px; margin: 0 auto; padding: 20px; }
        h2 { color: #B91C1C; }
        .field { margin-bottom: 15px; }
        .label { font-weight: bold; color: #374151; }
        .value { color: #6B7280; }
    </style>
</head>
<body>
    <div class='container'>
        <h2>New Enquiry from Website</h2>
        <p>A new enquiry has been submitted through the website contact form.</p>
        
        <div class='field'>
            <span class='label'>Name:</span>
            <span class='value'>{$data['firstName']} {$data['lastName']}</span>
        </div>
        
        <div class='field'>
            <span class='label'>Email:</span>
            <span class='value'>{$data['email']}</span>
        </div>
        
        <div class='field'>
            <span class='label'>Phone:</span>
            <span class='value'>{$data['phone']}</span>
        </div>
        
        <div class='field'>
            <span class='label'>Service Interested:</span>
            <span class='value'>" . ($data['service'] ?: 'Not specified') . "</span>
        </div>
        
        <div class='field'>
            <span class='label'>Preferred Country:</span>
            <span class='value'>" . ($data['country'] ?: 'Not specified') . "</span>
        </div>
        
        <div class='field'>
            <span class='label'>Message:</span>
            <p class='value'>" . nl2br($data['message'] ?: 'No message provided') . "</p>
        </div>
        
        <hr>
        <p><small>This enquiry was submitted on " . date('F j, Y, g:i a') . "</small></p>
    </div>
</body>
</html>
";

// Email headers
$headers = [
    'MIME-Version: 1.0',
    'Content-Type: text/html; charset=UTF-8',
    'From: ' . $config['from_name'] . ' <' . $config['from_email'] . '>',
    'Reply-To: ' . $data['email']
];

// Save to database or file (optional)
$enquiry_data = [
    'name' => $data['firstName'] . ' ' . $data['lastName'],
    'email' => $data['email'],
    'phone' => $data['phone'],
    'service' => $data['service'],
    'country' => $data['country'],
    'message' => $data['message'],
    'date' => date('Y-m-d H:i:s'),
    'ip_address' => $_SERVER['REMOTE_ADDR']
];

// Save to JSON file (simple storage)
$enquiries_file = __DIR__ . '/data/enquiries.json';
$enquiries_dir = dirname($enquiries_file);

if (!is_dir($enquiries_dir)) {
    mkdir($enquiries_dir, 0755, true);
}

$enquiries = [];
if (file_exists($enquiries_file)) {
    $enquiries = json_decode(file_get_contents($enquiries_file), true) ?: [];
}

$enquiries[] = $enquiry_data;
file_put_contents($enquiries_file, json_encode($enquiries, JSON_PRETTY_PRINT));

// Send email
$mail_sent = mail($config['admin_email'], $subject, $email_body, implode("\r\n", $headers));

// Send auto-reply to user
$auto_reply_subject = 'Thank you for contacting PDR Abroad Consultancy';
$auto_reply_body = "
<html>
<head>
    <style>
        body { font-family: Arial, sans-serif; line-height: 1.6; }
        .container { max-width: 600px; margin: 0 auto; padding: 20px; }
        h2 { color: #B91C1C; }
        .footer { margin-top: 30px; padding-top: 20px; border-top: 1px solid #e5e7eb; color: #6B7280; }
    </style>
</head>
<body>
    <div class='container'>
        <h2>Thank You for Contacting Us!</h2>
        <p>Dear {$data['firstName']},</p>
        <p>Thank you for reaching out to PDR Abroad Consultancy. We have received your enquiry and our team will get back to you within 24 hours.</p>
        <p>In the meantime, feel free to explore our services:</p>
        <ul>
            <li>Study Visa Services</li>
            <li>MBBS Abroad Programs</li>
            <li>Test Preparation (IELTS, TOEFL, PTE, GRE, GMAT, SAT)</li>
        </ul>
        <p>If you need immediate assistance, you can reach us at:</p>
        <ul>
            <li>Phone: +91 98765 43210</li>
            <li>WhatsApp: +91 98765 43210</li>
            <li>Email: info@pdrabroad.com</li>
        </ul>
        <div class='footer'>
            <p>Best regards,<br>PDR Abroad Consultancy Team</p>
        </div>
    </div>
</body>
</html>
";

$auto_reply_headers = [
    'MIME-Version: 1.0',
    'Content-Type: text/html; charset=UTF-8',
    'From: ' . $config['from_name'] . ' <' . $config['from_email'] . '>'
];

mail($data['email'], $auto_reply_subject, $auto_reply_body, implode("\r\n", $auto_reply_headers));

// Redirect to thank you page
header('Location: ' . $config['success_redirect']);
exit;
?>
