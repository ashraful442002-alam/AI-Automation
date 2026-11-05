
# AI Automation

## 1. What is Automation?

**Ans:**

Automation = Performing tasks automatically according to predefined rules, without requiring repeated human intervention.

Suppose you have an online business.

Every day, 20 customers send emails.

Every time, we have to:

1. Open the email.
2. Check the customer's name.
3. Read the message.
4. Enter the data into Google Sheets.
5. Reply to the customer.

We have to repeat these tasks over and over again.

Now, build a system where, whenever an email arrives, the customer's information is automatically saved to Google Sheets without any manual effort.

That is called Automation.

---

## 2. What is AI Automation?

**Ans:**

AI Automation = Using Artificial Intelligence (AI) and automation technologies to perform tasks automatically with minimal human intervention, including tasks that require understanding, learning, decision-making or problem-solving.

**Example:**

A customer sends the following message:

> My order has not arrived yet. Please help me.

**Traditional Automation:**

- Simply saves the message to Google Sheets.

**AI Automation:**

- Understands that this is a Delivery Complaint.
- Analyzes the sentiment of the message.
- Generates an appropriate reply draft.
- Forwards the complaint to a Human Support Agent if necessary.

---

## 3. What is WorkFlow?

**Ans:**

Workflow = A step-by-step process that describes how a task moves from beginning to completion.

### Real-Life Example

Imagine you run an online business.

When a customer places an order, the following steps happen:

1. Customer places an order.
2. System receives the order details.
3. Order information is saved to Google Sheets.
4. Customer receives a confirmation email.
5. Admin receives a notification.
6. Order is sent for processing.

All these connected steps together form a Workflow.

### Visual Representation of a Workflow

```text
             Step 1: Trigger
          Customer places an order
                     ||
                     \/
             Step 2: Receives data
       Get customer and order information
                     ||
                     \/
             Step 3: Process data
          Validate order information
                     ||
                     \/
              Step 4: Store data
          Save order to Google Sheets
                     ||
                     \/
              Step 5: Take Action
         Send order confirmation email
```

### Most Important Words

- **Trigger:** an event that starts a Workflow --> when to starts?

- **Node:** A specific tast or step in a Workflow --> which step to perform?

- **Action:** A task performed after a Workflow is triggered -->what task to execute?

- **Edit fields Node:** create and change data

---

# n8n AI Automation Learning Journey

A hands-on learning journey to understand workflow automation using n8n. This repository documents my environment setup, practical experiments, workflow development, and learning progress.

---

## Part 1 — Environment Setup

### Why n8n?

n8n is a workflow automation platform that connects different applications, APIs, and services to automate repetitive tasks and build powerful workflows.

**Official Resources:**

- Website: [https://n8n.io/](https://n8n.io/)
- Documentation: [https://docs.n8n.io/](https://docs.n8n.io/)
- Learning Path: [https://docs.n8n.io/learning-path/](https://docs.n8n.io/learning-path/)

### Setup Decision

My computer configuration:

| Configuration | Details |
|---|---|
| Operating System | Windows |
| RAM | 4 GB |
| Automation Platform | n8n Cloud |

**Why I Chose n8n Cloud**

I chose n8n Cloud to begin learning because running local services can consume significant computer resources. With limited RAM (4 GB), using the cloud platform is a more convenient option for getting started.

> **Note:** n8n Cloud offers a limited trial, not a permanently free cloud account. The self-hosted Community Edition is another option.

### First Setup Steps

1. Visit [https://n8n.io/](https://n8n.io/)
2. Create an account.
3. Verify your email address.
4. Open your n8n workspace.
5. Create a new workflow.

---

## Part 2 — Build the First Workflow

### Project Name

`My First Automation Workflow`

### Objective

Create a simple workflow that generates structured information using n8n nodes.

### Required Nodes

1. Manual Trigger
2. Edit Fields (Set)

### Workflow Structure

```text
Manual Trigger
      |
      v
  Edit Fields
```

### Step 1 — Add Manual Trigger

- Create a new workflow.
- Add a **Manual Trigger** node.
- This node starts the workflow when manually executed.

### Step 2 — Add Edit Fields Node

- Add an **Edit Fields (Set)** node.
- Select **Manual Mapping**.
- Add the following fields:

| Field Name | Type | Value |
|---|---|---|
| name | String | Mu Ashraful Alam |
| course | String | AI Automation |
| Day | Number | 1 |
| Status | String | Learning |

### Step 3 — Connect Nodes

Connect the two nodes:

`Manual Trigger → Edit Fields`

### Step 4 — Execute Workflow

1. Click **Execute Workflow**.
2. Open the Edit Fields node.
3. Inspect the Output panel.

### Expected Output

```json
{
  "name": "Mu Ashraful Alam",
  "course": "AI Automation",
  "Day": 1,
  "Status": "Learning"
}
```

---

## Part 3 — Experiment: Add and Modify Fields

### Objective

Practice modifying existing fields and creating new fields using the Edit Fields node.

### Task 1 — Modify Existing Field

Find the existing field:

```text
level = Beginner
```

Change its value to:

```text
level = Intermediate
```

### Task 2 — Add a New Field

Add the following field:

| Field Name | Type | Value |
|---|---|---|
| goal | String | First Freelance Client |

### Task 3 — Add More Fields

Configure the following fields in the Edit Fields node:

| Field Name | Type | Value |
|---|---|---|
| skill | String | Automation |
| country | String | Bangladesh |
| level | String | Intermediate |
| completed | Boolean | true |
| goal | String | First Freelance Client |

### Task 4 — Execute Again

1. Click **Execute Workflow**.
2. Open the Edit Fields node.
3. Inspect the updated Output panel.
4. Verify that all updated and newly added fields are present.

### Actual Output

```json
[
  {
    "name": "Mu Ashraful Alam",
    "course": "AI Automation",
    "Day": 1,
    "Status": "Learning",
    "skill": "Automation",
    "country": "Bangladesh",
    "level": "Intermediate",
    "completed": true,
    "goal": "First Freelance Client"
  }
]
```

---

## Part 4 — Learning Outcomes

Through these practical experiments, I learned:

- How to set up an n8n Cloud account.
- How to create a new workflow.
- How to use the Manual Trigger node.
- How to configure the Edit Fields (Set) node.
- How to create structured data.
- How to modify existing fields.
- How to add new fields.
- How to work with different data types:
  - String
  - Number
  - Boolean
- How to execute workflows and inspect output data.
- How n8n processes workflow data between nodes.

### Final Result

**Successfully completed my first n8n automation workflow and experimented with creating, modifying, and managing structured data.**

---

## Part 5 — My Learning Progress

| Learning Activity | Status |
|---|---|
| n8n Environment Setup | Completed |
| Account Creation | Completed |
| First Workflow Creation | Completed |
| Manual Trigger Node | Completed |
| Edit Fields Node | Completed |
| Field Modification | Completed |
| Adding New Fields | Completed |
| Output Inspection | Completed |

---

## Author

**Mu Ashraful Alam**

- GitHub: [https://github.com/ashraful442002-alam](https://github.com/your-username)
- Location: Bangladesh
- Learning Focus: AI Automation, n8n, APIs, and Workflow Development

---

## Learning Resources

- [n8n Official Website](https://n8n.io/)
- [n8n Documentation](https://docs.n8n.io/)
- [n8n Learning Path](https://docs.n8n.io/learning-path/)

---

**Learning by Building | Practicing | Experimenting | Improving**
