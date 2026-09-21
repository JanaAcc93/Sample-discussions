# Knowledge base of Salesforce deployment components, based on official Salesforce
# documentation (Salesforce Help, Salesforce DX Developer Guide, and Trailhead).
# Each entry has trigger keywords and a canned answer.
KNOWLEDGE_BASE = [
    {
        "keywords": ["change set", "change sets"],
        "answer": "Change sets let you send customizations from one org to a related org (e.g. sandbox "
        "to production) without using the Metadata API directly. Orgs must be connected via a "
        "deployment connection. Outbound change sets are created and uploaded from the source org; "
        "inbound change sets are validated and deployed from the target org. Change sets can't include "
        "all metadata types (e.g. some Apex settings, certain sharing rules) and don't support version "
        "control, so Salesforce recommends them mainly for simple, small-team deployments rather than "
        "enterprise release processes.",
    },
    {
        "keywords": ["metadata api", "metadata deploy", "retrieve metadata"],
        "answer": "The Metadata API lets you retrieve, deploy, create, update, and delete customization "
        "information (metadata) for your org, such as custom object definitions and page layouts. It's "
        "the foundation used by Salesforce CLI (sf/sfdx), Ant Migration Tool, and most CI/CD tooling. "
        "Deployments use a package.xml manifest to define which components to include, and can be run "
        "as a validation-only 'check-only' deploy before a real deploy.",
    },
    {
        "keywords": ["managed package", "second-generation", "2gp"],
        "answer": "Second-generation managed packages (2GP) are Salesforce's recommended packaging model "
        "for building and distributing apps (e.g. on AppExchange). They're built with Salesforce DX and "
        "scratch orgs, support source control natively, and produce versioned, installable package "
        "versions. Namespaced 2GP managed packages replace the older first-generation (1GP) managed "
        "packages for new development.",
    },
    {
        "keywords": ["unlocked package", "unlocked packages"],
        "answer": "Unlocked packages are Salesforce's recommended way to package and deploy metadata for "
        "a single org or a small set of related orgs (not for AppExchange distribution). Unlike managed "
        "packages, subscribers can inspect and modify unlocked package metadata. They support source-driven, "
        "modular development and are commonly used to organize enterprise metadata into logical, "
        "versioned units deployed via CI/CD pipelines.",
    },
    {
        "keywords": ["scratch org", "scratch orgs"],
        "answer": "Scratch orgs are temporary, source-driven Salesforce orgs used for development and "
        "automated testing. They are created from a configuration (project-scratch-def.json) via "
        "Salesforce CLI, fully configurable to emulate specific editions/features, and disposable — "
        "typically deleted after a feature branch is merged. Salesforce recommends scratch orgs as the "
        "standard development environment for source-driven, package-based development.",
    },
    {
        "keywords": ["ci/cd", "continuous integration", "continuous delivery", "pipeline"],
        "answer": "Salesforce's recommended CI/CD approach uses Salesforce CLI (sf) with source-driven "
        "development: metadata is stored in version control, and pipelines run 'sf project deploy start' "
        "(validation and deployment), automated Apex tests, and static code analysis on each commit/PR. "
        "Salesforce provides prebuilt CI/CD templates and reference architecture for GitHub Actions, "
        "GitLab CI, Azure DevOps, CircleCI, Jenkins, and Bitbucket Pipelines.",
    },
    {
        "keywords": ["devops center"],
        "answer": "DevOps Center is Salesforce's low-code release management tool that lets teams manage "
        "the software development lifecycle (planning, developing, testing, deploying) directly within "
        "Salesforce, backed by a GitHub repository. It automates source tracking, branching, and "
        "promotion of changes through a pipeline of environments (e.g. dev sandbox -> QA -> staging -> "
        "production) without requiring deep Git expertise.",
    },
    {
        "keywords": ["permission set", "permission sets", "profile", "profiles"],
        "answer": "Salesforce recommends using permission sets (and permission set groups) rather than "
        "profiles to grant access, because they let you assign granular permissions to users without "
        "changing their profile. Profiles should be kept minimal (login/session settings and baseline "
        "object access), while permission sets layer on top for feature- and role-specific access. This "
        "makes deployments and access changes easier to manage incrementally.",
    },
    {
        "keywords": ["sandbox", "sandboxes"],
        "answer": "Sandboxes are copies of your production org used for development, testing, and "
        "staging without affecting live data. Salesforce recommends a multi-sandbox strategy (e.g. "
        "Developer, Developer Pro, Partial Copy, Full copy sandboxes) aligned to a release pipeline, "
        "where changes are developed and validated in lower environments before being promoted to "
        "production.",
    },
    {
        "keywords": ["validate", "validation only", "check only"],
        "answer": "A validation-only deployment (check-only) runs all deployment steps, including Apex "
        "tests, without actually saving the changes to the target org. This lets you confirm a deployment "
        "will succeed before running it for real, and is recommended as part of a CI pipeline gate before "
        "merging or deploying to production.",
    },
    {
        "keywords": ["destructive change", "destructivechanges", "delete metadata"],
        "answer": "Destructive changes (deleting metadata) are deployed using a destructiveChanges.xml "
        "manifest alongside package.xml. Salesforce recommends deploying destructive changes separately "
        "from additive changes, and running them after the corresponding code/metadata dependencies have "
        "already been removed, to avoid dependency errors.",
    },
    {
        "keywords": ["deployment order", "dependencies", "deploy order"],
        "answer": "Salesforce metadata deployments are dependency-aware for a single deploy, but "
        "cross-metadata dependencies (e.g. a flow referencing a custom field that doesn't exist yet) can "
        "still cause failures. Salesforce recommends deploying in logical units (e.g. via unlocked "
        "packages) and testing deployments in a full or partial sandbox copy that mirrors production "
        "dependencies before deploying to production.",
    },
    {
        "keywords": ["naming convention", "department", "role-based", "custom object"],
        "answer": "Q: What's the role-based naming convention for a Custom Object? (Good for large "
        "teams with multiple admins/developers)\n"
        "A: `Dept_ObjectName__c` (e.g. `FIN_Invoice__c`). Prefix by department for clarity.",
    },
    {
        "keywords": ["naming convention", "department", "role-based", "field api", "custom field"],
        "answer": "Q: What's the role-based naming convention for a Field (API)?\n"
        "A: `deptFieldName__c` (e.g. `finInvoiceDate__c`). Matches the object's department prefix for "
        "grouping.",
    },
    {
        "keywords": ["naming convention", "department", "role-based", "flow", "workflow"],
        "answer": "Q: What's the role-based naming convention for a Flow?\n"
        "A: `Dept_Action_Object` (e.g. `FIN_Approve_Invoice`). Easy to search by department.",
    },
    {
        "keywords": ["naming convention", "department", "role-based", "report"],
        "answer": "Q: What's the role-based naming convention for a Report?\n"
        "A: `Dept - Report Name` (e.g. `FIN - Monthly Revenue`). Consistent folder sorting.",
    },
    {
        "keywords": ["naming convention", "lifecycle", "environment", "sandbox"],
        "answer": "Q: What's the lifecycle/environment-based naming convention for a Sandbox? (Useful "
        "for orgs with multiple sandboxes and deployment stages)\n"
        "A: `EnvType_Project` (e.g. `DEV_InvoiceApp`), using env types like DEV, UAT, QA, PROD.",
    },
    {
        "keywords": ["naming convention", "lifecycle", "environment", "flow", "workflow"],
        "answer": "Q: What's the lifecycle/environment-based naming convention for a Flow?\n"
        "A: `Env_Object_Action` (e.g. `UAT_Invoice_Approval`). Helps track versions per environment.",
    },
    {
        "keywords": ["naming convention", "lifecycle", "environment", "apex class"],
        "answer": "Q: What's the lifecycle/environment-based naming convention for an Apex Class?\n"
        "A: `Env_ObjectPurpose` (e.g. `QA_InvoiceValidator`). Avoids confusion during testing.",
    },
    {
        "keywords": ["naming convention", "lifecycle", "environment", "report"],
        "answer": "Q: What's the lifecycle/environment-based naming convention for a Report?\n"
        "A: `Env - Report Name` (e.g. `UAT - Invoice Summary`). Clear separation of test vs. live.",
    },
    {
        "keywords": ["naming convention", "function-oriented", "process", "flow", "workflow"],
        "answer": "Q: What's the function-oriented naming convention for a Flow? (Best for "
        "process-heavy orgs with automation focus)\n"
        "A: `Process_Object_Action` (e.g. `Approval_Invoice_Manager`). Start with the process type.",
    },
    {
        "keywords": ["naming convention", "function-oriented", "process", "validation rule"],
        "answer": "Q: What's the function-oriented naming convention for a Validation Rule?\n"
        "A: `Check_Object_Field` (e.g. `Check_Invoice_Date`). Easy to scan in lists.",
    },
    {
        "keywords": ["naming convention", "function-oriented", "process", "trigger"],
        "answer": "Q: What's the function-oriented naming convention for a Trigger?\n"
        "A: `Object_Event_Trigger` (e.g. `Invoice_BeforeInsert_Trigger`). Include the event type.",
    },
    {
        "keywords": ["naming convention", "function-oriented", "process", "dashboard"],
        "answer": "Q: What's the function-oriented naming convention for a Dashboard?\n"
        "A: `Function_Audience` (e.g. `Sales_Performance_Exec`). Clarifies purpose and audience.",
    },
]

FALLBACK_ANSWER = (
    "I don't have an answer for that yet. Try rephrasing your question, or ask about change sets, "
    "the Metadata API, managed/unlocked packages, scratch orgs, CI/CD, DevOps Center, permission sets, "
    "sandboxes, validation deployments, destructive changes, deployment order, or naming conventions."
)
