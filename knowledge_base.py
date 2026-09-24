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
]

# Salesforce does not mandate one universal naming standard. These conventions are
# designed for source-driven development and use PEP as this org's identifier.
NAMING_STANDARDS = [
    {
        "component": "Custom Object",
        "keywords": ["custom object", "object"],
        "pattern": "BusinessEntity_PEP__c",
        "example": "Invoice_PEP__c",
        "guidance": "Use singular PascalCase nouns. Place _PEP before the required final __c API suffix.",
    },
    {
        "component": "Custom Field",
        "keywords": ["custom field", "field api", "field"],
        "pattern": "BusinessMeaning_PEP__c",
        "example": "InvoiceDate_PEP__c",
        "guidance": "Use PascalCase API names that state the business meaning. Place _PEP before the required final __c API suffix.",
    },
    {
        "component": "Apex Class",
        "keywords": ["apex class", "apex"],
        "pattern": "ObjectPurpose_PEP",
        "example": "InvoiceService_PEP",
        "guidance": "Use PascalCase. Name the role explicitly, such as Service, Selector, Domain, Controller, Batch, Queueable, or Test; test classes end in _PEPTest.",
    },
    {
        "component": "Apex Trigger",
        "keywords": ["apex trigger", "trigger"],
        "pattern": "ObjectTrigger_PEP",
        "example": "InvoiceTrigger_PEP",
        "guidance": "Use one trigger per object and keep it thin; put event-specific logic in a handler class rather than encoding events in multiple trigger names.",
    },
    {
        "component": "Lightning Web Component",
        "keywords": ["lightning web component", "lwc"],
        "pattern": "camelCaseFeaturePep",
        "example": "invoiceApprovalPanelPep",
        "guidance": "Use lower camel case for the bundle name. LWC names cannot use _PEP, so use the equivalent Pep suffix; its generated custom-element tag is namespaced automatically.",
    },
    {
        "component": "Flow",
        "keywords": ["flow", "workflow", "automation"],
        "pattern": "Object - Trigger - Action - PEP",
        "example": "Invoice - Before Save - Set Status - PEP",
        "guidance": "Use the flow label to identify the object, execution context, outcome, and PEP ownership. Do not include DEV, UAT, or PROD.",
    },
    {
        "component": "Validation Rule",
        "keywords": ["validation rule", "validation"],
        "pattern": "Object_Condition_PEP",
        "example": "Invoice_InvoiceDateRequired_PEP",
        "guidance": "Use a positive, searchable API name that describes the rule being enforced; write the error message in user language separately.",
    },
    {
        "component": "Record Type",
        "keywords": ["record type"],
        "pattern": "BusinessProcess_PEP",
        "example": "PartnerInvoice_PEP",
        "guidance": "Use a stable business classification, not a department or environment. Keep the developer name and label aligned where practical.",
    },
    {
        "component": "Permission Set",
        "keywords": ["permission set", "permission"],
        "pattern": "Persona_Feature_Access_PEP",
        "example": "Billing_Invoice_Edit_PEP",
        "guidance": "Describe the persona, feature, access level, and PEP ownership. Prefer permission sets and groups over role- or environment-specific names.",
    },
    {
        "component": "Report",
        "keywords": ["report"],
        "pattern": "Domain - Audience - Purpose - PEP",
        "example": "Billing - Finance - Monthly Invoices - PEP",
        "guidance": "Use report folders for ownership and a label that makes the intended audience and decision clear.",
    },
    {
        "component": "Dashboard",
        "keywords": ["dashboard"],
        "pattern": "Domain - Audience - Purpose - PEP",
        "example": "Sales - Leadership - Pipeline Health - PEP",
        "guidance": "Align the dashboard label with its audience and outcome; use folders for access control and organization.",
    },
    {
        "component": "Integration",
        "keywords": ["named credential", "external credential", "integration"],
        "pattern": "System_Purpose_PEP",
        "example": "ERP_InvoiceSync_PEP",
        "guidance": "Name credentials, external services, and integration fields for the external system and business capability, never for an environment or secret.",
    },
    {
        "component": "Page Layout",
        "keywords": ["page layout", "layout"],
        "pattern": "Object - Audience - PEP",
        "example": "Invoice - Billing - PEP",
        "guidance": "Use a label that identifies the object, audience, and PEP ownership.",
    },
    {
        "component": "Profile",
        "keywords": ["profile"],
        "pattern": "Persona_PEP",
        "example": "StandardUser_PEP",
        "guidance": "Keep profiles minimal and use permission sets for feature access; use the PEP suffix on any custom profile.",
    },
    {
        "component": "Role",
        "keywords": ["role hierarchy", "user role", "role"],
        "pattern": "BusinessUnit_Role_PEP",
        "example": "Sales_Manager_PEP",
        "guidance": "Name the business unit and responsibility; do not use environment names.",
    },
    {
        "component": "Sharing Rule",
        "keywords": ["sharing rule", "sharing"],
        "pattern": "Object_AccessPurpose_PEP",
        "example": "Invoice_FinanceRead_PEP",
        "guidance": "Describe the object and access purpose, not the formula or implementation method.",
    },
    {
        "component": "Email Template",
        "keywords": ["email template", "email"],
        "pattern": "BusinessPurpose_PEP",
        "example": "InvoiceDueReminder_PEP",
        "guidance": "Name the communication's business purpose and use a folder for ownership and access.",
    },
    {
        "component": "Approval Process",
        "keywords": ["approval process", "approval"],
        "pattern": "Object_Process_PEP",
        "example": "Invoice_Approval_PEP",
        "guidance": "Identify the object and approval purpose; do not include a dollar threshold that is likely to change.",
    },
    {
        "component": "Custom Metadata Type",
        "keywords": ["custom metadata type", "custom metadata"],
        "pattern": "ConfigurationPurpose_PEP__mdt",
        "example": "InvoiceThreshold_PEP__mdt",
        "guidance": "Place _PEP before the required final __mdt API suffix and name the configuration purpose, not a specific environment.",
    },
]

NAMING_STANDARDS_ANSWER = (
    "This org's naming standard uses `_PEP` for all supported components. For custom object, field, and "
    "custom metadata APIs, `_PEP` appears before Salesforce's required final suffix (`__c` or `__mdt`). "
    "LWC bundle names use `Pep` because underscores are not valid in LWC names. Do not embed environment "
    "names in deployable metadata.\n\n"
    "Component | Pattern | Example\n"
    "--- | --- | ---\n"
    + "\n".join(
        f"{standard['component']} | `{standard['pattern']}` | `{standard['example']}`"
        for standard in NAMING_STANDARDS
    )
)

KNOWLEDGE_BASE.append(
    {
        "keywords": ["naming standard", "naming standards", "naming convention", "naming conventions"],
        "answer": NAMING_STANDARDS_ANSWER,
    }
)

for standard in NAMING_STANDARDS:
    KNOWLEDGE_BASE.append(
        {
            "keywords": ["naming", "convention", "standard", *standard["keywords"]],
            "answer": (
                f"{standard['component']} naming standard:\n"
                f"Pattern: `{standard['pattern']}`\n"
                f"Example: `{standard['example']}`\n"
                f"Guidance: {standard['guidance']}"
            ),
        }
    )

# Common Salesforce components expressed as data so the bot can give developers
# a definition and example instead of only matching deployment terminology.
SALESFORCE_COMPONENTS = [
    {
        "component": "Custom Object",
        "keywords": ["custom object", "object"],
        "definition": "A custom object is a database table you create to store business data that standard Salesforce objects do not cover.",
        "example": "An Invoice__c object can store invoice number, amount, due date, and its relationship to an Account.",
    },
    {
        "component": "Custom Field",
        "keywords": ["custom field", "field"],
        "definition": "A custom field is a column added to a standard or custom object to capture one additional piece of data.",
        "example": "Invoice__c.InvoiceDate__c can be a Date field that records when an invoice was issued.",
    },
    {
        "component": "Page Layout",
        "keywords": ["page layout", "layout"],
        "definition": "A page layout controls which fields, related lists, buttons, and quick actions users see when viewing or editing a record.",
        "example": "An Invoice page layout can place Amount and Due Date at the top, show Invoice Lines as a related list, and expose a Submit for Approval action.",
    },
    {
        "component": "Record Type",
        "keywords": ["record type"],
        "definition": "A record type lets one object support different business processes, picklist values, and page layouts for different users or records.",
        "example": "An Account can have Customer and Partner record types, each with its own sales process and layout.",
    },
    {
        "component": "Validation Rule",
        "keywords": ["validation rule"],
        "definition": "A validation rule prevents a record from being saved when its formula evaluates to true.",
        "example": "An Invoice validation rule can require DueDate__c when Status__c is Sent.",
    },
    {
        "component": "Flow",
        "keywords": ["flow", "workflow", "automation"],
        "definition": "A flow is Salesforce's declarative automation tool for updating data, guiding users through screens, calling actions, and running logic on a schedule or record change.",
        "example": "A record-triggered flow can set an Invoice status to Overdue when its due date passes and the balance remains unpaid.",
    },
    {
        "component": "Apex Class",
        "keywords": ["apex class", "apex"],
        "definition": "An Apex class is server-side Salesforce code that contains reusable business logic.",
        "example": "InvoiceService can calculate an invoice balance and be called by a flow, Lightning component, or REST endpoint.",
    },
    {
        "component": "Apex Trigger",
        "keywords": ["apex trigger", "trigger"],
        "definition": "An Apex trigger runs code before or after records are inserted, updated, deleted, or undeleted.",
        "example": "InvoiceTrigger can call InvoiceTriggerHandler before insert to populate a default payment term.",
    },
    {
        "component": "Lightning Web Component",
        "keywords": ["lightning web component", "lwc"],
        "definition": "A Lightning Web Component is a reusable client-side UI component built with HTML, JavaScript, and CSS for Lightning Experience.",
        "example": "invoiceApprovalPanel can show invoice details and let an approver approve or reject the record.",
    },
    {
        "component": "Permission Set",
        "keywords": ["permission set", "permission"],
        "definition": "A permission set grants additional object, field, app, and system access to users without changing their profile.",
        "example": "Billing_Invoice_Edit can grant the Billing team edit access to Invoice__c and its Amount__c field.",
    },
    {
        "component": "Profile",
        "keywords": ["profile"],
        "definition": "A profile provides each user with baseline login, app, object, and field access; Salesforce recommends keeping profiles minimal and layering access with permission sets.",
        "example": "A Standard User profile can provide baseline access while a Billing permission set grants invoice-specific permissions.",
    },
    {
        "component": "Role",
        "keywords": ["role hierarchy", "user role", "role"],
        "definition": "A role places a user in the role hierarchy, which can extend record visibility upward through the organization.",
        "example": "A Sales Manager role can allow a manager to see records owned by users in Sales Representative roles below it.",
    },
    {
        "component": "Sharing Rule",
        "keywords": ["sharing rule", "sharing"],
        "definition": "A sharing rule automatically grants record access to users in roles, public groups, territories, or queues based on record ownership or criteria.",
        "example": "A criteria-based rule can share high-value Invoice__c records with the Finance Operations public group.",
    },
    {
        "component": "Report",
        "keywords": ["report"],
        "definition": "A report is a configurable query and presentation of Salesforce records that users can filter, group, chart, export, or schedule.",
        "example": "Monthly Invoices by Account can group Invoice__c records by Account and sum Amount__c for the current month.",
    },
    {
        "component": "Dashboard",
        "keywords": ["dashboard"],
        "definition": "A dashboard displays report data as charts, metrics, gauges, or tables for monitoring a business outcome.",
        "example": "Billing Health can show overdue invoice count, total outstanding balance, and a chart of invoices by status.",
    },
    {
        "component": "Email Template",
        "keywords": ["email template", "email"],
        "definition": "An email template is a reusable email message that can merge Salesforce record data into a consistent communication.",
        "example": "Invoice Due Reminder can greet the Account contact and merge the invoice number and due date.",
    },
    {
        "component": "Approval Process",
        "keywords": ["approval process", "approval"],
        "definition": "An approval process routes records through defined approval steps and can update fields, send notifications, or lock records.",
        "example": "Invoice Approval can require Finance Manager approval before an invoice over $10,000 is sent.",
    },
    {
        "component": "Custom Metadata Type",
        "keywords": ["custom metadata type", "custom metadata"],
        "definition": "A custom metadata type stores deployable configuration records that Apex, flows, and formulas can reference.",
        "example": "InvoiceThreshold__mdt can hold country-specific approval limits deployed with the application.",
    },
    {
        "component": "Named Credential",
        "keywords": ["named credential", "external credential"],
        "definition": "A named credential stores an external endpoint and links it to an external credential that manages authentication, so code does not contain secrets.",
        "example": "ERP_InvoiceSync can let Apex call an ERP API using a configured OAuth principal.",
    },
]

for component in SALESFORCE_COMPONENTS:
    KNOWLEDGE_BASE.append(
        {
            "keywords": component["keywords"],
            "answer_type": "definition",
            "answer": (
                f"{component['component']}: {component['definition']}\n\n"
                f"Example: {component['example']}"
            ),
        }
    )

FALLBACK_ANSWER = (
    "I don't have an answer for that yet. Try rephrasing your question, or ask about change sets, "
    "the Metadata API, managed/unlocked packages, scratch orgs, CI/CD, DevOps Center, permission sets, "
    "sandboxes, validation deployments, destructive changes, deployment order, Salesforce components, or "
    "naming conventions."
)
