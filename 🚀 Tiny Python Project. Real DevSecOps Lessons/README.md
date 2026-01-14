# 🔐 Secure Task Logger

A simple lightweight Python CLI for secure, auditable task logging.

## 🗝️ Key Features

- **Modular Design:** Each component has a single, focused responsibility  
- **Traceable Workflow:** Captures and logs user-submitted tasks consistently  
- **User Context:** Explicitly records execution identity for auditability  
- **Audit-Style Logging:** Structured logs mimic real-world compliance patterns  
- **Learning Foundation:** Demonstrates security-conscious development practices without over-engineering


---

## ✍️ What This Project Is

- ✅ Understanding how modular Python components interact  
- ✅ Designing a simple, traceable audit-style workflow  
- ✅ Capturing user context deliberately and transparently  
- ✅ Practicing security-conscious design decisions early  
- ✅ Building a complete, functional workflow — then stopping  

**Philosophy:** Learn the shape of secure systems before scaling them.

---

## 🧭 The “Shallow Slice” Security Learning Model

Instead of deep-diving into a single component, this project follows a **horizontal slice approach**.  

Each slice addresses three security-relevant questions:
1️⃣ What initiates the action?  
2️⃣ What context is captured and recorded?  
3️⃣ Where does that record go, and why?  

Once these questions are answered, development **stops** — preventing over-engineering and burnout.  

**Guiding Principle:** Sampling > Perfection 🧪

---

## 🛠️ Project Intent (Why This Exists)

This project demonstrates how **security thinking manifests in small, everyday codebases**, not just enterprise tooling.  

It mirrors patterns used in:

- Audit logging  
- Forensic traceability  
- DevSecOps pipelines  
- Compliance-aware development  

…but at a scale appropriate for **learning and iteration**.

---

## 📦 Project Description

**Secure Task Logger** records user-submitted tasks alongside execution context, producing **structured logs** that resemble audit events.  

Key design principles:
- Explicit entry points  
- Clear data flow  
- Intentional, consistent logging  
- Separation of responsibilities  

Each module is **single-purpose** and easily auditable.

---

## 🧱 Core Components

| Component | Purpose |
|-----------|---------|
| 🧠 `main.py` | Entry point coordinating the application lifecycle |
| ✍️ `task_input.py` | Collects structured user input |
| 📁 `logger.py` | Writes task events to a persistent log |
| 👤 `user_context.py` | Captures execution identity (who ran this?) |
| 🔐 `.venv` | Isolated Python runtime environment |

---

## 🔄 Execution Flow

```text
👤 User launches application
        ↓
🧠 main.py initializes session
        ↓
👤 user_context captures identity
        ↓
✍️ task_input collects task data
        ↓
📁 logger writes structured event
        ↓
📊 summary output displayed

