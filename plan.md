# FreelanceOS — Build Plan

## Overview
FreelanceOS is a full-stack SaaS platform for freelancers. This plan breaks the project into 7 phases across July and August 2026 and is designed for project-based learning. Each phase should produce something visible and working before moving to the next one.

**Stack:** React · TypeScript · Tailwind CSS · FastAPI · SQLAlchemy · PostgreSQL · Redis · Docker · AWS · LangChain · OpenAI API

AI is a first-class feature of this product. The AI capabilities are not optional add-ons; they are core deliverables that demonstrate both AI engineering and full-stack engineering skills.

---

## Core Workflow

```text
New Lead → Proposal → Client Onboarded → Project Created → Milestone Tracking → Invoice Generated → Payment Collected → Follow-Up
```

---

## Phase 0 — Development Environment and Project Skeleton

**Goal:** The project runs locally end to end, even if most features are still empty.

**What you will learn:**
- What Docker is and why it is useful for local development
- What a Python virtual environment is
- Why the project structure matters from day one

**Tasks:**
- [ ] Create a GitHub repository with a Python- and Node-friendly .gitignore
- [ ] Create a docker-compose.yml file with PostgreSQL and Redis services
- [ ] Scaffold the FastAPI backend folder structure
- [ ] Scaffold the React + Vite + TypeScript + Tailwind frontend
- [ ] Verify the backend starts and connects to the database
- [ ] Verify the frontend renders in the browser

**Backend folder structure:**

```text
backend/
├── api/           # HTTP routes only
├── services/      # Business logic
├── repositories/  # Database queries
├── models/        # SQLAlchemy table definitions
├── schemas/       # Pydantic request/response models
├── middleware/    # Auth, logging, error handling
├── utils/         # Shared helpers
└── tests/         # Unit and integration tests
```

**Done when:**
- docker compose up starts without errors
- FastAPI docs open at /docs
- The frontend opens locally in the browser

---

## Phase 1 — Authentication and User Management

**Goal:** Users can register, log in, and access protected routes.

**What you will learn:**
- JWT authentication
- Password hashing and secure auth flows
- Backend route and schema design

**Tasks:**
- [ ] Set up PostgreSQL connection and SQLAlchemy models
- [ ] Create user model and auth schemas
- [ ] Implement registration and login endpoints
- [ ] Implement JWT-based auth middleware
- [ ] Create /users/me endpoint for authenticated users
- [ ] Add tests for auth flows

**Done when:**
- A user can register and log in
- A protected endpoint returns the logged-in user information
- Requests without a valid token are rejected

---

## Phase 2 — Core CRM Modules

**Goal:** Build the main freelancer CRM features.

**Modules:**
- Leads
- Clients
- Projects
- Milestones
- Invoices
- Tasks
- Payments
- Notes
- Follow-ups

**Architecture rule:**
- Routes should only handle HTTP concerns
- Business logic belongs in services
- Database access belongs in repositories

**Tasks:**
- [ ] Create database models for all core modules
- [ ] Implement CRUD endpoints for each module
- [ ] Add validation with Pydantic schemas
- [ ] Link related entities correctly
- [ ] Add tests for each module

**Done when:**
- All 9 modules can be created, read, updated, and deleted
- No business logic is placed directly inside route files

---

## Phase 3 — Frontend Shell and Navigation

**Goal:** The app has a polished, usable UI shell.

**Tasks:**
- [ ] Build a login and registration screen
- [ ] Create the main dashboard layout
- [ ] Add sidebar navigation
- [ ] Build the base page structure for all modules
- [ ] Connect the frontend to backend APIs

**Done when:**
- A user can log in and land on the dashboard
- Sidebar navigation works across pages
- The UI feels like a real product, not just a prototype

---

## Phase 4 — Lead-to-Client Conversion Flow

**Goal:** A lead can be converted into a client and project flow.

**Tasks:**
- [ ] Create a lead form and list view
- [ ] Implement lead status handling
- [ ] Add conversion from lead to client
- [ ] Create project and milestone records automatically
- [ ] Show the new client and project in the UI

**Done when:**
- A lead can be created in the browser
- Converting the lead produces a client and related project data
- The dashboard reflects the updated state

---

## Phase 5 — Project Operations and Finance Flow

**Goal:** The app supports the full delivery and billing experience.

**Tasks:**
- [ ] Track milestones and completion status
- [ ] Generate invoices tied to milestones
- [ ] Record payments
- [ ] Show dashboard statistics for revenue, active projects, and pending invoices
- [ ] Add follow-up reminders and task tracking

**Done when:**
- A lead marked as won creates a client record
- Invoices are linked to milestones
- Dashboard metrics update correctly

---

## Phase 6 — AI Features

**Goal:** Add AI features that are genuinely useful and integrated into the product experience.

### AI features to build

1. AI Proposal Generator
   - Input: project type, client requirements, budget, timeline
   - Output: structured proposal with scope, deliverables, timeline, assumptions, and pricing summary
   - Frontend: “Generate with AI” button in the proposal form

2. Meeting Summarizer
   - Input: raw meeting notes
   - Output: structured summary, decisions, and action items
   - Frontend: “Summarize” button in the meeting notes view

3. Follow-Up Email Generator
   - Input: client context, meeting summary, and email type
   - Output: a polished email ready to send
   - Frontend: “Generate Email” panel in the client detail view

4. Task Prioritization
   - Input: open tasks, due dates, deadlines, and project status
   - Output: a ranked task list with reasoning
   - Frontend: “AI Priority View” tab on the tasks page

**Backend AI service structure:**

```text
backend/
└── services/
    └── ai/
        ├── proposal_generator.py
        ├── meeting_summarizer.py
        ├── email_generator.py
        └── task_prioritizer.py
```

**Tasks:**
- [ ] Set up LangChain and OpenAI in the backend with OPENAI_API_KEY in .env
- [ ] Build structured AI services with Pydantic output
- [ ] Expose each feature through dedicated /ai/ API endpoints
- [ ] Stream responses to the frontend using SSE
- [ ] Handle OpenAI errors gracefully
- [ ] Add testing for each AI workflow

**Done when:**
- All 4 AI features work end to end
- Structured outputs are validated and displayed in the UI
- Responses stream smoothly without breaking the interface

---

## Phase 7 — Production Readiness and Deployment

**Goal:** Make the app production-ready and launch it publicly.

**Engineering tasks:**
- [ ] RBAC middleware for admin vs. user roles
- [ ] Redis caching for frequently queried data
- [ ] Background reminder system for overdue invoices and upcoming milestones
- [ ] Email notifications with SendGrid or SES
- [ ] Structured logging
- [ ] Polished OpenAPI documentation

**Deployment tasks:**
- [ ] Production Docker build with multi-stage images
- [ ] AWS deployment using EC2 or ECS
- [ ] Environment variable management without secrets in code
- [ ] Domain and HTTPS setup

**Portfolio artifacts:**
- [ ] README with setup instructions and feature list
- [ ] Architecture diagram
- [ ] Screenshots of key pages
- [ ] Demo video (2–3 minutes)

**Done when:**
- The app is live at a real URL
- The GitHub repository looks polished and professional

---

## Phase Verification Checklist

| Phase | Done When |
| --- | --- |
| 0 | docker compose up starts cleanly and FastAPI docs load at /docs |
| 1 | Registration, login, and /users/me work with JWT |
| 2 | Full CRUD works for all core modules with clear service-layer separation |
| 3 | Login redirects to the dashboard and sidebar navigation works |
| 4 | A lead can be created in the browser and converted to a client flow |
| 5 | Lead conversion creates a client, invoice, and milestone flow with updated dashboard stats |
| 6 | All AI features work end to end with streaming and validated outputs |
| 7 | The app is live, documented, and demo-ready |

---

## Key Architecture Rules (enforced from day 1)
1. **No business logic in routes.** Routes call services. Services call repositories.
2. **No raw SQL.** All DB queries go through SQLAlchemy models and repositories.
3. **All input validated by Pydantic.** Never trust raw request data.
4. **One Alembic migration per schema change.** Never edit the DB manually.
5. **Secrets in `.env` only.** Never commit API keys or passwords to git.
6. **AI is a core deliverable.** All 4 AI features must be built and integrated. `OPENAI_API_KEY` is a required environment variable.-

---

## Resume Line (when done)>
 **FreelanceOS** — Full-stack SaaS platform for freelancers built with React, TypeScript, FastAPI, PostgreSQL, Redis, Docker, and AWS. Features lead and client management, milestone-based project delivery, invoicing, and payment tracking. Integrates AI-powered proposal generation, meeting summarization, follow-up email drafting, and task prioritization using LangChain and OpenAI — designed with production-grade prompt engineering and structured output parsing.
