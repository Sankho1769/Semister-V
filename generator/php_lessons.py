# Complete 8 Modules for PHP with MySQL
from generator.helper import create_topic

def get_php_modules():
    modules = []

    # Module 1
    m1_topics = [
        create_topic(
            "php_m1_t1",
            "Introduction to Web Development: Client vs Server Architecture & HTTP Protocol",
            ["Web Development Overview", "Client-Side vs Server-Side Execution", "HTML Basics & DOM Integration", "Role of PHP and MySQL in Dynamic Web Systems"],
            "Web development is the systematic engineering of web applications operating across HTTP/HTTPS networks, partitioned into client-side presentation in web browsers and server-side logic executed on application host servers.",
            "Static web pages were introduced in Web 1.0. With the development of CGI in 1993 and Rasmus Lerdorf creating PHP in 1994, dynamic server execution became the global standard.",
            "Separating presentation from business logic guarantees data integrity, protects server credentials, and provides horizontal scalability for high-traffic platforms.",
            [
                "Differentiate browser rendering from server script execution.",
                "Trace the complete HTTP request-response transaction.",
                "Analyze PHP and MySQL roles in dynamic content synthesis.",
                "Explain DOM construction from compiled HTML payloads."
            ],
            "Client computing executes within the browser sandbox (HTML5, CSS3, JavaScript). Server computing operates with full OS and database access, producing dynamic HTML or JSON streams.",
            [
                ("Client-Side", "Presentation layer executing in web browsers without direct database access."),
                ("Server-Side", "Backend business layer running on servers, managing databases and authenticating users."),
                ("HTTP Lifecycle", "Stateless request-response protocol linking client browsers to web daemons."),
                ("LAMP Stack", "Software bundle comprising Linux, Apache, MySQL, and PHP.")
            ],
            "1. Stateless Protocol: HTTP retains no session memory between discrete requests without cookies or tokens.\n2. Zero Client Trust: All inputs must be strictly validated server-side.",
            "User Browser <== HTTP ==> Apache Server <== FastCGI ==> PHP 8 Zend Engine <== TCP 3306 ==> MySQL Server",
            [
                "1. User enters a URL or triggers an action button.",
                "2. Browser resolves DNS to server IP and performs TCP handshake.",
                "3. Browser transmits HTTP request header and payload.",
                "4. Apache identifies requested file; delegates .php to Zend Engine.",
                "5. Zend Engine parses bytecode, queries MySQL database via port 3306.",
                "6. MySQL returns relational recordsets to PHP.",
                "7. PHP blends dynamic data into HTML markup.",
                "8. Apache wraps HTML into HTTP 200 OK response and transmits to browser."
            ],
            ["Architectural Aspect", "Client-Side", "Server-Side (PHP)"],
            [
                ["Environment", "Web Browser (Chrome, Firefox, Safari)", "Server Daemon (Apache, Nginx, PHP-FPM)"],
                ["Source Code", "Publicly visible via View Source", "Private and concealed on host server"],
                ["Database Access", "Prohibited for security", "Direct authorized access via TCP socket"],
                ["Technologies", "HTML5, CSS3, JavaScript", "PHP, MySQL, Apache, Linux"]
            ],
            "<?php\n$db = new mysqli('localhost', 'root', '', 'university');\n$res = $db->query('SELECT name, course FROM students WHERE id = 1');\n$row = $res->fetch_assoc();\n?>\n<h1>Student: <?= htmlspecialchars($row['name']) ?></h1>\n<p>Course: <?= htmlspecialchars($row['course']) ?></p>",
            "<svg viewBox='0 0 800 220' xmlns='http://www.w3.org/2000/svg' style='width:100%;height:auto;background:#fff;border-radius:8px;border:1px solid #E5E9F1;'><rect x='30' y='30' width='180' height='160' rx='8' fill='#F7F8FC' stroke='#377FE6'/><text x='120' y='60' font-family='sans-serif' font-size='12' font-weight='700' fill='#377FE6' text-anchor='middle'>CLIENT (Browser)</text><text x='120' y='95' font-family='sans-serif' font-size='11' fill='#19283D' text-anchor='middle'>HTML5 / CSS3 / JS</text><text x='120' y='145' font-family='sans-serif' font-size='10' fill='#617087' text-anchor='middle'>DOM Tree Engine</text><path d='M 215 110 L 295 110' stroke='#377FE6' stroke-width='2'/><text x='255' y='100' font-family='sans-serif' font-size='9' font-weight='700' fill='#377FE6' text-anchor='middle'>1. HTTP Req</text><rect x='300' y='30' width='200' height='160' rx='8' fill='#F7F8FC' stroke='#786CE5'/><text x='400' y='60' font-family='sans-serif' font-size='12' font-weight='700' fill='#786CE5' text-anchor='middle'>APACHE + PHP 8</text><text x='400' y='95' font-family='sans-serif' font-size='11' fill='#19283D' text-anchor='middle'>Zend Opcode Engine</text><text x='400' y='145' font-family='sans-serif' font-size='10' fill='#617087' text-anchor='middle'>FastCGI Process</text><path d='M 505 110 L 585 110' stroke='#28A994' stroke-width='2'/><text x='545' y='100' font-family='sans-serif' font-size='9' font-weight='700' fill='#28A994' text-anchor='middle'>2. SQL</text><rect x='590' y='30' width='180' height='160' rx='8' fill='#F7F8FC' stroke='#28A994'/><text x='680' y='60' font-family='sans-serif' font-size='12' font-weight='700' fill='#28A994' text-anchor='middle'>MYSQL DATABASE</text><text x='680' y='95' font-family='sans-serif' font-size='11' fill='#19283D' text-anchor='middle'>Port 3306</text><text x='680' y='145' font-family='sans-serif' font-size='10' fill='#617087' text-anchor='middle'>InnoDB Tables</text></svg>",
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
        create_topic(
            "php_m1_t2",
            "Setting up Environment: Installation of XAMPP/WAMP, Apache, MySQL & PHP Configuration",
            ["XAMPP vs WAMP Architecture", "Apache httpd.conf Configuration", "PHP Engine php.ini Tuning", "MySQL Daemon Setup & Port Bindings"],
            "A local web development environment provides an isolated software stack simulating a production web server on a developer's desktop machine.",
            "Integrated packages like XAMPP package Apache, MariaDB/MySQL, and PHP into a unified executable tree with graphical administration.",
            "Mastery of port bindings, virtual hosts, and runtime directives in php.ini is required for enterprise and academic web engineering.",
            [
                "Install and start Apache and MySQL daemons via XAMPP.",
                "Resolve port 80 collisions caused by IIS or Skype.",
                "Configure upload_max_filesize and display_errors in php.ini.",
                "Deploy PHP projects to the public htdocs web root."
            ],
            "Apache listens on port 80/443 and MySQL on port 3306. Requests to http://localhost resolve to 127.0.0.1 and map to htdocs.",
            [
                ("htdocs", "Public web root directory in XAMPP serving executable scripts."),
                ("php.ini", "Central configuration file for PHP runtime memory and extensions."),
                ("httpd.conf", "Apache web server configuration governing listening ports and directories."),
                ("Loopback (127.0.0.1)", "Standard network interface pointing to the local host machine.")
            ],
            "1. Exclusive Ports: Each network service requires an exclusive port binding.\n2. Restart After Edit: Apache must be restarted after modifying php.ini.",
            "C:\\xampp\\htdocs (Web Root) | C:\\xampp\\php\\php.ini | C:\\xampp\\apache\\conf\\httpd.conf",
            [
                "1. Download and install XAMPP with administrative rights.",
                "2. Launch XAMPP Control Panel and start Apache and MySQL.",
                "3. If port 80 is occupied, update Listen 80 to 8080 in httpd.conf.",
                "4. Access http://localhost to confirm Apache is active.",
                "5. Open http://localhost/phpmyadmin to manage MySQL databases.",
                "6. Adjust upload_max_filesize = 32M and memory_limit = 256M in php.ini.",
                "7. Restart Apache service to reload updated configuration."
            ],
            ["Directive", "Development Value", "Production Value", "Significance"],
            [
                ["display_errors", "On", "Off", "Hides internal file paths from unauthorized viewers"],
                ["error_reporting", "E_ALL", "E_ALL & ~E_DEPRECATED", "Enforces strict coding standards locally"],
                ["upload_max_filesize", "32M", "10M", "Maximum size of individual uploaded files"],
                ["post_max_size", "64M", "20M", "Maximum size of complete HTTP POST request body"]
            ],
            "# php.ini settings\ndisplay_errors = On\nerror_reporting = E_ALL\nmemory_limit = 256M\npost_max_size = 64M\nupload_max_filesize = 32M\ndate.timezone = 'Asia/Kolkata'",
            "<svg viewBox='0 0 800 200' xmlns='http://www.w3.org/2000/svg' style='width:100%;height:auto;background:#fff;border-radius:8px;border:1px solid #E5E9F1;'><rect x='30' y='30' width='220' height='140' rx='8' fill='#F7F8FC' stroke='#786CE5'/><text x='140' y='60' font-family='sans-serif' font-size='12' font-weight='700' fill='#786CE5' text-anchor='middle'>Apache (Port 80/8080)</text><text x='50' y='90' font-family='sans-serif' font-size='10' fill='#19283D'>• httpd.conf</text><text x='50' y='110' font-family='sans-serif' font-size='10' fill='#19283D'>• Root: /htdocs</text><rect x='290' y='30' width='220' height='140' rx='8' fill='#F7F8FC' stroke='#377FE6'/><text x='400' y='60' font-family='sans-serif' font-size='12' font-weight='700' fill='#377FE6' text-anchor='middle'>PHP 8.x Engine</text><text x='310' y='90' font-family='sans-serif' font-size='10' fill='#19283D'>• php.ini</text><text x='310' y='110' font-family='sans-serif' font-size='10' fill='#19283D'>• Extensions: mysqli, pdo</text><rect x='550' y='30' width='220' height='140' rx='8' fill='#F7F8FC' stroke='#28A994'/><text x='660' y='60' font-family='sans-serif' font-size='12' font-weight='700' fill='#28A994' text-anchor='middle'>MySQL (Port 3306)</text><text x='570' y='90' font-family='sans-serif' font-size='10' fill='#19283D'>• my.ini</text><text x='570' y='110' font-family='sans-serif' font-size='10' fill='#19283D'>• GUI: phpMyAdmin</text></svg>",
            "Figure 1.2: Local XAMPP Environment Architecture",
            "Checking Environment Configuration",
            "<?php\necho 'PHP: ' . phpversion();\n$m = @new mysqli('localhost', 'root', '');\necho $m->connect_error ? ' DB Offline' : ' DB Connected on Port 3306';\n?>",
            [
                "XAMPP bundles Apache, MySQL, and PHP into one folder.",
                "Projects must be located in htdocs to be accessible via browser.",
                "Port 80 conflicts can be resolved by changing port in httpd.conf.",
                "Editing php.ini requires restarting Apache.",
                "phpinfo() outputs comprehensive runtime information."
            ],
            "Local web servers simulate production environments. Configuration files manage memory, ports, and errors.",
            "htdocs, php.ini, httpd.conf, port 80, port 3306, phpMyAdmin.",
            "Browser localhost -> Apache port 80 -> PHP parser -> MySQL 3306.",
            "Forgetting to restart Apache after editing php.ini."
        )
    ]
    modules.append({"module_no": 1, "title": "Introduction to Web Development & Setting up Environment", "hours": 4, "marks": 5, "topics": m1_topics})

    # Module 2
    m2_topics = [
        create_topic(
            "php_m2_t1",
            "PHP Basics: Syntax, Variables, Data Types, Operators and Control Structures",
            ["Variable Sigil ($)", "Data Types", "Type Juggling vs Strict Types", "Selection & Loops"],
            "PHP is a server-side language supporting procedural, object-oriented, and functional styles. Variables start with $ and are dynamically evaluated.",
            "Modern PHP 7 & 8 introduced scalar type declarations, strict type enforcement, union types, and the match expression.",
            "Mastery of control flow, data types, and equality operators prevents logic errors and security flaws.",
            ["Understand loose (==) vs strict (===) equality.", "Manipulate scalar and compound data types.", "Use if-else, switch, and match constructs.", "Iterate collections with foreach loops."],
            "Variables do not require explicit type declaration before assignment. Type juggling automatically coerces types during operations unless strict types are enabled.",
            [
                ("Type Juggling", "Automatic data type conversion by the runtime engine."),
                ("Strict Equality (===)", "Compares both value and datatype without coercion."),
                ("Match Expression", "PHP 8 expression returning values with strict comparison.")
            ],
            "1. Favor Strict Equality: Always use === to prevent type coercion vulnerabilities.\n2. Defend Boundaries: Ensure loop conditions terminate predictably.",
            "$var = value; | if (cond) {...} else {...} | $val = match($x) { 1 => 'A', default => 'B' };",
            [
                "1. Parser encounters variable prefixed with $.",
                "2. Type is dynamically allocated based on literal value.",
                "3. Expressions evaluate with type coercion if operators differ.",
                "4. Control structures branch based on boolean truthiness.",
                "5. Foreach iterates through array key-value elements."
            ],
            ["Construct", "Loose (==)", "Strict (===)"],
            [
                ["0 == '0'", "True", "False"],
                ["0 == ''", "True", "False"],
                ["0 == false", "True", "False"],
                ["100 === '100'", "False", "False"]
            ],
            "<?php\ndeclare(strict_types=1);\n$score = 82;\n$grade = match(true) {\n    $score >= 90 => 'O',\n    $score >= 80 => 'E',\n    default => 'Pass'\n};\n?>",
            "<svg viewBox='0 0 800 200' xmlns='http://www.w3.org/2000/svg' style='width:100%;height:auto;background:#fff;border-radius:8px;border:1px solid #E5E9F1;'><rect x='30' y='30' width='220' height='140' rx='8' fill='#F7F8FC' stroke='#377FE6'/><text x='140' y='60' font-family='sans-serif' font-size='12' font-weight='700' fill='#377FE6' text-anchor='middle'>Data Types</text><text x='50' y='90' font-family='sans-serif' font-size='10' fill='#19283D'>• int, float, string, bool</text><text x='50' y='110' font-family='sans-serif' font-size='10' fill='#19283D'>• array, object, null</text><rect x='290' y='30' width='220' height='140' rx='8' fill='#F7F8FC' stroke='#786CE5'/><text x='400' y='60' font-family='sans-serif' font-size='12' font-weight='700' fill='#786CE5' text-anchor='middle'>Control Flow</text><text x='310' y='90' font-family='sans-serif' font-size='10' fill='#19283D'>• if / elseif / else</text><text x='310' y='110' font-family='sans-serif' font-size='10' fill='#19283D'>• switch &amp; PHP 8 match</text><rect x='550' y='30' width='220' height='140' rx='8' fill='#F7F8FC' stroke='#28A994'/><text x='660' y='60' font-family='sans-serif' font-size='12' font-weight='700' fill='#28A994' text-anchor='middle'>Loop Iteration</text><text x='570' y='90' font-family='sans-serif' font-size='10' fill='#19283D'>• while &amp; do-while</text><text x='570' y='110' font-family='sans-serif' font-size='10' fill='#19283D'>• for &amp; foreach ($a as $k=&gt;$v)</text></svg>",
            "Figure 2.1: PHP Type System & Flow Control",
            "Grading and Attendance Evaluation",
            "<?php\n$att = 80;\necho ($att >= 75) ? 'Eligible for Exam' : 'Disbarred';\n?>",
            [
                "PHP variables are prefixed with $ and dynamically typed.",
                "Strict typing can be enforced using declare(strict_types=1).",
                "The match expression replaces switch with strict checking.",
                "Foreach is the standard tool for iterating associative arrays.",
                "Null coalescing (??) provides clean default fallback values."
            ],
            "PHP variables and types are versatile. Strict typing ensures predictable application state.",
            "Type Juggling, Strict Types, Match Expression, Foreach.",
            "Lexer -> Type Coercion -> Branching Logic -> Execution.",
            "Using loose == instead of strict === leading to logic bypasses."
        ),
        create_topic(
            "php_m2_t2",
            "Functions in PHP: Defining and Using Functions, Scope, Including Files & Built-in Functions",
            ["User Functions & Return Types", "Variable Scope (Local, Global, Static)", "include vs require", "Built-in Functions"],
            "Functions package reusable code blocks. PHP supports typed arguments, return types, pass-by-reference, and variadic parameters.",
            "Modular functions allow breaking large applications into testable subroutines across organized files.",
            "Understanding file inclusion prevents fatal errors and duplicated function declarations.",
            ["Declare functions with return type hints.", "Manage local and global scope.", "Compare include, require, include_once, and require_once.", "Use built-in utility functions."],
            "Function variables have local scope. File inclusion imports external script statements directly into the calling script.",
            [
                ("require_once", "Includes file once; triggers fatal E_COMPILE_ERROR if missing."),
                ("include_once", "Includes file once; triggers non-fatal E_WARNING if missing."),
                ("Static Variable", "Local variable retaining its value across function calls.")
            ],
            "1. Critical Files: Always use require_once for database config.\n2. DRY Code: Encapsulate shared routines into functions.",
            "function add(int $a, int $b): int { return $a + $b; } | require_once 'config.php';",
            [
                "1. Script invokes require_once 'db.php'.",
                "2. Engine verifies file has not been loaded previously.",
                "3. Engine loads and compiles external file.",
                "4. Function is invoked with parameter arguments.",
                "5. Local stack frame created, value computed, and returned."
            ],
            ["Statement", "Missing File Error", "Halts Execution?"],
            [
                ["include", "E_WARNING", "No"],
                ["include_once", "E_WARNING", "No"],
                ["require", "E_COMPILE_ERROR", "Yes"],
                ["require_once", "E_COMPILE_ERROR", "Yes"]
            ],
            "<?php\nfunction formatCurrency(float $val): string {\n    return '₹' . number_format($val, 2);\n}\necho formatCurrency(1499.5);\n?>",
            "<svg viewBox='0 0 800 180' xmlns='http://www.w3.org/2000/svg' style='width:100%;height:auto;background:#fff;border-radius:8px;border:1px solid #E5E9F1;'><rect x='40' y='30' width='330' height='120' rx='8' fill='#F7F8FC' stroke='#D65F64'/><text x='205' y='60' font-family='sans-serif' font-size='12' font-weight='700' fill='#D65F64' text-anchor='middle'>require / require_once</text><text x='60' y='90' font-family='sans-serif' font-size='11' fill='#19283D'>• Fatal E_COMPILE_ERROR</text><text x='60' y='110' font-family='sans-serif' font-size='11' fill='#19283D'>• Halts script execution</text><rect x='430' y='30' width='330' height='120' rx='8' fill='#F7F8FC' stroke='#F2C75C'/><text x='595' y='60' font-family='sans-serif' font-size='12' font-weight='700' fill='#B38600' text-anchor='middle'>include / include_once</text><text x='450' y='90' font-family='sans-serif' font-size='11' fill='#19283D'>• Warning E_WARNING</text><text x='450' y='110' font-family='sans-serif' font-size='11' fill='#19283D'>• Continues execution</text></svg>",
            "Figure 2.2: Comparison of File Inclusion Statements",
            "Hit Counter Using Static Variable",
            "<?php\nfunction hit() {\n    static $c = 0;\n    return ++$c;\n}\necho hit() . ' ' . hit(); // 1 2\n?>",
            [
                "`require_once` prevents duplicate declaration fatal crashes.",
                "Functions can have strict parameter and return type declarations.",
                "Static variables maintain their state across multiple calls.",
                "Prefixing parameter with & passes it by reference.",
                "Core math and string functions are globally accessible."
            ],
            "Modular programming in PHP uses functions and strict file inclusion statements.",
            "require_once, include_once, static variable, pass-by-reference.",
            "Path resolution -> Cache check -> Compilation -> Function execution.",
            "Using include for database credentials, causing script to crash silently."
        ),
        create_topic(
            "php_m2_t3",
            "Arrays and Strings: Working with Arrays, Array Functions, String Manipulation & String Functions",
            ["Indexed, Associative & Multidimensional", "Array Functions", "String Processing", "Regex Basics"],
            "Arrays in PHP are ordered hash maps. Strings are byte arrays supported by rich manipulation libraries.",
            "All database rows, forms, and sessions are modeled as associative arrays in PHP.",
            "Mastery of array transformations and string sanitization is crucial for backend engineering.",
            ["Create indexed and associative arrays.", "Filter and map arrays with callbacks.", "Tokenize strings with explode and implode.", "Search patterns using preg_match."],
            "Arrays map keys to values. Strings can be manipulated using offset indexing or helper functions.",
            [
                ("Associative Array", "Array with custom named string keys."),
                ("explode()", "Splits string by delimiter into array."),
                ("implode()", "Concatenates array elements with a delimiter into string.")
            ],
            "1. Key Uniqueness: Associative array keys must be distinct.\n2. Immutable Strings: Operations produce fresh string copies.",
            "$assoc = ['name' => 'Amit', 'sem' => 5]; | $arr = explode(',', $str); | $s = implode(';', $arr);",
            [
                "1. Array initialized with brackets `[]`.",
                "2. Elements added with auto-incremented integer or string keys.",
                "3. array_filter removes elements failing a test predicate.",
                "4. array_map transforms each element.",
                "5. implode formats array into displayable string."
            ],
            ["Function", "Operation", "Key Behavior"],
            [
                ["sort()", "Numeric sort", "Resets keys 0..N"],
                ["asort()", "Value sort", "Preserves associative keys"],
                ["ksort()", "Key sort", "Sorts by keys alphabetically"]
            ],
            "<?php\n$nums = [10, 25, 4, 90, 55];\n$high = array_filter($nums, fn($n) => $n >= 50);\necho implode(', ', $high); // 90, 55\n?>",
            "<svg viewBox='0 0 800 180' xmlns='http://www.w3.org/2000/svg' style='width:100%;height:auto;background:#fff;border-radius:8px;border:1px solid #E5E9F1;'><rect x='40' y='30' width='200' height='120' rx='8' fill='#F7F8FC' stroke='#377FE6'/><text x='140' y='60' font-family='sans-serif' font-size='12' font-weight='700' fill='#377FE6' text-anchor='middle'>Input Array</text><text x='140' y='95' font-family='monospace' font-size='10' fill='#19283D' text-anchor='middle'>[10, 25, 90, 55]</text><path d='M 245 90 L 305 90' stroke='#377FE6' stroke-width='2'/><rect x='310' y='30' width='200' height='120' rx='8' fill='#F7F8FC' stroke='#786CE5'/><text x='410' y='60' font-family='sans-serif' font-size='12' font-weight='700' fill='#786CE5' text-anchor='middle'>array_filter(>=50)</text><text x='410' y='95' font-family='monospace' font-size='10' fill='#19283D' text-anchor='middle'>[90, 55]</text><path d='M 515 90 L 575 90' stroke='#28A994' stroke-width='2'/><rect x='580' y='30' width='180' height='120' rx='8' fill='#F7F8FC' stroke='#28A994'/><text x='670' y='60' font-family='sans-serif' font-size='12' font-weight='700' fill='#28A994' text-anchor='middle'>implode(', ')</text><text x='670' y='95' font-family='monospace' font-size='11' font-weight='700' fill='#1B6F61' text-anchor='middle'>&quot;90, 55&quot;</text></svg>",
            "Figure 2.3: Array Filtering and Formatting Pipeline",
            "Parsing CSV Input",
            "<?php\n$csv = 'PHP,Java,Database,Management';\n$tags = explode(',', $csv);\nprint_r($tags);\n?>",
            [
                "PHP arrays function as ordered hash tables.",
                "explode() splits strings; implode() joins arrays.",
                "asort() preserves associative keys; sort() reindexes.",
                "array_map() transforms elements via callback.",
                "array_filter() extracts matching subsets."
            ],
            "Arrays and strings are core data carriers in PHP. Higher-order functions enable declarative transformations.",
            "explode, implode, asort, array_map, array_filter.",
            "Hash lookup -> Callback evaluation -> Array recombination.",
            "Using sort() on database rows and losing primary key indices."
        )
    ]
    modules.append({"module_no": 2, "title": "PHP Basics, Functions, Arrays and Strings", "hours": 8, "marks": 10, "topics": m2_topics})

    # Module 3
    m3_topics = [
        create_topic(
            "php_m3_t1",
            "Forms Handling and User Input: Handling Form Data & GET vs POST Methods",
            ["HTTP Form Methods", "$_GET vs $_POST Superglobals", "URL Encoding", "Post/Redirect/Get Pattern"],
            "Form handling processes user submissions sent across HTTP to backend PHP scripts for database persistence and verification.",
            "HTTP methods define how client data is transported. GET appends parameters to URLs; POST embeds data invisibly in request bodies.",
            "Proper method selection prevents sensitive data exposure in server logs and prevents accidental multiple submissions.",
            ["Differentiate GET and POST protocols.", "Inspect $_GET and $_POST superglobals.", "Select appropriate form enctype.", "Implement PRG pattern to prevent duplicates."],
            "GET is idempotent and visible. POST modifies server state and hides data from the URL bar.",
            [
                ("$_POST", "Superglobal holding key-value pairs submitted via HTTP POST."),
                ("$_GET", "Superglobal holding query parameters passed in the URL."),
                ("Idempotent", "An HTTP method that can be called repeatedly without changing state.")
            ],
            "1. Sensitive Data Rule: Never pass passwords or payment tokens via GET.\n2. Mutation Rule: Use POST for state-changing operations.",
            "<form action='save.php' method='POST'> <input name='title'> </form> | $t = $_POST['title'];",
            [
                "1. User fills HTML form and clicks submit.",
                "2. Browser serializes form fields into name=value pairs.",
                "3. For POST: pairs sent inside HTTP request message body.",
                "4. Apache populates $_POST superglobal array.",
                "5. PHP script validates data and executes database queries.",
                "6. Server sends 302 redirect to success page (PRG pattern)."
            ],
            ["Metric", "GET Method", "POST Method"],
            [
                ["Data Location", "Appended to URL query string", "Inside HTTP request body"],
                ["Visibility", "Visible in address bar & history", "Hidden from URL & logs"],
                ["Max Payload", "Limited (~2048 chars)", "Governed by post_max_size (64M)"],
                ["Caching", "Can be cached & bookmarked", "Never cached by default"]
            ],
            "<?php\nif ($_SERVER['REQUEST_METHOD'] === 'POST') {\n    $user = trim($_POST['user'] ?? '');\n    header('Location: thanks.php?u=' . urlencode($user));\n    exit;\n}\n?>",
            "<svg viewBox='0 0 800 180' xmlns='http://www.w3.org/2000/svg' style='width:100%;height:auto;background:#fff;border-radius:8px;border:1px solid #E5E9F1;'><rect x='40' y='30' width='330' height='120' rx='8' fill='#F7F8FC' stroke='#377FE6'/><text x='205' y='60' font-family='sans-serif' font-size='12' font-weight='700' fill='#377FE6' text-anchor='middle'>HTTP GET (Safe / Query)</text><text x='60' y='90' font-family='monospace' font-size='10' fill='#19283D'>/search.php?q=php&amp;page=1</text><text x='60' y='110' font-family='sans-serif' font-size='10' fill='#617087'>• Visible in URL • Bookmarkable</text><rect x='430' y='30' width='330' height='120' rx='8' fill='#F7F8FC' stroke='#28A994'/><text x='595' y='60' font-family='sans-serif' font-size='12' font-weight='700' fill='#28A994' text-anchor='middle'>HTTP POST (Mutating / Secure)</text><text x='450' y='90' font-family='monospace' font-size='10' fill='#19283D'>Body: user=amit&amp;pass=secret</text><text x='450' y='110' font-family='sans-serif' font-size='10' fill='#617087'>• Hidden payload • State modification</text></svg>",
            "Figure 3.1: HTTP GET vs POST Mechanics",
            "Contact Form Processing",
            "<?php\n$email = $_POST['email'] ?? '';\necho 'Processing submission for: ' . htmlspecialchars($email);\n?>",
            [
                "GET parameters are visible in URLs and must not carry passwords.",
                "POST places payloads inside the request message body.",
                "Use multipart/form-data for uploading files.",
                "$_SERVER['REQUEST_METHOD'] identifies the HTTP verb.",
                "PRG pattern prevents accidental double submissions on refresh."
            ],
            "Form handling links user input to server actions. GET is for reading; POST is for modifying state.",
            "GET, POST, $_POST, $_GET, Idempotent, PRG.",
            "Form submit -> HTTP message -> Server parse -> PHP $_POST -> Database.",
            "Passing sensitive login credentials through HTTP GET query strings."
        ),
        create_topic(
            "php_m3_t2",
            "Forms Handling: Validating and Sanitizing User Input",
            ["Validation vs Sanitization", "filter_var() Library", "HTML Entity Encoding", "XSS Prevention"],
            "Input validation verifies data matches expected formats and rules. Sanitization strips dangerous characters to prevent injection attacks.",
            "Untrusted user input is the primary attack surface on the web. Unsanitized outputs trigger Cross-Site Scripting (XSS).",
            "Enforcing server validation and output escaping ensures application data integrity and protects user sessions.",
            ["Differentiate validation from sanitization.", "Apply filter_var() with email and integer flags.", "Neutralize XSS using htmlspecialchars().", "Design comprehensive validation pipelines."],
            "Validation accepts or rejects data. Sanitization strips illegal characters. Escaping converts special characters to safe HTML entities.",
            [
                ("filter_var()", "PHP core function filtering variables with predefined filters."),
                ("htmlspecialchars()", "Encodes characters (&amp;, &quot;, &#039;, &lt;, &gt;) into HTML entities."),
                ("XSS", "Vulnerability where attackers inject client scripts into pages viewed by others.")
            ],
            "1. Validate Input: Verify format strictly before saving.\n2. Escape Output: Convert HTML special characters before rendering.",
            "$email = filter_var($_POST['e'], FILTER_VALIDATE_EMAIL); | echo htmlspecialchars($str, ENT_QUOTES, 'UTF-8');",
            [
                "1. User submits untrusted payload via POST.",
                "2. trim() removes whitespace.",
                "3. filter_var() checks email or integer validity.",
                "4. Regex checks complex formatting rules.",
                "5. Invalid records return error notifications.",
                "6. htmlspecialchars() escapes variables rendered into HTML."
            ],
            ["Operation", "Function", "Action"],
            [
                ["Validate Email", "filter_var($e, FILTER_VALIDATE_EMAIL)", "Returns email or false"],
                ["Sanitize Text", "filter_var($s, FILTER_SANITIZE_SPECIAL_CHARS)", "Escapes HTML tags"],
                ["Output Escaping", "htmlspecialchars($s, ENT_QUOTES)", "Neutralizes XSS scripts"]
            ],
            "<?php\n$email = trim($_POST['email'] ?? '');\nif (!filter_var($email, FILTER_VALIDATE_EMAIL)) {\n    die('Invalid email format');\n}\necho 'Valid email: ' . htmlspecialchars($email, ENT_QUOTES, 'UTF-8');\n?>",
            "<svg viewBox='0 0 800 180' xmlns='http://www.w3.org/2000/svg' style='width:100%;height:auto;background:#fff;border-radius:8px;border:1px solid #E5E9F1;'><rect x='40' y='30' width='200' height='120' rx='8' fill='#F7F8FC' stroke='#D65F64'/><text x='140' y='60' font-family='sans-serif' font-size='12' font-weight='700' fill='#D65F64' text-anchor='middle'>Untrusted Input</text><text x='140' y='95' font-family='monospace' font-size='9' fill='#19283D' text-anchor='middle'>&lt;script&gt;alert(1)&lt;/script&gt;</text><path d='M 245 90 L 305 90' stroke='#377FE6' stroke-width='2'/><rect x='310' y='30' width='200' height='120' rx='8' fill='#F7F8FC' stroke='#377FE6'/><text x='410' y='60' font-family='sans-serif' font-size='12' font-weight='700' fill='#377FE6' text-anchor='middle'>filter_var()</text><text x='410' y='95' font-family='sans-serif' font-size='10' fill='#19283D' text-anchor='middle'>Format Verification</text><path d='M 515 90 L 575 90' stroke='#28A994' stroke-width='2'/><rect x='580' y='30' width='180' height='120' rx='8' fill='#F7F8FC' stroke='#28A994'/><text x='670' y='60' font-family='sans-serif' font-size='12' font-weight='700' fill='#28A994' text-anchor='middle'>htmlspecialchars()</text><text x='670' y='95' font-family='monospace' font-size='10' font-weight='700' fill='#1B6F61' text-anchor='middle'>&amp;lt;script&amp;gt; safe</text></svg>",
            "Figure 3.2: Input Filtering and Output Escaping Pipeline",
            "Safe Output Rendering",
            "<?php\n$comment = '<script>evil()</script>';\necho htmlspecialchars($comment, ENT_QUOTES, 'UTF-8');\n?>",
            [
                "Never trust client data; validate server-side.",
                "filter_var() validates email, URL, and integer types.",
                "htmlspecialchars() with ENT_QUOTES converts quotes to entities.",
                "XSS attacks steal session tokens via injected JavaScript.",
                "Always specify UTF-8 encoding in htmlspecialchars()."
            ],
            "Input validation verifies format; output escaping prevents XSS execution.",
            "Validation, Sanitization, filter_var, htmlspecialchars, ENT_QUOTES, XSS.",
            "Input -> Filter Validation -> Strip / Escape -> Safe HTML output.",
            "Echoing raw user parameters directly into HTML templates."
        )
    ]
    modules.append({"module_no": 3, "title": "Forms Handling and User Input", "hours": 4, "marks": 5, "topics": m3_topics})


    # Module 4
    m4_topics = [
        create_topic(
            "php_m4_t1",
            "PHP and MySQL Integration: Connecting PHP to MySQL (MySQLi vs PDO)",
            ["MySQLi vs PDO Architecture", "DSN Connection Strings", "PDO Error Modes (ERRMODE_EXCEPTION)", "Connection Resource Management"],
            "Database integration enables PHP scripts to persist, query, and manipulate relational data in MySQL via native drivers (MySQLi) or database abstraction layers (PDO).",
            "Legacy mysql_* functions were removed in PHP 7. Modern development standardizes on PDO for multi-database flexibility and MySQLi for specialized MySQL operations.",
            "Database connectivity establishes the core of dynamic data-driven systems, requiring resilient error management and secure connection credentials.",
            ["Compare MySQLi and PDO drivers.", "Configure PDO with DSN and error modes.", "Catch PDOException safely.", "Manage database socket lifecycles."],
            "PDO is an object-oriented database abstraction layer. MySQLi supports both procedural and object-oriented syntax exclusively for MySQL.",
            [
                ("PDO", "PHP Data Objects: uniform interface supporting 12 relational databases."),
                ("MySQLi", "MySQL Improved: specialized driver for MySQL and MariaDB."),
                ("DSN", "Data Source Name: connection string containing host, dbname, and charset.")
            ],
            "1. Abstract Database Calls: Use PDO for database vendor independence.\n2. Exception Handling: Set ERRMODE_EXCEPTION to throw catchable errors.",
            "$pdo = new PDO('mysql:host=localhost;dbname=portal;charset=utf8mb4', 'root', '', [PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION]);",
            [
                "1. Assemble DSN string with host, dbname, and utf8mb4 encoding.",
                "2. Create PDO instance inside try block.",
                "3. Set default fetch mode to PDO::FETCH_ASSOC.",
                "4. If connection fails, catch PDOException and log details.",
                "5. Execute database queries via prepared statements.",
                "6. Close connection by setting $pdo = null."
            ],
            ["Feature", "PDO", "MySQLi"],
            [
                ["Databases", "12 RDBMS engines supported", "MySQL / MariaDB only"],
                ["Named Parameters", "Supported (:id, :name)", "Not supported (uses ? only)"],
                ["API Style", "Strictly Object-Oriented", "Dual: OOP & Procedural"]
            ],
            "<?php\ntry {\n    $pdo = new PDO('mysql:host=localhost;dbname=makaut;charset=utf8mb4', 'root', '', [\n        PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,\n        PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC\n    ]);\n} catch (PDOException $e) {\n    error_log($e->getMessage());\n    die('Database connection failure.');\n}\n?>",
            "<svg viewBox='0 0 800 180' xmlns='http://www.w3.org/2000/svg' style='width:100%;height:auto;background:#fff;border-radius:8px;border:1px solid #E5E9F1;'><rect x='40' y='30' width='220' height='120' rx='8' fill='#F7F8FC' stroke='#786CE5'/><text x='150' y='60' font-family='sans-serif' font-size='12' font-weight='700' fill='#786CE5' text-anchor='middle'>Application Logic</text><text x='60' y='90' font-family='sans-serif' font-size='10' fill='#19283D'>• Controllers / Models</text><text x='60' y='110' font-family='sans-serif' font-size='10' fill='#19283D'>• Business Rules</text><path d='M 265 90 L 325 90' stroke='#377FE6' stroke-width='2'/><rect x='330' y='30' width='220' height='120' rx='8' fill='#F7F8FC' stroke='#377FE6'/><text x='440' y='60' font-family='sans-serif' font-size='12' font-weight='700' fill='#377FE6' text-anchor='middle'>PDO Abstraction</text><text x='350' y='90' font-family='sans-serif' font-size='10' fill='#19283D'>• ERRMODE_EXCEPTION</text><text x='350' y='110' font-family='sans-serif' font-size='10' fill='#19283D'>• Prepared Statements</text><path d='M 555 90 L 615 90' stroke='#28A994' stroke-width='2'/><rect x='620' y='30' width='140' height='120' rx='8' fill='#F7F8FC' stroke='#28A994'/><text x='690' y='60' font-family='sans-serif' font-size='12' font-weight='700' fill='#28A994' text-anchor='middle'>MySQL</text><text x='640' y='90' font-family='sans-serif' font-size='10' fill='#19283D'>• Port 3306</text><text x='640' y='110' font-family='sans-serif' font-size='10' fill='#19283D'>• InnoDB</text></svg>",
            "Figure 4.1: Database Abstraction Architecture via PDO",
            "Database Connectivity Test",
            "<?php\n$stmt = $pdo->query('SELECT NOW() as t');\necho 'Server Time: ' . $stmt->fetch()['t'];\n?>",
            [
                "Legacy mysql_* functions are removed; use PDO or MySQLi.",
                "PDO supports multiple database engines with unified syntax.",
                "Always enable ERRMODE_EXCEPTION on PDO instances.",
                "Use utf8mb4 encoding to support all Unicode characters.",
                "Catching PDOException prevents password exposure on errors."
            ],
            "Database connectivity links PHP to MySQL. PDO provides an object-oriented, exception-safe abstraction interface.",
            "PDO, MySQLi, DSN, ERRMODE_EXCEPTION, utf8mb4.",
            "DSN creation -> PDO instantiation -> Exception check -> Query execution.",
            "Displaying raw PDOException messages containing DB passwords to web visitors."
        ),
        create_topic(
            "php_m4_t2",
            "PHP and MySQL: Implementing Create, Read, Update, Delete (CRUD) Operations",
            ["CRUD Operations Implementation", "Prepared Statements with Parameter Binding", "SQL Injection Prevention", "Result Set Iteration (fetch, fetchAll)"],
            "CRUD represents the four fundamental data persistence operations: Create (INSERT), Read (SELECT), Update (UPDATE), and Delete (DELETE).",
            "SQL injection occurs when unescaped user inputs alter SQL query logic. Prepared statements split query compilation from data binding, neutralizing SQLi.",
            "Implementing secure CRUD workflows is the central responsibility of database application developers.",
            ["Execute secure INSERT, SELECT, UPDATE, DELETE queries.", "Explain how prepared statements prevent SQL injection.", "Bind parameters using bindParam() and execute().", "Iterate result sets with fetch() and fetchAll()."],
            "Prepared statements compile the query execution plan on the database first. Parameters are transmitted as pure literal data values.",
            [
                ("Prepared Statement", "Pre-compiled SQL template with placeholders (? or :name)."),
                ("Parameter Binding", "Mapping variables to SQL placeholders as raw data."),
                ("SQL Injection", "Attack injecting SQL commands through user inputs.")
            ],
            "1. Code/Data Separation: Never concatenate raw variables into SQL queries.\n2. Safe Iteration: Use fetch() for large datasets to conserve RAM.",
            "$stmt = $pdo->prepare('SELECT * FROM users WHERE email = ?'); $stmt->execute([$email]); $user = $stmt->fetch();",
            [
                "1. Construct SQL template with placeholders: INSERT INTO items (name, price) VALUES (?, ?).",
                "2. Transmit template to database via $pdo->prepare().",
                "3. Database engine compiles execution tree.",
                "4. Bind values and execute via $stmt->execute([$name, $price]).",
                "5. Retrieve results with fetch() or fetchAll().",
                "6. Check rowCount() for UPDATE and DELETE operations."
            ],
            ["Operation", "SQL Keyword", "PDO Method", "Result Inspection"],
            [
                ["Create", "INSERT INTO", "$stmt->execute($params)", "$pdo->lastInsertId()"],
                ["Read", "SELECT ... FROM", "$stmt->fetchAll()", "Array of record rows"],
                ["Update", "UPDATE ... SET", "$stmt->execute($params)", "$stmt->rowCount()"],
                ["Delete", "DELETE FROM", "$stmt->execute($params)", "$stmt->rowCount()"]
            ],
            "<?php\n// Secure CRUD with PDO\n$stmt = $pdo->prepare('INSERT INTO students (name, email) VALUES (?, ?)');\n$stmt->execute(['Rahul Roy', 'rahul@makaut.ac.in']);\n$newId = $pdo->lastInsertId();\n\n$stmt = $pdo->prepare('SELECT * FROM students WHERE id = ?');\n$stmt->execute([$newId]);\n$student = $stmt->fetch();\n?>",
            "<svg viewBox='0 0 800 180' xmlns='http://www.w3.org/2000/svg' style='width:100%;height:auto;background:#fff;border-radius:8px;border:1px solid #E5E9F1;'><rect x='40' y='30' width='330' height='120' rx='8' fill='#F7F8FC' stroke='#377FE6'/><text x='205' y='60' font-family='sans-serif' font-size='12' font-weight='700' fill='#377FE6' text-anchor='middle'>1. Compile Template</text><text x='60' y='90' font-family='monospace' font-size='10' fill='#19283D'>SELECT * FROM users WHERE id = ?</text><text x='60' y='110' font-family='sans-serif' font-size='10' fill='#28A994'>✓ Execution plan compiled</text><rect x='430' y='30' width='330' height='120' rx='8' fill='#F7F8FC' stroke='#28A994'/><text x='595' y='60' font-family='sans-serif' font-size='12' font-weight='700' fill='#28A994' text-anchor='middle'>2. Bind Parameters</text><text x='450' y='90' font-family='monospace' font-size='10' fill='#19283D'>execute([$input]);</text><text x='450' y='110' font-family='sans-serif' font-size='10' fill='#369B72'>✓ Input treated strictly as literal data</text></svg>",
            "Figure 4.2: Two-Phase Prepared Statement Execution Neutralizing SQL Injection",
            "Listing Students in HTML Table",
            "<?php\n$stmt = $pdo->query('SELECT id, name FROM students LIMIT 5');\nwhile ($row = $stmt->fetch()) {\n    echo '<li>' . htmlspecialchars($row['name']) . '</li>';\n}\n?>",
            [
                "Prepared statements completely prevent SQL injection attacks.",
                "Never concatenate $_GET or $_POST into SQL query strings.",
                "$pdo->lastInsertId() returns the primary key of a new row.",
                "$stmt->rowCount() returns the number of affected rows.",
                "fetchAll() loads all rows; fetch() retrieves one row at a time."
            ],
            "CRUD operations manage database records. Prepared statements ensure complete immunity against SQL injection.",
            "CRUD, Prepared Statements, Parameter Binding, SQL Injection, lastInsertId, rowCount.",
            "Prepare SQL template -> Bind data -> Execute -> Process results cursor.",
            "Concatenating raw variables into SQL queries, exposing the database to SQL injection."
        )
    ]
    modules.append({"module_no": 4, "title": "PHP and MySQL Integration", "hours": 6, "marks": 10, "topics": m4_topics})

    # Module 5
    m5_topics = [
        create_topic(
            "php_m5_t1",
            "Session Management: Understanding Sessions & Cookies, Creating and Managing Sessions",
            ["HTTP Cookies & Security Flags", "Session Lifecycle & session_start()", "Session Fixation Defense", "session_regenerate_id()"],
            "Session management enables stateful tracking over stateless HTTP connections by storing session files on the server and issuing a session ID cookie (PHPSESSID) to the client.",
            "Netscape invented cookies in 1994, which PHP uses to bind client requests to server-side session files.",
            "Secure session management protects user logins, shopping carts, and private data from credential hijacking.",
            ["Differentiate client cookies from server sessions.", "Configure HttpOnly, Secure, and SameSite flags.", "Manage sessions via session_start() and $_SESSION.", "Prevent session fixation using session_regenerate_id()."],
            "Cookies reside in the browser (max 4KB). Sessions reside on the server storage, referenced by a unique session identifier cookie.",
            [
                ("PHPSESSID", "Standard session identifier cookie passed in HTTP request headers."),
                ("HttpOnly", "Flag preventing JavaScript from accessing the cookie via document.cookie."),
                ("SameSite", "Cookie flag (Strict/Lax) shielding cookies from Cross-Site Request Forgery.")
            ],
            "1. ID Regeneration: Always regenerate session ID upon user login.\n2. Server Storage: Store sensitive data in $_SESSION, never in plaintext cookies.",
            "session_start(['cookie_httponly' => true, 'cookie_samesite' => 'Strict']); $_SESSION['user_id'] = $id;",
            [
                "1. Browser makes request to server.",
                "2. session_start() inspects incoming PHPSESSID cookie.",
                "3. If missing: generates new session token and creates server file.",
                "4. If present: reads server file and populates $_SESSION.",
                "5. Upon login: session_regenerate_id(true) issues new token.",
                "6. Upon logout: $_SESSION = []; session_destroy();"
            ],
            ["Dimension", "HTTP Cookie", "PHP Session"],
            [
                ["Storage", "Client Web Browser disk", "Server Filesystem / Redis"],
                ["Capacity", "4KB per domain", "Bounded only by server memory"],
                ["Security", "Vulnerable to client tampering", "High; concealed on server"],
                ["Bandwidth", "Sent on every HTTP header", "Only session ID cookie sent"]
            ],
            "<?php\nsession_start([\n    'cookie_httponly' => true,\n    'cookie_secure' => true,\n    'cookie_samesite' => 'Strict'\n]);\n$_SESSION['user'] = 'Anita';\n?>",
            "<svg viewBox='0 0 800 180' xmlns='http://www.w3.org/2000/svg' style='width:100%;height:auto;background:#fff;border-radius:8px;border:1px solid #E5E9F1;'><rect x='40' y='30' width='220' height='120' rx='8' fill='#F7F8FC' stroke='#377FE6'/><text x='150' y='60' font-family='sans-serif' font-size='12' font-weight='700' fill='#377FE6' text-anchor='middle'>Client Browser</text><text x='60' y='90' font-family='monospace' font-size='10' fill='#19283D'>PHPSESSID=a8f9c1...</text><text x='60' y='110' font-family='sans-serif' font-size='10' fill='#617087'>HttpOnly &amp; SameSite</text><path d='M 265 90 L 325 90' stroke='#377FE6' stroke-width='2'/><rect x='330' y='30' width='220' height='120' rx='8' fill='#F7F8FC' stroke='#786CE5'/><text x='440' y='60' font-family='sans-serif' font-size='12' font-weight='700' fill='#786CE5' text-anchor='middle'>PHP Runtime</text><text x='350' y='90' font-family='monospace' font-size='10' fill='#19283D'>session_start()</text><text x='350' y='110' font-family='sans-serif' font-size='10' fill='#369B72'>session_regenerate_id()</text><path d='M 555 90 L 615 90' stroke='#28A994' stroke-width='2'/><rect x='620' y='30' width='140' height='120' rx='8' fill='#F7F8FC' stroke='#28A994'/><text x='690' y='60' font-family='sans-serif' font-size='12' font-weight='700' fill='#28A994' text-anchor='middle'>Server Storage</text><text x='640' y='90' font-family='sans-serif' font-size='10' fill='#19283D'>/tmp/sess_a8f9...</text><text x='640' y='110' font-family='sans-serif' font-size='10' fill='#617087'>user_id: 42</text></svg>",
            "Figure 5.1: Session Management Lifecycle & ID Binding",
            "Authentication Gatekeeper Script",
            "<?php\nsession_start();\nif (empty($_SESSION['auth'])) {\n    header('Location: login.php');\n    exit;\n}\necho 'Welcome, ' . htmlspecialchars($_SESSION['user']);\n?>",
            [
                "session_start() must be called before sending any HTML output.",
                "session_regenerate_id(true) neutralizes session fixation exploits.",
                "Cookies have a 4KB size limitation; sessions store large arrays.",
                "HttpOnly cookies cannot be stolen by JavaScript XSS attacks.",
                "SameSite=Strict shields applications from CSRF attacks."
            ],
            "Session management links stateless requests to server state. Proper cookie flags and token regeneration safeguard accounts.",
            "PHPSESSID, session_start, session_regenerate_id, HttpOnly, SameSite.",
            "Request -> Cookie inspection -> Session deserialization -> ID regeneration on auth.",
            "Outputting HTML before session_start(), causing headers already sent error."
        ),
        create_topic(
            "php_m5_t2",
            "User Authentication: Building User Login System & Password Hashing",
            ["Flaws of MD5 & SHA1", "Bcrypt & Argon2 Algorithms", "password_hash() & Cost Tuning", "password_verify() Verification"],
            "User authentication verifies user identity. Modern PHP authentication uses one-way salted key derivation functions (Bcrypt and Argon2id).",
            "Plaintext storage and fast hashes like MD5 and SHA-1 can be cracked in seconds via GPU rigs. PHP 5.5 introduced the native Password Hashing API.",
            "Secure hashing protects user passwords even if the underlying database is leaked or stolen.",
            ["Explain why MD5 and SHA-1 are insecure.", "Generate salted hashes using password_hash().", "Verify passwords safely with password_verify().", "Understand work factor cost tuning."],
            "Password hashing is one-way. It includes a random salt and computational cost factor to resist brute-force attacks.",
            [
                ("Salt", "Random bytes appended to passwords to prevent rainbow table attacks."),
                ("Bcrypt", "Key derivation algorithm based on Blowfish with adjustable work factor."),
                ("password_verify()", "Timing-safe function verifying plaintext passwords against stored hashes.")
            ],
            "1. Never Plaintext: Hash passwords immediately upon receipt.\n2. Timing Safe: Always use password_verify() to defeat timing attacks.",
            "$h = password_hash($pass, PASSWORD_DEFAULT, ['cost' => 12]); if (password_verify($pass, $h)) {...}",
            [
                "1. User submits password via HTTPS POST.",
                "2. password_hash() creates random salt and generates 60-char Bcrypt hash.",
                "3. Hash is stored in MySQL database VARCHAR(255) column.",
                "4. On login: Retrieve stored hash for the user.",
                "5. password_verify() hashes candidate input with stored salt and cost.",
                "6. If matches in constant time: authentication succeeds."
            ],
            ["Algorithm", "Type", "Brute-Force Resistance", "Status"],
            [
                ["MD5", "Fast Cryptographic Hash", "Zero (broken by GPUs)", "Deprecated / Insecure"],
                ["SHA-256", "General Hash", "Poor for passwords (too fast)", "Unsuitable"],
                ["Bcrypt", "Adaptive Key Derivation", "High (adjustable work cost)", "Standard (PASSWORD_BCRYPT)"],
                ["Argon2id", "Memory-Hard Function", "Highest (resists ASIC rigs)", "Recommended (PASSWORD_ARGON2ID)"]
            ],
            "<?php\n// Registration\n$hash = password_hash($_POST['password'], PASSWORD_DEFAULT, ['cost' => 12]);\n// Login\nif (password_verify($_POST['password'], $storedHash)) {\n    session_regenerate_id(true);\n    $_SESSION['auth'] = true;\n}\n?>",
            "<svg viewBox='0 0 800 180' xmlns='http://www.w3.org/2000/svg' style='width:100%;height:auto;background:#fff;border-radius:8px;border:1px solid #E5E9F1;'><rect x='40' y='30' width='720' height='55' rx='6' fill='#FFFFFF' stroke='#8DB9F0'/><text x='55' y='63' font-family='monospace' font-size='12' font-weight='700' fill='#19283D'><tspan fill='#D65F64'>$2y$</tspan><tspan fill='#377FE6'>12$</tspan><tspan fill='#786CE5'>N9qo8uLOickgx2ZMRZoMye</tspan><tspan fill='#28A994'>IjZAgcfl7p92ldGxad68LJZdL17lhWy</tspan></text><text x='65' y='110' font-family='sans-serif' font-size='10' font-weight='700' fill='#D65F64'>Algorithm (Bcrypt)</text><text x='160' y='110' font-family='sans-serif' font-size='10' font-weight='700' fill='#377FE6'>Cost Factor (12)</text><text x='300' y='110' font-family='sans-serif' font-size='10' font-weight='700' fill='#786CE5'>22-char Random Salt</text><text x='550' y='110' font-family='sans-serif' font-size='10' font-weight='700' fill='#28A994'>31-char Hash Digest</text><rect x='40' y='130' width='720' height='30' rx='4' fill='#E8F6F3'/><text x='400' y='150' font-family='sans-serif' font-size='10' font-weight='600' fill='#1B6F61' text-anchor='middle'>password_verify() compares candidate input against stored hash in constant time</text></svg>",
            "Figure 5.2: Bcrypt Hash Anatomy and Verification Workflow",
            "Testing Password Hashing",
            "<?php\n$h = password_hash('Secret123', PASSWORD_BCRYPT);\necho password_verify('Secret123', $h) ? 'Valid' : 'Invalid';\n?>",
            [
                "Never use MD5 or SHA-1 for passwords; they lack work factors.",
                "password_hash() automatically generates unique random salts.",
                "password_verify() prevents timing attacks with constant-time comparison.",
                "Database password columns should be VARCHAR(255).",
                "password_needs_rehash() checks if cost settings have been updated."
            ],
            "Secure authentication requires salted, adaptive hashing. PHP's password_hash() and password_verify() provide industry standard protection.",
            "password_hash, password_verify, Bcrypt, Argon2, Salt, Cost Factor.",
            "Plain password -> Random salt -> Work factor loops -> Stored hash -> password_verify().",
            "Using md5() to hash passwords, rendering them vulnerable to rainbow table lookups."
        ),
        create_topic(
            "php_m5_t3",
            "Error Handling and File Handling in PHP: Reading, Writing and Uploading Files",
            ["Structured Exceptions (try-catch)", "File Operations (fopen, file_get_contents)", "Secure File Upload Pipeline ($_FILES)", "MIME Type Validation & Whitelisting"],
            "File handling allows reading, writing, and uploading files on the server. Secure upload pipelines enforce MIME inspection, extension whitelisting, and execution prevention.",
            "Unrestricted file uploads represent a severe vulnerability. If an attacker uploads a .php file into a public directory, they gain Remote Code Execution (RCE).",
            "Engineering secure file upload pipelines ensures safety for profile images, assignment PDFs, and spreadsheets.",
            ["Perform atomic file reads and writes with file_get_contents/file_put_contents.", "Inspect $_FILES metadata.", "Validate MIME types using finfo_file().", "Relocate uploads using move_uploaded_file()."],
            "Uploaded files stage in a temporary folder. The PHP script validates magic bytes and moves the file to a permanent directory with a randomized filename.",
            [
                ("$_FILES", "Superglobal array containing uploaded file metadata and temp paths."),
                ("finfo_file()", "Inspects binary magic bytes to determine true MIME types."),
                ("move_uploaded_file()", "Validates and moves an uploaded file safely.")
            ],
            "1. Magic Bytes Check: Never trust client file extensions; inspect binary headers.\n2. Block Execution: Store uploads outside document root or disable script execution.",
            "if (move_uploaded_file($_FILES['doc']['tmp_name'], $targetPath)) {...}",
            [
                "1. Form includes method='POST' and enctype='multipart/form-data'.",
                "2. User selects file and submits; PHP stages it in /tmp.",
                "3. Script verifies $_FILES['upload']['error'] === UPLOAD_ERR_OK.",
                "4. Check file size against limit (e.g. 5MB).",
                "5. Verify MIME type using finfo_file(FILEINFO_MIME_TYPE).",
                "6. Check extension against strict whitelist (['jpg', 'png', 'pdf']).",
                "7. Generate random filename using bin2hex(random_bytes(16)).",
                "8. Relocate file using move_uploaded_file()."
            ],
            ["Function", "Operation", "Best Use Case"],
            [
                ["file_get_contents()", "Read full file into memory", "Small text/JSON files"],
                ["file_put_contents()", "Write full file with LOCK_EX", "Writing logs/caches"],
                ["move_uploaded_file()", "Relocate uploaded file", "Completing HTTP uploads"]
            ],
            "<?php\nif ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_FILES['doc'])) {\n    $f = $_FILES['doc'];\n    if ($f['error'] === UPLOAD_ERR_OK && $f['size'] <= 2*1024*1024) {\n        $finfo = new finfo(FILEINFO_MIME_TYPE);\n        if ($finfo->file($f['tmp_name']) === 'application/pdf') {\n            $dest = __DIR__ . '/uploads/' . bin2hex(random_bytes(16)) . '.pdf';\n            move_uploaded_file($f['tmp_name'], $dest);\n        }\n    }\n}\n?>",
            "<svg viewBox='0 0 800 180' xmlns='http://www.w3.org/2000/svg' style='width:100%;height:auto;background:#fff;border-radius:8px;border:1px solid #E5E9F1;'><rect x='30' y='30' width='160' height='120' rx='8' fill='#F7F8FC' stroke='#786CE5'/><text x='110' y='60' font-family='sans-serif' font-size='11' font-weight='700' fill='#786CE5' text-anchor='middle'>1. Error &amp; Size</text><text x='45' y='90' font-family='sans-serif' font-size='10' fill='#19283D'>UPLOAD_ERR_OK</text><text x='45' y='110' font-family='sans-serif' font-size='10' fill='#617087'>Size &lt; 5MB</text><path d='M 195 90 L 225 90' stroke='#377FE6' stroke-width='2'/><rect x='230' y='30' width='160' height='120' rx='8' fill='#F7F8FC' stroke='#377FE6'/><text x='310' y='60' font-family='sans-serif' font-size='11' font-weight='700' fill='#377FE6' text-anchor='middle'>2. Magic Bytes</text><text x='245' y='90' font-family='sans-serif' font-size='10' fill='#19283D'>finfo_file()</text><text x='245' y='110' font-family='sans-serif' font-size='10' fill='#369B72'>Real MIME check</text><path d='M 395 90 L 425 90' stroke='#377FE6' stroke-width='2'/><rect x='430' y='30' width='160' height='120' rx='8' fill='#F7F8FC' stroke='#28A994'/><text x='510' y='60' font-family='sans-serif' font-size='11' font-weight='700' fill='#28A994' text-anchor='middle'>3. Random Name</text><text x='445' y='90' font-family='sans-serif' font-size='10' fill='#19283D'>random_bytes(16)</text><text x='445' y='110' font-family='sans-serif' font-size='10' fill='#617087'>Prevent overwrite</text><path d='M 595 90 L 625 90' stroke='#28A994' stroke-width='2'/><rect x='630' y='30' width='140' height='120' rx='8' fill='#F7F8FC' stroke='#369B72'/><text x='700' y='60' font-family='sans-serif' font-size='11' font-weight='700' fill='#369B72' text-anchor='middle'>4. Storage</text><text x='645' y='90' font-family='sans-serif' font-size='10' fill='#19283D'>move_uploaded()</text><text x='645' y='110' font-family='sans-serif' font-size='10' fill='#369B72'>Safe folder</text></svg>",
            "Figure 5.3: Secure File Upload Validation Pipeline",
            "Appending Access Logs Safely",
            "<?php\n$entry = date('Y-m-d H:i:s') . ' User login\n';\nfile_put_contents('log.txt', $entry, FILE_APPEND | LOCK_EX);\n?>",
            [
                "Always use move_uploaded_file() to finalize uploads.",
                "Inspect file headers using finfo_file() to verify actual MIME type.",
                "Generate random filenames to avoid directory traversal risks.",
                "Store uploaded files in non-executable directories.",
                "Use LOCK_EX with file_put_contents() to prevent write collisions."
            ],
            "File handling requires validation of permissions, error codes, and MIME types. Strict upload pipelines prevent server code execution.",
            "$_FILES, move_uploaded_file, finfo_file, LOCK_EX, Magic Bytes.",
            "Multipart POST -> Temp folder -> MIME validation -> Random name -> move_uploaded_file.",
            "Trusting user-supplied filename extensions directly, allowing .php webshell uploads."
        ),
        create_topic(
            "php_m5_t4",
            "Security in PHP: SQL Injection Prevention, XSS Protection & Securing File Uploads",
            ["OWASP Top 10 Vulnerabilities", "SQL Injection Vector Defense", "Cross-Site Scripting (XSS) Mitigation", "CSRF Tokens & Timing-Safe Comparison"],
            "Web security encompasses defenses against common vulnerabilities including SQL Injection, Cross-Site Scripting (XSS), and Cross-Site Request Forgery (CSRF).",
            "The OWASP Foundation documents Injection and Broken Access Control as primary threats. PHP provides native defenses including prepared statements, entity escaping, and CSRF tokens.",
            "Robust security engineering protects student databases and enterprise applications against data exfiltration and credential theft.",
            ["Defend against SQL injection using prepared statements.", "Neutralize XSS using htmlspecialchars().", "Implement synchronizer CSRF tokens.", "Apply timing-attack safe comparisons using hash_equals()."],
            "SQLi attacks the database. XSS attacks client browsers via injected scripts. CSRF tricks authenticated users into submitting unwanted commands.",
            [
                ("SQL Injection", "Altering SQL query logic using malicious user inputs."),
                ("XSS", "Injecting client-side scripts into web pages viewed by others."),
                ("CSRF", "Forcing an authenticated browser to transmit forged HTTP requests."),
                ("Anti-CSRF Token", "Secret per-session token validated upon state-changing requests.")
            ],
            "1. Defense in Depth: Combine input validation, output encoding, and access controls.\n2. Timing Safe Comparison: Use hash_equals() for comparing secret tokens.",
            "if (!hash_equals($_SESSION['csrf'], $_POST['csrf'])) { die('CSRF verification failed'); }",
            [
                "1. Attacker hosts a malicious page triggering a request to target site.",
                "2. Victim visits malicious site while holding an active session cookie on target site.",
                "3. Browser automatically attaches target session cookies.",
                "4. Target server validates session and would execute forged command without CSRF defense.",
                "5. DEFENSE: Target server embeds unique secret token in legitimate forms.",
                "6. Malicious external site cannot read token due to Same-Origin Policy.",
                "7. Server compares tokens using hash_equals() and blocks forged requests."
            ],
            ["Vulnerability", "Target", "Attack Vector", "Primary Defense"],
            [
                ["SQL Injection", "MySQL Database", "Manipulated query strings", "PDO Prepared Statements"],
                ["XSS", "User Browser", "Injected JavaScript tags", "htmlspecialchars(ENT_QUOTES)"],
                ["CSRF", "User Session", "Forged cross-site requests", "Secret CSRF Tokens + SameSite cookies"]
            ],
            "<?php\nsession_start();\n// Form generation\n$_SESSION['csrf'] = $_SESSION['csrf'] ?? bin2hex(random_bytes(32));\n// Form submission check\nif ($_SERVER['REQUEST_METHOD'] === 'POST') {\n    if (!hash_equals($_SESSION['csrf'], $_POST['csrf'] ?? '')) {\n        http_response_code(403);\n        die('CSRF token mismatch.');\n    }\n}\n?>",
            "<svg viewBox='0 0 800 180' xmlns='http://www.w3.org/2000/svg' style='width:100%;height:auto;background:#fff;border-radius:8px;border:1px solid #E5E9F1;'><rect x='40' y='30' width='220' height='120' rx='8' fill='#F7F8FC' stroke='#D65F64'/><text x='150' y='60' font-family='sans-serif' font-size='12' font-weight='700' fill='#D65F64' text-anchor='middle'>Attacker Web Page</text><text x='60' y='90' font-family='sans-serif' font-size='10' fill='#19283D'>• Forged POST request</text><text x='60' y='110' font-family='sans-serif' font-size='10' fill='#D65F64'>⚠ No secret CSRF token</text><path d='M 265 90 L 325 90' stroke='#D65F64' stroke-width='2'/><rect x='330' y='30' width='220' height='120' rx='8' fill='#F7F8FC' stroke='#377FE6'/><text x='440' y='60' font-family='sans-serif' font-size='12' font-weight='700' fill='#377FE6' text-anchor='middle'>Victim Browser</text><text x='350' y='90' font-family='sans-serif' font-size='10' fill='#19283D'>• Active Session Cookie</text><text x='350' y='110' font-family='sans-serif' font-size='10' fill='#617087'>• Cookie automatically sent</text><path d='M 555 90 L 615 90' stroke='#369B72' stroke-width='2'/><rect x='620' y='30' width='140' height='120' rx='8' fill='#F7F8FC' stroke='#369B72'/><text x='690' y='60' font-family='sans-serif' font-size='12' font-weight='700' fill='#369B72' text-anchor='middle'>Server Check</text><text x='635' y='90' font-family='monospace' font-size='9' fill='#19283D'>hash_equals()</text><text x='635' y='110' font-family='sans-serif' font-size='10' font-weight='700' fill='#369B72'>✓ BLOCKED</text></svg>",
            "Figure 5.4: CSRF Attack Vector and Synchronizer Token Defense",
            "Hidden CSRF Input in HTML Form",
            "<form method='POST'>\n  <input type='hidden' name='csrf' value='<?= $_SESSION['csrf'] ?>'>\n  <button type='submit'>Transfer</button>\n</form>",
            [
                "SQL Injection is defeated by prepared statements with bound parameters.",
                "XSS is prevented by escaping output with htmlspecialchars().",
                "CSRF is mitigated using secret per-session tokens.",
                "Always use hash_equals() to compare tokens to prevent timing attacks.",
                "Apply Content Security Policy (CSP) headers to restrict script sources."
            ],
            "Web application security requires comprehensive defense against SQLi (prepared statements), XSS (escaping), and CSRF (tokens).",
            "SQL Injection, XSS, CSRF, Anti-CSRF Token, hash_equals, CSP.",
            "Token generation -> Form inclusion -> Server hash_equals verification -> Request authorization.",
            "Comparing security tokens using standard `==`, introducing timing attack vulnerabilities."
        )
    ]
    modules.append({"module_no": 5, "title": "Session Management, Authentication, File Handling & Security", "hours": 4, "marks": 15, "topics": m5_topics})

    # Module 6
    m6_topics = [
        create_topic(
            "php_m6_t1",
            "Advanced PHP Concepts: Object-Oriented PHP, Classes, Objects and Inheritance",
            ["Classes & Object Instantiation", "Visibility Modifiers (public, protected, private)", "Constructors (__construct)", "Inheritance (extends) & parent::"],
            "Object-Oriented Programming (OOP) in PHP models software systems around modular classes containing state properties and method behaviors.",
            "PHP 5 introduced the Zend Engine II with formal visibility controls, abstract classes, and interfaces. PHP 8 added constructor property promotion.",
            "OOP principles (Encapsulation, Inheritance, Polymorphism, Abstraction) form the foundation of modern frameworks like Laravel and Symfony.",
            ["Declare classes and instantiate objects.", "Apply public, protected, and private visibility modifiers.", "Implement constructor and destructor methods.", "Extend classes using inheritance and override methods."],
            "Classes are blueprints. Objects are instances in memory. Encapsulation hides internal state behind access modifiers.",
            [
                ("Encapsulation", "Hiding internal object details behind private and protected visibility modifiers."),
                ("Inheritance", "Deriving child classes from a parent class using the `extends` keyword."),
                ("$this", "Pseudo-variable referencing the current object instance.")
            ],
            "1. Single Responsibility: A class should have only one reason to change.\n2. Access Restriction: Keep properties protected or private, providing getters/setters.",
            "class Student extends User { public function __construct(string $n) { parent::__construct($n); } }",
            [
                "1. Class defined using `class` keyword.",
                "2. Properties declared with visibility modifiers.",
                "3. __construct() initializes state during instantiation.",
                "4. Objects instantiated with `$obj = new ClassName()`.",
                "5. Methods invoked via object operator `->`.",
                "6. Subclasses extend parent using `extends` and override methods."
            ],
            ["Modifier", "Inside Class", "Derived Class", "External Code"],
            [
                ["public", "Accessible", "Accessible", "Accessible"],
                ["protected", "Accessible", "Accessible", "Blocked"],
                ["private", "Accessible", "Blocked", "Blocked"]
            ],
            "<?php\nclass User {\n    public function __construct(protected string $name) {}\n    public function getName(): string { return $this->name; }\n}\nclass Student extends User {\n    public function __construct(string $name, private string $roll) {\n        parent::__construct($name);\n    }\n    public function getRoll(): string { return $this->roll; }\n}\n$s = new Student('Priya', 'BCA501');\necho $s->getName() . ' ' . $s->getRoll();\n?>",
            "<svg viewBox='0 0 800 180' xmlns='http://www.w3.org/2000/svg' style='width:100%;height:auto;background:#fff;border-radius:8px;border:1px solid #E5E9F1;'><rect x='60' y='30' width='280' height='120' rx='8' fill='#F7F8FC' stroke='#786CE5'/><text x='200' y='60' font-family='sans-serif' font-size='12' font-weight='700' fill='#786CE5' text-anchor='middle'>Base Class: User</text><text x='80' y='90' font-family='monospace' font-size='10' fill='#19283D'># protected string $name</text><text x='80' y='110' font-family='monospace' font-size='10' fill='#377FE6'>+ public getName()</text><path d='M 345 90 L 445 90' stroke='#377FE6' stroke-width='2'/><text x='395' y='80' font-family='sans-serif' font-size='9' font-weight='700' fill='#377FE6' text-anchor='middle'>extends</text><rect x='450' y='30' width='290' height='120' rx='8' fill='#F7F8FC' stroke='#28A994'/><text x='595' y='60' font-family='sans-serif' font-size='12' font-weight='700' fill='#28A994' text-anchor='middle'>Child Class: Student</text><text x='470' y='90' font-family='monospace' font-size='10' fill='#D65F64'>- private string $roll</text><text x='470' y='110' font-family='monospace' font-size='10' fill='#28A994'>+ public getRoll()</text></svg>",
            "Figure 6.1: Class Inheritance and Member Visibility in PHP",
            "Instantiating Domain Objects",
            "<?php\n$student = new Student('Rahul', 'BCAC501');\necho $student->getName();\n?>",
            [
                "Classes bundle properties and methods into reusable objects.",
                "__construct() runs automatically upon object instantiation.",
                "PHP supports single inheritance using the extends keyword.",
                "parent::__construct() invokes parent initialization logic.",
                "PHP 8 supports constructor property promotion."
            ],
            "Object-Oriented PHP provides encapsulation, inheritance, and polymorphism for structuring large applications.",
            "Class, Object, public, protected, private, __construct, extends, parent::.",
            "Class definition -> Object creation -> Constructor invocation -> Method dispatch.",
            "Trying to access private properties from derived child classes."
        ),
        create_topic(
            "php_m6_t2",
            "Advanced PHP Concepts: PHP’s Built-in OOP Features (Interfaces, Abstract Classes, Namespaces)",
            ["Abstract Classes vs Interfaces", "Traits for Code Reuse", "Namespaces & PSR-4 Autoloading", "Magic Methods (__get, __set, __toString)"],
            "Built-in advanced OOP features provide structural tools for decoupling software through interfaces, abstract classes, traits, and namespaces.",
            "As PHP systems expanded, dependency management and name collisions necessitated namespaces (PHP 5.3) and traits (PHP 5.4).",
            "Modern frameworks rely on interfaces for dependency injection and namespaces for Composer package resolution.",
            ["Differentiate abstract classes from interfaces.", "Implement multiple interfaces in a single class.", "Organize code using namespaces.", "Use magic methods like __toString()."],
            "Abstract classes cannot be instantiated and provide partial implementations. Interfaces specify pure method contracts.",
            [
                ("Interface", "Pure contract specifying method signatures without implementation bodies."),
                ("Abstract Class", "Base class containing both concrete and abstract methods."),
                ("Namespace", "Virtual directory separating class symbols to prevent name collisions.")
            ],
            "1. Program to Interfaces: Code against abstractions rather than concrete classes.\n2. PSR-4 Standard: Map namespace paths directly to directory structures.",
            "interface Logger { public function log(string $msg): void; } | namespace App\\Services;",
            [
                "1. Interface declared using `interface` keyword.",
                "2. Concrete classes use `implements InterfaceName`.",
                "3. Class must implement every method signature in the interface.",
                "4. Namespaces declared at the top of PHP files.",
                "5. Composer autoloads classes based on namespace mappings.",
                "6. Magic methods intercept operations like string conversion."
            ],
            ["Dimension", "Abstract Class", "Interface"],
            [
                ["Method Body", "Allowed for concrete methods", "Forbidden (signatures only)"],
                ["Properties", "Instance properties allowed", "Constants only"],
                ["Inheritance", "Single class inheritance only", "Multiple interfaces implemented"]
            ],
            "<?php\nnamespace App\\Services;\ninterface Notifier {\n    public function notify(string $msg): bool;\n}\nclass EmailNotifier implements Notifier {\n    public function notify(string $msg): bool {\n        return mail('admin@makaut.ac.in', 'Alert', $msg);\n    }\n}\n?>",
            "<svg viewBox='0 0 800 180' xmlns='http://www.w3.org/2000/svg' style='width:100%;height:auto;background:#fff;border-radius:8px;border:1px solid #E5E9F1;'><rect x='280' y='30' width='240' height='50' rx='6' fill='#E9E8F8' stroke='#786CE5'/><text x='400' y='52' font-family='sans-serif' font-size='11' font-weight='700' fill='#786CE5' text-anchor='middle'>&lt;&lt;interface&gt;&gt; Notifier</text><text x='400' y='68' font-family='monospace' font-size='10' fill='#19283D' text-anchor='middle'>+ notify(string): bool</text><path d='M 240 125 L 340 85' stroke='#377FE6' stroke-width='2' stroke-dasharray='4,4'/><rect x='100' y='125' width='200' height='45' rx='6' fill='#ffffff' stroke='#377FE6'/><text x='200' y='145' font-family='sans-serif' font-size='10' font-weight='700' fill='#377FE6' text-anchor='middle'>EmailNotifier</text><text x='200' y='160' font-family='sans-serif' font-size='9' fill='#617087' text-anchor='middle'>implements notify()</text><path d='M 560 125 L 460 85' stroke='#28A994' stroke-width='2' stroke-dasharray='4,4'/><rect x='500' y='125' width='200' height='45' rx='6' fill='#ffffff' stroke='#28A994'/><text x='600' y='145' font-family='sans-serif' font-size='10' font-weight='700' fill='#28A994' text-anchor='middle'>SmsNotifier</text><text x='600' y='160' font-family='sans-serif' font-size='9' fill='#617087' text-anchor='middle'>implements notify()</text></svg>",
            "Figure 6.2: Interface Contracts and Polymorphism in PHP",
            "Implementing __toString() Magic Method",
            "<?php\nclass Course {\n    public function __construct(private string $code) {}\n    public function __toString(): string { return 'Course: ' . $this->code; }\n}\necho new Course('BCAC501');\n?>",
            [
                "A class can implement multiple interfaces simultaneously.",
                "Abstract classes cannot be directly instantiated.",
                "Namespaces prevent class naming clashes across external libraries.",
                "Traits share methods horizontally across unrelated classes.",
                "Magic methods start with double underscores (`__`)."
            ],
            "Interfaces establish binding contracts; abstract classes provide partial implementations; namespaces organize codebases.",
            "Interface, Abstract Class, Trait, Namespace, Magic Methods.",
            "Contract definition -> Implementation -> Namespace resolution -> Autoloading.",
            "Declaring concrete method bodies inside an interface."
        )
    ]
    modules.append({"module_no": 6, "title": "Advanced PHP Concepts", "hours": 5, "marks": 5, "topics": m6_topics})

    # Module 7
    m7_topics = [
        create_topic(
            "php_m7_t1",
            "Introduction to PHP Frameworks: Overview of Popular Frameworks (Laravel, CodeIgniter)",
            ["Popular PHP Frameworks Overview", "CodeIgniter Architecture", "Symfony Components", "Laravel Ecosystem"],
            "A web framework provides a standardized scaffolding of pre-tested components for routing, database mapping, authentication, and templating.",
            "The PHP framework ecosystem evolved from CodeIgniter in 2006 to Symfony and Laravel, which dominates modern enterprise PHP development.",
            "Understanding framework tradeoffs helps developers select the right tool based on team size, performance requirements, and complexity.",
            ["Compare Laravel and CodeIgniter architectures.", "Understand Composer dependency management.", "Identify framework use cases.", "Analyze performance tradeoffs."],
            "CodeIgniter offers lightweight speed and minimal configuration. Laravel offers an expressive full-stack ecosystem with built-in ORM.",
            [
                ("Laravel", "Modern expressive framework featuring Eloquent ORM and Blade."),
                ("CodeIgniter", "Lightweight high-performance MVC framework with small footprint."),
                ("Composer", "Industry-standard dependency management tool for PHP.")
            ],
            "1. Convention over Configuration: Adopt standard framework directory patterns.\n2. Component Reusability: Build upon mature, tested open-source libraries.",
            "composer create-project laravel/laravel app | php artisan serve",
            [
                "1. Composer installs framework dependencies.",
                "2. Web server routes requests to front controller.",
                "3. Routing maps URIs to controller methods.",
                "4. Framework executes middleware and authentication.",
                "5. Controller queries model and renders view."
            ],
            ["Framework", "Architecture", "ORM Engine", "Best Suited For"],
            [
                ["CodeIgniter 4", "Lightweight MVC (<2MB)", "Query Builder", "Shared hosting & fast simple apps"],
                ["Laravel 11", "Full-Stack Expressive", "Eloquent ORM", "Modern SaaS & complex portals"]
            ],
            "// composer.json dependency definition\n{\n    \"require\": {\n        \"php\": \"^8.2\",\n        \"laravel/framework\": \"^11.0\"\n    }\n}",
            "<svg viewBox='0 0 800 180' xmlns='http://www.w3.org/2000/svg' style='width:100%;height:auto;background:#fff;border-radius:8px;border:1px solid #E5E9F1;'><rect x='50' y='30' width='320' height='120' rx='8' fill='#F7F8FC' stroke='#EF846B'/><text x='210' y='60' font-family='sans-serif' font-size='12' font-weight='700' fill='#EF846B' text-anchor='middle'>CodeIgniter 4</text><text x='70' y='90' font-family='sans-serif' font-size='10' fill='#19283D'>• Lightweight (&lt; 2MB)</text><text x='70' y='110' font-family='sans-serif' font-size='10' fill='#19283D'>• Fast execution speeds</text><rect x='430' y='30' width='320' height='120' rx='8' fill='#F7F8FC' stroke='#D65F64'/><text x='590' y='60' font-family='sans-serif' font-size='12' font-weight='700' fill='#D65F64' text-anchor='middle'>Laravel 11</text><text x='450' y='90' font-family='sans-serif' font-size='10' fill='#19283D'>• Eloquent ORM &amp; Blade</text><text x='450' y='110' font-family='sans-serif' font-size='10' fill='#369B72'>• Complete full-stack ecosystem</text></svg>",
            "Figure 7.1: PHP Framework Comparison: CodeIgniter vs Laravel",
            "Artisan CLI Scaffold Command",
            "# Scaffolds controller and model in Laravel\nphp artisan make:model Student -c",
            [
                "Frameworks provide built-in security, routing, and database abstraction.",
                "Laravel is the most widely adopted PHP framework globally.",
                "CodeIgniter provides high performance with minimal server requirements.",
                "Composer manages dependencies and PSR-4 autoloading.",
                "Frameworks eliminate boilerplate code for authentication and sessions."
            ],
            "PHP frameworks streamline web engineering. CodeIgniter provides lightweight speed; Laravel provides a complete full-stack environment.",
            "Framework, Laravel, CodeIgniter, Eloquent, Composer, Artisan.",
            "Composer install -> Kernel bootstrap -> Routing -> Controller -> Output.",
            "Building large systems without frameworks, resulting in security vulnerabilities."
        ),
        create_topic(
            "php_m7_t2",
            "Introduction to PHP Frameworks: Basic MVC Architecture Concepts",
            ["Monolithic vs Decoupled Code", "Model Responsibilities", "View Responsibilities", "Controller Coordination"],
            "The Model-View-Controller (MVC) pattern decouples web applications into three layers: Model (database & data rules), View (presentation & UI), and Controller (input handling).",
            "Early PHP scripts combined HTML, database queries, and styling into single files (spaghetti code). MVC introduced clean separation of concerns.",
            "All modern enterprise web frameworks implement MVC to maximize code maintainability, testability, and team collaboration.",
            ["Explain responsibilities of Model, View, and Controller.", "Understand the Front Controller pattern (index.php).", "Trace an HTTP request through the MVC lifecycle.", "Contrast MVC with spaghetti code architectures."],
            "Models handle data. Views render the user interface. Controllers coordinate data flow between Models and Views.",
            [
                ("Model", "Data layer encapsulating database queries, schemas, and validation rules."),
                ("View", "Presentation layer rendering HTML markup and UI templates."),
                ("Controller", "Mediator handling user input, querying models, and selecting views."),
                ("Front Controller", "Single entry point (public/index.php) routing all incoming traffic.")
            ],
            "1. Separation of Concerns: Views never query databases; Models never render HTML.\n2. Lean Controllers: Keep controllers lightweight by delegating business logic to models.",
            "Route -> Controller::action() -> Model::query() -> View::render() -> HTTP Response",
            [
                "1. User sends HTTP request to /students.",
                "2. Web server routes request to public/index.php.",
                "3. Router dispatches request to StudentController@index.",
                "4. Controller calls Student::all() on the Model.",
                "5. Model queries MySQL and returns recordsets.",
                "6. Controller injects recordset into students.blade.php View.",
                "7. View formats HTML output.",
                "8. Controller returns rendered HTML to user."
            ],
            ["MVC Layer", "Role", "Allowed Contents", "Forbidden Contents"],
            [
                ["Model", "Data & Logic", "SQL, validations, relations", "HTML tags, HTTP headers"],
                ["View", "UI Display", "HTML5, CSS, template tags", "Direct SQL queries"],
                ["Controller", "Coordination", "Request parsing, model calls", "Complex SQL algorithms"]
            ],
            "<?php\n// Conceptual MVC Controller Action\nclass StudentController {\n    public function index() {\n        $students = StudentModel::getAll();\n        return view('students_list', ['data' => $students]);\n    }\n}\n?>",
            "<svg viewBox='0 0 800 180' xmlns='http://www.w3.org/2000/svg' style='width:100%;height:auto;background:#fff;border-radius:8px;border:1px solid #E5E9F1;'><rect x='40' y='30' width='200' height='120' rx='8' fill='#F7F8FC' stroke='#786CE5'/><text x='140' y='60' font-family='sans-serif' font-size='12' font-weight='700' fill='#786CE5' text-anchor='middle'>Controller</text><text x='140' y='90' font-family='sans-serif' font-size='10' fill='#19283D' text-anchor='middle'>Coordinates requests</text><path d='M 245 65 L 325 65' stroke='#377FE6' stroke-width='2'/><text x='285' y='55' font-family='sans-serif' font-size='9' font-weight='700' fill='#377FE6' text-anchor='middle'>Query</text><rect x='330' y='30' width='200' height='120' rx='8' fill='#F7F8FC' stroke='#28A994'/><text x='430' y='60' font-family='sans-serif' font-size='12' font-weight='700' fill='#28A994' text-anchor='middle'>Model</text><text x='430' y='90' font-family='sans-serif' font-size='10' fill='#19283D' text-anchor='middle'>Database persistence</text><path d='M 325 105 L 245 105' stroke='#28A994' stroke-width='2'/><text x='285' y='120' font-family='sans-serif' font-size='9' font-weight='700' fill='#28A994' text-anchor='middle'>Data</text><path d='M 245 130 L 595 130' stroke='#F2C75C' stroke-width='2'/><text x='420' y='145' font-family='sans-serif' font-size='9' font-weight='700' fill='#B38600' text-anchor='middle'>Pass data to view</text><rect x='600' y='30' width='160' height='120' rx='8' fill='#F7F8FC' stroke='#F2C75C'/><text x='680' y='60' font-family='sans-serif' font-size='12' font-weight='700' fill='#B38600' text-anchor='middle'>View</text><text x='680' y='90' font-family='sans-serif' font-size='10' fill='#19283D' text-anchor='middle'>HTML rendering</text></svg>",
            "Figure 7.2: MVC Data Flow and Layer Interactions",
            "Rendering Data in a View Template",
            "<!-- View: students_list.php -->\n<ul>\n<?php foreach ($data as $s): ?>\n    <li><?= htmlspecialchars($s['name']) ?></li>\n<?php endforeach; ?>\n</ul>",
            [
                "MVC separates data (Model), UI (View), and logic (Controller).",
                "The Front Controller (index.php) handles initial request entry.",
                "Views should never execute direct database queries.",
                "Controllers coordinate workflow without heavy SQL algorithms.",
                "MVC architecture facilitates automated unit testing."
            ],
            "The MVC architecture decouples concerns. Models manage data, Views format HTML, and Controllers coordinate requests.",
            "MVC, Model, View, Controller, Front Controller, Separation of Concerns.",
            "Request -> Router -> Controller -> Model -> View -> HTML Response.",
            "Placing SQL queries inside view templates, violating separation of concerns."
        )
    ]
    modules.append({"module_no": 7, "title": "Introduction to PHP Frameworks", "hours": 6, "marks": 10, "topics": m7_topics})

    # Module 8
    m8_topics = [
        create_topic(
            "php_m8_t1",
            "Laravel FrameWork: Routing in Laravel, Controllers, Passing Data to Views & Route Parameters",
            ["web.php Route Definitions", "Route Parameters & Regex Constraints", "Controller Actions", "Passing View Data (compact, with)"],
            "Laravel routing maps incoming URIs to controller actions. Controllers handle business logic and pass formatted data payloads to views.",
            "Laravel replaces physical file paths with expressive virtual routes defined in routes/web.php.",
            "Proper routing produces readable RESTful URLs and decouples public URL structures from internal file paths.",
            ["Define routes for GET, POST, PUT, DELETE methods.", "Capture required and optional route parameters.", "Create controllers via Artisan CLI.", "Pass data to views using compact() and with()."],
            "Routes define URL patterns. Controllers encapsulate business workflows. Data is passed as associative arrays into view templates.",
            [
                ("Route Parameter", "Dynamic URI segment captured as an argument in controller methods."),
                ("Resource Controller", "Controller providing methods for all 7 standard CRUD actions."),
                ("compact()", "PHP function creating an associative array from variable names.")
            ],
            "1. RESTful Standards: Align route verbs with HTTP actions.\n2. Route Protection: Guard sensitive routes with authentication middleware.",
            "Route::get('/students/{id}', [StudentController::class, 'show'])->name('students.show');",
            [
                "1. User visits /students/101 in web browser.",
                "2. Router matches pattern in routes/web.php.",
                "3. Parameter '101' is extracted.",
                "4. Router dispatches to StudentController::show($id).",
                "5. Controller finds record and passes it to view: return view('students.show', compact('student')).",
                "6. View renders and returns HTTP 200 response."
            ],
            ["HTTP Verb", "URI Pattern", "Controller Action", "Purpose"],
            [
                ["GET", "/students", "index()", "Display list of students"],
                ["GET", "/students/{id}", "show($id)", "Display single student"],
                ["POST", "/students", "store()", "Save new student record"]
            ],
            "<?php\n// routes/web.php\nuse App\\Http\\Controllers\\StudentController;\nRoute::get('/students/{id}', [StudentController::class, 'show']);\n\n// StudentController.php\npublic function show($id) {\n    $student = Student::findOrFail($id);\n    return view('students.show', compact('student'));\n}\n?>",
            "<svg viewBox='0 0 800 180' xmlns='http://www.w3.org/2000/svg' style='width:100%;height:auto;background:#fff;border-radius:8px;border:1px solid #E5E9F1;'><rect x='40' y='30' width='200' height='120' rx='8' fill='#F7F8FC' stroke='#377FE6'/><text x='140' y='60' font-family='sans-serif' font-size='12' font-weight='700' fill='#377FE6' text-anchor='middle'>HTTP Request</text><text x='140' y='90' font-family='monospace' font-size='10' fill='#19283D' text-anchor='middle'>GET /students/42</text><path d='M 245 90 L 305 90' stroke='#377FE6' stroke-width='2'/><rect x='310' y='30' width='200' height='120' rx='8' fill='#F7F8FC' stroke='#786CE5'/><text x='410' y='60' font-family='sans-serif' font-size='12' font-weight='700' fill='#786CE5' text-anchor='middle'>Router Match</text><text x='410' y='90' font-family='monospace' font-size='10' fill='#19283D' text-anchor='middle'>routes/web.php</text><path d='M 515 90 L 575 90' stroke='#28A994' stroke-width='2'/><rect x='580' y='30' width='180' height='120' rx='8' fill='#F7F8FC' stroke='#28A994'/><text x='670' y='60' font-family='sans-serif' font-size='12' font-weight='700' fill='#28A994' text-anchor='middle'>Controller</text><text x='670' y='90' font-family='monospace' font-size='10' fill='#1B6F61' text-anchor='middle'>show(42)</text></svg>",
            "Figure 8.1: Laravel Routing and Controller Dispatch",
            "Passing Data to a View",
            "<?php\n$title = 'MAKAUT Semester V';\nreturn view('home', compact('title'));\n?>",
            [
                "Web routes are registered in routes/web.php.",
                "Parameters inside curly braces {id} are passed to controller methods.",
                "Route::resource() scaffolds all 7 standard CRUD routes.",
                "Named routes allow referencing routes cleanly in templates.",
                "compact('var') builds an associative array for view injection."
            ],
            "Routing maps web requests to controller actions. Controllers process logic and return views with data payloads.",
            "Route, Controller, Route Parameters, compact, Resource Controller.",
            "URI -> Route match -> Controller method -> View data injection -> Response.",
            "Forgetting to import the Controller class in routes/web.php."
        ),
        create_topic(
            "php_m8_t2",
            "Laravel FrameWork: Introduction to Blade Templating, Directives, Inheritance & Views",
            ["Blade Templating Overview", "Layout Inheritance (@extends, @yield, @section)", "Blade Directives (@if, @foreach, @csrf)", "Escaped Output {{ $var }}"],
            "Blade is Laravel's templating engine. It compiles clean template directives into raw cached PHP scripts for fast execution.",
            "Traditional templates mixed noisy PHP tags with HTML. Blade introduced clean @directives and double-curly braces for automatic escaping.",
            "Blade's layout inheritance allows defining a master layout once and extending it across all views, ensuring visual consistency.",
            ["Build master layouts with @yield.", "Extend master layouts using @extends and @section.", "Render escaped output using {{ }}.", "Apply directives: @if, @foreach, @csrf."],
            "Blade templates use .blade.php extensions. The compiler translates directives into raw PHP cached in storage/framework/views.",
            [
                ("@extends", "Declares which master layout the current child view inherits from."),
                ("@yield", "Placeholder slot in master layout where child templates inject content."),
                ("@section", "Defines content in a child view to inject into a layout @yield slot."),
                ("{{ $val }}", "Echoes data with automatic htmlspecialchars() escaping.")
            ],
            "1. Layout Reusability: Master layout is authored once and inherited by child views.\n2. Safe Output: Double curly braces {{ }} escape HTML to neutralize XSS.",
            "@extends('layouts.app') @section('content') <h1>{{ $title }}</h1> @endsection",
            [
                "1. Master layout created at resources/views/layouts/app.blade.php with @yield('content').",
                "2. Child view created with @extends('layouts.app').",
                "3. Content wrapped inside @section('content') ... @endsection.",
                "4. Controller returns view('students.index', ['title' => 'List']).",
                "5. Blade compiles directives to raw PHP and caches output.",
                "6. Cached file executes and delivers compiled HTML to user."
            ],
            ["Blade Directive", "PHP Equivalent", "Purpose"],
            [
                ["{{ $name }}", "htmlspecialchars($name, ENT_QUOTES)", "Escapes variables against XSS"],
                ["@extends('app')", "Layout inheritance", "Inherits master page template"],
                ["@yield('content')", "Slot placeholder", "Defines content injection slot"],
                ["@csrf", "<input type='hidden' name='_token' ...>", "Generates anti-CSRF form input"]
            ],
            "<!-- Layout: layouts/app.blade.php -->\n<!DOCTYPE html>\n<html>\n<body>\n  <header><h1>Portal</h1></header>\n  <main>@yield('content')</main>\n</body>\n</html>\n\n<!-- View: home.blade.php -->\n@extends('layouts.app')\n@section('content')\n  <p>Welcome, {{ $user }}</p>\n@endsection",
            "<svg viewBox='0 0 800 180' xmlns='http://www.w3.org/2000/svg' style='width:100%;height:auto;background:#fff;border-radius:8px;border:1px solid #E5E9F1;'><rect x='40' y='30' width='280' height='120' rx='8' fill='#F7F8FC' stroke='#786CE5'/><text x='180' y='60' font-family='sans-serif' font-size='12' font-weight='700' fill='#786CE5' text-anchor='middle'>Master Layout (app.blade.php)</text><rect x='60' y='80' width='240' height='45' rx='4' fill='#FFF2EB' stroke='#EF846B' stroke-dasharray='3,3'/><text x='180' y='108' font-family='monospace' font-size='11' font-weight='700' fill='#EF846B' text-anchor='middle'>@yield('content')</text><path d='M 325 90 L 435 90' stroke='#377FE6' stroke-width='2'/><text x='380' y='80' font-family='sans-serif' font-size='9' font-weight='700' fill='#377FE6' text-anchor='middle'>@extends</text><rect x='440' y='30' width='300' height='120' rx='8' fill='#F7F8FC' stroke='#28A994'/><text x='590' y='60' font-family='sans-serif' font-size='12' font-weight='700' fill='#28A994' text-anchor='middle'>Child View (home.blade.php)</text><text x='590' y='95' font-family='monospace' font-size='10' fill='#1B6F61' text-anchor='middle'>@section('content')</text><text x='590' y='115' font-family='sans-serif' font-size='10' fill='#19283D' text-anchor='middle'>Injects specific page markup</text></svg>",
            "Figure 8.2: Blade Template Inheritance Workflow",
            "Blade Form with CSRF Protection",
            "<form method=\"POST\" action=\"/submit\">\n    @csrf\n    <input name=\"name\" value=\"{{ old('name') }}\">\n    <button type=\"submit\">Submit</button>\n</form>",
            [
                "Blade files use the .blade.php file extension.",
                "Double curly braces {{ }} escape HTML entities automatically.",
                "@yield defines layout slots; @section injects content.",
                "@csrf generates hidden anti-CSRF token fields.",
                "@forelse handles loops with fallback empty states."
            ],
            "Blade provides expressive layout inheritance and directives. Compiled PHP templates ensure performance without overhead.",
            "Blade, @extends, @yield, @section, {{ }}, @csrf.",
            "Blade source -> Directive compilation -> Cached PHP -> HTML response.",
            "Using unescaped {!! $data !!} on untrusted user inputs."
        ),
        create_topic(
            "php_m8_t3",
            "Laravel FrameWork: Overview of Eloquent ORM, Defining Models, CRUD, Database Migrations & Relationships",
            ["Active Record in Eloquent", "Database Migrations", "Eloquent CRUD Operations", "Relational Associations (hasMany, belongsTo)"],
            "Eloquent ORM is Laravel's native Object-Relational Mapper implementing the Active Record pattern, where each database table corresponds to a PHP Model class.",
            "Database migrations provide version control for schemas. Eloquent relationships allow querying related tables through readable object methods.",
            "Eloquent eliminates boilerplate SQL, reduces query errors, and makes relational data modeling intuitive and maintainable.",
            ["Create database migrations using Artisan.", "Perform CRUD operations via Eloquent model methods.", "Define hasOne, hasMany, and belongsTo relationships.", "Eager-load relationships to solve the N+1 problem."],
            "Each model maps to a database table. Modifying model attributes and calling save() updates the database row automatically.",
            [
                ("Eloquent", "Laravel Active Record Object-Relational Mapper."),
                ("Migration", "Version-controlled PHP file defining database schema changes."),
                ("Eager Loading", "Loading related records upfront in one query via with() to eliminate N+1 bottlenecks.")
            ],
            "1. Schema Versioning: Always track database schema changes in migrations.\n2. Avoid N+1: Use with('relation') when displaying related records in loops.",
            "class Student extends Model { public function department() { return $this->belongsTo(Department::class); } }",
            [
                "1. Run php artisan make:migration create_students_table.",
                "2. Define columns in migration up() method.",
                "3. Execute php artisan migrate to generate tables in MySQL.",
                "4. Create Eloquent model inheriting Model.",
                "5. Define relationship methods (belongsTo, hasMany).",
                "6. Execute queries: Student::with('department')->where('gpa', '>=', 8)->get()."
            ],
            ["Relationship", "Method", "Foreign Key Location"],
            [
                ["One-to-Many", "$this->hasMany(Student::class)", "Stored in students table (department_id)"],
                ["Inverse", "$this->belongsTo(Department::class)", "Stored in students table (department_id)"]
            ],
            "<?php\n// Model definition\nnamespace App\\Models;\nuse Illuminate\\Database\\Eloquent\\Model;\n\nclass Student extends Model {\n    protected $fillable = ['name', 'department_id'];\n    public function department() {\n        return $this->belongsTo(Department::class);\n    }\n}\n// Eager loading query\n$students = Student::with('department')->get();\n?>",
            "<svg viewBox='0 0 800 180' xmlns='http://www.w3.org/2000/svg' style='width:100%;height:auto;background:#fff;border-radius:8px;border:1px solid #E5E9F1;'><rect x='40' y='30' width='220' height='120' rx='8' fill='#F7F8FC' stroke='#786CE5'/><text x='150' y='60' font-family='sans-serif' font-size='12' font-weight='700' fill='#786CE5' text-anchor='middle'>Department Model</text><text x='60' y='90' font-family='monospace' font-size='10' fill='#19283D'>hasMany(Student::class)</text><path d='M 265 90 L 345 90' stroke='#377FE6' stroke-width='2'/><text x='305' y='80' font-family='sans-serif' font-size='9' font-weight='700' fill='#377FE6' text-anchor='middle'>1 : N</text><rect x='350' y='30' width='230' height='120' rx='8' fill='#F7F8FC' stroke='#377FE6'/><text x='465' y='60' font-family='sans-serif' font-size='12' font-weight='700' fill='#377FE6' text-anchor='middle'>Student Model</text><text x='370' y='90' font-family='monospace' font-size='10' fill='#19283D'>belongsTo(Dept::class)</text><path d='M 585 90 L 635 90' stroke='#28A994' stroke-width='2'/><rect x='640' y='30' width='120' height='120' rx='8' fill='#F7F8FC' stroke='#28A994'/><text x='700' y='60' font-family='sans-serif' font-size='11' font-weight='700' fill='#28A994' text-anchor='middle'>MySQL</text><text x='650' y='90' font-family='sans-serif' font-size='10' fill='#19283D'>InnoDB Table</text></svg>",
            "Figure 8.3: Eloquent Model Relational Mapping",
            "Eloquent Query Execution",
            "<?php\n$toppers = Student::where('cgpa', '>=', 9.0)->orderByDesc('cgpa')->get();\nforeach ($toppers as $s) { echo $s->name; }\n?>",
            [
                "Eloquent models correspond to database tables via Active Record.",
                "Migrations track database schema changes in version control.",
                "Define relationships with hasMany() and belongsTo().",
                "Eager-load with with() to prevent N+1 performance bottlenecks.",
                "Specify $fillable to enable safe mass assignment."
            ],
            "Eloquent ORM maps database tables to object models. Migrations manage schema versions; relationships model relational links.",
            "Eloquent, Active Record, Migrations, belongsTo, hasMany, Eager Loading, N+1.",
            "Migration -> Table creation -> Model mapping -> Query builder -> Hydrated model collection.",
            "Looping over relations without eager loading, triggering N+1 queries."
        )
    ]
    modules.append({"module_no": 8, "title": "Laravel FrameWork", "hours": 8, "marks": 10, "topics": m8_topics})

    return modules