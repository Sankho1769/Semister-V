# Comprehensive Academic Quiz Bank Generator (84 Questions)

def get_quizzes_data():
    return [
    {
        "id": "quiz_php_1",
        "subject_id": "bcac501",
        "unit_no": 1,
        "difficulty": "easy",
        "type": "single_mcq",
        "question": "Which of the following functions is used in PHP to start a new session or resume an existing one?",
        "options": [
            "session_init()",
            "session_start()",
            "session_begin()",
            "start_session()"
        ],
        "correct_indices": [
            1
        ],
        "explanation": "session_start() initializes session data and reads session cookies. session_init() and session_begin() do not exist in PHP."
    },
    {
        "id": "quiz_php_2",
        "subject_id": "bcac501",
        "unit_no": 1,
        "difficulty": "easy",
        "type": "true_false",
        "question": "PHP variables are case-sensitive, but function and class names are case-insensitive.",
        "options": [
            "True",
            "False"
        ],
        "correct_indices": [
            0
        ],
        "explanation": "In PHP, variable identifiers ($var vs $Var) are strictly case-sensitive, whereas function names (myFunc vs myfunc) and built-in keywords are case-insensitive."
    },
    {
        "id": "quiz_php_3",
        "subject_id": "bcac501",
        "unit_no": 2,
        "difficulty": "medium",
        "type": "single_mcq",
        "question": "What is the difference between sort() and asort() when applied to PHP arrays?",
        "options": [
            "sort() sorts in ascending order while asort() sorts in descending order.",
            "sort() re-indexes array keys numerically starting from 0, while asort() preserves associative key-value associations.",
            "asort() is strictly for multi-dimensional arrays, whereas sort() only works on strings.",
            "sort() modifies the original array, whereas asort() returns a new array copy."
        ],
        "correct_indices": [
            1
        ],
        "explanation": "sort() resets all keys to 0..N, while asort() sorts values while preserving custom associative string and integer keys."
    },
    {
        "id": "quiz_php_4",
        "subject_id": "bcac501",
        "unit_no": 2,
        "difficulty": "medium",
        "type": "multi_mcq",
        "question": "Which of the following are valid array declaration syntaxes in modern PHP (PHP 7+ / 8+)? (Select all that apply)",
        "options": [
            "$arr = array('a', 'b', 'c');",
            "$arr = ['a', 'b', 'c'];",
            "$arr = new Array('a', 'b', 'c');",
            "$arr = ['key' => 'value'];"
        ],
        "correct_indices": [
            0,
            1,
            3
        ],
        "explanation": "array() and short bracket [] are native array syntax. 'new Array()' is JavaScript syntax and throws a fatal class error in PHP."
    },
    {
        "id": "quiz_php_5",
        "subject_id": "bcac501",
        "unit_no": 3,
        "difficulty": "easy",
        "type": "single_mcq",
        "question": "Which PHP superglobal contains form data submitted with the HTTP POST method?",
        "options": [
            "$_GET",
            "$_REQUEST_DATA",
            "$_POST",
            "$_SERVER_POST"
        ],
        "correct_indices": [
            2
        ],
        "explanation": "$_POST collects values from a form sent with method='post'. $_GET captures URL query parameters."
    },
    {
        "id": "quiz_php_6",
        "subject_id": "bcac501",
        "unit_no": 3,
        "difficulty": "medium",
        "type": "single_mcq",
        "question": "Which built-in function should be used to neutralize Cross-Site Scripting (XSS) by encoding characters into HTML entities?",
        "options": [
            "strip_tags()",
            "htmlspecialchars()",
            "md5()",
            "urlencode()"
        ],
        "correct_indices": [
            1
        ],
        "explanation": "htmlspecialchars() converts special characters (&, <, >, \", ') into HTML entities, preventing browser script execution."
    },
    {
        "id": "quiz_php_7",
        "subject_id": "bcac501",
        "unit_no": 4,
        "difficulty": "hard",
        "type": "single_mcq",
        "question": "Why are prepared statements in PDO completely immune to SQL injection?",
        "options": [
            "They use regex to remove SQL keywords from user input strings.",
            "They precompile the SQL statement template on the database server before parameters are sent, ensuring data is never parsed as code.",
            "They encrypt the entire database connection stream using TLS.",
            "They automatically reject any input containing quotation marks."
        ],
        "correct_indices": [
            1
        ],
        "explanation": "Prepared statements separate the query structure from literal parameter data; the DB compiler parses the AST first, so injected SQL syntax is treated strictly as string literals."
    },
    {
        "id": "quiz_php_8",
        "subject_id": "bcac501",
        "unit_no": 4,
        "difficulty": "medium",
        "type": "multi_mcq",
        "question": "Which PDO error modes can be configured using setAttribute(PDO::ATTR_ERRMODE, ...)? (Select all that apply)",
        "options": [
            "PDO::ERRMODE_SILENT",
            "PDO::ERRMODE_WARNING",
            "PDO::ERRMODE_EXCEPTION",
            "PDO::ERRMODE_CRITICAL"
        ],
        "correct_indices": [
            0,
            1,
            2
        ],
        "explanation": "PDO supports SILENT (sets error codes), WARNING (emits PHP warning), and EXCEPTION (throws PDOException). ERRMODE_CRITICAL does not exist."
    },
    {
        "id": "quiz_php_9",
        "subject_id": "bcac501",
        "unit_no": 4,
        "difficulty": "easy",
        "type": "true_false",
        "question": "PDO supports both positional placeholders (?) and named parameter placeholders (:name).",
        "options": [
            "True",
            "False"
        ],
        "correct_indices": [
            0
        ],
        "explanation": "True. PDO supports both ? and :named parameter binding, unlike MySQLi which only supports positional ?."
    },
    {
        "id": "quiz_php_10",
        "subject_id": "bcac501",
        "unit_no": 5,
        "difficulty": "medium",
        "type": "single_mcq",
        "question": "What is the primary vulnerability prevented by invoking session_regenerate_id(true) immediately upon user login?",
        "options": [
            "SQL Injection",
            "Session Fixation",
            "Cross-Origin Resource Sharing (CORS)",
            "Cross-Site Scripting (XSS)"
        ],
        "correct_indices": [
            1
        ],
        "explanation": "session_regenerate_id(true) issues a new session identifier and deletes the old pre-login session file, neutralizing Session Fixation attacks."
    },
    {
        "id": "quiz_php_11",
        "subject_id": "bcac501",
        "unit_no": 5,
        "difficulty": "hard",
        "type": "single_mcq",
        "question": "When validating file uploads in PHP, which method provides the most reliable verification of true file format?",
        "options": [
            "Checking the extension with pathinfo($_FILES['f']['name'], PATHINFO_EXTENSION)",
            "Reading the client MIME string in $_FILES['f']['type']",
            "Inspecting binary magic bytes using the finfo extension (finfo_file)",
            "Checking the filesize with filesize($_FILES['f']['tmp_name'])"
        ],
        "correct_indices": [
            2
        ],
        "explanation": "Client headers and extensions can be easily spoofed; inspecting binary magic bytes via finfo_file() reads actual binary headers directly on disk."
    },
    {
        "id": "quiz_php_12",
        "subject_id": "bcac501",
        "unit_no": 5,
        "difficulty": "medium",
        "type": "true_false",
        "question": "Marking session cookies as 'HttpOnly' prevents client-side JavaScript (e.g., document.cookie) from reading them.",
        "options": [
            "True",
            "False"
        ],
        "correct_indices": [
            0
        ],
        "explanation": "True. The HttpOnly flag instructs the browser that the cookie should not be accessible via client-side scripts, mitigating session theft via XSS."
    },
    {
        "id": "quiz_php_13",
        "subject_id": "bcac501",
        "unit_no": 6,
        "difficulty": "medium",
        "type": "single_mcq",
        "question": "In PHP object-oriented programming, which keyword is used to achieve horizontal code reuse across independent classes?",
        "options": [
            "extends",
            "implements",
            "trait",
            "namespace"
        ],
        "correct_indices": [
            2
        ],
        "explanation": "Traits (trait / use TraitName) provide horizontal method inclusion across unrelated classes, bypassing single-inheritance restrictions."
    },
    {
        "id": "quiz_php_14",
        "subject_id": "bcac501",
        "unit_no": 6,
        "difficulty": "hard",
        "type": "single_mcq",
        "question": "What was the architectural significance of introducing the Throwable interface in PHP 7?",
        "options": [
            "It eliminated the need for try-catch blocks.",
            "It unified internal engine fatal errors (Error) and userland exceptions (Exception) under a single catchable root.",
            "It enabled automated database rollback on any PHP notice.",
            "It replaced all PHP warnings with compile-time syntax errors."
        ],
        "correct_indices": [
            1
        ],
        "explanation": "Prior to PHP 7, fatal errors terminated scripts instantly. PHP 7 introduced Throwable, allowing both Error and Exception to be caught gracefully."
    },
    {
        "id": "quiz_php_15",
        "subject_id": "bcac501",
        "unit_no": 7,
        "difficulty": "easy",
        "type": "single_mcq",
        "question": "What architectural pattern is universally employed by modern PHP frameworks like Laravel and CodeIgniter?",
        "options": [
            "Model-View-Controller (MVC)",
            "Pipe and Filter",
            "Event-Sourced CQRS",
            "Peer-to-Peer"
        ],
        "correct_indices": [
            0
        ],
        "explanation": "MVC (Model-View-Controller) is the foundational design pattern decoupling database models from presentation views via controllers."
    },
    {
        "id": "quiz_php_16",
        "subject_id": "bcac501",
        "unit_no": 7,
        "difficulty": "medium",
        "type": "single_mcq",
        "question": "Which dependency management tool is the industry standard for PHP libraries and frameworks?",
        "options": [
            "npm",
            "pip",
            "Composer",
            "Maven"
        ],
        "correct_indices": [
            2
        ],
        "explanation": "Composer is the standard dependency manager for PHP, managing libraries defined in composer.json and generating PSR-4 autoloaders."
    },
    {
        "id": "quiz_php_17",
        "subject_id": "bcac501",
        "unit_no": 8,
        "difficulty": "medium",
        "type": "single_mcq",
        "question": "In the Laravel framework, which CLI tool is used to generate controllers, models, and run migrations?",
        "options": [
            "Spark",
            "Composer",
            "Artisan",
            "Breeze"
        ],
        "correct_indices": [
            2
        ],
        "explanation": "Artisan (`php artisan`) is the command-line interface included with Laravel providing commands for scaffolding, migrations, and caching."
    },
    {
        "id": "quiz_php_18",
        "subject_id": "bcac501",
        "unit_no": 8,
        "difficulty": "easy",
        "type": "single_mcq",
        "question": "What is the name of Laravel's built-in Object-Relational Mapping (ORM) engine?",
        "options": [
            "Doctrine",
            "Hibernate",
            "Eloquent",
            "ActiveRecord"
        ],
        "correct_indices": [
            2
        ],
        "explanation": "Eloquent is Laravel's native ActiveRecord ORM, allowing developers to interact with database tables as fluent object models."
    },
    {
        "id": "quiz_php_19",
        "subject_id": "bcac501",
        "unit_no": 8,
        "difficulty": "medium",
        "type": "true_false",
        "question": "In Laravel Blade templates, double curly braces {{ $variable }} automatically sanitize output through htmlspecialchars().",
        "options": [
            "True",
            "False"
        ],
        "correct_indices": [
            0
        ],
        "explanation": "True. {{ $var }} automatically escapes HTML entities. To render unescaped raw HTML, Blade requires {!! $var !!}."
    },
    {
        "id": "quiz_php_20",
        "subject_id": "bcac501",
        "unit_no": 4,
        "difficulty": "hard",
        "type": "case_study",
        "question": "Case Application: An e-commerce developer notices that users are submitting checkout forms multiple times by rapidly clicking the 'Pay Now' button, causing duplicate orders in the database. Which architectural remedy best guarantees idempotency?",
        "options": [
            "Relying solely on client-side JavaScript to disable the button after the first click.",
            "Wrapping the order insertion and inventory decrement in an InnoDB database transaction with a unique transaction token constraint.",
            "Switching from POST to GET requests for payment processing.",
            "Increasing the PHP script execution time limit."
        ],
        "correct_indices": [
            1
        ],
        "explanation": "Client-side button disabling can be bypassed or fail on network lag. Enforcing unique idempotent tokens inside a database transaction guarantees that duplicate submissions are rejected at the persistence layer."
    },
    {
        "id": "quiz_php_21",
        "subject_id": "bcac501",
        "unit_no": 3,
        "difficulty": "medium",
        "type": "single_mcq",
        "question": "What is the return value of password_verify('mypass', $hash) when the password matches the Bcrypt hash?",
        "options": [
            "1",
            "0",
            "true",
            "null"
        ],
        "correct_indices": [
            2
        ],
        "explanation": "password_verify() returns a strict boolean: true if the password matches the hash, false otherwise."
    },
    {
        "id": "quiz_java_1",
        "subject_id": "bcac502",
        "unit_no": 1,
        "difficulty": "easy",
        "type": "single_mcq",
        "question": "Which component of the Java runtime environment dynamically converts frequently executed bytecode into native CPU instructions?",
        "options": [
            "ClassLoader",
            "JIT Compiler",
            "Bytecode Verifier",
            "Garbage Collector"
        ],
        "correct_indices": [
            1
        ],
        "explanation": "The Just-In-Time (JIT) compiler translates hot-spot bytecode sequences directly into native machine code at runtime."
    },
    {
        "id": "quiz_java_2",
        "subject_id": "bcac502",
        "unit_no": 1,
        "difficulty": "easy",
        "type": "true_false",
        "question": "In the JVM memory model, Stack memory is shared across all threads, while Heap memory is private to each thread.",
        "options": [
            "True",
            "False"
        ],
        "correct_indices": [
            1
        ],
        "explanation": "False. Heap memory is shared across all threads; Stack memory is private and allocated per individual thread invocation."
    },
    {
        "id": "quiz_java_3",
        "subject_id": "bcac502",
        "unit_no": 2,
        "difficulty": "easy",
        "type": "single_mcq",
        "question": "What is the size in bits of the primitive 'int' data type in Java across all operating systems?",
        "options": [
            "16 bits",
            "32 bits",
            "64 bits",
            "Varies depending on whether the OS is 32-bit or 64-bit"
        ],
        "correct_indices": [
            1
        ],
        "explanation": "Unlike C/C++, Java's primitive bit widths are strictly platform-independent: int is guaranteed 32 bits two's complement on every CPU."
    },
    {
        "id": "quiz_java_4",
        "subject_id": "bcac502",
        "unit_no": 2,
        "difficulty": "medium",
        "type": "single_mcq",
        "question": "What is the result of evaluating the expression (5 / 2) in Java when both operands are integers?",
        "options": [
            "2.5",
            "2",
            "3",
            "Compile-time error"
        ],
        "correct_indices": [
            1
        ],
        "explanation": "Integer division truncates the fractional portion, resulting in 2. To get 2.5, at least one operand must be a float or double (e.g. 5.0 / 2)."
    },
    {
        "id": "quiz_java_5",
        "subject_id": "bcac502",
        "unit_no": 3,
        "difficulty": "easy",
        "type": "single_mcq",
        "question": "Which keyword is used inside a class constructor to explicitly invoke another overloaded constructor in the same class?",
        "options": [
            "super()",
            "this()",
            "self()",
            "constructor()"
        ],
        "correct_indices": [
            1
        ],
        "explanation": "this() performs constructor chaining within the same class and must be the very first statement of the constructor body."
    },
    {
        "id": "quiz_java_6",
        "subject_id": "bcac502",
        "unit_no": 3,
        "difficulty": "medium",
        "type": "multi_mcq",
        "question": "Which of the following statements regarding Java access modifiers are correct? (Select all that apply)",
        "options": [
            "private members are visible only within their own enclosing class.",
            "protected members are accessible to subclasses in other packages.",
            "default (package-private) members are accessible anywhere within the entire application.",
            "public members are accessible from any package across the JVM."
        ],
        "correct_indices": [
            0,
            1,
            3
        ],
        "explanation": "Default members are restricted to the same package. Private, protected, and public scopes are described accurately."
    },
    {
        "id": "quiz_java_7",
        "subject_id": "bcac502",
        "unit_no": 4,
        "difficulty": "medium",
        "type": "single_mcq",
        "question": "Which mechanism enables runtime polymorphism in Java when a superclass reference invokes an overridden method?",
        "options": [
            "Static Binding",
            "Dynamic Method Dispatch",
            "Operator Overloading",
            "Type Erasure"
        ],
        "correct_indices": [
            1
        ],
        "explanation": "Dynamic method dispatch inspects the actual object on the heap at runtime via the virtual method table (vtable) to invoke the overridden method."
    },
    {
        "id": "quiz_java_8",
        "subject_id": "bcac502",
        "unit_no": 4,
        "difficulty": "easy",
        "type": "true_false",
        "question": "In Java, private and static methods can be overridden by a subclass.",
        "options": [
            "True",
            "False"
        ],
        "correct_indices": [
            1
        ],
        "explanation": "False. Private methods are invisible to subclasses, and static methods participate in method hiding bound at compile time, not overriding."
    },
    {
        "id": "quiz_java_9",
        "subject_id": "bcac502",
        "unit_no": 4,
        "difficulty": "medium",
        "type": "single_mcq",
        "question": "What is the effect of applying the 'final' keyword to a class definition in Java?",
        "options": [
            "The class cannot be instantiated.",
            "The class cannot be extended by any subclass.",
            "All methods in the class automatically become abstract.",
            "The class is stored permanently in stack memory."
        ],
        "correct_indices": [
            1
        ],
        "explanation": "A final class (e.g. java.lang.String, Math) cannot be inherited or subclassed."
    },
    {
        "id": "quiz_java_10",
        "subject_id": "bcac502",
        "unit_no": 5,
        "difficulty": "medium",
        "type": "single_mcq",
        "question": "Given: String s1 = \"MAKAUT\"; String s2 = new String(\"MAKAUT\"); What will (s1 == s2) and s1.equals(s2) evaluate to?",
        "options": [
            "true and true",
            "false and true",
            "true and false",
            "false and false"
        ],
        "correct_indices": [
            1
        ],
        "explanation": "`==` compares memory addresses (s1 is in String Constant Pool; s2 is in general heap, so false). `.equals()` compares character values, returning true."
    },
    {
        "id": "quiz_java_11",
        "subject_id": "bcac502",
        "unit_no": 5,
        "difficulty": "medium",
        "type": "single_mcq",
        "question": "Which character sequence class is mutable and thread-safe via synchronized methods?",
        "options": [
            "String",
            "StringBuilder",
            "StringBuffer",
            "CharBuffer"
        ],
        "correct_indices": [
            2
        ],
        "explanation": "StringBuffer is mutable and thread-safe because its methods are synchronized. StringBuilder is mutable but unsynchronized."
    },
    {
        "id": "quiz_java_12",
        "subject_id": "bcac502",
        "unit_no": 6,
        "difficulty": "medium",
        "type": "single_mcq",
        "question": "Which keyword was introduced in Java 8 to permit concrete method implementations directly inside interfaces?",
        "options": [
            "static",
            "default",
            "concrete",
            "virtual"
        ],
        "correct_indices": [
            1
        ],
        "explanation": "default methods inside interfaces allow backward-compatible interface evolution without breaking existing implementing classes."
    },
    {
        "id": "quiz_java_13",
        "subject_id": "bcac502",
        "unit_no": 6,
        "difficulty": "easy",
        "type": "true_false",
        "question": "An interface in Java can have instance variables and non-static constructors.",
        "options": [
            "True",
            "False"
        ],
        "correct_indices": [
            1
        ],
        "explanation": "False. Interface fields are strictly `public static final` constants, and interfaces cannot have constructors."
    },
    {
        "id": "quiz_java_14",
        "subject_id": "bcac502",
        "unit_no": 7,
        "difficulty": "medium",
        "type": "single_mcq",
        "question": "Which of the following exceptions is a Checked Exception that must be explicitly handled or declared?",
        "options": [
            "NullPointerException",
            "ArithmeticException",
            "IOException",
            "ArrayIndexOutOfBoundsException"
        ],
        "correct_indices": [
            2
        ],
        "explanation": "IOException derives directly from Exception (not RuntimeException) and is checked at compile-time. The others are unchecked RuntimeExceptions."
    },
    {
        "id": "quiz_java_15",
        "subject_id": "bcac502",
        "unit_no": 7,
        "difficulty": "easy",
        "type": "single_mcq",
        "question": "In Java 7+, which language construct automatically closes resources implementing AutoCloseable without an explicit finally block?",
        "options": [
            "try-with-resources",
            "auto-try block",
            "safe-catch block",
            "resource-finally block"
        ],
        "correct_indices": [
            0
        ],
        "explanation": "try-with-resources syntax `try (Resource r = ...) { }` guarantees that `.close()` is automatically invoked on block exit."
    },
    {
        "id": "quiz_java_16",
        "subject_id": "bcac502",
        "unit_no": 8,
        "difficulty": "medium",
        "type": "single_mcq",
        "question": "What is the primary difference between InputStream/OutputStream and Reader/Writer classes in java.io?",
        "options": [
            "InputStream/OutputStream handle 8-bit byte binary data; Reader/Writer handle 16-bit Unicode character data.",
            "Reader/Writer are only for network sockets; InputStream is only for files.",
            "InputStream is deprecated in Java 17.",
            "Reader/Writer are asynchronous; InputStream is synchronous."
        ],
        "correct_indices": [
            0
        ],
        "explanation": "Byte streams handle 8-bit binary data; Character streams handle 16-bit Unicode text characters."
    },
    {
        "id": "quiz_java_17",
        "subject_id": "bcac502",
        "unit_no": 8,
        "difficulty": "medium",
        "type": "single_mcq",
        "question": "Which keyword prevents a sensitive class member variable from being serialized to disk?",
        "options": [
            "volatile",
            "transient",
            "static",
            "synchronized"
        ],
        "correct_indices": [
            1
        ],
        "explanation": "The transient keyword instructs ObjectOutputStream to skip that field during object serialization, keeping passwords and keys off disk."
    },
    {
        "id": "quiz_java_18",
        "subject_id": "bcac502",
        "unit_no": 9,
        "difficulty": "easy",
        "type": "single_mcq",
        "question": "Which method is invoked to transition a Java Thread from the NEW state to the RUNNABLE state in the OS scheduler queue?",
        "options": [
            "run()",
            "start()",
            "execute()",
            "init()"
        ],
        "correct_indices": [
            1
        ],
        "explanation": "Calling `.start()` allocates a new call stack and transitions the thread to RUNNABLE. Calling `.run()` merely executes code on the caller thread."
    },
    {
        "id": "quiz_java_19",
        "subject_id": "bcac502",
        "unit_no": 9,
        "difficulty": "hard",
        "type": "multi_mcq",
        "question": "Which of the following methods must be called STRICTLY within a synchronized context (block or method)? (Select all that apply)",
        "options": [
            "wait()",
            "notify()",
            "sleep()",
            "notifyAll()"
        ],
        "correct_indices": [
            0,
            1,
            3
        ],
        "explanation": "wait(), notify(), and notifyAll() manipulate the object's monitor lock and throw IllegalMonitorStateException if called outside synchronized blocks. sleep() can be called anywhere."
    },
    {
        "id": "quiz_java_20",
        "subject_id": "bcac502",
        "unit_no": 9,
        "difficulty": "hard",
        "type": "case_study",
        "question": "Case Application: An enterprise banking transaction engine reports intermittent data corruption where balance values randomly decrease below zero during concurrent transfers. Inspection reveals that Account.withdraw() lacks locking. What is the root cause and optimal remediation?",
        "options": [
            "Memory leak in JVM Metaspace; restart the server every hour.",
            "Race condition between concurrent threads reading stale balance; declare withdraw() synchronized or use AtomicLong.",
            "ClassLoader duplicate class loading; delete duplicate JAR files.",
            "Stack overflow; increase JVM thread stack size via -Xss."
        ],
        "correct_indices": [
            1
        ],
        "explanation": "Concurrent threads reading and updating shared un-synchronized fields cause race conditions. Synchronizing access enforces mutual exclusion and eliminates the defect."
    },
    {
        "id": "quiz_java_21",
        "subject_id": "bcac502",
        "unit_no": 5,
        "difficulty": "hard",
        "type": "single_mcq",
        "question": "In Java 8, when a HashMap bucket encounters more than 8 collisions (and table capacity is >= 64), how does its internal representation transform?",
        "options": [
            "It throws a HashCollisionException.",
            "It converts the linked node list into a balanced Red-Black Tree, improving lookup from O(n) to O(log n).",
            "It automatically evicts the oldest entry.",
            "It switches to an array of ArrayLists."
        ],
        "correct_indices": [
            1
        ],
        "explanation": "Java 8 treeifies hash bucket bins with >8 entries into Red-Black Trees, improving worst-case search complexity from O(n) to O(log n)."
    },
    {
        "id": "quiz_ent_1",
        "subject_id": "mim502",
        "unit_no": 1,
        "difficulty": "easy",
        "type": "single_mcq",
        "question": "Which economist formulated the concept of 'Creative Destruction', identifying the entrepreneur as the core agent of market disruption?",
        "options": [
            "Adam Smith",
            "Joseph Schumpeter",
            "John Maynard Keynes",
            "David Ricardo"
        ],
        "correct_indices": [
            1
        ],
        "explanation": "Joseph Schumpeter established that economic evolution is driven by Creative Destruction, where entrepreneurial innovations replace outdated firms."
    },
    {
        "id": "quiz_ent_2",
        "subject_id": "mim502",
        "unit_no": 1,
        "difficulty": "easy",
        "type": "true_false",
        "question": "Entrepreneurship contributes to balanced regional development by dispersing industrial production away from congested metropolitan centers.",
        "options": [
            "True",
            "False"
        ],
        "correct_indices": [
            0
        ],
        "explanation": "True. Setting up small and medium enterprises in backward and rural districts disperses wealth and curtails unplanned urban migration."
    },
    {
        "id": "quiz_ent_3",
        "subject_id": "mim502",
        "unit_no": 1,
        "difficulty": "medium",
        "type": "multi_mcq",
        "question": "According to Joseph Schumpeter, which of the following represent recognized forms of entrepreneurial innovation? (Select all that apply)",
        "options": [
            "Introduction of a new consumer good or service",
            "Introduction of a new technological method of production",
            "Conquest of a new source of raw material supply",
            "Copying an incumbent's exact product without any modifications"
        ],
        "correct_indices": [
            0,
            1,
            2
        ],
        "explanation": "Schumpeter's 5 forms include new goods, new production methods, new markets, new raw material sources, and industrial reorganization. Merely copying without change is not innovation."
    },
    {
        "id": "quiz_ent_4",
        "subject_id": "mim502",
        "unit_no": 2,
        "difficulty": "medium",
        "type": "single_mcq",
        "question": "According to Clarence Danhof's taxonomy, which type of entrepreneur is vital in developing economies by rapidly adapting proven global innovations to local markets?",
        "options": [
            "Innovating Entrepreneur",
            "Imitative (Adoptive) Entrepreneur",
            "Fabian Entrepreneur",
            "Drone Entrepreneur"
        ],
        "correct_indices": [
            1
        ],
        "explanation": "Imitative entrepreneurs adapt proven foreign technologies to local constraints, playing a crucial role in developing nations with limited indigenous R&D capital."
    },
    {
        "id": "quiz_ent_5",
        "subject_id": "mim502",
        "unit_no": 2,
        "difficulty": "easy",
        "type": "single_mcq",
        "question": "Which type of entrepreneur in Danhof's classification adamantly refuses to adopt modern production techniques even when suffering persistent losses?",
        "options": [
            "Fabian",
            "Drone",
            "Imitative",
            "Agricultural"
        ],
        "correct_indices": [
            1
        ],
        "explanation": "Drone entrepreneurs adhere strictly to traditional customary methods despite losses, leading to inevitable business liquidation."
    },
    {
        "id": "quiz_ent_6",
        "subject_id": "mim502",
        "unit_no": 2,
        "difficulty": "medium",
        "type": "single_mcq",
        "question": "What is the core distinction between an Entrepreneur and an Intrapreneur?",
        "options": [
            "Entrepreneurs operate within existing corporations; intrapreneurs work independently.",
            "An entrepreneur founds an independent venture bearing personal financial risk; an intrapreneur drives innovation inside an established corporation using company resources.",
            "Intrapreneurs have zero technical skills.",
            "Entrepreneurs never earn profits."
        ],
        "correct_indices": [
            1
        ],
        "explanation": "An intrapreneur exercises entrepreneurial vision as an employee using corporate backing without risking personal equity capital."
    },
    {
        "id": "quiz_ent_7",
        "subject_id": "mim502",
        "unit_no": 3,
        "difficulty": "easy",
        "type": "single_mcq",
        "question": "In David McClelland's Acquired Needs Theory, which psychological drive is identified as the primary determinant of high entrepreneurial motivation?",
        "options": [
            "Need for Affiliation (n-Aff)",
            "Need for Power (n-Pow)",
            "Need for Achievement (n-Ach)",
            "Need for Security (n-Sec)"
        ],
        "correct_indices": [
            2
        ],
        "explanation": "David McClelland proved that a high Need for Achievement (n-Ach) is the definitive psychological motivator for entrepreneurs."
    },
    {
        "id": "quiz_ent_8",
        "subject_id": "mim502",
        "unit_no": 3,
        "difficulty": "medium",
        "type": "true_false",
        "question": "High n-Ach entrepreneurs are extreme high-stakes gamblers who prefer situations determined purely by random chance.",
        "options": [
            "True",
            "False"
        ],
        "correct_indices": [
            1
        ],
        "explanation": "False. McClelland proved that high n-Ach entrepreneurs seek moderate calculated risks where personal competence, effort, and strategy control the outcome."
    },
    {
        "id": "quiz_ent_9",
        "subject_id": "mim502",
        "unit_no": 3,
        "difficulty": "medium",
        "type": "single_mcq",
        "question": "Which historic Indian field experiment conducted by David McClelland in 1964 proved that entrepreneurial motivation can be systematically developed in adults?",
        "options": [
            "The Kakinada Experiment",
            "The Ahmedabad Experiment",
            "The Pune Project",
            "The Bengaluru Trial"
        ],
        "correct_indices": [
            0
        ],
        "explanation": "The Kakinada Experiment in Andhra Pradesh demonstrated that Achievement Motivation Training (AMT) significantly elevates venture creation and investment rates."
    },
    {
        "id": "quiz_ent_10",
        "subject_id": "mim502",
        "unit_no": 3,
        "difficulty": "easy",
        "type": "single_mcq",
        "question": "Entrepreneurs driven into business by layoffs, poverty, or lack of alternative employment options are categorized under which motivational force?",
        "options": [
            "Pull Factors (Opportunity-based)",
            "Push Factors (Necessity-based)",
            "External Angel Factors",
            "Macro Scalers"
        ],
        "correct_indices": [
            1
        ],
        "explanation": "Push factors represent distress triggers (unemployment, underpayment) pushing individuals into necessity-driven self-employment."
    },
    {
        "id": "quiz_ent_11",
        "subject_id": "mim502",
        "unit_no": 4,
        "difficulty": "medium",
        "type": "single_mcq",
        "question": "Which document serves as the comprehensive techno-commercial master blueprint submitted to banks and institutions for term loan sanctions?",
        "options": [
            "Memorandum of Association",
            "Detailed Project Report (DPR)",
            "Articles of Incorporation",
            "Income Tax Return"
        ],
        "correct_indices": [
            1
        ],
        "explanation": "The Detailed Project Report (DPR) outlines technical specifications, plant layout, financial forecasts, DSCR ratios, and market demand for lending evaluation."
    },
    {
        "id": "quiz_ent_12",
        "subject_id": "mim502",
        "unit_no": 4,
        "difficulty": "hard",
        "type": "single_mcq",
        "question": "Which financial metric is scrutinized by lending banks to verify whether an enterprise's operating earnings can comfortably service annual loan principal and interest?",
        "options": [
            "Current Ratio",
            "Debt-Service Coverage Ratio (DSCR)",
            "Gross Profit Margin",
            "Inventory Turnover"
        ],
        "correct_indices": [
            1
        ],
        "explanation": "DSCR = (PAT + Depr + Interest) / (Interest + Principal Repayment). Banks mandate a benchmark ratio of 1.5\u20132.0 to ensure safe debt repayment."
    },
    {
        "id": "quiz_ent_13",
        "subject_id": "mim502",
        "unit_no": 4,
        "difficulty": "medium",
        "type": "single_mcq",
        "question": "At the Break-Even Point (BEP) of a proposed commercial manufacturing project:",
        "options": [
            "Total revenues equal total operational costs (Zero profit, zero loss).",
            "Taxes are zero.",
            "Debt is completely repaid.",
            "Variable costs equal zero."
        ],
        "correct_indices": [
            0
        ],
        "explanation": "BEP is the operational output volume where Total Revenue equals Total Cost (Fixed + Variable), yielding zero operational profit or loss."
    },
    {
        "id": "quiz_ent_14",
        "subject_id": "mim502",
        "unit_no": 5,
        "difficulty": "easy",
        "type": "single_mcq",
        "question": "Which apex financial institution in India acts as the principal body for refinancing, promotion, and development of MSME credit?",
        "options": [
            "NABARD",
            "SIDBI",
            "SEBI",
            "IRDAI"
        ],
        "correct_indices": [
            1
        ],
        "explanation": "Small Industries Development Bank of India (SIDBI) is the apex financial body for refinancing and direct lending to MSMEs."
    },
    {
        "id": "quiz_ent_15",
        "subject_id": "mim502",
        "unit_no": 5,
        "difficulty": "medium",
        "type": "single_mcq",
        "question": "Which nodal government center at the district level acts as a single-window interface for industrial registration, land allocation, and state subsidies?",
        "options": [
            "District Industries Centre (DIC)",
            "National Small Industries Corporation (NSIC)",
            "SIDO",
            "Export Promotion Council"
        ],
        "correct_indices": [
            0
        ],
        "explanation": "District Industries Centres (DICs) operate in district headquarters to provide single-window clearances, guidance, and subsidy disbursal."
    },
    {
        "id": "quiz_ent_16",
        "subject_id": "mim502",
        "unit_no": 5,
        "difficulty": "hard",
        "type": "single_mcq",
        "question": "Under the revised composite criteria (2020), an enterprise is classified as 'MICRO' if:",
        "options": [
            "Investment <= \u20b91 Crore AND Annual Turnover <= \u20b95 Crore",
            "Investment <= \u20b910 Crore AND Annual Turnover <= \u20b950 Crore",
            "Investment <= \u20b950 Crore AND Annual Turnover <= \u20b9250 Crore",
            "Investment <= \u20b925 Lakhs AND Annual Turnover <= \u20b91 Crore"
        ],
        "correct_indices": [
            0
        ],
        "explanation": "Micro enterprise threshold: Investment in Plant & Machinery <= \u20b91 Crore AND Annual Turnover <= \u20b95 Crore."
    },
    {
        "id": "quiz_ent_17",
        "subject_id": "mim502",
        "unit_no": 5,
        "difficulty": "easy",
        "type": "true_false",
        "question": "Under the revised MSME classification guidelines, export turnover is excluded when calculating an enterprise's annual turnover ceiling.",
        "options": [
            "True",
            "False"
        ],
        "correct_indices": [
            0
        ],
        "explanation": "True. Export revenues are explicitly excluded from turnover calculations to encourage MSMEs to export without losing their subsidy tiers."
    },
    {
        "id": "quiz_ent_18",
        "subject_id": "mim502",
        "unit_no": 5,
        "difficulty": "medium",
        "type": "single_mcq",
        "question": "What is the statutory payment deadline mandated by the MSMED Act for buyers purchasing goods or services from registered MSMEs?",
        "options": [
            "15 days",
            "30 days",
            "45 days",
            "90 days"
        ],
        "correct_indices": [
            2
        ],
        "explanation": "The MSMED Act mandates a 45-day statutory payment cap. Defaulting corporate buyers face penal interest at three times the RBI bank rate."
    },
    {
        "id": "quiz_ent_19",
        "subject_id": "mim502",
        "unit_no": 5,
        "difficulty": "medium",
        "type": "single_mcq",
        "question": "What is the primary difference between Angel Investors and Venture Capitalists (VCs)?",
        "options": [
            "Angel investors invest their personal net worth into early prototypes; VCs invest institutional pooled funds into scaling ventures.",
            "VCs only invest in non-profit charities.",
            "Angel investors require controlling majority equity; VCs never take equity.",
            "There is no difference; they are identical terms."
        ],
        "correct_indices": [
            0
        ],
        "explanation": "Angels are high-net-worth individuals investing personal wealth at early seed stages; VCs are professional institutions managing pooled third-party funds for growth stages."
    },
    {
        "id": "quiz_ent_20",
        "subject_id": "mim502",
        "unit_no": 5,
        "difficulty": "hard",
        "type": "case_study",
        "question": "Case Application: An agricultural biotech startup has successfully developed a drought-resistant seed in university laboratories but lacks $100k capital to survive field trials before generating commercial sales. Which institutional support mechanism specifically bridges this 'Valley of Death'?",
        "options": [
            "Listing on the main board of the National Stock Exchange (NSE).",
            "A University Technology Business Incubator (TBI) providing seed grants, wet lab access, and mentorship.",
            "Seeking an offshore sovereign wealth fund syndicated bond.",
            "Filing for corporate bankruptcy."
        ],
        "correct_indices": [
            1
        ],
        "explanation": "Technology Business Incubators (TBIs) provide subsidized lab equipment, seed capital, and mentorship precisely to guide early science ventures across the pre-revenue Valley of Death."
    },
    {
        "id": "quiz_ent_21",
        "subject_id": "mim502",
        "unit_no": 5,
        "difficulty": "easy",
        "type": "single_mcq",
        "question": "What is the name of the Government of India's unified online portal for paperless MSME registration?",
        "options": [
            "Startup India Hub",
            "Udyam Registration",
            "GeM Portal",
            "MCA21"
        ],
        "correct_indices": [
            1
        ],
        "explanation": "Udyam Registration (udyamregistration.gov.in) is the official paperless digital registration portal for MSMEs in India."
    },
    {
        "id": "quiz_fm_1",
        "subject_id": "mim501",
        "unit_no": 1,
        "difficulty": "easy",
        "type": "single_mcq",
        "question": "Why is Wealth Maximization universally preferred over Profit Maximization as the primary corporate financial objective?",
        "options": [
            "It strictly considers the time value of money, cash flow durations, and business risk.",
            "It guarantees zero corporate income tax.",
            "It focuses exclusively on short-term single-quarter accounting profits.",
            "It eliminates all need for debt financing."
        ],
        "correct_indices": [
            0
        ],
        "explanation": "Wealth maximization accounts for cash flow timing and risk, maximizing the net present value of equity shares."
    },
    {
        "id": "quiz_fm_2",
        "subject_id": "mim501",
        "unit_no": 1,
        "difficulty": "medium",
        "type": "single_mcq",
        "question": "If a corporation issues 10% debentures at par and pays a 30% corporate income tax rate, what is its effective after-tax Cost of Debt (Kd)?",
        "options": [
            "10.0%",
            "7.0%",
            "3.0%",
            "13.0%"
        ],
        "correct_indices": [
            1
        ],
        "explanation": "Kd(after-tax) = Pre-tax Kd * (1 - T) = 10% * (1 - 0.30) = 7.0% due to the interest tax shield."
    },
    {
        "id": "quiz_fm_3",
        "subject_id": "mim501",
        "unit_no": 1,
        "difficulty": "easy",
        "type": "true_false",
        "question": "Market value weights are theoretically superior to book value weights when calculating Weighted Average Cost of Capital (WACC).",
        "options": [
            "True",
            "False"
        ],
        "correct_indices": [
            0
        ],
        "explanation": "True. Market value weights reflect current economic opportunity costs, whereas book values reflect historical accounting costs."
    },
    {
        "id": "quiz_fm_4",
        "subject_id": "mim501",
        "unit_no": 2,
        "difficulty": "easy",
        "type": "single_mcq",
        "question": "What is the standard benchmark rule-of-thumb ratio for the Current Ratio in corporate financial analysis?",
        "options": [
            "1:1",
            "2:1",
            "3:1",
            "0.5:1"
        ],
        "correct_indices": [
            1
        ],
        "explanation": "A Current Ratio of 2:1 is the recognized conservative benchmark ensuring a 100% safety buffer over current liabilities."
    },
    {
        "id": "quiz_fm_5",
        "subject_id": "mim501",
        "unit_no": 2,
        "difficulty": "medium",
        "type": "single_mcq",
        "question": "When computing the Quick (Acid-Test) Ratio, which asset is explicitly deducted from Current Assets?",
        "options": [
            "Cash at Bank",
            "Marketable Securities",
            "Inventory and Prepaid Expenses",
            "Trade Debtors"
        ],
        "correct_indices": [
            2
        ],
        "explanation": "Quick Assets = Current Assets - Inventory - Prepaid Expenses. Inventories are excluded because they cannot be liquidated into cash immediately."
    },
    {
        "id": "quiz_fm_6",
        "subject_id": "mim501",
        "unit_no": 2,
        "difficulty": "hard",
        "type": "multi_mcq",
        "question": "Which of the following are the three multiplicative components of the classic DuPont identity for Return on Equity (ROE)? (Select all that apply)",
        "options": [
            "Net Profit Margin (Net Income / Sales)",
            "Asset Turnover (Sales / Total Assets)",
            "Financial Leverage Equity Multiplier (Total Assets / Equity)",
            "Price-to-Earnings Ratio (P/E)"
        ],
        "correct_indices": [
            0,
            1,
            2
        ],
        "explanation": "DuPont ROE = Operating Margin * Asset Velocity * Financial Multiplier. P/E is a market valuation multiple, not a DuPont operational component."
    },
    {
        "id": "quiz_fm_7",
        "subject_id": "mim501",
        "unit_no": 3,
        "difficulty": "easy",
        "type": "single_mcq",
        "question": "Under the Net Present Value (NPV) decision rule, an independent capital project should be accepted if its NPV is:",
        "options": [
            "Greater than 0",
            "Less than 0",
            "Equal to the Cost of Capital",
            "Equal to zero only"
        ],
        "correct_indices": [
            0
        ],
        "explanation": "NPV > 0 indicates that the present value of future cash inflows exceeds the initial capital outlay, expanding shareholder wealth."
    },
    {
        "id": "quiz_fm_8",
        "subject_id": "mim501",
        "unit_no": 3,
        "difficulty": "medium",
        "type": "single_mcq",
        "question": "What is the Internal Rate of Return (IRR) of an investment project?",
        "options": [
            "The discount rate that equates the present value of cash inflows to the initial investment outlay (NPV = 0).",
            "The accounting rate of return divided by project duration.",
            "The bank prime lending interest rate.",
            "The corporate tax rate."
        ],
        "correct_indices": [
            0
        ],
        "explanation": "IRR is the internal break-even discount rate where PV(Inflows) - Outlay = 0."
    },
    {
        "id": "quiz_fm_9",
        "subject_id": "mim501",
        "unit_no": 3,
        "difficulty": "hard",
        "type": "single_mcq",
        "question": "In mutually exclusive project ranking conflicts between NPV and IRR, why is the NPV decision rule theoretically superior?",
        "options": [
            "NPV assumes cash flows are reinvested at the realistic Cost of Capital (WACC), whereas IRR assumes reinvestment at the project's own IRR.",
            "NPV is always a percentage figure.",
            "NPV ignores cash flows beyond the payback period.",
            "IRR requires negative interest rates."
        ],
        "correct_indices": [
            0
        ],
        "explanation": "NPV assumes intermediate cash flows are reinvested at the firm's opportunity cost of capital (WACC), which is realistic; IRR assumes reinvestment at its own rate."
    },
    {
        "id": "quiz_fm_10",
        "subject_id": "mim501",
        "unit_no": 3,
        "difficulty": "medium",
        "type": "single_mcq",
        "question": "Under capital rationing constraints with divisible projects, how should project proposals be prioritized to maximize total portfolio NPV?",
        "options": [
            "Rank in descending order of Profitability Index (PI) and fund downward until the budget is exhausted.",
            "Select projects with the longest payback period.",
            "Accept projects alphabetically.",
            "Fund the single largest project by capital outlay."
        ],
        "correct_indices": [
            0
        ],
        "explanation": "Ranking by PI (PV of inflows / Outlay) maximizes capital efficiency per dollar invested under budget ceiling constraints."
    },
    {
        "id": "quiz_fm_11",
        "subject_id": "mim501",
        "unit_no": 4,
        "difficulty": "medium",
        "type": "single_mcq",
        "question": "What is the formula for calculating the Degree of Operating Leverage (DOL)?",
        "options": [
            "Contribution / EBIT",
            "EBIT / (EBIT - Interest)",
            "Sales / Variable Cost",
            "EBIT / Net Income"
        ],
        "correct_indices": [
            0
        ],
        "explanation": "DOL = Contribution / EBIT = % Change in EBIT / % Change in Sales. It quantifies business risk arising from fixed operating overheads."
    },
    {
        "id": "quiz_fm_12",
        "subject_id": "mim501",
        "unit_no": 4,
        "difficulty": "medium",
        "type": "single_mcq",
        "question": "If a corporation has a Degree of Operating Leverage (DOL) of 2.0 and a Degree of Financial Leverage (DFL) of 1.5, what is its Degree of Combined Leverage (DCL)?",
        "options": [
            "3.5",
            "3.0",
            "0.5",
            "1.33"
        ],
        "correct_indices": [
            1
        ],
        "explanation": "DCL = DOL * DFL = 2.0 * 1.5 = 3.0. A 10% increase in sales generates a 30% jump in EPS."
    },
    {
        "id": "quiz_fm_13",
        "subject_id": "mim501",
        "unit_no": 4,
        "difficulty": "medium",
        "type": "single_mcq",
        "question": "What does the EBIT-EPS Indifference Point represent?",
        "options": [
            "The operating profit (EBIT) level where two alternative financing plans produce identical Earnings Per Share (EPS).",
            "The point where income tax equals zero.",
            "The level where shareholders demand 100% dividend payout.",
            "The breakeven sales volume."
        ],
        "correct_indices": [
            0
        ],
        "explanation": "The indifference point is the EBIT level where competing debt and equity plans yield equal EPS."
    },
    {
        "id": "quiz_fm_14",
        "subject_id": "mim501",
        "unit_no": 4,
        "difficulty": "hard",
        "type": "single_mcq",
        "question": "In the Modigliani-Miller (MM) hypothesis without corporate taxes (1958), why is a firm's market value independent of its capital structure?",
        "options": [
            "Because arbitrage by investors substituting personal leverage for corporate leverage restores market valuation parity.",
            "Because banks are forbidden from charging interest.",
            "Because all debt is guaranteed by the central bank.",
            "Because equity shares can never change in price."
        ],
        "correct_indices": [
            0
        ],
        "explanation": "Investors engage in personal homemade leverage arbitrage, equalizing the cost of capital and firm value between levered and unlevered firms."
    },
    {
        "id": "quiz_fm_15",
        "subject_id": "mim501",
        "unit_no": 5,
        "difficulty": "medium",
        "type": "single_mcq",
        "question": "In the Risk-Adjusted Discount Rate (RADR) method of capital budgeting:",
        "options": [
            "The discount rate is increased by adding a risk premium to the risk-free rate (k = Rf + Rp).",
            "The cash inflows are reduced by a Certainty Equivalent factor while discounting at the risk-free rate.",
            "Only projects with zero risk are accepted.",
            "The discount rate is set to zero."
        ],
        "correct_indices": [
            0
        ],
        "explanation": "RADR adjusts the denominator (discount rate) upward: Hurdle rate k = Rf + Risk Premium."
    },
    {
        "id": "quiz_fm_16",
        "subject_id": "mim501",
        "unit_no": 5,
        "difficulty": "hard",
        "type": "single_mcq",
        "question": "Why is the Certainty Equivalent (CE) approach theoretically superior to the RADR method?",
        "options": [
            "It separates management's risk aversion perception from the time value of money.",
            "It requires zero mathematical calculations.",
            "It guarantees an IRR above 20%.",
            "It only works in inflationary economies."
        ],
        "correct_indices": [
            0
        ],
        "explanation": "CE scales uncertain cash flows to riskless sums first, and discounts them strictly at the pure risk-free rate Rf, avoiding compounded risk distortion."
    },
    {
        "id": "quiz_fm_17",
        "subject_id": "mim501",
        "unit_no": 6,
        "difficulty": "medium",
        "type": "single_mcq",
        "question": "According to James E. Walter's Dividend Model, what is the optimal dividend payout ratio for a Growth Firm where internal return (r) exceeds the cost of capital (k)?",
        "options": [
            "0% Payout (100% Retention)",
            "100% Payout (0% Retention)",
            "50% Payout",
            "Indifferent (any percentage)"
        ],
        "correct_indices": [
            0
        ],
        "explanation": "When r > k, shareholders earn higher compounding returns if the firm retains 100% of profits, maximizing market share price at 0% payout."
    },
    {
        "id": "quiz_fm_18",
        "subject_id": "mim501",
        "unit_no": 6,
        "difficulty": "medium",
        "type": "single_mcq",
        "question": "For a Declining Firm where internal return (r) is less than the cost of capital (k), Walter's model dictates that the optimal payout is:",
        "options": [
            "0%",
            "50%",
            "100%",
            "25%"
        ],
        "correct_indices": [
            2
        ],
        "explanation": "When r < k, internal retention destroys shareholder capital; wealth is maximized by distributing 100% of profits as dividends."
    },
    {
        "id": "quiz_fm_19",
        "subject_id": "mim501",
        "unit_no": 7,
        "difficulty": "easy",
        "type": "single_mcq",
        "question": "How is the Net Operating Cycle (Cash Conversion Cycle) calculated in working capital management?",
        "options": [
            "Raw Material Days + WIP Days + Finished Goods Days + Debtors Days - Creditors Deferral Days",
            "Total Current Assets minus Total Current Liabilities",
            "Annual Sales divided by Working Capital",
            "Inventory Days multiplied by Gross Margin"
        ],
        "correct_indices": [
            0
        ],
        "explanation": "The Net Operating Cycle measures the days cash is tied up in operations: Gross Operating Cycle minus supplier credit deferral days."
    },
    {
        "id": "quiz_fm_20",
        "subject_id": "mim501",
        "unit_no": 7,
        "difficulty": "medium",
        "type": "single_mcq",
        "question": "In the Economic Order Quantity (EOQ) inventory optimization model, at the optimal order quantity:",
        "options": [
            "Annual Ordering Costs exactly equal Annual Carrying (Holding) Costs.",
            "Carrying costs are zero.",
            "Ordering costs equal zero.",
            "Stockout risk is 100%."
        ],
        "correct_indices": [
            0
        ],
        "explanation": "EOQ = sqrt(2DS/H). At this point, the curves intersect and total annual ordering costs equal total annual carrying costs."
    },
    {
        "id": "quiz_fm_21",
        "subject_id": "mim501",
        "unit_no": 7,
        "difficulty": "hard",
        "type": "case_study",
        "question": "Case Application: A manufacturing enterprise has $1,000,000 annual cash requirements, transaction cost of $50 per conversion, and an opportunity interest rate of 8% on securities. Using Baumol's cash model C* = sqrt(2TF/i), what is the optimal cash conversion lot size?",
        "options": [
            "$35,355",
            "$50,000",
            "$12,500",
            "$80,000"
        ],
        "correct_indices": [
            0
        ],
        "explanation": "C* = sqrt( (2 * 1,000,000 * 50) / 0.08 ) = sqrt( 100,000,000 / 0.08 ) = sqrt( 1,250,000,000 ) = $35,355.34."
    }
]
