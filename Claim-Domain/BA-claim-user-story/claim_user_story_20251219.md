---
title: "Claim User Story 20251219"
date: 2025-12-19
---



## Initiative: Product Foundation

### Epic: Products in Scope

#### Feature: Products in Scope
---

### Epic: Policy Detail

#### Feature: Policy Detail
---
## Initiative: Customer Portfolio Claim View

### Epic: Search for a claim/event case

#### Feature: Search for a claim/event case
- **Role**: Customer Service Representative
- **Action**: search and locate case or claim records across multiple lines of business using flexible search criteria
- **Value**: I can quickly access relevant case and claim information to respond to customer inquiries and route them to appropriate workflows

**Description:**

> As a **Customer Service Representative**,
> I want to **search and locate case or claim records across multiple lines of business using flexible search criteria**,
> So that **I can quickly access relevant case and claim information to respond to customer inquiries and route them to appropriate workflows**


**Key Capabilities:**

> 1. User initiates search through single-line entry with real-time autosuggestion matching against claim identifiers, parties, and policies
>     1.1 Upon selection from autosuggestions, system navigates to appropriate workflow based on line of business and completion status
> 2. User applies advanced search filters using multiple optional parameters including identifiers, dates, party information, policy details, and claim types
> 3. System displays search results with sortable and filterable attributes including status, claim type, loss dates, and subject details
>     3.1 When user selects a result, system routes to appropriate claim overview, intake form, or case management page
> 4. User refines search results by removing individual filter tags or clearing all applied criteria
> 5. Upon encountering no results, user accesses parameter adjustment guidance to modify search strategy

---

### Epic: View history of claims/event cases

#### Feature: View history of claims/event cases
- **Role**: Customer Service Representative
- **Action**: access and review comprehensive claim and case history for a customer across all product lines
- **Value**: I can quickly understand the customer's complete loss history and provide informed service or make referrals for further claim handling

**Description:**

> As a **Customer Service Representative**,
> I want to **access and review comprehensive claim and case history for a customer across all product lines**,
> So that **I can quickly understand the customer's complete loss history and provide informed service or make referrals for further claim handling**


**Key Capabilities:**

> 1. User navigates to customer portfolio and retrieves consolidated claim and case history across multiple product lines
> 2. System presents searchable claim list with status indicators, loss dates, policy associations, and affected subjects
>     2.1 Upon toggling view mode, system adjusts sorting between claim-centric and case-centric display
> 3. User filters and sorts records to locate specific claims or cases based on date, status, or product line
> 4. User selects claim or case identifier to navigate to detailed product-specific overview for in-depth investigation
> 5. User accesses linked policy information to verify coverage context
> 6. System provides pagination controls for navigating large claim histories

---

### Epic: Action: Create New Case/Claim

#### Feature: Action: Create New Case/Claim
- **Role**: Customer Service Representative
- **Action**: initiate a new claim or case for a customer across multiple insurance product lines
- **Value**: customers receive timely claim processing through the appropriate intake channel based on their policy type and organizational relationship

**Description:**

> As a **Customer Service Representative**,
> I want to **initiate a new claim or case for a customer across multiple insurance product lines**,
> So that **customers receive timely claim processing through the appropriate intake channel based on their policy type and organizational relationship**.


**Key Capabilities:**

> 1. User accesses customer portfolio and selects create new claim action
> 2. System presents claim type options filtered by customer eligibility and product coverage
> 3. User selects appropriate claim category based on policy type
>     3.1 Upon selecting benefits coverage, system routes to standard event case intake
>     3.2 When group-sponsored individual selects portal option, system routes to employer portal workflow
>     3.3 If property or pet coverage selected, system validates individual customer status before proceeding
> 4. System initiates product-specific intake process with pre-populated customer context
> 5. User proceeds with claim details capture in designated intake interface

---
## Initiative: Open New Event Case

### Epic: Intake Sources

#### Feature: Intake Sources
- **Role**: Customer Service Representative
- **Action**: initiate and complete event case intake across multiple lines of business to automatically generate applicable claims based on member circumstances
- **Value**: the system efficiently creates a unified case structure with appropriate claims, ensuring accurate benefit adjudication while reducing manual effort and eligibility errors

**Description:**

> As a **Customer Service Representative**,
> I want to **initiate and complete event case intake across multiple lines of business to automatically generate applicable claims based on member circumstances**,
> So that **the system efficiently creates a unified case structure with appropriate claims, ensuring accurate benefit adjudication while reducing manual effort and eligibility errors**


**Key Capabilities:**

> 1. User initiates case creation by identifying member and providing employment context
>     1.1 Upon member not found, user is able to create new member record inline
>     1.2 When initiated from customer portfolio, system pre-populates member and employer information
> 2. User provides reporting details, selects claim subject and type of loss event
> 3. User documents event information including diagnosis codes and circumstances
> 4. User designates reporting party and completes intake process
> 5. System evaluates policy applicability rules against loss type and automatically generates eligible claims
>     5.1 System excludes master policies that have corresponding certificate policies
>     5.2 System prevents claim generation for canceled policies
> 6. System finalizes case in open status with all applicable claims initialized for adjudication

---

### Epic: Navigate step by step wizard

#### Feature: Navigate step by step wizard
- **Role**: Customer Service Representative
- **Action**: initiate and complete a structured event case intake through sequential information gathering stages
- **Value**: the system can automatically generate associated claims with accurate member, loss, and party details for efficient downstream adjudication

**Description:**

> As a **Customer Service Representative**,
> I want to **initiate and complete a structured event case intake through sequential information gathering stages**,
> So that **the system can automatically generate associated claims with accurate member, loss, and party details for efficient downstream adjudication**


**Key Capabilities:**

> 1. User initiates case creation by identifying and validating the insured member against group sponsor eligibility requirements
> 2. Upon member validation, system provisions draft case workspace with unique case identifier and enables progressive data capture
> 3. User provides loss event details including classification, occurrence dates, affected loss types, and diagnostic information with system validation for data completeness
> 4. When navigating between workflow stages, system persists draft data and enforces sequential progression while allowing revisitation of completed stages
> 5. User designates additional involved parties and their relationships to the insured member
> 6. Upon intake completion, system automatically generates associated loss records based on selected event types and navigates to case management workspace

---

### Epic: Member Detail

#### Feature: Member Info
- **Role**: Claim Intaker
- **Action**: associate an injured member with a new event case by searching existing customers or registering new individuals
- **Value**: the case can be accurately linked to the correct injured party and their employment context, enabling proper claim adjudication

**Description:**

> As a **Claim Intaker**,
> I want to **associate an injured member with a new event case by searching existing customers or registering new individuals**,
> So that **the case can be accurately linked to the correct injured party and their employment context, enabling proper claim adjudication**.


**Key Capabilities:**

> 1. User initiates member association workflow as first step of case creation process
> 2. User searches existing customers by identity attributes; system returns prioritized matches from customer database
>     2.1 If customer exists, system retrieves and displays member with associated employment and address data
>     2.2 If customer not found, user registers new member by providing identity, contact preferences, location, and employment information
> 3. Upon member selection or registration, system validates employment context by associating employer organization
> 4. System prepopulates work details (occupation, hire date, work location) from existing employment records when available
> 5. System captures or retrieves member address information for correspondence and jurisdiction determination
> 6. User confirms member association; system locks member selection and enables progression to incident details capture

---

#### Feature: Work Details
- **Role**: Claim Intaker
- **Action**: capture and validate member employment information during event case initiation
- **Value**: the system maintains accurate member work relationships and employment data required for case processing and eligibility determination

**Description:**

> As a **Claim Intaker**,
> I want to **capture and validate member employment information during event case initiation**,
> So that **the system maintains accurate member work relationships and employment data required for case processing and eligibility determination**


**Key Capabilities:**

> 1. User initiates member identification and searches existing member records or adds new member to the case
> 2. Upon member selection, user provides employer affiliation from validated group sponsors
>     2.1 System dynamically reveals employment detail capture fields when employer is selected
>     2.2 System auto-populates work details from authoritative customer data sources with fallback hierarchy
> 3. System displays member address information in read-only format from customer entity records
> 4. User completes employment profile including work jurisdiction, occupation classification, and hire date
> 5. User submits member work details to create employee record and advance case workflow
> 6. User can return to revise employment details while address data remains protected from modification

---

### Epic: Case Detail

#### Feature: Case Detail - Generic Details(Subject of Claim, Accident vs Sickness etc.)
- **Role**: Customer Service Representative
- **Action**: capture comprehensive event case details, identify claim subjects, classify loss types, and record diagnosis information during the case intake process
- **Value**: the system accurately categorizes and routes claims based on loss characteristics, enabling efficient downstream adjudication and ensuring complete case documentation from initial intake

**Description:**

> As a **Customer Service Representative**,
> I want to **capture comprehensive event case details, identify claim subjects, classify loss types, and record diagnosis information during the case intake process**,
> So that **the system accurately categorizes and routes claims based on loss characteristics, enabling efficient downstream adjudication and ensuring complete case documentation from initial intake**


**Key Capabilities:**

> 1. User is able to record core event metadata including reporting method, reported date, event date, and narrative description of the incident
> 2. User is able to identify claim subjects by selecting from active member and dependent relationships or registering new individuals not previously in the system
> 3. User is able to classify the loss origin as accident, sickness, or other to determine applicable coverage and investigation requirements
> 4. User is able to select multiple loss types from predefined categories (death, absence, serious illness, accident, hospital service, wellness, accelerated death, work accommodation) that apply to the event
>     4.1 System enforces business rules such as disabling absence selection when the subject is not the primary member
> 5. User is able to capture and manage diagnosis codes with primary designation and effective dates to support medical claim processing
> 6. Upon completion, system routes to additional information collection specific to selected loss types for comprehensive case documentation

---

#### Feature: Case Detail - ICD Code
- **Role**: Case Manager
- **Action**: maintain and update medical diagnosis information (ICD codes) associated with event cases throughout the claim lifecycle
- **Value**: event case records remain accurate and comprehensive, enabling proper claim adjudication and ensuring associated claims reflect current medical conditions

**Description:**

> As a **Case Manager**,
> I want to **maintain and update medical diagnosis information (ICD codes) associated with event cases throughout the claim lifecycle**,
> So that **event case records remain accurate and comprehensive, enabling proper claim adjudication and ensuring associated claims reflect current medical conditions**.


**Key Capabilities:**

> 1. User is able to access existing event case diagnosis records and associated medical information
> 2. User is able to add new diagnosis entries with standardized medical codes and classifications
>     2.1 Upon selection, system validates code format and retrieval from medical terminology database
>     2.2 User designates primary diagnosis indicator and effective dates
> 3. User is able to modify diagnosis details for open cases while preserving audit history
> 4. When saving diagnosis updates, system validates data completeness and invokes duplicate case detection logic
> 5. System propagates diagnosis changes to applicable associated claims based on product type and claim status
> 6. Upon case closure, system restricts diagnosis modifications and transitions to read-only access mode

---

### Epic: Claim Events

#### Feature: Define Applicable Events
- **Role**: Claim Adjuster
- **Action**: define, update, and associate loss events to an event case to determine applicable claims and ensure accurate case categorization
- **Value**: the system automatically creates or updates claims based on event types, maintains data integrity across multiple claim lines, and enables proper loss adjudication

**Description:**

> As a **Claim Adjuster**,
> I want to **define, update, and associate loss events to an event case to determine applicable claims and ensure accurate case categorization**,
> So that **the system automatically creates or updates claims based on event types, maintains data integrity across multiple claim lines, and enables proper loss adjudication**


**Key Capabilities:**

> 1. User accesses case overview and views current claim events, injury/sickness classification, and diagnostic codes
> 2. User initiates event modification and selects new loss types from available options (Death, Accident, Wellness, Hospital Services, etc.)
>     2.1 Upon case closure status, user views event details in read-only mode without edit capability
>     2.2 When subject is non-employee, absence loss type becomes unavailable for selection
> 3. User provides loss-specific information based on selected event types and manages diagnostic code records
> 4. User submits event updates triggering duplicate case validation
> 5. System cascades changes to existing associated claims and auto-creates new claims for newly added loss types
> 6. System refreshes case overview displaying updated events and maintains claim line integrity

---

#### Feature: Event details - Absence
- **Role**: Claim Intaker
- **Action**: capture and validate employee absence information including reasons, periods, work schedule, and critical absence dates
- **Value**: the absence case is properly established with complete foundational data, enabling accurate benefit adjudication and timely claims processing

**Description:**

> As a **Claim Intaker**,
> I want to **capture and validate employee absence information including reasons, periods, work schedule, and critical absence dates**,
> So that **the absence case is properly established with complete foundational data, enabling accurate benefit adjudication and timely claims processing**.


**Key Capabilities:**

> 1. User is able to specify one or multiple absence reasons based on organizational policy rules
> 2. User is able to define one or multiple absence periods with actual dates and return-to-work information
> 3. User is able to configure typical work schedule including work days and daily hours
>     3.1 Upon system integration availability, work schedule defaults from employee master data
> 4. User is able to capture critical absence timeline including initial absence date, actively-at-work date, and last-worked date
> 5. User is able to optionally record hospitalization and outpatient surgery dates when applicable
> 6. System validates date logical consistency and prevents submission when mandatory absence information is incomplete

---

#### Feature: Event details - Death
- **Role**: Customer Service Representative
- **Action**: capture death-specific loss information during event case initiation
- **Value**: the insurer can accurately document critical death details required for claims adjudication and compliance

**Description:**

> As a **Customer Service Representative**,
> I want to **capture death-specific loss information during event case initiation**,
> So that **the insurer can accurately document critical death details required for claims adjudication and compliance**


**Key Capabilities:**

> 1. User initiates death event case and system activates death-specific information collection workflow
> 2. User provides mandatory official death date and optional supporting details including certificate receipt date, manner and cause of death, underlying conditions, and death location
>     2.1 Upon entering official death date earlier than event date, system issues warning but permits continuation
> 3. System validates completeness of mandatory death information before allowing progression
> 4. System adapts data collection based on jurisdictional requirements and regional locale settings
> 5. User submits death event details and system persists information for claims processing

---

#### Feature: Event details - Accelerated Death
- **Role**: Customer Service Representative
- **Action**: capture accelerated death event details including medical timeline and life expectancy information during event intake
- **Value**: the system accurately documents critical medical milestones required for policy benefit adjudication and regulatory compliance

**Description:**

> As a **Customer Service Representative**,
> I want to **capture accelerated death event details including medical timeline and life expectancy information during event intake**,
> So that **the system accurately documents critical medical milestones required for policy benefit adjudication and regulatory compliance**


**Key Capabilities:**

> 1. System triggers accelerated death information collection when loss type is designated during event intake
> 2. User captures medical timeline milestones including prescribed life expectancy duration and diagnosis date
> 3. System validates temporal consistency of medical events against reported event date
>     3.1 When diagnosis date precedes event date, system alerts user while permitting acknowledgment to proceed
> 4. User optionally documents treatment commencement date to complete medical history
> 5. System persists captured medical data and advances intake workflow upon completion

---

#### Feature: Event details - Serious Illness
- **Role**: Customer Service Representative
- **Action**: capture critical illness diagnosis and treatment information during event intake
- **Value**: the claim can be properly classified, routed, and adjudicated with complete medical context from the first notification

**Description:**

> As a **Customer Service Representative**,
> I want to **capture critical illness diagnosis and treatment information during event intake**,
> So that **the claim can be properly classified, routed, and adjudicated with complete medical context from the first notification**


**Key Capabilities:**

> 1. User reports a serious illness loss event and system presents structured intake workflow
> 2. User provides mandatory diagnosis information including diagnosis date and standardized diagnostic codes
> 3. User optionally records treatment timeline details and medical provider information
>     3.1 Upon diagnosis date being earlier than event date, system issues warning but permits progression
>     3.2 When treatment date precedes diagnosis date, system prevents submission until corrected
> 4. System validates completeness and logical consistency of medical information
> 5. User submits intake data and system persists event details for claim adjudication

---

#### Feature: Event details - Hospital services
- **Role**: Customer Service Representative
- **Action**: capture and manage hospital services information during event case intake
- **Value**: accurate loss event documentation enables timely claim processing and appropriate service allocation

**Description:**

> As a **Customer Service Representative**,
> I want to **capture and manage hospital services information during event case intake**,
> So that **accurate loss event documentation enables timely claim processing and appropriate service allocation**.


**Key Capabilities:**

> 1. User initiates hospital services loss intake process and specifies number of service episodes to document
> 2. User captures service details including provider identification, treatment codes, and service timing for each episode
>     2.1 Upon entering dates, system validates temporal consistency with event occurrence
>     2.2 User provides either specific service date or date range per business requirements
> 3. User submits service records for system validation and storage
> 4. User reviews aggregated service list and is able to modify or remove records as needed
> 5. When editing existing records, system pre-populates data for correction
> 6. User finalizes intake documentation and advances to subsequent case processing stages

---

#### Feature: Event details - Accident details
- **Role**: Customer Service Representative
- **Action**: collect and validate accident-specific event details during loss intake
- **Value**: the system captures comprehensive accident information to enable accurate claim processing and routing

**Description:**

> As a **Customer Service Representative**,
> I want to **collect and validate accident-specific event details during loss intake**,
> So that **the system captures comprehensive accident information to enable accurate claim processing and routing**


**Key Capabilities:**

> 1. User selects accident loss type, triggering collection of accident-specific details
> 2. User provides temporal information including accident date and initial treatment date with system validation
> 3. User specifies accident location and circumstances from standardized reference data
>     3.1 Upon selecting non-standard location, user provides additional descriptive information
> 4. User indicates employment and activity-related context through classification flags
>     4.1 When claim subject is a minor, user classifies organized sport involvement
> 5. User identifies affected loss items from multi-value selection options
> 6. System validates data completeness and logical consistency before advancing intake workflow

---

#### Feature: Event details - Wellness
- **Role**: Customer Service Representative
- **Action**: capture essential wellness visit information during event case initiation to establish the foundational claim record
- **Value**: the system can automatically classify the wellness event, prepopulate clinical codes when applicable, and route the case for efficient processing without manual data correction

**Description:**

> As a **Customer Service Representative**,
> I want to **capture essential wellness visit information during event case initiation to establish the foundational claim record**,
> So that **the system can automatically classify the wellness event, prepopulate clinical codes when applicable, and route the case for efficient processing without manual data correction**


**Key Capabilities:**

> 1. User initiates wellness loss type selection within the case intake workflow.
> 2. User provides the wellness visit date to establish incident timing.
> 3. System validates temporal accuracy against event date and prevents future-dated entries.
>     3.1 Upon detection of date conflicts, system issues warnings while permitting workflow continuation for review.
> 4. When wellness represents the sole claim event, system automatically assigns standard preventive care clinical code and synchronizes diagnostic date.
> 5. System advances to subsequent intake stage upon successful validation completion.

---

### Epic: Claim Without Policy

#### Feature: Claim Without Policy
---

### Epic: Additional Parties

#### Feature: Add/Update new claim party
- **Role**: Customer Service Representative
- **Action**: manage parties and their roles throughout the event case intake process
- **Value**: all relevant parties are properly identified, associated with the case, and assigned appropriate claim roles to ensure accurate case processing and communication

**Description:**

> As a **Customer Service Representative**,
> I want to **manage parties and their roles throughout the event case intake process**,
> So that **all relevant parties are properly identified, associated with the case, and assigned appropriate claim roles to ensure accurate case processing and communication**.


**Key Capabilities:**

> 1. Search for existing parties in the system to avoid duplicate records
>     1.1 Upon party not found, initiate new party creation workflow
> 2. Add new parties to the case with appropriate business entity or vendor classification
> 3. Assign claim-specific roles to parties based on their involvement in the event
> 4. Update party contact information as case progresses
>     4.1 When party is vendor, use vendor-specific editing workflow
> 5. Manage payment methods separately from contact information
> 6. View comprehensive party details including vendor-specific attributes when applicable

---

#### Feature: Manage payment method for the party
- **Role**: Claim Adjuster
- **Action**: configure and maintain payment delivery methods for additional parties involved in an event case
- **Value**: payments are processed accurately and efficiently to the correct recipients through their preferred payment channels

**Description:**

> As a **Claim Adjuster**,
> I want to **configure and maintain payment delivery methods for additional parties involved in an event case**,
> So that **payments are processed accurately and efficiently to the correct recipients through their preferred payment channels**.


**Key Capabilities:**

> 1. User is able to access party management within an active event case context
> 2. User is able to identify and select the additional party requiring payment method configuration
> 3. User is able to specify payment delivery preferences including method type and routing details
>     3.1 Upon selecting electronic payment, system captures necessary banking information
>     3.2 Upon selecting paper check, system captures mailing address details
> 4. User is able to validate payment method information meets business and regulatory requirements
> 5. User is able to update or modify existing payment methods when party circumstances change
> 6. System associates payment method with party profile for future claim disbursements

---

### Epic: Applicability validation - automated claim creation

#### Feature: Applicability validation - automated claim creation
- **Role**: Claim Intaker
- **Action**: initiate an event case and trigger automated claim creation based on applicability validation rules
- **Value**: claims are systematically created when eligibility criteria are met, reducing manual effort and ensuring consistent processing

**Description:**

> As a **Claim Intaker**,
> I want to **initiate an event case and trigger automated claim creation based on applicability validation rules**,
> So that **claims are systematically created when eligibility criteria are met, reducing manual effort and ensuring consistent processing**


**Key Capabilities:**

> 1. User initiates a new event case by providing loss event information
> 2. System validates applicability criteria against policy rules and coverage conditions
>     2.1 When validation succeeds, system automatically creates associated claims
>     2.2 When validation fails, system prevents claim creation and flags ineligibility
> 3. User reviews generated claims linked to the event case
> 4. System records audit trail of validation outcomes and claim generation activities

---
## Initiative: Case Overview

### Epic: Case Header

#### Feature: Case Header Details
- **Role**: Case Manager
- **Action**: view, review, and update comprehensive event case information including case header details, member information, claim events, and diagnostic codes throughout the case lifecycle
- **Value**: I can maintain accurate case records, ensure timely event classification, coordinate multi-claim processing, and make informed decisions based on complete case context and member history

**Description:**

> As a **Case Manager**,
> I want to **view, review, and update comprehensive event case information including case header details, member information, claim events, and diagnostic codes throughout the case lifecycle**,
> So that **I can maintain accurate case records, ensure timely event classification, coordinate multi-claim processing, and make informed decisions based on complete case context and member history**


**Key Capabilities:**

> 1. User navigates to event case and views consolidated case header displaying case identification, status indicators, member and subject information with contextual access links, event and reporting dates, assigned case manager, and special handling flags
> 2. User accesses member and subject detailed information through interactive links to review demographics, employment details, work schedules, contact information, and dependent relationships
> 3. User reviews claim events section containing event type classifications, accident versus sickness determination, and diagnostic code records with primary indicators
> 4. User initiates case information modification for open cases and accesses event detail editing interface
>     4.1 Upon case closure, user accesses read-only view mode for historical reference
> 5. User updates claim event details including event type selections, diagnostic information, event-specific attributes, and associated ICD coding
> 6. System validates case information for duplicates, saves updates, triggers workflow to cascade changes to related claims, and creates new claims when applicable

---

#### Feature: Case Manager Assignment
- **Role**: Case Manager
- **Action**: assign or reassign event cases to qualified personnel or queues based on workload distribution and authority requirements
- **Value**: cases are routed efficiently to available, authorized resources, ensuring balanced workloads and timely case resolution

**Description:**

> As a **Case Manager**,
> I want to **assign or reassign event cases to qualified personnel or queues based on workload distribution and authority requirements**,
> So that **cases are routed efficiently to available, authorized resources, ensuring balanced workloads and timely case resolution**.


**Key Capabilities:**

> 1. Upon case intake completion, system automatically identifies eligible personnel based on claim authority, active status, and availability period.
> 2. System applies load balancing by evaluating active case counts and assigns to personnel with smallest workload, with queue fallback when no eligible users exist.
> 3. Authorized users access current case manager information including contact details and assignment history.
> 4. User initiates reassignment process by selecting individual personnel through organizational search or queue-based assignment.
> 5. System validates assignee eligibility, captures reassignment rationale, and updates case ownership across all related components.
> 6. When reassignment is cancelled mid-process, system prompts confirmation to prevent accidental data loss before reverting changes.

---

#### Feature: Special Handling
- **Role**: Case Manager
- **Action**: configure and maintain special handling classifications for event cases to ensure appropriate processing protocols and escalation workflows are applied
- **Value**: cases requiring specialized attention are properly identified, tracked, and processed according to designated protocols, reducing risk exposure and ensuring compliance with organizational policies

**Description:**

> As a **Case Manager**,
> I want to **configure and maintain special handling classifications for event cases to ensure appropriate processing protocols and escalation workflows are applied**,
> So that **cases requiring specialized attention are properly identified, tracked, and processed according to designated protocols, reducing risk exposure and ensuring compliance with organizational policies**


**Key Capabilities:**

> 1. Case Manager accesses case overview and reviews current special handling status indicators
> 2. Upon identifying need for special designation, Case Manager initiates special handling classification workflow
>     2.1 When case involves fraud suspicion, legal representation, or litigation, system applies appropriate investigative protocols
>     2.2 If priority handling required, system configures expedited review timelines
> 3. System validates user privileges and case status before allowing special handling modifications
> 4. Case Manager documents justification and supporting details for special handling designation
> 5. System updates case routing, notification rules, and processing workflows based on applied classifications
> 6. Special handling indicators remain visible and hyperlinked throughout case lifecycle for stakeholder transparency

---

#### Feature: Case closing reasons
- **Role**: Case Manager
- **Action**: designate and record the business reason for closing an event case
- **Value**: closure decisions are documented with proper justification for audit compliance and business intelligence reporting

**Description:**

> As a **Case Manager**,
> I want to **designate and record the business reason for closing an event case**,
> So that **closure decisions are documented with proper justification for audit compliance and business intelligence reporting**.


**Key Capabilities:**

> 1. User accesses the case header section to initiate case closure workflow
> 2. System presents predefined business closure reason categories aligned with organizational taxonomy
> 3. User selects the appropriate closure reason that reflects the business outcome
> 4. System validates closure reason selection against case status and business rules
>     4.1 If prerequisites are unmet, system prevents closure and prompts corrective action
> 5. System records closure reason with timestamp and user attribution for audit trail
> 6. Upon successful closure, system updates case status and triggers downstream reporting processes

---

### Epic: Case Actions ("I want to")

#### Feature: Update Case Information
- **Role**: Claim Adjuster
- **Action**: modify case-level details and associated claim events to maintain accurate records and support appropriate claim adjudication
- **Value**: the system reflects current circumstances, ensures compliance with reporting requirements, and enables accurate downstream claim processing decisions

**Description:**

> As a **Claim Adjuster**,
> I want to **modify case-level details and associated claim events to maintain accurate records and support appropriate claim adjudication**,
> So that **the system reflects current circumstances, ensures compliance with reporting requirements, and enables accurate downstream claim processing decisions**.


**Key Capabilities:**

> 1. User accesses existing case records and initiates modification of case and claim event information
> 2. User updates case-level details including reporting method, event timing, event description, and employment information
> 3. User manages loss types by adding new claim events while preserving previously recorded losses
>     3.1 When user selects new loss types, system displays loss-specific information sections
>     3.2 Upon adding loss types, system maintains previously selected losses as non-removable
> 4. User maintains ICD code associations relevant to medical claim events
> 5. User submits consolidated changes for system validation and processing
> 6. System validates data integrity, triggers claim creation workflows, performs duplicate detection, and updates case records across integrated systems

---

#### Feature: Add Related Case
- **Role**: Case Manager
- **Action**: link related event cases to track dependencies and shared contexts
- **Value**: I can manage interconnected cases holistically, improve investigative efficiency, and ensure consistent handling across related events

**Description:**

> As a **Case Manager**,
> I want to **link related event cases to track dependencies and shared contexts**,
> So that **I can manage interconnected cases holistically, improve investigative efficiency, and ensure consistent handling across related events**


**Key Capabilities:**

> 1. User initiates case relationship establishment from source case overview
> 2. User identifies target case through search capabilities with filtering options
>     2.1 Upon entering search criteria, system provides suggested matches with key identifiers
>     2.2 User can refine results using advanced filters when initial matches exceed threshold
> 3. User selects target case and specifies relationship classification and business justification
> 4. Upon submission, system establishes bidirectional relationship with validation checks
>     4.1 System prevents self-referencing and duplicate relationship configurations
> 5. User can modify relationship classifications or remove associations when business context changes
> 6. System maintains comprehensive audit trail of all relationship lifecycle events across linked cases

---

#### Feature: Create a new Claim manually
- **Role**: Claim Intaker
- **Action**: manually create a new claim from an existing case
- **Value**: I can establish a claim record linked to the case for subsequent adjudication and processing

**Description:**

> As a **Claim Intaker**,
> I want to **manually create a new claim from an existing case**,
> So that **I can establish a claim record linked to the case for subsequent adjudication and processing**


**Key Capabilities:**

> 1. User accesses the case overview and initiates claim creation workflow
> 2. User provides core loss information including parties, coverage, and incident details
> 3. System validates claim eligibility against policy terms and case context
> 4. System establishes claim record with unique identifier and associates it to the parent case
> 5. System confirms successful claim creation and makes it available for adjudication
>     5.1 If validation fails, system prevents claim creation and provides guidance
> 6. User transitions to claim management workspace for continued processing

---

### Epic: Case Lifecycle: Status / Substatus

#### Feature: Case Lifecycle: Status / Substatus
- **Role**: Case Manager
- **Action**: manage the complete lifecycle of an event case from initiation through closure and potential reopening
- **Value**: ensure all related claims are properly processed, validated, and closed with appropriate business controls while maintaining data integrity and regulatory compliance

**Description:**

> As a **Case Manager**,
> I want to **manage the complete lifecycle of an event case from initiation through closure and potential reopening**,
> So that **ensure all related claims are properly processed, validated, and closed with appropriate business controls while maintaining data integrity and regulatory compliance**


**Key Capabilities:**

> 1. Initiate event case with incomplete status and complete required business data
> 2. Submit case for validation and applicability evaluation, transitioning to open status
>     2.1 Upon validation, system automatically retrieves policies and initiates applicable claims
>     2.2 System aggregates claim types across coverages and triggers data transformations
> 3. Monitor linked claims processing while maintaining case oversight
> 4. Execute case closure after reviewing open items including active tasks, unclosed claims, unpaid coverages, incomplete payments, unposted recurring payments, and unprocessed balances
>     4.1 When hard-stop items exist (incomplete payments or premium waiver periods), system prevents closure until resolved
> 5. Select closure reason with business rule enforcement based on payment and coverage status
> 6. Reopen closed cases when business needs require resuming processing activities

---

### Epic: Case Duplication Validation

#### Feature: Case Duplication Validation
- **Role**: Case Manager
- **Action**: review potential duplicate cases and override false-positive duplication warnings when appropriate
- **Value**: I can ensure accurate case management by preventing duplicate case creation while maintaining flexibility to proceed with legitimate cases that are flagged as potential duplicates

**Description:**

> As a **Case Manager**,
> I want to **review potential duplicate cases and override false-positive duplication warnings when appropriate**,
> So that **I can ensure accurate case management by preventing duplicate case creation while maintaining flexibility to proceed with legitimate cases that are flagged as potential duplicates**


**Key Capabilities:**

> 1. System validates case intake against existing cases and triggers duplicate warning when threshold scores are exceeded
> 2. User accesses duplication details to review flagged cases with scoring breakdown based on matching criteria (subject of claim, diagnosis codes, incident characteristics)
> 3. User investigates potential duplicates by navigating to related case records and customer portfolios for comprehensive comparison
> 4. User exercises override authority with documented justification when determining flagged cases are not duplicates
>     4.1 Upon override, system records authorization reason and removes duplication warnings
>     4.2 If cancelled, duplication warning persists for continued monitoring
> 5. System prevents override without proper authorization privileges and mandatory justification documentation

---

### Epic: Claim Events

#### Feature: View/ Edit
- **Role**: Claim Adjuster
- **Action**: view, modify, and add claim event information to ensure accurate case documentation and trigger appropriate downstream claim processing
- **Value**: comprehensive event records drive automated claim creation, maintain data integrity across multiple claim types, and enable informed adjudication decisions

**Description:**

> As a **Claim Adjuster**,
> I want to **view, modify, and add claim event information to ensure accurate case documentation and trigger appropriate downstream claim processing**,
> So that **comprehensive event records drive automated claim creation, maintain data integrity across multiple claim types, and enable informed adjudication decisions**.


**Key Capabilities:**

> 1. User accesses existing claim event details including event classifications, injury/sickness designations, and diagnostic records.
> 2. User initiates event modification process to update established event attributes and add new loss types to the case.
> 3. System validates event changes against duplicate case and claim detection rules to prevent fraudulent submissions.
> 4. User submits consolidated event updates triggering automated API integration with customer and case management systems.
> 5. System cascades event modifications to existing Life, Critical Illness, and Hospital Indemnity claims while generating new Accident claims when applicable.
>     5.1 Upon case closure, user accesses read-only event details without modification capabilities.
>     5.2 When subject is non-employee, system restricts absence-related event selection.
> 6. User verifies updated event information reflects accurately across case overview and related claim records.

---

### Epic: Other Claims

#### Feature: Claim Quick View
- **Role**: Case Manager
- **Action**: access and navigate through all claims associated with a life insurance case to monitor claim status and assignments across multiple loss types
- **Value**: I can efficiently oversee the complete claims landscape for a case, identify related claims requiring attention, and maintain comprehensive case management across different coverage types

**Description:**

> As a **Case Manager**,
> I want to **access and navigate through all claims associated with a life insurance case to monitor claim status and assignments across multiple loss types**,
> So that **I can efficiently oversee the complete claims landscape for a case, identify related claims requiring attention, and maintain comprehensive case management across different coverage types**


**Key Capabilities:**

> 1. User accesses the case overview to retrieve all associated claims across coverage types
> 2. System presents claim portfolio organized by claim type with key identifiers, loss benefit details, subject information, and current status
> 3. User toggles between card-based claim view and loss-type organized view based on analysis needs
>     3.1 Card view groups by individual claim instances
>     3.2 Loss view aggregates by loss type categories
> 4. User identifies claims requiring attention through status indicators and assignment information
> 5. User selects specific claim for detailed investigation
> 6. System navigates to selected claim's full overview workspace

---

#### Feature: Loss View
- **Role**: Claim Adjuster
- **Action**: review and analyze all coverages associated with specific loss types within an event case to assess claim exposure and identify patterns
- **Value**: I can efficiently evaluate the full scope of coverage exposure across multiple claims stemming from the same loss event, enabling faster adjudication and better case management decisions

**Description:**

> As a **Claim Adjuster**,
> I want to **review and analyze all coverages associated with specific loss types within an event case to assess claim exposure and identify patterns**,
> So that **I can efficiently evaluate the full scope of coverage exposure across multiple claims stemming from the same loss event, enabling faster adjudication and better case management decisions**.


**Key Capabilities:**

> 1. User switches perspective from individual claim view to loss-centric view to analyze all related coverages
> 2. System organizes and presents coverages grouped by loss type (Death, Serious Illness, Hospital Services, Dismemberment, Waiver of Premium) with visibility into item counts
> 3. User selects a loss type category to examine associated coverages across all claims in the case
> 4. System displays coverage details including claim identifiers, eligibility status, diagnostic codes, incident dates, service periods, and financial exposure with accumulator limits
> 5. When reviewing Premium Waiver coverages, user accesses benefit period details including elimination periods, approval history, and remaining duration
> 6. User navigates to detailed claim information for further investigation when needed

---

### Epic: Change History

#### Feature: Change History
- **Role**: Case Manager
- **Action**: access and review historical changes made to event cases and claims to track modifications and maintain audit trails
- **Value**: I can monitor case evolution, ensure accountability, support compliance requirements, and make informed decisions based on complete change history

**Description:**

> As a **Case Manager**,
> I want to **access and review historical changes made to event cases and claims to track modifications and maintain audit trails**,
> So that **I can monitor case evolution, ensure accountability, support compliance requirements, and make informed decisions based on complete change history**


**Key Capabilities:**

> 1. User is able to access change history from event case and claim interfaces
> 2. User is able to search historical modifications using business-relevant criteria
> 3. User is able to preview change records showing what was modified, when, and by whom
> 4. System tracks all material changes to event cases and associated claims
> 5. System presents change information in chronological sequence for audit purposes

---
## Initiative: Claim Overview

### Epic: Claim Header

#### Feature: Claim Header Details
- **Role**: Claim Adjuster
- **Action**: view and manage comprehensive claim header information including status, policy details, subject information, and special handling indicators
- **Value**: I can quickly assess claim context, monitor key business indicators, and apply appropriate case handling flags to ensure proper adjudication and compliance

**Description:**

> As a **Claim Adjuster**,
> I want to **view and manage comprehensive claim header information including status, policy details, subject information, and special handling indicators**,
> So that **I can quickly assess claim context, monitor key business indicators, and apply appropriate case handling flags to ensure proper adjudication and compliance**


**Key Capabilities:**

> 1. System displays consolidated claim header with status, subject identity, loss dates, policy references, payment status, and assigned resources
> 2. User is able to access detailed subject information including contact data retrieved from customer management system
> 3. System retrieves billing information and alerts user when paid-to-date falls behind loss occurrence date
> 4. User is able to navigate to related policy and member records for comprehensive context review
> 5. User is able to configure special handling flags for regulatory, legal, or investigative scenarios including litigation, appeals, subrogation, and fraud indicators
> 6. Upon saving special handling changes, system persists selections and displays active flags in header for ongoing visibility

---

#### Feature: Claim Manager Assignement
- **Role**: Claim Manager
- **Action**: assign and reassign claims to appropriate personnel or queues based on workload, authority, and availability
- **Value**: claims are distributed efficiently across the team, ensuring timely handling and optimal resource utilization while maintaining proper oversight

**Description:**

> As a **Claim Manager**,
> I want to **assign and reassign claims to appropriate personnel or queues based on workload, authority, and availability**,
> So that **claims are distributed efficiently across the team, ensuring timely handling and optimal resource utilization while maintaining proper oversight**.


**Key Capabilities:**

> 1. Upon claim creation completion, system automatically evaluates available personnel using authority verification, active status confirmation, and availability period checks
>     1.1 When no qualified personnel exist, system assigns to default management queue
>     1.2 When multiple qualified personnel exist, system applies load balancing based on active claim counts
> 2. System presents current claim manager information with reassignment capability through accessible interface
> 3. User is able to reassign claims to alternative personnel or queues when claim status permits modification
> 4. System validates reassignment eligibility by evaluating claim status, preventing changes to closed claims unless reopened
> 5. User is able to search and select assignees using flexible criteria, with system filtering based on security permissions and organizational roles
> 6. Upon successful assignment, system updates claim ownership across all integrated components including task management and workflow engines

---

### Epic: Special Handling

#### Feature: Special Handling
- **Role**: Claim Adjuster
- **Action**: configure and track special handling status flags for claims requiring elevated attention or specialized processing
- **Value**: claims with unique circumstances (litigation, appeals, fraud investigation) receive appropriate oversight and comply with regulatory and organizational protocols

**Description:**

> As a **Claim Adjuster**,
> I want to **configure and track special handling status flags for claims requiring elevated attention or specialized processing**,
> So that **claims with unique circumstances (litigation, appeals, fraud investigation) receive appropriate oversight and comply with regulatory and organizational protocols**


**Key Capabilities:**

> 1. User accesses claim overview and initiates special handling configuration
> 2. System presents available handling categories (fraud investigation, appeal, complaint, litigation, attorney involvement, policy considerations)
> 3. User designates applicable special handling indicators based on claim circumstances
>     3.1 Upon manual activation, system applies status flag to claim record
>     3.2 System validates user authorization for special handling modifications
> 4. System persists indicator selections and displays active flags on claim header
> 5. User reviews consolidated special handling status across claim lifecycle
> 6. System provides visibility of all active special handling conditions for reporting and escalation purposes

---

### Epic: Fraud check / Duplicate Claim check

#### Feature: Fraud check / Duplicate Claim check
---

### Epic: Beneficiaries

#### Feature: View / Add / Edit Beneficiary details
- **Role**: Claim Adjuster
- **Action**: manage beneficiaries and their coverage allocations throughout the life claim lifecycle
- **Value**: accurate benefit distribution is ensured according to policy terms and regulatory requirements while maintaining payment integrity

**Description:**

> As a **Claim Adjuster**,
> I want to **manage beneficiaries and their coverage allocations throughout the life claim lifecycle**,
> So that **accurate benefit distribution is ensured according to policy terms and regulatory requirements while maintaining payment integrity**


**Key Capabilities:**

> 1. Upon accessing claim overview, system auto-populates policy beneficiaries with designation warnings for incomplete coverage assignments
> 2. User is able to designate new beneficiaries with coverage selections and allocation percentages, triggering automatic amount calculations
>     2.1 When claim subject is a dependent, system defaults beneficiary to member at 100% allocation
>     2.2 When beneficiary requires support, user assigns guardian with independent payment routing
> 3. User is able to modify beneficiary allocations and payment details for pending designations
> 4. System validates total allocation percentages per beneficiary type and coverage do not exceed 100%
> 5. System prevents modification or removal of beneficiaries with executed payment schedules
> 6. Upon guardian assignment, system pre-fills payment details and enables separate payment routing per beneficiary-guardian relationship

---

### Epic: no content

#### Feature: ICD codes
- **Role**: Claim Adjuster
- **Action**: manage diagnostic codes on claims through addition, editing, and removal operations while maintaining data integrity and validation compliance
- **Value**: accurate medical diagnosis tracking supports proper claim adjudication, regulatory compliance, and audit readiness throughout the claim lifecycle

**Description:**

> As a **Claim Adjuster**,
> I want to **manage diagnostic codes on claims through addition, editing, and removal operations while maintaining data integrity and validation compliance**,
> So that **accurate medical diagnosis tracking supports proper claim adjudication, regulatory compliance, and audit readiness throughout the claim lifecycle**


**Key Capabilities:**

> 1. Upon claim initiation, system defaults diagnosis codes and accident/sickness classification from Event Case as one-time unidirectional copy
> 2. User is able to add new diagnosis codes by searching available codes, designating primary status, and recording diagnosis date
> 3. User is able to modify existing diagnosis codes including code selection, primary designation, and diagnosis date
>     3.1 System prevents changes to primary codes when multiple codes exist to maintain data integrity
>     3.2 System validates uniqueness and enforces single primary designation
> 4. User is able to remove diagnosis codes with system confirmation and validation enforcement
> 5. System validates all operations ensuring code uniqueness, single primary designation, minimum one primary code, and past/present dates only
> 6. When validation fails, system prevents data persistence and displays contextual error guidance

---

### Epic: Claim Actions ("I want to")

#### Feature: Policy Refresh
- **Role**: Claim Adjuster
- **Action**: refresh claim calculations when policy updates occur after loss date
- **Value**: the claim reflects accurate policy terms, eligibility, and benefit amounts based on the latest policy version, ensuring proper adjudication and payment accuracy

**Description:**

> As a **Claim Adjuster**,
> I want to **refresh claim calculations when policy updates occur after loss date**,
> So that **the claim reflects accurate policy terms, eligibility, and benefit amounts based on the latest policy version, ensuring proper adjudication and payment accuracy**.


**Key Capabilities:**

> 1. User initiates policy refresh for pending or open claims based on loss date
> 2. System validates availability of new policy version and presents comparison summary for review
> 3. Upon confirmation, system re-integrates claim with updated policy data
> 4. System re-evaluates eligibility rules based on modified waiting periods or incurral conditions
> 5. System recalculates gross benefit amounts, accumulators, and reschedules payments accordingly
>     5.1 When coverage is removed, system marks previous coverage as non-eligible
>     5.2 When benefit amounts or maximums change, system updates accumulator balances
> 6. System generates payment balance adjustments while preserving manual overrides

---

#### Feature: Change Claim Sub-status
- **Role**: Claim Adjuster
- **Action**: update the claim sub-status to reflect the current stage of claim processing
- **Value**: I can accurately track and communicate the claim's detailed processing state while maintaining workflow transparency

**Description:**

> As a **Claim Adjuster**,
> I want to **update the claim sub-status to reflect the current stage of claim processing**,
> So that **I can accurately track and communicate the claim's detailed processing state while maintaining workflow transparency**


**Key Capabilities:**

> 1. User accesses claim sub-status modification capability from the claim overview
> 2. System validates claim eligibility based on current main status
>     2.1 When status is Pending, system offers sub-statuses: Additional POL, Policy Information, Future Claim
>     2.2 When status is Open, system offers sub-statuses: Internal Review, SIU, Payment Scheduled
>     2.3 If status is Closed, system prevents sub-status modification
> 3. User selects appropriate sub-status value aligned with claim processing stage
> 4. User confirms the sub-status change to persist updates
> 5. Upon cancellation, system discards changes without affecting current sub-status
> 6. System records sub-status transition in claim record

---

#### Feature: Claim Closure
- **Role**: Claim Adjuster
- **Action**: finalize and close a claim after all adjudication activities are complete
- **Value**: the claim lifecycle is properly concluded, case records are updated, and operational capacity is freed for new work

**Description:**

> As a **Claim Adjuster**,
> I want to **finalize and close a claim after all adjudication activities are complete**,
> So that **the claim lifecycle is properly concluded, case records are updated, and operational capacity is freed for new work**.


**Key Capabilities:**

> 1. System validates closure request and verifies adjuster authorization
> 2. System confirms claim status transition eligibility according to lifecycle rules
> 3. Upon validation success, system updates claim status to Closed
> 4. System triggers business activity monitoring for closure event
> 5. System completes associated case and task records in work management
>     5.1 If status transition is invalid, system prevents closure and notifies adjuster
> 6. System returns updated claim record confirming closure

---

#### Feature: Claim Automatic Closure (Auto-adjudication)
- **Role**: Claim Adjuster
- **Action**: enable automatic closure of eligible claims and event cases upon payment completion
- **Value**: processing efficiency is improved, manual closure tasks are eliminated, and resources are redirected to complex cases requiring judgment

**Description:**

> As a **Claim Adjuster**,
> I want to **enable automatic closure of eligible claims and event cases upon payment completion**,
> So that **processing efficiency is improved, manual closure tasks are eliminated, and resources are redirected to complex cases requiring judgment**.


**Key Capabilities:**

> 1. Upon payment schedule completion, system initiates auto-closure evaluation process.
> 2. System validates auto-closure eligibility by verifying claim status, coverage approval states, and auto-adjudication completion.
> 3. System confirms closure readiness by checking payment issuance, payee balance reconciliation, task completion, and automated process finalization.
> 4. System closes all eligible claims meeting both eligibility and readiness criteria.
> 5. System evaluates event case for closure when all associated claims reach closed state.
>     5.1 If closure conditions unmet, system generates exception task for manual review.
>     5.2 Event case remains open until all claims satisfy closure requirements.

---

### Epic: Claim Lifecycle

#### Feature: Claim Lifecycle
- **Role**: Claim Adjuster
- **Action**: manage the complete lifecycle of a claim from submission through closure
- **Value**: I can efficiently process claims through all required stages, maintain accurate status tracking, and ensure timely resolution

**Description:**

> As a **Claim Adjuster**,
> I want to **manage the complete lifecycle of a claim from submission through closure**,
> So that **I can efficiently process claims through all required stages, maintain accurate status tracking, and ensure timely resolution**


**Key Capabilities:**

> 1. User is able to initiate claim submission to begin the adjudication process
> 2. User is able to transition claim status through lifecycle stages (submit, close, reopen)
> 3. User is able to update claim substatus to reflect detailed processing milestones
> 4. User is able to generate required claim documentation throughout the process
> 5. User is able to synchronize policy information to validate coverage eligibility
> 6. Upon status change, system records audit trail and enforces business rules

---

### Epic: Policy Summary

#### Feature: Policy Summary
- **Role**: Claim Adjuster
- **Action**: access comprehensive policy information within the claim context to understand coverage scope, insured parties, exclusions, and limitations
- **Value**: I can make informed claim decisions by having immediate visibility into all relevant policy terms and conditions that govern the claim

**Description:**

> As a **Claim Adjuster**,
> I want to **access comprehensive policy information within the claim context to understand coverage scope, insured parties, exclusions, and limitations**,
> So that **I can make informed claim decisions by having immediate visibility into all relevant policy terms and conditions that govern the claim**


**Key Capabilities:**

> 1. User accesses claim overview to initiate claim assessment activities
> 2. System retrieves and presents associated policy information for the claim under review
> 3. User reviews policy coverage details to determine claim eligibility
> 4. User examines insured parties to validate claimant relationship
> 5. User evaluates exclusions and limitations to identify coverage restrictions
> 6. User leverages complete policy context to support adjudication decisions

---

### Epic: Reserving

#### Feature: Reserving
---
## Initiative: Claim Adjudication Benefit Calculations

### Epic: Face Values

#### Feature: Face Values
- **Role**: Claim Adjuster
- **Action**: review, validate, and manage face value calculations across life and accident claims with override capabilities
- **Value**: accurate benefit determinations are made with flexibility to adjust calculations based on policy terms, age reductions, and claim-specific circumstances

**Description:**

> As a **Claim Adjuster**,
> I want to **review, validate, and manage face value calculations across life and accident claims with override capabilities**,
> So that **accurate benefit determinations are made with flexibility to adjust calculations based on policy terms, age reductions, and claim-specific circumstances**.


**Key Capabilities:**

> 1. System retrieves policy financial data and calculates face value based on benefit type (single value, multiple of salary, percentage), applying age reduction schedules when member's age at date of loss meets policy thresholds
>     1.1 When annual covered earnings unavailable for salary-based calculations, system prompts adjuster to enter required data before enabling override
>     1.2 When benefit amount unavailable for spouse/child claims, system requests member's face value for percentage-based calculation
> 2. Adjuster reviews calculated face value with age reduction indicators and benefit type details displayed on product-specific cards
> 3. Upon determination that calculation requires adjustment, adjuster overrides face value with justified amount, system flags override and preserves original calculated value
> 4. System prevents recalculation of overridden values during policy updates or case cascades while maintaining age reduction flag accuracy
> 5. Adjuster reverses override when business conditions change, system restores pre-override calculated value and removes override indicators
> 6. System triggers benefit recalculation when underlying coverage gross amounts change due to updated earnings or policy modifications

---

#### Feature: Face Values (IPL)
- **Role**: Claim Adjuster
- **Action**: evaluate and calculate face value benefits with age reduction considerations for whole life and variable universal life claims
- **Value**: accurate benefit determinations are made automatically based on policy terms, member age, and loss type to ensure proper claim settlements

**Description:**

> As a **Claim Adjuster**,
> I want to **evaluate and calculate face value benefits with age reduction considerations for whole life and variable universal life claims**,
> So that **accurate benefit determinations are made automatically based on policy terms, member age, and loss type to ensure proper claim settlements**.


**Key Capabilities:**

> 1. Upon claim intake completion, system retrieves face value financial data from policy system and displays benefit calculations
> 2. System calculates member age based on date of loss and applies age reduction schedule from policy terms
>     2.1 When age reduction applies, system displays reduction indicator with original face value reference
>     2.2 When no reduction applies, system proceeds without adjustment flags
> 3. System determines benefit type from policy configuration (face plus cash value, maximum of face or cash, face only)
> 4. When loss type is accelerated death, system integrates cash management data at settlement adjudication
> 5. System recalculates face values when coverage gross amount is overridden or modified
> 6. User is able to view calculated face values without manual intervention for standard death claims on member subjects

---

#### Feature: Age Reduction
- **Role**: Claim Adjuster
- **Action**: apply age-based face value reductions during claim adjudication across multiple product lines
- **Value**: benefit amounts are accurately calculated according to policy terms and regulatory requirements, ensuring correct claim payments

**Description:**

> As a **Claim Adjuster**,
> I want to **apply age-based face value reductions during claim adjudication across multiple product lines**,
> So that **benefit amounts are accurately calculated according to policy terms and regulatory requirements, ensuring correct claim payments**.


**Key Capabilities:**

> 1. System retrieves insured's age and applicable face value from policy at time of claim
> 2. System identifies product line and routes to appropriate benefit calculation rules
> 3. System applies product-specific age reduction schedules to determine adjusted face value
>     3.1 Upon Term Life claim, system applies GTL age reduction tables
>     3.2 Upon Critical Illness claim, system applies CI-specific calculations
>     3.3 Upon Individual Permanent Life claim, system applies IWL reduction factors
>     3.4 Upon Accident claim, system calculates accidental death benefit amounts
> 4. System displays calculated face value on claim overview for adjudicator review
> 5. Adjuster is able to validate calculation accuracy before finalizing claim decision

---

### Epic: Accumulators

#### Feature: Configure Accumulators
- **Role**: Claim Adjuster
- **Action**: configure and manage accumulator-based benefit calculation rules throughout the claim lifecycle to ensure accurate payment limits and tracking
- **Value**: benefit payments comply with policy terms, prevent overpayments, and maintain accurate financial reserves across individual and group coverage scenarios

**Description:**

> As a **Claim Adjuster**,
> I want to **configure and manage accumulator-based benefit calculation rules throughout the claim lifecycle to ensure accurate payment limits and tracking**,
> So that **benefit payments comply with policy terms, prevent overpayments, and maintain accurate financial reserves across individual and group coverage scenarios**.


**Key Capabilities:**

> 1. System generates accumulator instances upon coverage creation, initializing maximum limits from policy terms or defaults based on product type and coverage scope.
> 2. System calculates payable amounts using minimum threshold logic (calculated amount, remaining coverage limit, group remaining) and reserves amounts when settlement approved.
>     2.1 Upon coverage marked non-eligible or cancelled, system returns reserved amounts to available limits.
> 3. System transitions reserved amounts to used status upon successful payment issuance and tracks complete audit trail.
>     3.1 When payment declined, voided, or stopped, system recovers used amounts back to reserved status.
>     3.2 Upon payment cancellation, system clears reservations and restores full remaining limits.
> 4. System adjusts limits and recalculates reserves when face values overridden, maintaining negative balances internally while displaying compliant values.
> 5. System dynamically recalculates group limits for fracture/dislocation scenarios, filtering cancelled settlements from aggregate calculations.
> 6. System provides real-time visibility into limit status (maximum, reserved, used, remaining) at coverage addition and modification milestones.

---

#### Feature: View accumulator remaining
- **Role**: Claim Adjuster
- **Action**: view remaining policy limit information for a coverage to assess available benefit capacity
- **Value**: I can make informed adjudication decisions based on current limit utilization and availability

**Description:**

> As a **Claim Adjuster**,
> I want to **view remaining policy limit information for a coverage to assess available benefit capacity**,
> So that **I can make informed adjudication decisions based on current limit utilization and availability**


**Key Capabilities:**

> 1. User accesses accumulator summary for a specific coverage under adjudication
> 2. System retrieves lifetime individual limit parameters including total authorized amount and measurement basis
> 3. System calculates and presents current utilization metrics
>     3.1 Upon multiple settlements exist, system aggregates successfully paid amounts
>     3.2 When pending settlements exist, system includes reserved amounts
> 4. System displays remaining capacity calculated from authorized limit minus planned and used amounts
> 5. User evaluates available benefit capacity to determine settlement feasibility
> 6. When coverage involves bundled benefits, system presents combined limit impact across related benefit types

---

#### Feature: Accumulator Transaction History
- **Role**: Claim Adjuster
- **Action**: review accumulator transaction history across claim coverages to understand benefit utilization patterns and validate claim adjudication accuracy
- **Value**: I can ensure benefit calculations align with policy terms, identify discrepancies in accumulator processing, and make informed adjudication decisions based on historical benefit usage

**Description:**

> As a **Claim Adjuster**,
> I want to **review accumulator transaction history across claim coverages to understand benefit utilization patterns and validate claim adjudication accuracy**,
> So that **I can ensure benefit calculations align with policy terms, identify discrepancies in accumulator processing, and make informed adjudication decisions based on historical benefit usage**


**Key Capabilities:**

> 1. User accesses accumulator transaction history from claim coverage overview for the subject of claim
> 2. System retrieves and displays transaction records filtered by policy and claim subject, excluding technical system entries
> 3. System organizes transactions by accumulator type (single vs. group) with chronological sorting from latest to earliest
> 4. When accumulators span multiple benefit or calendar years, system segments history into separate year-specific views
> 5. User reviews transaction details including dates, associated cases/claims, descriptions, amounts, units, and applicable extension periods
> 6. User sorts and navigates paginated transaction records to analyze benefit utilization patterns and validate calculation accuracy

---
## Initiative: Claim Adjudication

### Epic: Claim level Adjudication

#### Feature: Override non-eligible claim
- **Role**: Claim Adjuster
- **Action**: override system-determined claim ineligibility to proceed with claim processing
- **Value**: legitimate claims can be processed despite automated eligibility validation failures, ensuring customer service and reducing claim processing delays

**Description:**

> As a **Claim Adjuster**,
> I want to **override system-determined claim ineligibility to proceed with claim processing**,
> So that **legitimate claims can be processed despite automated eligibility validation failures, ensuring customer service and reducing claim processing delays**.


**Key Capabilities:**

> 1. System executes automated claim eligibility validation upon claim submission
> 2. Upon eligibility validation failure, system marks claim as non-eligible and restricts standard processing workflows
> 3. User identifies non-eligible claim through system indicators on claim overview
> 4. User reviews eligibility failure reasons and supporting claim documentation
> 5. When business justification exists, user invokes override functionality to bypass eligibility restriction
> 6. System records override action with authorization details and proceeds with claim adjudication workflow

---

#### Feature: Claim Eligibility
- **Role**: Claim Adjuster
- **Action**: validate claim and coverage eligibility through automated multi-tier business rule evaluation
- **Value**: claims are accurately assessed for eligibility at both claim and settlement levels, preventing ineligible payouts while enabling efficient manual override when business judgment is required

**Description:**

> As a **Claim Adjuster**,
> I want to **validate claim and coverage eligibility through automated multi-tier business rule evaluation**,
> So that **claims are accurately assessed for eligibility at both claim and settlement levels, preventing ineligible payouts while enabling efficient manual override when business judgment is required**


**Key Capabilities:**

> 1. System executes claim-level eligibility validation upon claim creation or update, evaluating waiting periods, insured relationships, policy status, coverage availability, duplicate detection, and event type matching
> 2. Upon successful claim-level validation, system performs settlement-level adjudication for each coverage, applying common rules (claim cascade, policy refresh validation, duplicate coverage detection, date range validation)
> 3. System applies coverage-specific business logic including benefit waiting periods, incurral periods, separation periods, parent-child coverage dependencies, and recurrence benefit validation
> 4. When validation failures occur, system categorizes severity and displays corresponding messages with rule identifiers (C###, CS###, S###)
> 5. User is able to manually override non-blocking eligibility results when authorized, documenting business justification
> 6. Upon policy refresh or plan updates, system re-adjudicates existing settlements to ensure continued eligibility under modified terms

---
## Initiative: Coverage Adjudication

### Epic: Coverages

#### Feature: Coverage Adjudication flow (HI)
- **Role**: Claim Adjuster
- **Action**: adjudicate policy coverage eligibility and determine applicable benefits for submitted health insurance claims
- **Value**: I can ensure accurate coverage determination, prevent improper payments, and expedite legitimate claim settlements while maintaining regulatory compliance

**Description:**

> As a **Claim Adjuster**, I want to **adjudicate policy coverage eligibility and determine applicable benefits for submitted health insurance claims**, so that **I can ensure accurate coverage determination, prevent improper payments, and expedite legitimate claim settlements while maintaining regulatory compliance**.


**Key Capabilities:**

> 1. User initiates coverage adjudication for the health insurance claim requiring benefit determination
> 2. System evaluates policy status, effective dates, and member eligibility at time of service
> 3. User reviews applicable coverage provisions, exclusions, and benefit limitations
> 4. System applies coordination of benefits rules when multiple coverages exist
>     4.1 Upon primary coverage exhaustion, secondary coverage is evaluated
> 5. User determines coverage decision with supporting rationale
> 6. System records adjudication outcome and proceeds to payment calculation or denial processing

---

#### Feature: Coverage Eligibility
- **Role**: Claim Adjuster
- **Action**: evaluate member eligibility for coverage based on policy waiting periods and employment status
- **Value**: I can ensure claims are processed only for eligible members, reducing improper payments and ensuring policy compliance

**Description:**

> As a **Claim Adjuster**,
> I want to **evaluate member eligibility for coverage based on policy waiting periods and employment status**,
> So that **I can ensure claims are processed only for eligible members, reducing improper payments and ensuring policy compliance**


**Key Capabilities:**

> 1. System classifies member as new or existing employee by comparing hire date against policy effective date for the applicable policy type
> 2. System retrieves waiting period configuration parameters including calculation method, duration amount, and time unit based on employee classification
> 3. System calculates eligibility date by applying the configured waiting period rule to the hire date
>     3.1 When no waiting period applies, eligibility begins at hire date
>     3.2 When amount-based periods apply, system adds duration to hire date with optional month-boundary adjustments
> 4. System validates loss date occurs on or after the calculated eligibility date (exclusive)
> 5. System determines member eligibility status and communicates result for adjudication decisioning

---

#### Feature: Configure new and change existing coverages
---

#### Feature: Coverage List
- **Role**: Claim Adjuster
- **Action**: adjudicate and manage coverages on claims through automated evaluation and manual oversight
- **Value**: accurate benefit calculations are achieved, policy limits are enforced, and claim settlements are processed efficiently with audit controls

**Description:**

> As a **Claim Adjuster**,
> I want to **adjudicate and manage coverages on claims through automated evaluation and manual oversight**,
> So that **accurate benefit calculations are achieved, policy limits are enforced, and claim settlements are processed efficiently with audit controls**


**Key Capabilities:**

> 1. User initiates coverage selection process filtered by policy terms, loss types, and insured relationships
> 2. System executes automated adjudication via rules engine, validating eligibility, calculating gross amounts, and initializing benefit accumulators
> 3. Upon adjudication failure or data incompleteness, user reviews and corrects coverage attributes (incident dates, service periods, diagnosis codes) in edit mode
>     3.1 System enforces date range logic and recalculates benefit units in real-time
>     3.2 System validates overrides against remaining limits when privileged user adjusts gross amounts or benefit units
> 4. System maintains accumulator balances across benefit/calendar years, generating new periods when coverage spans multiple cycles
> 5. User cancels coverage when eligibility conditions change, with system preventing cancellation if payments issued or dependencies exist
> 6. User views comprehensive coverage status including paid amounts, remaining limits, and calculation formulas through detailed information panels

---

#### Feature: Coverages - Add
- **Role**: Claim Adjuster
- **Action**: associate additional policy coverages to an in-progress claim
- **Value**: I can accurately expand the claim scope to reflect all applicable coverages from the underlying policy, enabling proper adjudication and payment processing

**Description:**

> As a **Claim Adjuster**,
> I want to **associate additional policy coverages to an in-progress claim**,
> So that **I can accurately expand the claim scope to reflect all applicable coverages from the underlying policy, enabling proper adjudication and payment processing**


**Key Capabilities:**

> 1. Adjuster accesses existing claim and reviews currently associated coverages
> 2. Adjuster initiates coverage addition process to view available policy coverages not yet associated
> 3. System presents selectable policy coverages based on policy configuration and product line rules
> 4. Adjuster selects one or multiple applicable coverages for association
> 5. System validates coverage eligibility and adds selected coverages to the claim
> 6. System auto-calculates initial coverage attributes (gross amounts, limits, date ranges) per product-specific configuration
>     6.1 Upon calculation completion, system displays override indicators where manual adjustments are permitted
>     6.2 When configuration requires, system enforces mandatory fields per product line

---

#### Feature: Coverages - Override/Edit
- **Role**: Claim Adjuster
- **Action**: review system-adjudicated settlement eligibility results and override determinations when business judgment warrants deviation from automated validation
- **Value**: I can ensure claims are appropriately settled based on comprehensive evaluation that balances automated rule validation with case-specific circumstances requiring professional discretion

**Description:**

> As a **Claim Adjuster**,
> I want to **review system-adjudicated settlement eligibility results and override determinations when business judgment warrants deviation from automated validation**,
> So that **I can ensure claims are appropriately settled based on comprehensive evaluation that balances automated rule validation with case-specific circumstances requiring professional discretion**


**Key Capabilities:**

> 1. Review automated settlement eligibility determinations with detailed validation failure explanations across all coverage lines within claim context
> 2. Access override functionality to reverse system-adjudicated eligibility results when authorized by privilege controls
> 3. Apply override decision that toggles eligibility status and suspends automatic re-validation to preserve adjudicator determination
>     3.1 Upon override activation, system prevents subsequent automatic eligibility re-checks when case information updates
>     3.2 System maintains override indicator distinguishing manual determinations from automated results
> 4. Modify underlying claim parameters to trigger fresh automated eligibility validation as alternative to override
> 5. Remove override status to restore automatic validation behavior and obtain current rule-based eligibility determination
> 6. Track override history with persistent visual indicators distinguishing manual adjudication from system-generated results

---

#### Feature: Coverage auto-creation for Death (TL/ACC)
- **Role**: Claim Adjuster
- **Action**: enable automatic creation and activation of death coverage for Term Life and Accidental Death policies during claim adjudication
- **Value**: claims are processed efficiently with accurate coverage applicability, reducing manual effort and ensuring consistent adjudication outcomes

**Description:**

> As a **Claim Adjuster**,
> I want to **enable automatic creation and activation of death coverage for Term Life and Accidental Death policies during claim adjudication**,
> So that **claims are processed efficiently with accurate coverage applicability, reducing manual effort and ensuring consistent adjudication outcomes**.


**Key Capabilities:**

> 1. System identifies claim type as death-related during intake or assignment
> 2. System automatically retrieves applicable policy provisions for Term Life or Accidental Death coverage
> 3. System validates policy active status and coverage effective dates against loss occurrence
> 4. System creates coverage records and links to the claim adjudication workflow
>     4.1 If policy conditions are not met, system flags for manual review
> 5. System activates coverage for financial evaluation and benefit calculation
> 6. User is able to review auto-created coverage determinations and override if business rules require adjustment

---

#### Feature: Coverage auto-creation for HI (HI)
- **Role**: Claim Adjuster
- **Action**: automatically establish applicable coverage lines during claim adjudication without manual intervention
- **Value**: claim processing efficiency improves and coverage assessment accuracy increases from the outset of adjudication

**Description:**

> As a **Claim Adjuster**,
> I want to **automatically establish applicable coverage lines during claim adjudication without manual intervention**,
> So that **claim processing efficiency improves and coverage assessment accuracy increases from the outset of adjudication**


**Key Capabilities:**

> 1. System retrieves active homeowners insurance policy details upon claim initiation
> 2. System analyzes loss characteristics and automatically matches applicable coverage types from the policy
> 3. System generates coverage line entries for adjudication without manual input
> 4. System applies policy terms, limits, and deductibles to each created coverage line
>     4.1 When multiple coverage types apply, system creates all relevant lines simultaneously
> 5. System notifies adjuster of coverage framework establishment for damage evaluation
> 6. System maintains audit trail of auto-created coverage decisions for compliance review

---

#### Feature: Coverage Duplication Check
- **Role**: Claim Adjuster
- **Action**: validate and prevent duplicate coverages during claim adjudication
- **Value**: ensure accurate claim settlement by eliminating redundant coverage processing and maintaining data integrity

**Description:**

> As a **Claim Adjuster**,
> I want to **validate and prevent duplicate coverages during claim adjudication**,
> So that **I can ensure accurate claim settlement by eliminating redundant coverage processing and maintaining data integrity**


**Key Capabilities:**

> 1. System initiates adjudication or re-adjudication process for open claims
> 2. System validates coverage uniqueness based on policy number, case number, coverage name, and incident details
>     2.1 Upon detecting special coverage types (Coma, Anesthesia, Child benefits), system applies coverage-specific duplication criteria
>     2.2 System excludes incomplete or previously non-eligible coverages from validation
> 3. When duplication is detected, system marks coverage as non-eligible and prevents updates
> 4. When validation passes, system confirms coverage eligibility and enables processing
> 5. System enforces overlap period rules treating adjacent date ranges as duplicates

---

#### Feature: Cancel/Undo Cancel Coverage
- **Role**: Claim Adjuster
- **Action**: cancel or restore coverage status while managing associated financial reserves, payments, and eligibility determinations
- **Value**: accurate financial accounting is maintained, policy limits are properly managed, and coverage decisions can be reversed when business circumstances require adjustment

**Description:**

> As a **Claim Adjuster**,
> I want to **cancel or restore coverage status while managing associated financial reserves, payments, and eligibility determinations**,
> So that **accurate financial accounting is maintained, policy limits are properly managed, and coverage decisions can be reversed when business circumstances require adjustment**.


**Key Capabilities:**

> 1. User is able to initiate coverage cancellation by recording business justification and setting cancellation indicators
> 2. Upon cancellation, system releases reserved amounts from applicable accumulators and adjusts remaining limits based on payment status
> 3. When payments exist, system manages payment record visibility and generates overpayment balances for issued payments while locking coverage from further adjudication
> 4. User is able to reverse cancellation by clearing indicators and triggering settlement re-adjudication
> 5. Upon restoration, system re-reserves accumulator amounts and restores payment visibility based on payment issuance status
> 6. If payments were issued prior to cancellation, system clears overpayment balances without recreating payment records

---

### Epic: Benefit Calculations : Life Products

#### Feature: Death Benefit calculations
- **Role**: Claim Adjuster
- **Action**: calculate the gross settlement amount for death benefit claims using policy coverage limits and accumulator balances
- **Value**: accurate benefit payments are determined within policy limits and regulatory compliance is maintained while preventing overpayment

**Description:**

> As a **Claim Adjuster**,
> I want to **calculate the gross settlement amount for death benefit claims using policy coverage limits and accumulator balances**,
> So that **accurate benefit payments are determined within policy limits and regulatory compliance is maintained while preventing overpayment**


**Key Capabilities:**

> 1. System verifies whether gross amount requires manual override or automatic calculation
> 2. System retrieves policy contract data including face value and benefit amounts from the policy system
> 3. System calculates remaining accumulator balances at both coverage and group levels following predefined accumulation rules
> 4. System determines gross settlement amount using minimum of face amount and calculated remaining amount
>     4.1 Upon override indicator, system applies override value and bypasses calculation
>     4.2 When unit override exists, system uses specified units without recalculation
> 5. System applies configured formula specific to settlement type and coverage combination
> 6. System records calculation results and source data for audit and reconciliation purposes

---

#### Feature: Accelerated Death Benefit calculations
- **Role**: Claim Adjuster
- **Action**: adjudicate accelerated death benefit claim settlement amounts using policy limits, accumulator constraints, and configured calculation formulas
- **Value**: ensure accurate benefit payments that comply with policy face value limits, accumulator thresholds, and regulatory requirements while supporting manual override capabilities for exceptional circumstances

**Description:**

> As a **Claim Adjuster**,
> I want to **adjudicate accelerated death benefit claim settlement amounts using policy limits, accumulator constraints, and configured calculation formulas**,
> So that **I can ensure accurate benefit payments that comply with policy face value limits, accumulator thresholds, and regulatory requirements while supporting manual override capabilities for exceptional circumstances**.


**Key Capabilities:**

> 1. System evaluates manual override indicator and applies override amount directly when flagged, bypassing automated calculation
> 2. System retrieves policy face value, benefit amount, and settlement data from policy records
> 3. System calculates accumulator remaining amounts considering settlement usage, coverage limits, and group accumulator constraints
> 4. System applies coverage-specific formula using minimum of face amount and remaining accumulator balance
>     4.1 When unit override indicator is disabled, system constrains units to minimum of requested units and remaining amount
>     4.2 When unit override indicator is enabled, system uses override unit value without accumulator constraint
> 5. System persists calculated gross amount to settlement record

---

#### Feature: View calculation formula
- **Role**: Claim Adjuster
- **Action**: review the calculation methodology and computed benefit amounts for life insurance coverage
- **Value**: I can verify the accuracy of benefit calculations, understand the formula logic applied, and ensure transparency in adjudication decisions

**Description:**

> As a **Claim Adjuster**,
> I want to **review the calculation methodology and computed benefit amounts for life insurance coverage**,
> So that **I can verify the accuracy of benefit calculations, understand the formula logic applied, and ensure transparency in adjudication decisions**


**Key Capabilities:**

> 1. User is able to access benefit calculation details for specific coverage during claim adjudication
> 2. System retrieves and displays the business formula logic configured for the coverage type
> 3. System presents the actual parameter values applied in the calculation
>     3.1 Upon parameter unavailability, system indicates missing data
>     3.2 When values are negative, system applies floor adjustment
> 4. System computes and displays the final benefit amount with appropriate formatting
> 5. When coverage involves multiple periods, system presents year-by-year calculations
> 6. When coverage involves recurring payments, system displays per-frequency benefit amounts

---

### Epic: Special Coverage Process

#### Feature: Process Recurrence Benefits
- **Role**: Claim Adjuster
- **Action**: adjudicate and manage recurrence benefits by distinguishing initial diagnosis from recurring coverage instances while enforcing separation periods and incident date sequencing
- **Value**: I ensure accurate benefit calculation, prevent duplicate payments, and maintain compliance with policy recurrence rules and temporal eligibility requirements

**Description:**

> As a **Claim Adjuster**,
> I want to **adjudicate and manage recurrence benefits by distinguishing initial diagnosis from recurring coverage instances while enforcing separation periods and incident date sequencing**,
> So that **I ensure accurate benefit calculation, prevent duplicate payments, and maintain compliance with policy recurrence rules and temporal eligibility requirements**


**Key Capabilities:**

> 1. User initiates coverage addition process and selects eligible coverages filtered by active policy information
> 2. System executes auto-adjudication upon coverage selection and calculates gross amount based on benefit type (initial diagnosis vs recurrence percentage)
> 3. User provides incident date to establish coverage instance timeline
>     3.1 Upon first instance, system designates as initial diagnosis and disables recurrence classification
>     3.2 When subsequent instances added, system validates incident date against separation period threshold
> 4. System enforces temporal sequencing rules preventing initial diagnosis dates from occurring after recurring benefit dates
> 5. User manages recurrence classification changes, triggering benefit recalculation when initial diagnosis status is modified
> 6. System marks coverage as non-eligible when separation period validation fails or incident date sequencing violations occur

---

#### Feature: Process Special Coverages (ACC)
- **Role**: Claim Adjuster
- **Action**: manage accident special coverage eligibility and financial allocation for covered incidents
- **Value**: accurate coverage determination and appropriate benefit allocation are ensured while maintaining compliance with policy terms and temporal constraints

**Description:**

> As a **Claim Adjuster**,
> I want to **manage accident special coverage eligibility and financial allocation for covered incidents**,
> So that **accurate coverage determination and appropriate benefit allocation are ensured while maintaining compliance with policy terms and temporal constraints**


**Key Capabilities:**

> 1. User accesses claim overview to review existing accident special coverage entries with associated parties, date ranges, financial allocations, and eligibility determinations
> 2. User initiates new coverage record creation by identifying the affected party and establishing treatment period boundaries
> 3. System validates temporal constraints ensuring coverage period commences after loss occurrence date
> 4. Upon successful validation, system persists coverage entry with comprehensive details including party identification, incident dates, occurrence counts, financial limits, and payment tracking
> 5. User monitors financial allocation displaying gross amounts, paid benefits, and remaining limits for ongoing coverage management
> 6. System prevents incomplete submissions when required party identification or temporal information is missing

---
## Initiative: Waiver of Premium

### Epic: Waiver of Premium

#### Feature: Premium Waiver Process: Claims
- **Role**: Claim Adjuster
- **Action**: manage premium waiver periods and approvals throughout the claim lifecycle
- **Value**: the insured's coverage eligibility is accurately tracked and premium obligations are appropriately waived during qualifying disability periods

**Description:**

> As a **Claim Adjuster**,
> I want to **manage premium waiver periods and approvals throughout the claim lifecycle**,
> So that **the insured's coverage eligibility is accurately tracked and premium obligations are appropriately waived during qualifying disability periods**.


**Key Capabilities:**

> 1. Assess premium waiver coverage details including elimination, benefit, and approval period status
> 2. Update elimination period information when qualifying disability thresholds are met
>     2.1 Validate period meets contractual requirements before confirmation
> 3. Update benefit period parameters as claim circumstances evolve
> 4. Establish new approval periods when continued waiver eligibility is determined
>     4.1 System calculates reserved units per accumulator rules upon approval
> 5. Transition approval periods to completed status when benefit period concludes
>     5.1 System recalculates completed units and restricts further period modifications
> 6. Review accumulated waiver units to ensure policy limits are respected

---

#### Feature: Premium Waiver Process: related Policy impact
---

#### Feature: Premium Waiver Process: related Billing impact
- **Role**: Claim Adjuster
- **Action**: process and approve premium waiver claims for disabled policyholders and coordinate billing adjustments
- **Value**: policyholders can maintain insurance coverage during disability periods without premium payment obligations while ensuring accurate billing reconciliation

**Description:**

> As a **Claim Adjuster**,
> I want to **process and approve premium waiver claims for disabled policyholders and coordinate billing adjustments**,
> So that **policyholders can maintain insurance coverage during disability periods without premium payment obligations while ensuring accurate billing reconciliation**


**Key Capabilities:**

> 1. User initiates premium waiver claim and validates policy payment status against loss dates to confirm coverage eligibility
> 2. User investigates disability evidence and determines waiver qualification based on policyholder medical condition
> 3. User approves premium waiver for designated approval periods with defined start and end dates
> 4. Upon approval period completion, system transmits waiver period data to billing subsystem for premium correction processing
> 5. Billing system receives approval data and executes appropriate premium waivers or refunds for the approved timeframe
> 6. System maintains audit trail of waiver approvals and billing adjustments for compliance reporting

---
## Initiative: Manage Claim Payment

### Epic: Create Payment Action

#### Feature: Payment Frequency/Scheduling
- **Role**: Claim Adjuster
- **Action**: create and schedule payment allocations with automated calculation of net payment amounts based on approved benefits, frequencies, reductions, and business rules
- **Value**: payments are accurately calculated, scheduled according to approved benefit periods and payment frequencies, and automatically approved within authority limits to ensure timely and compliant benefit disbursement

**Description:**

> As a **Claim Adjuster**,
> I want to **create and schedule payment allocations with automated calculation of net payment amounts based on approved benefits, frequencies, reductions, and business rules**,
> So that **payments are accurately calculated, scheduled according to approved benefit periods and payment frequencies, and automatically approved within authority limits to ensure timely and compliant benefit disbursement**.


**Key Capabilities:**

> 1. User initiates payment creation by adding payment allocations for selected payee, specifying allocation type, coverage/benefit, and period details; system validates claim eligibility, status, and prevents duplicates
> 2. System executes calculation dry run preview including adjusted gross benefit amount, prorations, interest, and all reductions (offsets, deductions, taxes)
> 3. Upon confirmation, system creates or updates payment schedule by combining allocations, deactivating prior schedules if necessary, and cancelling conflicting approved payments
> 4. System applies complex scheduling rules to split approved benefit periods by payment frequency and calculates payment dates based on occurrence type
> 5. System attempts automatic approval based on user authority limits; if authorized, schedule becomes active with payments pending post; otherwise, approval required
> 6. User previews combined payment schedule across all payees with calculated net amounts and statuses

---

#### Feature: Payment Details
- **Role**: Claim Adjuster
- **Action**: create or update payment schedules with allocations based on claim settlements and beneficiary entitlements
- **Value**: ensure accurate financial disbursement to appropriate parties while maintaining compliance with policy coverage terms and preventing duplicate payments

**Description:**

> As a **Claim Adjuster**,
> I want to **create or update payment schedules with allocations based on claim settlements and beneficiary entitlements**,
> So that **ensure accurate financial disbursement to appropriate parties while maintaining compliance with policy coverage terms and preventing duplicate payments**.


**Key Capabilities:**

> 1. User initiates payment creation from case overview and provides payee identification with optional guardian relationships
> 2. User selects allocation strategy (Indemnity, Expense, or Ex Gratia) and associates eligible claims based on payee role filtering
>     2.1 When Indemnity selected, system retrieves eligible coverages and settlement data via product-specific APIs
>     2.2 When guardian acts on behalf of minor, system filters coverages based on beneficiary relationship
> 3. User defines allocation periods for recurring payments and selects interest-only options where applicable
> 4. System validates payment method compatibility and checks for duplicate allocations using product-specific rules (coverage combinations for Life products; allocation period overlaps for Disability)
> 5. Upon successful validation, system generates payment schedule with calculated amounts and transitions to allocation detail review
> 6. User finalizes or updates payment allocations with post-date adjustments (create mode only) before submission

---

#### Feature: Payment Allocation Details
- **Role**: Claim Adjuster
- **Action**: review and adjust payment allocation distributions across claims, coverages, and payees to ensure accurate benefit calculations before creating payments
- **Value**: payments are accurately allocated with correct interest, deductions, offsets, and beneficiary distributions, ensuring compliance with policy terms and regulatory requirements while preventing duplicate or overlapping payment periods

**Description:**

> As a **Claim Adjuster**,
> I want to **review and adjust payment allocation distributions across claims, coverages, and payees to ensure accurate benefit calculations before creating payments**,
> So that **payments are accurately allocated with correct interest, deductions, offsets, and beneficiary distributions, ensuring compliance with policy terms and regulatory requirements while preventing duplicate or overlapping payment periods**


**Key Capabilities:**

> 1. User reviews system-generated payment allocations aggregated by post date with coverage and payee breakdowns
> 2. User validates incident details, benefit periods, and pre-filled allocation parameters inherited from claim intake
> 3. User modifies adjustable calculation parameters including interest dates, interest calculation amounts, payment frequencies for recurring benefits, and applies manual interest overrides when justified
>     3.1 Upon parameter modification, system requires recalculation to regenerate payment schedule with updated net amounts and validation results
> 4. System validates allocation integrity by detecting duplicate allocations and overlapping benefit periods for same claim and coverage combinations
> 5. User finalizes allocation review and proceeds to payment creation when all validations pass and calculations are current
> 6. System automatically distributes gross amounts proportionally across beneficiary payees based on designated percentages

---

#### Feature: Configure EOB Remarks
- **Role**: Claim Adjuster
- **Action**: configure Explanation of Benefits (EOB) remarks during payment processing to document payment rationale and adjustments
- **Value**: beneficiaries receive clear explanations for payment calculations and adjustments, ensuring transparency and regulatory compliance

**Description:**

> As a **Claim Adjuster**,
> I want to **configure Explanation of Benefits (EOB) remarks during payment processing to document payment rationale and adjustments**,
> So that **beneficiaries receive clear explanations for payment calculations and adjustments, ensuring transparency and regulatory compliance**


**Key Capabilities:**

> 1. System auto-generates EOB remarks via business rules during claim processing for standard scenarios (age reductions, face value overrides, wellness payments)
> 2. User selects applicable manual EOB codes when updating payments to explain adjustments (guardian payments, salary adjustments, benefit overrides)
> 3. Upon selecting 'Other' EOB code, user provides custom remarks text to document unique payment scenarios
> 4. System associates EOB remarks to specific allocations based on payment context (coverage type, payee relationship, benefit adjustments)
> 5. When guardian is payee with beneficiary designation, system applies appropriate EOB code documenting the guardian payment relationship
> 6. System validates EOB remark completeness before allowing payment submission or update

---

#### Feature: Allocation Type: Indemnity, Expense, Ex Gratia
- **Role**: Claim Adjuster
- **Action**: review and validate payment allocation details across coverage types and reserve categories to ensure accurate distribution of claim payments
- **Value**: payment amounts are correctly allocated according to policy terms, benefit calculations, and regulatory requirements before final disbursement

**Description:**

> As a **Claim Adjuster**,
> I want to **review and validate payment allocation details across coverage types and reserve categories to ensure accurate distribution of claim payments**,
> So that **payment amounts are correctly allocated according to policy terms, benefit calculations, and regulatory requirements before final disbursement**.


**Key Capabilities:**

> 1. User reviews aggregated allocation summary showing total amounts grouped by scheduled disbursement dates and detailed breakdowns by claim and coverage type.
> 2. User examines allocation details specific to payment category (life/critical illness/health, disability, expense, or ex gratia) including benefit calculations, previously paid amounts, remaining limits, and net payment values.
> 3. Upon identifying premium paid-to-date gaps or calculation discrepancies, user receives system alerts and warnings to address coverage eligibility concerns.
> 4. User modifies editable allocation components such as interest calculation parameters, allocation periods for recurring payments, and payment frequency settings when business conditions warrant adjustments.
> 5. When changes are applied, system recalculates all dependent allocation values, validates for duplicate or overlapping allocation periods, and updates net payment amounts accordingly.
> 6. User confirms allocation accuracy and proceeds to payment execution once all validations pass and calculations reconcile to expected benefit amounts.

---

#### Feature: Payment Frequency
- **Role**: Claim Adjuster
- **Action**: create and manage recurring payment schedules with automated generation and issuance capabilities
- **Value**: eligible claimants receive timely, accurate payments without manual intervention for each installment, reducing processing time and ensuring consistent payment delivery

**Description:**

> As a **Claim Adjuster**,
> I want to **create and manage recurring payment schedules with automated generation and issuance capabilities**,
> So that **eligible claimants receive timely, accurate payments without manual intervention for each installment, reducing processing time and ensuring consistent payment delivery**.


**Key Capabilities:**

> 1. User initiates payment schedule creation from claim overview, triggering automated schedule build process.
> 2. System deactivates existing active schedules and cancels unapproved payments to prevent duplicates within the same payment level.
> 3. Payment scheduler converts financial data into calculated payment installments based on adjudicated coverage and frequency rules.
>     3.1 Upon scheduling errors, system creates intervention task and halts process.
>     3.2 Upon activation failure, system creates review task for manual assessment.
> 4. System initializes and activates payment schedule, determining if immediate issuance or future processing is required.
> 5. Automated jobs generate pending payments to approved status, then issue payments when valid payment methods exist.
> 6. User is able to monitor payment status transitions and initiate stop payment or void actions when business conditions require intervention.

---

#### Feature: Addition & Reductions
- **Role**: Claim Adjuster
- **Action**: create and manage payment additions and reductions to ensure accurate claim settlement amounts
- **Value**: the final payment reflects all authorized adjustments, deductions, and additional compensation, ensuring accurate and compliant disbursement

**Description:**

> As a **Claim Adjuster**,
> I want to **create and manage payment additions and reductions to ensure accurate claim settlement amounts**,
> So that **the final payment reflects all authorized adjustments, deductions, and additional compensation, ensuring accurate and compliant disbursement**


**Key Capabilities:**

> 1. User is able to initiate payment adjustment action within an active claim payment workflow
> 2. User is able to specify adjustment type as addition or reduction with business justification
>     2.1 Upon selecting addition, user provides supplementary cost categories
>     2.2 Upon selecting reduction, user identifies deduction reasons such as deductibles or recoveries
> 3. User is able to define adjustment amounts and associate supporting documentation
> 4. System validates adjustment against policy limits and claim reserves
> 5. User is able to review cumulative impact of all adjustments on net payment amount
> 6. System records adjustment history for audit and approval workflows

---

#### Feature: Dividends
---

#### Feature: FICA
- **Role**: Claim Adjuster
- **Action**: configure FICA tax exemption status and ensure accurate payroll tax calculations for claim payments
- **Value**: claim payments comply with federal tax regulations while accommodating legitimate exemptions, reducing tax calculation errors and regulatory risk

**Description:**

> As a **Claim Adjuster**,
> I want to **configure FICA tax exemption status and ensure accurate payroll tax calculations for claim payments**,
> So that **claim payments comply with federal tax regulations while accommodating legitimate exemptions, reducing tax calculation errors and regulatory risk**.


**Key Capabilities:**

> 1. System applies FICA Social Security tax at 6.2% until calendar year earnings reach annual threshold, then exempts further earnings from this component
> 2. System applies Medicare tax at 1.45% base rate, escalating to additional 0.9% when earnings exceed $200,000 threshold
> 3. User configures exemption indicators for individual claimants based on qualifying criteria
>     3.1 When exemption status is updated, system recalculates all past and future payments in payment schedule
>     3.2 For specific product configurations, system applies default exemption settings
> 4. System validates exemption changes and triggers comprehensive payment recalculation upon confirmation
> 5. User reviews tax summary displaying exemption status alongside taxable wages and withheld amounts across tax categories

---

#### Feature: Interest
- **Role**: Claim Adjuster
- **Action**: calculate state-compliant interest on payment allocations and apply appropriate interest additions
- **Value**: payments comply with state-specific interest regulations, beneficiaries receive accurate interest entitlements, and the organization mitigates regulatory non-compliance risks

**Description:**

> As a **Claim Adjuster**,
> I want to **calculate state-compliant interest on payment allocations and apply appropriate interest additions**,
> So that **payments comply with state-specific interest regulations, beneficiaries receive accurate interest entitlements, and the organization mitigates regulatory non-compliance risks**


**Key Capabilities:**

> 1. System determines applicable interest jurisdiction based on state override codes, loss type classification, and beneficiary location
> 2. System retrieves state-specific interest configuration including rates, thresholds, calculation methods, and reference date types
> 3. System calculates interest amounts using appropriate formulas based on annual/monthly and compound/simple flags
>     3.1 Upon threshold validation, system applies amount and time thresholds to determine eligibility
>     3.2 When multiple states apply, system selects jurisdiction yielding highest interest amount
> 4. System generates interest addition records with calculation details and updates payment item amounts accordingly

---

### Epic: Payment List

#### Feature: Payment List
- **Role**: Claim Adjuster
- **Action**: view, monitor, and manage all claim payments including upcoming, posted, underpayments, and deductions throughout their lifecycle
- **Value**: I can track payment status, control payment schedules, approve underpayments, and take corrective actions to ensure accurate and timely disbursement to payees

**Description:**

> As a **Claim Adjuster**,
> I want to **view, monitor, and manage all claim payments including upcoming, posted, underpayments, and deductions throughout their lifecycle**,
> So that **I can track payment status, control payment schedules, approve underpayments, and take corrective actions to ensure accurate and timely disbursement to payees**


**Key Capabilities:**

> 1. **View Payment Inventory**: User is able to access comprehensive list of upcoming payments (post date beyond last generated), posted payments (single transactions already issued), underpayments, and deduction payments with status indicators
>     1.1 Upon accessing upcoming payments, system retrieves schedules with Open, Active, or Suspended status
>     1.2 Upon accessing posted payments, system retrieves transactions where post date has passed
> 2. **Review Payment Details**: User is able to expand payment records to view allocation breakdowns including indemnity, deductions, interest, offsets, taxes, and benefits explanations
> 3. **Manage Payment Schedules**: User is able to activate pending schedules, suspend or unsuspend active schedules, generate payments reaching post dates, update schedule parameters, or cancel entire schedules
> 4. **Control Payment Lifecycle**: User is able to approve or disapprove underpayments, request payment issuance, request payment stop, or void issued payments based on authority privileges
> 5. **Monitor Payment Status**: When payment status changes occur, system updates indicators including Pending Approval, Issued, Suspended, Failed, Cancelled, or Issue Requested

---

### Epic: Payment Lifecycle/Actions

#### Feature: Payment Lifecycle / Payment Actions
- **Role**: Claim Adjuster
- **Action**: manage and control payments through their complete lifecycle from creation to issuance or cancellation
- **Value**: payments are properly authorized, tracked, and processed according to business rules while maintaining ability to prevent erroneous payments

**Description:**

> As a **Claim Adjuster**,
> I want to **manage and control payments through their complete lifecycle from creation to issuance or cancellation**,
> So that **payments are properly authorized, tracked, and processed according to business rules while maintaining ability to prevent erroneous payments**


**Key Capabilities:**

> 1. User is able to create and submit payments for authorization on claim or event cases
> 2. Upon approval, user is able to request payment issuance which transmits information to Payment Hub
> 3. When payment progresses, system transitions through predefined states: Created → Approved → Issue Requested → Issued
>     3.1 If payment must not proceed, user cancels payment with documented reason
>     3.2 If issued payment must be stopped, user requests stop and system updates to Failed or Issued based on timing
> 4. User is able to perform bulk operations to generate, cancel, suspend, or unsuspend all payments on a case
> 5. User is able to establish recurring payment schedules with automated generation and issuance

---

### Epic: Payment Approval Flow

#### Feature: Payment Approval Flow
- **Role**: Claim Supervisor
- **Action**: review and approve payment schedules that exceed standard authority limits
- **Value**: payment amounts requiring elevated authorization are properly controlled and disbursed in compliance with financial governance policies

**Description:**

> As a **Claim Supervisor**,
> I want to **review and approve payment schedules that exceed standard authority limits**,
> So that **payment amounts requiring elevated authorization are properly controlled and disbursed in compliance with financial governance policies**


**Key Capabilities:**

> 1. System validates initial payment request against user's authority threshold and coverage type
> 2. Upon exceeding authority limit, system transitions payment schedule to pending approval status and notifies stakeholders
> 3. System prevents unauthorized approval attempts and displays specific authority deficiency messages
> 4. Authorized supervisor reviews pending payment schedule and validates business justification
> 5. Upon successful authorization, system activates payment schedule and initiates disbursement workflow
>     5.1 If payee payment method is invalid or missing, system cancels transaction
>     5.2 System records approval audit trail with approver credentials and timestamp

---

### Epic: Recovery Payment

#### Feature: Post Recovery action
- **Role**: Claim Adjuster
- **Action**: manage recovery payment lifecycle after receipt, including issuing, stopping, canceling, or handling failures
- **Value**: recoveries are properly processed through their lifecycle states, ensuring financial accuracy, audit compliance, and timely resolution of payment exceptions

**Description:**

> As a **Claim Adjuster**,
> I want to **manage recovery payment lifecycle after receipt, including issuing, stopping, canceling, or handling failures**,
> So that **recoveries are properly processed through their lifecycle states, ensuring financial accuracy, audit compliance, and timely resolution of payment exceptions**.


**Key Capabilities:**

> 1. User is able to approve recovery payment for issuance with system-generated unique transaction number
> 2. User is able to request payment issuance, triggering automated submission to payment hub for processing
> 3. Upon successful issuance, system transitions payment to issued state and evaluates schedule completion rules
> 4. When payment cannot be sent to payment hub, system automatically rolls back to approved state for remediation and resubmission
> 5. User is able to request stop-payment on issued recovery, with system handling approval or rejection responses from payment hub
> 6. User is able to cancel approved payments prior to issuance, preventing further processing actions

---
## Initiative: Manage Claim Balances

### Epic: Recalculation Triggers

#### Feature: Recalculation Flow
- **Role**: Claim Adjuster
- **Action**: automatically recalculate claim balances and reconcile settlements when claim or coverage information changes
- **Value**: payments remain accurate, overpayments and underpayments are identified and resolved, and accumulators reflect current claim status

**Description:**

> As a **Claim Adjuster**,
> I want to **automatically recalculate claim balances and reconcile settlements when claim or coverage information changes**,
> So that **payments remain accurate, overpayments and underpayments are identified and resolved, and accumulators reflect current claim status**


**Key Capabilities:**

> 1. Upon claim or coverage update, system validates existing settlement records against current plan eligibility and coverage continuity.
> 2. When settlement remains valid, system triggers readjudication, recalculates gross amounts, updates accumulator, and regenerates payment schedules with revised amounts.
> 3. When settlement becomes invalid due to coverage changes, system marks coverage non-eligible, disables editing, removes payment allocations from schedule, and reverses accumulator credits.
> 4. System evaluates existing payment status and generates balance transactions for issued/cleared payments, calculating overpayment or underpayment amounts.
> 5. User applies balance management actions including recovery posting, overpayment waiving, or underpayment payment, with appropriate accumulator impact per transaction type.
> 6. System applies clawback logic using FIFO rules to reverse previously credited accumulator amounts, tracking recovery and clearance steps separately.

---

#### Feature: Recalculation due class change
- **Role**: Claim Adjuster
- **Action**: trigger automatic recalculation of claim financial balances when coverage class changes occur
- **Value**: claim reserves, payments, and exposures accurately reflect updated coverage classification without manual intervention

**Description:**

> As a **Claim Adjuster**,
> I want to **trigger automatic recalculation of claim financial balances when coverage class changes occur**,
> So that **claim reserves, payments, and exposures accurately reflect updated coverage classification without manual intervention**.


**Key Capabilities:**

> 1. System detects coverage class modification event on active claim
> 2. System retrieves current claim financial balances and applicable coverage parameters
> 3. System applies recalculation logic based on new class coverage limits and reserve formulas
> 4. System updates reserve amounts, exposure values, and payment thresholds accordingly
>     4.1 When recalculation identifies overpayment, system flags for recovery review
>     4.2 When additional reserves required, system notifies adjuster for approval
> 5. System records recalculation audit trail with before/after values
> 6. System confirms updated balances available for claim processing

---

### Epic: Manage Balances

#### Feature: Balancing per Payee and claim
- **Role**: Claim Adjuster
- **Action**: manage payment discrepancies by calculating, reviewing, and resolving balances between scheduled and issued payments for each payee and claim
- **Value**: accurate financial reconciliation is maintained, overpayments and underpayments are systematically identified and resolved, and accumulator integrity is preserved throughout the claim lifecycle

**Description:**

> As a **Claim Adjuster**,
> I want to **manage payment discrepancies by calculating, reviewing, and resolving balances between scheduled and issued payments for each payee and claim**,
> So that **accurate financial reconciliation is maintained, overpayments and underpayments are systematically identified and resolved, and accumulator integrity is preserved throughout the claim lifecycle**.


**Key Capabilities:**

> 1. System automatically triggers balance recalculation when claim data, benefit details, or payment allocations change, comparing issued payments against scheduled payments per payee and claim.
> 2. User reviews calculated balance status: zero balance indicates reconciliation; positive balance identifies carrier debt (underpayment); negative balance identifies insured debt (overpayment).
> 3. Upon detecting overpayment, user selects resolution method: post recovery for immediate collection, waive overpayment to forgive carrier debt, reduce future payments through withholding, or record external overpayment from outside sources.
> 4. Upon detecting underpayment, user posts corrective payment which follows standard approval and issuance workflow while reverting accumulator amounts.
> 5. System maintains balance transaction history and automatically performs self-balancing to offset items, preserving accumulator accuracy throughout resolution lifecycle.
> 6. User monitors all balance-affecting activities and transaction status changes through consolidated balance review interface per selected payee.

---

#### Feature: Balance Activities / Recalculated Payments / Payment Withholdings
- **Role**: Claim Adjuster
- **Action**: review and manage payment balance information for payees associated with claims or event cases
- **Value**: I can monitor financial obligations, track payment distributions, and ensure accurate claim settlement reconciliation

**Description:**

> As a **Claim Adjuster**,
> I want to **review and manage payment balance information for payees associated with claims or event cases**,
> So that **I can monitor financial obligations, track payment distributions, and ensure accurate claim settlement reconciliation**


**Key Capabilities:**

> 1. System retrieves and displays payment balance information for payees linked to the selected claim or event case
> 2. User accesses consolidated balance and recalculation records within the payments context
> 3. Upon viewing balance details, user evaluates payment history and identifies discrepancies or pending adjustments
> 4. System maintains audit trail of balance recalculations and modifications
>     4.1 When recalculation occurs, system documents triggering event and resulting balance changes
> 5. User monitors withholding activities and outstanding payment obligations

---

### Epic: Taxes

#### Feature: Tax & Withholding Management
- **Role**: Claim Adjuster
- **Action**: manage tax withholdings and review comprehensive tax summaries within the claim lifecycle
- **Value**: accurate tax compliance is maintained, financial obligations are properly documented, and claim settlement calculations reflect correct tax withholding impacts

**Description:**

> As a **Claim Adjuster**,
> I want to **manage tax withholdings and review comprehensive tax summaries within the claim lifecycle**,
> So that **accurate tax compliance is maintained, financial obligations are properly documented, and claim settlement calculations reflect correct tax withholding impacts**


**Key Capabilities:**

> 1. Access taxes management interface within the claim context to initiate tax operations
> 2. Manage withholding entries by creating new withholding records or modifying existing entries with required tax withholding information
>     2.1 Upon adding withholding, system validates data completeness and updates withholding repository
>     2.2 Upon editing withholding, system preserves audit trail of modifications
> 3. Review consolidated tax summary displaying aggregated withholding impacts and calculated tax totals
> 4. System automatically recalculates tax summaries when withholding entries are added, modified, or removed
> 5. Validate withholding data integrity before finalizing claim financial settlement

---

#### Feature: Summary of Taxes
- **Role**: Claim Adjuster
- **Action**: manage and configure year-to-date earnings and tax exemption information for claims
- **Value**: ensure accurate tax reporting and regulatory compliance for claim-related payments

**Description:**

> As a **Claim Adjuster**,
> I want to **manage and configure year-to-date earnings and tax exemption information for claims**,
> So that **I can ensure accurate tax reporting and regulatory compliance for claim-related payments**.


**Key Capabilities:**

> 1. User is able to access year-to-date earnings management functionality within claim context
> 2. User is able to view existing earnings entries and associated tax information for the claim
> 3. User is able to add new year-to-date earnings records or modify existing entries
> 4. User is able to configure Federal Insurance Contributions Act exemption indicators
>     4.1 When tax exemption applies, user designates appropriate FICA exemption status
>     4.2 Upon exemption changes, system updates associated tax calculations
> 5. User is able to validate and save earnings and tax data for reporting purposes
> 6. Upon completion, system associates all tax information with the claim record

---

### Epic: Deductions

#### Feature: UI Display / Add Deduction
- **Role**: Claim Adjuster
- **Action**: configure and apply deductions to withhold benefit portions for third-party payment obligations
- **Value**: claimant financial obligations are systematically satisfied while ensuring accurate benefit disbursement and regulatory compliance

**Description:**

> As a **Claim Adjuster**,
> I want to **configure and apply deductions to withhold benefit portions for third-party payment obligations**,
> So that **claimant financial obligations are systematically satisfied while ensuring accurate benefit disbursement and regulatory compliance**.


**Key Capabilities:**

> 1. User establishes deduction record at event case level after case submission and links to existing claim
>     1.1 Upon claim type CI/HI/TL, system restricts to child support and wage garnishment with percentage-only calculation
> 2. System validates user privileges and claim existence before enabling deduction configuration
> 3. User defines deduction parameters including type, calculation method, and third-party recipient details
> 4. Upon payment creation, system automatically generates secondary deduction payment when type is child support or wage garnishment
> 5. System applies payment scheduler rules to calculate deduction amounts and establishes master-to-deduction payment relationships
> 6. System finalizes event case updates and generates business activity messages for downstream integration

---
## Initiative: Claim Party Management

### Epic: Party Information

#### Feature: View / Add Parties
- **Role**: Claim Adjuster
- **Action**: register and associate individuals or organizations as parties to a case
- **Value**: all relevant stakeholders are properly documented and linked to the case for comprehensive claim processing

**Description:**

> As a **Claim Adjuster**,
> I want to **register and associate individuals or organizations as parties to a case**,
> So that **all relevant stakeholders are properly documented and linked to the case for comprehensive claim processing**


**Key Capabilities:**

> 1. User initiates party registration by selecting entity type (individual or organization) for case association
> 2. User provides identity information, contact preferences, and address details based on party type
>     2.1 Upon specific case contexts, system enforces additional mandatory identity verification requirements
>     2.2 When geographic location selected, system applies jurisdiction-specific validation rules
> 3. System validates submitted information against business rules and data format requirements
> 4. System persists party record and establishes relationship with the case
> 5. Upon successful registration, system confirms party association and makes information available for case processing

---

#### Feature: Individual / Organization
- **Role**: Claim Adjuster
- **Action**: register and associate new parties (individuals or organizations) to a claim case with complete identity and contact information
- **Value**: the claim can be properly linked to all relevant stakeholders, enabling accurate case processing, communication, and settlement distribution

**Description:**

> As a **Claim Adjuster**,
> I want to **register and associate new parties (individuals or organizations) to a claim case with complete identity and contact information**,
> So that **the claim can be properly linked to all relevant stakeholders, enabling accurate case processing, communication, and settlement distribution**


**Key Capabilities:**

> 1. User initiates party registration by selecting party classification (individual or organizational entity)
> 2. User provides identity information appropriate to party type and role requirements
> 3. User establishes contact methodology and captures corresponding contact coordinates
> 4. User records location information with jurisdiction-specific validation applied automatically
> 5. Upon data completeness verification, system persists party record and establishes case association
>     5.1 When user abandons registration, system confirms intent before discarding changes
>     5.2 When party role requires additional attributes, system enforces conditional data capture

---

#### Feature: Vendor (Individual / Facility)
- **Role**: Claim Adjuster
- **Action**: identify, select, and assign vendor parties with service configurations and payment preferences to an event case
- **Value**: the appropriate service providers are engaged with correct payment arrangements to support claim resolution activities

**Description:**

> As a **Claim Adjuster**,
> I want to **identify, select, and assign vendor parties with service configurations and payment preferences to an event case**,
> So that **the appropriate service providers are engaged with correct payment arrangements to support claim resolution activities**


**Key Capabilities:**

> 1. User initiates vendor party assignment to an existing event case
> 2. System searches integrated provider network using business criteria including service specialization and geographic location
> 3. User reviews qualified vendor candidates with available service capabilities and contact information
> 4. User selects vendor and system retrieves validated electronic payment configurations
> 5. User confirms service type assignments and payment method preferences
> 6. System establishes vendor relationship to case with designated service scope and payment instructions

---
## Initiative: Integration

### Epic: Policy Integration

#### Feature: Policy Search
- **Role**: Claim Adjuster
- **Action**: integrate with the policy system to retrieve and validate policy information during claim lifecycle events
- **Value**: the system can automatically identify applicable policy coverage, adjudicate benefits, and ensure claim decisions are based on accurate policy data at the time of loss

**Description:**

> As a **Claim Adjuster**,
> I want to **integrate with the policy system to retrieve and validate policy information during claim lifecycle events**,
> So that **the system can automatically identify applicable policy coverage, adjudicate benefits, and ensure claim decisions are based on accurate policy data at the time of loss**


**Key Capabilities:**

> 1. System retrieves active policy image data from policy system based on event date, excluding archived versions
> 2. System locates applicable policy version using date of loss as reference point
>     2.1 Upon product type is CapAbsence or CapNonAbsence, system applies product-specific business rules
> 3. System determines insured relationship context based on claim type
>     3.1 When claim type is CWCP, relationship derives from insured role in claim party
>     3.2 When claim type is CWMP, relationship derives from customer entity management
> 4. System auto-adjudicates applicable coverages and benefits based on loss details and relationship hierarchy

---

### Epic: Customer Integration

#### Feature: Retrieve Customer data
- **Role**: Customer Service Representative
- **Action**: retrieve and integrate customer information from external systems into the claims platform
- **Value**: I can access accurate, up-to-date customer data to expedite claim processing and improve service quality

**Description:**

> As a **Customer Service Representative**, I want to **retrieve and integrate customer information from external systems into the claims platform**, so that **I can access accurate, up-to-date customer data to expedite claim processing and improve service quality**.


**Key Capabilities:**

> 1. User initiates customer data retrieval by providing customer identifier
> 2. System connects to external customer database or CRM system via integration interface
> 3. System validates data completeness and formats information according to claims platform standards
> 4. Upon successful retrieval, system populates customer profile with updated information
>     4.1 If customer not found, system prompts for manual entry or alternative search criteria
> 5. System logs integration transaction for audit and troubleshooting purposes
> 6. User verifies retrieved data accuracy before proceeding with claim activities

---

### Epic: Claim-Billing Integration

#### Feature: Integration for Premium Paid to Date
- **Role**: Claim Adjuster
- **Action**: validate premium payment status and process premium waiver approvals through integrated billing system coordination
- **Value**: claims are adjudicated only for paid coverages and premium payment obligations are appropriately waived for qualified disabled policyholders

**Description:**

> As a **Claim Adjuster**,
> I want to **validate premium payment status and process premium waiver approvals through integrated billing system coordination**,
> So that **claims are adjudicated only for paid coverages and premium payment obligations are appropriately waived for qualified disabled policyholders**


**Key Capabilities:**

> 1. Upon claim initiation, system retrieves policy payment status and paid-to-date information from billing subsystem
> 2. System validates coverage eligibility by comparing loss date against paid-to-date threshold
>     2.1 When policy status indicates cancellation or pending cancellation, system restricts benefit payment processing
> 3. User investigates disability evidence for premium waiver rider eligibility determination
> 4. User approves waiver coverage for defined time periods based on disability validation
> 5. Upon approval completion, system transmits waiver period data to billing subsystem for premium correction execution
> 6. System maintains audit trail of payment validations and waiver approvals throughout claim lifecycle

---

#### Feature: Key points of inbound/outbound integration
---

### Epic: Payment Hub Integration

#### Feature: Payment Hub Integration
- **Role**: Claim Adjuster
- **Action**: initiate and manage outbound payment processing through Payment Hub integration while monitoring payment lifecycle events and handling payment stop or cancellation requests
- **Value**: payments are successfully transferred from the claims system to the Payment Hub for processing with financial institutions, maintaining synchronized payment states and enabling timely payment control actions

**Description:**

> As a **Claim Adjuster**,
> I want to **initiate and manage outbound payment processing through Payment Hub integration while monitoring payment lifecycle events and handling payment stop or cancellation requests**,
> So that **payments are successfully transferred from the claims system to the Payment Hub for processing with financial institutions, maintaining synchronized payment states and enabling timely payment control actions**.


**Key Capabilities:**

> 1. User initiates payment issuance request after completing prerequisite payment scheduling or underpayment processes.
> 2. System collects required payment data including payment methods and generates outbound payment request with domain correlation ID for future synchronization.
> 3. System transmits outbound payment creation request to Payment Hub and confirms payment has transferred to independent Payment Hub lifecycle.
> 4. System continuously monitors Payment Hub events (Created, Canceled, Failed, Paid) to synchronize payment states between systems.
> 5. Upon user request to stop or cancel payment, system submits cancellation request to Payment Hub and awaits confirmation.
>     5.1 If Payment Hub reports payment already paid, system cancels stop request and notifies user of failure with payment-method-specific messaging.
>     5.2 If Payment Hub successfully cancels payment, system updates payment state and completes cancellation process.
> 6. System applies business rules to set appropriate failure messages based on payment method type (CHECK vs EFT) and failure reason.

---
## Initiative: No-touch flow

### Epic: No-touch flow

#### Feature: Wellness benefit
- **Role**: Claim Adjuster
- **Action**: automatically adjudicate and process wellness benefit claims through streamlined no-touch automation
- **Value**: claims are evaluated, approved, and paid without manual intervention, reducing processing time and operational costs while ensuring accurate benefit delivery

**Description:**

> As a **Claim Adjuster**,
> I want to **automatically adjudicate and process wellness benefit claims through streamlined no-touch automation**,
> So that **claims are evaluated, approved, and paid without manual intervention, reducing processing time and operational costs while ensuring accurate benefit delivery**


**Key Capabilities:**

> 1. System validates claim applicability by confirming only Wellness event type was selected and subject is the member with reason 'Other'
> 2. System determines payment eligibility by verifying policy active status, both general and wellness-specific waiting periods satisfied, and coverage limits not exceeded
> 3. System submits eligible claims to Open status and adjudicates wellness coverage across applicable policies
> 4. System schedules automated payments with member as payee, allocating benefit amounts per policy and setting incident date to wellness visit date
>     4.1 Upon coverage limit reached, system sets benefit amount to zero while maintaining allocation record
>     4.2 When multiple policies exist with varying waiting periods, system creates payments only for satisfied policies
> 5. System issues payments through scheduled payment process and triggers automatic case closure after payment completion
> 6. Upon multiple event types selected or incorrect case reason, system creates claims in Pending status without automated payments for manual review

---
## Initiative: Other Configurations

### Epic: Other Configurations

#### Feature: Configure coverage-based claim properties
- **Role**: Claim Adjuster
- **Action**: configure coverage-based claim properties to control override capabilities for monetary and occurrence-based claim attributes
- **Value**: the system automatically enforces business rules that prevent conflicting claim adjustments and ensures accurate benefit calculations aligned with policy coverage terms

**Description:**

> As a **Claim Adjuster**,
> I want to **configure coverage-based claim properties to control override capabilities for monetary and occurrence-based claim attributes**,
> So that **the system automatically enforces business rules that prevent conflicting claim adjustments and ensures accurate benefit calculations aligned with policy coverage terms**.


**Key Capabilities:**

> 1. System determines override eligibility based on coverage limit unit type (monetary vs. non-monetary vs. day-based)
> 2. Upon identifying monetary coverage with auto-calculated gross amounts, system enables gross amount override while restricting occurrence overrides
> 3. When coverage uses non-monetary units with auto-calculated quantities, system enables occurrence override while restricting gross amount changes
>     3.1 If fields are directly editable, system disables all override capabilities
>     3.2 For special benefit types (ambulance, wellness, coma), system restricts both override types
> 4. System enforces mutual exclusivity rule preventing simultaneous override of gross amounts and occurrence counts
> 5. Configuration applies automatically during claim intake and adjudication workflows

---

#### Feature: Premium Paid to Date process
- **Role**: Claim Adjuster
- **Action**: validate premium payment status against claim dates to ensure coverage eligibility before authorizing claim payments
- **Value**: the organization mitigates financial risk by preventing payment on claims where premiums are delinquent, ensuring policy compliance and protecting company assets

**Description:**

> As a **Claim Adjuster**,
> I want to **validate premium payment status against claim dates to ensure coverage eligibility before authorizing claim payments**,
> So that **the organization mitigates financial risk by preventing payment on claims where premiums are delinquent, ensuring policy compliance and protecting company assets**.


**Key Capabilities:**

> 1. System retrieves premium paid-to-date information from billing subsystem upon claim creation or date modifications.
> 2. System validates premium payment coverage against claim loss dates, applying type-specific rules for Disability versus Life/Accident claims.
> 3. Upon detecting payment shortfalls, system alerts adjuster through visual warnings in claim overview and payment interfaces.
> 4. System automatically generates investigation task when premium deficiency is identified and no duplicate task exists.
> 5. Adjuster reviews investigation task to determine claim eligibility and coordinates with billing to resolve premium discrepancies.
> 6. When validation passes, system permits normal payment processing without restrictions or manual interventions.

---

#### Feature: Calendar Full Month Calculation
- **Role**: Claim Adjuster
- **Action**: configure full month calculation rules to determine benefit payment periods based on varying calendar month lengths
- **Value**: benefit payments are processed accurately and consistently across all calendar months, accounting for month-end variations and leap years

**Description:**

> As a **Claim Adjuster**,
> I want to **configure full month calculation rules to determine benefit payment periods based on varying calendar month lengths**,
> So that **benefit payments are processed accurately and consistently across all calendar months, accounting for month-end variations and leap years**.


**Key Capabilities:**

> 1. System calculates full month end date from provided start date using default formula (start date + 1 month - 1 day)
> 2. Upon start date falling on last day of any month, system overrides default and sets end date to last day of following month
> 3. When start date is January 28th-31st, system applies special rule setting end date to last day of February in same year, accounting for leap year variation
> 4. System processes one monthly General Benefit Amount payment uniformly for each determined full month period
> 5. User is able to validate calculation results across different start date scenarios including edge cases
> 6. System prevents benefit payment processing until valid full month period is established

---

#### Feature: Common Rounding Rules
- **Role**: Claim Adjuster
- **Action**: define and apply standardized rounding rules for financial calculations across claim processing
- **Value**: ensure consistent and compliant monetary calculations throughout the claim lifecycle, reducing discrepancies and improving financial accuracy

**Description:**

> As a **Claim Adjuster**,
> I want to **define and apply standardized rounding rules for financial calculations across claim processing**,
> So that **I ensure consistent and compliant monetary calculations throughout the claim lifecycle, reducing discrepancies and improving financial accuracy**.


**Key Capabilities:**

> 1. System administrator configures rounding rules with business parameters and thresholds
> 2. Rounding rules are applied automatically during claim financial calculations
> 3. System validates calculation results against configured precision requirements
>     3.1 Upon detecting rounding discrepancies, system alerts for review
> 4. User is able to review and audit rounding applications across transactions
> 5. System maintains consistency across reserves, payments, and recovery calculations
> 6. Configuration supports jurisdiction-specific rounding requirements when applicable

---

#### Feature: Timezone Support
- **Role**: Claim Manager
- **Action**: configure and manage timezone settings across the claim management system
- **Value**: claim activities, timestamps, and reporting reflect accurate local time zones for distributed operations and regulatory compliance

**Description:**

> As a **Claim Manager**,
> I want to **configure and manage timezone settings across the claim management system**,
> So that **claim activities, timestamps, and reporting reflect accurate local time zones for distributed operations and regulatory compliance**.


**Key Capabilities:**

> 1. User is able to define and maintain timezone configurations for the claim system
> 2. System applies appropriate timezone conversions to all claim timestamps and activity records
> 3. Upon timezone configuration changes, system recalibrates existing timestamps without data loss
> 4. User is able to associate specific timezones to organizational units, users, or geographical territories
> 5. System displays all temporal data consistently according to configured timezone rules
> 6. When generating reports, system presents timestamps in relevant local timezone context

---
## Initiative: Auditing

### Epic: Activities

#### Feature: BAMs (Business Activity Monitoring)
- **Role**: Claim Manager
- **Action**: monitor and navigate claim lifecycle transitions across multiple product lines to ensure proper processing, state management, and financial reconciliation
- **Value**: I can maintain visibility of claim progression through all lifecycle stages, identify exceptions requiring intervention, and ensure regulatory compliance across diverse insurance products

**Description:**

> As a **Claim Manager**,
> I want to **monitor and navigate claim lifecycle transitions across multiple product lines to ensure proper processing, state management, and financial reconciliation**,
> So that **I can maintain visibility of claim progression through all lifecycle stages, identify exceptions requiring intervention, and ensure regulatory compliance across diverse insurance products**


**Key Capabilities:**

> 1. Monitor claim lifecycle state transitions from intake through payment to closure across all product lines
> 2. Track command execution and business activity milestones throughout claim processing workflow
> 3. Identify and manage financial imbalances including underpayments, overpayments, and recovery requirements
>     3.1 Upon detecting imbalance, system triggers product-specific correction workflows
> 4. Apply special handling flags when non-standard processing or alternate approval paths are required
> 5. Manage post-closure claim activities including reopening and reassignment when circumstances change
> 6. Access product-specific and market-specific processing rules including UK regulatory compliance requirements

---
## Initiative: Claim Workflow

### Epic: Define Claim Workflows

#### Feature: Contestability workflow
- **Role**: Claim Adjuster
- **Action**: manage claim processing through contestability review and resolution workflows including policy validation, payment adjudication exceptions, and claim status transitions
- **Value**: claims are properly adjudicated with appropriate manual intervention for exceptions, ensuring compliance with contestability provisions and accurate payment execution

**Description:**

> As a **Claim Adjuster**,
> I want to **manage claim processing through contestability review and resolution workflows including policy validation, payment adjudication exceptions, and claim status transitions**,
> So that **claims are properly adjudicated with appropriate manual intervention for exceptions, ensuring compliance with contestability provisions and accurate payment execution**


**Key Capabilities:**

> 1. System performs auto-adjudication of eligible claims and generates payment schedules according to established rules
> 2. Upon auto-adjudication failure, system routes claim to manual intervention workflow for closure or payment generation correction
> 3. When payment execution fails or cancellation occurs, adjuster reviews failure causes and determines corrective actions
> 4. System validates policy data synchronization and triggers refresh review when discrepancies are detected
> 5. Upon underpayment detection, system initiates approval workflow for payment adjustment authorization
> 6. When claim status transitions occur (LTD, return-to-work), adjuster validates eligibility and processes status-specific requirements

---

### Epic: Manual Task Definition

#### Feature: Manual Task Definition
- **Role**: Claim Manager
- **Action**: configure reusable task templates with assignment rules and time-based workflows
- **Value**: standardized work assignments can be automatically routed to appropriate teams with predefined deadlines and priorities

**Description:**

> As a **Claim Manager**,
> I want to **configure reusable task templates with assignment rules and time-based workflows**,
> So that **standardized work assignments can be automatically routed to appropriate teams with predefined deadlines and priorities**.


**Key Capabilities:**

> 1. Define task template with unique identifier, entity associations, and effective date ranges
> 2. Configure assignment parameters including preferred queues and read-only priority levels
> 3. Specify task attributes such as display names, descriptions, and extension parameters
> 4. Instantiate tasks from definitions with warning date calculations (period-based or fixed dates)
> 5. Apply due date requirements with configurable calculation methods
>     5.1 Upon Event Case task creation, system applies period-based date offsets
>     5.2 Upon Follow-Up task creation, user selects specific warning and due dates
> 6. Activate definitions on effective date for authorized task creation

---

### Epic: Queue Configuration

#### Feature: Queue Configuration
- **Role**: Claim Manager
- **Action**: organize and distribute claim-related tasks through specialized queues based on business function and user privileges
- **Value**: tasks are efficiently routed to appropriate personnel, ensuring proper oversight, workload distribution, and workflow progression across the claims lifecycle

**Description:**

> As a **Claim Manager**,
> I want to **organize and distribute claim-related tasks through specialized queues based on business function and user privileges**,
> So that **tasks are efficiently routed to appropriate personnel, ensuring proper oversight, workload distribution, and workflow progression across the claims lifecycle**


**Key Capabilities:**

> 1. User accesses designated queues based on assigned business privileges and functional responsibilities
> 2. System filters queue visibility according to user access rights for specialized functions
> 3. User views pending tasks within authorized queues and assesses priority
> 4. User assigns or reassigns tasks to appropriate personnel based on workload and expertise
>     4.1 When user lacks control privilege, system restricts assignment capabilities
> 5. User updates task details and progresses work items through workflow stages
> 6. User completes tasks and triggers downstream workflow events upon resolution

---
## Initiative: Notes

### Epic: Note Definition

#### Feature: Note Definition
- **Role**: Claim Adjuster
- **Action**: configure and manage standardized note definitions for claim documentation
- **Value**: I can ensure consistent, compliant, and efficient claim documentation across all claim activities

**Description:**

> As a **Claim Adjuster**,
> I want to **configure and manage standardized note definitions for claim documentation**,
> So that **I can ensure consistent, compliant, and efficient claim documentation across all claim activities**.


**Key Capabilities:**

> 1. User is able to establish note definition templates with business classification criteria
> 2. User is able to configure note category hierarchies and association rules for claim contexts
> 3. Upon defining note structure, system validates completeness and business rule compliance
> 4. User is able to assign note definitions to specific claim types, loss categories, or workflow stages
>     4.1 When conflicts exist, system prompts resolution
> 5. User is able to version and retire note definitions while preserving historical references
> 6. System applies defined note templates during claim documentation activities

---
## Initiative: Document Management

### Epic: Inbound Document Management

#### Feature: Inbound Document Management
- **Role**: Claim Adjuster
- **Action**: generate, validate, and deliver documents through on-demand or automated workflows with conditional approval
- **Value**: documents are accurately produced, properly reviewed when required, securely stored, and efficiently delivered to appropriate parties, reducing manual effort and ensuring compliance

**Description:**

> As a **Claim Adjuster**,
> I want to **generate, validate, and deliver documents through on-demand or automated workflows with conditional approval**,
> So that **documents are accurately produced, properly reviewed when required, securely stored, and efficiently delivered to appropriate parties, reducing manual effort and ensuring compliance**.


**Key Capabilities:**

> 1. User initiates on-demand generation or system triggers automated generation based on business events
> 2. System validates preconditions and prefills data from existing records to minimize manual entry
>     2.1 Upon precondition failure, process terminates immediately
>     2.2 When editing needed, user provides payee details, entity associations, delivery preferences, and content updates
> 3. User previews document and confirms generation after system validates mandatory field completion
> 4. System generates final document, links to appropriate entity, and uploads to centralized eFolder repository
> 5. When approval required, designated approver reviews and decides; rejection terminates process without delivery
> 6. System delivers via configured method (email with notification or review task assignment) based on business rules

---

### Epic: Outbound Document Management

#### Feature: Outbound Document Management
- **Role**: Claim Adjuster
- **Action**: generate, review, approve, and distribute claim-related documents through a controlled workflow
- **Value**: documents are accurate, compliant, and delivered to appropriate parties efficiently while maintaining audit trail and approval controls

**Description:**

> As a **Claim Adjuster**,
> I want to **generate, review, approve, and distribute claim-related documents through a controlled workflow**,
> So that **documents are accurate, compliant, and delivered to appropriate parties efficiently while maintaining audit trail and approval controls**


**Key Capabilities:**

> 1. System initiates document generation based on business trigger and captures required parameters
> 2. System creates document and automatically archives to electronic folder for recordkeeping
> 3. Upon approval requirement, system assigns review task to designated approver with document preview capability
> 4. User is able to review document content and approve or reject based on accuracy and compliance standards
>     4.1 If rejected, system creates revision task and regenerates document with feedback
>     4.2 If approved, system proceeds to distribution evaluation
> 5. System determines delivery method and distributes document via selected channel with confirmation notification
> 6. System finalizes document state and completes workflow with full audit trail

---

### Epic: eFolder

#### Feature: Configure eFolder Structure
- **Role**: Claim Manager
- **Action**: configure and establish standardized electronic folder structures to organize claim-related documents systematically
- **Value**: documents are consistently categorized, enabling efficient retrieval, compliance adherence, and streamlined claim processing across the organization

**Description:**

> As a **Claim Manager**,
> I want to **configure and establish standardized electronic folder structures to organize claim-related documents systematically**,
> So that **documents are consistently categorized, enabling efficient retrieval, compliance adherence, and streamlined claim processing across the organization**


**Key Capabilities:**

> 1. User is able to define hierarchical folder taxonomy aligned with business and regulatory requirements
> 2. User is able to establish document categories and classification rules for automated routing
> 3. User is able to configure folder templates based on claim type, line of business, or jurisdictional needs
> 4. Upon configuration completion, system validates structure integrity and enforces mandatory folder requirements
> 5. User is able to publish approved folder structures for organizational deployment
> 6. System applies configured structures automatically when new claims or cases are initiated

---
## Initiative: Administration

### Epic: User Management

#### Feature: User roles and Privileges
- **Role**: Claim Manager
- **Action**: configure and assign role-based access controls with inherited privilege hierarchies to ensure appropriate system authorization levels across the claims organization
- **Value**: the organization maintains proper segregation of duties, minimizes security risks, and enables efficient privilege management through automated inheritance while supporting both human and system actors

**Description:**

> As a **Claim Manager**,
> I want to **configure and assign role-based access controls with inherited privilege hierarchies to ensure appropriate system authorization levels across the claims organization**,
> So that **the organization maintains proper segregation of duties, minimizes security risks, and enables efficient privilege management through automated inheritance while supporting both human and system actors**


**Key Capabilities:**

> 1. Configure ascending privilege inheritance hierarchy from Customer Service Representative through Claim Adjuster to Claim Supervisor roles
> 2. Assign role-based authorization levels determining claims processing capabilities, financial transaction limits, and queue access rights
> 3. Establish specialized system roles for automated workflow orchestration and financial subsystem integration
>     3.1 When automated processes execute, system activates System User role with automation privileges
>     3.2 When financial integration required, CAP Financial Integration role manages payment operations
> 4. Map actors to roles supporting multiple role assignments based on situational requirements
> 5. Reuse configured roles across organizational units to minimize duplication and ensure consistency

---

#### Feature: Configure Authority levels
- **Role**: Claim Manager
- **Action**: configure authority level limits that govern automatic approval thresholds for claim payment processing across different claim subtypes
- **Value**: the system can automatically route payments for approval or manual review based on user authority, reducing processing delays and ensuring appropriate oversight

**Description:**

> As a **Claim Manager**,
> I want to **configure authority level limits that govern automatic approval thresholds for claim payment processing across different claim subtypes**,
> So that **the system can automatically route payments for approval or manual review based on user authority, reducing processing delays and ensuring appropriate oversight**


**Key Capabilities:**

> 1. Define authority level hierarchy with corresponding maximum payment amounts for each claim subtype (Life, Disability, Expense, Overpayment Waive, Dental, Pet, etc.)
> 2. Establish subtype-specific thresholds allowing granular control, including unlimited approval authority for senior levels
> 3. Configure special handling rules for sensitive subtypes requiring heightened scrutiny regardless of amount
> 4. When payment schedule is submitted, system validates amount against user's authority level and claim subtype configuration
>     4.1 Upon finding valid configuration where amount is within limit, system auto-approves payment
>     4.2 Upon exceeding limit or missing configuration, system routes for manual review
> 5. Support multi-tiered escalation where payments automatically route to appropriate authority level based on amount

---
## Initiative: Portability & Continuation

### Epic: Claim impacts of Portability & Continuation processing

#### Feature: Claim impacts of Portability & Continuation processing
---
## Initiative: ASO Fee Management

### Epic: Claim impacts and integrations required for ASO processing

#### Feature: Claim impacts and integrations required for ASO processing
---
## Initiative: Large Loss Claims

### Epic: Approvals

#### Feature: Approvals
---

#### Feature: Mobile Interface for CSSR users for specifc handling
---

### Epic: Reinsurance

#### Feature: Reinsurance
---
## Initiative: Claim Progress Tracker

### Epic: Claim Progress Tracker

#### Feature: Claim Progress Tracker
---
