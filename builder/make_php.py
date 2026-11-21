import json, os

os.makedirs("builder/data", exist_ok=True)

def T(t_id, title, subtopics, definition, background, importance, objectives,
      concepts, terminology, principles, structures,
      sequence, comparison_headers, comparison_rows, code_arch,
      svg_content, caption, scenario, sample_code,
      important_points, summary, terms_str, mechanisms, common_mistakes):
    return {
        "id": t_id,
        "title": title,
        "subtopics": subtopics,
        "intro": {"definition": definition, "background": background, "importance": importance, "objectives": objectives},
        "fundamentals": {"concepts": concepts, "terminology": [{"term": t[0], "definition": t[1]} for t in terminology], "principles": principles, "structures": structures},
        "detailed_explanation": {"sequence": sequence, "comparison_table": {"headers": comparison_headers, "rows": comparison_rows}, "code_architecture": code_arch},
        "diagram": {"caption": caption, "svg": svg_content},
        "examples": {"scenario": scenario, "code": sample_code},
        "important_points": important_points,
        "revision": {"summary": summary, "terminology": terms_str, "mechanisms": mechanisms, "common_mistakes": common_mistakes}
    }

modules = []

# M1
modules.append({
    "module_no": 1,
    "title": "Introduction to Web Development & Setting up Environment",
    "hours": 4,
    "marks": 5,
    "topics": [
        T(
            "php_m1_t1",
            "Web Development Architecture: Client vs Server-Side & HTTP Request Lifecycle",
            ["Client vs Server Architecture", "HTML Basics & DOM", "Role of PHP and MySQL", "HTTP Request-Response Lifecycle"],
            "Web development encompasses client-side presentation in the browser and server-side computing where scripts synthesize dynamic markup, query databases, and handle security.",
            "Static web pages were replaced in the 1990s by server-side scripting. Rasmus Lerdorf developed PHP in 1994, which combined with MySQL and Apache into the LAMP stack.",
            "Separating client rendering from server logic guarantees security, transactional atomicity, and scalable architecture.",
            ["Differentiate client-side from server-side execution.", "Trace HTTP request lifecycle from DNS to rendering.", "Understand PHP execution on Apache.", "Explain dynamic HTML synthesis."],
            "Client code runs in the browser sandbox. Server code executes with full OS and database access on the backend server.",
            [
                ("Client-Side", "Code executed in browser without direct database access."),
                ("Server-Side", "Code compiled on web server prior to output delivery."),
                ("HTTP", "Stateless request-response protocol between client and server."),
                ("LAMP", "Linux, Apache, MySQL, and PHP software stack.")
            ],
            "1. Statelessness: HTTP does not store conversational state.\n2. Zero-Trust Client: Validate all inputs server-side.",
            "Client Browser <== HTTP ==> Apache Server <== FastCGI ==> PHP Zend Engine <== SQL ==> MySQL Server",
            [
                "1. User enters URL or clicks submit.",
                "2. Browser resolves DNS and establishes TCP handshake.",
                "3. Browser transmits HTTP request header and body.",
                "4. Apache routes .php requests to the Zend Engine.",
                "5. Zend Engine executes bytecode and queries MySQL if needed.",
                "6. Database returns relational recordsets.",
                "7. PHP blends dynamic data into HTML markup.",
                "8. Apache sends HTTP 200 response with HTML payload to browser."
            ],
            ["Dimension", "Client-Side", "Server-Side (PHP)"],
            [
                ["Environment", "Web Browser (Chrome, Firefox)", "Server (Apache, PHP-FPM)"],
                ["Visibility", "Exposed via DevTools", "Private and hidden on server"],
                ["DB Access", "Blocked for security", "Direct authorized access"],
                ["Languages", "HTML, CSS, JavaScript", "PHP, MySQL, Apache"]
            ],
            "<?php\n$db = new mysqli('localhost', 'root', '', 'makaut');\n$res = $db->query('SELECT * FROM students WHERE id = 1');\n$student = $res->fetch_assoc();\n?>\n<h1><?= htmlspecialchars($student['name']) ?></h1>",
            "<svg viewBox='0 0 800 220' xmlns='http://www.w3.org/2000/svg' style='width:100%;height:auto;background:#fff;border-radius:8px;border:1px solid #E5E9F1;'><rect x='30' y='30' width='180' height='160' rx='8' fill='#F7F8FC' stroke='#377FE6'/><text x='120' y='60' font-family='sans-serif' font-size='12' font-weight='700' fill='#377FE6' text-anchor='middle'>CLIENT (Browser)</text><text x='120' y='95' font-family='sans-serif' font-size='11' fill='#19283D' text-anchor='middle'>HTML5 / CSS3 / JS</text><text x='120' y='145' font-family='sans-serif' font-size='10' fill='#617087' text-anchor='middle'>User Agent</text><path d='M 215 110 L 295 110' stroke='#377FE6' stroke-width='2'/><text x='255' y='100' font-family='sans-serif' font-size='9' font-weight='700' fill='#377FE6' text-anchor='middle'>1. HTTP Req</text><rect x='300' y='30' width='200' height='160' rx='8' fill='#F7F8FC' stroke='#786CE5'/><text x='400' y='60' font-family='sans-serif' font-size='12' font-weight='700' fill='#786CE5' text-anchor='middle'>APACHE + PHP 8</text><text x='400' y='95' font-family='sans-serif' font-size='11' fill='#19283D' text-anchor='middle'>Zend Opcode Engine</text><text x='400' y='145' font-family='sans-serif' font-size='10' fill='#617087' text-anchor='middle'>FastCGI Process</text><path d='M 505 110 L 585 110' stroke='#28A994' stroke-width='2'/><text x='545' y='100' font-family='sans-serif' font-size='9' font-weight='700' fill='#28A994' text-anchor='middle'>2. SQL</text><rect x='590' y='30' width='180' height='160' rx='8' fill='#F7F8FC' stroke='#28A994'/><text x='680' y='60' font-family='sans-serif' font-size='12' font-weight='700' fill='#28A994' text-anchor='middle'>MYSQL DB</text><text x='680' y='95' font-family='sans-serif' font-size='11' fill='#19283D' text-anchor='middle'>Port 3306</text><text x='680' y='145' font-family='sans-serif' font-size='10' fill='#617087' text-anchor='middle'>InnoDB Tables</text></svg>",
            "Figure 1.1: Web Request-Response Architecture",
            "Student Portal Live Lookup",
            "<?php\n$roll = $_GET['roll'] ?? 'N/A';\necho 'Result for Roll: ' . htmlspecialchars($roll);\n?>",
            [
                "Browser executes client-side presentation code.",
                "PHP executes exclusively on the server before transmitting output.",
                "HTTP is a stateless protocol.",
                "Zend Engine compiles PHP into opcodes.",
                "Client-side validation must always be backed by server validation."
            ],
            "Three-tier architecture separates browser presentation, server application logic, and database persistence.",
            "Client, Server, Zend Engine, HTTP, FastCGI, LAMP.",
            "Browser Req -> Apache -> PHP Compile -> MySQL -> Render -> HTTP 200.",
            "Relying on browser JavaScript validation for data security."
        ),
        T(
            "php_m1_t2",
            "Development Environment Setup: Installation of XAMPP/WAMP, Apache, MySQL & PHP Configuration",
            ["XAMPP vs WAMP", "Apache Configuration (httpd.conf)", "php.ini Directives", "MySQL Configuration (my.ini)"],
            "A local development environment bundles Apache, MySQL, and PHP into an offline software package on a developer's desktop.",
            "Bundled distributions like XAMPP provide a single control panel to start and stop services without manual binary compilation.",
            "Knowledge of port binding, document roots, and runtime php.ini directives is essential for troubleshooting setup issues.",
            ["Install and start Apache and MySQL.", "Resolve port 80 and 3306 conflicts.", "Adjust upload limits in php.ini.", "Set up web root in htdocs."],
            "Apache listens on port 80, MySQL on port 3306. Browser requests to localhost point to loopback IP 127.0.0.1.",
            [
                ("htdocs", "Public directory serving PHP and web assets in XAMPP."),
                ("php.ini", "Configuration file controlling PHP runtime execution limits."),
                ("httpd.conf", "Apache server configuration file governing ports and directories.")
            ],
            "1. Unique Ports: Each network daemon requires an exclusive port.\n2. Restart After Edit: php.ini changes require an Apache restart.",
            "C:\\xampp\\htdocs (Web Root) | C:\\xampp\\php\\php.ini | C:\\xampp\\apache\\conf\\httpd.conf",
            [
                "1. Download and run XAMPP installer.",
                "2. Start Apache and MySQL in XAMPP Control Panel.",
                "3. If port 80 is blocked by IIS, change port to 8080 in httpd.conf.",
                "4. Open http://localhost to verify Apache status.",
                "5. Open http://localhost/phpmyadmin to manage MySQL.",
                "6. Set upload_max_filesize = 32M in php.ini and restart Apache."
            ],
            ["Directive", "Dev Value", "Prod Value"],
            [
                ["display_errors", "On", "Off"],
                ["error_reporting", "E_ALL", "E_ALL & ~E_DEPRECATED"],
                ["upload_max_filesize", "32M", "10M"],
                ["post_max_size", "64M", "20M"]
            ],
            "# php.ini settings\ndisplay_errors = On\nerror_reporting = E_ALL\nmemory_limit = 256M\nupload_max_filesize = 32M",
            "<svg viewBox='0 0 800 200' xmlns='http://www.w3.org/2000/svg' style='width:100%;height:auto;background:#fff;border-radius:8px;border:1px solid #E5E9F1;'><rect x='30' y='30' width='220' height='140' rx='8' fill='#F7F8FC' stroke='#786CE5'/><text x='140' y='60' font-family='sans-serif' font-size='12' font-weight='700' fill='#786CE5' text-anchor='middle'>Apache (Port 80/8080)</text><text x='50' y='90' font-family='sans-serif' font-size='10' fill='#19283D'>• httpd.conf</text><text x='50' y='110' font-family='sans-serif' font-size='10' fill='#19283D'>• Root: /htdocs</text><rect x='290' y='30' width='220' height='140' rx='8' fill='#F7F8FC' stroke='#377FE6'/><text x='400' y='60' font-family='sans-serif' font-size='12' font-weight='700' fill='#377FE6' text-anchor='middle'>PHP 8.x Engine</text><text x='310' y='90' font-family='sans-serif' font-size='10' fill='#19283D'>• php.ini</text><text x='310' y='110' font-family='sans-serif' font-size='10' fill='#19283D'>• Extensions: mysqli, pdo</text><rect x='550' y='30' width='220' height='140' rx='8' fill='#F7F8FC' stroke='#28A994'/><text x='660' y='60' font-family='sans-serif' font-size='12' font-weight='700' fill='#28A994' text-anchor='middle'>MySQL (Port 3306)</text><text x='570' y='90' font-family='sans-serif' font-size='10' fill='#19283D'>• my.ini</text><text x='570' y='110' font-family='sans-serif' font-size='10' fill='#19283D'>• GUI: phpMyAdmin</text></svg>",
            "Figure 1.2: Local XAMPP Environment Architecture",
            "Checking Environment Configuration",
            "<?php\necho 'PHP: ' . phpversion();\n$m = @new mysqli('localhost', 'root', '');\necho $m->connect_error ? ' DB Error' : ' DB Connected';\n?>",
            [
                "XAMPP bundles Apache, MySQL, and PHP into one folder.",
                "Projects must be located in htdocs to be accessible via browser.",
                "Port 80 collisions can be resolved by changing port in httpd.conf.",
                "Editing php.ini requires restarting Apache.",
                "phpinfo() outputs comprehensive runtime information."
            ],
            "Local web servers simulate production environments. Configuration files manage memory, ports, and errors.",
            "htdocs, php.ini, httpd.conf, port 80, port 3306.",
            "Browser localhost -> Apache port 80 -> PHP parser -> MySQL 3306.",
            "Forgetting to restart Apache after editing php.ini."
        )
    ]
})

print("Generated Module 1")
