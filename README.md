# 👋 Hi, I'm Talha Zubair Asim

🚀 **Full Stack .NET Developer | React | Azure | Microservices | DevOps Enthusiast**  
💻 Passionate about building scalable, enterprise-grade web applications and cloud-native solutions.

---

## 🧠 About Me

I'm a **Software Developer with 3+ years of professional experience**, specializing in building robust backend systems using **C#, .NET (Core, 6, 8), and SQL** — and creating modern, responsive UIs with **React.js**.

I’ve worked in **corporate** and **startup** environments, contributing to large-scale enterprise solutions, cloud deployments, and CI/CD pipelines. My focus lies in writing clean, maintainable, and testable code that delivers real business value.

🌍 Currently based in **Pakistan**  
✈️ Open to relocation opportunities (Europe, UAE, Australia, or Remote)  
🧩 Interested in **Microservices**, **CQRS**, **Event Sourcing**, and **Distributed Systems**

---

## 🛠️ Tech Stack

### 💻 Backend
- **Languages:** C#, Python, Node.js (basic)
- **Frameworks:** ASP.NET Core (MVC, Web API, Razor), Entity Framework Core, LINQ
- **Architectures:** RESTful APIs, Microservices, Monolith-to-Microservices migrations
- **Authentication:** JWT, OAuth 2.0, Identity Server
- **Caching & Messaging:** Redis, Apache Kafka
- **ORM / Database:** Entity Framework, Dapper

### ⚛️ Frontend
- **Libraries/Frameworks:** React.js, Blazor, jQuery
- **State Management:** Redux, Context API
- **Form Handling:** Formik, Yup
- **Styling:** TailwindCSS, Bootstrap, CSS3, HTML5

### ☁️ Cloud & DevOps
- **Cloud:** Azure (App Services, Functions, Storage, Pipelines)
- **CI/CD:** Azure DevOps, Jenkins, GitHub Actions
- **Containers:** Docker, Kubernetes
- **Version Control:** Git, GitHub, Azure Repos

### 🗄️ Databases
- **SQL:** MySQL, SQL Server, PostgreSQL, Oracle
- **NoSQL:** MongoDB (learning)
- **Tools:** SSMS, DBeaver, pgAdmin

### 🧩 Other Tools
- Visual Studio, VS Code  
- Postman, Swagger, Fiddler  
- Jira, Trello, Azure Boards  

---

## 🚀 Featured Projects

### 🛒 [ShopFlow – .NET 8 Microservices E-commerce](https://github.com/talhazubairasim/shopflow)
An **e-commerce platform** split into six .NET 8 services behind a YARP API gateway, with a React + TypeScript storefront.
- Checkout is a **MassTransit saga over RabbitMQ**: reserve stock → charge card → confirm, with compensation (stock released, order cancelled) when a step fails.
- CQRS with MediatR + FluentValidation, optimistic-concurrency stock reservations, Redis baskets, JWT auth with roles, OpenTelemetry and health checks.
- CI runs unit, API and saga tests, then boots the whole stack with Docker Compose and drives real checkouts end to end; Kubernetes manifests included.
- **Tech:** .NET 8, ASP.NET Core, MassTransit, RabbitMQ, EF Core, PostgreSQL, Redis, YARP, React, Tailwind CSS, Docker, Kubernetes.

---

### 🏥 [ClinicDesk – Multi-tenant Clinic SaaS](https://github.com/talhazubairasim/clinicdesk)
A **multi-tenant SaaS** where clinics sign up, set practitioners' hours, book patients, run visits and bill them, on Free / Pro / Enterprise plans.
- Tenant isolation with EF Core global query filters plus write guards, proven by tests where one clinic tries to read and change another's data.
- **No double booking, even under concurrent load**: a Postgres exclusion constraint on time ranges; a test fires 8 simultaneous bookings at one slot and exactly one succeeds.
- Time-zone-aware slots, role-based policies, invoicing with tax and partial payments, pro-rata plan upgrades, reminder and billing jobs, audit trail.
- Integration tests on real Postgres via Testcontainers; CI runs an end-to-end script against the Docker Compose stack.
- **Tech:** .NET 8, ASP.NET Core minimal APIs, EF Core, PostgreSQL, FluentValidation, React, TypeScript, Tailwind CSS, Docker, Kubernetes.

---

### 🧱 [TaskBoard – Go + React](https://github.com/talhazubairasim/taskboard-go-react)
A **Kanban-style task management system** with a Go backend and a React + TypeScript frontend.
- GraphQL API (queries, mutations, real-time subscriptions over WebSocket) **and** a REST API, both on one service layer.
- Clean architecture: handlers/resolvers → services → repositories, JWT auth with refresh tokens, Redis caching.
- 97% backend / 99% frontend test coverage enforced in CI; Docker Compose and Kubernetes manifests.
- **Tech:** Go, gqlgen, PostgreSQL, Redis, React, Apollo Client, Tailwind CSS, Docker, Kubernetes.

---

### 🧭 [Hotel Management System – ASP.NET Core](https://github.com/talhazubairasim/Hotel-Management)
A **workflow management system** for hotel room bookings: receptionists raise booking requests, admins approve them, and the front desk checks guests in and out.
- Custom middleware for OWASP security headers with a nonce-based Content-Security-Policy.
- Role-based access (Admin / Receptionist dashboards), guest profiles, automatic invoicing at check-out.
- Dynamic form validation (server rules mirrored in the browser) and workflow automation (stale requests expire, no-shows flagged).
- **Tech:** ASP.NET Core MVC (.NET 8), ASP.NET Core Identity, Entity Framework Core, SQL Server, jQuery, Bootstrap, xUnit.

---

### 🤖 [Self-Driving Car – Deep Q-Learning](https://github.com/talhazubairasim/self-driving-car)
A car that **learns to drive with reinforcement learning**, avoiding obstacles you draw on the map.
- Deep Q-network with experience replay in PyTorch; three sand sensors plus orientation to the goal as inputs.
- Interactive Kivy simulator, plus a headless environment and CLI for training and evaluation.
- Trained agent reaches the goal 25× per 5,000 steps vs. 0× untrained; tested with pytest in CI.
- **Tech:** Python, PyTorch, NumPy, Kivy, Matplotlib.

📘 *Started from the AI A–Z course and extended with a headless simulator, evaluation and tests.*

---

## 📈 GitHub Stats

<p align="center">
  <img height="165" src="https://github-readme-stats.vercel.app/api?username=talhazubairasim&show_icons=true&theme=tokyonight" />
  <img height="165" src="https://github-readme-streak-stats.herokuapp.com/?user=talhazubairasim&theme=tokyonight" />
</p>

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=talhazubairasim&layout=compact&theme=tokyonight" />
</p>

---

## 🏆 Certifications

🎓 **Application Development using Microservices and Serverless**  
🎓 **Developing Back-End Apps with Node.js and Express**  
🎓 **Python Project for AI & Application Development**

*(More certifications and credentials available on my [LinkedIn](https://linkedin.com/in/talha-zubair-asim-8aa731171))*

---

## 🧩 What I’m Currently Working On

- 🔭 Building **enterprise microservices** with .NET 8 and React  
- ⚙️ Enhancing DevOps skills with **Azure Pipelines** and **Kubernetes**  
- 📚 Learning **Event Sourcing**, **CQRS**, and **MediatR** in-depth  
- 💡 Planning a **startup-scale SaaS platform** (stay tuned 😉)

---

## 🌐 Connect With Me

<p align="left">
  <a href="https://linkedin.com/in/talha-zubair-asim-8aa731171"><img src="https://img.shields.io/badge/LinkedIn-Talha%20Zubair%20Asim-blue?style=for-the-badge&logo=linkedin" /></a>
  <a href="mailto:talhazubairasim987@gmail.com"><img src="https://img.shields.io/badge/Gmail-talhazubairasim987%40gmail.com-red?style=for-the-badge&logo=gmail" /></a>
  <a href="https://github.com/talhazubairasim"><img src="https://img.shields.io/badge/GitHub-talhazubairasim-black?style=for-the-badge&logo=github" /></a>
</p>

---

## 💬 Fun Facts

- 🧩 I love solving real-world problems through code.  
- 🎮 When I’m not coding, you’ll find me exploring new tech trends, AI tools, or gaming.  
- ✈️ Dreaming to build a product that scales globally — from Pakistan to the world.  

---

### ⚡ “The code you write defines the future you build.”  

⭐️ **If you like my work, consider giving a star to my repositories and following me!**
