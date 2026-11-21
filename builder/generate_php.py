import json, os

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

modules = [
    {
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
                    "Port 80 conflicts can be resolved by changing port in httpd.conf.",
                    "Editing php.ini requires restarting Apache.",
                    "phpinfo() outputs comprehensive runtime information."
                ],
                "Local web servers simulate production environments. Configuration files manage memory, ports, and errors.",
                "htdocs, php.ini, httpd.conf, port 80, port 3306.",
                "Browser localhost -> Apache port 80 -> PHP parser -> MySQL 3306.",
                "Forgetting to restart Apache after editing php.ini."
            )
        ]
    },
    {
        "module_no": 2,
        "title": "PHP Basics, Functions, Arrays and Strings",
        "hours": 8,
        "marks": 10,
        "topics": [
            T(
                "php_m2_t1",
                "PHP Syntax, Variables, Data Types, Type Juggling & Control Structures",
                ["Variables Sigil ($)", "Data Types", "Type Juggling vs Strict Types", "Selection & Loops"],
                "PHP syntax supports procedural and object-oriented paradigms. Variables start with $ and are dynamically typed.",
                "PHP 7 and 8 introduced scalar type declarations and match expressions for strict computational evaluation.",
                "Mastery of control flow, data types, and equality operators prevents logic bugs and security flaws.",
                ["Understand loose (==) vs strict (===) equality.", "Manipulate scalar and compound data types.", "Use if-else, switch, and match constructs.", "Iterate collections with foreach loops."],
                "Variables are declared on assignment. Type juggling automatically coerces types during operations unless strict types are enabled.",
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
            T(
                "php_m2_t2",
                "Functions in PHP: Scope, File Inclusion & Built-in Library",
                ["User Functions & Return Types", "Variable Scope", "include vs require", "Built-in Functions"],
                "Functions package reusable code blocks. PHP supports typed arguments, return types, and pass-by-reference.",
                "Modular functions allow breaking large systems into isolated, testable modules across multiple files.",
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
            T(
                "php_m2_t3",
                "Arrays & Strings: Array Functions, String Manipulation & Unicode Processing",
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
                "<svg viewBox='0 0 800 180' xmlns='http://www.w3.org/2000/svg' style='width:100%;height:auto;background:#fff;border-radius:8px;border:1px solid #E5E9F1;'><rect x='40' y='30' width='200' height='120' rx='8' fill='#F7F8FC' stroke='#377FE6'/><text x='140' y='60' font-family='sans-serif' font-size='12' font-weight='700' fill='#377FE6' text-anchor='middle'>Input Array</text><text x='140' y='95' font-family='monospace' font-size='10' fill='#19283D' text-anchor='middle'>[10, 25, 90, 55]</text><path d='M 245 90 L 305 90' stroke='#377FE6' stroke-width='2'/><rect x='310' y='30' width='200' height='120' rx='8' fill='#F7F8FC' stroke='#786CE5'/><text x='410' y='60' font-family='sans-serif' font-size='12' font-weight='700' fill='#786CE5' text-anchor='middle'>array_filter(>=50)</text><text x='410' y='95' font-family='monospace' font-size='10' fill='#19283D' text-anchor='middle'>[90, 55]</text><path d='M 515 90 L 575 90' stroke='#28A994' stroke-width='2'/><rect x='580' y='30' width='180' height='120' rx='8' fill='#F7F8FC' stroke='#28A994'/><text x='670' y='60' font-family='sans-serif' font-size='12' font-weight='700' fill='#28A994' text-anchor='middle'>implode(', ')</text><text x='670' y='95' font-family='monospace' font-size='11' font-weight='700' fill='#1B6F61' text-anchor='middle'>\"90, 55\"</text></svg>",
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
    }
]

print("Saving base modules...")
with open("builder/data/lessons_php.json", "w", encoding="utf-8") as f:
    json.dump(modules, f, indent=2)

print("Modules 1-2 written.")
