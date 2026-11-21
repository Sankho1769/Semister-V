# Lessons data for BCAC501: PHP WITH MYSQL

PHP_MODULES = [
    {
        "module_no": 1,
        "title": "Introduction to Web Development & Setting up Environment",
        "hours": 4,
        "marks": 5,
        "topics": [
            {
                "id": "php_m1_t1",
                "title": "Web Development Architecture: Client vs Server-Side & HTTP Request Lifecycle",
                "subtopics": ["Client-Side vs Server-Side Architecture", "HTML Basics & DOM", "Role of PHP and MySQL in Dynamic Web Applications", "HTTP Request-Response Lifecycle"],
                "intro": {
                    "definition": "Web development encompasses the creation, maintenance, and architectural design of web applications that operate over the Hypertext Transfer Protocol (HTTP/HTTPS). It is divided into client-side execution (presentation layer in the browser) and server-side execution (business logic, data persistence, and dynamic content synthesis).",
                    "background": "The early World Wide Web (Web 1.0) was strictly static, serving flat HTML files via web servers like NCSA HTTPd. The emergence of the Common Gateway Interface (CGI) in 1993, followed by Rasmus Lerdorf\'s introduction of Personal Home Page Tools (PHP) in 1994, enabled dynamic server-side content generation. Pairing PHP with the open-source relational database MySQL and Apache HTTP Server formed the legendary LAMP stack, powering over 75% of dynamic websites globally.",
                    "importance": "Understanding the separation of concerns between client-side rendering (HTML/CSS/JS) and server-side compilation (PHP/MySQL) is fundamental for software engineers. It guarantees secure data processing, transaction atomicity, scalable system architectures, and defense against unauthorized client manipulations.",
                    "objectives": [
                        "Differentiate between client-side rendering and server-side scripting paradigms.",
                        "Trace the complete lifecycle of an HTTP request from browser DNS lookup to server HTML rendering.",
                        "Explain how PHP executes scripts and interfaces with MySQL databases.",
                        "Analyze the role of HTML structural markup within dynamic server responses."
                    ]
                },
                "fundamentals": {
                    "concepts": "Client-side computing operates within the user\'s browser sandbox (HTML for structure, CSS for presentation, JavaScript for interactive behaviors). Server-side computing operates on remote web servers, executing scripts, authenticating requests, querying relational databases, and returning compiled HTML or JSON payloads.",
                    "terminology": [
                        {"term": "Client-Side", "definition": "Code executed inside the client browser engine (e.g., V8, SpiderMonkey) without direct access to the server operating system or database."},
                        {"term": "Server-Side", "definition": "Code compiled and executed on the web server before any output is transmitted to the client, concealing source code and protecting credentials."},
                        {"term": "HTTP Request-Response", "definition": "The stateless stateless application-layer communication protocol where clients transmit request verbs (GET, POST) and servers return status codes (200, 404, 500) and payloads."},
                        {"term": "LAMP/WAMP Stack", "definition": "A foundational software architecture consisting of Linux/Windows OS, Apache web server, MySQL/MariaDB database, and PHP runtime."}
                    ],
                    "principles": "1. Statelessness: HTTP does not retain state between sequential requests; servers must utilize session tokens or cookies to maintain identity.\n2. Principle of Least Privilege: Client applications are inherently untrusted; all security constraints and validation must be enforced server-side.\n3. Separation of Concerns: Presentation is decoupled from data storage and business rules.",
                    "structures": "Web Browser (User Agent) <---> Network / HTTP Protocol <---> Web Server (Apache/Nginx) <---> PHP Interpreter Engine (Zend Engine) <---> Relational Database (MySQL Server)"
                },
                "detailed_explanation": {
                    "sequence": [
                        "1. User initiates a request by typing a URL or submitting an HTML form.",
                        "2. Browser performs DNS resolution to convert the hostname into an IP address and opens a TCP/TLS connection on port 80/443.",
                        "3. Browser transmits an HTTP Request Header and optional body (in POST) to the web server.",
                        "4. The Web Server (Apache) receives the request. When it detects a .php extension, it delegates execution to the PHP runtime via mod_php or FastCGI Process Manager (PHP-FPM).",
                        "5. PHP interpreter (Zend Engine) parses, compiles script into opcodes, and executes instructions.",
                        "6. When database queries are encountered, PHP establishes a socket connection to MySQL over port 3306, executes SQL queries, and fetches result sets.",
                        "7. PHP blends dynamic database values into the HTML template and produces a pure HTML stream.",
                        "8. Web Server wraps the rendered HTML into an HTTP Response (Status 200 OK) and sends it across TCP to the client.",
                        "9. The browser parses HTML, constructs the Document Object Model (DOM), loads external assets, and renders the graphical view."
                    ],
                    "comparison_table": {
                        "headers": ["Attribute", "Client-Side Execution", "Server-Side Execution (PHP)"],
                        "rows": [
                            ["Execution Environment", "User\'s Web Browser (Chrome, Firefox, Safari)", "Web Server Infrastructure (Apache, Nginx, PHP-FPM)"],
                            ["Source Code Visibility", "Fully exposed to user via View Source / DevTools", "Completely hidden; only compiled output is visible"],
                            ["Database Access", "No direct access (security risk)", "Direct, secured access via internal network sockets"],
                            ["Processing Load", "Distributed across millions of client devices", "Concentrated on server CPU and RAM"],
                            ["Primary Technologies", "HTML5, CSS3, JavaScript, WebAssembly", "PHP, Python, Java, Node.js, Ruby, Go"]
                        ]
                    },
                    "code_architecture": "<?php\n// Server-Side PHP execution\n$user_id = 42;\n// Connect to database and retrieve dynamic user information\n$db = new mysqli(\'localhost\', \'root\', \'\', \'university_db\');\n$stmt = $db->prepare(\'SELECT username, email FROM users WHERE id = ?\');\n$stmt->bind_param(\'i\', $user_id);\n$stmt->execute();\n$result = $stmt->get_result();\n$user = $result->fetch_assoc();\n?>\n<!-- Compiled HTML sent to client -->\n<!DOCTYPE html>\n<html lang=\"en\">\n<head><title>User Profile</title></head>\n<body>\n    <h1>Welcome, <?php echo htmlspecialchars($user[\'username\']); ?>!</h1>\n    <p>Contact: <?php echo htmlspecialchars($user[\'email\']); ?></p>\n</body>\n</html>"
                },
                "diagram": {
                    "caption": "Figure 1.1: Complete Architectural Workflow of Client-Server Interaction in PHP-MySQL Applications",
                    "svg": '''<svg viewBox="0 0 800 320" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto;max-height:340px;background:#ffffff;border-radius:8px;border:1px solid #E5E9F1;box-shadow:0 2px 8px rgba(0,0,0,0.04);">
  <defs>
    <linearGradient id="clientGrad" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#8DB9F0"/><stop offset="100%" stop-color="#377FE6"/></linearGradient>
    <linearGradient id="serverGrad" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#E9E8F8"/><stop offset="100%" stop-color="#786CE5"/></linearGradient>
    <linearGradient id="dbGrad" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#28A994"/><stop offset="100%" stop-color="#1B6F61"/></linearGradient>
    <marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#377FE6"/>
    </marker>
    <marker id="arrowGreen" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#28A994"/>
    </marker>
  </defs>
  <!-- Client Box -->
  <rect x="30" y="70" width="180" height="180" rx="10" fill="#F7F8FC" stroke="#8DB9F0" stroke-width="2"/>
  <rect x="30" y="70" width="180" height="38" rx="10" fill="url(#clientGrad)"/>
  <text x="120" y="94" font-family="Inter,sans-serif" font-size="14" font-weight="700" fill="#ffffff" text-anchor="middle">CLIENT TIER</text>
  <text x="120" y="130" font-family="Inter,sans-serif" font-size="12" font-weight="600" fill="#19283D" text-anchor="middle">Web Browser</text>
  <text x="120" y="150" font-family="Inter,sans-serif" font-size="11" fill="#617087" text-anchor="middle">• DOM Tree & HTML5</text>
  <text x="120" y="170" font-family="Inter,sans-serif" font-size="11" fill="#617087" text-anchor="middle">• CSS3 Styling Engine</text>
  <text x="120" y="190" font-family="Inter,sans-serif" font-size="11" fill="#617087" text-anchor="middle">• JavaScript V8 Runtime</text>
  <rect x="55" y="212" width="130" height="24" rx="4" fill="#E9E8F8" stroke="#786CE5" stroke-width="1"/>
  <text x="120" y="228" font-family="Inter,sans-serif" font-size="10" font-weight="600" fill="#786CE5" text-anchor="middle">HTTP Client Agent</text>

  <!-- Request Arrow -->
  <path d="M 215 115 L 305 115" stroke="#377FE6" stroke-width="2.5" marker-end="url(#arrow)"/>
  <text x="260" y="105" font-family="Inter,sans-serif" font-size="10" font-weight="700" fill="#377FE6" text-anchor="middle">1. HTTP GET/POST</text>

  <!-- Response Arrow -->
  <path d="M 305 195 L 215 195" stroke="#369B72" stroke-width="2.5" marker-end="url(#arrowGreen)"/>
  <text x="260" y="215" font-family="Inter,sans-serif" font-size="10" font-weight="700" fill="#369B72" text-anchor="middle">4. HTML/CSS/JSON</text>

  <!-- Web Server Box -->
  <rect x="310" y="50" width="220" height="220" rx="10" fill="#F7F8FC" stroke="#786CE5" stroke-width="2"/>
  <rect x="310" y="50" width="220" height="38" rx="10" fill="url(#serverGrad)"/>
  <text x="420" y="74" font-family="Inter,sans-serif" font-size="14" font-weight="700" fill="#ffffff" text-anchor="middle">APPLICATION SERVER</text>
  <text x="420" y="112" font-family="Inter,sans-serif" font-size="12" font-weight="700" fill="#19283D" text-anchor="middle">Apache / Nginx Server</text>
  <line x1="330" y1="126" x2="510" y2="126" stroke="#E5E9F1" stroke-width="1.5"/>
  <rect x="330" y="136" width="180" height="70" rx="6" fill="#FFFFFF" stroke="#8DB9F0" stroke-width="1.5"/>
  <text x="420" y="156" font-family="Inter,sans-serif" font-size="12" font-weight="700" fill="#377FE6" text-anchor="middle">Zend Engine (PHP 8.x)</text>
  <text x="420" y="174" font-family="Inter,sans-serif" font-size="10" fill="#617087" text-anchor="middle">• Lexical Parser & Opcode Cache</text>
  <text x="420" y="192" font-family="Inter,sans-serif" font-size="10" fill="#617087" text-anchor="middle">• Session & Script Execution</text>
  <text x="420" y="244" font-family="Inter,sans-serif" font-size="11" font-weight="600" fill="#786CE5" text-anchor="middle">FastCGI / mod_php Socket</text>

  <!-- Database Arrow Forward -->
  <path d="M 535 125 L 595 125" stroke="#28A994" stroke-width="2.5" marker-end="url(#arrowGreen)"/>
  <text x="565" y="115" font-family="Inter,sans-serif" font-size="10" font-weight="700" fill="#28A994" text-anchor="middle">2. SQL Query</text>

  <!-- Database Arrow Back -->
  <path d="M 595 185 L 535 185" stroke="#786CE5" stroke-width="2.5" marker-end="url(#arrow)"/>
  <text x="565" y="205" font-family="Inter,sans-serif" font-size="10" font-weight="700" fill="#786CE5" text-anchor="middle">3. Recordset</text>

  <!-- Database Box -->
  <rect x="600" y="70" width="170" height="180" rx="10" fill="#F7F8FC" stroke="#28A994" stroke-width="2"/>
  <rect x="600" y="70" width="170" height="38" rx="10" fill="url(#dbGrad)"/>
  <text x="685" y="94" font-family="Inter,sans-serif" font-size="14" font-weight="700" fill="#ffffff" text-anchor="middle">DATABASE TIER</text>
  <text x="685" y="130" font-family="Inter,sans-serif" font-size="12" font-weight="600" fill="#19283D" text-anchor="middle">MySQL / MariaDB</text>
  <text x="685" y="152" font-family="Inter,sans-serif" font-size="11" fill="#617087" text-anchor="middle">• Port 3306 TCP Socket</text>
  <text x="685" y="172" font-family="Inter,sans-serif" font-size="11" fill="#617087" text-anchor="middle">• InnoDB Storage Engine</text>
  <text x="685" y="192" font-family="Inter,sans-serif" font-size="11" fill="#617087" text-anchor="middle">• ACID Transactions</text>
  <rect x="620" y="212" width="130" height="24" rx="4" fill="#E8F6F3" stroke="#28A994" stroke-width="1"/>
  <text x="685" y="228" font-family="Inter,sans-serif" font-size="10" font-weight="600" fill="#1B6F61" text-anchor="middle">Relational Schema</text>
</svg>'''
                },
                "examples": {
                    "scenario": "Online Examination Result Portal",
                    "code": "<?php\n// Real-world dynamic page request execution\nheader(\'Content-Type: text/html; charset=UTF-8\');\n$roll_no = filter_input(INPUT_GET, \'roll\', FILTER_SANITIZE_SPECIAL_CHARS);\n\nif (!$roll_no) {\n    http_response_code(400);\n    die(\'<h1>Error 400: Roll number required.</h1>\');\n}\n\n// Mocking secure DB retrieval\n$student = [\'name\' => \'Aarav Sharma\', \'sem\' => \'Semester V\', \'grade\' => \'A+\'];\n?>\n<div class=\"result-card\">\n    <h2>MAKAUT Semester V Examination Result</h2>\n    <p>Student Name: <strong><?= $student[\'name\'] ?></strong></p>\n    <p>Roll: <?= htmlspecialchars($roll_no) ?></p>\n    <p>Status: <span style=\"color:green;font-weight:bold;\">PASSED (<?= $student[\'grade\'] ?>)</span></p>\n</div>"
                },
                "important_points": [
                    "Client-side code executes entirely within the browser sandbox and cannot directly inspect or modify server-side database tables securely.",
                    "PHP is an interpreted, server-side scripting language embedded directly within HTML tags using the `<?php ... ?>` delimiter.",
                    "HTTP is inherently stateless; every request from the browser is treated as completely independent by the web server unless session tracking mechanisms are introduced.",
                    "Apache uses multi-processing modules (MPM) and interfaces with PHP using FastCGI (PHP-FPM) or mod_php.",
                    "The client never sees PHP code; the web server transmits only the compiled output (HTML, CSS, JSON, XML).",
                    "Security validation must always be conducted on the server tier, as client-side checks can be bypassed using tools like curl or Postman."
                ],
                "revision": {
                    "summary": "Web development relies on a three-tier architecture: the Client Tier (presentation), the Application Tier (Apache + PHP Zend Engine), and the Database Tier (MySQL). HTTP coordinates communication via stateless requests and responses.",
                    "terminology": "Client-Side, Server-Side, Zend Engine, HTTP Request/Response, FastCGI, LAMP/WAMP.",
                    "mechanisms": "DNS Resolution -> TCP Handshake -> HTTP Request -> Apache Routing -> PHP Compilation -> MySQL Socket Query -> HTML Rendering -> HTTP Response -> DOM Construction.",
                    "common_mistakes": "Assuming client-side JavaScript validation is sufficient for security. In reality, attackers can bypass all browser validation by submitting raw HTTP requests directly to PHP endpoints."
                }
            },
            {
                "id": "php_m1_t2",
                "title": "Development Environment Setup: XAMPP, WAMP, Apache, MySQL & PHP Configuration",
                "subtopics": ["XAMPP vs WAMP Architecture", "Apache Web Server Configuration (httpd.conf)", "PHP Engine Runtime Tuning (php.ini)", "MySQL Daemon Configuration (my.ini)"],
                "intro": {
                    "definition": "A local web development environment provides an isolated software stack simulating a production web server on a developer\'s local operating system. XAMPP (Cross-Platform, Apache, MariaDB/MySQL, PHP, Perl) and WAMP (Windows, Apache, MySQL, PHP) package these server daemons into a unified, installable bundle.",
                    "background": "Historically, configuring an Apache web server alongside PHP and MySQL required manual compilation from source code, configuring shared libraries, and binding system ports. Integrated development stacks like XAMPP (developed by Apache Friends) simplified this by pre-compiling all dependencies into self-contained directory trees.",
                    "importance": "Proficiency in environment configuration enables developers to diagnose port binding conflicts (e.g., IIS or Skype blocking port 80), fine-tune memory limits, adjust file upload thresholds, and configure error logging required for university projects and enterprise applications.",
                    "objectives": [
                        "Configure and run Apache and MySQL services via XAMPP/WAMP control managers.",
                        "Modify `php.ini` directives for error reporting, memory allocation, and file uploads.",
                        "Resolve common port collisions on port 80 (HTTP) and port 3306 (MySQL).",
                        "Configure local virtual hosts and document root directories in Apache."
                    ]
                },
                "fundamentals": {
                    "concepts": "The local server environment runs Apache listening on port 80/443 and MySQL listening on port 3306. Requests addressed to `http://localhost` resolve to the loopback IP `127.0.0.1`, which Apache routes to the web root directory (`htdocs` in XAMPP, `www` in WAMP).",
                    "terminology": [
                        {"term": "htdocs / www", "definition": "The public document root directory of the web server where executable PHP scripts and static assets must reside."},
                        {"term": "php.ini", "definition": "The central configuration file for the PHP interpreter engine controlling runtime behavior, execution time, error display, and extensions."},
                        {"term": "httpd.conf", "definition": "The primary configuration text file for the Apache HTTP daemon regulating listening ports, virtual hosts, and directory access permissions."},
                        {"term": "Loopback Address (127.0.0.1)", "definition": "The standard IP address reserved for establishing network connections back to the local host machine."}
                    ],
                    "principles": "1. Port Isolation: Each listening service requires a unique TCP port.\n2. Directory Security: The web server should restrict directory indexing (`Options -Indexes`) to prevent file enumeration.\n3. Verbose Local Debugging: Error reporting (`display_errors = On`) should be activated in development, but strictly disabled in production.",
                    "structures": "C:\xampp\htdocs\ <--- Web Root | C:\xampp\php\php.ini <--- PHP Config | C:\xampp\apache\conf\httpd.conf <--- Apache Config | C:\xampp\mysql\bin\my.ini <--- MySQL Config"
                },
                "detailed_explanation": {
                    "sequence": [
                        "1. Download and run the XAMPP installer with administrative privileges.",
                        "2. Select core components: Apache, MySQL, PHP, and phpMyAdmin (uncheck FileZilla and Mercury if not needed).",
                        "3. Launch XAMPP Control Panel. Start Apache and MySQL services.",
                        "4. If Apache fails with error 'Port 80 in use by PID 4 (System)', edit `httpd.conf` to change `Listen 80` to `Listen 8080`, or disable the conflicting Windows World Wide Web Publishing Service (W3SVC).",
                        "5. If MySQL fails on port 3306, inspect running services for a pre-existing standalone MySQL installation.",
                        "6. Navigate to `http://localhost/` in the web browser to verify successful installation.",
                        "7. Access `http://localhost/phpmyadmin` to verify graphical MySQL database administration.",
                        "8. Create a new directory `C:\xampp\htdocs\bca_project` and save an `index.php` containing `<?php phpinfo(); ?>`.",
                        "9. Access `http://localhost/bca_project/index.php` to inspect all compiled modules and configuration settings."
                    ],
                    "comparison_table": {
                        "headers": ["Configuration Directive", "Default Development Value", "Production Recommended Value", "Functional Significance"],
                        "rows": [
                            ["display_errors", "On", "Off", "Prevents sensitive system path disclosure to potential attackers."],
                            ["error_reporting", "E_ALL", "E_ALL & ~E_DEPRECATED & ~E_STRICT", "Ensures strict runtime validation during local testing."],
                            ["upload_max_filesize", "2M", "20M - 64M", "Dictates the maximum size of single file uploads allowed through HTTP POST."],
                            ["post_max_size", "8M", "32M - 128M", "Must be larger than upload_max_filesize to accommodate multipart form payloads."],
                            ["memory_limit", "128M / 512M", "256M - 1024M", "Upper limit of RAM a single PHP script execution thread can consume."]
                        ]
                    },
                    "code_architecture": "# Key modifications in php.ini\nerror_reporting = E_ALL\ndisplay_errors = On\ndisplay_startup_errors = On\nmax_execution_time = 300\nmemory_limit = 256M\npost_max_size = 64M\nupload_max_filesize = 32M\ndate.timezone = \"Asia/Kolkata\""
                },
                "diagram": {
                    "caption": "Figure 1.2: Local Development Architecture in XAMPP Environment",
                    "svg": '''<svg viewBox="0 0 800 280" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto;max-height:300px;background:#ffffff;border-radius:8px;border:1px solid #E5E9F1;box-shadow:0 2px 8px rgba(0,0,0,0.04);">
  <defs>
    <linearGradient id="boxGrad" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#E9E8F8"/><stop offset="100%" stop-color="#8DB9F0"/></linearGradient>
  </defs>
  <!-- Main Frame -->
  <rect x="20" y="20" width="760" height="240" rx="12" fill="#F7F8FC" stroke="#377FE6" stroke-width="2"/>
  <rect x="20" y="20" width="760" height="36" rx="12" fill="#377FE6"/>
  <text x="400" y="44" font-family="Inter,sans-serif" font-size="14" font-weight="700" fill="#ffffff" text-anchor="middle">XAMPP / WAMP LOCAL STACK ARCHITECTURE (127.0.0.1 / localhost)</text>

  <!-- Apache Service -->
  <rect x="50" y="75" width="210" height="160" rx="8" fill="#ffffff" stroke="#786CE5" stroke-width="1.5"/>
  <rect x="50" y="75" width="210" height="28" rx="8" fill="#786CE5"/>
  <text x="155" y="94" font-family="Inter,sans-serif" font-size="12" font-weight="700" fill="#ffffff" text-anchor="middle">APACHE HTTP SERVER</text>
  <text x="65" y="125" font-family="Inter,sans-serif" font-size="11" fill="#19283D">• TCP Port: <tspan font-weight="700" fill="#377FE6">80 / 8080</tspan></text>
  <text x="65" y="145" font-family="Inter,sans-serif" font-size="11" fill="#19283D">• Config: <tspan font-family="monospace" fill="#786CE5">httpd.conf</tspan></text>
  <text x="65" y="165" font-family="Inter,sans-serif" font-size="11" fill="#19283D">• Document Root:</text>
  <text x="75" y="185" font-family="monospace" font-size="10" fill="#28A994">C:/xampp/htdocs</text>
  <text x="65" y="210" font-family="Inter,sans-serif" font-size="11" fill="#617087">• Multi-Processing Module</text>

  <!-- PHP Runtime -->
  <rect x="295" y="75" width="210" height="160" rx="8" fill="#ffffff" stroke="#377FE6" stroke-width="1.5"/>
  <rect x="295" y="75" width="210" height="28" rx="8" fill="#377FE6"/>
  <text x="400" y="94" font-family="Inter,sans-serif" font-size="12" font-weight="700" fill="#ffffff" text-anchor="middle">PHP ZEND ENGINE</text>
  <text x="310" y="125" font-family="Inter,sans-serif" font-size="11" fill="#19283D">• Runtime Version: <tspan font-weight="700">8.2 / 8.3</tspan></text>
  <text x="310" y="145" font-family="Inter,sans-serif" font-size="11" fill="#19283D">• Master Config: <tspan font-family="monospace" fill="#786CE5">php.ini</tspan></text>
  <text x="310" y="165" font-family="Inter,sans-serif" font-size="11" fill="#19283D">• Extensions Loaded:</text>
  <text x="320" y="185" font-family="monospace" font-size="10" fill="#EF846B">mysqli, pdo_mysql, curl, mbstring</text>
  <text x="310" y="210" font-family="Inter,sans-serif" font-size="11" fill="#617087">• CLI & FastCGI Interfaces</text>

  <!-- MySQL Service -->
  <rect x="540" y="75" width="210" height="160" rx="8" fill="#ffffff" stroke="#28A994" stroke-width="1.5"/>
  <rect x="540" y="75" width="210" height="28" rx="8" fill="#28A994"/>
  <text x="645" y="94" font-family="Inter,sans-serif" font-size="12" font-weight="700" fill="#ffffff" text-anchor="middle">MYSQL / MARIADB</text>
  <text x="555" y="125" font-family="Inter,sans-serif" font-size="11" fill="#19283D">• TCP Port: <tspan font-weight="700" fill="#28A994">3306</tspan></text>
  <text x="555" y="145" font-family="Inter,sans-serif" font-size="11" fill="#19283D">• Config File: <tspan font-family="monospace" fill="#786CE5">my.ini</tspan></text>
  <text x="555" y="165" font-family="Inter,sans-serif" font-size="11" fill="#19283D">• Admin UI: <tspan font-weight="600" fill="#377FE6">phpMyAdmin</tspan></text>
  <text x="555" y="185" font-family="Inter,sans-serif" font-size="11" fill="#617087">• Default User: <tspan font-weight="700">root</tspan></text>
  <text x="555" y="210" font-family="Inter,sans-serif" font-size="11" fill="#617087">• Storage: InnoDB Engine</text>
</svg>'''
                },
                "examples": {
                    "scenario": "Verifying System Configuration via Diagnostic Script",
                    "code": "<?php\n// File: C:/xampp/htdocs/test_env.php\necho \"<h2>Environment Diagnostic Report</h2>\";\necho \"PHP Version: \" . phpversion() . \"<br>\";\necho \"Loaded Extensions: <br>\";\n$extensions = [\'mysqli\', \'pdo_mysql\', \'mbstring\', \'openssl\'];\nforeach ($extensions as $ext) {\n    $status = extension_loaded($ext) ? \'<span style=\"color:green;\">ENABLED</span>\' : \'<span style=\"color:red;\">DISABLED</span>\';\n    echo \"Extension <strong>$ext</strong>: $status<br>\";\n}\n\n// Test MySQL Connectivity on 3306\n$conn = @new mysqli(\'localhost\', \'root\', \'\');\nif ($conn->connect_error) {\n    echo \"<p style=\'color:red;\'>MySQL Connection Failed: \" . $conn->connect_error . \"</p>\";\n} else {\n    echo \"<p style=\'color:green;\'>MySQL Connected Successfully to 127.0.0.1:3306!</p>\";\n}\n?>"
                },
                "important_points": [
                    "XAMPP is an all-in-one distribution packaging Apache, MariaDB/MySQL, PHP, and Perl.",
                    "The default web directory in XAMPP on Windows is `C:\xampp\htdocs`; files placed here are accessed via `http://localhost/`.",
                    "Port 80 conflicts commonly occur when Skype, VMware, or Windows IIS (World Wide Web Publishing Service) are running simultaneously.",
                    "The `php.ini` configuration file controls vital runtime parameters including `upload_max_filesize`, `post_max_size`, and `display_errors`.",
                    "Never run production databases using the default XAMPP root user with an empty password; passwords must be assigned via `mysqladmin` or phpMyAdmin.",
                    "The `phpinfo()` function generates a comprehensive report of all compiled PHP modules, environment variables, and active ini directives."
                ],
                "revision": {
                    "summary": "Setting up XAMPP or WAMP establishes an isolated local environment for Apache (HTTP), MySQL (RDBMS), and PHP runtime. Modifying configuration files (`httpd.conf`, `php.ini`, `my.ini`) is essential for debugging and performance tuning.",
                    "terminology": "XAMPP, WAMP, htdocs, php.ini, httpd.conf, loopback, port 80, port 3306, phpMyAdmin.",
                    "mechanisms": "Browser request to localhost -> DNS resolves to 127.0.0.1 -> Apache listener intercepts port 80 -> Handler executes PHP -> Output returned to browser.",
                    "common_mistakes": "Forgetting that editing `php.ini` requires restarting the Apache service in XAMPP Control Panel for modifications to take effect."
                }
            }
        ]
    }
]
