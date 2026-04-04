<?php
/**
 * PDR Abroad Consultancy - Enquiries Management
 */
require_once '../php/config.php';
requireLogin();

$enquiries = getEnquiries();

// Handle delete
if (isset($_GET['delete'])) {
    $index = (int)$_GET['delete'];
    if (isset($enquiries[$index])) {
        array_splice($enquiries, $index, 1);
        $file = __DIR__ . '/../php/data/enquiries.json';
        file_put_contents($file, json_encode($enquiries, JSON_PRETTY_PRINT));
        header('Location: enquiries.php?deleted=1');
        exit;
    }
}

$message = '';
if (isset($_GET['deleted'])) {
    $message = 'Enquiry deleted successfully.';
}

// Reverse for newest first
$enquiries_display = array_reverse($enquiries, true);
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Enquiries | Admin Panel</title>
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
                <h1>Enquiries</h1>
                <p>View and manage contact form submissions</p>
            </header>
            
            <?php if ($message): ?>
            <div class="alert alert-success"><?php echo e($message); ?></div>
            <?php endif; ?>
            
            <div class="card">
                <div class="card-header">
                    <h2>All Enquiries (<?php echo count($enquiries); ?>)</h2>
                </div>
                <div class="card-body">
                    <?php if (empty($enquiries)): ?>
                    <div class="empty-state">
                        <p>No enquiries yet. Enquiries from the contact form will appear here.</p>
                    </div>
                    <?php else: ?>
                    <div class="table-responsive">
                        <table class="table">
                            <thead>
                                <tr>
                                    <th>#</th>
                                    <th>Name</th>
                                    <th>Email</th>
                                    <th>Phone</th>
                                    <th>Service</th>
                                    <th>Country</th>
                                    <th>Date</th>
                                    <th>Actions</th>
                                </tr>
                            </thead>
                            <tbody>
                                <?php foreach ($enquiries_display as $index => $enquiry): ?>
                                <tr>
                                    <td><?php echo $index + 1; ?></td>
                                    <td><strong><?php echo e($enquiry['name']); ?></strong></td>
                                    <td><a href="mailto:<?php echo e($enquiry['email']); ?>"><?php echo e($enquiry['email']); ?></a></td>
                                    <td><?php echo e($enquiry['phone']); ?></td>
                                    <td><?php echo e($enquiry['service'] ?? 'N/A'); ?></td>
                                    <td><?php echo e($enquiry['country'] ?? 'N/A'); ?></td>
                                    <td><?php echo formatDate($enquiry['date'], 'M j, Y'); ?></td>
                                    <td>
                                        <div style="display: flex; gap: 0.5rem;">
                                            <button class="btn btn-sm btn-secondary" onclick="showDetails(<?php echo $index; ?>)">View</button>
                                            <a href="enquiries.php?delete=<?php echo $index; ?>" class="btn btn-sm btn-outline" onclick="return confirm('Are you sure you want to delete this enquiry?')">Delete</a>
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

    <!-- Detail Modal -->
    <div id="detailModal" style="display:none; position:fixed; top:0; left:0; right:0; bottom:0; background:rgba(0,0,0,0.5); z-index:1000; align-items:center; justify-content:center;">
        <div style="background:white; border-radius:1rem; max-width:500px; width:90%; padding:2rem; margin:auto; margin-top:10vh; max-height:70vh; overflow-y:auto;">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:1.5rem;">
                <h3 style="margin:0;">Enquiry Details</h3>
                <button onclick="closeModal()" style="background:none; border:none; font-size:1.5rem; cursor:pointer;">&times;</button>
            </div>
            <div id="modalContent"></div>
        </div>
    </div>

    <script>
        const enquiries = <?php echo json_encode(array_values($enquiries_display)); ?>;
        
        function showDetails(index) {
            const eq = enquiries[index];
            if (!eq) return;
            
            document.getElementById('modalContent').innerHTML = `
                <div style="margin-bottom:1rem;"><strong>Name:</strong> ${escapeHtml(eq.name)}</div>
                <div style="margin-bottom:1rem;"><strong>Email:</strong> ${escapeHtml(eq.email)}</div>
                <div style="margin-bottom:1rem;"><strong>Phone:</strong> ${escapeHtml(eq.phone)}</div>
                <div style="margin-bottom:1rem;"><strong>Service:</strong> ${escapeHtml(eq.service || 'N/A')}</div>
                <div style="margin-bottom:1rem;"><strong>Country:</strong> ${escapeHtml(eq.country || 'N/A')}</div>
                <div style="margin-bottom:1rem;"><strong>Message:</strong><br>${escapeHtml(eq.message || 'No message')}</div>
                <div style="margin-bottom:1rem;"><strong>Date:</strong> ${escapeHtml(eq.date)}</div>
                <div><strong>IP Address:</strong> ${escapeHtml(eq.ip_address || 'N/A')}</div>
            `;
            document.getElementById('detailModal').style.display = 'flex';
        }
        
        function closeModal() {
            document.getElementById('detailModal').style.display = 'none';
        }
        
        function escapeHtml(str) {
            const div = document.createElement('div');
            div.appendChild(document.createTextNode(str));
            return div.innerHTML;
        }
        
        document.getElementById('detailModal').addEventListener('click', function(e) {
            if (e.target === this) closeModal();
        });
    </script>
    
    <script src="scripts.js"></script>
</body>
</html>
