# 📦 CloudTrail Monitoring & Security Infrastructure (Terraform)

🔁 *Provision a secure AWS environment with logging, monitoring, and alerting using Terraform IaC.*

---

## 📌 Project Description

This mini-project demonstrates building a **secure AWS logging and monitoring environment** with **CloudTrail**, **S3**, **SNS**, **SQS**, and an **Application Load Balancer**. The infrastructure is deployed and managed using **Terraform**, emphasizing **security-first architecture**, **event-driven notifications**, and **scalable infrastructure components**.

---

## 🚀 Key Steps Simulated in This Project

* 🕸️   **Create a VPC and public subnets** for hosting cloud resources.
* 📜   **Deploy CloudTrail** to capture AWS API activity and deliver logs to S3.
* 📦   **Provision an S3 bucket** for secure CloudTrail log storage.
* 🔔   **Set up an SNS topic** to send notifications for security events.
* 📥   **Integrate SQS queue** with SNS for asynchronous processing of alerts.
* 🛂   **Create IAM users and policies** for log monitoring and publishing access.
* ⚖️   **Deploy an Application Load Balancer** and attach an existing EC2 instance for web traffic routing.

---

## ✅ Project Goals

* 🛡️   Ensure centralized logging for security visibility.
* 🔔   Automate notifications for detected AWS events.
* 📂   Use IAM least-privilege policies for log monitoring and alert publishing.
* 🌐   Demonstrate high availability with ALB + multi-AZ subnets.
* 🧭   Build everything declaratively using Terraform for repeatability and control.

---

## 🔧 What I Accomplished

* 🧑‍💻   Created a VPC with two public subnets across availability zones.
* 📜   Configured **CloudTrail** with validation enabled to ensure tamper-proof logs.
* 📦   Deployed an **S3 bucket** for CloudTrail with secure access controls.
* 🔔   Provisioned an **SNS topic** and integrated with email for security alerts.
* 📥   Created an **SQS queue** and subscribed it to the SNS topic for alert processing.
* 🛂   Defined IAM policies for:

  * **log-monitor-user** → read-only S3 access for CloudTrail logs.
  * **log-monitor-publisher** → SNS publish/subscribe permissions.
* ⚖️   Provisioned an **Application Load Balancer**, health-checked target group, and attached an existing EC2 instance.

---

## 💡 Key Learnings & Outcomes

* ☁️   Strengthened knowledge of **Terraform workflows** (init, plan, apply, outputs).
* 🔐   Gained hands-on experience with **IAM policies and attachments** for least privilege.
* 🔄   Learned how **SNS + SQS integration** supports scalable, event-driven alerts.
* 📜   Understood how **CloudTrail and S3** enable secure, centralized audit logging.
* ⚙️   Improved ability to design security-focused AWS architectures with IaC.


