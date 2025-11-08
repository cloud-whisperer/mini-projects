# ⚙️ AWS Event-Driven Mini Project 3.0  
🪄 *Build a Fully Decoupled Serverless Flow with Lambda, SNS, SQS & DynamoDB*

## 📌 Project Description  
This mini-project demonstrates how to **implement a decoupled, event-driven architecture** on AWS using **Lambda**, **SNS**, **SQS**, and **DynamoDB**. It simulates an **order processing pipeline** where one Lambda function acts as a **producer** that publishes high-value order events to an SNS topic, which then fans out messages to an **SQS queue** consumed by another Lambda function (the **consumer**).  
All events and actions are **securely logged in CloudWatch**, following the **principles of least privilege and modular design**.

---

## 🏗️ The architecture performs the following actions:

- 🧩 &nbsp;&nbsp;**Lambda Producer** publishes order data to **SNS Topic** (`HighValueOrderTopic`).  
- 📬 &nbsp;&nbsp;**SNS Topic** distributes messages to **SQS Queue** (`HighValueQueue`).  
- 📨 &nbsp;&nbsp;**Lambda Consumer** polls the **SQS Queue**, processes messages, and writes items to **DynamoDB** (`OrdersTable`).  
- 💾 &nbsp;&nbsp;**DynamoDB Table** stores all order details with partition key `OrderId` and sort key `Timestamp`.  
- 🪵 &nbsp;&nbsp;**CloudWatch Logs** capture message content, events, and function activity for observability.  
- 🔐 &nbsp;&nbsp;**IAM Roles & Policies** restrict Lambda permissions to only the required resources (SNS, SQS, DynamoDB, and CloudWatch).

---

## ✅ Key Learnings

| 🔍 Topic                    | 💡 Takeaway                                                                 |
|-----------------------------|-----------------------------------------------------------------------------|
| **Event-Driven Design**     | Decouples producer and consumer for asynchronous and scalable workflows.   |
| **SNS + SQS Integration**   | Reliable fan-out messaging pattern for event broadcasting.                 |
| **Lambda Triggers**         | SQS acts as a buffer to control processing rate and handle retries.        |
| **IAM Permissions**         | Separate execution roles enforce least privilege for each Lambda.          |
| **CloudWatch Monitoring**   | Centralized logging for debugging and message visibility.                  |

---

![Alt Text](900x500_GITHUB_TWITTER_projekt_lc_WATERMARKED_lc.jpg)

## ✅ Project Goals  
- ⚙️ &nbsp;&nbsp;Create a **producer Lambda** that publishes events to an **SNS topic**.  
- 🔔 &nbsp;&nbsp;Set up an **SNS topic** and subscribe an **SQS queue** for fan-out.  
- 📬 &nbsp;&nbsp;Create a **consumer Lambda** triggered by **SQS** to process messages.  
- 💾 &nbsp;&nbsp;Store processed order data in **DynamoDB**.  
- 🪵 &nbsp;&nbsp;Enable **CloudWatch logging** for end-to-end visibility.  
- 🔐 &nbsp;&nbsp;Enforce **IAM least privilege** via tailored execution roles.  

---

## 🔧 What I Accomplished  

🧩 **Built a Decoupled Architecture**  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Designed a Lambda → SNS → SQS → Lambda → DynamoDB flow, ensuring resilience and scalability.

📦 **Configured SNS and SQS Messaging**  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Established reliable asynchronous communication between services.

💾 **Created DynamoDB Table (OrdersTable)**  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Implemented `OrderId` as the partition key and `Timestamp` for time-based queries.

🔐 **Defined IAM Roles with Precision**  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Granted `sns:Publish`, `sqs:ReceiveMessage`, and `dynamodb:PutItem` permissions per function.

🪵 **Monitored with CloudWatch Logs**  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Verified message body delivery, Lambda execution, and event lifecycle in real time.

---

## 💡 Key Learnings & Outcomes
- 🧠 &nbsp;&nbsp;Understood **decoupled microservice communication** via SNS and SQS.  
- 🛡️ &nbsp;&nbsp;Applied **least privilege IAM principles** in Lambda execution roles.  
- 🧾 &nbsp;&nbsp;Learned to **trace events** across multiple AWS services using CloudWatch.  
- 🌩️ &nbsp;&nbsp;Reinforced understanding of **serverless event-driven architectures** in practice.  

---
