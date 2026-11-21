# Prescribed Practical Labs Generator (BCAC591 & BCAC592)

def get_practicals_data():
    return {
    "bcac591": [
        {
            "id": "lab_php_case1",
            "code": "BCAC591",
            "lab_name": "PHP WITH MYSQL LAB",
            "case_no": 1,
            "title": "Case 1: User Registration and Secure Login Authentication System",
            "objective": "Design, implement, and verify a production-grade user authentication portal featuring input sanitization, Argon2id/Bcrypt password hashing, prepared SQL statements, and session fixation protection.",
            "principle": "Stateful user authentication over stateless HTTP requires server-side credential verification against a one-way cryptographic hash and issuance of an unguessable session token (PHPSESSID) protected by HttpOnly and Secure cookie attributes.",
            "materials_setup": "Apache 2.4+ / Nginx, PHP 8.2+, MySQL 8.0 / MariaDB, phpMyAdmin or MySQL CLI client, modern web browser.",
            "architecture_svg": "<svg viewBox='0 0 700 130' xmlns='http://www.w3.org/2000/svg' style='width:100%;height:auto;background:#fff;border-radius:6px;border:1px solid #E5E9F1;'><rect x='20' y='25' width='130' height='80' rx='6' fill='#F7F8FC' stroke='#377FE6'/><text x='85' y='55' font-family='sans-serif' font-size='11' font-weight='700' fill='#377FE6' text-anchor='middle'>User Form</text><text x='85' y='75' font-family='monospace' font-size='9' fill='#19283D' text-anchor='middle'>POST login.php</text><path d='M 155 65 L 215 65' stroke='#377FE6' stroke-width='2'/><rect x='220' y='25' width='160' height='80' rx='6' fill='#F7F8FC' stroke='#786CE5'/><text x='300' y='55' font-family='sans-serif' font-size='11' font-weight='700' fill='#786CE5' text-anchor='middle'>Password Verify</text><text x='300' y='75' font-family='monospace' font-size='9' fill='#19283D' text-anchor='middle'>password_verify()</text><path d='M 385 65 L 445 65' stroke='#786CE5' stroke-width='2'/><rect x='450' y='25' width='230' height='80' rx='6' fill='#E9E8F8' stroke='#28A994'/><text x='565' y='55' font-family='sans-serif' font-size='11' font-weight='700' fill='#1B6F61' text-anchor='middle'>Session Issued</text><text x='565' y='75' font-family='monospace' font-size='9' fill='#19283D' text-anchor='middle'>session_regenerate_id(true)</text><text x='565' y='92' font-family='sans-serif' font-size='8' fill='#369B72' text-anchor='middle'>PHPSESSID with HttpOnly &amp; Secure</text></svg>",
            "procedure_steps": [
                "1. Establish MySQL schema `makaut_portal` with `users` table including `id`, `email`, `password_hash`, and `created_at`.",
                "2. Configure database connection wrapper via PDO with exception error reporting enabled.",
                "3. Process registration form using `password_hash($pwd, PASSWORD_BCRYPT)` and prepared SQL statements.",
                "4. Implement login validation: fetch record by email, verify hash with `password_verify()`, and invoke `session_regenerate_id(true)` upon success."
            ],
            "full_code": "-- 1. Database Schema\nCREATE DATABASE IF NOT EXISTS makaut_portal;\nUSE makaut_portal;\nCREATE TABLE IF NOT EXISTS users (\n    id INT AUTO_INCREMENT PRIMARY KEY,\n    name VARCHAR(100) NOT NULL,\n    email VARCHAR(150) NOT NULL UNIQUE,\n    password_hash VARCHAR(255) NOT NULL,\n    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;\n\n-- 2. db.php\n<?php\n$dsn = \"mysql:host=localhost;dbname=makaut_portal;charset=utf8mb4\";\n$options = [\n    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,\n    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,\n    PDO::ATTR_EMULATE_PREPARES => false\n];\ntry {\n    $pdo = new PDO($dsn, \"dbuser\", \"secretpass\", $options);\n} catch (PDOException $e) {\n    die(\"Database connection failed: \" . $e->getMessage());\n}\n?>\n\n-- 3. login.php\n<?php\nrequire_once 'db.php';\nsession_start();\n\nif ($_SERVER['REQUEST_METHOD'] === 'POST') {\n    $email = filter_input(INPUT_POST, 'email', FILTER_VALIDATE_EMAIL);\n    $password = $_POST['password'] ?? '';\n\n    if (!$email || empty($password)) {\n        die(\"Invalid credentials supplied.\");\n    }\n\n    $stmt = $pdo->prepare(\"SELECT id, name, password_hash FROM users WHERE email = :email\");\n    $stmt->execute(['email' => $email]);\n    $user = $stmt->fetch();\n\n    if ($user && password_verify($password, $user['password_hash'])) {\n        session_regenerate_id(true); // Neutralizes session fixation\n        $_SESSION['user_id'] = $user['id'];\n        $_SESSION['user_name'] = $user['name'];\n        header(\"Location: dashboard.php\");\n        exit;\n    } else {\n        echo \"Authentication failed. Incorrect email or password.\";\n    }\n}\n?>",
            "expected_outputs": "1. Successful user registration generates a 60-character bcrypt hash starting with `$2y$10$` in MySQL.\\n2. Valid credentials trigger `session_regenerate_id()` and issue HTTP 302 redirect to `dashboard.php`.\\n3. Malicious inputs containing SQL injection (`' OR 1=1 --`) fail safely and return 'Authentication failed'.",
            "interpretation": "The verification demonstrates that parameterized queries prevent SQL syntax manipulation while bcrypt hashing shields credentials against rainbow table lookups.",
            "viva_qa": [
                {
                    "q": "Why is md5() or sha1() strictly prohibited for password hashing in web applications?",
                    "a": "MD5 and SHA-1 are fast general-purpose cryptographic checksums with severe mathematical collision vulnerabilities. Modern GPU clusters can compute billions of MD5 hashes per second, making rainbow table and brute-force cracking trivial. Modern password hashing must use adaptive, computationally expensive algorithms like Bcrypt or Argon2id."
                },
                {
                    "q": "What attack vector does session_regenerate_id(true) neutralize?",
                    "a": "It prevents Session Fixation attacks, where an attacker tricks a user into authenticating using a pre-determined session ID. Regenerating the ID upon login immediately invalidates the pre-login token and assigns a new cryptographically random ID."
                },
                {
                    "q": "What is the purpose of PDO::ATTR_EMULATE_PREPARES => false?",
                    "a": "It forces PDO to communicate directly with MySQL's native prepared statement engine rather than emulating prepared statements through client-side string substitution, guaranteeing absolute SQL injection immunity."
                }
            ]
        },
        {
            "id": "lab_php_case2",
            "code": "BCAC591",
            "lab_name": "PHP WITH MYSQL LAB",
            "case_no": 2,
            "title": "Case 2: Content Management System (CMS) with WYSIWYG & Role-Based Access Control",
            "objective": "Build a modular Content Management System (CMS) with Role-Based Access Control (RBAC), article publishing workflows, and XSS sanitization.",
            "principle": "CMS architectures decouple editorial content creation from HTML presentation, enforcing authorization boundaries via session roles (Admin vs Author vs Reader) and neutralizing Stored XSS via HTML entity sanitization.",
            "materials_setup": "PHP 8.2+, MySQL 8.0, TinyMCE or Quill WYSIWYG editor, Apache web server.",
            "architecture_svg": "<svg viewBox='0 0 700 130' xmlns='http://www.w3.org/2000/svg' style='width:100%;height:auto;background:#fff;border-radius:6px;border:1px solid #E5E9F1;'><rect x='30' y='25' width='160' height='80' rx='6' fill='#F7F8FC' stroke='#377FE6'/><text x='110' y='55' font-family='sans-serif' font-size='11' font-weight='700' fill='#377FE6' text-anchor='middle'>Author / Admin</text><text x='110' y='75' font-family='monospace' font-size='9' fill='#19283D' text-anchor='middle'>Editor WYSIWYG</text><path d='M 195 65 L 265 65' stroke='#377FE6' stroke-width='2'/><rect x='270' y='25' width='180' height='80' rx='6' fill='#F7F8FC' stroke='#786CE5'/><text x='360' y='55' font-family='sans-serif' font-size='11' font-weight='700' fill='#786CE5' text-anchor='middle'>RBAC Middleware</text><text x='360' y='75' font-family='monospace' font-size='9' fill='#19283D' text-anchor='middle'>Role &gt;= 'EDITOR'</text><path d='M 455 65 L 525 65' stroke='#786CE5' stroke-width='2'/><rect x='530' y='25' width='140' height='80' rx='6' fill='#E9E8F8' stroke='#28A994'/><text x='600' y='55' font-family='sans-serif' font-size='11' font-weight='700' fill='#1B6F61' text-anchor='middle'>Articles DB</text><text x='600' y='75' font-family='monospace' font-size='9' fill='#369B72' text-anchor='middle'>Published Content</text></svg>",
            "procedure_steps": [
                "1. Create database tables `roles`, `users`, `categories`, and `articles`.",
                "2. Enforce RBAC middleware verifying `$_SESSION['role'] === 'ADMIN'` before allowing article publication.",
                "3. Sanitize submitted HTML using `strip_tags()` with whitelisted tags or `htmlspecialchars()` for plain text.",
                "4. Query and render articles sorted by publication date with pagination controls."
            ],
            "full_code": "<?php\n// cms_publish.php\nrequire_once 'db.php';\nsession_start();\n\n// Authorization check: Only ADMIN and EDITOR can publish\nif (!isset($_SESSION['role']) || !in_array($_SESSION['role'], ['ADMIN', 'EDITOR'])) {\n    http_response_code(403);\n    die(\"Forbidden: Insufficient administrative privileges.\");\n}\n\nif ($_SERVER['REQUEST_METHOD'] === 'POST') {\n    $title = trim($_POST['title'] ?? '');\n    $slug = strtolower(trim(preg_replace('/[^A-Za-z0-9-]+/', '-', $title)));\n    $body = strip_tags($_POST['body'] ?? '', '<p><br><b><i><strong><em><ul><ol><li><h2><h3>');\n    $author_id = $_SESSION['user_id'];\n\n    $stmt = $pdo->prepare(\"INSERT INTO articles (title, slug, body, author_id, published_at) VALUES (:title, :slug, :body, :author_id, NOW())\");\n    $stmt->execute([\n        'title' => $title,\n        'slug' => $slug,\n        'body' => $body,\n        'author_id' => $author_id\n    ]);\n\n    echo \"Article successfully published with ID: \" . $pdo->lastInsertId();\n}\n?>",
            "expected_outputs": "1. Unauthorized users visiting `cms_publish.php` receive an HTTP 403 Forbidden response.\\n2. Valid article submissions generate an SEO-friendly URL slug and insert sanitized markup into the database.\\n3. Malicious `<script>alert('xss')</script>` tags are cleanly stripped before database storage.",
            "interpretation": "The implementation validates that role verification prior to mutation protects administration endpoints and markup filtering eliminates Stored Cross-Site Scripting.",
            "viva_qa": [
                {
                    "q": "What is the difference between Stored XSS and Reflected XSS?",
                    "a": "Stored XSS permanently injects malicious scripts into the database, executing every time any user loads that page. Reflected XSS reflects the payload immediately in the response from a transient request (e.g., search query)."
                },
                {
                    "q": "How does slug generation enhance SEO and URL readability?",
                    "a": "Slugs convert arbitrary titles into lowercase hyphenated strings containing descriptive keywords instead of cryptic numeric database IDs (e.g., `/articles/php-mysql-guide` vs `/articles?id=49`)."
                }
            ]
        },
        {
            "id": "lab_php_case3",
            "code": "BCAC591",
            "lab_name": "PHP WITH MYSQL LAB",
            "case_no": 3,
            "title": "Case 3: Real-Time Online Voting and Polling System with Race Condition Prevention",
            "objective": "Implement an online voting system ensuring one-vote-per-user integrity, preventing race conditions via database transactions and row-level locking.",
            "principle": "Electoral integrity requires atomicity: recording a vote and marking a user as having voted must succeed or fail as an indivisible unit using `START TRANSACTION`, `COMMIT`, and `ROLLBACK`.",
            "materials_setup": "PHP 8.2+, MySQL 8.0 InnoDB engine, Apache.",
            "architecture_svg": "<svg viewBox='0 0 700 130' xmlns='http://www.w3.org/2000/svg' style='width:100%;height:auto;background:#fff;border-radius:6px;border:1px solid #E5E9F1;'><rect x='30' y='25' width='160' height='80' rx='6' fill='#F7F8FC' stroke='#377FE6'/><text x='110' y='55' font-family='sans-serif' font-size='11' font-weight='700' fill='#377FE6' text-anchor='middle'>Voter Submission</text><text x='110' y='75' font-family='monospace' font-size='9' fill='#19283D' text-anchor='middle'>POST vote.php</text><path d='M 195 65 L 265 65' stroke='#377FE6' stroke-width='2'/><rect x='270' y='25' width='190' height='80' rx='6' fill='#E9E8F8' stroke='#786CE5'/><text x='365' y='55' font-family='sans-serif' font-size='11' font-weight='700' fill='#786CE5' text-anchor='middle'>InnoDB Transaction</text><text x='365' y='75' font-family='monospace' font-size='8' fill='#19283D' text-anchor='middle'>SELECT FOR UPDATE (Lock)</text><path d='M 465 65 L 535 65' stroke='#28A994' stroke-width='2'/><rect x='540' y='25' width='130' height='80' rx='6' fill='#F7F8FC' stroke='#28A994'/><text x='605' y='55' font-family='sans-serif' font-size='11' font-weight='700' fill='#28A994' text-anchor='middle'>Atomic Commit</text><text x='605' y='75' font-family='monospace' font-size='9' fill='#369B72' text-anchor='middle'>Vote Count + 1</text></svg>",
            "procedure_steps": [
                "1. Design tables `candidates` (`id`, `name`, `votes_count`) and `voters` (`id`, `user_id`, `has_voted`).",
                "2. Begin transaction via `$pdo->beginTransaction()`.",
                "3. Check voter eligibility using `SELECT has_voted FROM voters WHERE id = ? FOR UPDATE`.",
                "4. Update voter status, increment candidate votes, and execute `$pdo->commit()`."
            ],
            "full_code": "<?php\n// vote.php\nrequire_once 'db.php';\nsession_start();\n\nif (!isset($_SESSION['user_id'])) {\n    die(\"Please authenticate to cast your ballot.\");\n}\n\n$user_id = $_SESSION['user_id'];\n$candidate_id = filter_input(INPUT_POST, 'candidate_id', FILTER_VALIDATE_INT);\n\ntry {\n    $pdo->beginTransaction();\n\n    // Check voting status with exclusive row-level lock\n    $check_stmt = $pdo->prepare(\"SELECT has_voted FROM voters WHERE user_id = :uid FOR UPDATE\");\n    $check_stmt->execute(['uid' => $user_id]);\n    $voter = $check_stmt->fetch();\n\n    if ($voter && $voter['has_voted'] == 1) {\n        $pdo->rollBack();\n        die(\"Double voting prohibited. Your ballot has already been recorded.\");\n    }\n\n    // Record the vote\n    $vote_stmt = $pdo->prepare(\"UPDATE candidates SET votes_count = votes_count + 1 WHERE id = :cid\");\n    $vote_stmt->execute(['cid' => $candidate_id]);\n\n    // Update voter status\n    $status_stmt = $pdo->prepare(\"UPDATE voters SET has_voted = 1, voted_at = NOW() WHERE user_id = :uid\");\n    $status_stmt->execute(['uid' => $user_id]);\n\n    $pdo->commit();\n    echo \"Ballot successfully cast and recorded.\";\n} catch (Exception $e) {\n    if ($pdo->inTransaction()) {\n        $pdo->rollBack();\n    }\n    die(\"Transaction failed: \" . $e->getMessage());\n}\n?>",
            "expected_outputs": "1. First voting attempt increments candidate vote tally and marks voter as `has_voted = 1`.\\n2. Subsequent rapid concurrent duplicate voting attempts trigger `rollBack()` and are rejected.\\n3. Simulated database server crashes during processing trigger automated rollback, ensuring zero phantom votes.",
            "interpretation": "The experiment demonstrates that ACID transactions combined with row-level locking (`SELECT ... FOR UPDATE`) prevent double-spend and race conditions.",
            "viva_qa": [
                {
                    "q": "What is the purpose of FOR UPDATE in MySQL transactions?",
                    "a": "It applies an exclusive write lock on the queried rows, preventing other concurrent transactions from reading or updating those rows until the active transaction commits or rolls back."
                },
                {
                    "q": "Why is the MyISAM storage engine unsuitable for this voting application?",
                    "a": "MyISAM does not support transactions or row-level locking; it only supports full table-level locks, causing severe concurrency bottlenecks and risking partial data corruption during crashes. InnoDB is mandatory for transactional ACID compliance."
                }
            ]
        },
        {
            "id": "lab_php_case4",
            "code": "BCAC591",
            "lab_name": "PHP WITH MYSQL LAB",
            "case_no": 4,
            "title": "Case 4: E-Commerce Product Catalog with Multi-Facet Filtering and Cart Persistence",
            "objective": "Develop an e-commerce catalog featuring dynamic category and price filtering, product pagination, and session cart persistence.",
            "principle": "E-commerce catalogs dynamically assemble SQL queries based on client query filters using parameterized binding, while session arrays preserve cart quantities across requests.",
            "materials_setup": "PHP 8.2+, MySQL 8.0, Bootstrap 5 / Vanilla CSS, Apache.",
            "architecture_svg": "<svg viewBox='0 0 700 130' xmlns='http://www.w3.org/2000/svg' style='width:100%;height:auto;background:#fff;border-radius:6px;border:1px solid #E5E9F1;'><rect x='30' y='25' width='160' height='80' rx='6' fill='#F7F8FC' stroke='#377FE6'/><text x='110' y='55' font-family='sans-serif' font-size='11' font-weight='700' fill='#377FE6' text-anchor='middle'>Filter Controls</text><text x='110' y='75' font-family='monospace' font-size='8' fill='#19283D' text-anchor='middle'>category=electronics&amp;max=500</text><path d='M 195 65 L 265 65' stroke='#377FE6' stroke-width='2'/><rect x='270' y='25' width='180' height='80' rx='6' fill='#F7F8FC' stroke='#786CE5'/><text x='360' y='55' font-family='sans-serif' font-size='11' font-weight='700' fill='#786CE5' text-anchor='middle'>Dynamic Query Builder</text><text x='360' y='75' font-family='monospace' font-size='8' fill='#19283D' text-anchor='middle'>WHERE cat = :c AND price &lt;= :p</text><path d='M 455 65 L 525 65' stroke='#786CE5' stroke-width='2'/><rect x='530' y='25' width='140' height='80' rx='6' fill='#E9E8F8' stroke='#28A994'/><text x='600' y='55' font-family='sans-serif' font-size='11' font-weight='700' fill='#1B6F61' text-anchor='middle'>Cart Array</text><text x='600' y='75' font-family='monospace' font-size='8' fill='#369B72' text-anchor='middle'>$_SESSION['cart'][id] = qty</text></svg>",
            "procedure_steps": [
                "1. Structure schema `products` (`id`, `category_id`, `name`, `price`, `stock`).",
                "2. Construct dynamic SQL where-clause array matching active GET filter parameters.",
                "3. Execute paginated query with LIMIT and OFFSET parameters.",
                "4. Implement cart actions (`add`, `update`, `remove`) stored in `$_SESSION['cart']`."
            ],
            "full_code": "<?php\n// catalog.php\nrequire_once 'db.php';\nsession_start();\n\n$conditions = [\"1=1\"];\n$params = [];\n\nif (!empty($_GET['category'])) {\n    $conditions[] = \"category_id = :cat\";\n    $params['cat'] = (int)$_GET['category'];\n}\nif (!empty($_GET['max_price'])) {\n    $conditions[] = \"price <= :max_p\";\n    $params['max_p'] = (float)$_GET['max_price'];\n}\n\n$page = max(1, (int)($_GET['page'] ?? 1));\n$limit = 12;\n$offset = ($page - 1) * $limit;\n\n$sql = \"SELECT * FROM products WHERE \" . implode(' AND ', $conditions) . \" ORDER BY id DESC LIMIT :limit OFFSET :offset\";\n$stmt = $pdo->prepare($sql);\nforeach ($params as $k => $v) {\n    $stmt->bindValue($k, $v);\n}\n$stmt->bindValue(':limit', $limit, PDO::PARAM_INT);\n$stmt->bindValue(':offset', $offset, PDO::PARAM_INT);\n$stmt->execute();\n$products = $stmt->fetchAll();\n?>",
            "expected_outputs": "1. Selecting 'Category: Electronics' updates URL and displays matching filtered items.\\n2. Appending `max_price=2000` filters products within budget.\\n3. Clicking 'Add to Cart' updates `$_SESSION['cart'][productId]` with count.",
            "interpretation": "The dynamic parameter-bound query builder provides flexible filtering while maintaining complete security against SQL injection.",
            "viva_qa": [
                {
                    "q": "Why must LIMIT and OFFSET be explicitly bound as PDO::PARAM_INT?",
                    "a": "By default, PDO treats bound parameters as strings. MySQL syntax rejects quotes around integers in LIMIT/OFFSET clauses (e.g., `LIMIT '10'`). Explicitly specifying `PDO::PARAM_INT` ensures parameters are bound as raw integers."
                }
            ]
        },
        {
            "id": "lab_php_case5",
            "code": "BCAC591",
            "lab_name": "PHP WITH MYSQL LAB",
            "case_no": 5,
            "title": "Case 5: Event Management and Ticket Registration Portal with PDF Confirmation",
            "objective": "Build an event registration portal supporting ticket capacity tracking and automated confirmation generation.",
            "principle": "Event ticketing requires inventory decrement validations to prevent overselling past venue capacity limits.",
            "materials_setup": "PHP 8.2+, MySQL 8.0, FPDF or TCPDF library, Apache.",
            "architecture_svg": "<svg viewBox='0 0 700 130' xmlns='http://www.w3.org/2000/svg' style='width:100%;height:auto;background:#fff;border-radius:6px;border:1px solid #E5E9F1;'><rect x='30' y='25' width='160' height='80' rx='6' fill='#F7F8FC' stroke='#377FE6'/><text x='110' y='55' font-family='sans-serif' font-size='11' font-weight='700' fill='#377FE6' text-anchor='middle'>Registration Form</text><text x='110' y='75' font-family='monospace' font-size='9' fill='#19283D' text-anchor='middle'>Attendee Info</text><path d='M 195 65 L 265 65' stroke='#377FE6' stroke-width='2'/><rect x='270' y='25' width='180' height='80' rx='6' fill='#F7F8FC' stroke='#786CE5'/><text x='360' y='55' font-family='sans-serif' font-size='11' font-weight='700' fill='#786CE5' text-anchor='middle'>Capacity Gate</text><text x='360' y='75' font-family='monospace' font-size='9' fill='#19283D' text-anchor='middle'>available_seats &gt; 0</text><path d='M 455 65 L 525 65' stroke='#786CE5' stroke-width='2'/><rect x='530' y='25' width='140' height='80' rx='6' fill='#E9E8F8' stroke='#28A994'/><text x='600' y='55' font-family='sans-serif' font-size='11' font-weight='700' fill='#1B6F61' text-anchor='middle'>Ticket Issued</text><text x='600' y='75' font-family='monospace' font-size='9' fill='#369B72' text-anchor='middle'>Unique QR Code</text></svg>",
            "procedure_steps": [
                "1. Design schema `events` (`id`, `title`, `capacity`, `registered_count`) and `registrations` (`id`, `event_id`, `attendee_email`, `ticket_code`).",
                "2. Check available capacity: `capacity - registered_count > 0`.",
                "3. Insert registration record and increment `registered_count` within a transaction.",
                "4. Generate unique ticket confirmation token."
            ],
            "full_code": "<?php\n// register_event.php\nrequire_once 'db.php';\n\n$event_id = filter_input(INPUT_POST, 'event_id', FILTER_VALIDATE_INT);\n$email = filter_input(INPUT_POST, 'email', FILTER_VALIDATE_EMAIL);\n\nif (!$event_id || !$email) {\n    die(\"Invalid input parameters.\");\n}\n\ntry {\n    $pdo->beginTransaction();\n\n    $stmt = $pdo->prepare(\"SELECT capacity, registered_count FROM events WHERE id = :id FOR UPDATE\");\n    $stmt->execute(['id' => $event_id]);\n    $event = $stmt->fetch();\n\n    if (!$event || $event['registered_count'] >= $event['capacity']) {\n        $pdo->rollBack();\n        die(\"Event is sold out. No seats available.\");\n    }\n\n    $ticket_code = \"TKT-\" . strtoupper(bin2hex(random_bytes(6)));\n    $ins = $pdo->prepare(\"INSERT INTO registrations (event_id, email, ticket_code) VALUES (:eid, :email, :code)\");\n    $ins->execute(['eid' => $event_id, 'email' => $email, 'code' => $ticket_code]);\n\n    $upd = $pdo->prepare(\"UPDATE events SET registered_count = registered_count + 1 WHERE id = :id\");\n    $upd->execute(['id' => $event_id]);\n\n    $pdo->commit();\n    echo \"Registration confirmed! Your ticket code is: \" . $ticket_code;\n} catch (Exception $e) {\n    if ($pdo->inTransaction()) $pdo->rollBack();\n    die(\"Error processing registration: \" . $e->getMessage());\n}\n?>",
            "expected_outputs": "1. Successful registration generates ticket code (e.g., `TKT-A9B1C2D3E4F5`).\\n2. When `registered_count` equals `capacity`, subsequent attempts output 'Event is sold out'.",
            "interpretation": "The transactional lock prevents overselling beyond stadium or auditorium physical capacity limits.",
            "viva_qa": [
                {
                    "q": "Why is bin2hex(random_bytes(6)) preferred over rand() or mt_rand() for ticket codes?",
                    "a": "random_bytes() uses the operating system's cryptographically secure pseudo-random number generator (CSPRNG), making codes unpredictable and unguessable."
                }
            ]
        },
        {
            "id": "lab_php_case6",
            "code": "BCAC591",
            "lab_name": "PHP WITH MYSQL LAB",
            "case_no": 6,
            "title": "Case 6: Community Discussion Forum with Threaded Hierarchy and CSRF Defense",
            "objective": "Build a threaded discussion board supporting parent-child reply relationships, pagination, and anti-CSRF token verification.",
            "principle": "Threaded forum comments model hierarchical self-referencing relationships (`parent_id`), requiring anti-CSRF tokens to protect state-changing POST requests.",
            "materials_setup": "PHP 8.2+, MySQL 8.0, Apache.",
            "architecture_svg": "<svg viewBox='0 0 700 130' xmlns='http://www.w3.org/2000/svg' style='width:100%;height:auto;background:#fff;border-radius:6px;border:1px solid #E5E9F1;'><rect x='30' y='25' width='160' height='80' rx='6' fill='#F7F8FC' stroke='#377FE6'/><text x='110' y='55' font-family='sans-serif' font-size='11' font-weight='700' fill='#377FE6' text-anchor='middle'>CSRF Token</text><text x='110' y='75' font-family='monospace' font-size='9' fill='#19283D' text-anchor='middle'>hash_equals()</text><path d='M 195 65 L 265 65' stroke='#377FE6' stroke-width='2'/><rect x='270' y='25' width='180' height='80' rx='6' fill='#F7F8FC' stroke='#786CE5'/><text x='360' y='55' font-family='sans-serif' font-size='11' font-weight='700' fill='#786CE5' text-anchor='middle'>Threaded Comments</text><text x='360' y='75' font-family='monospace' font-size='9' fill='#19283D' text-anchor='middle'>parent_id -&gt; comment_id</text><path d='M 455 65 L 525 65' stroke='#786CE5' stroke-width='2'/><rect x='530' y='25' width='140' height='80' rx='6' fill='#E9E8F8' stroke='#28A994'/><text x='600' y='55' font-family='sans-serif' font-size='11' font-weight='700' fill='#1B6F61' text-anchor='middle'>Render Tree</text><text x='600' y='75' font-family='monospace' font-size='9' fill='#369B72' text-anchor='middle'>Nested Discussion</text></svg>",
            "procedure_steps": [
                "1. Design schema `forum_posts` with `id`, `parent_id` (NULL for top-level topics), `title`, `body`, and `user_id`.",
                "2. Generate hidden CSRF token via `bin2hex(random_bytes(32))` stored in `$_SESSION['csrf_token']`.",
                "3. Validate token on submission using timing-attack resistant `hash_equals()`.",
                "4. Render nested reply threads recursively."
            ],
            "full_code": "<?php\n// post_reply.php\nrequire_once 'db.php';\nsession_start();\n\nif ($_SERVER['REQUEST_METHOD'] === 'POST') {\n    // CSRF verification using timing-safe comparison\n    $submitted_token = $_POST['csrf_token'] ?? '';\n    if (!hash_equals($_SESSION['csrf_token'] ?? '', $submitted_token)) {\n        http_response_code(403);\n        die(\"CSRF token validation failed. Unauthorized request.\");\n    }\n\n    $parent_id = !empty($_POST['parent_id']) ? (int)$_POST['parent_id'] : null;\n    $body = htmlspecialchars(trim($_POST['body'] ?? ''), ENT_QUOTES, 'UTF-8');\n    $user_id = $_SESSION['user_id'];\n\n    $stmt = $pdo->prepare(\"INSERT INTO forum_posts (parent_id, user_id, body, created_at) VALUES (:pid, :uid, :body, NOW())\");\n    $stmt->execute(['pid' => $parent_id, 'uid' => $user_id, 'body' => $body]);\n\n    echo \"Reply successfully posted!\";\n}\n?>",
            "expected_outputs": "1. Valid form submission with matching CSRF token records the discussion reply.\\n2. Cross-domain requests without valid token receive HTTP 403 Forbidden.\\n3. Replies inherit `parent_id` and display indented under parent posts.",
            "interpretation": "Anti-CSRF tokens defend state-changing forum posts against Cross-Site Request Forgery, and self-referencing `parent_id` foreign keys maintain thread hierarchy.",
            "viva_qa": [
                {
                    "q": "Why is hash_equals() used instead of standard '===' for comparing security tokens?",
                    "a": "Standard string comparison terminates at the first mismatching character, leaking timing information that allows attackers to reconstruct tokens. hash_equals() performs a constant-time comparison, eliminating timing attack vectors."
                }
            ]
        }
    ],
    "bcac592": [
        {
            "id": "lab_java_case1",
            "code": "BCAC592",
            "lab_name": "Object Oriented Programming with Java Lab",
            "case_no": 1,
            "title": "Case 1: Library Book Issuing and Returning System with Fine Calculation",
            "objective": "Implement an object-oriented Library Management System modeling Books, Members, and Loan transactions with automated fine calculations and custom exception handling.",
            "principle": "Encapsulates catalog state within domain classes, enforcing business borrowing rules (loan period limits, member quotas) and throwing custom checked exceptions upon violations.",
            "materials_setup": "JDK 17+, Eclipse / IntelliJ / VS Code, terminal console.",
            "architecture_svg": "<svg viewBox='0 0 700 130' xmlns='http://www.w3.org/2000/svg' style='width:100%;height:auto;background:#fff;border-radius:6px;border:1px solid #E5E9F1;'><rect x='30' y='25' width='160' height='80' rx='6' fill='#F7F8FC' stroke='#377FE6'/><text x='110' y='55' font-family='sans-serif' font-size='11' font-weight='700' fill='#377FE6' text-anchor='middle'>Book Entity</text><text x='110' y='75' font-family='monospace' font-size='9' fill='#19283D' text-anchor='middle'>isAvailable: boolean</text><path d='M 195 65 L 265 65' stroke='#377FE6' stroke-width='2'/><rect x='270' y='25' width='180' height='80' rx='6' fill='#F7F8FC' stroke='#786CE5'/><text x='360' y='55' font-family='sans-serif' font-size='11' font-weight='700' fill='#786CE5' text-anchor='middle'>Loan Transaction</text><text x='360' y='75' font-family='monospace' font-size='9' fill='#19283D' text-anchor='middle'>issueBook() / returnBook()</text><path d='M 455 65 L 525 65' stroke='#786CE5' stroke-width='2'/><rect x='530' y='25' width='140' height='80' rx='6' fill='#E9E8F8' stroke='#28A994'/><text x='600' y='55' font-family='sans-serif' font-size='11' font-weight='700' fill='#1B6F61' text-anchor='middle'>Fine Engine</text><text x='600' y='75' font-family='monospace' font-size='9' fill='#369B72' text-anchor='middle'>Days &gt; 14: $2/day</text></svg>",
            "procedure_steps": [
                "1. Define domain classes `Book`, `Member`, and transaction manager `LibraryService`.",
                "2. Create custom exception `BookUnavailableException` extending `Exception`.",
                "3. In `issueBook()`, verify availability; mark book as issued.",
                "4. In `returnBook()`, calculate overdue days beyond standard 14-day loan period and assess fines."
            ],
            "full_code": "// LibraryApp.java\nimport java.time.LocalDate;\nimport java.time.temporal.ChronoUnit;\n\nclass BookUnavailableException extends Exception {\n    public BookUnavailableException(String msg) { super(msg); }\n}\n\nclass Book {\n    private String isbn;\n    private String title;\n    private boolean available = true;\n\n    public Book(String isbn, String title) {\n        this.isbn = isbn;\n        this.title = title;\n    }\n    public boolean isAvailable() { return available; }\n    public void setAvailable(boolean status) { this.available = status; }\n    public String getTitle() { return title; }\n}\n\npublic class LibraryApp {\n    public static void issueBook(Book book) throws BookUnavailableException {\n        if (!book.isAvailable()) {\n            throw new BookUnavailableException(\"Error: Book '\" + book.getTitle() + \"' is currently on loan.\");\n        }\n        book.setAvailable(false);\n        System.out.println(\"Book '\" + book.getTitle() + \"' successfully issued.\");\n    }\n\n    public static double calculateFine(LocalDate issueDate, LocalDate returnDate) {\n        long days = ChronoUnit.DAYS.between(issueDate, returnDate);\n        if (days > 14) {\n            return (days - 14) * 2.0; // $2 per day overdue\n        }\n        return 0.0;\n    }\n\n    public static void main(String[] args) {\n        Book b1 = new Book(\"978-0134685991\", \"Effective Java\");\n        try {\n            issueBook(b1);\n            // Simulating overdue return\n            LocalDate issued = LocalDate.now().minusDays(20);\n            LocalDate returned = LocalDate.now();\n            double fine = calculateFine(issued, returned);\n            System.out.println(\"Return processed. Overdue fine: $\" + fine);\n\n            // Attempting duplicate issue triggers exception\n            issueBook(b1);\n        } catch (BookUnavailableException e) {\n            System.err.println(\"Transaction blocked: \" + e.getMessage());\n        }\n    }\n}",
            "expected_outputs": "Book 'Effective Java' successfully issued.\\nReturn processed. Overdue fine: $12.0\\nTransaction blocked: Error: Book 'Effective Java' is currently on loan.",
            "interpretation": "The application proves encapsulation of book availability and validates that checked custom exceptions halt illegal operational transactions.",
            "viva_qa": [
                {
                    "q": "Why create a custom checked exception instead of throwing a generic RuntimeException?",
                    "a": "Checked exceptions mandate compile-time handling, forcing the calling service to handle business failure cases explicitly (e.g., prompting the student to choose an alternative title) rather than allowing the application to crash unexpectedly."
                }
            ]
        },
        {
            "id": "lab_java_case2",
            "code": "BCAC592",
            "lab_name": "Object Oriented Programming with Java Lab",
            "case_no": 2,
            "title": "Case 2: Corporate Payroll and Compensation Hierarchy System",
            "objective": "Model an employee payroll hierarchy utilizing inheritance, abstract classes, and polymorphic salary computation algorithms.",
            "principle": "Abstract superclasses define generic contracts (`calculateNetSalary()`), while derived classes (`FullTimeEmployee`, `ContractEmployee`, `Executive`) implement specific compensation models polymorphic to the caller.",
            "materials_setup": "JDK 17+, Terminal.",
            "architecture_svg": "<svg viewBox='0 0 700 130' xmlns='http://www.w3.org/2000/svg' style='width:100%;height:auto;background:#fff;border-radius:6px;border:1px solid #E5E9F1;'><rect x='270' y='10' width='160' height='40' rx='6' fill='#F7F8FC' stroke='#377FE6'/><text x='350' y='35' font-family='sans-serif' font-size='11' font-weight='700' fill='#377FE6' text-anchor='middle'>abstract Employee</text><path d='M 300 50 L 150 75' stroke='#377FE6' stroke-width='2'/><path d='M 350 50 L 350 75' stroke='#786CE5' stroke-width='2'/><path d='M 400 50 L 550 75' stroke='#28A994' stroke-width='2'/><rect x='60' y='75' width='160' height='40' rx='6' fill='#F7F8FC' stroke='#377FE6'/><text x='140' y='100' font-family='sans-serif' font-size='10' fill='#19283D' text-anchor='middle'>FullTime (Basic + DA + HRA)</text><rect x='260' y='75' width='170' height='40' rx='6' fill='#F7F8FC' stroke='#786CE5'/><text x='345' y='100' font-family='sans-serif' font-size='10' fill='#19283D' text-anchor='middle'>Contract (Hours * Rate)</text><rect x='460' y='75' width='180' height='40' rx='6' fill='#E9E8F8' stroke='#28A994'/><text x='550' y='100' font-family='sans-serif' font-size='10' font-weight='700' fill='#1B6F61' text-anchor='middle'>Executive (Salary + Stock)</text></svg>",
            "procedure_steps": [
                "1. Create abstract class `Employee` with abstract method `calculateSalary()`.",
                "2. Subclass `FullTimeEmployee` with HRA (20%), DA (10%), and PF deductions.",
                "3. Subclass `ContractEmployee` based on hourly wage and hours logged.",
                "4. Process a mixed polymorphic array of `Employee[]`, generating payroll totals."
            ],
            "full_code": "// PayrollSystem.java\nabstract class Employee {\n    protected String empId;\n    protected String name;\n\n    public Employee(String empId, String name) {\n        this.empId = empId;\n        this.name = name;\n    }\n    public abstract double calculateSalary();\n    public void printPayslip() {\n        System.out.println(\"Emp [\" + empId + \"] \" + name + \" | Net Payable: $\" + calculateSalary());\n    }\n}\n\nclass FullTimeEmployee extends Employee {\n    private double basic;\n    public FullTimeEmployee(String id, String name, double basic) {\n        super(id, name);\n        this.basic = basic;\n    }\n    @Override\n    public double calculateSalary() {\n        double hra = basic * 0.20;\n        double da = basic * 0.10;\n        double pf = basic * 0.12;\n        return basic + hra + da - pf;\n    }\n}\n\nclass ContractEmployee extends Employee {\n    private int hoursWorked;\n    private double hourlyRate;\n    public ContractEmployee(String id, String name, int hours, double rate) {\n        super(id, name);\n        this.hoursWorked = hours;\n        this.hourlyRate = rate;\n    }\n    @Override\n    public double calculateSalary() {\n        return hoursWorked * hourlyRate;\n    }\n}\n\npublic class PayrollSystem {\n    public static void main(String[] args) {\n        Employee[] payroll = {\n            new FullTimeEmployee(\"FT-101\", \"Dr. A. Sharma\", 50000),\n            new ContractEmployee(\"CT-204\", \"R. Sen\", 160, 25.0)\n        };\n\n        double total = 0;\n        for (Employee e : payroll) {\n            e.printPayslip();\n            total += e.calculateSalary();\n        }\n        System.out.println(\"Total Corporate Payroll Disbursal: $\" + total);\n    }\n}",
            "expected_outputs": "Emp [FT-101] Dr. A. Sharma | Net Payable: $59000.0\\nEmp [CT-204] R. Sen | Net Payable: $4000.0\\nTotal Corporate Payroll Disbursal: $63000.0",
            "interpretation": "Polymorphism enables the payroll engine to calculate net pay accurately without caring about the concrete type of each employee.",
            "viva_qa": [
                {
                    "q": "Why can an abstract class have constructors if it cannot be instantiated with 'new'?",
                    "a": "An abstract class constructor initializes the shared state fields inherited by subclasses and is invoked via `super()` during subclass instantiation."
                }
            ]
        },
        {
            "id": "lab_java_case3",
            "code": "BCAC592",
            "lab_name": "Object Oriented Programming with Java Lab",
            "case_no": 3,
            "title": "Case 3: Bank Account and Transaction Management with Thread-Safe Synchronization",
            "objective": "Build a multi-threaded banking transaction system that prevents overdrafts and race conditions using the synchronized keyword.",
            "principle": "Concurrent deposit and withdrawal transactions on a shared account require mutual exclusion locking via Java monitors to prevent race condition balance corruptions.",
            "materials_setup": "JDK 17+, Terminal.",
            "architecture_svg": "<svg viewBox='0 0 700 130' xmlns='http://www.w3.org/2000/svg' style='width:100%;height:auto;background:#fff;border-radius:6px;border:1px solid #E5E9F1;'><rect x='30' y='25' width='160' height='80' rx='6' fill='#F7F8FC' stroke='#377FE6'/><text x='110' y='55' font-family='sans-serif' font-size='11' font-weight='700' fill='#377FE6' text-anchor='middle'>ATM Thread A</text><text x='110' y='75' font-family='monospace' font-size='9' fill='#19283D' text-anchor='middle'>withdraw(500)</text><path d='M 195 65 L 265 65' stroke='#377FE6' stroke-width='2'/><rect x='270' y='25' width='180' height='80' rx='6' fill='#E9E8F8' stroke='#786CE5'/><text x='360' y='55' font-family='sans-serif' font-size='11' font-weight='700' fill='#786CE5' text-anchor='middle'>Synchronized Monitor</text><text x='360' y='75' font-family='monospace' font-size='9' fill='#19283D' text-anchor='middle'>Acquires Account Lock</text><path d='M 455 65 L 525 65' stroke='#28A994' stroke-width='2'/><rect x='530' y='25' width='140' height='80' rx='6' fill='#F7F8FC' stroke='#28A994'/><text x='600' y='55' font-family='sans-serif' font-size='11' font-weight='700' fill='#28A994' text-anchor='middle'>Safe Balance</text><text x='600' y='75' font-family='monospace' font-size='9' fill='#369B72' text-anchor='middle'>Zero Race Conditions</text></svg>",
            "procedure_steps": [
                "1. Design class `BankAccount` with private field `balance`.",
                "2. Mark `deposit()` and `withdraw()` with the `synchronized` modifier.",
                "3. Spawn multiple concurrent threads attempting simultaneous withdrawals.",
                "4. Verify that balance deductions occur sequentially and overdrafts are rejected."
            ],
            "full_code": "// BankingApp.java\nclass Account {\n    private double balance;\n    public Account(double initial) { this.balance = initial; }\n\n    public synchronized void withdraw(String user, double amt) {\n        if (balance >= amt) {\n            System.out.println(user + \" is initiating withdrawal of $\" + amt);\n            try { Thread.sleep(50); } catch (InterruptedException e) {}\n            balance -= amt;\n            System.out.println(user + \" completed withdrawal. New Balance: $\" + balance);\n        } else {\n            System.err.println(user + \" attempted to withdraw $\" + amt + \" but INSUFFICIENT FUNDS. Current: $\" + balance);\n        }\n    }\n}\n\npublic class BankingApp {\n    public static void main(String[] args) {\n        Account jointAccount = new Account(1000);\n\n        Thread user1 = new Thread(() -> jointAccount.withdraw(\"User 1\", 700));\n        Thread user2 = new Thread(() -> jointAccount.withdraw(\"User 2\", 500));\n\n        user1.start();\n        user2.start();\n    }\n}",
            "expected_outputs": "User 1 is initiating withdrawal of $700\\nUser 1 completed withdrawal. New Balance: $300.0\\nUser 2 attempted to withdraw $500 but INSUFFICIENT FUNDS. Current: $300.0",
            "interpretation": "The synchronized monitor enforces mutual exclusion, preventing concurrent threads from reading an outdated balance and causing double-withdrawal overdrafts.",
            "viva_qa": [
                {
                    "q": "What happens if the synchronized keyword is omitted from withdraw()?",
                    "a": "Both threads read the balance as $1000 simultaneously, both pass the balance check, and both proceed to withdraw, resulting in a negative balance ($1000 - $700 - $500 = -$200) known as a race condition."
                }
            ]
        },
        {
            "id": "lab_java_case4",
            "code": "BCAC592",
            "lab_name": "Object Oriented Programming with Java Lab",
            "case_no": 4,
            "title": "Case 4: Vehicle Rental Service Hierarchy with Interface Contracts",
            "objective": "Build a vehicle rental fleet management system utilizing multiple interfaces (Rentable, Insurable) and polymorphic rate dispatch.",
            "principle": "Demonstrates multiple interface inheritance in Java where a single concrete class (`Car`, `Truck`, `Motorcycle`) satisfies multiple functional contracts.",
            "materials_setup": "JDK 17+, Terminal.",
            "architecture_svg": "<svg viewBox='0 0 700 130' xmlns='http://www.w3.org/2000/svg' style='width:100%;height:auto;background:#fff;border-radius:6px;border:1px solid #E5E9F1;'><rect x='60' y='25' width='160' height='40' rx='6' fill='#F7F8FC' stroke='#377FE6'/><text x='140' y='50' font-family='sans-serif' font-size='11' font-weight='700' fill='#377FE6' text-anchor='middle'>&lt;&lt;Rentable&gt;&gt;</text><rect x='270' y='25' width='160' height='40' rx='6' fill='#F7F8FC' stroke='#786CE5'/><text x='350' y='50' font-family='sans-serif' font-size='11' font-weight='700' fill='#786CE5' text-anchor='middle'>&lt;&lt;Insurable&gt;&gt;</text><path d='M 140 65 L 250 85' stroke='#377FE6' stroke-width='2' stroke-dasharray='4,4'/><path d='M 350 65 L 250 85' stroke='#786CE5' stroke-width='2' stroke-dasharray='4,4'/><rect x='160' y='80' width='180' height='40' rx='6' fill='#E9E8F8' stroke='#28A994'/><text x='250' y='105' font-family='sans-serif' font-size='11' font-weight='700' fill='#1B6F61' text-anchor='middle'>Car (Implements Both)</text></svg>",
            "procedure_steps": [
                "1. Define interfaces `Rentable` (`calculateRent(int days)`) and `Insurable` (`getInsuranceCost()`).",
                "2. Implement concrete classes `SedanCar` and `CargoTruck`.",
                "3. Compute total customer checkout billing combining rental fees and insurance."
            ],
            "full_code": "// RentalSystem.java\ninterface Rentable {\n    double calculateRent(int days);\n}\n\ninterface Insurable {\n    double getInsuranceCost();\n}\n\nclass SedanCar implements Rentable, Insurable {\n    private String model;\n    private double dailyRate = 45.0;\n\n    public SedanCar(String model) { this.model = model; }\n    @Override public double calculateRent(int days) { return dailyRate * days; }\n    @Override public double getInsuranceCost() { return 15.0; }\n}\n\npublic class RentalSystem {\n    public static void main(String[] args) {\n        SedanCar car = new SedanCar(\"Honda Civic\");\n        int days = 5;\n        double total = car.calculateRent(days) + car.getInsuranceCost();\n        System.out.println(\"Vehicle Rental Invoice for 5 Days: $\" + total);\n    }\n}",
            "expected_outputs": "Vehicle Rental Invoice for 5 Days: $240.0",
            "interpretation": "Validates multiple interface inheritance, showing how an object can fulfill independent contracts cleanly.",
            "viva_qa": [
                {
                    "q": "Why does Java support multiple inheritance of interfaces but disallows multiple inheritance of classes?",
                    "a": "Multiple inheritance of classes introduces the Diamond Problem where identical method implementations in two superclasses create ambiguity. Interfaces avoid this because traditional interface methods have no state or implementation."
                }
            ]
        },
        {
            "id": "lab_java_case5",
            "code": "BCAC592",
            "lab_name": "Object Oriented Programming with Java Lab",
            "case_no": 5,
            "title": "Case 5: Warehouse Inventory Tracking System with Serialization",
            "objective": "Build an inventory management system supporting persistent object state serialization to binary storage files.",
            "principle": "Object serialization converts active in-memory object graphs into a standardized binary byte stream via `ObjectOutputStream` for disk persistence.",
            "materials_setup": "JDK 17+, Terminal.",
            "architecture_svg": "<svg viewBox='0 0 700 130' xmlns='http://www.w3.org/2000/svg' style='width:100%;height:auto;background:#fff;border-radius:6px;border:1px solid #E5E9F1;'><rect x='30' y='25' width='160' height='80' rx='6' fill='#F7F8FC' stroke='#377FE6'/><text x='110' y='55' font-family='sans-serif' font-size='11' font-weight='700' fill='#377FE6' text-anchor='middle'>InventoryItem</text><text x='110' y='75' font-family='monospace' font-size='9' fill='#19283D' text-anchor='middle'>implements Ser</text><path d='M 195 65 L 265 65' stroke='#377FE6' stroke-width='2'/><rect x='270' y='25' width='180' height='80' rx='6' fill='#E9E8F8' stroke='#786CE5'/><text x='360' y='55' font-family='sans-serif' font-size='11' font-weight='700' fill='#786CE5' text-anchor='middle'>ObjectOutputStream</text><text x='360' y='75' font-family='monospace' font-size='9' fill='#19283D' text-anchor='middle'>Binary Serialization</text><path d='M 455 65 L 525 65' stroke='#786CE5' stroke-width='2'/><rect x='530' y='25' width='140' height='80' rx='6' fill='#F7F8FC' stroke='#28A994'/><text x='600' y='55' font-family='sans-serif' font-size='11' font-weight='700' fill='#28A994' text-anchor='middle'>Disk File</text><text x='600' y='75' font-family='monospace' font-size='9' fill='#369B72' text-anchor='middle'>inventory.dat</text></svg>",
            "procedure_steps": [
                "1. Implement `Serializable` on class `InventoryItem` and declare `serialVersionUID`.",
                "2. Serialize a list of inventory items to file using `ObjectOutputStream`.",
                "3. Read back and restore objects using `ObjectInputStream`."
            ],
            "full_code": "// InventoryApp.java\nimport java.io.*;\nimport java.util.*;\n\nclass Item implements Serializable {\n    private static final long serialVersionUID = 1L;\n    private int id;\n    private String name;\n    private int quantity;\n\n    public Item(int id, String name, int qty) {\n        this.id = id; this.name = name; this.quantity = qty;\n    }\n    @Override public String toString() {\n        return \"Item #\" + id + \": \" + name + \" (Qty: \" + quantity + \")\";\n    }\n}\n\npublic class InventoryApp {\n    public static void main(String[] args) throws Exception {\n        List<Item> warehouse = Arrays.asList(new Item(101, \"Monitors\", 45), new Item(102, \"Keyboards\", 120));\n        String file = \"inventory.dat\";\n\n        // Serialization\n        try (ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream(file))) {\n            oos.writeObject(warehouse);\n            System.out.println(\"Warehouse state serialized to disk.\");\n        }\n\n        // Deserialization\n        try (ObjectInputStream ois = new ObjectInputStream(new FileInputStream(file))) {\n            @SuppressWarnings(\"unchecked\")\n            List<Item> restored = (List<Item>) ois.readObject();\n            System.out.println(\"Restored state from disk:\");\n            restored.forEach(System.out::println);\n        }\n        new File(file).delete(); // cleanup\n    }\n}",
            "expected_outputs": "Warehouse state serialized to disk.\\nRestored state from disk:\\nItem #101: Monitors (Qty: 45)\\nItem #102: Keyboards (Qty: 120)",
            "interpretation": "Validates object graph serialization and deserialization, proving that serialized in-memory collections can be accurately restored.",
            "viva_qa": [
                {
                    "q": "What happens if a field is marked with the transient modifier during serialization?",
                    "a": "The JVM skips the field during serialization; upon deserialization, the field is assigned its default type value (null for objects, 0 for numbers)."
                }
            ]
        },
        {
            "id": "lab_java_case6",
            "code": "BCAC592",
            "lab_name": "Object Oriented Programming with Java Lab",
            "case_no": 6,
            "title": "Case 6: Hotel Room Reservation System with Collections Framework",
            "objective": "Build a hotel booking system using Java Collections (HashMap, ArrayList) and Stream API filtering.",
            "principle": "Leverages the Java Collections Framework to organize room availability by room number, using Streams for declarative queries.",
            "materials_setup": "JDK 17+, Terminal.",
            "architecture_svg": "<svg viewBox='0 0 700 130' xmlns='http://www.w3.org/2000/svg' style='width:100%;height:auto;background:#fff;border-radius:6px;border:1px solid #E5E9F1;'><rect x='30' y='25' width='160' height='80' rx='6' fill='#F7F8FC' stroke='#377FE6'/><text x='110' y='55' font-family='sans-serif' font-size='11' font-weight='700' fill='#377FE6' text-anchor='middle'>HashMap&lt;Int, Room&gt;</text><text x='110' y='75' font-family='monospace' font-size='9' fill='#19283D' text-anchor='middle'>O(1) Room Lookup</text><path d='M 195 65 L 265 65' stroke='#377FE6' stroke-width='2'/><rect x='270' y='25' width='180' height='80' rx='6' fill='#F7F8FC' stroke='#786CE5'/><text x='360' y='55' font-family='sans-serif' font-size='11' font-weight='700' fill='#786CE5' text-anchor='middle'>Stream API Filter</text><text x='360' y='75' font-family='monospace' font-size='9' fill='#19283D' text-anchor='middle'>filter(!isBooked)</text><path d='M 455 65 L 525 65' stroke='#786CE5' stroke-width='2'/><rect x='530' y='25' width='140' height='80' rx='6' fill='#E9E8F8' stroke='#28A994'/><text x='600' y='55' font-family='sans-serif' font-size='11' font-weight='700' fill='#1B6F61' text-anchor='middle'>Available Suites</text><text x='600' y='75' font-family='monospace' font-size='9' fill='#369B72' text-anchor='middle'>Reservation Done</text></svg>",
            "procedure_steps": [
                "1. Model class `Room` (`roomNumber`, `type`, `price`, `isBooked`).",
                "2. Maintain inventory in a `Map<Integer, Room>`.",
                "3. Query vacant rooms using `rooms.values().stream().filter(...)`.",
                "4. Book room by updating state."
            ],
            "full_code": "// HotelApp.java\nimport java.util.*;\nimport java.util.stream.Collectors;\n\nclass Room {\n    int number;\n    String type;\n    boolean booked = false;\n\n    public Room(int n, String t) { this.number = n; this.type = t; }\n    public boolean isBooked() { return booked; }\n    public void setBooked(boolean b) { this.booked = b; }\n    @Override public String toString() {\n        return \"Room \" + number + \" (\" + type + \") - \" + (booked ? \"OCCUPIED\" : \"VACANT\");\n    }\n}\n\npublic class HotelApp {\n    public static void main(String[] args) {\n        Map<Integer, Room> hotel = new HashMap<>();\n        hotel.put(101, new Room(101, \"Deluxe\"));\n        hotel.put(102, new Room(102, \"Standard\"));\n        hotel.put(103, new Room(103, \"Suite\"));\n\n        // Book Room 101\n        hotel.get(101).setBooked(true);\n\n        // Filter vacant rooms via Java Streams\n        List<Room> vacant = hotel.values().stream()\n            .filter(r -> !r.isBooked())\n            .collect(Collectors.toList());\n\n        System.out.println(\"Vacant Rooms Available:\");\n        vacant.forEach(System.out::println);\n    }\n}",
            "expected_outputs": "Vacant Rooms Available:\\nRoom 102 (Standard) - VACANT\\nRoom 103 (Suite) - VACANT",
            "interpretation": "Demonstrates efficient O(1) room lookup via HashMap combined with functional Stream filtering.",
            "viva_qa": [
                {
                    "q": "What is the time complexity of HashMap.get() vs ArrayList.contains()?",
                    "a": "HashMap.get() provides O(1) average constant time lookup via hash calculation, whereas ArrayList.contains() requires O(n) sequential linear search."
                }
            ]
        }
    ]
}
