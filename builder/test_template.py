import json, os

def make_php_data():
    modules = [
        {
            'module_no': 1,
            'title': 'Introduction to Web Development & Setting up Environment',
            'hours': 4,
            'marks': 5,
            'topics': [
                {
                    'id': 'php_m1_t1',
                    'title': 'Web Development Architecture: Client vs Server-Side & HTTP Request Lifecycle',
                    'subtopics': ['Client-Side vs Server-Side Architecture', 'HTML Basics & DOM', 'Role of PHP and MySQL in Dynamic Web Applications', 'HTTP Request-Response Lifecycle'],
                    'intro': {
                        'definition': 'Web development encompasses the creation, maintenance, and architectural design of web applications operating across the World Wide Web. It is divided into client-side computing (presentation and interaction in the browser) and server-side computing (business logic, persistent data processing, and dynamic markup synthesis).',
                        'background': 'The early Web was strictly static, serving flat HTML files. The emergence of CGI in 1993, followed by Rasmus Lerdorf creating PHP in 1994, enabled dynamic server-side content generation. Pairing PHP with MySQL and Apache formed the legendary LAMP stack, powering over 75% of dynamic websites globally.',
                        'importance': 'Understanding the client-server separation guarantees application security, data integrity, transactional atomicity, and scalable distributed system design.',
                        'objectives': [
                            'Differentiate client-side rendering from server-side script execution.',
                            'Trace the end-to-end lifecycle of an HTTP request from DNS lookup to HTML rendering.',
                            'Explain how PHP executes scripts and interfaces with MySQL databases.',
                            'Analyze DOM construction and server-side markup generation.'
                        ]
                    },
                    'fundamentals': {
                        'concepts': 'Client-side computing executes within the restricted sandbox of the web browser using HTML5, CSS3, and JavaScript. Server-side computing executes on host operating systems, orchestrating database transactions, session persistence, and API integrations.',
                        'terminology': [
                            {'term': 'Client-Side', 'definition': 'Code executed inside the browser engine without direct access to host storage or backend databases.'},
                            {'term': 'Server-Side', 'definition': 'Code compiled and executed on remote servers prior to transmission, concealing credentials and proprietary business logic.'},
                            {'term': 'HTTP Protocol', 'definition': 'Stateless application-layer protocol coordinating request verbs (GET, POST, PUT, DELETE) and status responses (200, 404, 500).'},
                            {'term': 'LAMP Stack', 'definition': 'Open-source enterprise software stack: Linux OS, Apache HTTP Server, MySQL/MariaDB RDBMS, and PHP engine.'}
                        ],
                        'principles': '1. Statelessness: HTTP retains no conversational state between discrete requests without cookies or tokens.\\n2. Zero-Trust Client: Client input must always be validated server-side as browsers can be manipulated.\\n3. Separation of Concerns: Presentation is decoupled from data modeling and application logic.',
                        'structures': 'User Agent (Browser) <== Network / HTTP ==> Web Server (Apache) <== FastCGI ==> PHP Zend Engine <== TCP 3306 ==> MySQL Server'
                    },
                    'detailed_explanation': {
                        'sequence': [
                            '1. User initiates a request by submitting a URL or clicking an action button.',
                            '2. The browser resolves the hostname to an IP address via DNS lookup and establishes a TCP handshake on port 80/443.',
                            '3. The browser sends an HTTP request payload containing headers, cookies, and parameters.',
                            '4. The Apache web server accepts the connection and identifies requested file types.',
                            '5. For .php files, Apache forwards the request to the PHP interpreter via FastCGI (PHP-FPM) or mod_php.',
                            '6. The Zend Engine compiles PHP code to intermediate opcodes and executes the logic.',
                            '7. If data is required, PHP establishes a socket connection to MySQL on port 3306 and runs SQL queries.',
                            '8. MySQL executes queries and returns relational recordsets back to the PHP process.',
                            '9. PHP embeds dynamic data into HTML templates and streams the output to Apache.',
                            '10. Apache wraps the response into an HTTP 200 payload and transmits it back to the client browser for rendering.'
                        ],
                        'comparison_table': {
                            'headers': ['Architectural Dimension', 'Client-Side Execution', 'Server-Side Execution (PHP)'],
                            'rows': [
                                ['Runtime Environment', 'Web Browser (Chrome V8, Firefox Gecko)', 'Server Host (Apache / PHP-FPM / CLI)'],
                                ['Code Visibility', 'Completely exposed via DevTools', 'Fully private and protected on server'],
                                ['Database Communication', 'Blocked directly due to security risks', 'Full authorized access via internal sockets'],
                                ['Processing Load', 'Distributed over user hardware', 'Concentrated on server CPU and RAM'],
                                ['Primary Technologies', 'HTML5, CSS3, JavaScript, WebAssembly', 'PHP, Python, Java, Node.js, Go']
                            ]
                        },
                        'code_architecture': '<?php\\n// Server-Side Dynamic Generation\\n$userId = 101;\\n$db = new mysqli(\'localhost\', \'root\', \'\', \'makaut_portal\');\\n$stmt = $db->prepare(\'SELECT name, course, cgpa FROM students WHERE id = ?\');\\n$stmt->bind_param(\'i\', $userId);\\n$stmt->execute();\\n$student = $stmt->get_result()->fetch_assoc();\\n?>\\n<!DOCTYPE html>\\n<html>\\n<body>\\n  <h1>Student Profile: <?= htmlspecialchars($student[\'name\']) ?></h1>\\n  <p>Enrolled Course: <?= htmlspecialchars($student[\'course\']) ?></p>\\n  <p>Current CGPA: <strong><?= number_format($student[\'cgpa\'], 2) ?></strong></p>\\n</body>\\n</html>'
                    },
                    'diagram': {
                        'caption': 'Figure 1.1: Complete Architectural Workflow of Client-Server Interaction in PHP-MySQL Applications',
                        'svg': "<svg viewBox='0 0 800 260' xmlns='http://www.w3.org/2000/svg' style='width:100%;height:auto;max-height:260px;background:#ffffff;border-radius:8px;border:1px solid #E5E9F1;'><rect x='25' y='40' width='180' height='180' rx='10' fill='#F7F8FC' stroke='#8DB9F0' stroke-width='2'/><rect x='25' y='40' width='180' height='36' rx='10' fill='#377FE6'/><text x='115' y='63' font-family='sans-serif' font-size='13' font-weight='700' fill='#ffffff' text-anchor='middle'>CLIENT TIER</text><text x='115' y='100' font-family='sans-serif' font-size='12' font-weight='600' fill='#19283D' text-anchor='middle'>Web Browser</text><text x='115' y='125' font-family='sans-serif' font-size='11' fill='#617087' text-anchor='middle'>• DOM &amp; HTML5</text><text x='115' y='145' font-family='sans-serif' font-size='11' fill='#617087' text-anchor='middle'>• CSS3 Styles</text><text x='115' y='165' font-family='sans-serif' font-size='11' fill='#617087' text-anchor='middle'>• JavaScript Runtime</text><rect x='45' y='185' width='140' height='22' rx='4' fill='#E9E8F8'/><text x='115' y='200' font-family='sans-serif' font-size='10' font-weight='600' fill='#786CE5' text-anchor='middle'>User Agent</text><path d='M 210 90 L 305 90' stroke='#377FE6' stroke-width='2.5'/><text x='258' y='80' font-family='sans-serif' font-size='10' font-weight='700' fill='#377FE6' text-anchor='middle'>1. HTTP GET/POST</text><path d='M 305 160 L 210 160' stroke='#28A994' stroke-width='2.5'/><text x='258' y='180' font-family='sans-serif' font-size='10' font-weight='700' fill='#28A994' text-anchor='middle'>4. HTML Response</text><rect x='310' y='30' width='220' height='200' rx='10' fill='#F7F8FC' stroke='#786CE5' stroke-width='2'/><rect x='310' y='30' width='220' height='36' rx='10' fill='#786CE5'/><text x='420' y='53' font-family='sans-serif' font-size='13' font-weight='700' fill='#ffffff' text-anchor='middle'>SERVER TIER</text><text x='420' y='90' font-family='sans-serif' font-size='12' font-weight='700' fill='#19283D' text-anchor='middle'>Apache HTTP Server</text><rect x='330' y='105' width='180' height='60' rx='6' fill='#FFFFFF' stroke='#8DB9F0' stroke-width='1.5'/><text x='420' y='125' font-family='sans-serif' font-size='11' font-weight='700' fill='#377FE6' text-anchor='middle'>PHP 8.x Zend Engine</text><text x='420' y='145' font-family='sans-serif' font-size='10' fill='#617087' text-anchor='middle'>Opcode Compilation</text><text x='420' y='205' font-family='sans-serif' font-size='10' font-weight='600' fill='#786CE5' text-anchor='middle'>FastCGI / mod_php Process</text><path d='M 535 95 L 595 95' stroke='#28A994' stroke-width='2.5'/><text x='565' y='85' font-family='sans-serif' font-size='10' font-weight='700' fill='#28A994' text-anchor='middle'>2. SQL Query</text><path d='M 595 155 L 535 155' stroke='#377FE6' stroke-width='2.5'/><text x='565' y='175' font-family='sans-serif' font-size='10' font-weight='700' fill='#377FE6' text-anchor='middle'>3. Recordset</text><rect x='600' y='40' width='175' height='180' rx='10' fill='#F7F8FC' stroke='#28A994' stroke-width='2'/><rect x='600' y='40' width='175' height='36' rx='10' fill='#28A994'/><text x='687' y='63' font-family='sans-serif' font-size='13' font-weight='700' fill='#ffffff' text-anchor='middle'>DATABASE TIER</text><text x='687' y='100' font-family='sans-serif' font-size='12' font-weight='600' fill='#19283D' text-anchor='middle'>MySQL Server (3306)</text><text x='687' y='125' font-family='sans-serif' font-size='11' fill='#617087' text-anchor='middle'>• InnoDB Storage</text><text x='687' y='145' font-family='sans-serif' font-size='11' fill='#617087' text-anchor='middle'>• Relational Schema</text><rect x='620' y='180' width='135' height='22' rx='4' fill='#E8F6F3'/><text x='687' y='195' font-family='sans-serif' font-size='10' font-weight='600' fill='#1B6F61' text-anchor='middle'>Persistent Tables</text></svg>"
                    },
                    'examples': {
                        'scenario': 'Live University Portal Result Lookup',
                        'code': '<?php\\nheader(\'Content-Type: text/html; charset=UTF-8\');\\n$roll = filter_input(INPUT_GET, \'roll\', FILTER_SANITIZE_SPECIAL_CHARS);\\nif (!$roll) { die(\'<p>Roll missing</p>\'); }\\n$student = [\'name\' => \'Sourav Ghosh\', \'course\' => \'BCA Sem V\', \'grade\' => \'O\'];\\necho \"Student: \" . htmlspecialchars($student[\'name\']) . \" Result: \" . $student[\'grade\'];\\n?>'
                    },
                    'important_points': [
                        'Client-side scripts run inside browser sandboxes without direct OS or database access.',
                        'PHP is an interpreted, server-side language that outputs compiled markup to the client.',
                        'HTTP is inherently stateless; state management requires cookies or sessions.',
                        'The client never receives raw PHP script code; only the resulting HTML output is transmitted.',
                        'Validation must be executed on the server side because client-side checks can be bypassed.'
                    ],
                    'revision': {
                        'summary': 'Three-tier architecture separates client presentation, server application logic, and database persistence. HTTP links the client and server via stateless request-response transactions.',
                        'terminology': 'Client-side, Server-side, Zend Engine, HTTP protocol, LAMP stack.',
                        'mechanisms': 'DNS -> TCP handshake -> HTTP Request -> Apache -> PHP Compilation -> MySQL Query -> HTML Stream -> DOM Parsing.',
                        'common_mistakes': 'Believing client-side JavaScript validation provides security against malicious data submission.'
                    }
                },
                {
                    'id': 'php_m1_t2',
                    'title': 'Development Environment Setup: Installation of XAMPP/WAMP, Apache, MySQL & PHP Configuration',
                    'subtopics': ['XAMPP vs WAMP Architecture', 'Apache Web Server Configuration (httpd.conf)', 'PHP Engine Runtime Tuning (php.ini)', 'MySQL Daemon Configuration (my.ini)'],
                    'intro': {
                        'definition': 'A local development environment bundles the Apache web server, MySQL/MariaDB database, and PHP runtime into an integrated desktop installation, enabling offline development without remote hosting.',
                        'background': 'Historically, compiling Apache, PHP, and MySQL individually on Windows required manual configuration of binaries, C++ runtimes, and ports. Bundled suites like XAMPP and WAMP streamlined this workflow with unified graphical controls.',
                        'importance': 'Configuring web daemons, adjusting memory limits, tuning upload sizes, and troubleshooting port 80 collisions are fundamental administrative skills for web engineers.',
                        'objectives': [
                            'Install and configure Apache, MySQL, and PHP via XAMPP Control Manager.',
                            'Tune runtime directives in php.ini including display_errors and memory_limit.',
                            'Resolve network port collisions on ports 80, 443, and 3306.',
                            'Configure document roots and virtual host directories.'
                        ]
                    },
                    'fundamentals': {
                        'concepts': 'XAMPP runs Apache on port 80 and MySQL on port 3306. Requests to http://localhost route to loopback address 127.0.0.1, pointing to the htdocs directory.',
                        'terminology': [
                            {'term': 'htdocs', 'definition': 'The default public document root directory where web files are served from.'},
                            {'term': 'php.ini', 'definition': 'The master configuration file regulating PHP runtime memory, error reporting, and extensions.'},
                            {'term': 'httpd.conf', 'definition': 'The central configuration file governing Apache web server behavior and port bindings.'},
                            {'term': 'Loopback (127.0.0.1)', 'definition': 'Standard IP address assigned to the local host network interface.'}
                        ],
                        'principles': '1. Port Exclusivity: Only one operating system process can bind to a specific TCP port simultaneously.\\n2. Least Privilege: Secure default administrative credentials before deployment.\\n3. Verbose Local Debugging: Enable full error reporting in development while suppressing it in production.',
                        'structures': 'C:\\xampp\\htdocs\\ <--- Web Root | C:\\xampp\\php\\php.ini <--- PHP Config | C:\\xampp\\apache\\conf\\httpd.conf <--- Apache Config'
                    },
                    'detailed_explanation': {
                        'sequence': [
                            '1. Download and run the XAMPP installer on Windows.',
                            '2. Select Apache, MySQL, and phpMyAdmin components.',
                            '3. Launch XAMPP Control Panel and start Apache and MySQL.',
                            '4. If port 80 is occupied by Windows IIS, change the port in httpd.conf to 8080.',
                            '5. If port 3306 is occupied, reconfigure my.ini to port 3307.',
                            '6. Navigate to http://localhost/phpmyadmin to verify MySQL database management.',
                            '7. Create a project directory in C:\\xampp\\htdocs\\bca_portal.',
                            '8. Adjust upload_max_filesize = 32M and post_max_size = 64M in php.ini.',
                            '9. Restart Apache service in the control panel to apply php.ini adjustments.'
                        ],
                        'comparison_table': {
                            'headers': ['Directive', 'Development Value', 'Production Value', 'Significance'],
                            'rows': [
                                ['display_errors', 'On', 'Off', 'Prevents sensitive path disclosure to users'],
                                ['error_reporting', 'E_ALL', 'E_ALL & ~E_DEPRECATED', 'Enforces strict local code quality'],
                                ['upload_max_filesize', '32M', '10M', 'Maximum size of a single uploaded file'],
                                ['post_max_size', '64M', '20M', 'Maximum size of entire HTTP POST request body']
                            ]
                        },
                        'code_architecture': '# Recommended php.ini Directives\\nerror_reporting = E_ALL\\ndisplay_errors = On\\nmax_execution_time = 300\\nmemory_limit = 256M\\npost_max_size = 64M\\nupload_max_filesize = 32M\\ndate.timezone = "Asia/Kolkata"'
                    },
                    'diagram': {
                        'caption': 'Figure 1.2: Local Development Architecture and Directory Paths in XAMPP',
                        'svg': "<svg viewBox='0 0 800 240' xmlns='http://www.w3.org/2000/svg' style='width:100%;height:auto;max-height:240px;background:#ffffff;border-radius:8px;border:1px solid #E5E9F1;'><rect x='20' y='20' width='760' height='200' rx='10' fill='#F7F8FC' stroke='#377FE6' stroke-width='2'/><rect x='20' y='20' width='760' height='34' rx='10' fill='#377FE6'/><text x='400' y='43' font-family='sans-serif' font-size='13' font-weight='700' fill='#ffffff' text-anchor='middle'>XAMPP LOCAL STACK ARCHITECTURE (127.0.0.1 / localhost)</text><rect x='40' y='70' width='220' height='130' rx='8' fill='#ffffff' stroke='#786CE5' stroke-width='1.5'/><text x='150' y='95' font-family='sans-serif' font-size='12' font-weight='700' fill='#786CE5' text-anchor='middle'>Apache (Port 80/8080)</text><text x='55' y='125' font-family='sans-serif' font-size='11' fill='#19283D'>• Document Root: /htdocs</text><text x='55' y='150' font-family='sans-serif' font-size='11' fill='#19283D'>• Config: httpd.conf</text><text x='55' y='175' font-family='sans-serif' font-size='11' fill='#617087'>• MPM Multi-threading</text><rect x='290' y='70' width='220' height='130' rx='8' fill='#ffffff' stroke='#377FE6' stroke-width='1.5'/><text x='400' y='95' font-family='sans-serif' font-size='12' font-weight='700' fill='#377FE6' text-anchor='middle'>PHP 8.x Engine</text><text x='305' y='125' font-family='sans-serif' font-size='11' fill='#19283D'>• Config: php.ini</text><text x='305' y='150' font-family='sans-serif' font-size='11' fill='#19283D'>• Extensions: mysqli, pdo</text><text x='305' y='175' font-family='sans-serif' font-size='11' fill='#617087'>• Memory: 256MB</text><rect x='540' y='70' width='220' height='130' rx='8' fill='#ffffff' stroke='#28A994' stroke-width='1.5'/><text x='650' y='95' font-family='sans-serif' font-size='12' font-weight='700' fill='#28A994' text-anchor='middle'>MySQL (Port 3306)</text><text x='555' y='125' font-family='sans-serif' font-size='11' fill='#19283D'>• Config: my.ini</text><text x='555' y='150' font-family='sans-serif' font-size='11' fill='#19283D'>• Default User: root</text><text x='555' y='175' font-family='sans-serif' font-size='11' fill='#617087'>• Admin: phpMyAdmin</text></svg>"
                    },
                    'examples': {
                        'scenario': 'Local Environment Diagnostic Script',
                        'code': '<?php\\necho \'<h2>System Environment Verification</h2>\';\\necho \'PHP Version: \' . phpversion() . \'<br>\';\\n$db = @new mysqli(\'localhost\', \'root\', \'\');\\nif ($db->connect_error) { echo \'MySQL Offline\'; } else { echo \'MySQL Connected on Port 3306\'; }\\n?>'
                    },
                    'important_points': [
                        'XAMPP consolidates Apache, MySQL, PHP, and Perl into one local directory tree.',
                        'Web project folders must be placed under C:\\xampp\\htdocs to be reachable via localhost.',
                        'Port 80 conflicts are solved by editing Listen 80 to Listen 8080 in httpd.conf.',
                        'Modifying php.ini requires restarting the Apache daemon to take effect.',
                        'The phpinfo() function displays active configuration settings and loaded modules.'
                    ],
                    'revision': {
                        'summary': 'XAMPP provides an isolated local stack for web development. Proper configuration of ports and config files (httpd.conf, php.ini, my.ini) ensures an efficient local workflow.',
                        'terminology': 'htdocs, php.ini, httpd.conf, loopback, port 80, port 3306, phpMyAdmin.',
                        'mechanisms': 'Browser -> localhost -> Apache Port 80 -> PHP runtime -> MySQL Port 3306.',
                        'common_mistakes': 'Forgetting to restart Apache after making adjustments to php.ini.'
                    }
                }
            ]
        }
    ]
    return modules

print('Template created.')
