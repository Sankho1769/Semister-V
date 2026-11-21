# Model Examination Questions for BCAC501: PHP WITH MYSQL (10 Questions)

def get_php_exams():
    return [
    {
        "id": "exam_php_q1",
        "subject_id": "bcac501",
        "question_no": 1,
        "title": "Explain the architecture and execution lifecycle of PHP server-side scripting.",
        "intro": {
            "definition": "PHP (Hypertext Preprocessor) is an open-source, interpreted server-side scripting language designed primarily for dynamic web application development.",
            "background": "Introduced by Rasmus Lerdorf in 1994, PHP evolved into a high-performance engine through the Zend Engine architecture, transitioning from direct interpretation to modern opcode caching.",
            "significance": "Underpins over 75% of content management systems globally, providing seamless database integration, cross-platform portability, and rapid web request dispatching."
        },
        "diagram": {
            "svg": "<svg viewBox='0 0 700 140' xmlns='http://www.w3.org/2000/svg' style='width:100%;height:auto;background:#fff;border-radius:6px;border:1px solid #E5E9F1;'><rect x='20' y='30' width='130' height='80' rx='6' fill='#F7F8FC' stroke='#377FE6'/><text x='85' y='65' font-family='sans-serif' font-size='11' font-weight='700' fill='#377FE6' text-anchor='middle'>Client Browser</text><text x='85' y='85' font-family='monospace' font-size='9' fill='#617087' text-anchor='middle'>HTTP Request</text><path d='M 155 70 L 225 70' stroke='#377FE6' stroke-width='2'/><rect x='230' y='30' width='130' height='80' rx='6' fill='#F7F8FC' stroke='#786CE5'/><text x='295' y='65' font-family='sans-serif' font-size='11' font-weight='700' fill='#786CE5' text-anchor='middle'>Web Server</text><text x='295' y='85' font-family='monospace' font-size='9' fill='#617087' text-anchor='middle'>Apache / Nginx</text><path d='M 365 70 L 435 70' stroke='#786CE5' stroke-width='2'/><rect x='440' y='30' width='130' height='80' rx='6' fill='#F7F8FC' stroke='#28A994'/><text x='505' y='65' font-family='sans-serif' font-size='11' font-weight='700' fill='#28A994' text-anchor='middle'>Zend Engine</text><text x='505' y='85' font-family='monospace' font-size='9' fill='#1B6F61' text-anchor='middle'>Opcode Execution</text><path d='M 575 70 L 645 70' stroke='#28A994' stroke-width='2'/><rect x='650' y='30' width='30' height='80' rx='4' fill='#E9E8F8' stroke='#F2C75C'/></svg>",
            "explanation": "Illustrates the request-response cycle from client HTTP initiation through Apache/Nginx web server routing, FastCGI delegation, and Zend Engine compilation into opcode.",
            "caption": "Figure E1.1: PHP Zend Engine Request Processing Lifecycle"
        },
        "points": [
            {
                "point_no": 1,
                "heading": "HTTP Request Dispatching and SAPI Layer",
                "explanation": "Incoming HTTP requests pass through the Server API (SAPI) abstraction layer connecting web servers (Apache mod_php or PHP-FPM) to the underlying scripting engine.",
                "terminology": "SAPI (Server API), FastCGI Process Manager (PHP-FPM), mod_php.",
                "example": "Nginx passes requests via fastcgi_pass 127.0.0.1:9000 to the PHP-FPM worker pool."
            },
            {
                "point_no": 2,
                "heading": "Lexical Analysis and AST Compilation",
                "explanation": "Zend Compiler scans source tokens, performs syntactic analysis, and constructs an Abstract Syntax Tree (AST) representing program semantics.",
                "terminology": "Lexer, Tokenizer, Abstract Syntax Tree (AST), Zend Compiler.",
                "example": "Source token T_VARIABLE ($name) is transformed into an AST node for variable lookup."
            },
            {
                "point_no": 3,
                "heading": "Bytecode (Opcode) Generation and OPcache",
                "explanation": "The AST compiles into intermediate Zend Virtual Machine instructions termed opcodes. OPcache stores compiled opcodes in shared memory to bypass repetitive parsing on subsequent requests.",
                "terminology": "Opcodes, OPcache, Shared Memory Allocation, ZEND_EVAL.",
                "example": "OPcache reduces CPU execution cycles by reusing compiled opcodes cached in RAM."
            },
            {
                "point_no": 4,
                "heading": "Zend Virtual Machine Execution",
                "explanation": "Zend Virtual Machine (Zend VM) executes the opcode sequence within an isolated runtime request environment, allocating memory pools that are cleared upon request termination.",
                "terminology": "Zend VM, Memory Manager (Zend MM), Request Scope.",
                "example": "All global variables, resource handles, and arrays allocated during execution are freed after flush."
            },
            {
                "point_no": 5,
                "heading": "HTTP Response Assembly and Buffer Output",
                "explanation": "Generated HTML and HTTP response headers are assembled in output buffers and dispatched back to the web server for final client transmission.",
                "terminology": "Output Buffering (ob_start), HTTP Headers, Content-Type, HTTP Status.",
                "example": "header('Content-Type: application/json') transmits payload metadata prior to flushing output."
            }
        ],
        "conclusion": "The Zend Engine provides an isolated, share-nothing runtime model ensuring that PHP requests execute independently with minimal memory leaks and high request throughput."
    },
    {
        "id": "exam_php_q2",
        "subject_id": "bcac501",
        "question_no": 2,
        "title": "Discuss PHP Superglobals and their role in HTTP state and environment management.",
        "intro": {
            "definition": "Superglobals are built-in auto-global associative arrays in PHP available across all scopes without requiring global declarations.",
            "background": "Introduced in PHP 4.1.0 to replace unsafe register_globals which posed severe remote parameter tampering and security risks.",
            "significance": "Forms the standard interface through which PHP scripts capture client input, inspect server headers, preserve session state, and manipulate cookies."
        },
        "diagram": {
            "svg": "<svg viewBox='0 0 700 140' xmlns='http://www.w3.org/2000/svg' style='width:100%;height:auto;background:#fff;border-radius:6px;border:1px solid #E5E9F1;'><rect x='30' y='30' width='120' height='80' rx='6' fill='#F7F8FC' stroke='#377FE6'/><text x='90' y='65' font-family='sans-serif' font-size='11' font-weight='700' fill='#377FE6' text-anchor='middle'>$_GET / $_POST</text><text x='90' y='85' font-family='sans-serif' font-size='9' fill='#617087' text-anchor='middle'>Client Input</text><rect x='180' y='30' width='120' height='80' rx='6' fill='#F7F8FC' stroke='#786CE5'/><text x='240' y='65' font-family='sans-serif' font-size='11' font-weight='700' fill='#786CE5' text-anchor='middle'>$_SESSION</text><text x='240' y='85' font-family='sans-serif' font-size='9' fill='#617087' text-anchor='middle'>Persistent State</text><rect x='330' y='30' width='120' height='80' rx='6' fill='#F7F8FC' stroke='#28A994'/><text x='390' y='65' font-family='sans-serif' font-size='11' font-weight='700' fill='#28A994' text-anchor='middle'>$_COOKIE</text><text x='390' y='85' font-family='sans-serif' font-size='9' fill='#617087' text-anchor='middle'>Client Storage</text><rect x='480' y='30' width='120' height='80' rx='6' fill='#F7F8FC' stroke='#EF846B'/><text x='540' y='65' font-family='sans-serif' font-size='11' font-weight='700' fill='#EF846B' text-anchor='middle'>$_SERVER</text><text x='540' y='85' font-family='sans-serif' font-size='9' fill='#617087' text-anchor='middle'>Header &amp; Env</text></svg>",
            "explanation": "Illustrates the major categories of PHP Superglobals segregating external user input, persistent session storage, and server runtime headers.",
            "caption": "Figure E2.1: Functional Classification of PHP Superglobal Arrays"
        },
        "points": [
            {
                "point_no": 1,
                "heading": "Request Input Extraction ($_GET and $_POST)",
                "explanation": "$_GET extracts URL query string parameters, while $_POST extracts form payloads transmitted via HTTP request body.",
                "terminology": "URL Encoded Parameters, Request Body, Idempotency, Payload.",
                "example": "$id = filter_input(INPUT_GET, 'id', FILTER_VALIDATE_INT);"
            },
            {
                "point_no": 2,
                "heading": "Session State Persistence ($_SESSION)",
                "explanation": "Enables stateful communication over stateless HTTP by associating a unique session ID (PHPSESSID) with server-side serialized session files.",
                "terminology": "Session Serialization, PHPSESSID, session_start(), State Management.",
                "example": "$_SESSION['user_id'] = $auth_user->id;"
            },
            {
                "point_no": 3,
                "heading": "Client State Management ($_COOKIE)",
                "explanation": "Stores small tokens on client browsers set via setcookie() and automatically transmitted back on subsequent requests.",
                "terminology": "HTTP Cookies, HttpOnly, Secure Flag, SameSite Attribute.",
                "example": "setcookie('remember_token', $token, ['httponly' => true, 'secure' => true]);"
            },
            {
                "point_no": 4,
                "heading": "Server and Environment Inspection ($_SERVER & $_ENV)",
                "explanation": "Provides access to HTTP headers, client IP addresses, script paths, request methods, and server host configurations.",
                "terminology": "REMOTE_ADDR, REQUEST_METHOD, HTTP_USER_AGENT, SERVER_PORT.",
                "example": "if ($_SERVER['REQUEST_METHOD'] === 'POST') { process_order(); }"
            },
            {
                "point_no": 5,
                "heading": "Multipart File Upload Processing ($_FILES)",
                "explanation": "Contains metadata and temporary server storage locations for files uploaded via multipart/form-data forms.",
                "terminology": "tmp_name, mime_content_type, move_uploaded_file, UPLOAD_ERR_OK.",
                "example": "move_uploaded_file($_FILES['avatar']['tmp_name'], '/storage/avatars/' . $safe_name);"
            }
        ],
        "conclusion": "PHP Superglobals provide an intuitive abstraction for HTTP protocol handling, requiring strict input sanitization to prevent injection vulnerabilities."
    },
    {
        "id": "exam_php_q3",
        "subject_id": "bcac501",
        "question_no": 3,
        "title": "Compare PDO (PHP Data Objects) with MySQLi for enterprise database access.",
        "intro": {
            "definition": "Database abstraction interfaces in PHP facilitate secure, object-oriented, and performant interaction with relational database management systems.",
            "background": "MySQLi was developed exclusively for MySQL databases, whereas PDO was engineered in PHP 5.1 as a universal database abstraction layer supporting 12+ database drivers.",
            "significance": "Crucial for writing maintainable enterprise applications that adhere to secure database access patterns and multi-database compatibility."
        },
        "diagram": {
            "svg": "<svg viewBox='0 0 700 140' xmlns='http://www.w3.org/2000/svg' style='width:100%;height:auto;background:#fff;border-radius:6px;border:1px solid #E5E9F1;'><rect x='30' y='30' width='280' height='80' rx='6' fill='#F7F8FC' stroke='#377FE6'/><text x='170' y='60' font-family='sans-serif' font-size='12' font-weight='700' fill='#377FE6' text-anchor='middle'>PDO (Universal)</text><text x='170' y='80' font-family='sans-serif' font-size='10' fill='#19283D' text-anchor='middle'>Supports MySQL, PostgreSQL, SQLite, Oracle</text><text x='170' y='95' font-family='sans-serif' font-size='9' fill='#369B72' text-anchor='middle'>Named Parameters &amp; Exception Mode</text><rect x='390' y='30' width='280' height='80' rx='6' fill='#F7F8FC' stroke='#786CE5'/><text x='530' y='60' font-family='sans-serif' font-size='12' font-weight='700' fill='#786CE5' text-anchor='middle'>MySQLi (MySQL Exclusive)</text><text x='530' y='80' font-family='sans-serif' font-size='10' fill='#19283D' text-anchor='middle'>MySQL Server 4.1.3+ Only</text><text x='530' y='95' font-family='sans-serif' font-size='9' fill='#617087' text-anchor='middle'>Positional (?) Parameters Only</text></svg>",
            "explanation": "Contrasts PDO's multi-driver portability with MySQLi's single-engine specialization.",
            "caption": "Figure E3.1: Architecture Comparison: PDO vs MySQLi"
        },
        "points": [
            {
                "point_no": 1,
                "heading": "Database Driver Portability",
                "explanation": "PDO supports 12 distinct database drivers (MySQL, PostgreSQL, Oracle, SQLite, MSSQL), whereas MySQLi connects strictly to MySQL servers.",
                "terminology": "Data Source Name (DSN), Database Driver Abstraction, Portability.",
                "example": "new PDO('pgsql:host=localhost;dbname=portal', 'user', 'pass'); switches engines without rewriting API calls."
            },
            {
                "point_no": 2,
                "heading": "Named Parameter Binding Support",
                "explanation": "PDO allows readable named parameter placeholders (:email, :id), whereas MySQLi only permits positional question mark placeholders (?).",
                "terminology": "Named Parameters, Positional Placeholders, bindParam, bindValue.",
                "example": "$stmt = $pdo->prepare('SELECT * FROM users WHERE email = :email');"
            },
            {
                "point_no": 3,
                "heading": "Error Handling and Exception Modes",
                "explanation": "PDO natively supports PDO::ERRMODE_EXCEPTION, throwing catchable PDOExceptions, whereas classic MySQLi required manual error flag checking.",
                "terminology": "PDOException, ERRMODE_EXCEPTION, try-catch, Error Suppression.",
                "example": "$pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);"
            },
            {
                "point_no": 4,
                "heading": "Programming Paradigms Supported",
                "explanation": "MySQLi supports both procedural (mysqli_connect) and object-oriented paradigms, while PDO enforces strict object-oriented design patterns.",
                "terminology": "Object-Oriented Programming, Procedural Wrapper, API Uniformity.",
                "example": "$mysqli->query() vs mysqli_query($conn) shows MySQLi's dual nature."
            },
            {
                "point_no": 5,
                "heading": "Object Mapping and Fetch Modes",
                "explanation": "PDO provides sophisticated fetch modes (PDO::FETCH_CLASS, PDO::FETCH_ASSOC) allowing direct mapping of result sets into domain model objects.",
                "terminology": "FETCH_CLASS, Domain Entity Hydration, Result Set Mapping.",
                "example": "$stmt->fetchAll(PDO::FETCH_CLASS, 'UserEntity'); instantiates UserEntity models directly."
            }
        ],
        "conclusion": "While MySQLi provides minor performance advantages in MySQL-only environments, PDO is the modern enterprise standard due to named binding, driver flexibility, and clean exception handling."
    },
    {
        "id": "exam_php_q4",
        "subject_id": "bcac501",
        "question_no": 4,
        "title": "Explain SQL Injection vulnerabilities and demonstrate prevention using Prepared Statements.",
        "intro": {
            "definition": "SQL Injection (SQLi) is a critical security vulnerability where untrusted client input dynamically alters the syntax and logic of database queries executed by the backend engine.",
            "background": "Consistently ranked in the OWASP Top 10 vulnerabilities, stemming from vulnerable string concatenation in dynamic SQL statements.",
            "significance": "A single SQLi breach can lead to complete database theft, authentication bypass, data destruction, and server compromise."
        },
        "diagram": {
            "svg": "<svg viewBox='0 0 700 140' xmlns='http://www.w3.org/2000/svg' style='width:100%;height:auto;background:#fff;border-radius:6px;border:1px solid #E5E9F1;'><rect x='30' y='30' width='180' height='80' rx='6' fill='#F7F8FC' stroke='#377FE6'/><text x='120' y='60' font-family='sans-serif' font-size='11' font-weight='700' fill='#377FE6' text-anchor='middle'>1. SQL Template Sent</text><text x='120' y='80' font-family='monospace' font-size='9' fill='#19283D' text-anchor='middle'>SELECT * WHERE id = ?</text><text x='120' y='95' font-family='sans-serif' font-size='8' fill='#617087' text-anchor='middle'>Database parses &amp; compiles AST</text><path d='M 215 70 L 285 70' stroke='#377FE6' stroke-width='2'/><rect x='290' y='30' width='180' height='80' rx='6' fill='#F7F8FC' stroke='#786CE5'/><text x='380' y='60' font-family='sans-serif' font-size='11' font-weight='700' fill='#786CE5' text-anchor='middle'>2. Parameter Sent Separately</text><text x='380' y='80' font-family='monospace' font-size='9' fill='#D65F64' text-anchor='middle'>Input: ' OR 1=1 --</text><text x='380' y='95' font-family='sans-serif' font-size='8' fill='#617087' text-anchor='middle'>Treated strictly as literal data</text><path d='M 475 70 L 545 70' stroke='#28A994' stroke-width='2'/><rect x='550' y='30' width='120' height='80' rx='6' fill='#E9E8F8' stroke='#28A994'/><text x='610' y='65' font-family='sans-serif' font-size='11' font-weight='700' fill='#1B6F61' text-anchor='middle'>Safe Execution</text><text x='610' y='85' font-family='sans-serif' font-size='9' fill='#369B72' text-anchor='middle'>0 Injection Risk</text></svg>",
            "explanation": "Prepared statements decouple SQL query compilation from user data transmission, guaranteeing literal string treatment.",
            "caption": "Figure E4.1: Two-Phase Prepared Statement Execution Architecture"
        },
        "points": [
            {
                "point_no": 1,
                "heading": "Mechanics of the SQL Injection Attack",
                "explanation": "Attackers inject SQL operators (' OR 1=1 --) into unescaped input fields, terminating query strings and appending arbitrary database commands.",
                "terminology": "Tautology Attack, String Concatenation, SQL Query Parsing, AST Manipulation.",
                "example": "$sql = \"SELECT * FROM users WHERE user = '$u' AND pass = '$p'\"; input `' OR 1=1 --` bypasses login."
            },
            {
                "point_no": 2,
                "heading": "Two-Phase Separation in Prepared Statements",
                "explanation": "Prepared statements compile the query structure on the database engine first before parameters are transmitted, ensuring user data can never be evaluated as SQL code.",
                "terminology": "Prepare Phase, Execute Phase, Query Plan Precompilation, Parameter Binding.",
                "example": "$stmt = $pdo->prepare('SELECT * FROM users WHERE email = ?'); $stmt->execute([$input]);"
            },
            {
                "point_no": 3,
                "heading": "Type-Safe Parameter Binding with PDO",
                "explanation": "Parameters are explicitly bound to defined data types (PARAM_INT, PARAM_STR), enforcing runtime structural integrity.",
                "terminology": "PDO::PARAM_INT, PDO::PARAM_STR, bindValue, Data Sanitization.",
                "example": "$stmt->bindValue(':id', $id, PDO::PARAM_INT);"
            },
            {
                "point_no": 4,
                "heading": "Mitigating Second-Order SQL Injections",
                "explanation": "Second-order SQLi occurs when poisoned data stored safely in the database is re-executed dynamically elsewhere; persistent parameter binding across all modules neutralizes this threat.",
                "terminology": "Second-Order Injection, Stored Payload, Re-execution Vulnerability.",
                "example": "Always use prepared statements when reading database records to feed downstream queries."
            },
            {
                "point_no": 5,
                "heading": "Defense-in-Depth: Principle of Least Privilege",
                "explanation": "Database user accounts configured for PHP applications must hold only necessary permissions (SELECT, INSERT, UPDATE), disallowing administrative commands (DROP, GRANT).",
                "terminology": "Principle of Least Privilege (PoLP), RBAC, Grant Revocation.",
                "example": "Revoke FILE, SUPER, and DROP privileges from the standard web application DB user."
            }
        ],
        "conclusion": "Prepared statements completely eliminate SQL injection by separating code from data during query execution, serving as the non-negotiable standard for web persistence layers."
    },
    {
        "id": "exam_php_q5",
        "subject_id": "bcac501",
        "question_no": 5,
        "title": "Analyze Session Fixation and Session Hijacking threats, detailing countermeasure implementations in PHP.",
        "intro": {
            "definition": "Session management is the mechanism of preserving user identity and authenticated state across stateless HTTP requests using server-side session tokens.",
            "background": "HTTP is inherently stateless. Web applications employ session identifiers (PHPSESSID) passed via cookies to identify client request contexts.",
            "significance": "Flaws in session handling allow unauthorized attackers to impersonate legitimate authenticated users without needing their primary credentials."
        },
        "diagram": {
            "svg": "<svg viewBox='0 0 700 140' xmlns='http://www.w3.org/2000/svg' style='width:100%;height:auto;background:#fff;border-radius:6px;border:1px solid #E5E9F1;'><rect x='30' y='30' width='180' height='80' rx='6' fill='#FFF2EB' stroke='#EF846B'/><text x='120' y='60' font-family='sans-serif' font-size='11' font-weight='700' fill='#EF846B' text-anchor='middle'>Pre-Login State</text><text x='120' y='80' font-family='monospace' font-size='9' fill='#19283D' text-anchor='middle'>Token: ABC123XYZ</text><path d='M 215 70 L 295 70' stroke='#377FE6' stroke-width='2'/><text x='255' y='60' font-family='sans-serif' font-size='8' fill='#377FE6' text-anchor='middle'>Login Auth</text><rect x='300' y='30' width='220' height='80' rx='6' fill='#F7F8FC' stroke='#377FE6'/><text x='410' y='55' font-family='sans-serif' font-size='10' font-weight='700' fill='#377FE6' text-anchor='middle'>session_regenerate_id(true)</text><text x='410' y='75' font-family='monospace' font-size='9' fill='#28A994' text-anchor='middle'>New Token: 987FED456</text><text x='410' y='95' font-family='sans-serif' font-size='8' fill='#617087' text-anchor='middle'>Old pre-login token destroyed</text><path d='M 525 70 L 595 70' stroke='#28A994' stroke-width='2'/><rect x='600' y='30' width='75' height='80' rx='6' fill='#E9E8F8' stroke='#28A994'/><text x='637' y='75' font-family='sans-serif' font-size='10' font-weight='700' fill='#1B6F61' text-anchor='middle'>Secured</text></svg>",
            "explanation": "Illustrates session ID regeneration upon successful user privilege elevation, neutralizing session fixation attacks.",
            "caption": "Figure E5.1: Session Token Regeneration Workflow on User Login"
        },
        "points": [
            {
                "point_no": 1,
                "heading": "Threat Mechanics: Session Fixation vs Hijacking",
                "explanation": "In fixation, an attacker tricks a victim into authenticating with a known session ID. In hijacking, the attacker steals an active session cookie over an unencrypted channel or via XSS.",
                "terminology": "Session Fixation, Session Hijacking, Man-in-the-Middle (MITM), Cross-Site Scripting (XSS).",
                "example": "Attacker supplies link `login.php?PHPSESSID=evil123` to fix the victim's session."
            },
            {
                "point_no": 2,
                "heading": "Session Regeneration Defense (session_regenerate_id)",
                "explanation": "Invoking session_regenerate_id(true) immediately upon user login discards the old session ID and generates a cryptographically random new identifier.",
                "terminology": "session_regenerate_id, Token Rotation, Privilege Escalation Boundary.",
                "example": "if (password_verify($pwd, $hash)) { session_regenerate_id(true); $_SESSION['auth'] = true; }"
            },
            {
                "point_no": 3,
                "heading": "Hardening Session Cookies (HttpOnly, Secure, SameSite)",
                "explanation": "Setting session cookie flags prevents client-side JavaScript access and enforces strict HTTPS transport.",
                "terminology": "session_set_cookie_params, HttpOnly Flag, Secure Flag, SameSite=Strict.",
                "example": "session_set_cookie_params(['lifetime' => 0, 'secure' => true, 'httponly' => true, 'samesite' => 'Strict']);"
            },
            {
                "point_no": 4,
                "heading": "Session Inactivity and Absolute Timeouts",
                "explanation": "Enforce both idle timeouts (expiring after 15 minutes of inactivity) and absolute maximum session lifespans (expiring after 8 hours regardless of activity).",
                "terminology": "Idle Timeout, Absolute Expiration, Inactivity Invalidation.",
                "example": "if (time() - $_SESSION['last_activity'] > 900) { session_destroy(); header('Location: /login'); }"
            },
            {
                "point_no": 5,
                "heading": "Client Fingerprint and User-Agent Validation",
                "explanation": "Hashing client User-Agent and subnet IP address into the session allows instantaneous invalidation if the request signature changes abruptly.",
                "terminology": "Client Fingerprinting, User-Agent Hash, Session Tampering Detection.",
                "example": "if ($_SESSION['user_agent'] !== hash('sha256', $_SERVER['HTTP_USER_AGENT'])) { session_destroy(); }"
            }
        ],
        "conclusion": "Robust session security requires proactive token regeneration upon authentication, hardened cookie directives (HttpOnly, Secure, SameSite), and strict idle timeouts."
    },
    {
        "id": "exam_php_q6",
        "subject_id": "bcac501",
        "question_no": 6,
        "title": "Explain secure file upload validation techniques in PHP to prevent Remote Code Execution (RCE).",
        "intro": {
            "definition": "File upload validation is the multi-layered verification process ensuring uploaded files conform to safe file types, sizes, and binary headers without executing server-side scripts.",
            "background": "Allowing arbitrary file uploads is a leading attack vector enabling hackers to upload PHP webshells (.php, .phtml) resulting in full server takeover.",
            "significance": "Essential for enterprise document management, user profile avatar uploads, and media storage portals."
        },
        "diagram": {
            "svg": "<svg viewBox='0 0 700 140' xmlns='http://www.w3.org/2000/svg' style='width:100%;height:auto;background:#fff;border-radius:6px;border:1px solid #E5E9F1;'><rect x='20' y='30' width='120' height='80' rx='6' fill='#F7F8FC' stroke='#377FE6'/><text x='80' y='60' font-family='sans-serif' font-size='10' font-weight='700' fill='#377FE6' text-anchor='middle'>1. Error Check</text><text x='80' y='80' font-family='monospace' font-size='9' fill='#19283D' text-anchor='middle'>UPLOAD_ERR_OK</text><path d='M 145 70 L 175 70' stroke='#377FE6' stroke-width='2'/><rect x='180' y='30' width='130' height='80' rx='6' fill='#F7F8FC' stroke='#786CE5'/><text x='245' y='60' font-family='sans-serif' font-size='10' font-weight='700' fill='#786CE5' text-anchor='middle'>2. Size &amp; Whitelist</text><text x='245' y='80' font-family='monospace' font-size='9' fill='#19283D' text-anchor='middle'>[jpg, png, pdf]</text><path d='M 315 70 L 345 70' stroke='#786CE5' stroke-width='2'/><rect x='350' y='30' width='150' height='80' rx='6' fill='#F7F8FC' stroke='#28A994'/><text x='425' y='60' font-family='sans-serif' font-size='10' font-weight='700' fill='#28A994' text-anchor='middle'>3. Magic Bytes (finfo)</text><text x='425' y='80' font-family='monospace' font-size='9' fill='#19283D' text-anchor='middle'>image/jpeg (binary)</text><path d='M 505 70 L 535 70' stroke='#28A994' stroke-width='2'/><rect x='540' y='30' width='140' height='80' rx='6' fill='#E9E8F8' stroke='#F2C75C'/><text x='610' y='60' font-family='sans-serif' font-size='10' font-weight='700' fill='#19283D' text-anchor='middle'>4. Rename &amp; Move</text><text x='610' y='80' font-family='monospace' font-size='9' fill='#369B72' text-anchor='middle'>Outside docroot</text></svg>",
            "explanation": "Illustrates the 4-tier validation pipeline: error checking, extension whitelisting, magic byte MIME inspection, and secure out-of-root relocation.",
            "caption": "Figure E6.1: Multi-Tier Secure File Upload Verification Pipeline"
        },
        "points": [
            {
                "point_no": 1,
                "heading": "PHP Upload Error Status Verification",
                "explanation": "Validate $_FILES['upload']['error'] === UPLOAD_ERR_OK before initiating any file operations to handle partial or truncated transmissions.",
                "terminology": "UPLOAD_ERR_OK, UPLOAD_ERR_INI_SIZE, Multipart Stream Validation.",
                "example": "if ($_FILES['file']['error'] !== UPLOAD_ERR_OK) { throw new Exception('Upload error code: ' . $_FILES['file']['error']); }"
            },
            {
                "point_no": 2,
                "heading": "Strict File Extension Whitelisting",
                "explanation": "Check file extensions against a strict whitelist rather than a blacklist to prevent execution of alternative extensions (.php5, .phtml, .phar).",
                "terminology": "Extension Whitelist, pathinfo(), PATHINFO_EXTENSION, Blacklist Bypass.",
                "example": "$ext = strtolower(pathinfo($_FILES['doc']['name'], PATHINFO_EXTENSION)); in_array($ext, ['pdf', 'png']);"
            },
            {
                "point_no": 3,
                "heading": "Binary Header and Magic Byte Inspection (finfo)",
                "explanation": "Never trust client-supplied $_FILES['type']; verify the file's binary magic bytes using PHP's Fileinfo extension (finfo_file) on the temporary file.",
                "terminology": "Magic Bytes, finfo_open, FILEINFO_MIME_TYPE, MIME Spoofing.",
                "example": "$finfo = new finfo(FILEINFO_MIME_TYPE); $mime = $finfo->file($_FILES['avatar']['tmp_name']);"
            },
            {
                "point_no": 4,
                "heading": "Cryptographic Filename Obfuscation",
                "explanation": "Discard the original client filename to prevent directory traversal attacks (../); generate a random UUID or SHA-256 filename.",
                "terminology": "Directory Traversal, bin2hex(random_bytes(16)), UUID Sanitization.",
                "example": "$safe_name = bin2hex(random_bytes(16)) . '.' . $ext;"
            },
            {
                "point_no": 5,
                "heading": "Storage Outside Document Root and Execution Disabling",
                "explanation": "Store uploaded binaries outside the public web root directory (/var/www/html/public) and configure server rules to deny script execution.",
                "terminology": "Document Root Isolation, readfile() Proxying, .htaccess Disallow Script.",
                "example": "In Apache: `php_flag engine off` inside the upload directory disallows PHP execution."
            }
        ],
        "conclusion": "Secure file uploads mandate server-side magic byte verification (finfo), randomized filename hashing, and isolated out-of-root storage."
    },
    {
        "id": "exam_php_q7",
        "subject_id": "bcac501",
        "question_no": 7,
        "title": "Explain Object-Oriented Programming (OOP) in PHP, including Inheritance, Interfaces, and Traits.",
        "intro": {
            "definition": "Object-Oriented Programming (OOP) in PHP is a programming paradigm organizing software design around discrete data classes and object instances encapsulating state and behavior.",
            "background": "PHP 5 completely overhauled object handling by passing objects by handle rather than value, with PHP 7 and 8 adding strict typing, union types, and constructor property promotion.",
            "significance": "Underpins modern PHP frameworks (Laravel, Symfony) enabling modular software architecture, dependency injection, and clean code maintainability."
        },
        "diagram": {
            "svg": "<svg viewBox='0 0 700 140' xmlns='http://www.w3.org/2000/svg' style='width:100%;height:auto;background:#fff;border-radius:6px;border:1px solid #E5E9F1;'><rect x='30' y='30' width='160' height='80' rx='6' fill='#F7F8FC' stroke='#377FE6'/><text x='110' y='60' font-family='sans-serif' font-size='11' font-weight='700' fill='#377FE6' text-anchor='middle'>Superclass</text><text x='110' y='80' font-family='monospace' font-size='9' fill='#19283D' text-anchor='middle'>Model (Single Inh.)</text><path d='M 195 70 L 265 70' stroke='#377FE6' stroke-width='2'/><rect x='270' y='30' width='160' height='80' rx='6' fill='#F7F8FC' stroke='#786CE5'/><text x='350' y='60' font-family='sans-serif' font-size='11' font-weight='700' fill='#786CE5' text-anchor='middle'>Subclass</text><text x='350' y='80' font-family='monospace' font-size='9' fill='#19283D' text-anchor='middle'>User extends Model</text><path d='M 435 70 L 505 70' stroke='#28A994' stroke-width='2'/><rect x='510' y='30' width='160' height='80' rx='6' fill='#F7F8FC' stroke='#28A994'/><text x='590' y='60' font-family='sans-serif' font-size='11' font-weight='700' fill='#28A994' text-anchor='middle'>Traits &amp; Interfaces</text><text x='590' y='80' font-family='monospace' font-size='9' fill='#1B6F61' text-anchor='middle'>use HasApiTokens</text></svg>",
            "explanation": "Illustrates PHP's single class inheritance model supplemented by horizontal code reuse via Traits and multiple contract compliance via Interfaces.",
            "caption": "Figure E7.1: Class Inheritance Combined with Traits in Modern PHP"
        },
        "points": [
            {
                "point_no": 1,
                "heading": "Single Inheritance and Method Overriding",
                "explanation": "PHP supports single class inheritance using the extends keyword, allowing child classes to inherit public and protected methods from a parent class.",
                "terminology": "Single Inheritance, extends, parent::, Method Overriding.",
                "example": "class AdminUser extends User { public function getRole(): string { return 'ADMIN'; } }"
            },
            {
                "point_no": 2,
                "heading": "Interface Contracts for Multiple Compliance",
                "explanation": "Interfaces specify method signatures that implementing classes must satisfy using the implements keyword, enabling polymorphic substitution.",
                "terminology": "interface, implements, Polymorphism, Contract Enforcement.",
                "example": "class StripeGateway implements PaymentGatewayInterface { public function charge(float $amt): bool { ... } }"
            },
            {
                "point_no": 3,
                "heading": "Horizontal Code Reuse via Traits",
                "explanation": "Traits enable developers to reuse method implementations horizontally across independent classes without requiring vertical inheritance.",
                "terminology": "trait, use Keyword, Horizontal Reuse, Conflict Resolution (insteadof).",
                "example": "trait Loggable { public function log($m) { echo $m; } } class Order { use Loggable; }"
            },
            {
                "point_no": 4,
                "heading": "Encapsulation and Visibility Modifiers",
                "explanation": "Visibility keywords (public, protected, private) restrict variable and method access, guarding internal state against unauthorized external corruption.",
                "terminology": "Encapsulation, public, protected, private, Getters and Setters.",
                "example": "private string $passwordHash prevents external direct field manipulation."
            },
            {
                "point_no": 5,
                "heading": "PHP 8 Constructor Property Promotion",
                "explanation": "Streamlines class definitions by declaring visibility modifiers directly inside constructor parameters, automatically mapping them to class properties.",
                "terminology": "Constructor Property Promotion, Boilerplate Reduction, Typed Properties.",
                "example": "public function __construct(public string $name, private float $price) {}"
            }
        ],
        "conclusion": "PHP's modern OOP model merges clean single inheritance with horizontal Trait reuse and strict typing, powering modular enterprise application architectures."
    },
    {
        "id": "exam_php_q8",
        "subject_id": "bcac501",
        "question_no": 8,
        "title": "Explain Exception Handling in modern PHP, custom exceptions, and the Throwable hierarchy.",
        "intro": {
            "definition": "Exception handling in PHP is an object-oriented mechanism for intercepting runtime anomalies and maintaining controlled program execution flow using try-catch-finally blocks.",
            "background": "PHP 7 introduced the Throwable interface, unifying engine fatal errors (TypeError, ParseError) with userland Exceptions into a single catchable hierarchy.",
            "significance": "Prevents catastrophic application crashes, provides meaningful error logs, and facilitates graceful error recovery in production web systems."
        },
        "diagram": {
            "svg": "<svg viewBox='0 0 700 140' xmlns='http://www.w3.org/2000/svg' style='width:100%;height:auto;background:#fff;border-radius:6px;border:1px solid #E5E9F1;'><rect x='280' y='20' width='140' height='35' rx='6' fill='#F7F8FC' stroke='#377FE6'/><text x='350' y='42' font-family='sans-serif' font-size='11' font-weight='700' fill='#377FE6' text-anchor='middle'>Throwable Interface</text><path d='M 310 55 L 200 75' stroke='#D65F64' stroke-width='2'/><path d='M 390 55 L 500 75' stroke='#28A994' stroke-width='2'/><rect x='120' y='75' width='160' height='35' rx='6' fill='#FFF2EB' stroke='#D65F64'/><text x='200' y='97' font-family='sans-serif' font-size='10' font-weight='700' fill='#D65F64' text-anchor='middle'>Error (Engine Faults)</text><rect x='420' y='75' width='160' height='35' rx='6' fill='#F7F8FC' stroke='#28A994'/><text x='500' y='97' font-family='sans-serif' font-size='10' font-weight='700' fill='#28A994' text-anchor='middle'>Exception (Application)</text></svg>",
            "explanation": "Illustrates PHP's unified Throwable hierarchy branching into engine Error faults and recoverable Exception classes.",
            "caption": "Figure E8.1: PHP 7+ Unified Throwable Inheritance Tree"
        },
        "points": [
            {
                "point_no": 1,
                "heading": "Throwable Interface Unification",
                "explanation": "The Throwable interface is the base interface for all objects thrown via throw statements. Both Exception and Error implement Throwable.",
                "terminology": "Throwable, Error, Exception, TypeError, ArithmeticError.",
                "example": "try { ... } catch (Throwable $e) catches both PHP engine errors and application exceptions."
            },
            {
                "point_no": 2,
                "heading": "Structured try-catch-finally Flow",
                "explanation": "The try block encapsulates risky operations, catch handles specific exception instances, and finally executes unconditionally for cleanup.",
                "terminology": "try, catch, finally, Stack Trace, Resource Deallocation.",
                "example": "try { $db->commit(); } catch (PDOException $e) { $db->rollBack(); } finally { $db->close(); }"
            },
            {
                "point_no": 3,
                "heading": "Custom Domain Exception Creation",
                "explanation": "Subclassing Exception allows applications to define semantic domain error types carrying specific HTTP status codes and diagnostic data.",
                "terminology": "Custom Exception, Domain Exception, Exception Chaining.",
                "example": "class InsufficientBalanceException extends Exception { public function __construct($m, $code=422) { super($m, $code); } }"
            },
            {
                "point_no": 4,
                "heading": "Multiple Catch Blocks and Union Catch Types",
                "explanation": "PHP allows multiple catch blocks arranged from specific to general, as well as union catch syntax (TypeA | TypeB $e) to reduce code redundancy.",
                "terminology": "Union Catch, Exception Hierarchies, Type Narrowing.",
                "example": "catch (InvalidArgumentException | ValidationException $e) { handle_client_error($e); }"
            },
            {
                "point_no": 5,
                "heading": "Global Uncaught Exception Handlers",
                "explanation": "Registering set_exception_handler() configures a centralized fallback handler that logs unhandled exceptions and returns a generic 500 error page.",
                "terminology": "set_exception_handler, Error Logging, 500 Internal Server Error.",
                "example": "set_exception_handler(function(Throwable $e) { error_log($e); render_500_view(); });"
            }
        ],
        "conclusion": "Unified Throwable handling and custom exception hierarchies enable resilient PHP web applications capable of recovering gracefully from faults."
    },
    {
        "id": "exam_php_q9",
        "subject_id": "bcac501",
        "question_no": 9,
        "title": "Explain the Model-View-Controller (MVC) architectural pattern in PHP frameworks like Laravel.",
        "intro": {
            "definition": "Model-View-Controller (MVC) is an architectural design pattern that separates application concerns into three interconnected components: data logic (Model), user interface (View), and flow control (Controller).",
            "background": "Formulated by Trygve Reenskaug in 1979 for Smalltalk, MVC became the structural foundation for modern PHP frameworks (Laravel, Symfony, CodeIgniter).",
            "significance": "Enables modular team development, code reusability, testability, and separation of business rules from HTML presentation logic."
        },
        "diagram": {
            "svg": "<svg viewBox='0 0 700 140' xmlns='http://www.w3.org/2000/svg' style='width:100%;height:auto;background:#fff;border-radius:6px;border:1px solid #E5E9F1;'><rect x='30' y='30' width='160' height='80' rx='6' fill='#F7F8FC' stroke='#377FE6'/><text x='110' y='60' font-family='sans-serif' font-size='11' font-weight='700' fill='#377FE6' text-anchor='middle'>Controller</text><text x='110' y='80' font-family='monospace' font-size='9' fill='#19283D' text-anchor='middle'>OrderController.php</text><path d='M 195 50 L 295 50' stroke='#786CE5' stroke-width='2'/><rect x='300' y='10' width='160' height='60' rx='6' fill='#F7F8FC' stroke='#786CE5'/><text x='380' y='35' font-family='sans-serif' font-size='11' font-weight='700' fill='#786CE5' text-anchor='middle'>Model (ORM)</text><text x='380' y='52' font-family='monospace' font-size='8' fill='#19283D' text-anchor='middle'>Order.php (Database)</text><path d='M 195 90 L 295 90' stroke='#28A994' stroke-width='2'/><rect x='300' y='75' width='160' height='60' rx='6' fill='#F7F8FC' stroke='#28A994'/><text x='380' y='100' font-family='sans-serif' font-size='11' font-weight='700' fill='#28A994' text-anchor='middle'>View (Blade)</text><text x='380' y='117' font-family='monospace' font-size='8' fill='#19283D' text-anchor='middle'>order.blade.php</text><rect x='520' y='30' width='150' height='80' rx='6' fill='#E9E8F8' stroke='#F2C75C'/><text x='595' y='65' font-family='sans-serif' font-size='11' font-weight='700' fill='#19283D' text-anchor='middle'>Client Browser</text><text x='595' y='85' font-family='monospace' font-size='9' fill='#369B72' text-anchor='middle'>HTML / JSON Output</text></svg>",
            "explanation": "Illustrates the MVC routing sequence: Controller coordinates data fetching from the Model and presentation rendering via the View.",
            "caption": "Figure E9.1: Model-View-Controller Request Delegation Flow"
        },
        "points": [
            {
                "point_no": 1,
                "heading": "Routing and Front Controller Entry Point",
                "explanation": "All incoming HTTP traffic is directed through a single entry point (index.php) where the Router maps URI patterns to designated Controller actions.",
                "terminology": "Front Controller Pattern, Router, HTTP Verbs (GET/POST/PUT/DELETE).",
                "example": "Route::get('/students', [StudentController::class, 'index']);"
            },
            {
                "point_no": 2,
                "heading": "Controller Orchestration and Business Flow",
                "explanation": "The Controller processes incoming request parameters, coordinates business logic, retrieves entities from Models, and passes view models to the template engine.",
                "terminology": "Controller Action, Dependency Injection, Request Validation.",
                "example": "public function show($id) { $user = User::findOrFail($id); return view('user.profile', ['user' => $user]); }"
            },
            {
                "point_no": 3,
                "heading": "Model Layer and Object-Relational Mapping (ORM)",
                "explanation": "Models represent database tables as rich objects, encapsulating relationships (one-to-many), data access methods, and business validation rules.",
                "terminology": "Eloquent ORM, Active Record Pattern, Entity Relationships, Query Builder.",
                "example": "class Student extends Model { public function courses() { return $this->hasMany(Course::class); } }"
            },
            {
                "point_no": 4,
                "heading": "View Layer and Blade Templating Engine",
                "explanation": "Views handle presentation markup using templating engines (Blade) that support layout inheritance, automatic XSS sanitization ({{ }}), and component slots.",
                "terminology": "Blade Template Engine, Layout Inheritance (@extends, @yield), XSS Escaping.",
                "example": "@extends('layouts.app') @section('content') <h1>{{ $student->name }}</h1> @endsection"
            },
            {
                "point_no": 5,
                "heading": "Separation of Concerns and Testability Benefits",
                "explanation": "Decoupling database queries from HTML allows isolated unit testing of Models and Controllers with mock objects without spinning up a live browser.",
                "terminology": "Separation of Concerns (SoC), Unit Testing, PHPUnit, Mocking.",
                "example": "Unit tests can execute `$controller->index()` and assert JSON responses directly."
            }
        ],
        "conclusion": "The MVC architecture enforces clear separation of concerns, transforming disorganized spaghetti PHP scripts into scalable, testable enterprise applications."
    },
    {
        "id": "exam_php_q10",
        "subject_id": "bcac501",
        "question_no": 10,
        "title": "Explain RESTful API architecture, JSON serialization, and stateless authentication in PHP.",
        "intro": {
            "definition": "A RESTful API is an architectural style for building scalable distributed web services utilizing standard HTTP methods and stateless JSON data payloads.",
            "background": "Formulated by Roy Fielding in 2000, REST superseded SOAP and XML-RPC by leveraging native HTTP protocols (GET, POST, PUT, DELETE) and uniform resource identifiers.",
            "significance": "Serves as the standard communication protocol connecting modern mobile apps, Single Page Applications (React, Vue), and microservices to PHP backends."
        },
        "diagram": {
            "svg": "<svg viewBox='0 0 700 140' xmlns='http://www.w3.org/2000/svg' style='width:100%;height:auto;background:#fff;border-radius:6px;border:1px solid #E5E9F1;'><rect x='30' y='30' width='160' height='80' rx='6' fill='#F7F8FC' stroke='#377FE6'/><text x='110' y='60' font-family='sans-serif' font-size='11' font-weight='700' fill='#377FE6' text-anchor='middle'>Client (SPA / Mobile)</text><text x='110' y='80' font-family='monospace' font-size='8' fill='#19283D' text-anchor='middle'>Authorization: Bearer JWT</text><path d='M 195 70 L 295 70' stroke='#377FE6' stroke-width='2'/><text x='245' y='60' font-family='sans-serif' font-size='8' fill='#377FE6' text-anchor='middle'>JSON Payload</text><rect x='300' y='30' width='210' height='80' rx='6' fill='#F7F8FC' stroke='#786CE5'/><text x='405' y='55' font-family='sans-serif' font-size='11' font-weight='700' fill='#786CE5' text-anchor='middle'>PHP REST Controller</text><text x='405' y='75' font-family='monospace' font-size='9' fill='#19283D' text-anchor='middle'>json_decode / json_encode</text><text x='405' y='95' font-family='sans-serif' font-size='8' fill='#617087' text-anchor='middle'>JWT Signature Verification</text><path d='M 515 70 L 595 70' stroke='#28A994' stroke-width='2'/><rect x='600' y='30' width='75' height='80' rx='6' fill='#E9E8F8' stroke='#28A994'/><text x='637' y='75' font-family='sans-serif' font-size='10' font-weight='700' fill='#1B6F61' text-anchor='middle'>JSON Resp</text></svg>",
            "explanation": "Illustrates client-server stateless REST interaction via JSON payloads and Bearer Token header authentication.",
            "caption": "Figure E10.1: RESTful API Communication and Stateless Authentication Architecture"
        },
        "points": [
            {
                "point_no": 1,
                "heading": "Standard HTTP Verbs and Resource Routing",
                "explanation": "REST routes endpoints around plural nouns (/api/books), applying standard verbs: GET (read), POST (create), PUT (update), DELETE (remove).",
                "terminology": "HTTP Methods, Idempotency, Resource Endpoints, CRUD Mapping.",
                "example": "POST /api/students inserts a new record; GET /api/students/101 retrieves record 101."
            },
            {
                "point_no": 2,
                "heading": "JSON Serialization and Header Management",
                "explanation": "PHP reads raw JSON input using file_get_contents('php://input') with json_decode(), and transmits responses with header('Content-Type: application/json') and json_encode().",
                "terminology": "json_encode, json_decode, php://input, Content-Type: application/json.",
                "example": "echo json_encode(['status' => 'success', 'data' => $students], JSON_THROW_ON_ERROR);"
            },
            {
                "point_no": 3,
                "heading": "Accurate HTTP Status Code Semantics",
                "explanation": "RESTful services must return accurate HTTP response codes: 200 (OK), 201 (Created), 400 (Bad Request), 401 (Unauthorized), 404 (Not Found), 500 (Server Error).",
                "terminology": "HTTP Status Codes, http_response_code(), REST Contract Semantics.",
                "example": "http_response_code(201); sets created status following successful record insertion."
            },
            {
                "point_no": 4,
                "heading": "Stateless Token Authentication (JWT / Bearer Tokens)",
                "explanation": "Stateless services disallow server sessions, requiring clients to transmit a cryptographically signed token (JWT) inside the HTTP Authorization: Bearer header with every request.",
                "terminology": "JSON Web Token (JWT), Statelessness, Authorization Header, Signature Verification.",
                "example": "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
            },
            {
                "point_no": 5,
                "heading": "CORS (Cross-Origin Resource Sharing) Headers",
                "explanation": "Browsers restrict cross-origin API calls; PHP must return explicit CORS headers (Access-Control-Allow-Origin, Methods, Headers) to authorize cross-domain SPA interactions.",
                "terminology": "CORS, Pre-flight OPTIONS Request, Access-Control-Allow-Origin.",
                "example": "header('Access-Control-Allow-Origin: https://portal.makaut.ac.in');"
            }
        ],
        "conclusion": "RESTful PHP APIs leverage native HTTP verbs, JSON serialization, and stateless bearer authentication to deliver high-performance backends for cross-platform applications."
    }
]
