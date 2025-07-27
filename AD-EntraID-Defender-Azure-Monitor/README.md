# 🛡️ Cloud-Native Library Access Control System (LACS)

🌐 *Secure, High-Availability, Multi-Cloud Architecture for Sensitive Data Governance*

---

## 📌 Project Description

This advanced infrastructure project simulates a **Library Access Control System (LACS)** leveraging **AWS-native services, multi-cloud principles**, and **DevSecOps tooling** to enforce secure, highly available, and automated access to digital resources. It reflects enterprise-grade architecture patterns, regulatory considerations, and integration of real-world data ingestion scenarios for research or sensitive institutional environments.

---

## 🚀 Key Steps Simulated in This Project

- 🏗️ **Provision AWS infrastructure** using Python and AWS CLI (no roles attached initially).  
- 🔐 **Create IAM users, roles, and permissions** via CloudFormation for secure identity access.  
- 📦 **Ingest structured/unstructured data** from sources like SQL, NoSQL, logs, and IoT streams.  
- 🔎 **Monitor and respond to traffic events** with EventBridge, Lambda, and CloudWatch.  
- 🧠 **Configure threat detection** and auditing via CloudTrail and GuardDuty.  
- 🔁 **Enable high-availability & self-healing** using Auto Scaling, SNS, and SQS.  
- 🛜 **Route securely via load balancer**, with encryption and logging.  
- 📚 **Store and govern** files in Amazon S3 with custom bucket policies and VPC endpoints.  
- 🏥 **Simulate compliance workflows** for healthcare or research-sensitive environments.  

   ![Alt Text](900x500_Step_7_Network_diagram_lc_WATERMARK_lc.jpg)

---

## 🧱 Core Infrastructure (Simulated)

| Component                      | Description                                                                 |
|-------------------------------|-----------------------------------------------------------------------------|
| 🖥️ EC2 (no IAM role)           | Simulates minimal-trust, legacy-like server initiating secure CLI actions. |
| 🔐 IAM Policies & Roles        | Built for granular, least-privilege enforcement and automation.            |
| 📜 CloudFormation              | Used to automate consistent policy and resource creation.                  |
| 🪣 Amazon S3                   | Acts as secure data lake and long-term archival store.                     |
| 🕸️ VPC Endpoints (Gateway)     | Ensures private access to S3 for compliant network behavior.               |
| 🌍 Application Load Balancer   | Fronts access with WAF and TLS termination.                                |
| 📡 EventBridge + Lambda        | Detect and respond to suspicious or critical traffic behavior.             |
| 📬 SNS + SQS                   | Automate notifications and remediation pipelines.                          |
| 🔍 CloudTrail + GuardDuty      | Provides auditing, anomaly detection, and logging insights.                |

---

## 🧪 Testing & Validation

- 🔐 Run secure AWS CLI actions from EC2 instance with credentials pulled via Secrets Manager.
- 🛡️ Confirm access policies block public access and allow only tagged resources.
- 📂 Validate objects uploaded from EC2 to S3 appear in the correct folder and have encryption.
- 🧠 Trigger event simulation (e.g., failed login, unusual access) and validate Lambda/SNS action.

---

## 🧹 Clean-Up Checklist

- 🧼 Remove created IAM roles, policies, and test users.
- 🗑️ Empty and delete S3 buckets with test data.
- 💻 Decommission EC2 instance and deregister from load balancer.
- 🔕 Remove CloudWatch alarms, SNS topics, and associated Lambda functions.

---

## 🎯 Learning Outcomes

- 🔒 Deepen understanding of **identity-first security** across hybrid environments.
- 📡 Master **event-driven automation** using Lambda, SNS, and EventBridge.
- 📁 Apply **secure file handling and access governance** using bucket policies and endpoints.
- ⚙️ Practice using **DevSecOps pipelines** with Infrastructure-as-Code and observability.
- 🌐 Explore real-world **multi-cloud readiness** and **compliance-driven design**.




