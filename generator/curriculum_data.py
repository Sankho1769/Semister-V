# Curriculum data extracted directly from university syllabus PDFs

def get_curriculum():
    return {
        "university": {
            "name": "Maulana Abul Kalam Azad University of Technology, West Bengal",
            "former_name": "West Bengal University of Technology (WBUT)",
            "program": "Bachelor of Computer Applications (BCA) & Management Programs",
            "effective_session": "Effective from 2023-24 Academic Sessions",
            "semester": "SEMESTER: V",
            "credit_rules": [
                {"activity": "Lecture (L)", "weekly_hours": 1, "credit": 1, "rule": "1 HR LECTURE PER WEEK = 1 CREDIT"},
                {"activity": "Tutorial (T)", "weekly_hours": 1, "credit": 1, "rule": "1 HR TUTORIAL PER WEEK = 1 CREDIT"},
                {"activity": "Practical (P)", "weekly_hours": 2, "credit": 1, "rule": "2 HR PRACTICAL PER WEEK = 1 CREDIT"}
            ],
            "numbering_scheme": {
                "dept_code": "C (CORE MAJOR)",
                "subject_type": "CORE MAJOR",
                "semester": "V"
            }
        },
        "subjects": [
            {
                "id": "bcac501",
                "code": "BCAC501",
                "name": "PHP WITH MYSQL",
                "type": "Theory & Practical Lab",
                "category": "Core Major (C)",
                "credit": "5 (3L + 2P)",
                "credits_numeric": 5,
                "total_hours": 48,
                "theory_hours": 45,
                "internal_exam_hours": 3,
                "total_marks": 100,
                "theory_marks": 70,
                "internal_marks": 30,
                "practical_code": "BCAC591",
                "practical_name": "PHP WITH MYSQL LAB",
                "practical_credit": 2,
                "objective": "Equip students with the knowledge and skills necessary to design and develop dynamic, data-driven web applications. Learn fundamentals of server-side scripting using PHP, understand interaction with MySQL databases, and apply best practices in web development including security, error handling, and deploy modern applications using frameworks.",
                "outcomes": [
                    {"code": "CO1", "desc": "Understand the fundamentals of web development, PHP syntax, and MySQL database management."},
                    {"code": "CO2", "desc": "Develop dynamic web pages using PHP by incorporating server-side scripting and user input handling."},
                    {"code": "CO3", "desc": "Implement database-driven web applications by integrating PHP with MySQL to perform CRUD operations with proper session management and Error handling."},
                    {"code": "CO4", "desc": "Demonstrate knowledge of advanced PHP concepts such as OOP, security measures, and API integration."},
                    {"code": "CO5", "desc": "Design, develop, and deploy a web project using the PHP framework."}
                ],
                "module_count": 8,
                "modules_meta": [
                    {"module_no": 1, "title": "Introduction to Web Development & Setting up Environment", "hours": 4, "marks": 5},
                    {"module_no": 2, "title": "PHP Basics, Functions, Arrays and Strings", "hours": 8, "marks": 10},
                    {"module_no": 3, "title": "Forms Handling and User Input", "hours": 4, "marks": 5},
                    {"module_no": 4, "title": "PHP and MySQL Integration", "hours": 6, "marks": 10},
                    {"module_no": 5, "title": "Session Management, Authentication, File Handling & Security", "hours": 4, "marks": 15},
                    {"module_no": 6, "title": "Advanced PHP Concepts (OOP)", "hours": 5, "marks": 5},
                    {"module_no": 7, "title": "Introduction to PHP Frameworks", "hours": 6, "marks": 10},
                    {"module_no": 8, "title": "Laravel FrameWork", "hours": 8, "marks": 10}
                ],
                "books": [
                    "Gilmore, W. J. (2010). Beginning PHP and MySQL: From Novice to Professional (4th ed.). Apress.",
                    "Naramore, E., Gerner, J., Scouarnec, Y. L., Stolz, J., & Glass, M. (2005). Beginning PHP5, Apache, and MySQL Web Development. Wiley India Pvt. Ltd.",
                    "Welling, L., & Thomson, L. (2009). PHP and MySQL Web Development (4th ed.). Pearson Education.",
                    "Beighley, L., & Morrison, M. (2008). Head First PHP & MySQL. O'Reilly Media.",
                    "Powers, D., & McGrath, M. (2015). PHP & MySQL in Easy Steps. McGraw Hill Education.",
                    "Robson, E., & Freeman, E. (2007). Head First PHP & MySQL. O'Reilly Media.",
                    "Gosselin, D., Kokoska, R., & Easterbrooks, P. (2010). PHP Programming with MySQL: The Web Technologies Series (2nd ed.). Cengage Learning.",
                    "Sharma, V. (2017). PHP with MySQL: A Practical Approach. BPB Publications.",
                    "Narayan, N. (2016). PHP & MySQL: Server-side Web Development. McGraw Hill Education.",
                    "Zandstra, M. (2014). PHP Objects, Patterns, and Practice (4th ed.). Apress."
                ]
            },
            {
                "id": "bcac502",
                "code": "BCAC502",
                "name": "Object Oriented Programming with Java",
                "type": "Theory & Practical Lab",
                "category": "Core Major (C)",
                "credit": "5 (3L + 2P)",
                "credits_numeric": 5,
                "total_hours": 48,
                "theory_hours": 45,
                "internal_exam_hours": 3,
                "total_marks": 100,
                "theory_marks": 70,
                "internal_marks": 30,
                "practical_code": "BCAC592",
                "practical_name": "Object Oriented Programming with Java Lab",
                "practical_credit": 2,
                "objective": "Provide students with a comprehensive understanding of object-oriented programming principles and their application using Java. Equip students with skills needed to design, develop, and maintain robust, scalable software systems covering classes, inheritance, polymorphism, encapsulation, interfaces, abstract classes, exception handling, file I/O, serialization, and multithreading.",
                "outcomes": [
                    {"code": "CO1", "desc": "Understand and apply the fundamental concepts of Java programming, including data types, operators, control structures, and basic syntax, to develop simple applications."},
                    {"code": "CO2", "desc": "Demonstrate proficiency in object-oriented programming principles such as classes, objects, inheritance, polymorphism, encapsulation, and abstraction, to design and implement robust software solutions."},
                    {"code": "CO3", "desc": "Implement interfaces and abstract classes to create flexible and reusable code, enabling the development of modular and maintainable applications."},
                    {"code": "CO4", "desc": "Handle exceptions and errors in Java programs using try-catch blocks, custom exceptions, and other exception-handling mechanisms to ensure reliability and robustness of software."},
                    {"code": "CO5", "desc": "Perform file I/O operations and implement serialization in Java to persist data across different sessions."},
                    {"code": "CO6", "desc": "Understand and implement multithreading in Java to develop concurrent applications, improving performance and responsiveness."}
                ],
                "module_count": 9,
                "modules_meta": [
                    {"module_no": 1, "title": "Introduction to Java & JVM Architecture", "hours": 2, "marks": 5},
                    {"module_no": 2, "title": "Basics of Java Programming", "hours": 8, "marks": 10},
                    {"module_no": 3, "title": "Object-Oriented Programming Concepts", "hours": 6, "marks": 8},
                    {"module_no": 4, "title": "Inheritance and Polymorphism", "hours": 6, "marks": 10},
                    {"module_no": 5, "title": "Arrays and Strings", "hours": 6, "marks": 8},
                    {"module_no": 6, "title": "Interfaces and Abstract Classes", "hours": 4, "marks": 7},
                    {"module_no": 7, "title": "Exception Handling", "hours": 4, "marks": 8},
                    {"module_no": 8, "title": "File I/O and Serialization", "hours": 5, "marks": 6},
                    {"module_no": 9, "title": "Multithreading", "hours": 4, "marks": 8}
                ],
                "books": [
                    "Schildt, H. (2018). Java: The Complete Reference (11th ed.). McGraw Hill Education.",
                    "Horstmann, C. S., & Cornell, G. (2019). Core Java Volume I – Fundamentals (11th ed.). Pearson Education.",
                    "Balagurusamy, E. (2020). Object-Oriented Programming with Java (7th ed.). McGraw Hill Education.",
                    "Sierra, K., & Bates, B. (2005). Head First Java (2nd ed.). O'Reilly Media.",
                    "Deitel, P., & Deitel, H. (2018). Java: How to Program (11th ed.). Pearson Education.",
                    "Liang, Y. D. (2018). Introduction to Java Programming and Data Structures (11th ed.). Pearson Education.",
                    "Halterman, R. L. (2005). Object-Oriented Programming in Java. WCB/McGraw Hill.",
                    "Tanweer Alam (2021). Core JAVA. Khanna Publishing House.",
                    "Tanweer Alam (2020). Object Oriented Systems with Java 2.0. Khanna Publishing House.",
                    "Arunesh Goyal (2020). The Essentials of Java. Khanna Publishing House."
                ]
            },
            {
                "id": "mim502",
                "code": "MIM 502",
                "name": "Entrepreneurship",
                "type": "Theory",
                "category": "Management",
                "credit": "4",
                "credits_numeric": 4,
                "mode": "Offline",
                "total_hours": 48,
                "theory_hours": 40,
                "tutorial_hours": 8,
                "total_marks": 100,
                "objective": "Equip students with the knowledge, skills, and mindset necessary to start, manage, and grow their own business ventures. Identify and evaluate business opportunities, develop viable business plans, and understand financial, legal, ethical, and organizational assistance frameworks.",
                "outcomes": [
                    {"code": "CO1", "desc": "Students will be able to create a comprehensive and viable business plan, incorporating market research, financial projections, and operational strategies, demonstrating readiness to launch a new venture."},
                    {"code": "CO2", "desc": "Students will demonstrate the ability to identify, evaluate, and select profitable business opportunities using analytical tools and techniques."},
                    {"code": "CO3", "desc": "Students will acquire skills to manage the financial aspects of a startup, including budgeting, fundraising, cash flow management, and financial statement analysis."},
                    {"code": "CO4", "desc": "Students will showcase ability to apply innovative thinking and problem-solving skills to overcome challenges in the entrepreneurial process."},
                    {"code": "CO5", "desc": "Students will be able to make informed and ethical business decisions considering legal implications, social responsibility, and strategic goals."}
                ],
                "module_count": 5,
                "modules_meta": [
                    {"module_no": 1, "title": "Introduction to Entrepreneurship", "hours": 10, "weightage": "30%", "bloom": "1, 2"},
                    {"module_no": 2, "title": "Introduction to entrepreneur", "hours": 6, "weightage": "20%", "bloom": "1, 2, 3"},
                    {"module_no": 3, "title": "Entrepreneurial Motivation", "hours": 7, "weightage": "10%", "bloom": "1, 2, 3"},
                    {"module_no": 4, "title": "Project Management", "hours": 7, "weightage": "20%", "bloom": "1, 2, 3"},
                    {"module_no": 5, "title": "Organisation Assistance", "hours": 10, "weightage": "20%", "bloom": "2, 3"}
                ],
                "books": [
                    "Entrepreneurship – Anindita Sarkar – Taurean Publications",
                    "Entrepreneurship Development and Project Management – Dr. Dilip M. Sarwate – Everest Publishing House"
                ]
            },
            {
                "id": "mim501",
                "code": "MIM501",
                "name": "FINANCIAL MANAGEMENT",
                "type": "Theory",
                "category": "Management",
                "credit": "4",
                "credits_numeric": 4,
                "mode": "Offline",
                "total_hours": 48,
                "theory_hours": 40,
                "tutorial_hours": 8,
                "total_marks": 100,
                "objective": "Attain a comprehensive understanding of the basics of Financial Management and its application. Understand financial allocation, tools of finance departments, investment decisions, financing decisions, dividend decisions, capital budgeting, leverage analysis, working capital, and valuation of investment proposals.",
                "outcomes": [
                    {"code": "CO1", "desc": "Equips students with foundational knowledge in Financial Management and cost of capital determination."},
                    {"code": "CO2", "desc": "Students will know the fundamentals of a financial plan and corporate final accounts analysis."},
                    {"code": "CO3", "desc": "Facilitates active learning regarding capital budgeting and emerging financial management trends."},
                    {"code": "CO4", "desc": "Furnishes students with decision-making skills relevant to leverage, risk appraisal, and capital structure."},
                    {"code": "CO5", "desc": "Equips students to find solutions to financial challenges, dividend decisions, and working capital optimization."}
                ],
                "module_count": 7,
                "modules_meta": [
                    {"module_no": 1, "title": "Introduction: Concepts, Scope, Functions & Cost of Capital", "hours": 6, "weightage": "15%", "bloom": "1, 2"},
                    {"module_no": 2, "title": "Analysis and Interpretation of Corporate Final Accounts", "hours": 6, "weightage": "15%", "bloom": "1, 2, 3"},
                    {"module_no": 3, "title": "Capital Budgeting", "hours": 4, "weightage": "10%", "bloom": "1, 2"},
                    {"module_no": 4, "title": "Leverage Analysis & Capital Structure Theories", "hours": 6, "weightage": "15%", "bloom": "1, 2, 3"},
                    {"module_no": 5, "title": "Investment Decisions & Risk Appraisal", "hours": 6, "weightage": "15%", "bloom": "1, 2, 3"},
                    {"module_no": 6, "title": "Dividend Policies", "hours": 6, "weightage": "15%", "bloom": "1, 2, 3"},
                    {"module_no": 7, "title": "Management of Working Capital", "hours": 6, "weightage": "15%", "bloom": "1, 2, 3"}
                ],
                "books": [
                    "'Financial Management: Theory and Practice' by Prasanna Chandra",
                    "'Financial Management' by I. M. Pandey",
                    "'Financial Management: Principles and Applications' by S. N. Maheshwari",
                    "'Strategic Financial Management' by Ravi M. Kishore",
                    "'Financial Management: Text, Problems and Cases' by M. Y. Khan and P. K. Jain"
                ]
            }
        ],
        "practicals": [
            {
                "id": "bcac591",
                "code": "BCAC591",
                "name": "PHP WITH MYSQL LAB",
                "subject_ref": "bcac501",
                "credit": 2,
                "instruction": "The practical classes should comprehensively cover the theoretical syllabus, including the implementation of a small-scale project to enhance conceptual understanding and enable students to learn how to apply their knowledge to solve real-world problems.",
                "sample_cases": [
                    {"case_no": 1, "title": "User Registration and Login System", "description": "Develop a PHP and MySQL-based system where users can register with username/password, and log in to access profile with secure password hashing."},
                    {"case_no": 2, "title": "Content Management System (CMS)", "description": "Design a blog CMS in PHP/MySQL where authors log in, create, edit, delete posts, and display structured articles to the public."},
                    {"case_no": 3, "title": "Online Voting System", "description": "Create a voting system where users register, cast votes for candidates, and view results with strict single-vote enforcement."},
                    {"case_no": 4, "title": "E-commerce Product Catalog", "description": "Implement a product catalog where users browse by category, search specific products, and inspect pricing and descriptions."},
                    {"case_no": 5, "title": "Event Management System", "description": "Develop an event management system where users register for events, view schedules, and inspect participant rosters."},
                    {"case_no": 6, "title": "Forum or Discussion Board", "description": "Build a community forum where users create discussion threads, reply to topics, and manage posts with user authentication."}
                ]
            },
            {
                "id": "bcac592",
                "code": "BCAC592",
                "name": "Object Oriented Programming with Java Lab",
                "subject_ref": "bcac502",
                "credit": 2,
                "instruction": "The practical classes should comprehensively cover the theoretical syllabus, including the implementation of a small-scale project to enhance conceptual understanding and enable students to learn how to apply their knowledge to solve real-world problems.",
                "sample_cases": [
                    {"case_no": 1, "title": "Library Book Issuing and Returning System", "description": "Automate book issuing/returning with classes Book, Library, Member, tracking available and borrowed titles."},
                    {"case_no": 2, "title": "Payroll System for Employee Salary", "description": "Calculate employee salaries based on hours worked and hourly rate, generating payroll reports with class Employee."},
                    {"case_no": 3, "title": "Bank Account and Transaction Management", "description": "Manage accounts with deposit, withdrawal, balance inquiry, and custom InsufficientBalanceException handling."},
                    {"case_no": 4, "title": "Vehicle Rental Service Hierarchy", "description": "Base class Vehicle with derived Car, Bike, Truck implementing rental availability, rent, and return methods."},
                    {"case_no": 5, "title": "Warehouse Inventory Tracking System", "description": "Track stock levels, adding items, updating stock, and generating inventory reports with classes Item, Inventory, Warehouse."},
                    {"case_no": 6, "title": "Hotel Room Reservation System", "description": "Design classes Room, Hotel, Reservation to check room availability, book rooms, and display reservation details."}
                ]
            }
        ]
    }
