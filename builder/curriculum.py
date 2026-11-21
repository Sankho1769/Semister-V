# Curriculum data extracted directly from university syllabus PDFs

UNIVERSITY_INFO = {
    "name": "Maulana Abul Kalam Azad University of Technology, West Bengal",
    "former_name": "West Bengal University of Technology (WBUT)",
    "program": "Bachelor of Computer Applications (BCA) & Management Programs",
    "effective_session": "2023-24 Academic Sessions Onwards",
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
}

SUBJECTS = [
    {
        "id": "bcac501",
        "name": "PHP WITH MYSQL",
        "code": "BCAC501",
        "category": "Core Major (C)",
        "credit": "5 (3L + 2P)",
        "mode": "Lecture & Practical Lab",
        "total_hours": 48,
        "theory_hours": 45,
        "internal_exam_hours": 3,
        "total_marks": 100,
        "theory_marks": 70,
        "internal_marks": 30,
        "practical_code": "BCAC591",
        "practical_name": "PHP WITH MYSQL LAB",
        "practical_credit": 2,
        "objective": "Equip students with the knowledge and skills necessary to design and develop dynamic, data-driven web applications. Learn fundamentals of server-side scripting using PHP, MySQL interaction, security, error handling, and deploy modern applications using frameworks.",
        "course_outcomes": [
            {"code": "CO1", "desc": "Understand the fundamentals of web development, PHP syntax, and MySQL database management."},
            {"code": "CO2", "desc": "Develop dynamic web pages using PHP by incorporating server-side scripting and user input handling."},
            {"code": "CO3", "desc": "Implement database-driven web applications by integrating PHP with MySQL to perform CRUD operations with proper session management and Error handling."},
            {"code": "CO4", "desc": "Demonstrate knowledge of advanced PHP concepts such as OOP, security measures, and API integration."},
            {"code": "CO5", "desc": "Design, develop, and deploy a web project using the PHP framework."}
        ],
        "books": [
            "Gilmore, W. J. (2010). Beginning PHP and MySQL: From Novice to Professional (4th ed.). Apress.",
            "Naramore, E., Gerner, J., Scouarnec, Y. L., Stolz, J., & Glass, M. (2005). Beginning PHP5, Apache, and MySQL Web Development. Wiley India Pvt. Ltd.",
            "Welling, L., & Thomson, L. (2009). PHP and MySQL Web Development (4th ed.). Pearson Education.",
            "Beighley, L., & Morrison, M. (2008). Head First PHP & MySQL. O\'Reilly Media.",
            "Powers, D., & McGrath, M. (2015). PHP & MySQL in Easy Steps. McGraw Hill Education.",
            "Robson, E., & Freeman, E. (2007). Head First PHP & MySQL. O\'Reilly Media.",
            "Gosselin, D., Kokoska, R., & Easterbrooks, P. (2010). PHP Programming with MySQL: The Web Technologies Series (2nd ed.). Cengage Learning.",
            "Sharma, V. (2017). PHP with MySQL: A Practical Approach. BPB Publications.",
            "Narayan, N. (2016). PHP & MySQL: Server-side Web Development. McGraw Hill Education.",
            "Zandstra, M. (2014). PHP Objects, Patterns, and Practice (4th ed.). Apress."
        ]
    },
    {
        "id": "bcac502",
        "name": "Object Oriented Programming with Java",
        "code": "BCAC502",
        "category": "Core Major (C)",
        "credit": "5 (3L + 2P)",
        "mode": "Lecture & Practical Lab",
        "total_hours": 48,
        "theory_hours": 45,
        "internal_exam_hours": 3,
        "total_marks": 100,
        "theory_marks": 70,
        "internal_marks": 30,
        "practical_code": "BCAC592",
        "practical_name": "Object Oriented Programming with Java Lab",
        "practical_credit": 2,
        "objective": "Provide students with a comprehensive understanding of object-oriented programming principles and their application using Java. Equip students to design, develop, and maintain robust, scalable software systems covering classes, objects, inheritance, polymorphism, encapsulation, interfaces, abstract classes, file I/O, serialization, and multithreading.",
        "course_outcomes": [
            {"code": "CO1", "desc": "Understand and apply the fundamental concepts of Java programming, including data types, operators, control structures, and basic syntax, to develop simple applications."},
            {"code": "CO2", "desc": "Demonstrate proficiency in object-oriented programming principles such as classes, objects, inheritance, polymorphism, encapsulation, and abstraction, to design and implement robust software solutions."},
            {"code": "CO3", "desc": "Implement interfaces and abstract classes to create flexible and reusable code, enabling the development of modular and maintainable applications."},
            {"code": "CO4", "desc": "Handle exceptions and errors in Java programs using try-catch blocks, custom exceptions, and other exception-handling mechanisms to ensure the reliability and robustness of software."},
            {"code": "CO5", "desc": "Perform file I/O operations and implement serialization in Java to persist data, enabling the storage and retrieval of information across different sessions."},
            {"code": "CO6", "desc": "Understand and implement multithreading in Java to develop applications that perform multiple tasks concurrently, improving performance and responsiveness."}
        ],
        "books": [
            "Schildt, H. (2018). Java: The Complete Reference (11th ed.). McGraw Hill Education.",
            "Horstmann, C. S., & Cornell, G. (2019). Core Java Volume I – Fundamentals (11th ed.). Pearson Education.",
            "Balagurusamy, E. (2020). Object-Oriented Programming with Java (7th ed.). McGraw Hill Education.",
            "Sierra, K., & Bates, B. (2005). Head First Java (2nd ed.). O\'Reilly Media.",
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
        "name": "Entrepreneurship",
        "code": "MIM 502",
        "category": "Management",
        "credit": "4",
        "mode": "Offline",
        "total_hours": 48,
        "theory_hours": 40,
        "tutorial_hours": 8,
        "total_marks": 100,
        "objective": "Equip students with the knowledge, skills, and mindset necessary to start, manage, and grow business ventures. Identify and evaluate opportunities, develop comprehensive business plans, and understand financial, legal, and organizational assistance frameworks.",
        "course_outcomes": [
            {"code": "CO1", "desc": "Students will be able to create a comprehensive and viable business plan, incorporating market research, financial projections, and operational strategies, demonstrating their readiness to launch a new venture."},
            {"code": "CO2", "desc": "Student will demonstrate the ability to identify, evaluate, and select profitable business opportunities, using analytical tools and techniques to assess market needs and potential risks."},
            {"code": "CO3", "desc": "Students will acquire the skills to manage the financial aspects of a startup, including budgeting, fundraising, cash flow management, and financial statement analysis, ensuring financial sustainability."},
            {"code": "CO4", "desc": "Students will showcase their ability to apply innovative thinking and problem-solving skills to overcome challenges in the entrepreneurial process, developing unique value-adding solutions."},
            {"code": "CO5", "desc": "Students will be able to make informed and ethical business decisions, considering legal implications, social responsibility, and long-term strategic goals in managing entrepreneurial ventures."}
        ],
        "books": [
            "Entrepreneurship – Anindita Sarkar – Taurean Publications",
            "Entrepreneurship Development and Project Management – Dr. Dilip M. Sarwate – Everest Publishing House"
        ]
    },
    {
        "id": "mim501",
        "name": "FINANCIAL MANAGEMENT",
        "code": "MIM501",
        "category": "Management",
        "credit": "4",
        "mode": "Offline",
        "total_hours": 48,
        "theory_hours": 40,
        "tutorial_hours": 8,
        "total_marks": 100,
        "objective": "Attain a comprehensive understanding of the basics of Financial Management and its application. Master investment, financing, and dividend decisions, capital structure theories, leverage analysis, working capital management, and project appraisal.",
        "course_outcomes": [
            {"code": "CO1", "desc": "This course equips students with foundational knowledge in Financial Management and cost of capital determination."},
            {"code": "CO2", "desc": "Through this course, students will know the fundamentals of financial plans and corporate final accounts analysis."},
            {"code": "CO3", "desc": "The course will facilitate active learning and acquiring knowledge regarding capital budgeting and emerging financial management trends."},
            {"code": "CO4", "desc": "The course is designed to furnish students with decision-making skills relevant to leverage, risk appraisal, and capital structure."},
            {"code": "CO5", "desc": "Upon completing this course, students will be equipped to find solutions to financial challenges, dividend decisions, and working capital optimization."}
        ],
        "books": [
            ""Financial Management: Theory and Practice" by Prasanna Chandra",
            ""Financial Management" by I. M. Pandey",
            ""Financial Management: Principles and Applications" by S. N. Maheshwari",
            ""Strategic Financial Management" by Ravi M. Kishore",
            ""Financial Management: Text, Problems and Cases" by M. Y. Khan and P. K. Jain"
        ]
    }
]
