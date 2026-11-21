# Model Examination Questions for BCAC502: Java OOP (10 Questions)

def get_java_exams():
    return [
    {
        "id": "exam_java_q1",
        "subject_id": "bcac502",
        "question_no": 1,
        "title": "Explain the Java Virtual Machine (JVM) Architecture, ClassLoader subsystem, and Memory Areas.",
        "intro": {
            "definition": "The Java Virtual Machine (JVM) is an abstract computing machine that provides the runtime execution environment for compiled Java bytecode.",
            "background": "Engineered by Sun Microsystems to fulfill the 'Write Once, Run Anywhere' (WORA) philosophy by decoupling bytecode from host CPU architectures.",
            "significance": "Underpins enterprise software execution, managing automated garbage collection, dynamic memory allocation, and hardware abstraction."
        },
        "diagram": {
            "svg": "<svg viewBox='0 0 700 140' xmlns='http://www.w3.org/2000/svg' style='width:100%;height:auto;background:#fff;border-radius:6px;border:1px solid #E5E9F1;'><rect x='20' y='25' width='130' height='90' rx='6' fill='#F7F8FC' stroke='#377FE6'/><text x='85' y='55' font-family='sans-serif' font-size='11' font-weight='700' fill='#377FE6' text-anchor='middle'>ClassLoader</text><text x='85' y='75' font-family='sans-serif' font-size='9' fill='#617087' text-anchor='middle'>Loading, Linking</text><text x='85' y='92' font-family='sans-serif' font-size='9' fill='#617087' text-anchor='middle'>&amp; Initialization</text><path d='M 155 70 L 215 70' stroke='#377FE6' stroke-width='2'/><rect x='220' y='20' width='260' height='100' rx='6' fill='#E9E8F8' stroke='#786CE5'/><text x='350' y='42' font-family='sans-serif' font-size='11' font-weight='700' fill='#19283D' text-anchor='middle'>JVM Memory Areas</text><rect x='235' y='52' width='110' height='30' rx='4' fill='#FFF' stroke='#377FE6'/><text x='290' y='72' font-family='sans-serif' font-size='9' font-weight='700' fill='#377FE6' text-anchor='middle'>Heap Area</text><rect x='355' y='52' width='110' height='30' rx='4' fill='#FFF' stroke='#786CE5'/><text x='410' y='72' font-family='sans-serif' font-size='9' font-weight='700' fill='#786CE5' text-anchor='middle'>Method Area</text><rect x='235' y='86' width='110' height='26' rx='4' fill='#FFF' stroke='#28A994'/><text x='290' y='103' font-family='sans-serif' font-size='8' fill='#28A994' text-anchor='middle'>JVM Stack</text><rect x='355' y='86' width='110' height='26' rx='4' fill='#FFF' stroke='#F2C75C'/><text x='410' y='103' font-family='sans-serif' font-size='8' fill='#19283D' text-anchor='middle'>PC Registers</text><path d='M 485 70 L 545 70' stroke='#28A994' stroke-width='2'/><rect x='550' y='25' width='130' height='90' rx='6' fill='#F7F8FC' stroke='#28A994'/><text x='615' y='55' font-family='sans-serif' font-size='11' font-weight='700' fill='#28A994' text-anchor='middle'>Execution Engine</text><text x='615' y='75' font-family='sans-serif' font-size='9' fill='#1B6F61' text-anchor='middle'>Interpreter + JIT</text><text x='615' y='92' font-family='sans-serif' font-size='9' fill='#1B6F61' text-anchor='middle'>Garbage Collector</text></svg>",
            "explanation": "Illustrates the ClassLoader subsystem delivering compiled bytecode to JVM memory areas for execution via Interpreter, JIT, and Garbage Collector.",
            "caption": "Figure E1.2: Java Virtual Machine Subsystems and Memory Architecture"
        },
        "points": [
            {
                "point_no": 1,
                "heading": "ClassLoader Delegation Hierarchy",
                "explanation": "Follows the parent-delegation model consisting of Bootstrap, Extension (Platform), and Application (System) ClassLoaders to ensure core security.",
                "terminology": "Bootstrap ClassLoader, Platform ClassLoader, Application ClassLoader, Delegation Model.",
                "example": "java.lang.Object is always loaded by the Bootstrap ClassLoader, preventing rogue replacements."
            },
            {
                "point_no": 2,
                "heading": "Shared Heap and Method Memory Areas",
                "explanation": "Heap memory stores all object instances and arrays shared across threads. The Method Area stores class metadata, static fields, and runtime constant pool.",
                "terminology": "Heap Space, Young/Old Generation, Method Area, Metaspace.",
                "example": "Student s = new Student(); creates the object instance in the Heap area."
            },
            {
                "point_no": 3,
                "heading": "Thread-Private Stack Frames and PC Registers",
                "explanation": "Each thread maintains a private stack where every method invocation pushes a stack frame storing local variables, operand stacks, and return values.",
                "terminology": "Stack Frame, Local Variable Array, Operand Stack, Program Counter (PC).",
                "example": "Deep recursion exceeding thread stack memory triggers java.lang.StackOverflowError."
            },
            {
                "point_no": 4,
                "heading": "Execution Engine: Interpreter vs JIT Compiler",
                "explanation": "The Interpreter executes bytecode sequentially. The Just-In-Time (JIT) compiler compiles frequently executed loops into native CPU machine code.",
                "terminology": "Interpreter, JIT Compiler, HotSpot Detection, Native Machine Code.",
                "example": "Loops executed over 10,000 times are compiled into native instructions by the C2 JIT compiler."
            },
            {
                "point_no": 5,
                "heading": "Automated Garbage Collection (GC)",
                "explanation": "The Garbage Collector runs as an asynchronous background daemon identifying and sweeping unreferenced heap objects using root tracing.",
                "terminology": "GC Roots, Mark-and-Sweep, Generational Collection, OutOfMemoryError.",
                "example": "Setting reference `s = null;` marks the heap object eligible for garbage collection."
            }
        ],
        "conclusion": "The JVM's robust architecture achieves cross-platform execution while enforcing memory safety via automated garbage collection and sandboxed execution."
    },
    {
        "id": "exam_java_q2",
        "subject_id": "bcac502",
        "question_no": 2,
        "title": "Explain Encapsulation, Data Hiding, and the Four Java Access Modifiers.",
        "intro": {
            "definition": "Encapsulation is the fundamental OOP principle of binding state fields and operational methods together inside a class while hiding internal representation.",
            "background": "Designed to prevent arbitrary manipulation of internal object invariants, replacing direct field access with controlled accessors.",
            "significance": "Guarantees data integrity, enables validation rules on mutations, and supports long-term refactoring without breaking client interfaces."
        },
        "diagram": {
            "svg": "<svg viewBox='0 0 700 140' xmlns='http://www.w3.org/2000/svg' style='width:100%;height:auto;background:#fff;border-radius:6px;border:1px solid #E5E9F1;'><rect x='40' y='25' width='220' height='90' rx='8' fill='#F7F8FC' stroke='#377FE6'/><text x='150' y='50' font-family='sans-serif' font-size='12' font-weight='700' fill='#377FE6' text-anchor='middle'>Encapsulated Class</text><rect x='60' y='60' width='180' height='22' rx='4' fill='#FFF2EB' stroke='#EF846B'/><text x='150' y='75' font-family='monospace' font-size='10' fill='#D65F64' text-anchor='middle'>- private double balance</text><rect x='60' y='86' width='180' height='22' rx='4' fill='#E9E8F8' stroke='#28A994'/><text x='150' y='101' font-family='monospace' font-size='10' fill='#1B6F61' text-anchor='middle'>+ public deposit(amt)</text><path d='M 270 70 L 360 70' stroke='#377FE6' stroke-width='2'/><text x='315' y='60' font-family='sans-serif' font-size='9' fill='#377FE6' text-anchor='middle'>Validation</text><rect x='370' y='25' width='290' height='90' rx='8' fill='#E9E8F8' stroke='#786CE5'/><text x='515' y='50' font-family='sans-serif' font-size='11' font-weight='700' fill='#19283D' text-anchor='middle'>Client Layer</text><text x='515' y='75' font-family='sans-serif' font-size='10' fill='#617087' text-anchor='middle'>Direct field access denied (Compiler error)</text><text x='515' y='95' font-family='monospace' font-size='10' font-weight='700' fill='#28A994' text-anchor='middle'>account.deposit(500); // Authorized</text></svg>",
            "explanation": "Illustrates private data shielding wrapped within public validated accessor and mutator methods.",
            "caption": "Figure E2.2: Encapsulation and Data Shielding Architecture"
        },
        "points": [
            {
                "point_no": 1,
                "heading": "Data Hiding and Invariant Protection",
                "explanation": "Declaring fields private hides memory representation, ensuring state can only be mutated through validated public setter methods.",
                "terminology": "Data Hiding, Invariants, Accessor (Getter), Mutator (Setter).",
                "example": "private double balance; setBalance(double b) verifies b > 0 before updating."
            },
            {
                "point_no": 2,
                "heading": "Private Access Modifier Scope",
                "explanation": "The private modifier restricts accessibility strictly to the declaring class body; child classes and external packages cannot see private members.",
                "terminology": "private, Class Scope, Information Hiding.",
                "example": "A private helper method encryptData() cannot be invoked outside its host class."
            },
            {
                "point_no": 3,
                "heading": "Default (Package-Private) Scope",
                "explanation": "When no modifier keyword is provided, access is granted to all classes within the same Java package, but prohibited to outside packages.",
                "terminology": "Package-Private, Default Scope, Package Boundary.",
                "example": "Package-level utility classes collaborate internally while hidden from consumer modules."
            },
            {
                "point_no": 4,
                "heading": "Protected Modifier and Inheritance Access",
                "explanation": "The protected modifier grants access to classes in the same package and to derived subclasses residing in different packages.",
                "terminology": "protected, Subclass Visibility, Cross-Package Inheritance.",
                "example": "protected void calculateBonus() can be overridden by a manager class in another package."
            },
            {
                "point_no": 5,
                "heading": "Public Modifier and Global Availability",
                "explanation": "The public keyword makes a class, method, or field universally accessible across all packages in the JVM environment.",
                "terminology": "public, Global Scope, Public API Contract.",
                "example": "public static void main(String[] args) must be public for the JVM to invoke entry points."
            }
        ],
        "conclusion": "Encapsulation safeguards internal software state against illegal modifications by pairing private fields with public mutator validation logic."
    },
    {
        "id": "exam_java_q3",
        "subject_id": "bcac502",
        "question_no": 3,
        "title": "Explain Method Overriding, Dynamic Method Dispatch, and Runtime Polymorphism in Java.",
        "intro": {
            "definition": "Runtime polymorphism is the OOP capability where a method call is bound to its concrete implementation dynamically at runtime based on the actual object instance on the heap.",
            "background": "Derived from theoretical virtual method tables (vtables) to enable extensible plugin architectures where base types operate on specialized child classes.",
            "significance": "Underpins modern frameworks (Spring, Hibernate), allowing polymorphic container dispatch and decoupling interfaces from implementations."
        },
        "diagram": {
            "svg": "<svg viewBox='0 0 700 140' xmlns='http://www.w3.org/2000/svg' style='width:100%;height:auto;background:#fff;border-radius:6px;border:1px solid #E5E9F1;'><rect x='30' y='30' width='160' height='70' rx='6' fill='#F7F8FC' stroke='#377FE6'/><text x='110' y='55' font-family='sans-serif' font-size='11' font-weight='700' fill='#377FE6' text-anchor='middle'>Superclass: Animal</text><text x='110' y='75' font-family='monospace' font-size='9' fill='#19283D' text-anchor='middle'>void makeSound()</text><path d='M 195 65 L 265 65' stroke='#786CE5' stroke-width='2'/><polygon points='265,60 275,65 265,70' fill='#786CE5'/><rect x='280' y='30' width='160' height='70' rx='6' fill='#F7F8FC' stroke='#786CE5'/><text x='360' y='55' font-family='sans-serif' font-size='11' font-weight='700' fill='#786CE5' text-anchor='middle'>Subclass: Dog</text><text x='360' y='75' font-family='monospace' font-size='9' fill='#28A994' text-anchor='middle'>@Override makeSound()</text><rect x='480' y='25' width='190' height='85' rx='6' fill='#E9E8F8' stroke='#28A994'/><text x='575' y='50' font-family='sans-serif' font-size='10' font-weight='700' fill='#1B6F61' text-anchor='middle'>Dynamic Dispatch</text><text x='575' y='70' font-family='monospace' font-size='9' fill='#19283D' text-anchor='middle'>Animal a = new Dog();</text><text x='575' y='88' font-family='monospace' font-size='9' fill='#19283D' text-anchor='middle'>a.makeSound();</text><text x='575' y='103' font-family='sans-serif' font-size='8' font-weight='700' fill='#369B72' text-anchor='middle'>-&gt; Executes Dog.makeSound()</text></svg>",
            "explanation": "Illustrates a superclass reference variable dynamically invoking the overridden method implementation residing on the child heap instance.",
            "caption": "Figure E3.2: Dynamic Method Dispatch via Superclass Reference"
        },
        "points": [
            {
                "point_no": 1,
                "heading": "Method Overriding Signature Rules",
                "explanation": "An overriding method in a subclass must match the superclass method's name, argument types, and return type (or covariant subtype) identically.",
                "terminology": "Method Overriding, Covariant Return Type, @Override Annotation.",
                "example": "class Dog extends Animal { @Override public void makeSound() { System.out.println('Bark'); } }"
            },
            {
                "point_no": 2,
                "heading": "Dynamic Method Dispatch Mechanics",
                "explanation": "When an overridden method is called via a superclass reference, the JVM looks up the target object's virtual method table (vtable) at runtime to resolve the call.",
                "terminology": "Dynamic Method Dispatch, vtable, Late Binding, Reference Type vs Object Type.",
                "example": "Shape s = new Circle(); s.draw(); dynamically dispatches to Circle's draw method."
            },
            {
                "point_no": 3,
                "heading": "Access Privilege Escalation Rule",
                "explanation": "An overriding method cannot impose more restrictive access privileges than the overridden parent method, though it can broaden accessibility.",
                "terminology": "Access Broadening, Visibility Invariance, Liskov Substitution.",
                "example": "A protected method in the parent can be overridden as public, but not as private."
            },
            {
                "point_no": 4,
                "heading": "Compile-time Binding of Static and Private Methods",
                "explanation": "Static methods cannot be overridden; they participate in method hiding determined at compile-time. Private methods are not visible to subclasses and cannot participate in dynamic dispatch.",
                "terminology": "Method Hiding, Static Binding, Early Resolution, Final Methods.",
                "example": "Calling a hidden static method resolves to the reference type, not the runtime object instance."
            },
            {
                "point_no": 5,
                "heading": "Constructor Invocation via super()",
                "explanation": "Overridden child classes invoke superclass constructors using super() as the first executable line, ensuring proper base initialization.",
                "terminology": "super Keyword, Constructor Chaining, Base Initialization.",
                "example": "public Dog(String name) { super(name); } ensures Animal constructor runs first."
            }
        ],
        "conclusion": "Dynamic method dispatch enables polymorphism by deferring method binding to runtime, forming the core mechanism for scalable object hierarchies in Java."
    },
    {
        "id": "exam_java_q4",
        "subject_id": "bcac502",
        "question_no": 4,
        "title": "Explain String Immutability and the String Constant Pool (SCP) Architecture in Java.",
        "intro": {
            "definition": "String immutability is the architectural property whereby a java.lang.String object's character sequence cannot be modified after memory allocation.",
            "background": "Introduced in Java 1.0 to ensure cryptographic security for classloading, networking, and memory conservation via literal pooling.",
            "significance": "Guarantees thread safety across concurrent workers, enables hashcode caching in HashMaps, and prevents malicious connection parameter mutation."
        },
        "diagram": {
            "svg": "<svg viewBox='0 0 700 140' xmlns='http://www.w3.org/2000/svg' style='width:100%;height:auto;background:#fff;border-radius:6px;border:1px solid #E5E9F1;'><rect x='30' y='25' width='180' height='90' rx='6' fill='#F7F8FC' stroke='#377FE6'/><text x='120' y='50' font-family='sans-serif' font-size='11' font-weight='700' fill='#377FE6' text-anchor='middle'>Stack Variables</text><text x='120' y='70' font-family='monospace' font-size='9' fill='#19283D' text-anchor='middle'>String s1 = &quot;MAKAUT&quot;;</text><text x='120' y='90' font-family='monospace' font-size='9' fill='#19283D' text-anchor='middle'>String s2 = &quot;MAKAUT&quot;;</text><path d='M 215 70 L 315 70' stroke='#377FE6' stroke-width='2'/><rect x='320' y='20' width='340' height='100' rx='6' fill='#E9E8F8' stroke='#786CE5'/><text x='490' y='42' font-family='sans-serif' font-size='11' font-weight='700' fill='#19283D' text-anchor='middle'>Heap Memory: String Constant Pool</text><rect x='340' y='55' width='300' height='40' rx='4' fill='#FFF' stroke='#377FE6'/><text x='490' y='80' font-family='monospace' font-size='12' font-weight='700' fill='#377FE6' text-anchor='middle'>&quot;MAKAUT&quot; (Single Shared Literal)</text></svg>",
            "explanation": "Illustrates multiple stack references pointing to a single shared String instance in the String Constant Pool inside heap memory.",
            "caption": "Figure E4.2: String Constant Pool Memory Optimization Model"
        },
        "points": [
            {
                "point_no": 1,
                "heading": "Mechanics of String Immutability",
                "explanation": "String stores characters in a private final byte/char array without exposing any mutator methods; all modification methods return a new String instance.",
                "terminology": "Immutable Object, final char[], Value Semantics, State Invariance.",
                "example": "String s = 'Hello'; s.concat(' World'); leaves original s unchanged unless reassigned."
            },
            {
                "point_no": 2,
                "heading": "String Constant Pool (SCP) Caching",
                "explanation": "Literal strings are stored in the String Constant Pool in the JVM Heap; subsequent identical literals point to the existing instance, saving memory.",
                "terminology": "String Constant Pool (SCP), Literal Deduplication, String.intern().",
                "example": "String a = 'WBUT'; String b = 'WBUT'; (a == b) is true due to SCP caching."
            },
            {
                "point_no": 3,
                "heading": "Security Implications in Network & ClassLoading",
                "explanation": "Critical runtime parameters like DB connection URLs, passwords, and file paths are immutable to prevent tampering between authorization checks and socket access.",
                "terminology": "Time-of-Check to Time-of-Use (TOCTOU), Security Vector, Integrity.",
                "example": "If strings were mutable, a malicious thread could alter a verified socket port before transmission."
            },
            {
                "point_no": 4,
                "heading": "Thread Safety and Concurrency",
                "explanation": "Because internal string state cannot be altered after instantiation, String instances are inherently thread-safe without requiring synchronized locking overhead.",
                "terminology": "Thread Safety, Lock-Free Concurrency, Safe Publication.",
                "example": "Hundreds of worker threads can concurrently access a shared String without race conditions."
            },
            {
                "point_no": 5,
                "heading": "Mutable Alternatives: StringBuffer and StringBuilder",
                "explanation": "When intensive character concatenation is required, use StringBuilder (high-speed, single-threaded) or StringBuffer (synchronized, thread-safe).",
                "terminology": "StringBuilder, StringBuffer, Mutability, Append Buffer.",
                "example": "StringBuilder sb = new StringBuilder(); for(int i=0;i<1000;i++) sb.append(i); avoids 1000 temporary objects."
            }
        ],
        "conclusion": "String immutability optimizes memory utilization via the String Pool while providing inherent thread safety and security in enterprise Java systems."
    },
    {
        "id": "exam_java_q5",
        "subject_id": "bcac502",
        "question_no": 5,
        "title": "Compare Interfaces with Abstract Classes and analyze Java 8 Default Methods.",
        "intro": {
            "definition": "Abstract classes and interfaces are abstraction abstractions defining behavioral contracts for derived classes, differing in state retention and inheritance models.",
            "background": "Java 8 transformed interfaces by introducing default and static methods to support backward compatibility for lambda expressions without breaking existing classes.",
            "significance": "Underpins modern clean architecture, interface segregation (SOLID), and API contract stability across enterprise codebases."
        },
        "diagram": {
            "svg": "<svg viewBox='0 0 700 140' xmlns='http://www.w3.org/2000/svg' style='width:100%;height:auto;background:#fff;border-radius:6px;border:1px solid #E5E9F1;'><rect x='30' y='25' width='280' height='90' rx='6' fill='#F7F8FC' stroke='#377FE6'/><text x='170' y='50' font-family='sans-serif' font-size='12' font-weight='700' fill='#377FE6' text-anchor='middle'>Abstract Class (extends)</text><text x='170' y='70' font-family='sans-serif' font-size='10' fill='#19283D' text-anchor='middle'>Single Inheritance | Has Constructors</text><text x='170' y='88' font-family='sans-serif' font-size='9' fill='#617087' text-anchor='middle'>Can maintain instance state &amp; final fields</text><rect x='390' y='25' width='280' height='90' rx='6' fill='#F7F8FC' stroke='#786CE5'/><text x='530' y='50' font-family='sans-serif' font-size='12' font-weight='700' fill='#786CE5' text-anchor='middle'>Interface (implements)</text><text x='530' y='70' font-family='sans-serif' font-size='10' fill='#19283D' text-anchor='middle'>Multiple Inheritance | No Constructors</text><text x='530' y='88' font-family='sans-serif' font-size='9' fill='#28A994' text-anchor='middle'>default &amp; static methods (Java 8+)</text></svg>",
            "explanation": "Contrasts abstract class single inheritance and state retention with interface multiple contract implementation and default behaviors.",
            "caption": "Figure E5.2: Structural Comparison: Abstract Class vs Interface"
        },
        "points": [
            {
                "point_no": 1,
                "heading": "Inheritance Multiplicity Model",
                "explanation": "A class can extend only one abstract class (single inheritance), but can implement an unlimited number of interfaces using comma separation.",
                "terminology": "Single Class Inheritance, Multiple Interface Implementation, implements Keyword.",
                "example": "class SmartPhone extends Phone implements Camera, GPS, MediaRenderer {}"
            },
            {
                "point_no": 2,
                "heading": "State Retention and Constructor Capabilities",
                "explanation": "Abstract classes can declare instance state fields and define constructors called by child super(), whereas interfaces cannot hold instance variables or constructors.",
                "terminology": "Constructors, Instance State, public static final Constants.",
                "example": "All interface variables are implicitly `public static final` constants."
            },
            {
                "point_no": 3,
                "heading": "Java 8 Default Methods and API Evolution",
                "explanation": "Default methods (default void log()) provide concrete fallback implementations inside interfaces, allowing libraries to add methods without breaking existing implementing classes.",
                "terminology": "default Keyword, Interface Evolution, Backward Compatibility.",
                "example": "default void printLog(String msg) { System.out.println(msg); }"
            },
            {
                "point_no": 4,
                "heading": "Disambiguating Multiple Default Method Conflicts",
                "explanation": "If a class implements two interfaces containing identical default method signatures, the class must explicitly override and resolve the conflict using InterfaceName.super.method().",
                "terminology": "Diamond Problem Resolution, Explicit Override Disambiguation.",
                "example": "A.super.display(); explicitly specifies which interface's default method to execute."
            },
            {
                "point_no": 5,
                "heading": "Functional Interfaces and Lambda Readiness",
                "explanation": "An interface with exactly one abstract method is a Functional Interface (@FunctionalInterface), capable of being instantiated using modern lambda expressions.",
                "terminology": "Functional Interface, @FunctionalInterface, Single Abstract Method (SAM), Lambda.",
                "example": "Runnable r = () -> System.out.println('Thread running');"
            }
        ],
        "conclusion": "Abstract classes provide shared implementation state for related hierarchies, whereas interfaces define flexible contracts that support multiple inheritance of type."
    },
    {
        "id": "exam_java_q6",
        "subject_id": "bcac502",
        "question_no": 6,
        "title": "Explain Exception Handling in Java: Throwable Hierarchy, Checked vs Unchecked, and try-with-resources.",
        "intro": {
            "definition": "Exception handling is a structured language mechanism for intercepting runtime abnormal conditions to prevent process termination and preserve program flow.",
            "background": "Standardized in Java to supersede C-style error return codes, enforcing strict compiler verification of recoverable checked exceptions.",
            "significance": "Crucial for writing resilient enterprise applications that handle I/O, network, and database interruptions cleanly."
        },
        "diagram": {
            "svg": "<svg viewBox='0 0 700 140' xmlns='http://www.w3.org/2000/svg' style='width:100%;height:auto;background:#fff;border-radius:6px;border:1px solid #E5E9F1;'><rect x='280' y='15' width='140' height='30' rx='6' fill='#F7F8FC' stroke='#377FE6'/><text x='350' y='35' font-family='sans-serif' font-size='11' font-weight='700' fill='#377FE6' text-anchor='middle'>Throwable</text><path d='M 310 45 L 180 70' stroke='#D65F64' stroke-width='2'/><path d='M 390 45 L 520 70' stroke='#28A994' stroke-width='2'/><rect x='100' y='70' width='160' height='30' rx='6' fill='#FFF2EB' stroke='#D65F64'/><text x='180' y='90' font-family='sans-serif' font-size='10' font-weight='700' fill='#D65F64' text-anchor='middle'>Error (Unrecoverable)</text><rect x='440' y='70' width='160' height='30' rx='6' fill='#F7F8FC' stroke='#28A994'/><text x='520' y='90' font-family='sans-serif' font-size='10' font-weight='700' fill='#28A994' text-anchor='middle'>Exception (Recoverable)</text><rect x='400' y='108' width='110' height='24' rx='4' fill='#FFF' stroke='#377FE6'/><text x='455' y='124' font-family='sans-serif' font-size='8' fill='#377FE6' text-anchor='middle'>Checked (IOException)</text><rect x='530' y='108' width='130' height='24' rx='4' fill='#FFF' stroke='#F2C75C'/><text x='595' y='124' font-family='sans-serif' font-size='8' fill='#19283D' text-anchor='middle'>RuntimeException (Unchk)</text></svg>",
            "explanation": "Illustrates the Throwable class hierarchy segregating unrecoverable Errors from recoverable Checked and Unchecked Exceptions.",
            "caption": "Figure E6.2: Java Throwable Class Hierarchy"
        },
        "points": [
            {
                "point_no": 1,
                "heading": "Throwable Class Hierarchy Structure",
                "explanation": "All exceptions and errors derive from java.lang.Throwable. Errors represent fatal JVM failures (OutOfMemoryError); Exceptions represent recoverable anomalies.",
                "terminology": "Throwable, Error, Exception, Stack Trace, JVM Crash.",
                "example": "OutOfMemoryError cannot be gracefully handled; IOException can be handled."
            },
            {
                "point_no": 2,
                "heading": "Checked vs Unchecked Exceptions",
                "explanation": "Checked exceptions (IOException, SQLException) are checked at compile time and mandate try-catch or throws. Unchecked exceptions subclass RuntimeException and reflect logic flaws.",
                "terminology": "Checked Exception, Unchecked Exception, RuntimeException, throws Clause.",
                "example": "NullPointerException is unchecked; ClassNotFoundException is checked."
            },
            {
                "point_no": 3,
                "heading": "try-catch-finally Block Execution Flow",
                "explanation": "The try block holds code prone to exceptions, catch executes remediation, and finally executes unconditionally even if return statements are triggered.",
                "terminology": "try, catch, finally, Unconditional Execution, Cleanup.",
                "example": "finally { dbConn.close(); } ensures database socket disconnection."
            },
            {
                "point_no": 4,
                "heading": "Automated Resource Cleanup (try-with-resources)",
                "explanation": "Introduced in Java 7, resources implementing java.lang.AutoCloseable are automatically closed at block exit without explicit finally clauses.",
                "terminology": "try-with-resources, AutoCloseable, Resource Leak Prevention.",
                "example": "try (BufferedReader br = new BufferedReader(new FileReader(f))) { br.readLine(); }"
            },
            {
                "point_no": 5,
                "heading": "Custom User-Defined Exceptions",
                "explanation": "Subclassing Exception (checked) or RuntimeException (unchecked) allows developers to build domain-specific exception types conveying meaningful error diagnostics.",
                "terminology": "Custom Exception, Domain Exception, Exception Chaining, getMessage().",
                "example": "class InsufficientFundsException extends Exception { public InsufficientFundsException(String m) { super(m); } }"
            }
        ],
        "conclusion": "Java's dual checked/unchecked exception model combined with try-with-resources guarantees robust error handling and automated resource reclamation."
    },
    {
        "id": "exam_java_q7",
        "subject_id": "bcac502",
        "question_no": 7,
        "title": "Explain Multithreading in Java: Thread Life Cycle, Synchronization, and Thread Coordination.",
        "intro": {
            "definition": "Multithreading is the capability of executing multiple lightweight execution paths (threads) concurrently within a single program process to maximize CPU utilization.",
            "background": "Designed into Java's core from inception, mapping Java threads directly to underlying operating system kernel threads with built-in monitor locking.",
            "significance": "Essential for responsive GUI applications, high-throughput network servers, and concurrent transaction engines."
        },
        "diagram": {
            "svg": "<svg viewBox='0 0 700 140' xmlns='http://www.w3.org/2000/svg' style='width:100%;height:auto;background:#fff;border-radius:6px;border:1px solid #E5E9F1;'><rect x='20' y='50' width='80' height='40' rx='6' fill='#F7F8FC' stroke='#377FE6'/><text x='60' y='75' font-family='sans-serif' font-size='10' font-weight='700' fill='#377FE6' text-anchor='middle'>NEW</text><path d='M 105 70 L 155 70' stroke='#377FE6' stroke-width='2'/><rect x='160' y='50' width='110' height='40' rx='6' fill='#F7F8FC' stroke='#28A994'/><text x='215' y='75' font-family='sans-serif' font-size='10' font-weight='700' fill='#28A994' text-anchor='middle'>RUNNABLE</text><path d='M 275 60 L 355 35' stroke='#786CE5' stroke-width='2'/><rect x='360' y='15' width='160' height='40' rx='6' fill='#FFF2EB' stroke='#EF846B'/><text x='440' y='40' font-family='sans-serif' font-size='10' font-weight='700' fill='#EF846B' text-anchor='middle'>BLOCKED / WAITING</text><path d='M 360 45 L 275 70' stroke='#786CE5' stroke-width='2'/><path d='M 275 80 L 555 80' stroke='#369B72' stroke-width='2'/><rect x='560' y='50' width='110' height='40' rx='6' fill='#F7F8FC' stroke='#617087'/><text x='615' y='75' font-family='sans-serif' font-size='10' font-weight='700' fill='#617087' text-anchor='middle'>TERMINATED</text></svg>",
            "explanation": "Illustrates the Java thread lifecycle transitions: NEW -> RUNNABLE -> BLOCKED/WAITING -> TERMINATED.",
            "caption": "Figure E7.2: Java Thread State Transition Architecture"
        },
        "points": [
            {
                "point_no": 1,
                "heading": "Thread Life Cycle States",
                "explanation": "A thread transitions across 6 defined states: NEW, RUNNABLE, BLOCKED, WAITING, TIMED_WAITING, and TERMINATED.",
                "terminology": "Thread.State, Life Cycle, Scheduler Dispatch, OS Time-Slicing.",
                "example": "Calling .start() transitions a NEW thread instance into the RUNNABLE state."
            },
            {
                "point_no": 2,
                "heading": "Thread Creation: Extending Thread vs Implementing Runnable",
                "explanation": "Implementing Runnable is preferred because it separates the task logic from thread execution and preserves single class inheritance flexibility.",
                "terminology": "Runnable Interface, Thread Class, Single Inheritance, Decoupling.",
                "example": "Thread t = new Thread(() -> doWork()); allows class to extend other business models."
            },
            {
                "point_no": 3,
                "heading": "Synchronization and Object Monitor Locks",
                "explanation": "The synchronized keyword acquires the target object's internal monitor lock (mutex), preventing race conditions by enforcing single-thread execution in critical sections.",
                "terminology": "synchronized, Mutual Exclusion (Mutex), Intrinsic Lock, Race Condition.",
                "example": "public synchronized void increment() { count++; } eliminates shared counter corruption."
            },
            {
                "point_no": 4,
                "heading": "Thread Coordination (wait, notify, notifyAll)",
                "explanation": "Invoked strictly inside synchronized blocks, wait() releases the object lock and suspends the calling thread; notify() wakes up a waiting thread upon condition fulfillment.",
                "terminology": "wait(), notify(), notifyAll(), Monitor Wait Queue, Inter-thread Signaling.",
                "example": "In Producer-Consumer queues: consumer waits when queue is empty; producer notifies on insert."
            },
            {
                "point_no": 5,
                "heading": "Deadlock Formation and Mitigation",
                "explanation": "Deadlock occurs when two threads wait indefinitely for locks held by each other; mitigated by enforcing uniform global lock acquisition ordering.",
                "terminology": "Deadlock, Circular Wait, Lock Ordering, Lock Acquisition Timeout.",
                "example": "Always acquire Lock A before Lock B across all application threads."
            }
        ],
        "conclusion": "Java provides language-level multithreading with intrinsic monitors, life-cycle management, and condition signaling to coordinate concurrent execution safely."
    },
    {
        "id": "exam_java_q8",
        "subject_id": "bcac502",
        "question_no": 8,
        "title": "Explain Byte Streams vs Character Streams, File I/O, and Object Serialization in Java.",
        "intro": {
            "definition": "Java I/O streams are sequential data flow abstractions connecting programs to storage files, memory buffers, and network sockets, categorized into 8-bit Byte and 16-bit Character streams.",
            "background": "Character streams (Reader/Writer) were introduced in Java 1.1 to provide international Unicode support, complementing foundational binary Byte streams (InputStream/OutputStream).",
            "significance": "Underpins document persistence, file uploads, distributed object transfer (RMI), and inter-process communication."
        },
        "diagram": {
            "svg": "<svg viewBox='0 0 700 140' xmlns='http://www.w3.org/2000/svg' style='width:100%;height:auto;background:#fff;border-radius:6px;border:1px solid #E5E9F1;'><rect x='30' y='30' width='160' height='80' rx='6' fill='#F7F8FC' stroke='#377FE6'/><text x='110' y='60' font-family='sans-serif' font-size='11' font-weight='700' fill='#377FE6' text-anchor='middle'>Heap Object</text><text x='110' y='80' font-family='monospace' font-size='9' fill='#19283D' text-anchor='middle'>User implements Ser</text><path d='M 195 70 L 295 70' stroke='#786CE5' stroke-width='2'/><text x='245' y='60' font-family='sans-serif' font-size='8' fill='#786CE5' text-anchor='middle'>writeObject()</text><rect x='300' y='30' width='160' height='80' rx='6' fill='#E9E8F8' stroke='#786CE5'/><text x='380' y='60' font-family='sans-serif' font-size='11' font-weight='700' fill='#786CE5' text-anchor='middle'>ObjectOutputStream</text><text x='380' y='80' font-family='monospace' font-size='9' fill='#19283D' text-anchor='middle'>Binary Byte Stream</text><path d='M 465 70 L 545 70' stroke='#28A994' stroke-width='2'/><rect x='550' y='30' width='120' height='80' rx='6' fill='#F7F8FC' stroke='#28A994'/><text x='610' y='65' font-family='sans-serif' font-size='11' font-weight='700' fill='#28A994' text-anchor='middle'>Disk Storage</text><text x='610' y='85' font-family='monospace' font-size='9' fill='#1B6F61' text-anchor='middle'>user.ser</text></svg>",
            "explanation": "Illustrates Object Serialization converting an active heap object into a persistent binary byte stream for disk storage.",
            "caption": "Figure E8.2: Java Object Serialization Data Flow"
        },
        "points": [
            {
                "point_no": 1,
                "heading": "Byte Streams vs Character Streams",
                "explanation": "Byte streams (InputStream/OutputStream) operate on 8-bit raw bytes for binary files (images/audio), whereas Character streams (Reader/Writer) process 16-bit Unicode characters for text files.",
                "terminology": "Byte Stream, Character Stream, Unicode Support, Charset Encoding.",
                "example": "FileInputStream reads binary JPGs; FileReader reads UTF-8 text documents."
            },
            {
                "point_no": 2,
                "heading": "Buffered I/O Performance Optimization",
                "explanation": "BufferedReader and BufferedWriter reduce costly OS disk read calls by buffering data chunks in 8KB memory arrays, supporting readLine() calls.",
                "terminology": "BufferedReader, BufferedWriter, I/O Buffering, readLine().",
                "example": "BufferedReader br = new BufferedReader(new FileReader('data.txt'));"
            },
            {
                "point_no": 3,
                "heading": "Object Serialization Mechanics",
                "explanation": "Serialization converts an active in-memory object graph into a sequence of binary bytes via ObjectOutputStream for file storage or network transport.",
                "terminology": "Serialization, Deserialization, ObjectOutputStream, ObjectInputStream.",
                "example": "oos.writeObject(student); persists student object state to disk."
            },
            {
                "point_no": 4,
                "heading": "Serializable Marker Interface and serialVersionUID",
                "explanation": "Classes must implement the empty java.io.Serializable marker interface and declare a static final long serialVersionUID to verify version compatibility during deserialization.",
                "terminology": "Serializable, Marker Interface, serialVersionUID, InvalidClassException.",
                "example": "private static final long serialVersionUID = 1L; guarantees class schema versioning."
            },
            {
                "point_no": 5,
                "heading": "Security Protection via the transient Keyword",
                "explanation": "Fields marked with the transient keyword are omitted during serialization, preventing sensitive plaintext secrets from being written to persistent storage.",
                "terminology": "transient Keyword, Field Masking, Secret Protection.",
                "example": "private transient String userPassword; ensures passwords are never saved to disk."
            }
        ],
        "conclusion": "Java provides versatile stream abstractions for binary and textual I/O, while serialization and the transient modifier preserve complex object graphs securely."
    },
    {
        "id": "exam_java_q9",
        "subject_id": "bcac502",
        "question_no": 9,
        "title": "Analyze the Java Collections Framework: ArrayList vs LinkedList and HashMap Internals.",
        "intro": {
            "definition": "The Java Collections Framework (JCF) is a unified architecture representing and manipulating collections of data objects independently of implementation details.",
            "background": "Engineered by Joshua Bloch in Java 1.2 to replace legacy Vector and Hashtable classes with standardized interfaces (List, Set, Map, Queue).",
            "significance": "Provides high-performance data structures essential for in-memory searching, caching, sorting, and algorithmic processing."
        },
        "diagram": {
            "svg": "<svg viewBox='0 0 700 140' xmlns='http://www.w3.org/2000/svg' style='width:100%;height:auto;background:#fff;border-radius:6px;border:1px solid #E5E9F1;'><rect x='30' y='30' width='160' height='80' rx='6' fill='#F7F8FC' stroke='#377FE6'/><text x='110' y='60' font-family='sans-serif' font-size='11' font-weight='700' fill='#377FE6' text-anchor='middle'>ArrayList</text><text x='110' y='80' font-family='sans-serif' font-size='9' fill='#19283D' text-anchor='middle'>Contiguous Array</text><text x='110' y='95' font-family='sans-serif' font-size='8' fill='#369B72' text-anchor='middle'>O(1) Random Access</text><rect x='220' y='30' width='160' height='80' rx='6' fill='#F7F8FC' stroke='#786CE5'/><text x='300' y='60' font-family='sans-serif' font-size='11' font-weight='700' fill='#786CE5' text-anchor='middle'>LinkedList</text><text x='300' y='80' font-family='sans-serif' font-size='9' fill='#19283D' text-anchor='middle'>Doubly-Linked Nodes</text><text x='300' y='95' font-family='sans-serif' font-size='8' fill='#786CE5' text-anchor='middle'>O(1) Head/Tail Insertion</text><rect x='410' y='30' width='260' height='80' rx='6' fill='#E9E8F8' stroke='#28A994'/><text x='540' y='60' font-family='sans-serif' font-size='11' font-weight='700' fill='#1B6F61' text-anchor='middle'>HashMap Internal Architecture</text><text x='540' y='80' font-family='sans-serif' font-size='9' fill='#19283D' text-anchor='middle'>Array of Node Buckets (Hashing)</text><text x='540' y='95' font-family='sans-serif' font-size='8' fill='#28A994' text-anchor='middle'>Treeified into Red-Black Tree at &gt;8 collisions</text></svg>",
            "explanation": "Contrasts contiguous memory in ArrayList with node pointers in LinkedList and bucket hashing in HashMap.",
            "caption": "Figure E9.2: Data Structure Memory Layouts in Java Collections Framework"
        },
        "points": [
            {
                "point_no": 1,
                "heading": "ArrayList Architectural Tradeoffs",
                "explanation": "ArrayList is backed by a dynamically resizing contiguous array. It provides instantaneous O(1) random index access via get(i), but slow O(n) element insertions and deletions due to array shifting.",
                "terminology": "Dynamic Array, Random Access, O(1) Lookup, Array Shifting.",
                "example": "list.get(50) accesses memory directly via base address + (index * size)."
            },
            {
                "point_no": 2,
                "heading": "LinkedList Architectural Tradeoffs",
                "explanation": "LinkedList is implemented as a doubly linked list of node wrappers. It excels at fast O(1) insertion and removal at head and tail, but requires O(n) sequential pointer traversal for index lookups.",
                "terminology": "Doubly Linked List, Node Pointer, O(n) Traversal, Memory Overhead.",
                "example": "LinkedList is optimal for FIFO queues and stack implementations."
            },
            {
                "point_no": 3,
                "heading": "HashMap Hashing and Bucket Index Calculation",
                "explanation": "HashMap stores key-value pairs inside an internal array of Node buckets. The bucket index is calculated via hash(key) & (n - 1), distributing entries across buckets.",
                "terminology": "Hash Function, Bucket Index, Bitwise AND Masking, Key-Value Entry.",
                "example": "int index = (key.hashCode() ^ (h >>> 16)) & (table.length - 1);"
            },
            {
                "point_no": 4,
                "heading": "Collision Resolution and Java 8 Treeification",
                "explanation": "Hash collisions store entries in linked chains. In Java 8, when a bucket exceeds 8 collisions and table capacity is 64+, the chain converts into a balanced Red-Black Tree, improving lookup from O(n) to O(log n).",
                "terminology": "Hash Collision, Red-Black Tree, Treeification Threshold (8), O(log n).",
                "example": "Treeification defends against Denial of Service (DoS) attacks exploiting hash collisions."
            },
            {
                "point_no": 5,
                "heading": "Load Factor and Rehashing Dynamics",
                "explanation": "When the number of stored entries exceeds capacity * load factor (default 0.75), HashMap doubles bucket capacity (rehash), re-indexing all entries to maintain O(1) operational performance.",
                "terminology": "Load Factor (0.75), Rehashing, Capacity Doubling, Threshold.",
                "example": "A 16-bucket map rehashes to 32 buckets upon storing its 13th key-value pair."
            }
        ],
        "conclusion": "The Java Collections Framework balances computational complexity against memory layouts, with HashMap treeification ensuring O(1) to O(log n) performance."
    },
    {
        "id": "exam_java_q10",
        "subject_id": "bcac502",
        "question_no": 10,
        "title": "Explain Java Generics, Type Erasure, and Wildcard Bounded Types.",
        "intro": {
            "definition": "Java Generics is a language facility providing compile-time type safety by allowing classes, interfaces, and methods to operate on parameterized types.",
            "background": "Introduced in Java 5 to eliminate widespread runtime ClassCastExceptions and abolish repetitive manual object type casting.",
            "significance": "Underpins type-safe collections, generic repository interfaces, and compile-time data validation in enterprise applications."
        },
        "diagram": {
            "svg": "<svg viewBox='0 0 700 140' xmlns='http://www.w3.org/2000/svg' style='width:100%;height:auto;background:#fff;border-radius:6px;border:1px solid #E5E9F1;'><rect x='30' y='30' width='280' height='80' rx='6' fill='#F7F8FC' stroke='#377FE6'/><text x='170' y='55' font-family='sans-serif' font-size='11' font-weight='700' fill='#377FE6' text-anchor='middle'>Compile-Time Source Code</text><text x='170' y='75' font-family='monospace' font-size='9' fill='#19283D' text-anchor='middle'>List&lt;String&gt; list = new ArrayList&lt;&gt;();</text><text x='170' y='95' font-family='sans-serif' font-size='8' fill='#369B72' text-anchor='middle'>Compiler verifies type safety (rejects non-strings)</text><path d='M 315 70 L 385 70' stroke='#786CE5' stroke-width='2'/><text x='350' y='60' font-family='sans-serif' font-size='8' fill='#786CE5' text-anchor='middle'>Erasure</text><rect x='390' y='30' width='280' height='80' rx='6' fill='#E9E8F8' stroke='#786CE5'/><text x='530' y='55' font-family='sans-serif' font-size='11' font-weight='700' fill='#786CE5' text-anchor='middle'>Runtime Bytecode (.class)</text><text x='530' y='75' font-family='monospace' font-size='9' fill='#19283D' text-anchor='middle'>List list = new ArrayList();</text><text x='530' y='95' font-family='sans-serif' font-size='8' fill='#617087' text-anchor='middle'>Type parameters replaced with Object or bounds</text></svg>",
            "explanation": "Illustrates Type Erasure converting parameterized generic source types into raw Object types in compiled bytecode.",
            "caption": "Figure E10.2: Java Generics Type Erasure Mechanism"
        },
        "points": [
            {
                "point_no": 1,
                "heading": "Compile-Time Type Safety Verification",
                "explanation": "Generics enforce strict type checking during compilation, rejecting incompatible object types before runtime execution.",
                "terminology": "Type Safety, Parameterized Type, Compile-Time Checking, Cast Elimination.",
                "example": "List<Integer> list = new ArrayList<>(); list.add('text') triggers compile-time error."
            },
            {
                "point_no": 2,
                "heading": "Mechanism of Type Erasure",
                "explanation": "To preserve binary backward compatibility with pre-Java 5 bytecode, the compiler erases all generic type parameters, replacing them with Object or bounding types in bytecode.",
                "terminology": "Type Erasure, Bytecode Compatibility, Raw Type, Synthetic Casts.",
                "example": "In compiled bytecode, `List<String>` and `List<Integer>` both execute as raw `List`."
            },
            {
                "point_no": 3,
                "heading": "Upper Bounded Wildcards (? extends T)",
                "explanation": "Upper bounded wildcards relax type restrictions, accepting type T or any of its subclasses. Follows the Producer Extends principle for read-only consumption.",
                "terminology": "Upper Bounded Wildcard, ? extends Number, Producer Extends (PECS).",
                "example": "public void printNumbers(List<? extends Number> list) accepts Integer or Double lists."
            },
            {
                "point_no": 4,
                "heading": "Lower Bounded Wildcards (? super T)",
                "explanation": "Lower bounded wildcards accept type T or any of its superclasses. Follows the Consumer Super principle, authorizing write operations into the collection.",
                "terminology": "Lower Bounded Wildcard, ? super Integer, Consumer Super (PECS).",
                "example": "public void addNumbers(List<? super Integer> list) allows adding Integer objects safely."
            },
            {
                "point_no": 5,
                "heading": "Generic Methods and Constructor Type Inference",
                "explanation": "Methods can declare independent type parameters (<T>) scoped to their invocation, allowing type inference without parameterizing the enclosing class.",
                "terminology": "Generic Method, Diamond Operator (<>), Type Inference.",
                "example": "public static <T> void swap(T[] arr, int i, int j) operates on any object array."
            }
        ],
        "conclusion": "Java Generics provide compile-time type safety without runtime performance penalties by leveraging Type Erasure and bounded wildcard flexibility."
    }
]
