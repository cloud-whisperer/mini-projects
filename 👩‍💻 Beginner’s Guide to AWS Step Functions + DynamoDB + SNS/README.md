# 🧭 AWS Event-Driven Mini Project: Orders Processing

🔁 *Process incoming orders with Lambda, store in DynamoDB, and notify high-value orders via SNS*

---

## 📌 Project Description

This Proof of Concept (PoC) demonstrates a **basic serverless, event-driven workflow** in AWS:

- 💾 **Amazon DynamoDB** stores order records.  
- 🧠 **AWS Lambda** processes order events automatically.  
- 🔔 **Amazon SNS** notifies stakeholders for high-value orders.  
- 📊 **CloudWatch Logs** captures Lambda execution and event details.

Designed to highlight practical skills in **serverless compute**, **database operations**, **messaging**, and **monitoring**, ideal for **DVA-C02 exam domains**: Compute, Database, Messaging, Permissions, and Monitoring & Logging.

---

## 🚀 Key Steps Simulated in This Project

- 💾 **Create a DynamoDB table** named `OrdersTable`.  
- 🧠 **Create a Lambda function** to process orders.  
- 🔐 **Attach an IAM role** granting Lambda `dynamodb:PutItem` and `sns:Publish` permissions.  
- 🔔 **Publish to SNS** automatically for orders with `Amount > 100`.  
- 📤 **Send test events** to Lambda to simulate incoming orders.  
- 📊 **Inspect logs in CloudWatch** to validate order processing.  
- 🧹 **Clean up resources** to avoid charges.

![Workflow Diagram](900x500_AWS_Lambda_DynamoDB_SNS_CloudWatch.jpg)

---

## 🧱 Core Infrastructure

| Component                | Description                                                              |
|--------------------------|--------------------------------------------------------------------------|
| 💾 DynamoDB Table         | Stores order records (`OrderId`, `Amount`)                                |
| 🧠 AWS Lambda Function    | Processes order events and triggers SNS notifications                     |
| 🔔 Amazon SNS Topic       | Notifies on high-value orders (Amount > 100)                              |
| 🔐 IAM Role               | Provides least-privilege permissions for Lambda (DynamoDB + SNS access)  |
| 📊 CloudWatch Logs        | Monitors Lambda execution and captures event details                      |
| 🌐 AWS Management Console | Web interface to create, configure, and test all resources               |

---

## 🧪 Testing & Validation

### ✅ Summary Table 

| 🔢 Step | Goal                                | Tool                  |
|--------|-------------------------------------|----------------------|
| 1️⃣     | Create DynamoDB table               | AWS Console / DynamoDB |
| 2️⃣     | Create Lambda function              | AWS Console / Lambda |
| 3️⃣     | Attach IAM role with permissions    | IAM Console          |
| 4️⃣     | Configure Lambda environment vars   | Lambda → Configuration |
| 5️⃣     | Send test event to Lambda           | Lambda → Test Event  |
| 6️⃣     | Verify DynamoDB record creation     | DynamoDB Console     |
| 7️⃣     | Verify SNS notification (if Amount > 100) | Email / SNS Console |
| 8️⃣     | Inspect Lambda execution logs       | CloudWatch Logs      |

### 🧠 Event Behavior Confirmations

| 🔍 What to Confirm                       | 📌 Status | 🧾 Evidence Provided                      |
|----------------------------------------|-----------|-----------------------------------------|
| Lambda triggered by test event          | ✅        | CloudWatch Logs shows event details      |
| IAM permissions allow DynamoDB write    | ✅        | No `AccessDenied` errors                 |
| IAM permissions allow SNS publish       | ✅        | SNS email received for high-value order  |
| Order JSON saved in DynamoDB            | ✅        | DynamoDB console shows `OrderId` & `Amount` |
| CloudWatch logs show structured output  | ✅        | Logs include JSON request + Lambda response |

---

## 🛡️ Permissions & Security (IAM Role)

### 🔐 What Was Implemented

- ✅ **Role Name**: `ProcessOrderFunction-role`  
- 👤 **Assigned to Lambda**  
- 🧾 **Policy**:
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "dynamodb:PutItem",
        "sns:Publish"
      ],
      "Resource": [
        "arn:aws:dynamodb:us-east-1:<account-id>:table/OrdersTable",
        "arn:aws:sns:us-east-1:<account-id>:HighValueOrderTopic"
      ]
    }
  ]
}
```
---

## 🎯 Learning Outcomes

By completing this mini-project, you will be able to:

- 🔁 **Build a serverless event-driven workflow** with Lambda → DynamoDB → SNS
- 💾 **Apply DynamoDB CRUD operations** for real-time event processing
- 🔔 **Implement SNS notifications** for high-value orders
- 🧠 **Configure IAM roles with least privilege** for Lambda functions
- 📊 **Monitor execution and event processing** using CloudWatch Logs
- 🚀 **Reinforce core DVA-C02 domains**: Compute, Database, Messaging, Permissions, Monitoring
- 🧹 **Practice clean-up best practices** to minimize cost

---

