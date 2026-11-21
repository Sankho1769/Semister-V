# Java OOP (BCAC502) Lessons Generator
from generator.helper import create_topic

def get_java_modules():
    return [
        {
            "module_no": 1,
            "title": "Introduction to Java & JVM Architecture",
            "hours": 2,
            "marks": 5,
            "topics": [
                create_topic(
                    "java_m1_t1",
                    "Java Platform Independence and JVM Architecture",
                    ["Write Once Run Anywhere (WORA)", "JVM Subsystems", "ClassLoader Subsystem", "JIT Compiler", "Memory Areas"],
                    "Java is a high-level, class-based, object-oriented programming language designed for platform independence via the Java Virtual Machine (JVM).",
                    "Developed by James Gosling at Sun Microsystems in 1995 to overcome C++ platform-dependency and manual memory risks.",
                    "Forms the runtime backbone for enterprise enterprise architectures, Android applications, and distributed cloud computing systems.",
                    ["Explain the WORA paradigm and bytecode compilation.", "Trace JVM execution from ClassLoader to Execution Engine.", "Differentiate JVM memory areas (Heap, Stack, Method Area).", "Explain JIT optimization and Garbage Collection."],
                    "Java source code (.java) compiles to intermediate bytecode (.class) which the JVM executes across any underlying CPU architecture.",
                    [
                        ("Bytecode", "Intermediate non-machine-specific instruction set executed by the JVM."),
                        ("ClassLoader", "Subsystem responsible for loading, linking, and initializing .class binaries."),
                        ("JIT Compiler", "Just-In-Time compiler translating frequent bytecode hotspots directly into native machine code."),
                        ("Garbage Collector", "Automated background daemon reclaiming unreachable heap memory allocations.")
                    ],
                    "1. Platform Abstraction: Compile once to bytecode, execute on any OS with a compliant JVM.\n2. Safe Execution: Strict verification and memory isolation prevent unauthorized hardware access.",
                    "javac source.java -> Bytecode (.class) -> ClassLoader -> Execution Engine (Interpreter + JIT) -> Native OS.",
                    [
                        "1. Developer compiles Java source using javac compiler producing standardized bytecode.",
                        "2. Bootstrap, Extension, and Application ClassLoaders locate and verify class files.",
                        "3. Execution engine interprets bytecode instructions sequentially.",
                        "4. JIT compiler identifies hotspot loops and compiles them to native machine code.",
                        "5. Garbage Collector sweeps unreferenced heap objects asynchronously."
                    ],
                    ["Component", "Primary Responsibility", "Memory Storage / Scope"],
                    [
                        ["Method Area", "Class structures, method code, runtime constant pool", "Shared across all threads"],
                        ["Heap Area", "All instantiated objects and instance arrays", "Shared across all threads"],
                        ["JVM Stack", "Stack frames, local variables, method invocations", "Per-thread private memory"],
                        ["PC Register", "Address of current bytecode instruction executing", "Per-thread private memory"]
                    ],
                    "// JVM Entry Point\npublic class App {\n    public static void main(String[] args) {\n        System.out.println(\"Running on: \" + System.getProperty(\"java.vm.name\"));\n    }\n}",
                    """<svg viewBox='0 0 800 220' xmlns='http://www.w3.org/2000/svg' style='width:100%;height:auto;background:#fff;border-radius:8px;border:1px solid #E5E9F1;'><rect x='30' y='30' width='160' height='160' rx='8' fill='#F7F8FC' stroke='#377FE6'/><text x='110' y='60' font-family='sans-serif' font-size='12' font-weight='700' fill='#377FE6' text-anchor='middle'>Source Code</text><text x='110' y='95' font-family='monospace' font-size='11' fill='#19283D' text-anchor='middle'>Main.java</text><path d='M 110 120 L 110 145' stroke='#377FE6' stroke-width='2'/><text x='110' y='165' font-family='sans-serif' font-size='10' fill='#617087' text-anchor='middle'>javac Compiler</text><path d='M 195 110 L 255 110' stroke='#377FE6' stroke-width='2'/><rect x='260' y='30' width='160' height='160' rx='8' fill='#F7F8FC' stroke='#786CE5'/><text x='340' y='60' font-family='sans-serif' font-size='12' font-weight='700' fill='#786CE5' text-anchor='middle'>Java Bytecode</text><text x='340' y='95' font-family='monospace' font-size='11' fill='#19283D' text-anchor='middle'>Main.class</text><text x='340' y='135' font-family='sans-serif' font-size='10' fill='#617087' text-anchor='middle'>Platform Neutral</text><path d='M 425 110 L 485 110' stroke='#786CE5' stroke-width='2'/><rect x='490' y='20' width='280' height='180' rx='8' fill='#E9E8F8' stroke='#786CE5'/><text x='630' y='45' font-family='sans-serif' font-size='13' font-weight='700' fill='#19283D' text-anchor='middle'>Java Virtual Machine (JVM)</text><rect x='510' y='60' width='115' height='55' rx='4' fill='#FFF' stroke='#377FE6'/><text x='567' y='85' font-family='sans-serif' font-size='10' font-weight='700' fill='#377FE6' text-anchor='middle'>ClassLoader</text><text x='567' y='102' font-family='sans-serif' font-size='8' fill='#617087' text-anchor='middle'>Load/Link/Init</text><rect x='635' y='60' width='115' height='55' rx='4' fill='#FFF' stroke='#28A994'/><text x='692' y='85' font-family='sans-serif' font-size='10' font-weight='700' fill='#28A994' text-anchor='middle'>Execution Engine</text><text x='692' y='102' font-family='sans-serif' font-size='8' fill='#617087' text-anchor='middle'>Interpreter + JIT</text><rect x='510' y='125' width='240' height='60' rx='4' fill='#FFF' stroke='#F2C75C'/><text x='630' y='145' font-family='sans-serif' font-size='10' font-weight='700' fill='#19283D' text-anchor='middle'>JVM Memory Areas</text><text x='630' y='165' font-family='sans-serif' font-size='8' fill='#617087' text-anchor='middle'>Heap | Stack | Method Area | Native Registers</text></svg>""",
                    "Figure 1.1: Java Architecture from Bytecode Compilation to JVM Execution",
                    "Inspecting JVM Runtime Environment Details",
                    "public class JvmInspector {\n    public static void main(String[] args) {\n        Runtime rt = Runtime.getRuntime();\n        System.out.println(\"JVM Cores: \" + rt.availableProcessors());\n        System.out.println(\"Free Memory: \" + (rt.freeMemory() / 1024 / 1024) + \" MB\");\n        System.out.println(\"Max Memory: \" + (rt.maxMemory() / 1024 / 1024) + \" MB\");\n    }\n}",
                    [
                        "JDK contains tools (javac, debugger); JRE provides runtime libraries; JVM executes bytecode.",
                        "Bytecode format (.class) is standardized across all platforms.",
                        "JIT (Just-In-Time) compiler dynamically converts bytecode hotspots into native CPU code.",
                        "Heap memory is shared across threads; Stack memory is isolated per thread invocation.",
                        "Garbage Collector prevents memory leaks by reclaiming unreferenced allocations.",
                        "ClassLoader adheres to the delegation hierarchy: Bootstrap -> Platform -> Application."
                    ],
                    "Java achieves architecture neutrality through bytecode execution on the JVM, combining interpreter flexibility with JIT native performance.",
                    "Bytecode, ClassLoader, JIT Compiler, Garbage Collection, Stack, Heap.",
                    "Source (.java) -> javac -> Bytecode (.class) -> ClassLoader -> Execution Engine (JIT) -> OS Native instructions.",
                    "Assuming bytecode executes without a JVM, or confusing JDK with JRE."
                )
            ]
        },
        {
            "module_no": 2,
            "title": "Basics of Java Programming",
            "hours": 8,
            "marks": 10,
            "topics": [
                create_topic(
                    "java_m2_t1",
                    "Data Types, Variables, Type Casting, and Operators in Java",
                    ["Primitive vs Reference Types", "Implicit & Explicit Casting", "Arithmetic & Bitwise Operators", "Operator Precedence"],
                    "Java data types define the size, format, and behavior of in-memory values, categorized into 8 primitive types and reference objects.",
                    "Inherited from C/C++ syntactic conventions but designed with strictly enforced bit-widths independent of underlying OS hardware.",
                    "Ensures cross-platform computational consistency and prevents low-level buffer and sign overflow bugs.",
                    ["Categorize Java's 8 primitive types and their bit widths.", "Execute safe widening and deliberate narrowing type casting.", "Apply relational, logical, and bitwise operators.", "Solve operator precedence in complex mathematical expressions."],
                    "Variables reserve memory locations. Strongly typed syntax mandates explicit variable type declaration prior to memory allocation.",
                    [
                        ("Primitive Type", "Predefined byte, short, int, long, float, double, char, boolean storing raw values."),
                        ("Reference Type", "Objects, arrays, and interfaces storing heap memory addresses."),
                        ("Widening Casting", "Automatic type conversion from smaller to larger data types (e.g., int to double)."),
                        ("Narrowing Casting", "Manual explicit conversion from larger to smaller data types requiring cast syntax.")
                    ],
                    "1. Strong Typing: Type mismatches trigger compile-time errors.\n2. Fixed Bit Width: int is guaranteed 32-bit two's complement across every OS.",
                    "int x = 10; -> Widening: double d = x; -> Narrowing: int y = (int) d; -> Bitwise: int z = x & 1;",
                    [
                        "1. Variable identifier declared with specific type specifier.",
                        "2. JVM allocates fixed stack memory for primitive or reference pointer.",
                        "3. Expressions evaluated according to strict operator precedence rules.",
                        "4. Narrowing casts truncate high-order bits without runtime warning."
                    ],
                    ["Type", "Size in Bits", "Range / Format", "Default Value"],
                    [
                        ["byte", "8 bits", "-128 to 127", "0"],
                        ["int", "32 bits", "-2^31 to 2^31 - 1", "0"],
                        ["double", "64 bits", "IEEE 754 floating point", "0.0d"],
                        ["boolean", "1 bit (logical)", "true or false", "false"]
                    ],
                    "// Type conversion and bitwise operations\nint a = 130;\nbyte b = (byte) a; // Overflows to -126 due to two's complement\nSystem.out.println(b);",
                    """<svg viewBox='0 0 800 180' xmlns='http://www.w3.org/2000/svg' style='width:100%;height:auto;background:#fff;border-radius:8px;border:1px solid #E5E9F1;'><rect x='30' y='30' width='340' height='120' rx='8' fill='#F7F8FC' stroke='#377FE6'/><text x='200' y='60' font-family='sans-serif' font-size='12' font-weight='700' fill='#377FE6' text-anchor='middle'>Primitive Types (Stack)</text><text x='50' y='90' font-family='monospace' font-size='11' fill='#19283D'>int age = 22; (32-bit)</text><text x='50' y='115' font-family='monospace' font-size='11' fill='#19283D'>double gpa = 3.85; (64-bit)</text><path d='M 380 90 L 440 90' stroke='#786CE5' stroke-width='2'/><rect x='450' y='30' width='320' height='120' rx='8' fill='#F7F8FC' stroke='#786CE5'/><text x='610' y='60' font-family='sans-serif' font-size='12' font-weight='700' fill='#786CE5' text-anchor='middle'>Reference Types (Heap Pointer)</text><text x='470' y='90' font-family='monospace' font-size='11' fill='#19283D'>String name = &quot;MAKAUT&quot;;</text><text x='470' y='115' font-family='monospace' font-size='11' fill='#617087'>Stack holds reference -> Heap holds data</text></svg>""",
                    "Figure 2.1: Memory Allocation for Java Primitive vs Reference Types",
                    "Demonstrating Safe Type Conversion and Precedence",
                    "public class TypeCastDemo {\n    public static void main(String[] args) {\n        int score = 85;\n        double normalized = (double) score / 100.0;\n        System.out.println(\"Normalized: \" + normalized);\n    }\n}",
                    [
                        "Java features 8 primitives: byte, short, int, long, float, double, char, boolean.",
                        "Primitive values are stored directly on the execution stack.",
                        "Widening conversions (byte -> short -> int -> long -> float -> double) occur automatically.",
                        "Narrowing conversions require explicit casting and may cause data loss or sign reversal.",
                        "Java does not support pointer arithmetic or direct memory addressing for security.",
                        "The ternary operator (cond ? val1 : val2) provides concise branch selection."
                    ],
                    "Java strictly enforces static typing and platform-independent bit widths for all primitive types.",
                    "Primitive, Reference, Widening, Narrowing, Two's Complement, Stack Allocation.",
                    "Declaration -> Type Allocation -> Implicit Widening / Explicit Narrowing -> Expression Evaluation.",
                    "Integer division truncation: `int r = 5 / 2;` evaluates to 2 instead of 2.5."
                ),
                create_topic(
                    "java_m2_t2",
                    "Control Statements: Selection, Iteration, and Jump Statements",
                    ["if-else & switch-case", "Enhanced switch (Java 14+)", "for, while, do-while Loops", "break, continue, return"],
                    "Control statements regulate the sequential execution path of Java programs based on boolean condition evaluations.",
                    "Fundamental paradigm of imperative programming implemented in Java with structured branching and loop safeguards.",
                    "Enables complex business logic, input validation algorithms, data searching, and processing workflows.",
                    ["Implement conditional branching using if-else and switch statements.", "Formulate iterative computations using for, while, and do-while loops.", "Apply break and continue with labeled statements for deep loop control.", "Utilize enhanced switch expressions."],
                    "Execution flows line-by-line unless diverted by selection (if/switch), repetition (loops), or jump statements.",
                    [
                        ("Selection", "Branching mechanism executing specific blocks based on condition evaluation."),
                        ("Iteration", "Loop construct repeating execution until termination condition is met."),
                        ("Jump Statement", "Directs control immediately to break out of loops or skip iterations.")
                    ],
                    "1. Boolean Strictness: Java conditions require strict boolean expressions (integers like `if(1)` are invalid).\n2. Fall-through: Classic switch statements fall through cases unless explicitly halted by `break`.",
                    "if (x > 0) { ... } else { ... } | switch(val) { case 1: ... break; } | for (int i=0; i<n; i++) { ... }",
                    [
                        "1. Expression evaluates to true or false.",
                        "2. Control branches to the matching block.",
                        "3. In loops, the condition is evaluated at entrance (for, while) or exit (do-while).",
                        "4. `break` terminates the loop; `continue` skips to the next iteration."
                    ],
                    ["Statement", "Evaluation Timing", "Guaranteed Iterations", "Primary Use Case"],
                    [
                        ["while", "Pre-test (entrance)", "0 times", "Indeterminate loop count"],
                        ["do-while", "Post-test (exit)", "At least 1 time", "Menu-driven CLI programs"],
                        ["for", "Pre-test (entrance)", "0 times", "Determinate index iteration"],
                        ["switch", "Value matching", "1 match (or default)", "Multi-branch discrete matching"]
                    ],
                    "// Labeled break demonstration\nouter: for (int i = 0; i < 5; i++) {\n    for (int j = 0; j < 5; j++) {\n        if (i * j > 6) break outer;\n    }\n}",
                    """<svg viewBox='0 0 800 180' xmlns='http://www.w3.org/2000/svg' style='width:100%;height:auto;background:#fff;border-radius:8px;border:1px solid #E5E9F1;'><polygon points='180,30 280,90 180,150 80,90' fill='#F7F8FC' stroke='#377FE6' stroke-width='2'/><text x='180' y='95' font-family='sans-serif' font-size='11' font-weight='700' fill='#377FE6' text-anchor='middle'>Condition ?</text><path d='M 280 90 L 380 90' stroke='#369B72' stroke-width='2'/><text x='330' y='80' font-family='sans-serif' font-size='10' font-weight='700' fill='#369B72'>TRUE</text><rect x='385' y='60' width='160' height='60' rx='6' fill='#F7F8FC' stroke='#369B72'/><text x='465' y='95' font-family='sans-serif' font-size='11' font-weight='700' fill='#369B72' text-anchor='middle'>Execute Action A</text><path d='M 180 150 L 180 170 L 630 170 L 630 125' stroke='#D65F64' stroke-width='2'/><text x='250' y='165' font-family='sans-serif' font-size='10' font-weight='700' fill='#D65F64'>FALSE</text><rect x='580' y='60' width='160' height='60' rx='6' fill='#F7F8FC' stroke='#D65F64'/><text x='660' y='95' font-family='sans-serif' font-size='11' font-weight='700' fill='#D65F64' text-anchor='middle'>Execute Action B</text></svg>""",
                    "Figure 2.2: Structured Conditional Branching Architecture",
                    "Enhanced Pattern Matching Switch in Java",
                    "public class GradeEvaluator {\n    public static String getFeedback(char grade) {\n        return switch (grade) {\n            case 'A', 'E' -> \"Excellent performance\";\n            case 'B' -> \"Commendable performance\";\n            case 'C' -> \"Average performance\";\n            default -> \"Remedial attention required\";\n        };\n    }\n}",
                    [
                        "Java conditions require explicit boolean values, unlike C/C++ which permit integers.",
                        "Enhanced switch expressions (`->`) eliminate accidental fall-through bugs.",
                        "The `do-while` loop evaluates the condition at the end, executing at least once.",
                        "Labeled `break` and `continue` allow breaking out of deeply nested loop matrices.",
                        "Modern Java allows `switch` statements on String and enum data types.",
                        "Loop counter increments occur after statement execution in standard `for` loops."
                    ],
                    "Java control flow statements govern program paths via strict boolean-evaluated conditions and bounded iterations.",
                    "Selection, Iteration, switch-case, Labeled Break, Fall-through.",
                    "Condition Evaluation -> Branch Selection -> Loop Iteration / Termination.",
                    "Omitting `break` in classic switch statements resulting in unintended cascade execution."
                )
            ]
        },
        {
            "module_no": 3,
            "title": "Object-Oriented Programming Concepts",
            "hours": 6,
            "marks": 8,
            "topics": [
                create_topic(
                    "java_m3_t1",
                    "Classes, Objects, Constructors, and the 'this' Keyword",
                    ["Class Blueprint vs Object Instance", "Default & Parameterized Constructors", "Constructor Overloading", "this Keyword Usage", "Access Modifiers"],
                    "A class is a user-defined blueprint from which individual object instances are created, encapsulating state (fields) and behavior (methods).",
                    "Developed as the foundational paradigm of object-oriented design by Alan Kay and standardized in Java.",
                    "Provides modular abstraction, data encapsulation, and high maintainability in complex software development.",
                    ["Construct classes encapsulating private state and public accessors.", "Instantiate objects dynamically using the new keyword.", "Design overloaded constructors with constructor chaining via this().", "Apply appropriate access modifiers (private, default, protected, public)."],
                    "Objects reside on the JVM Heap. Variables store references pointing to these heap allocations.",
                    [
                        ("Class", "Template defining fields and methods for instances."),
                        ("Object", "Concrete runtime instance allocated on the JVM heap."),
                        ("Constructor", "Special method invoked during new instantiation to initialize state."),
                        ("this Keyword", "Reference to the current executing object instance.")
                    ],
                    "1. Encapsulation: Keep instance variables private; expose controlled access via public getters and setters.\n2. Constructor Identity: Constructor shares the exact class name and possesses no return type.",
                    "Class declaration -> Constructor definition -> new Operator invocation -> Heap allocation -> Reference assignment.",
                    [
                        "1. `new Student()` allocates memory on the JVM heap.",
                        "2. Default values (0, null, false) initialize fields.",
                        "3. Constructor executes to assign parameter values.",
                        "4. Constructor returns reference address assigned to stack reference variable."
                    ],
                    ["Access Modifier", "Within Class", "Within Package", "Outside via Subclass", "Everywhere"],
                    [
                        ["private", "Yes", "No", "No", "No"],
                        ["default (no keyword)", "Yes", "Yes", "No", "No"],
                        ["protected", "Yes", "Yes", "Yes", "No"],
                        ["public", "Yes", "Yes", "Yes", "Yes"]
                    ],
                    "public class Student {\n    private int roll;\n    private String name;\n    public Student(int roll, String name) {\n        this.roll = roll;\n        this.name = name;\n    }\n}",
                    """<svg viewBox='0 0 800 180' xmlns='http://www.w3.org/2000/svg' style='width:100%;height:auto;background:#fff;border-radius:8px;border:1px solid #E5E9F1;'><rect x='40' y='30' width='280' height='120' rx='8' fill='#F7F8FC' stroke='#377FE6'/><text x='180' y='60' font-family='sans-serif' font-size='12' font-weight='700' fill='#377FE6' text-anchor='middle'>Stack Memory</text><text x='60' y='95' font-family='monospace' font-size='11' fill='#19283D'>Student s1 = 0x4A1F</text><text x='60' y='125' font-family='sans-serif' font-size='10' fill='#617087'>Stores 64-bit reference address</text><path d='M 325 90 L 440 90' stroke='#377FE6' stroke-width='2' stroke-dasharray='4,4'/><rect x='450' y='30' width='310' height='120' rx='8' fill='#F7F8FC' stroke='#786CE5'/><text x='605' y='60' font-family='sans-serif' font-size='12' font-weight='700' fill='#786CE5' text-anchor='middle'>Heap Memory (0x4A1F)</text><text x='480' y='90' font-family='monospace' font-size='11' fill='#19283D'>roll: 101</text><text x='480' y='110' font-family='monospace' font-size='11' fill='#19283D'>name: &quot;Rahul Ghosh&quot;</text><text x='480' y='130' font-family='sans-serif' font-size='9' fill='#28A994'>Class Metadata Pointer</text></svg>""",
                    "Figure 3.1: Stack Reference Pointing to Heap Allocated Object Instance",
                    "Constructor Chaining Using this()",
                    "public class Account {\n    private String id;\n    private double balance;\n    public Account() {\n        this(\"ACC-DEFAULT\", 0.0); // Constructor chaining\n    }\n    public Account(String id, double balance) {\n        this.id = id;\n        this.balance = balance;\n    }\n}",
                    [
                        "A class defines the blueprint; an object is a distinct runtime realization on the heap.",
                        "Constructors initialize newly created objects and have no return type.",
                        "If no constructor is defined, the Java compiler provides a default no-argument constructor.",
                        "`this()` allows constructor chaining and must be the very first line of a constructor.",
                        "Encapsulation protects internal object state by declaring fields private with public methods.",
                        "Access modifiers control visibility: private, default (package-private), protected, and public."
                    ],
                    "Classes establish structured types; objects encapsulate state and operations with controlled exposure.",
                    "Class, Object, Constructor Chaining, this Keyword, Encapsulation, Access Modifiers.",
                    "Class Blueprint -> new Memory Allocation -> Constructor Initialization -> Heap Reference.",
                    "Declaring a return type on a constructor (e.g., `public void Student()`), which turns it into a regular method."
                )
            ]
        },
        {
            "module_no": 4,
            "title": "Inheritance and Polymorphism",
            "hours": 6,
            "marks": 10,
            "topics": [
                create_topic(
                    "java_m4_t1",
                    "Inheritance, Method Overriding, super Keyword, and Dynamic Dispatch",
                    ["Single & Multilevel Inheritance", "Method Overriding vs Overloading", "super() Constructor & Method Invocation", "Dynamic Method Dispatch", "final Keyword"],
                    "Inheritance enables a subclass to inherit state and behaviors from a superclass using the extends keyword, while polymorphism permits a single interface to control different underlying implementations.",
                    "Core foundation of object-oriented reuse derived from Simula 67 and perfected in Java.",
                    "Eliminates boilerplate code redundancy and enables extensible plugin architectures via dynamic dispatch.",
                    ["Implement class hierarchies using extends and super.", "Differentiate compile-time polymorphism (overloading) from runtime polymorphism (overriding).", "Demonstrate dynamic method dispatch using superclass references to subclass objects.", "Prevent inheritance and overriding using the final keyword."],
                    "Subclasses gain access to non-private fields and methods of the superclass. Method overriding replaces superclass behavior dynamically.",
                    [
                        ("Inheritance", "Mechanism where a new class derives properties from an existing parent class."),
                        ("Method Overriding", "Redefining a superclass method in a subclass with identical signature."),
                        ("Dynamic Dispatch", "Runtime resolution of overridden method calls based on the actual object type."),
                        ("final Keyword", "Restricts modification: final variables are constants; final methods cannot be overridden; final classes cannot be extended.")
                    ],
                    "1. Is-A Relationship: Subclass must represent an 'is-a' specialization of the superclass.\n2. Covariant Return Types: Overridden methods may return a subclass of the superclass return type.",
                    "Parent p = new Child(); -> p.display(); -> JVM inspects actual heap object -> Child.display() executed.",
                    [
                        "1. JVM resolves method call via virtual method table (vtable).",
                        "2. Stack reference type verified at compile time.",
                        "3. At runtime, JVM dereferences reference pointer to heap object.",
                        "4. Executes the overriding implementation in the concrete child class."
                    ],
                    ["Feature", "Method Overloading", "Method Overriding"],
                    [
                        ["Resolution Phase", "Compile time (Static Binding)", "Runtime (Dynamic Binding)"],
                        ["Method Signature", "Same name, different parameter list", "Identical name and identical parameters"],
                        ["Scope", "Within same class (or inherited)", "Between superclass and subclass"],
                        ["Return Type", "Can vary arbitrarily", "Must be identical or covariant"]
                    ],
                    "// Dynamic Method Dispatch\nclass Animal { void sound() { System.out.println(\"Generic sound\"); } }\nclass Dog extends Animal { void sound() { System.out.println(\"Bark\"); } }\nAnimal a = new Dog();\na.sound(); // Output: Bark",
                    """<svg viewBox='0 0 800 180' xmlns='http://www.w3.org/2000/svg' style='width:100%;height:auto;background:#fff;border-radius:8px;border:1px solid #E5E9F1;'><rect x='60' y='30' width='220' height='70' rx='8' fill='#F7F8FC' stroke='#377FE6'/><text x='170' y='55' font-family='sans-serif' font-size='12' font-weight='700' fill='#377FE6' text-anchor='middle'>Superclass: Animal</text><text x='170' y='80' font-family='monospace' font-size='11' fill='#19283D' text-anchor='middle'>void makeSound()</text><path d='M 170 105 L 170 120 L 400 120 L 400 105' stroke='#786CE5' stroke-width='2'/><polygon points='170,105 165,115 175,115' fill='#786CE5'/><rect x='300' y='30' width='200' height='70' rx='8' fill='#F7F8FC' stroke='#786CE5'/><text x='400' y='55' font-family='sans-serif' font-size='12' font-weight='700' fill='#786CE5' text-anchor='middle'>Subclass: Dog</text><text x='400' y='80' font-family='monospace' font-size='11' fill='#28A994' text-anchor='middle'>@Override makeSound()</text><rect x='540' y='30' width='230' height='120' rx='8' fill='#E9E8F8' stroke='#28A994'/><text x='655' y='60' font-family='sans-serif' font-size='11' font-weight='700' fill='#1B6F61' text-anchor='middle'>Dynamic Method Dispatch</text><text x='655' y='90' font-family='monospace' font-size='10' fill='#19283D' text-anchor='middle'>Animal ref = new Dog();</text><text x='655' y='110' font-family='monospace' font-size='10' fill='#19283D' text-anchor='middle'>ref.makeSound();</text><text x='655' y='135' font-family='sans-serif' font-size='10' font-weight='700' fill='#28A994' text-anchor='middle'>-> Executes Dog.makeSound()</text></svg>""",
                    "Figure 4.1: Dynamic Method Dispatch and Inheritance Hierarchy",
                    "Calling Superclass Constructor with super()",
                    "class Employee {\n    protected double basic;\n    public Employee(double basic) { this.basic = basic; }\n}\nclass Manager extends Employee {\n    private double allowance;\n    public Manager(double basic, double allowance) {\n        super(basic); // Invokes superclass constructor\n        this.allowance = allowance;\n    }\n}",
                    [
                        "Java supports single class inheritance and multilevel inheritance, but avoids multiple class inheritance to prevent diamond ambiguity.",
                        "The `super` keyword refers to immediate superclass constructors and methods.",
                        "Method overriding provides polymorphic dynamic dispatch decided at runtime.",
                        "The `@Override` annotation ensures compiler validation of matching signatures.",
                        "A `final` class cannot be extended; a `final` method cannot be overridden.",
                        "Private and static methods cannot be overridden in Java."
                    ],
                    "Inheritance establishes hierarchical relationships and dynamic method dispatch enables polymorphic extensibility.",
                    "Inheritance, Dynamic Method Dispatch, super, Method Overriding, vtable, final.",
                    "Compile-time reference type check -> Runtime vtable inspection -> Concrete method dispatch.",
                    "Attempting to override private or static methods; static methods hide rather than override."
                )
            ]
        },
        {
            "module_no": 5,
            "title": "Arrays and Strings",
            "hours": 6,
            "marks": 8,
            "topics": [
                create_topic(
                    "java_m5_t1",
                    "Arrays, String Immutability, String Pool, StringBuffer and StringBuilder",
                    ["Array Allocation and Bounds", "String Immutability Concept", "String Constant Pool (SCP)", "StringBuffer vs StringBuilder", "Useful String Methods"],
                    "In Java, an array is an indexed object storing homogeneous elements, while a String is an immutable sequence of Unicode characters backed by an internal byte/char array.",
                    "Java designed Strings to be immutable for security, thread safety, and memory optimization via the String Constant Pool.",
                    "Essential for memory efficiency, network protocols, caching mechanisms, and concurrent programming.",
                    ["Allocate single and multidimensional arrays with bounds verification.", "Explain String immutability and its architectural benefits.", "Trace String Constant Pool memory reuse.", "Choose between String, StringBuffer (thread-safe), and StringBuilder (high-speed)."],
                    "Arrays are instantiated with fixed length. String literals are stored in the String Constant Pool inside heap memory; new String() forces separate heap allocation.",
                    [
                        ("String Pool", "Special cache memory in heap storing unique string literals."),
                        ("Immutability", "Condition where internal state cannot be modified after object construction."),
                        ("StringBuffer", "Mutable, thread-safe sequence of characters with synchronized methods."),
                        ("StringBuilder", "Mutable, non-thread-safe sequence optimized for maximum single-threaded performance.")
                    ],
                    "1. Memory Reuse: Identical string literals share a single pool instance.\n2. Safe HashCode: Immutability enables caching of hashCode, making Strings ideal HashMap keys.",
                    "String s1 = &quot;Makaut&quot;; String s2 = &quot;Makaut&quot;; // s1 == s2 is true (shared pool reference)",
                    [
                        "1. JVM checks String Constant Pool for existing literal match.",
                        "2. If present, returns existing memory address.",
                        "3. If absent, allocates new literal instance in SCP.",
                        "4. `new String(&quot;Makaut&quot;)` forces duplicate instance in general heap."
                    ],
                    ["Feature", "String", "StringBuffer", "StringBuilder"],
                    [
                        ["Mutability", "Immutable", "Mutable", "Mutable"],
                        ["Thread Safety", "Thread-safe (Immutable)", "Thread-safe (Synchronized)", "Not Thread-safe"],
                        ["Performance", "Slow for concatenation", "Moderate", "Fastest"],
                        ["Memory Storage", "String Pool / Heap", "Heap", "Heap"]
                    ],
                    "// String concatenation vs StringBuilder\nStringBuilder sb = new StringBuilder();\nfor(int i = 0; i < 1000; i++) { sb.append(i); } // Highly efficient\nString result = sb.toString();",
                    """<svg viewBox='0 0 800 180' xmlns='http://www.w3.org/2000/svg' style='width:100%;height:auto;background:#fff;border-radius:8px;border:1px solid #E5E9F1;'><rect x='40' y='30' width='320' height='120' rx='8' fill='#F7F8FC' stroke='#377FE6'/><text x='200' y='55' font-family='sans-serif' font-size='12' font-weight='700' fill='#377FE6' text-anchor='middle'>Stack Variables</text><text x='60' y='90' font-family='monospace' font-size='11' fill='#19283D'>String s1 = &quot;WBUT&quot;;</text><text x='60' y='115' font-family='monospace' font-size='11' fill='#19283D'>String s2 = &quot;WBUT&quot;;</text><text x='60' y='140' font-family='monospace' font-size='11' fill='#786CE5'>String s3 = new String(&quot;WBUT&quot;);</text><path d='M 240 90 L 460 70' stroke='#377FE6' stroke-width='2'/><path d='M 240 115 L 460 70' stroke='#377FE6' stroke-width='2'/><path d='M 280 140 L 460 135' stroke='#786CE5' stroke-width='2'/><rect x='460' y='30' width='310' height='120' rx='8' fill='#E9E8F8' stroke='#786CE5'/><rect x='480' y='50' width='270' height='40' rx='4' fill='#FFF' stroke='#377FE6'/><text x='615' y='75' font-family='sans-serif' font-size='11' font-weight='700' fill='#377FE6' text-anchor='middle'>String Constant Pool: &quot;WBUT&quot;</text><rect x='480' y='110' width='270' height='35' rx='4' fill='#FFF' stroke='#786CE5'/><text x='615' y='133' font-family='sans-serif' font-size='10' fill='#786CE5' text-anchor='middle'>Regular Heap Object: &quot;WBUT&quot;</text></svg>""",
                    "Figure 5.1: String Constant Pool vs Heap Object Allocation",
                    "Comparing Equality: == vs .equals()",
                    "public class StringEqualityDemo {\n    public static void main(String[] args) {\n        String a = \"Java\";\n        String b = new String(\"Java\");\n        System.out.println(a == b);      // false (distinct memory references)\n        System.out.println(a.equals(b));  // true (identical character contents)\n    }\n}",
                    [
                        "Java arrays are indexed objects with fixed `.length` property.",
                        "Accessing indices beyond array bounds throws `ArrayIndexOutOfBoundsException`.",
                        "Strings are immutable; modification operations return new String instances.",
                        "String literals are stored in the String Constant Pool to conserve heap memory.",
                        "Use `==` to compare memory references; use `.equals()` to compare character content.",
                        "`StringBuilder` is preferred for single-threaded string construction due to absence of synchronization overhead."
                    ],
                    "Arrays store indexed homogeneous sequences; Strings are immutable objects backed by the String Pool.",
                    "Array, String Pool, Immutability, equals(), StringBuffer, StringBuilder.",
                    "Literal Declaration -> Pool Lookup -> Heap Pointer Assignment -> Immutability Enforcement.",
                    "Using `==` to compare String values instead of the `.equals()` method."
                )
            ]
        },
        {
            "module_no": 6,
            "title": "Interfaces and Abstract Classes",
            "hours": 4,
            "marks": 7,
            "topics": [
                create_topic(
                    "java_m6_t1",
                    "Abstract Classes, Interfaces, and Multiple Inheritance in Java",
                    ["abstract Classes vs Interfaces", "Interface Implementation", "Multiple Inheritance via Interfaces", "default and static Methods in Interfaces", "Functional Interfaces"],
                    "An abstract class is a restricted class that cannot be instantiated and may contain abstract and concrete methods, whereas an interface is a contract defining abstract behavior that implementing classes must satisfy.",
                    "Created to separate specification from implementation and provide multiple inheritance of type without C++ diamond ambiguity.",
                    "Serves as the architectural foundation for clean API contracts, dependency inversion, and enterprise design patterns.",
                    ["Design abstract base classes with abstract and template methods.", "Implement multiple interfaces in a single class.", "Utilize default and static methods in Java 8+ interfaces.", "Apply functional interfaces with lambda expressions."],
                    "A class can extend only one superclass (single inheritance) but can implement multiple interfaces (`implements A, B`).",
                    [
                        ("Abstract Class", "Class declared with abstract keyword; can possess state and constructors."),
                        ("Interface", "Pure specification contract whose methods are public abstract by default."),
                        ("default Method", "Interface method with default implementation introduced in Java 8."),
                        ("Marker Interface", "Empty interface (e.g., Serializable) conveying runtime metadata to the JVM.")
                    ],
                    "1. Program to Interfaces: Declare variables using interface types to allow swappable implementations.\n2. Diamond Resolution: If two interfaces have identical default methods, the implementing class must explicitly override and resolve.",
                    "interface Printable { void print(); } | interface Showable { void show(); } | class Doc implements Printable, Showable { ... }",
                    [
                        "1. Class declares implemented interfaces via `implements`.",
                        "2. Compiler validates that all non-default interface methods are fully overridden.",
                        "3. Instances can be assigned to references of any implemented interface type."
                    ],
                    ["Comparison Criterion", "Abstract Class", "Interface"],
                    [
                        ["Inheritance Model", "Single inheritance (extends)", "Multiple inheritance (implements)"],
                        ["Field Variables", "Can have instance and static fields", "Only public static final constants"],
                        ["Constructors", "Can define constructors", "Cannot have constructors"],
                        ["Method Types", "Abstract, concrete, final, static", "Abstract, default, static, private"]
                    ],
                    "interface PaymentGateway {\n    void processPayment(double amount);\n    default void logTransaction(String id) {\n        System.out.println(\"Logged txn: \" + id);\n    }\n}",
                    """<svg viewBox='0 0 800 180' xmlns='http://www.w3.org/2000/svg' style='width:100%;height:auto;background:#fff;border-radius:8px;border:1px solid #E5E9F1;'><rect x='60' y='30' width='200' height='60' rx='8' fill='#F7F8FC' stroke='#377FE6'/><text x='160' y='55' font-family='sans-serif' font-size='12' font-weight='700' fill='#377FE6' text-anchor='middle'>&lt;&lt;interface&gt;&gt;</text><text x='160' y='75' font-family='sans-serif' font-size='11' fill='#19283D' text-anchor='middle'>Printable</text><rect x='340' y='30' width='200' height='60' rx='8' fill='#F7F8FC' stroke='#786CE5'/><text x='440' y='55' font-family='sans-serif' font-size='12' font-weight='700' fill='#786CE5' text-anchor='middle'>&lt;&lt;interface&gt;&gt;</text><text x='440' y='75' font-family='sans-serif' font-size='11' fill='#19283D' text-anchor='middle'>Exportable</text><path d='M 160 90 L 290 130' stroke='#377FE6' stroke-width='2' stroke-dasharray='4,4'/><path d='M 440 90 L 310 130' stroke='#786CE5' stroke-width='2' stroke-dasharray='4,4'/><rect x='200' y='125' width='200' height='45' rx='6' fill='#F7F8FC' stroke='#28A994'/><text x='300' y='152' font-family='sans-serif' font-size='11' font-weight='700' fill='#28A994' text-anchor='middle'>Invoice (implements both)</text></svg>""",
                    "Figure 6.1: Multiple Interface Implementation Architecture",
                    "Resolving Conflicting Default Methods",
                    "interface A { default void hello() { System.out.println(\"Hello from A\"); } }\ninterface B { default void hello() { System.out.println(\"Hello from B\"); } }\nclass Demo implements A, B {\n    public void hello() {\n        A.super.hello(); // Disambiguates diamond conflict\n    }\n}",
                    [
                        "Abstract classes cannot be instantiated with the `new` operator.",
                        "A class can extend only one class, but can implement unlimited interfaces.",
                        "Interface fields are implicitly `public static final` constants.",
                        "Java 8 introduced `default` and `static` methods to support interface backward compatibility.",
                        "Java 9 permitted `private` helper methods inside interfaces.",
                        "Interfaces with exactly one abstract method qualify as Functional Interfaces for Lambdas."
                    ],
                    "Interfaces establish pure contracts supporting multiple inheritance of type, whereas abstract classes provide partial implementations.",
                    "Interface, Abstract Class, Multiple Inheritance, default Method, Contract.",
                    "Contract Specification -> Class Implementation -> Method Override Validation -> Interface Reference Dispatch.",
                    "Attempting to instantiate an interface directly with `new InterfaceName()` without an anonymous inner class."
                )
            ]
        },
        {
            "module_no": 7,
            "title": "Exception Handling",
            "hours": 4,
            "marks": 8,
            "topics": [
                create_topic(
                    "java_m7_t1",
                    "Exception Hierarchy, try-catch-finally, throws, and Custom Exceptions",
                    ["Throwable Hierarchy (Error vs Exception)", "Checked vs Unchecked Exceptions", "try-catch-finally Flow", "try-with-resources", "Custom Exception Development"],
                    "Exception handling is a structured mechanism in Java to intercept runtime abnormalities and maintain graceful program execution flow without unexpected JVM termination.",
                    "Engineered to separate error-handling code from regular business logic, superseding C-style error return codes.",
                    "Crucial for high-availability enterprise services, financial transaction systems, and network communication resilience.",
                    ["Navigate the java.lang.Throwable inheritance hierarchy.", "Differentiate checked (compile-time) and unchecked (runtime) exceptions.", "Implement try-catch-finally and modern try-with-resources blocks.", "Throw and declare exceptions using throw and throws.", "Author domain-specific custom exception classes."],
                    "All exceptions inherit from `Throwable`. Errors represent unrecoverable JVM faults; Exceptions represent recoverable program conditions.",
                    [
                        ("Checked Exception", "Subclasses of Exception (excluding RuntimeException) verified at compile-time."),
                        ("Unchecked Exception", "Subclasses of RuntimeException caused by programming defects (e.g., NullPointerException)."),
                        ("finally Block", "Guaranteed execution block following try-catch regardless of exception occurrence."),
                        ("try-with-resources", "Auto-closes AutoCloseable resources automatically at block completion.")
                    ],
                    "1. Fail Fast: Throw descriptive exceptions at the point of failure.\n2. Catch Specificity: Catch specific subclasses before broader parent exception classes.",
                    "try { riskyOperation(); } catch (SpecificException e) { handle(); } finally { cleanup(); }",
                    [
                        "1. Runtime anomaly triggers creation of Exception object on heap.",
                        "2. Normal control flow suspended; JVM searches stack for matching catch block.",
                        "3. Matching catch block executes exception handling logic.",
                        "4. `finally` block executes before control exits method.",
                        "5. If unhandled, uncaught exception handler prints stack trace and terminates thread."
                    ],
                    ["Category", "Superclass", "Checked by Compiler?", "Typical Examples"],
                    [
                        ["Error", "java.lang.Error", "No", "OutOfMemoryError, StackOverflowError"],
                        ["Checked Exception", "java.lang.Exception", "Yes", "IOException, SQLException, ClassNotFoundException"],
                        ["Unchecked Exception", "java.lang.RuntimeException", "No", "NullPointerException, ArithmeticException, IndexOutOfBoundsException"]
                    ],
                    "// Custom Domain Exception\nclass InsufficientBalanceException extends Exception {\n    public InsufficientBalanceException(String msg) { super(msg); }\n}\npublic void withdraw(double amt) throws InsufficientBalanceException {\n    if (amt > balance) throw new InsufficientBalanceException(\"Overdraft denied\");\n}",
                    """<svg viewBox='0 0 800 200' xmlns='http://www.w3.org/2000/svg' style='width:100%;height:auto;background:#fff;border-radius:8px;border:1px solid #E5E9F1;'><rect x='300' y='20' width='200' height='40' rx='6' fill='#F7F8FC' stroke='#377FE6'/><text x='400' y='45' font-family='sans-serif' font-size='12' font-weight='700' fill='#377FE6' text-anchor='middle'>Throwable</text><path d='M 350 60 L 220 90' stroke='#D65F64' stroke-width='2'/><path d='M 450 60 L 580 90' stroke='#377FE6' stroke-width='2'/><rect x='120' y='90' width='200' height='40' rx='6' fill='#FFF2EB' stroke='#D65F64'/><text x='220' y='115' font-family='sans-serif' font-size='12' font-weight='700' fill='#D65F64' text-anchor='middle'>Error (Unrecoverable)</text><rect x='480' y='90' width='200' height='40' rx='6' fill='#F7F8FC' stroke='#377FE6'/><text x='580' y='115' font-family='sans-serif' font-size='12' font-weight='700' fill='#377FE6' text-anchor='middle'>Exception (Recoverable)</text><path d='M 530 130 L 460 155' stroke='#28A994' stroke-width='2'/><path d='M 630 130 L 700 155' stroke='#F2C75C' stroke-width='2'/><rect x='360' y='155' width='200' height='35' rx='4' fill='#FFF' stroke='#28A994'/><text x='460' y='178' font-family='sans-serif' font-size='10' font-weight='700' fill='#1B6F61' text-anchor='middle'>Checked (IOException)</text><rect x='600' y='155' width='190' height='35' rx='4' fill='#FFF' stroke='#F2C75C'/><text x='695' y='178' font-family='sans-serif' font-size='10' font-weight='700' fill='#19283D' text-anchor='middle'>RuntimeException (Unchecked)</text></svg>""",
                    "Figure 7.1: Java Throwable Hierarchy Structure",
                    "Automated Resource Cleanup with try-with-resources",
                    "import java.io.*;\npublic class ResourceDemo {\n    public static void readHeader(String path) {\n        try (BufferedReader br = new BufferedReader(new FileReader(path))) {\n            System.out.println(br.readLine());\n        } catch (IOException e) {\n            System.err.println(\"File error: \" + e.getMessage());\n        }\n    }\n}",
                    [
                        "All exception types derive from `java.lang.Throwable`.",
                        "Checked exceptions must be either handled via `try-catch` or declared using `throws`.",
                        "Unchecked exceptions subclass `RuntimeException` and reflect logic errors.",
                        "The `finally` block executes unconditionally, even when a return statement is encountered in `try`.",
                        "`try-with-resources` automatically invokes `.close()` on `AutoCloseable` resources.",
                        "Catch blocks must be arranged from most specific subclass to most general superclass."
                    ],
                    "Structured exception handling intercepts runtime errors, maintaining service availability and resource cleanup.",
                    "Throwable, Checked Exception, Unchecked Exception, try-with-resources, finally.",
                    "Exception Creation -> Stack Unwinding -> Catch Block Match -> Finally Execution.",
                    "Catching general `Exception` or `Throwable` early and swallowing exceptions with empty catch blocks."
                )
            ]
        },
        {
            "module_no": 8,
            "title": "File I/O and Serialization",
            "hours": 5,
            "marks": 6,
            "topics": [
                create_topic(
                    "java_m8_t1",
                    "Byte Streams, Character Streams, File I/O, and Object Serialization",
                    ["InputStream vs Reader", "OutputStream vs Writer", "BufferedReader & BufferedWriter", "Object Serialization & Deserialization", "transient Keyword"],
                    "Java File I/O facilitates persistent data exchange via streaming abstractions, divided into 8-bit Byte Streams and 16-bit Character Streams, alongside Object Serialization for object graph persistence.",
                    "Introduced in `java.io` and expanded in `java.nio` to provide robust, platform-neutral filesystem interactions.",
                    "Powers document management systems, state preservation, distributed RPC data exchange, and network file transfers.",
                    ["Differentiate byte streams (binary) from character streams (text).", "Buffer stream operations with BufferedReader and BufferedWriter for performance.", "Serialize object graphs using ObjectOutputStream and Serializable interface.", "Prevent sensitive field serialization using the transient modifier."],
                    "Streams flow sequentially. Serialization converts heap object state into a binary byte sequence; deserialization reconstructs it.",
                    [
                        ("Byte Stream", "Processes data byte-by-byte (8-bit) using InputStream and OutputStream."),
                        ("Character Stream", "Processes data character-by-character (16-bit Unicode) using Reader and Writer."),
                        ("Serialization", "Converting an active object into a byte sequence for storage or network transmission."),
                        ("transient Keyword", "Variable modifier preventing field serialization to protect passwords/keys.")
                    ],
                    "1. Stream Flushing and Closing: Streams must be flushed and closed to release OS file handles.\n2. serialVersionUID: Declared static final long ID guaranteeing version compatibility during deserialization.",
                    "ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream(&quot;data.ser&quot;)); -> oos.writeObject(obj);",
                    [
                        "1. Class implements `java.io.Serializable` marker interface.",
                        "2. ObjectOutputStream traverses the object graph recursively.",
                        "3. Primitive fields and non-transient object references are written to byte stream.",
                        "4. ObjectInputStream reads binary header, verifies serialVersionUID, and reconstructs object in heap."
                    ],
                    ["Stream Type", "Base Abstract Class", "Unit Size", "Optimal Use Case"],
                    [
                        ["Byte Input", "InputStream", "8 bits", "Images, audio, compiled binaries"],
                        ["Byte Output", "OutputStream", "8 bits", "Writing raw bytes / network packets"],
                        ["Character Input", "Reader", "16 bits", "UTF-8 / ASCII text file reading"],
                        ["Character Output", "Writer", "16 bits", "Text log writing and formatting"]
                    ],
                    "// Object Serialization\nclass User implements Serializable {\n    private static final long serialVersionUID = 1L;\n    String username;\n    transient String password; // Will not be saved\n    public User(String u, String p) { this.username = u; this.password = p; }\n}",
                    """<svg viewBox='0 0 800 180' xmlns='http://www.w3.org/2000/svg' style='width:100%;height:auto;background:#fff;border-radius:8px;border:1px solid #E5E9F1;'><rect x='40' y='30' width='220' height='120' rx='8' fill='#F7F8FC' stroke='#377FE6'/><text x='150' y='60' font-family='sans-serif' font-size='12' font-weight='700' fill='#377FE6' text-anchor='middle'>Active Heap Object</text><text x='60' y='90' font-family='monospace' font-size='11' fill='#19283D'>User user = new User();</text><text x='60' y='115' font-family='monospace' font-size='10' fill='#D65F64'>transient password</text><path d='M 265 90 L 375 90' stroke='#786CE5' stroke-width='2'/><text x='320' y='80' font-family='sans-serif' font-size='9' font-weight='700' fill='#786CE5' text-anchor='middle'>writeObject()</text><rect x='380' y='30' width='160' height='120' rx='8' fill='#E9E8F8' stroke='#786CE5'/><text x='460' y='60' font-family='sans-serif' font-size='12' font-weight='700' fill='#786CE5' text-anchor='middle'>Binary Byte Stream</text><text x='460' y='95' font-family='monospace' font-size='11' fill='#19283D' text-anchor='middle'>[0xAC, 0xED, ...]</text><path d='M 545 90 L 635 90' stroke='#28A994' stroke-width='2'/><rect x='640' y='30' width='120' height='120' rx='8' fill='#F7F8FC' stroke='#28A994'/><text x='700' y='60' font-family='sans-serif' font-size='12' font-weight='700' fill='#28A994' text-anchor='middle'>Persistent File</text><text x='700' y='95' font-family='monospace' font-size='11' fill='#1B6F61' text-anchor='middle'>user.ser</text></svg>""",
                    "Figure 8.1: Java Object Serialization Architecture to Persistent Binary File",
                    "Reading Text File Line-by-Line with BufferedReader",
                    "public class FileReaderDemo {\n    public static void printLines(String filePath) throws IOException {\n        try (BufferedReader br = new BufferedReader(new FileReader(filePath))) {\n            String line;\n            while ((line = br.readLine()) != null) {\n                System.out.println(line);\n            }\n        }\n    }\n}",
                    [
                        "Byte streams (InputStream/OutputStream) operate on 8-bit binary data.",
                        "Character streams (Reader/Writer) operate on 16-bit Unicode characters.",
                        "`BufferedReader` minimizes disk I/O operations by buffering character chunks.",
                        "Serialization requires classes to implement the `Serializable` marker interface.",
                        "The `transient` keyword omits specific fields from serialized byte streams.",
                        "`serialVersionUID` ensures sender and receiver maintain matching class definitions."
                    ],
                    "Java Stream abstractions standardize I/O across hardware devices, while serialization persists complex in-memory object graphs.",
                    "Byte Stream, Character Stream, BufferedReader, Serialization, transient, serialVersionUID.",
                    "Stream Initialization -> Buffer Reading/Writing -> Object Graph Serialization -> Handle Closure.",
                    "Forgetting to mark sensitive credentials as `transient`, exposing plaintext secrets in serialized files."
                )
            ]
        },
        {
            "module_no": 9,
            "title": "Multithreading",
            "hours": 4,
            "marks": 8,
            "topics": [
                create_topic(
                    "java_m9_t1",
                    "Thread Life Cycle, Creation (Thread vs Runnable), Synchronization, and Inter-thread Communication",
                    ["Thread Life Cycle States", "Extending Thread vs Implementing Runnable", "synchronized Keyword and Monitors", "wait(), notify(), and notifyAll()", "Deadlock Prevention"],
                    "Multithreading is a concurrent execution model enabling a Java application to run two or more concurrent execution paths (threads) simultaneously to maximize CPU multi-core utilization.",
                    "Engineered into Java's language core from inception, mapping Java threads directly onto operating system kernel threads.",
                    "Essential for asynchronous GUI interfaces, web servers handling concurrent HTTP requests, and high-performance financial order processing.",
                    ["Diagram the 6 states of the Java Thread life cycle.", "Implement threads via Thread inheritance and the Runnable interface.", "Apply synchronized blocks and methods to prevent race conditions on shared memory.", "Coordinate thread messaging using wait(), notify(), and notifyAll()."],
                    "Threads share the JVM Heap and Method Area, but maintain private Stack frames, Program Counters, and Local Variable arrays.",
                    [
                        ("Thread", "Lightweight sub-process with independent execution call stack."),
                        ("Race Condition", "Flaw where program outcome depends on unpredictable thread execution timing."),
                        ("Monitor / Lock", "Synchronization lock enforcing mutually exclusive access to shared blocks."),
                        ("Deadlock", "Stalemate where two or more threads wait indefinitely for locks held by each other.")
                    ],
                    "1. Mutex Locking: Every Java object possesses an internal monitor lock.\n2. Wait Queue: `wait()` releases the object lock and suspends the calling thread until `notify()` is invoked.",
                    "New -> Runnable -> Running -> Blocked/Waiting/Timed-Waiting -> Terminated.",
                    [
                        "1. Thread instantiated via `new MyThread()` (NEW state).",
                        "2. Calling `.start()` transitions thread to RUNNABLE in the OS scheduler queue.",
                        "3. OS allocates CPU time slice (RUNNING).",
                        "4. Synchronized contention transitions thread to BLOCKED.",
                        "5. Execution finishes entering TERMINATED state; dead threads cannot be restarted."
                    ],
                    ["Criterion", "Extending Thread", "Implementing Runnable"],
                    [
                        ["Inheritance Flexibility", "Consumes single class inheritance (cannot extend others)", "Free to extend any other class"],
                        ["Design Decoupling", "Tightly couples task logic with thread management", "Separates executable task from thread worker"],
                        ["Thread Pooling", "Cannot be submitted to ExecutorService directly", "Directly compatible with ExecutorService"],
                        ["Recommended Practice", "Discouraged in modern design", "Industry standard best practice"]
                    ],
                    "// Synchronized Counter\nclass SafeCounter {\n    private int count = 0;\n    public synchronized void increment() { count++; }\n    public synchronized int getCount() { return count; }\n}",
                    """<svg viewBox='0 0 800 200' xmlns='http://www.w3.org/2000/svg' style='width:100%;height:auto;background:#fff;border-radius:8px;border:1px solid #E5E9F1;'><rect x='30' y='80' width='100' height='45' rx='6' fill='#F7F8FC' stroke='#377FE6'/><text x='80' y='107' font-family='sans-serif' font-size='11' font-weight='700' fill='#377FE6' text-anchor='middle'>NEW</text><path d='M 135 102 L 195 102' stroke='#377FE6' stroke-width='2'/><text x='165' y='95' font-family='sans-serif' font-size='9' fill='#617087' text-anchor='middle'>start()</text><rect x='200' y='80' width='130' height='45' rx='6' fill='#F7F8FC' stroke='#28A994'/><text x='265' y='107' font-family='sans-serif' font-size='11' font-weight='700' fill='#28A994' text-anchor='middle'>RUNNABLE</text><path d='M 335 90 L 415 50' stroke='#786CE5' stroke-width='2'/><rect x='420' y='30' width='160' height='45' rx='6' fill='#FFF2EB' stroke='#EF846B'/><text x='500' y='57' font-family='sans-serif' font-size='11' font-weight='700' fill='#EF846B' text-anchor='middle'>BLOCKED / WAITING</text><path d='M 420 65 L 335 102' stroke='#786CE5' stroke-width='2'/><path d='M 335 110 L 615 110' stroke='#369B72' stroke-width='2'/><text x='480' y='105' font-family='sans-serif' font-size='9' fill='#617087' text-anchor='middle'>run() completes</text><rect x='620' y='80' width='130' height='45' rx='6' fill='#F7F8FC' stroke='#617087'/><text x='685' y='107' font-family='sans-serif' font-size='11' font-weight='700' fill='#617087' text-anchor='middle'>TERMINATED</text></svg>""",
                    "Figure 9.1: Java Thread Life Cycle State Transition Diagram",
                    "Thread Coordination with wait() and notify()",
                    "class MessageQueue {\n    private String msg;\n    private boolean empty = true;\n    public synchronized void put(String m) throws InterruptedException {\n        while (!empty) wait();\n        this.msg = m;\n        empty = false;\n        notifyAll();\n    }\n    public synchronized String take() throws InterruptedException {\n        while (empty) wait();\n        empty = true;\n        notifyAll();\n        return msg;\n    }\n}",
                    [
                        "A Java thread transitions through 6 states: NEW, RUNNABLE, BLOCKED, WAITING, TIMED_WAITING, TERMINATED.",
                        "Implementing `Runnable` is preferred over extending `Thread` to preserve single inheritance.",
                        "Invoke `.start()` to spawn a new OS thread; invoking `.run()` runs synchronously on the caller thread.",
                        "`synchronized` prevents race conditions by acquiring the target object's monitor lock.",
                        "`wait()`, `notify()`, and `notifyAll()` must be invoked strictly within synchronized context.",
                        "Volatile variables guarantee memory visibility across CPU caches without mutual exclusion locking."
                    ],
                    "Java multithreading executes concurrent paths sharing heap memory while maintaining isolation via synchronization monitors.",
                    "Thread, Runnable, Life Cycle, synchronized, Monitor, wait/notify, Deadlock.",
                    "start() -> Scheduler Dispatch -> Execution -> Lock Contention -> Terminated.",
                    "Calling `.run()` directly instead of `.start()`, which causes the code to execute sequentially on the main thread."
                )
            ]
        }
    ]
