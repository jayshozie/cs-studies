# Comprehensive Computer Science and Computer Engineering Learning Curriculum:
# A Phased Approach

This curriculum is designed to provide a comprehensive and rigorous
understanding of both Computer Science and Computer Engineering
fundamentals, progressing from foundational mathematics and programming to
advanced systems, applications, and specialized fields.

---

## Phase 1: Foundational Mathematics & Core Programming
*(This phase establishes the mathematical and logical bedrock, along with your
primary programming language for initial implementation.)*

1.  **Discrete Mathematics**
    * [x] Logic (Propositional & Predicate)
        * **Depth Defined:**
            * **Propositional Logic:** Master propositions, logical connectives, truth tables, identifying tautologies/contradictions/contingencies, logical equivalence (including De Morgan's Laws, Distributive Laws), and converting to Conjunctive Normal Form (CNF) and Disjunctive Normal Form (DNF). Fluency in translating between complex English statements and logical expressions.
            * **Predicate Logic:** Master predicates, universal ($\forall$) and existential ($\exists$) quantifiers, defining domains. Strong understanding of nested quantifiers and their interpretation. Proficiency in negating quantified statements. Basic understanding of rules of inference for both propositional and predicate logic, leading into formal proofs.
    * [x] Set Theory
        * **Depth Defined:**
            * **Mastery of Basics & Operations:** Fluency with definitions (sets, elements, well-defined, empty set, cardinality, roster/set-builder notation) and fundamental operations ($\cup, \cap, \setminus, A^c$).
            * **Visualizations:** Effective use of Venn diagrams.
            * **Set Identities & Proofs:** Formal proofs of set identities (e.g., De Morgan's Laws for sets, distributive laws for sets) using element-wise proofs, Venn diagrams, or logical equivalences.
            * **Advanced Concepts:** Power Sets ($P(A)$) and Cartesian Products ($A \times B$).
            * **Introductory Functions & Relations:** Understanding functions as special types of relations (injective, surjective, bijective) as grounded in set theory.
            * **Cardinality of Infinite Sets (Brief):** Conceptual understanding of countable vs. uncountable sets.
    * [ ] Combinatorics
        * **Depth Defined:**
            * **Mastery of Fundamentals:** Fluency in applying the Fundamental Principle of Counting, Permutations (order matters, with/without repetition), and Combinations (order doesn't matter, with/without repetition).
            * **Advanced Counting Principles:** Understanding and applying the Pigeonhole Principle and the Inclusion-Exclusion Principle.
            * **Binomial Theorem:** Understanding its relation to combinations and expanding binomial expressions.
            * **Basic Recurrence Relations (Introductory):** Formulating and solving simple linear recurrence relations.
    * [ ] Graph Theory
        * **Depth Defined:**
            * **Basic Definitions:** Vertices, edges (directed/undirected, weighted), loops, multiple edges, simple graphs, degree.
            * **Types of Graphs:** Complete ($K_n$), cycles ($C_n$), paths ($P_n$), wheels ($W_n$), bipartite graphs.
            * **Representations:** Adjacency matrices and adjacency lists (pros/cons).
            * **Connectivity:** Paths, cycles, connectedness, components, bridges, articulation points.
            * **Graph Traversal Algorithms:** Breadth-First Search (BFS) and Depth-First Search (DFS) (mechanisms, properties).
            * **Trees:** Definition, properties, rooted trees.
            * **Spanning Trees:** Definition and conceptual understanding of Minimum Spanning Trees (MSTs).
            * **Eulerian and Hamiltonian Paths/Circuits (Introductory):** Definitions and basic conditions/theorems.
            * **Planar Graphs:** Definition and Euler's formula for planar graphs.
    * [ ] Proof Techniques (Direct, Contrapositive, Contradiction, Mathematical Induction)
        * **Depth Defined:**
            * **Importance:** Understanding the necessity of proofs in CS and mathematics.
            * **Mastery of Techniques:** Direct Proof, Proof by Contraposition, Proof by Contradiction, Proof by Cases.
            * **Mathematical Induction (Strong Emphasis):** Mastery of the Principle of Mathematical Induction (base case, inductive hypothesis, inductive step) and Strong Induction. Application to proving properties of integers, sequences, sums, inequalities, algorithms, and data structures.
            * **Disproof by Counterexample:** Understanding how to disprove universal statements.
            * **Proof Structures/Pitfalls:** Recognizing valid/invalid arguments and common logical fallacies.
    * **Recommended Textbooks:**
        * "Discrete Mathematics and Its Applications" by Kenneth H. Rosen
        * "Discrete Mathematics" by Richard Johnsonbaugh
        * "Introduction to Graph Theory" by Douglas B. West (Specific to Graph Theory)
        * "Introduction to Graph Theory" by Richard J. Trudeau (Specific to Graph Theory, very accessible)
2.  **Probability and Statistics**
    * [ ] Probability Theory (Sample Spaces, Events, Conditional Probability, Random Variables, Probability Distributions)
        * **Depth Defined:**
            * **Foundations:** Sample Spaces, Events, Axioms of Probability. Application of Combinatorics for probability calculation.
            * **Key Probability Concepts:** Conditional Probability, Independence, Bayes' Theorem (derivation and application).
            * **Random Variables:** Discrete and Continuous Random Variables, Probability Mass Functions (PMF), Probability Density Functions (PDF), Cumulative Distribution Functions (CDF).
            * **Expectation & Variance:** Calculation and properties for various random variables.
            * **Common Distributions:** Bernoulli, Binomial, Poisson, Geometric (discrete); Uniform, Exponential, Normal (continuous) - understanding properties and applications.
            * **Joint Probability Distributions (Introductory):** Concepts of covariance and correlation.
    * [ ] Statistical Inference (Estimation, Hypothesis Testing, Confidence Intervals)
        * **Depth Defined:**
            * **Sampling:** Sampling and Sampling Distributions, Central Limit Theorem (conceptual understanding).
            * **Estimation:** Point Estimation, Confidence Intervals (construction and interpretation for means and proportions).
            * **Hypothesis Testing:** Fundamentals (Null/Alternative Hypotheses, Type I/II errors, p-values, significance levels). Common tests: Z-tests, T-tests, Chi-squared tests (application and interpretation).
    * [ ] Regression Analysis (basics)
        * **Depth Defined:**
            * **Simple Linear Regression:** Model understanding, least squares method.
            * **Interpretation:** Coefficients, R-squared.
            * **Assumptions:** Awareness of basic assumptions.
    * **Recommended Textbooks:**
        * "A First Course in Probability" by Sheldon Ross
        * "Probability and Statistics for Engineering and the Sciences" by Jay L. Devore
        * "Head First Statistics" by Dawn Griffiths (More interactive/beginner-friendly)
3.  **Python Programming**
    * [x] Basics (syntax, data types, control structures, functions)
        * **Depth Defined:** Fluent in fundamental syntax, built-in data types (numbers, strings, booleans, lists, tuples, dictionaries, sets), control flow, and defining/using functions (parameters, return values, scope). Understanding mutability/immutability.
    * [ ] Libraries: `numpy`, `scipy`, `matplotlib`, `sympy`, `pandas`
        * **Depth Defined:** Practical application for scientific computing, data analysis, visualization, and symbolic mathematics. Mastery of array manipulation (`numpy`), data manipulation (`pandas`), plotting (`matplotlib`), numerical routines (`scipy`), and symbolic math (`sympy`). Emphasis on *using* these libraries to solve CS/engineering problems.
    * [x] Advanced Python: File handling, Error handling, Object-Oriented Programming (OOP)
        * **Depth Defined:** Reading/writing to files (text/binary). Effective use of `try-except-finally`. Mastery of OOP core concepts (classes, objects, attributes, methods) and pillars (Encapsulation, Inheritance, Polymorphism) with practical application. Understanding special methods (`__init__`, `__str__`).
    * [ ] Automation and scripting with Python
        * **Depth Defined:** Writing practical scripts for tasks (file manipulation, basic web scraping). Parsing command-line arguments. Understanding and using `pip` and `venv` for environment/dependency management.
    * **Recommended Textbooks/Resources:**
        * "Python Crash Course" by Eric Matthes (Excellent for beginners)
        * "Automate the Boring Stuff with Python" by Al Sweigart (Practical scripting focus)
        * "Fluent Python" by Luciano Ramalho (For intermediate/advanced)
4.  **C/C++ Programming**
    * [ ] Basics of C: variables, data types, control structures, functions
        * **Depth Defined:** Fluent in C's fundamental syntax, primitive data types, control flow, functions (declarations, definitions, parameters, return types, recursion, scope). Understanding the compilation process.
    * [ ] Pointers, memory management, and file I/O
        * **Depth Defined:** **Deep Understanding** of pointers (arithmetic, dereferencing, void pointers, function pointers, pointers to pointers, `const` with pointers). Mastery of dynamic memory allocation (`malloc`, `calloc`, `realloc`, `free`), understanding stack/heap/static memory, and common memory errors. Proficient C-style file I/O.
    * [ ] Object-Oriented Programming in C++
        * **Depth Defined:** **Deep Understanding** of OOP principles: Classes, objects, constructors (default, parameterized, copy, move), destructors (virtual). Rule of Three/Five/Zero. Inheritance (single, multiple, virtual), Polymorphism (function/operator overloading, virtual functions, abstract classes, interfaces, dynamic vs. static binding). Friend functions/classes, static members, `this` pointer.
    * [ ] Applications: numerical methods, simulations, and performance-critical tasks
        * **Depth Defined:** Understanding *why* C/C++ is used for performance-critical applications. Practical implementation of algorithms (numerical methods, data processing).
    * [ ] Advanced C++ Memory Management & RAII
        * **Depth Defined:** Mastery of `new`/`delete`. **Crucial understanding and application of RAII.** In-depth knowledge and practical use of `std::unique_ptr`, `std::shared_ptr`, `std::weak_ptr` for modern C++ resource management.
    * [ ] Templates and Generic Programming
        * **Depth Defined:** **Deep Understanding** of function and class templates, template instantiation/specialization. Introduction to Variadic Templates and Concepts (C++20).
    * [ ] Standard Template Library (STL)
        * **Depth Defined:** **Extensive Mastery** of STL containers (sequence, associative, unordered associative, adapters), iterators (types, invalidation), algorithms (extensive use and understanding of complexity), function objects (functors) and Lambdas.
    * [ ] Error Handling and Exceptions
        * **Depth Defined:** Mastery of `try`, `catch`, `throw`. Understanding exception hierarchy, custom exceptions, exception safety guarantees, `noexcept`.
    * [ ] File I/O in C++ (`fstream`)
        * **Depth Defined:** Proficient use of `ifstream`, `ofstream`, `fstream` for text and binary I/O, file pointers (`seekg`, `tellg`, `seekp`, `tellp`).
    * [ ] Concurrency and Parallelism
        * **Depth Defined:** Understanding `std::thread`, synchronization primitives (`std::mutex`, `std::lock_guard`, `std::condition_variable`). Atomic operations. `std::async`, `std::future`, `std::promise`. Awareness of concurrency issues (race conditions, deadlocks).
    * [ ] Modern C++ Features (C++11 onwards)
        * **Depth Defined:** Practical understanding of `auto`, `decltype`, rvalue references/move semantics (`std::move`, `std::forward`), lambda expressions, `nullptr`, `constexpr`, `if constexpr`, structured bindings (C++17), three-way comparison (C++20).
    * [ ] Build Systems, Debugging, and Tools
        * **Depth Defined:** Understanding compiler flags (`g++`, `clang++`), basic Makefiles, practical introduction to CMake, effective use of debuggers (`gdb` basics), conceptual understanding of profilers (`perf`, `Valgrind`).
    * [ ] C++ Best Practices & Idioms
        * **Depth Defined:** Adherence to RAII principle. Application of "Effective C++" guidelines for robust, efficient, and maintainable code. Awareness of coding style guides. Introduction to unit testing principles.
    * **Recommended Textbooks:**
        * "The C Programming Language" by Brian W. Kernighan and Dennis M. Ritchie (K&R - The classic, essential for C)
        * "Programming: Principles and Practice Using C++" by Bjarne Stroustrup (C++ creator's comprehensive intro)
        * "Effective C++" by Scott Meyers (For intermediate C++ best practices)
        * "Effective Modern C++" by Scott Meyers (For C++11/14 best practices)
        * "C++ Primer" by Stanley B. Lippman, Josée Lajoie, Barbara E. Moo (Comprehensive reference)
        * "Professional C++" by Marc Gregoire et al. (Practical, modern C++)
5.  **Version Control with Git**
    * [x] All Basic Commands: `init`, `add`, `commit`, `log`, `branch`, `merge`, `push`, `pull`.
        * **Depth Defined:** Mastery of all basic commands.
    * [x] Git Workflow: Deep understanding of the typical development cycle.
        * **Depth Defined:** Strong practical foundation in Git for individual and basic team development.
    * [x] Conflict Resolution: Proficiency in resolving merge conflicts.
        * **Depth Defined:** Mastering merge conflicts.
    * [x] Inspecting History: Advanced use of `git log` (filtering, formatting).
        * **Depth Defined:** Proficient use of `git log`, `git status`, `git diff`.
    * [ ] Undoing Changes: Mastering `git restore` (or `git checkout` for files), `git revert`, and `git reset` (soft, mixed, hard).
        * **Depth Defined:** Mastery of `git restore`, `git revert`, `git reset` for undoing changes.
    * [ ] Branch Management: Creating, deleting, and listing branches.
        * **Depth Defined:** Proficient branch management.
    * [ ] Remote Repositories: Adding, removing, and interacting with remotes.
        * **Depth Defined:** Mastery of remote interaction.
    * [ ] Tagging: Using tags to mark specific points in history.
        * **Depth Defined:** Understanding and using tags.
    * [ ] Ignoring Files: Using `.gitignore`.
        * **Depth Defined:** Effective use of `.gitignore`.
    * [ ] Stashing: Using `git stash` to temporarily save changes.
        * **Depth Defined:** Proficient use of `git stash`.
    * [ ] Rebasing (Introductory): Understanding the basics of `git rebase` and when it might be preferable to `git merge`.
        * **Depth Defined:** Basic understanding of `git rebase`.
    * [ ] Conceptual Understanding: A solid understanding of Git's distributed nature.
        * **Depth Defined:** Solid conceptual understanding of Git's distributed nature.
    * **Recommended Textbooks/Resources:**
        * "Pro Git" by Scott Chacon and Ben Straub (Freely available online, comprehensive)
        * "Version Control with Git" by Jon Loeliger and Matthew McCullough (O'Reilly, practical guide)
    *(Note: Linear Algebra and Multivariable Calculus are covered by your
    university courses: Math 120, ES202)*

---

## Phase 2: Core Computer Science Theory & Data Structures
*(This phase builds directly on the mathematical foundation, diving into how
data is organized and fundamental computational theory.)*

6.  **Data Structures and Algorithms**
    * [ ] Core data structures: arrays, linked lists (singly, doubly,
          circular), stacks, queues, hash tables, trees (binary, BST,
          heaps), graphs
    * [ ] Algorithms: sorting, searching, recursion, dynamic programming,
          basic graph algorithms (traversal: BFS, DFS)
    * [ ] Time and space complexity (Big-O notation)
    * **Recommended Textbooks:**
        * "Introduction to Algorithms" by Thomas H. Cormen, Charles E.
          Leiserson, Ronald L. Rivest, Clifford Stein (CLRS - The
          definitive comprehensive text)
        * "Algorithms (4th Edition)" by Robert Sedgewick and Kevin Wayne
          (Excellent for applications, Java-based but concepts universal)
        * "Data Structures and Algorithms in Python" by Michael T.
          Goodrich, Roberto Tamassia, Michael H. Goldwasser (Python-specific)
7.  **Advanced Algorithms**
    * [ ] Topics typically include: Network flow, Linear Programming,
          Approximation Algorithms, Randomized Algorithms, Computational
          Geometry, String Algorithms, deeper Complexity Theory
    * **Recommended Textbooks:**
        * "Algorithm Design" by Jon Kleinberg and Éva Tardos
        * "Algorithms" by Sanjoy Dasgupta, Christos Papadimitriou, Umesh
          Vazirani
8.  **Theory of Computation / Formal Languages & Automata**
    * [ ] Automata Theory (Finite Automata, Pushdown Automata, Turing
          Machines)
    * [ ] Formal Languages (Regular Expressions, Context-Free Grammars)
    * [ ] Computability Theory (Halting Problem, Undecidability)
    * [ ] Complexity Theory (P, NP, NP-complete)
    * **Recommended Textbooks:**
        * "Introduction to the Theory of Computation" by Michael Sipser
          (Standard, highly regarded)
        * "Elements of the Theory of Computation" by Harry Lewis and
          Christos Papadimitriou

---

## Phase 3: Deep Dive into Computer Systems (Hardware-Software Interface)
*(This phase explores how computers fundamentally work, from the CPU to the
operating system, and how software translates to hardware instructions.)*

9.  **Digital Logic Design / Digital Systems**
    * [ ] Boolean Algebra, Logic Gates (AND, OR, NOT, XOR, etc.)
    * [ ] Combinational Logic (Adders, Multiplexers, Decoders)
    * [ ] Sequential Logic (Flip-flops, Registers, Counters)
    * [ ] Finite State Machines (FSMs)
    * [ ] Memory elements (RAM, ROM basics)
    * **Recommended Textbooks:**
        * "Digital Design" by M. Morris Mano and Michael D. Ciletti
        * "Fundamentals of Digital Logic with VHDL Design" by Stephen Brown
          and Zvonko Vranesic
10. **Computer Architecture**
    * [ ] CPU Components (Control Unit, ALU, Registers)
    * [ ] Instruction Set Architecture (ISA)
    * [ ] Memory Addressing, Memory Hierarchy (Cache, RAM, Virtual Memory
          concepts)
    * [ ] Fetch-Decode-Execute Cycle
    * [ ] Basic I/O Mechanisms
    * **Recommended Textbooks:**
        * "Computer Organization and Design: The Hardware/Software
          Interface" by David A. Patterson and John L. Hennessy (P&H -
          Classic, widely used)
        * "Computer Architecture: A Quantitative Approach" by John L.
          Hennessy and David A. Patterson (More advanced than COD)
11. **Assembly Language**
    * [ ] Processor-specific assembly (e.g., x86 or ARM basics)
    * [ ] Registers, Instructions, Memory Access
    * [ ] Calling conventions, Function calls
    * [ ] **Recommended Textbooks:**
        * "Assembly Language for Intel-Based Computers" by Kip R. Irvine
        * "Professional Assembly Language" by Richard Blum
        * (Often highly dependent on specific architecture being taught,
          e.g., ARM Cortex-M Assembly Guide)
12. **Operating System Internals**
    * [ ] Processes (Creation, Termination, States, PCB, Context Switching)
    * [ ] Process Scheduling Algorithms
    * [ ] Inter-Process Communication (IPC)
    * [ ] Memory Management (Paging, Segmentation, Virtual Memory, Swapping)
    * [ ] File Systems (Structure, Operations, I/O Management)
    * [ ] Protection and Security (OS level)
    * [ ] **Implementation of Key OS Components** (e.g., a simple scheduler,
          memory manager, bootloader)
    * **Recommended Textbooks:**
        * "Operating System Concepts" by Abraham Silberschatz, Peter B.
          Galvin, Greg Gagne (The "Dinosaur Book" - widely used)
        * "Modern Operating Systems" by Andrew S. Tanenbaum and Herbert Bos
13. **Compilers**
    * [ ] Phases of Compilation (Lexical Analysis, Parsing, Semantic
          Analysis, Intermediate Code Generation, Code Optimization, Code
          Generation)
    * [ ] Basic compiler design principles
    * **Recommended Textbooks:**
        * "Compilers: Principles, Techniques, and Tools" by Alfred V. Aho,
          Monica S. Lam, Ravi Sethi, Jeffrey D. Ullman (The "Dragon Book" -
          definitive)
        * "Engineering a Compiler" by Keith Cooper and Linda Torczon
14. **Linux and WSL**
    * [ ] Linux Basics: Command-line (file navigation, permissions, shell
          scripting), File system structure
    * [ ] Intermediate Linux: Process management (`ps`, `top`), Disk usage
          (`df`, `du`), Networking tools (`ping`, `curl`)
    * [ ] Advanced Linux: User/group management, System monitoring/logs,
          Package management
    * [ ] WSL-Specific Topics: Setting up and managing WSL distributions,
          WSLg for GUI apps, Integrating WSL with Windows
    * [ ] Automation and Scripting (advanced shell scripting, `cron`)
    * [ ] Linux for Development: Setting up dev environments (`make`, `gcc`,
          `gdb`)
    * **Recommended Textbooks/Resources:**
        * "The Linux Command Line: A Complete Introduction" by William E.
          Shotts Jr. (Excellent for beginners)
        * "Linux System Programming" by Robert Love (More advanced, focus on
          system calls)
        * (Many excellent online resources and distributions' official
          documentation are also vital)

---

## Phase 4: Building Connected Systems & Software Engineering Practices
*(This phase focuses on how software systems interact with each other and how
to build them effectively and reliably.)*

15. **Computer Networks**
    * [ ] OSI Model / TCP/IP Stack (detailed understanding of layers and
          protocols)
    * [ ] Network Protocols (HTTP, DNS, TCP, UDP, IP, Ethernet)
    * [ ] Routing concepts and algorithms
    * [ ] Network Security Fundamentals (firewalls, IDS, basic threats)
    * [ ] Socket programming (client-server communication)
    * **Recommended Textbooks:**
        * "Computer Networking: A Top-Down Approach" by James F. Kurose
          and Keith W. Ross (Popular, clear, accessible)
        * "Computer Networks" by Andrew S. Tanenbaum and David Wetherall
          (Comprehensive, classic)
16. **Parallel and Distributed Systems**
    * [ ] Concurrency vs. Parallelism
    * [ ] Multi-threading and Multi-processing
    * [ ] Distributed Systems Concepts (e.g., distributed consensus -
          Paxos/Raft basics, fault tolerance, distributed file systems)
    * [ ] Message Passing Interface (MPI) concepts
    * **Recommended Textbooks:**
        * "Distributed Systems" by Maarten van Steen and Andrew S. Tanenbaum
        * "Designing Data-Intensive Applications" by Martin Kleppmann (More
          practical, highly regarded)
17. **Database Systems**
    * [ ] Relational Database Theory & SQL (Normalization, ACID properties)
    * [ ] Database Design (Entity-Relationship modeling, Schema design)
    * [ ] Transaction Management (Concurrency Control, Recovery)
    * [ ] Indexing & Query Optimization
    * [ ] Introduction to NoSQL databases (Key-value, Document, Graph,
          Columnar)
    * **Recommended Textbooks:**
        * "Database System Concepts" by Abraham Silberschatz, Henry F.
          Korth, S. Sudarshan
        * "Database Management Systems" by Raghu Ramakrishnan and Johannes
          Gehrke
18. **Software Engineering Principles & Methodologies**
    * [ ] Software Development Lifecycles (Agile, Scrum, Kanban)
    * [ ] Requirements Engineering
    * [ ] Software Design Patterns (Creational, Structural, Behavioral)
    * [ ] Software Architecture principles
    * [ ] Testing Methodologies (Unit testing, Integration testing, System
          testing, Test-Driven Development - TDD)
    * [ ] Code Quality & Review practices
    * [ ] Project Management & Teamwork (tools and techniques for larger
          projects)
    * **Recommended Textbooks:**
        * "Software Engineering: A Practitioner's Approach" by Roger Pressman
        * "Code Complete" by Steve McConnell (Focus on practical construction)
        * "Design Patterns: Elements of Reusable Object-Oriented Software"
          by Erich Gamma et al. (Gang of Four - The classic for patterns)
19. **Computer Security (Dedicated & Advanced)**
    * [ ] Cryptography (beyond basics: symmetric/asymmetric, hashing,
          digital signatures)
    * [ ] Network Security (attacks, defenses, firewalls)
    * [ ] Operating System Security (access control, sandboxing)
    [ ] Web Security Vulnerabilities (XSS, SQL Injection, CSRF)
    * [ ] Software Security (buffer overflows, exploit development basics)
    * [ ] Security Policies and Management
    * **Recommended Textbooks:**
        * "Computer Security: Principles and Practice" by William Stallings
          and Lawrie Brown
        * "Security Engineering" by Ross Anderson (Broad and deep)
        * "The Web Application Hacker's Handbook" by Dafydd Stuttard and
          Marcus Pinto (Practical web security)
20. **Human-Computer Interaction (HCI) / User Interface Design**
    * [ ] User Research and Analysis
    * [ ] Usability Principles and Heuristics
    * [ ] UI/UX Design Principles
    * [ ] Prototyping and Wireframing
    * [ ] Usability Testing
    * **Recommended Textbooks:**
        * "About Face: The Essentials of Interaction Design" by Alan Cooper
          et al.
        * "Don't Make Me Think, Revisited" by Steve Krug (Focus on usability)
        * "Designing with the Mind in Mind" by Jeff Johnson

---

## Phase 5: Application Development & Specialized Fields
*(This phase applies all the foundational knowledge to build real-world
applications and explore advanced or specialized domains.)*

21. **Web Development**
    * [ ] Frontend: HTML, CSS, JavaScript (The Odin Project)
    * [ ] Backend: Python frameworks (Flask/Django)
    [ ] APIs: Building and consuming REST APIs
    * [ ] Deployment: Hosting web apps (Heroku, AWS)
    * **Recommended Textbooks/Resources:**
        * "Eloquent JavaScript" by Marijn Haverbeke (For JavaScript
          fundamentals)
        * "Fullstack Python" (Online resource covering many topics)
        * "Learning Web Design" by Jennifer Robbins (Broad introduction)
22. **App Development**
    * [ ] Mobile app development (e.g., Flutter or React Native)
    * [ ] Desktop app development (e.g., Python libraries like PyQt or Tkinter)
    * **Recommended Textbooks/Resources:**
        * (Highly platform/framework specific; online documentation and
          official guides are often primary)
        * For Flutter: "Flutter in Action" by Eric Windmill
        * For React Native: "Learning React Native" by Bonnie Eisenman
        * For Python Desktop (PyQt): "Create GUI Applications with Python
          & Qt6" by Martin Fitzpatrick
25. **Advanced Programming Topics**
    * [ ] Cryptography (if not fully covered in Security)
    * [ ] Parallel programming (if not fully covered in P&DS)
    *(Note: AI/ML Theory, Computer Vision, NLP are deferred but can be added
    here later)*
    * **Recommended Textbooks:**
        * "The Art of Computer Programming" by Donald Knuth (Vol 1-4 -
          Monumental and foundational for deep theory)
        * "Structure and Interpretation of Computer Programs" by Harold
          Abelson and Gerald Jay Sussman (SICP - Focus on computational
          thinking)
24. **Computer Graphics**
    * [ ] 2D and 3D Transformations
    * [ ] Geometric Modeling
    * [ ] Rendering Pipelines & Shaders (conceptual)
    * [ ] Introduction to Graphics APIs (OpenGL/Vulkan basics)
    * **Recommended Textbooks:**
        * "Fundamentals of Computer Graphics" by Peter Shirley et al.
        * "Interactive Computer Graphics: A Top-Down Approach with WebGL"
          by Edward Angel and Dave Shreiner
25. **Engineering Applications**
    * [ ] Math and Physics Applications: Symbolic math (`sympy`), Numerical
          methods (`numpy`, `scipy`), Simulations of physical systems
    * [ ] Structural Analysis: Solve linear equations for truss/beam,
          Visualize stress-strain/deflection (`matplotlib`)
    [ ] Geotechnical Applications: Analyze soil data (`pandas`), Visualize
          geotechnical data
    * [ ] Fluid Mechanics: Simulate fluid flow (numerical methods), Use tools
          like OpenFOAM (CFD)
    * [ ] Finite Element Analysis (FEA): Python libraries (FEniCS), Solve
          beam deflection/heat transfer
    * [ ] Geospatial Analysis: Work with geospatial data (`geopandas`,
          `shapely`), Visualize maps
    * **Recommended Textbooks/Resources:**
        * "Python for Data Analysis" by Wes McKinney (For pandas/numpy in
          practical use)
        * "Numerical Methods for Engineers" by Steven C. Chapra (Classic,
          applied numerical methods)
        * (Specific engineering domain textbooks will also be relevant here,
          e.g., for Structural Analysis, Fluid Mechanics, etc.)

---

## Overarching / Continuous Themes
*(These activities and topics should ideally be woven throughout the entire
learning journey.)*

* [ ] **Ethics and Society in Computing**
    * [ ] Data Privacy & Security, Algorithmic Bias, Accountability for
      AI/Autonomous Systems, Misinformation & Digital Divide, Intellectual
      Property in Software, Professional responsibility.
    * **Recommended Textbooks:**
        * "Ethics for the Information Age" by Michael J. Quinn
        * "Weapons of Math Destruction" by Cathy O'Neil (Focus on
          algorithmic bias)
* [ ] **Build Projects**
    * This is an ongoing activity. Aim to build small, medium, and large
      projects at each phase to apply and solidify learned concepts. For
      Engineering Applications, specific project ideas are listed.
    * **Recommended Resources:**
        * (Project-based learning is often best through online tutorials,
          open-source contributions, and personal challenges, rather than
          specific textbooks)
