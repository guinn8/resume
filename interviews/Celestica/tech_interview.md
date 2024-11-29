# Technical Interview Preparation with Edward Stodola

## 1. Understanding Celestica and Edward Stodola’s Role

### 1.1 Celestica Overview

- **Industry Role**: Provides design, manufacturing, and supply chain solutions.
- **Services**: Specializes in commercialization services, including test development and production solutions.

### 1.2 Edward Stodola’s Background

- **Current Role**: Commercialization Services Director at Celestica.
- **Experience**: Over 25 years at Celestica in various engineering and management positions.
- **Key Responsibilities**:
  - Leading global commercialization strategies.
  - Overseeing engineering teams for test solutions and after-market services.
  - Managing capabilities and capacities across manufacturing operations.

---

## 2. VxWorks Overview

### 2.1 Key Features

- **Deterministic and Certified**: Ensures reliability for critical applications.
- **Time Partition Scheduler**:
  - Ensures critical processes never lack resources.
  - Isolates non-critical failures (e.g., UI crashes) from affecting essential systems (e.g., pumps, sensors in medical devices).
- **GUI Support**:
  - Offers extensive driver support for various touchscreen hardware.

### 2.2 Development Environment

- **Possible Tools**: May involve using a VxWorks plugin in Visual Studio.
- **Debugging Capabilities**:
  - Identifies stack overflows and delayed interrupt servicing.

---

## 3. Qt (Cute) Framework

### 3.1 Key Features

- **WYSIWYG Editor**:
  - HTML-like markup with a direct C++ API.
  - Reduces complexity compared to XML-heavy UI code.
- **Built-in Features**: Offers enhanced aesthetics and functionality compared to LVGL.

### 3.2 Comparison with LVGL

- **Advantages**:
  - Superior built-in components.
  - Better visual appearance and user experience.
- **Considerations**:
  - Evaluate learning curve and compatibility with existing systems.

---

## 4. ClearCase

- **Functionality**:
  - Centralized version control system with file and version history management.
- **Features**:
  - Specific file checkouts with global edit locks to prevent conflicts.

---

## 5. IMDS (International Material Data System)

- **Definition**: A system for tracking material composition, particularly in the automotive industry.
- **Purpose**: Ensures compliance with regulations and standards.

---

## 6. Questions and Notes

### Questions

1. **Is the client located in the Greater Toronto Area (GTA)?**
1. **Is the client in question use a startup structure?**
2. **What workflows justify the inclusion of a GUI on the test equipment?**
   - Debugging, parameter configuration, or real-time data visualization?
3. **What level of firmware customization is expected for adapting test systems to client requirements?**
   - Frequent feature additions or modular parameter updates?
4. **Does Celestica's additional design work indicate limited design bandwidth from the original company?**
    - or is about focusing on R&D rather than the customer service
5. **Is the testing for the final product, PCBA, or raw PCB electrical checks?**
6. **What limitations exist in reusing test fixtures across different customizations?**
   - Common bottlenecks like varying pin configurations or mechanical constraints?
7. **How does Celestica address manufacturability challenges for prototypes when working with startups?**
   - Is there a structured process to balance innovation and scalability?
8. **Will the role involve working on resource-constrained devices or more robust SoCs?**

---

## Notes and Advice

### Key Facts

- **Client Engagement**:
  - On-site client work expected in Q1.
  - Ed was unsure of specific client needs.
- **Celestica's Role**:
  - Acting as an Original Equipment Manufacturer (OEM).
- **Core Project**:
  - Maintaining firmware for test equipment with a GUI.
- **Challenges with Startups**:
  - Balancing innovation and scalability while maintaining safety and manufacturability.
- **Test Development Experience**:
  - Developed PCB test checklists to identify components with high defect rates.
  - Collaborated on a bed-of-nails test fixture design.
  - Mitigated issues from delayed test jig development.
- **Highlighting DFM Failures**:
  - Lack of planning led to extended hours during prototype shipments and manual testing.

### Advice

- **Answering RTOS Questions**:
  - Use specific examples:
    - Delays in RFID services due to interrupt issues.
    - Crashes from exceeding stack limits.
    - Debugging memory leaks in UI code with LVGL.
- **Relating Experiences**:
  - Connect test development experiences to Celestica’s challenges.
  - Emphasize collaboration with hardware and software teams.
- **Expressing Interest**:
  - Demonstrate enthusiasm for contributing to commercialization services.
  - Share specific test fixture development and manufacturing solutions experience.