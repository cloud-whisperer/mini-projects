# 📢 Azure AD: Role-Based Access Control (RBAC) Test  
🛡️ *Manage Access Securely Using Azure Active Directory Groups and Roles*

## 📌 Project Description  
This mini-project demonstrates how to **securely assign role-based access** using **Azure Active Directory (Azure AD)** by creating a **test user**, placing them into a **group**, and then assigning a **built-in role** (`Reader`) to that group. It includes a verification step to ensure the user can **only view but not modify** resources — following the principle of **least privilege**.

---

## 🏗️ The architecture performs the following actions:

- 👤   &nbsp;&nbsp;**Creates a test user** (`demo`) in Azure AD  
- 👥   &nbsp;&nbsp;**Creates a group** (`MyTestGroup`) for centralized access control  
- ➕   &nbsp;&nbsp;**Adds the test user to the group** to inherit permissions  
- 🔐   &nbsp;&nbsp;**Assigns the built-in `Reader` role** to the group  
- 🧪   &nbsp;&nbsp;**Tests user access** in a new browser window or incognito session  
- 🚫   &nbsp;&nbsp;**Validates restricted access** — user can **view resources** but **not create/delete/modify**  
- 🧹   &nbsp;&nbsp;**Cleans up** by deleting the test user and group (optional)

---

## ✅ Key Learnings

| 🔍 Topic               | 💡 Takeaway                                                                 |
|-------------------------|-----------------------------------------------------------------------------|
| **Azure RBAC**          | Roles can be assigned to groups, not just individuals, for scalable access. |
| **Reader Role**         | Grants **read-only access** across Azure resources.                         |
| **Group Management**    | Centralized group control simplifies permission changes.                    |
| **Testing Permissions** | Always verify access by logging in as the test user.                        |

---

  ![Alt Text](900x500_GITHUB_TWITTER_projekt_lc_WATERMARKED_lc.jpg)
