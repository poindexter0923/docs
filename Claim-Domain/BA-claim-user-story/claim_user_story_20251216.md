---
title: "Claim User Story 20251216"
date: 2025-12-16
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
- **Role**: Claims User
- **Action**: search for and retrieve case and claim records across Benefits, P&C, Dental, and Pet lines of business using flexible single-line or advanced multi-field search options
- **Value**: I can quickly locate and access relevant case or claim information to perform my job functions efficiently, regardless of the line of business or claim type

**Description:**

> **As a** Claims User,
> **I want to** search for and retrieve case and claim records across Benefits, P&C, Dental, and Pet lines of business using flexible single-line or advanced multi-field search options,
> **so that** I can quickly locate and access relevant case or claim information to perform my job functions efficiently, regardless of the line of business or claim type.


**Key Capabilities:**

> 1. User accesses the CEM search interface from their current location within the application.
> 2. User selects their preferred search method:
>    2.1 Single-Line Search: User activates the search bar and begins typing a search query, receiving real-time auto-suggestions (up to 5 results) based on input.
>    2.2 Advanced Search: User opens the advanced search panel to access multiple optional search fields tailored to their needs.
> 3. For Single-Line Search, user either selects an auto-suggestion for immediate navigation or presses Enter/clicks 'View All' to see complete search results.
> 4. For Advanced Search, user enters search criteria across available fields (including Case #, Claim #, Date of Loss/Service, Name, Customer #, Location details, Policy Number, Claim Type, Tax ID, Business Name) and executes the search.
> 5. System retrieves matching records and displays the Case/Claim Search Results page with summary information, applied filters, and a paginated table of results.
> 6. User reviews search results showing key information (Case/Claim #, Status, Claim Type, Date, Policy #, Subject of Claim/Patient) organized in sortable and filterable columns.
> 7. User refines search results by:
>    7.1 Removing individual filter tags to adjust search parameters.
>    7.2 Using 'Clear All' to remove all applied filters.
>    7.3 Sorting results by Case/Claim # or Date columns.
>    7.4 Filtering by Claim Type through multi-select options.
> 8. User selects a specific case or claim record by clicking the hyperlinked Case/Claim # to navigate to the appropriate destination page.
> 9. System intelligently routes user to the correct page based on line of business, claim type, and status:
>    9.1 Benefits Claims: Routes to Claim Overview, Member Form (incomplete intake), or Event Case Overview depending on case/claim combination and intake status.
>    9.2 Dental Claims: Routes to Dental Claim Intake or Dental Claim Overview based on claim status.
>    9.3 P&C Claims: Routes directly to P&C claim overview page.
> 10. If search returns no results, system displays 'No results' message with guidance to adjust search parameters.
> 11. User can clear all advanced search inputs at any time before executing search to start fresh.

---

### Epic: View history of claims/event cases

#### Feature: View history of claims/event cases
- **Role**: Claims Adjuster
- **Action**: view a comprehensive history of claims and event cases across all lines of business (Benefits, P&C, Dental, and Pet) associated with a customer
- **Value**: I can efficiently access and review all claim-related activities for a customer in a single consolidated view, enabling faster decision-making and better customer service

**Description:**

> **As a** Claims Adjuster,
> **I want to** view a comprehensive history of claims and event cases across all lines of business (Benefits, P&C, Dental, and Pet) associated with a customer,
> **so that** I can efficiently access and review all claim-related activities for a customer in a single consolidated view, enabling faster decision-making and better customer service.


**Key Capabilities:**

> 1. User navigates to the customer portfolio page and selects the 'Claims' tab to access the consolidated claims history view.
> 2. System retrieves and displays all claims and event cases associated with the customer across Benefits, P&C, Dental, and Pet lines of business.
> 3. System presents claim records in a structured table view containing:
>    3.1. Claim identification information (claim number, case number where applicable)
>    3.2. Temporal information (date of loss or date of service based on LOB)
>    3.3. Policy association details
>    3.4. Product and line of business classification
>    3.5. Claim type designation
>    3.6. Current status with visual color-coding
>    3.7. Subject of claim or patient information
>    3.8. Financial summary (incurred amount and paid amounts for Benefits LOB)
> 4. System applies LOB-specific business rules for data display:
>    4.1. Benefits: Displays both case records and claim records where customer is Subject of Claim or Patient, shows product-specific naming conventions, includes financial totals
>    4.2. P&C: Shows risk item details (vehicle or property information), handles multiple risk items with expandable tooltips
>    4.3. Dental: Displays all service dates, shows patient name from dental records
>    4.4. Pet: Shows pet name, displays appropriate date based on claim type (service date or purchase date)
> 5. System enables navigation to detailed views:
>    5.1. Clicking claim numbers routes to appropriate LOB-specific claim overview pages
>    5.2. Clicking case numbers routes to event case overview or member intake form based on completion status
>    5.3. Clicking policy numbers routes to master or individual policy consolidated views
> 6. System sorts records appropriately:
>    6.1. For claim view: Sorted by date of loss/service in descending order (most recent first)
>    6.2. For case view: Primary sort by case number descending, secondary sort by claim number descending
> 7. System provides pagination controls to navigate large result sets with configurable page sizes (5-15 items per page, default 10).

---

### Epic: Action: Create New Case/Claim

#### Feature: Action: Create New Case/Claim
- **Role**: Claim Intaker
- **Action**: initiate a new claim from the Customer Portfolio by selecting the appropriate claim type (Benefits, Benefits (Portal), Dental, Pet, P&C (OOS), or Property and Casualty)
- **Value**: the system routes the user to the correct intake workflow based on the customer type and line of business, ensuring accurate and efficient claim initiation

**Description:**

> **As a** Claim Intaker,
> **I want to** initiate a new claim from the Customer Portfolio by selecting the appropriate claim type (Benefits, Benefits (Portal), Dental, Pet, P&C (OOS), or Property and Casualty),
> **so that** the system routes me to the correct intake workflow based on the customer type and line of business, ensuring accurate and efficient claim initiation.


**Key Capabilities:**

> 1. User accesses the Customer Portfolio UI and locates the claim component section.
> 2. User initiates claim creation by clicking the 'Create New Claim' button, which displays a submenu with available claim type options.
> 3. System presents claim type options based on customer eligibility:
>    3.1 Benefits option is available for all customers and navigates to Event Case Intake - Member (Claim) page.
>    3.2 Benefits (Portal) option is available only for individual customers with Group Sponsor relationship and navigates to Employer Portal - File a Claim for Employee intake wizard.
>    3.3 Dental option is available for all customers and navigates to Select Policy and Patient UI.
>    3.4 Pet option is displayed only for individual customers and navigates to Pet Claim Intake - Select Policy and Pet page.
>    3.5 P&C (OOS) option is available for all customers and is marked as out of scope.
>    3.6 Property and Casualty option is displayed only for individual customers and navigates to Jade Claim Initialization - Loss Event & Reporting Party page.
> 4. System provides visual feedback by highlighting the option button when user hovers over it.
> 5. User selects the appropriate claim type from the submenu.
> 6. System routes the user to the corresponding line of business-specific claim intake interface to begin the claim creation process.

---
## Initiative: Open New Event Case

### Epic: Intake Sources

#### Feature: Intake Sources
- **Role**: Claim Intaker
- **Action**: create and manage a single Event Case across Life, Absence, and Supplemental Benefits using a wizard-based intake process
- **Value**: multiple related claims are consolidated under one case for unified viewing, management, and payment processing

**Description:**

> **As a** Claim Intaker,
> **I want to** create and manage a single Event Case across Life, Absence, and Supplemental Benefits using a wizard-based intake process,
> **so that** multiple related claims are consolidated under one case for unified viewing, management, and payment processing.


**Key Capabilities:**

> 1. User initiates Event Case Intake from UI or Customer Portfolio, requiring appropriate access privileges (Initialize Case, Update Case Draft, Submit Case, Create Case).
>    1.1 When initiated from Customer Portfolio for individual customer, system pre-fills member information from CEM data.
>    1.2 When initiated from Customer Portfolio for organization customer, system pre-fills Organization, Class values, and Address details from CEM data.
>
> 2. User searches for existing Member or creates a new Member record.
>    2.1 If Member not found during search, user can create new Member within the intake workspace.
>    2.2 For Individual Policy intake, employer search and work details can be skipped during Member creation.
>
> 3. User completes Work Details form specifying employment information and clicks 'Create Case and Continue'.
>
> 4. System saves Member details, initializes the case, generates a unique Case Number, and saves the case in INCOMPLETE status.
>
> 5. User completes Case Detail form (Step 2 of wizard) by selecting Reporting Details (method, date), identifying the subject of the claim, selecting Type of Loss (Death, CriticalIllness, HospitalIndemnity, Accelerated Death, or Accident), entering Event Information, and entering ICD Code.
>    5.1 At any point during Case Detail entry, user can click 'Save & Exit' to save incomplete data (even if validation fails) and resume later via Customer Portfolio.
>    5.2 User can click 'Cancel' to exit without saving changes.
>    5.3 User can navigate between wizard steps using 'Next' and 'Previous' buttons.
>
> 6. User adds Reporting Party and other relevant parties in Party Detail form (Step 3 of wizard).
>
> 7. User clicks 'Complete Intake' to submit the Event Case.
>
> 8. System validates that minimum required data is present for Event Case Opening.
>
> 9. System saves Party details and updates case status from INCOMPLETE to OPEN.
>
> 10. System executes automated Event Case creation process, including:
>     - Evaluating Event Case applicability against Policy coverages based on Applicability Business Rules (mapping Claim Events to Policy Product Codes and Loss Types).
>     - Applying MP (Master Policy) filter to exclude Master Policies that already have Certificate Policies during claim initialization.
>     - Checking Claim Availability for the Event Case.
>     - Automatically generating applicable Claims based on evaluation results.
>     - For each applicable coverage, automatically generating coverage records, calculating Gross Amount, and marking as ready to pay.
>     - Evaluating Eligibility for the generated claims.
>     10.1 If policy status equals Canceled in StateMachine, system prevents generating new claims for that invalid policy.
>
> 11. System exits Case Intake workspace and displays the newly created case on Case Overview screen.

---

### Epic: Navigate step by step wizard

#### Feature: Navigate step by step wizard
- **Role**: Claim Intaker
- **Action**: navigate through a multi-step wizard to create and submit a new event case by selecting or adding a member, entering case details, managing additional parties, and completing the intake process
- **Value**: event cases are accurately captured with all required information, duplicate cases are detected, and claims are automatically initiated based on loss types while maintaining data integrity throughout the process

**Description:**

> **As a** Claim Intaker,
> **I want to** navigate through a multi-step wizard to create and submit a new event case by selecting or adding a member, entering case details, managing additional parties, and completing the intake process,
> **so that** event cases are accurately captured with all required information, duplicate cases are detected, and claims are automatically initiated based on loss types while maintaining data integrity throughout the process.


**Key Capabilities:**

> 1. User initiates case creation and begins with member selection step where system disables action buttons until member is identified.
> 2. User searches for existing member or adds new member, enabling case initialization.
> 3. User creates and initializes the case, which generates a case number with 'Incomplete' status and enables draft saving functionality.
> 4. User navigates to case detail step and enters event-specific information including loss types, dates, and relevant medical or absence details.
>    4.1 If duplicate cases are detected during validation, system presents confirmation modal with links to potentially duplicate cases for user review.
>    4.2 User can collapse optional forms such as Death or Accelerated Death forms as needed.
> 5. User navigates to additional parties step and manages party information associated with the case.
> 6. User completes intake which finalizes case creation, triggers loss and claim creation based on selected loss types, and saves all party information.
>    6.1 If group policy class information is missing, system creates claims in 'Pending' status and does not create premium waiver.
>    6.2 If group policy work state information is missing, system does not create SMP claims.
>    6.3 If dependents are not insured on policy, system flags non-eligible claims.
> 7. System redirects user to Case Overview screen displaying the completed case and any generated claims.
> 8. Throughout the workflow, user can save progress and exit at any time after case initialization, preserving all entered data including unvalidated fields.
> 9. User can navigate backward through visited steps using Previous button or step icons, with all data preserved during navigation.
> 10. User can cancel the intake process at any point, which closes the case if initialized or simply exits if case has not been created.

---

### Epic: Member Detail

#### Feature: Member Info
- **Role**: Claim Intaker
- **Action**: search for and select an existing member or add a new member to initiate an event case, including employment and address details
- **Value**: accurate member data is captured from the first point of contact, reducing duplicate data entry and ensuring proper case initiation

**Description:**

> **As a** Claim Intaker,
> **I want to** search for and select an existing member or add a new member to initiate an event case, including employment and address details,
> **so that** accurate member data is captured from the first point of contact, reducing duplicate data entry and ensuring proper case initiation.


**Key Capabilities:**

> 1. User initiates the member detail step and searches for an existing member by entering search criteria (minimum 3 characters) supporting case-insensitive, space-separated multi-parameter searches.
> 2. System retrieves and displays up to 10 matching members from CEM showing first name, last name, and date of birth, sorted alphabetically with search term highlights.
> 3. User selects a member from search results, and the system populates the member's name and displays the work detail section with employer search capability.
>   3.1 If member has existing employment data in CEM, the system pre-fills employer, work state, occupation, date of hire, and class fields while allowing user edits.
>   3.2 If no employment data exists, user searches and selects an employer, then enters or edits work detail attributes (work state, occupation, date of hire, class).
> 4. System displays address detail component with pre-filled member address from CEM (address lines, city, state/province, zip/postal code, country) in read-only format.
> 5. If member is not found or does not exist in the system, user initiates 'Add New Member' workflow to create a new member record.
>   5.1 User completes the Add New Member form capturing personal information (first name, last name, middle name, date of birth, gender), contact information (phone number, email address, contact preference), location details (address lines, country, city, state/province, zip/postal code), and employment information (employer and work details).
>   5.2 System validates mandatory fields and contact preferences, applies locale-specific formatting and field labels (e.g., UK locale uses DD/MM/YYYY date format, relabels State/Province to County, defaults country to United Kingdom).
>   5.3 Upon submission, system creates new member record in CEM, making it searchable in Customer Portfolio and available for case creation.
>   5.4 User can navigate back to member search from the Add New Member form, with entered data preserved.
> 6. When case creation is initiated from CEM Customer Portfolio for an individual customer, the system pre-fills member name and work detail attributes from CEM data.
>   6.1 For organization customers from CEM, system sets the organization as default employer (disabled for editing), auto-fills available class values for selection, and pre-fills and disables address fields, while allowing user to search and select member.
> 7. Once member details are captured, the search member section and Add New Member button become disabled to prevent changes after case number generation.
> 8. User proceeds to create the event case using 'Create Case and Continue' button, or can cancel to return to home page before case creation.

---

#### Feature: Work Details
- **Role**: Claim Intaker
- **Action**: add or edit member employment and work details during event case creation, including the ability to navigate back and modify previously entered information
- **Value**: accurate member work and employer information is captured and can be corrected before case finalization, reducing data entry errors and ensuring proper policy identification

**Description:**

> **As a** Claim Intaker,
> **I want to** add or edit member employment and work details during event case creation, including the ability to navigate back and modify previously entered information,
> **so that** accurate member work and employer information is captured and can be corrected before case finalization, reducing data entry errors and ensuring proper policy identification.


**Key Capabilities:**

> 1. User initiates Member detail entry and completes the form with member information, then proceeds to Step 2 by clicking 'Create Case and Continue'.
> 2. User can navigate back to Step 1 at any time by clicking the Step 1 Icon to review or edit previously entered information.
> 3. Upon returning to Step 1, the system displays:
>    3.1 Member's First name and Last name in disabled search bars (non-editable).
>    3.2 Work Detail Component with prefilled values that remain editable: Employer, Work State, Occupation, Date of Hire, Class, and Occupation Class.
>    3.3 Address Detail Component with prefilled employer address information in disabled/read-only state.
> 4. User can search and select an employer from organization customers marked as group sponsors (maximum 10 search results displayed).
> 5. Once an employer is entered, the system reveals and enables work detail fields for editing:
>    5.1 Work State becomes mandatory (US states only; hidden for UK locale).
>    5.2 Date of Hire becomes mandatory.
>    5.3 Occupation becomes optional.
>    5.4 Class and Occupation Class are pre-populated from employee census data but remain editable.
> 6. System auto-populates employer address fields from CEM based on the member's employment data, displaying preferred, mailing, or first available address.
> 7. User edits work detail fields as needed to correct or update employment information.
> 8. User submits the updated form by clicking the Next button.
> 9. System adds the new employee record to the system and opens the Case Detail form (Step 2).
> 10. If user chooses not to edit any fields after navigating back, user can proceed directly by clicking Next without making changes.

---

### Epic: Case Detail

#### Feature: Case Detail - Generic Details(Subject of Claim, Accident vs Sickness etc.)
- **Role**: Claim Intaker
- **Action**: capture comprehensive case detail information including reporting method, event classification, loss types, claim subject identification, and diagnosis codes during the second step of the event case intake process
- **Value**: accurate case classification and subject identification are established early in the intake workflow, enabling downstream policy applicability evaluation and claim creation

**Description:**

> **As a** Claim Intaker,
> **I want to** capture comprehensive case detail information including reporting method, event classification, loss types, claim subject identification, and diagnosis codes during the second step of the event case intake process,
> **so that** accurate case classification and subject identification are established early in the intake workflow, enabling downstream policy applicability evaluation and claim creation.


**Key Capabilities:**

> 1. User completes case detail entry including reporting method selection, date reported (mandatory, cannot be future date), event date (mandatory, validated against earliest Date of Loss), and optional event description (maximum 1000 characters).
> 2. User identifies the subject of the claim by selecting from available options including the primary member, active dependents (spouse or children with Personal relationship type and Active membership status displayed with relationship roles such as Wife, Husband, Domestic Partner, Daughter, Son), or other party.
>    2.1 If the claim subject is not listed among member or active dependents, user selects 'Other' option which opens the Add Additional Individual Party dialog where party information can be entered and saved before continuing.
> 3. User classifies the case by selecting mandatory Accident vs. Sickness designation (Accident, Sickness, or Other) using radio button selection.
> 4. User specifies applicable loss types by selecting one or more options from available loss types: Death, Accident, Serious Illness, Absence, Accelerated Death, Hospital Service, ADA - Work Accommodation, and Wellness.
>    4.1 Absence loss type is automatically disabled when the claim subject is not the employee per business rules.
>    4.2 For each selected loss type, user provides additional type-specific information through dedicated workflows (handled separately for Absence, Death, Accelerated Death, Serious Illness, Hospital Services, Accident, or Wellness).
> 5. User manages ICD diagnosis codes by searching and selecting from the searchable ICD code table, with each entry capturing ICD Code, Description, Primary indicator, and Date in user locale format.
>    5.1 User can edit existing ICD codes by clicking the Edit icon, updating information inline within the table, and saving changes, or cancel the edit to discard changes.
>    5.2 User can delete ICD codes by clicking the Delete icon and confirming removal via system confirmation dialog ('Are you sure you want to remove this entry?'), or cancel deletion to retain the entry.
>    5.3 System enforces validation rule that only one ICD code can be marked as primary across all entries.
> 6. User navigates to the next step (Step 3: Additional Parties) by clicking the Next button after completing all required information.
>    6.1 User can return to the previous step (Step 1: Member) by clicking the Previous button at any time during case detail entry.

---

#### Feature: Case Detail - ICD Code
- **Role**: Claim Adjuster
- **Action**: modify existing claim event information, add new loss types, manage ICD codes, and update event-specific details through a comprehensive editing interface
- **Value**: claim events accurately reflect all relevant loss information, enabling proper claim creation, routing, and processing across multiple lines of business

**Description:**

> **As a** Claim Adjuster,
> **I want to** modify existing claim event information, add new loss types, manage ICD codes, and update event-specific details through a comprehensive editing interface,
> **so that** claim events accurately reflect all relevant loss information, enabling proper claim creation, routing, and processing across multiple lines of business.


**Key Capabilities:**

> 1. User accesses existing event case overview and views associated claim events including loss types (Death, Accident, Serious Illness, Absence, Accelerated Death, Hospital Services, Dismemberment, ADA Work Accommodation, Wellness), Injury/Sickness classifications, and ICD code records.
> 2. User initiates edit process to modify claim event information.
>    2.1 If case status is 'Closed', system provides read-only view access only without edit capability.
> 3. System presents comprehensive Edit Claim Event drawer containing all loss type options, event description field, loss-specific information sections, accident vs. sickness classification, ICD code management, and action controls.
> 4. System displays loss type selection with pre-selected default losses (3 default losses greyed out and disabled from deselection) and available additional loss types.
>    4.1 If subject is not the employee, Absence option is automatically disabled and unavailable for selection.
> 5. User selects additional loss types (e.g., Death, Accident, Wellness) and completes required loss-specific information for each newly selected type.
> 6. User reviews and modifies existing loss information (e.g., Life Expectancy for Accelerated Death, work hours for Absence), with all previously captured values displayed and editable for losses where associated claims are not closed.
> 7. User adds or updates event description (optional, maximum 1000 characters) providing narrative context for the event.
> 8. User manages ICD code records by adding, editing, or removing diagnostic codes associated with the claim events.
> 9. User saves all modifications, triggering system validation, duplicate case/claim checks, event case update processing, and re-evaluation of auto-claim creation rules.
> 10. System processes updates, invokes backend APIs (GET/PUT event-cases, PUT individual-customers), cascades changes to existing Life, Critical Illness, and Hospital Indemnity claims, creates new claims as applicable (e.g., Accident), and returns user to case overview displaying all updated claim event information.
>    10.1 User may cancel editing at any time, discarding all unsaved changes and returning to case overview.

---

### Epic: Claim Events

#### Feature: Define Applicable Events
- **Role**: Claim Adjuster
- **Action**: view, edit, and manage claim events and associated diagnostic information for an event case
- **Value**: claim events are accurately documented, validated, and propagated to appropriate claims for consistent case management

**Description:**

> **As a** Claim Adjuster,
> **I want to** view, edit, and manage claim events and associated diagnostic information for an event case,
> **so that** claim events are accurately documented, validated, and propagated to appropriate claims for consistent case management.


**Key Capabilities:**

> 1. User navigates to a specific case overview page and accesses the Claim Events section, which displays current claim events, accident/sickness classification, ICD code information, and available action buttons based on case status.
> 2. User initiates editing of claim events by clicking the Edit button, which opens an interactive drawer displaying existing event information and available loss type options.
> 3. User manages loss type selection by adding new event types (Death, Accident, Accelerated Death, Absence, Serious Illness, Hospital Services, Wellness) while previously selected types remain locked to prevent data loss.
> 4. User provides event-level details including optional event description (up to 1000 characters) and completes loss-specific information across collapsible sections:
>    4.1. For Death events: death certificate date, official death date/manner/cause, underlying conditions, and location details.
>    4.2. For Accident events: accident date, first treatment date, location, work-related status, sport involvement, loss item, and description.
>    4.3. For Accelerated Death events: life expectancy prescription date, life expectancy in months, diagnosis date, and first treatment day.
>    4.4. For Absence events (only available when subject is the employee): absence reason, period, member work days, and relevant dates (last work date, initial absence date, reporting date, actively at work date, return to work date, first day of hospitalization, outpatient surgery date).
>    4.5. For Serious Illness events: diagnosis date, provider name, first treatment day, POL received date, and recurring status.
>    4.6. For Hospital Services: table-based entry of place of service, provider name, CPT code, and service date with add functionality.
>    4.7. For Wellness events: wellness visit date.
> 5. User manages ICD diagnostic codes by adding, editing, or deleting records in the ICD code table, including ICD code, description, primary indicator, and date.
> 6. User saves all changes, triggering system validation, duplicate case/claim validation workflow, and event case update command.
> 7. System propagates event changes to existing Life, Critical Illness, and Hospital Indemnity claims, creates new claims for newly added event types (e.g., Accident), and maintains existing Disability claims without modification.
> 8. For closed cases:
>    8.1. User accesses claim events in read-only mode via the View Details button.
>    8.2. System displays all event information, loss-specific details, and ICD codes in a non-editable information drawer.
>    8.3. User reviews historical claim event data without ability to modify any information.

---

#### Feature: Event details - Absence
- **Role**: Claim Intaker
- **Action**: collect employee information, absence reasons, absence periods, work schedule, and key absence-related dates during the initial absence case intake process
- **Value**: all required absence data is captured systematically at first point of contact, enabling accurate case creation and downstream claims processing

**Description:**

> **As a** Claim Intaker,
> **I want to** collect employee information, absence reasons, absence periods, work schedule, and key absence-related dates during the initial absence case intake process,
> **so that** all required absence data is captured systematically at first point of contact, enabling accurate case creation and downstream claims processing.


**Key Capabilities:**

> 1. User accesses the absence case creation interface (Step 1: Member) with required 'Initiate Loss' privilege.
> 2. Upon selecting 'Absence' as the loss type being reported, the system presents Additional Information for Absence section organized into four collapsible areas.
> 3. User captures Absence Reason information:
>    3.1 Adds at least one absence reason (mandatory requirement).
>    3.2 Can add multiple absence reasons using '+ Add Absence Reason' functionality following multiplicity rules.
> 4. User captures Absence Period information:
>    4.1 Adds at least one absence period (mandatory requirement).
>    4.2 Can add multiple absence periods using '+ Add Absence Period' functionality.
> 5. User defines the employee's typical work schedule:
>    5.1 Selects Member Work Days from available options (Sunday through Saturday).
>    5.2 For each selected work day, enters the number of hours worked (numeric values only).
>    5.3 System applies default work schedule (Monday-Friday, 8 hours each) if no existing CEM data is available, or pre-populates from existing employment records if available.
> 6. User enters mandatory absence-related dates:
>    6.1 Initial Absence Date (first day of absence).
>    6.2 Actively At Work Date (last day employee was fully active).
>    6.3 Date Last Worked (most recent work date).
>    6.4 If Initial Absence Date is earlier than Event Date, system displays warning to user.
>    6.5 If Date Last Worked is earlier than Event Date or is a future date, system displays warning to user.
> 7. User optionally enters additional clinical dates:
>    7.1 First Day of Hospitalization (if applicable).
>    7.2 Outpatient Surgery Date (if applicable).
>    7.3 If First Day of Hospitalization is earlier than Initial Absence Date, system prevents progression with error message.
>    7.4 If Outpatient Surgery Date is earlier than Initial Absence Date, system prevents progression with error message.
> 8. User submits the information by clicking Next button.
> 9. System validates all mandatory fields and date logic, then advances to Step 2 (Case Detail page) for further absence period management including actual absence periods and return-to-work dates.
> 10. If user attempts to proceed without required Absence Reason, system prevents progression.
> 11. If user attempts to proceed without required Absence Period, system prevents progression.

---

#### Feature: Event details - Death
- **Role**: Claim Intaker
- **Action**: capture comprehensive death-related details during event case intake, including official date of death, manner and cause of death, underlying conditions, and location information
- **Value**: accurate death loss information is recorded at first notice of loss to support claims adjudication, compliance, and investigation requirements

**Description:**

> **As a** Claim Intaker,
> **I want to** capture comprehensive death-related details during event case intake, including official date of death, manner and cause of death, underlying conditions, and location information,
> **so that** accurate death loss information is recorded at first notice of loss to support claims adjudication, compliance, and investigation requirements.


**Key Capabilities:**

> 1. System conditionally displays the 'Additional Information' section with a collapsible 'Death' subsection when the user selects 'Death' as the loss type during event case intake.
> 2. User captures official death information:
>    2.1 Records the Official Date of Death (required) with appropriate date format based on user locale.
>    2.2 Optionally records the date the death certificate was received.
>    2.3 Selects the Official Manner of Death from predefined options.
>    2.4 Provides optional description for the manner of death when applicable.
> 3. User documents medical and causal information:
>    3.1 Enters the Official Cause of Death as free text.
>    3.2 Records any Underlying Conditions contributing to the death.
> 4. User specifies location of death by selecting Country and State (where applicable based on locale).
> 5. System validates data integrity:
>    5.1 If Official Date of Death is missing, system prevents progression and displays required field error.
>    5.2 If Official Date of Death precedes the Event Date, system displays a warning but allows the user to proceed.
>    5.3 System adjusts field visibility and date formats based on user locale (e.g., hides State field for UK users).
> 6. User collapses or expands the Death section as needed using fold/unfold controls to manage screen real estate.
> 7. Upon completion, user proceeds to the next step in the event case intake workflow with all death details captured and persisted to the event case entity.

---

#### Feature: Event details - Accelerated Death
- **Role**: Claim Intaker
- **Action**: collect and record detailed accelerated death event information including life expectancy prescription date, life expectancy duration, diagnosis date, and treatment date during the event intake process
- **Value**: complete and accurate accelerated death claim data is captured at the point of intake to support timely claim processing and regulatory compliance

**Description:**

> **As a** Claim Intaker,
> **I want to** collect and record detailed accelerated death event information including life expectancy prescription date, life expectancy duration, diagnosis date, and treatment date during the event intake process,
> **so that** complete and accurate accelerated death claim data is captured at the point of intake to support timely claim processing and regulatory compliance.


**Key Capabilities:**

> 1. User selects 'Accelerated Death' as the loss type during the Event Intake process, triggering display of the specialized data collection section.
> 2. User accesses the collapsible 'Additional Information for Accelerated Death' section and expands it to view and enter required details.
> 3. User records mandatory clinical information:
>    3.1 Date when life expectancy was medically prescribed (via calendar date picker)
>    3.2 Life expectancy duration in months (numeric value)
>    3.3 Reported day of diagnosis (via date picker)
> 4. User optionally records first day of treatment information when available (via date picker).
> 5. System validates entered data according to business rules:
>    5.1 If reported diagnosis date precedes the event date, system displays non-blocking warning to alert user of potential date discrepancy while allowing continuation.
> 6. User collapses or expands the section as needed to manage screen real estate during multi-step intake process.
> 7. User proceeds to next step in the intake workflow after completing all required fields.
> 8. System persists all accelerated death details to the appropriate data entity for downstream claim processing.

---

#### Feature: Event details - Serious Illness
- **Role**: Claims Intake Specialist
- **Action**: capture and validate comprehensive Serious Illness loss details during event case intake, including diagnosis information, treatment dates, medical provider details, and diagnostic codes
- **Value**: accurate, complete Serious Illness claims are initiated with all critical medical information captured at first point of contact, reducing rework and enabling timely claims adjudication

**Description:**

> **As a** Claims Intake Specialist,
> **I want to** capture and validate comprehensive Serious Illness loss details during event case intake, including diagnosis information, treatment dates, medical provider details, and diagnostic codes,
> **so that**: accurate, complete Serious Illness claims are initiated with all critical medical information captured at first point of contact, reducing rework and enabling timely claims adjudication.


**Key Capabilities:**

> 1. User with case initiation privileges logs into the system and selects 'Serious Illness' as the type of loss being reported during event intake.
> 2. System presents a dedicated 'Serious Illness' information section within the Additional Information area, with collapsible display controls for efficient screen real estate management.
> 3. User captures the Initial Diagnosis Date of the Serious Illness, which is mandatory for submission.
> 4. User records one or more ICD diagnostic codes associated with the Serious Illness, with at least one code required for intake completion.
> 5. User optionally documents supporting medical information:
>    5.1 Provider Name identifying the hospital or medical facility
>    5.2 First Day of Treatment date marking the commencement of medical care
>    5.3 Proof of Loss Received Date documenting when medical documentation was obtained
> 6. System validates all entered data against business rules:
>    6.1 If Diagnosis Date is missing, system blocks progression and requires entry
>    6.2 If First Day of Treatment precedes Diagnosis Date, system blocks progression until corrected
>    6.3 If Diagnosis Date is earlier than Event Date, system issues warning but allows user to proceed with verification
>    6.4 If no ICD codes are provided, system blocks progression until at least one code is added
> 7. Upon successful validation, user proceeds to the next stage of the intake workflow.
> 8. All captured Serious Illness details are persisted to the event case record for downstream claims processing and adjudication.

---

#### Feature: Event details - Hospital services
- **Role**: Claim Intaker
- **Action**: capture and manage hospital services information (including place of service, provider name, CPT codes, service dates, and proof of loss received dates) during event case intake
- **Value**: all relevant hospital services details are accurately recorded at the point of loss reporting, enabling timely claims processing and reducing downstream data collection efforts

**Description:**

> **As a** Claim Intaker,
> **I want to** capture and manage hospital services information (including place of service, provider name, CPT codes, service dates, and proof of loss received dates) during event case intake,
> **so that** all relevant hospital services details are accurately recorded at the point of loss reporting, enabling timely claims processing and reducing downstream data collection efforts.


**Key Capabilities:**

> 1. User selects 'Hospital Services' as the loss type, which displays the 'Additional Information for Hospital Services' collapsible section within the case intake workflow.
> 2. User specifies the number of services to be added (1-20, defaulting to 1) and initiates the service entry process.
> 3. System presents a service entry interface where user captures details for each service:
>    3.1 User selects place of service from a predefined lookup list.
>    3.2 User enters provider name.
>    3.3 User searches and selects CPT code using fuzzy search capabilities.
>    3.4 User enters either a specific service date or a date range (mandatory validation).
>    3.5 User records proof of loss received date.
> 4. User can dynamically add additional service entries beyond the initial number specified.
> 5. User can delete service entries during the entry process:
>    5.1 System prompts for confirmation before removing service cards.
>    5.2 If the last service card is deleted, the card remains but attributes are cleared.
>    5.3 Service sequence numbers automatically refresh after deletions.
> 6. User submits all service entries for validation and addition to the service list.
>    6.1 If validation fails (missing mandatory dates or dates earlier than event date), system displays warning messages and user must correct errors.
>    6.2 If user cancels the entry process, system discards all unsaved entries and returns to the case detail page.
> 7. System displays all successfully added services in an expandable accordion format showing all captured attributes.
> 8. User can edit existing services in the list:
>    8.1 System opens an edit interface pre-populated with existing service data.
>    8.2 User updates values and submits changes.
>    8.3 System validates updates using the same business rules as initial entry.
> 9. User can delete services from the service list after confirmation.
> 10. User can collapse or expand the hospital services section to manage screen real estate.
> 11. User proceeds to the next step in the case intake workflow once all hospital services information is captured.
> 12. System saves all captured hospital services data to the event case record and maps to the appropriate data model entities.

---

#### Feature: Event details - Accident details
- **Role**: Claim Intaker
- **Action**: capture accident-specific details including dates, location, work-relatedness, and child sport participation when initiating a case or event intake with 'Accident' as the loss type
- **Value**: all accident-related information is systematically collected, validated, and stored to support accurate claim processing and regulatory compliance

**Description:**

> **As a** Claim Intaker,
> **I want to** capture accident-specific details including dates, location, work-relatedness, and child sport participation when initiating a case or event intake with 'Accident' as the loss type,
> **so that** all accident-related information is systematically collected, validated, and stored to support accurate claim processing and regulatory compliance.


**Key Capabilities:**

> 1. User initiates case/event intake and selects 'Accident' as the loss type, triggering the display of an 'Additional Information' section specific to accident details.
> 2. User provides mandatory accident information:
>   2.1 Date of Accident using locale-dependent calendar control (DD/MM/YYYY for en_GB, MM/DD/YYYY otherwise).
>   2.2 Date of First Treatment of Accident using calendar control with validation to ensure it occurs on or after the Date of Accident.
>   2.3 Work Related indicator (Yes/No) to identify workplace accidents.
>   2.4 Child Organized Sport indicator (Yes/No) when the claim subject is identified as a child.
> 3. User optionally provides supplementary accident information:
>   3.1 Accident Location from a predefined dropdown list.
>   3.2 When 'Other' is selected for Accident Location, user provides a text description of the accident location.
>   3.3 Loss Item(s) using multi-select dropdown to identify specific items damaged or lost in the accident.
> 4. System performs real-time validation:
>   4.1 Enforces completion of all mandatory fields before allowing progression.
>   4.2 Validates chronological consistency between Date of Accident and Date of First Treatment.
>   4.3 Issues warning (non-blocking) if Date of Accident is earlier than Event Date to alert user of potential data inconsistency.
> 5. User clicks 'Next' to save all entered accident information to CapAccidentDetailEntity and advance to the next step in the case intake workflow.

---

#### Feature: Event details - Wellness
- **Role**: Claim Intaker
- **Action**: capture and validate Wellness loss event details during case intake, including the Wellness Visit Date and automatic ICD code assignment when applicable
- **Value**: accurate wellness claim event data is recorded, validated against business rules, and properly stored for downstream claim processing

**Description:**

> **As a** Claim Intaker,
> **I want to** capture and validate Wellness loss event details during case intake, including the Wellness Visit Date and automatic ICD code assignment when applicable,
> **so that** accurate wellness claim event data is recorded, validated against business rules, and properly stored for downstream claim processing.


**Key Capabilities:**

> 1. User with appropriate privilege navigates to Case Intake for Accident products and selects 'Wellness' as the type of loss being reported.
> 2. System conditionally displays the Additional Information section as a collapsible panel when Wellness is selected.
> 3. User specifies the Wellness Visit Date using a date picker, which is mandatory for submission.
> 4. System validates the Wellness Visit Date against multiple business rules:
>    4.1 If the date field is empty, system blocks submission with mandatory field error.
>    4.2 If the date is earlier than the Event Date, system displays a warning but allows the user to proceed.
>    4.3 If the date is in the future, system blocks submission with future date error.
> 5. When Wellness is the only Claim Event in the case, system automatically pre-populates the ICD code field with Z00.00 and sets the ICD date equal to the Wellness Visit Date.
> 6. Upon successful validation, user proceeds to the next step in the intake process, and system persists the wellness event details to the appropriate data entity.
> 7. System navigates to the next information collection step in the intake workflow.

---

### Epic: Claim Without Policy

#### Feature: Claim Without Policy
---

### Epic: Additional Parties

#### Feature: Add/Update new claim party
- **Role**: Claim Intaker
- **Action**: search for, add, and manage parties (including vendors) associated with an Event Case, assigning them appropriate claim roles and maintaining their contact information
- **Value**: all relevant parties are accurately identified, associated with the case, and have up-to-date information for effective claim processing and communication

**Description:**

> **As a** Claim Intaker,
> **I want to** search for, add, and manage parties (including vendors) associated with an Event Case, assigning them appropriate claim roles and maintaining their contact information,
> **so that** all relevant parties are accurately identified, associated with the case, and have up-to-date information for effective claim processing and communication.


**Key Capabilities:**

> 1. User searches for existing parties in the system to identify if the party is already registered.
> 2. User adds identified parties to the Event Case and assigns appropriate claim roles based on their involvement in the loss event.
> 3. When a party does not exist in the system:
>    3.1 User initiates the Add New Party process to create a new party record.
>    3.2 User captures all required party information during creation.
>    3.3 User associates the newly created party with the case and assigns the appropriate claim role.
> 4. When party contact information requires updating:
>    4.1 User accesses the Edit Party Contact Information functionality for existing parties associated with the case.
>    4.2 User updates contact details as needed (note: payment method editing is handled separately in the Additional Parties section).
> 5. When managing vendor parties:
>    5.1 User follows specialized vendor workflows for creating new vendor records (Add New Party - Vendor).
>    5.2 User updates vendor-specific information through the Edit Vendor functionality.
>    5.3 User reviews comprehensive vendor information using the View Detail - Vendor capability.
> 6. User views associated party information throughout the case lifecycle to support claim processing decisions and communications.
> 7. System maintains party-to-case associations and role assignments for downstream claim processing workflows.

---

#### Feature: Manage payment method for the party
- **Role**: Claim Intaker
- **Action**: configure and manage payment methods for additional parties involved in an event case during the intake process
- **Value**: payments can be processed accurately and efficiently to the correct parties using their preferred payment methods

**Description:**

> **As a** Claim Intaker,
> **I want to** configure and manage payment methods for additional parties involved in an event case during the intake process,
> **so that** payments can be processed accurately and efficiently to the correct parties using their preferred payment methods.


**Key Capabilities:**

> 1. During the third step 'Additional Parties' of the event case intake wizard, user can add and manage additional parties involved in the event case.
> 2. For each additional party, user can configure payment method details including:
>   2.1 Payment method type selection (e.g., ACH/Direct Deposit, Check, Wire Transfer, Payment Card).
>   2.2 Required banking or financial account information based on the selected payment method.
>   2.3 Payee name and verification details.
> 3. User can add multiple payment methods for a single party if needed for different payment scenarios.
> 4. User can edit or remove payment methods for additional parties before completing the intake process.
> 5. System validates payment method information for completeness and format (e.g., valid routing numbers, account numbers) before allowing progression.
> 6. Payment method information is saved along with other party details when user clicks 'Save & Exit' or upon completion of the intake process.
> 7. Upon completing intake, payment method information becomes available for downstream payment processing workflows.

---

### Epic: Applicability validation - automated claim creation

#### Feature: Applicability validation - automated claim creation
- **Role**: Claim Intaker
- **Action**: create a new event case through a guided wizard process that automatically validates policy applicability and generates eligible claims
- **Value**: loss events are captured accurately and claims are initiated efficiently without manual policy lookup or duplicate data entry

**Description:**

> **As a** Claim Intaker,
> **I want to** create a new event case through a guided wizard process that automatically validates policy applicability and generates eligible claims,
> **so that** loss events are captured accurately and claims are initiated efficiently without manual policy lookup or duplicate data entry.


**Key Capabilities:**

> 1. User initiates event case creation through a three-step guided wizard (Member Selection, Case Detail Entry, Additional Parties).
> 2. During the Member step, user searches for and selects an existing member or adds a new member to the system.
>   2.1 Upon successful member selection or creation, user can proceed to create the event case by confirming the action.
>   2.2 User has the option to cancel the process and return to the home page before the event case is created.
> 3. Once the event case is created after the Member step, the system enables draft management capabilities.
>   3.1 User can save entered data and exit the wizard at any point, preserving work in progress.
>   3.2 User can cancel and close the case creation process if needed.
> 4. During the Case Detail step, user provides loss event information (e.g., date of loss, type of incident, location) and navigates between wizard steps.
>   4.1 User can move forward to the next step after entering required case details.
>   4.2 User can navigate back to the previous step to review or modify member information.
> 5. During the Additional Parties step, user identifies and adds relevant parties to the loss event (e.g., claimants, witnesses, third parties).
> 6. User completes the intake process by submitting the event case for processing.
> 7. Upon submission, the system automatically executes applicability validation to determine which policies are relevant to the loss event.
>   7.1 System evaluates active policies associated with the member against the loss date and event details.
>   7.2 For each applicable policy, the system automatically creates corresponding claim records.
>   7.3 If applicability cannot be automatically determined, the system flags the event case for manual review.
> 8. After applicability processing and claim creation, the system navigates the user to the Case Overview screen displaying the event case and all generated claims.

---
## Initiative: Case Overview

### Epic: Case Header

#### Feature: Case Header Details
- **Role**: Case Manager
- **Action**: view and manage comprehensive event case information including member details, claim events, special handling indicators, and case assignments through a consolidated case overview interface
- **Value**: I can efficiently manage all aspects of an event case from a single view, ensure accurate claim event tracking, and maintain up-to-date case information throughout the claims lifecycle

**Description:**

> **As a** Case Manager,
> **I want to** view and manage comprehensive event case information including member details, claim events, special handling indicators, and case assignments through a consolidated case overview interface,
> **so that** I can efficiently manage all aspects of an event case from a single view, ensure accurate claim event tracking, and maintain up-to-date case information throughout the claims lifecycle.


**Key Capabilities:**

> 1. User navigates to case overview by searching for and entering a case number.
> 2. System displays consolidated event case view with case header information including auto-generated case number, color-coded status badges (Gray=Incomplete, Green=Open, Blue=Closed), event date, reporting date, and reporting method.
> 3. User views member information including name, customer ID, demographics, employment details (occupation, work state, occupation class, job title), work schedule, contact information, and dependent relationships.
>    3.1 User can click member name hyperlink to view key member information in pop-up with option to access comprehensive member data and full CEM customer portfolio.
>    3.2 User can update Occupation Class and Participant Work Days inline using edit icons with changes saved and reflected immediately.
>    3.3 User can click dependent name link to navigate to dependent's individual customer portfolio.
> 4. User views subject of claim information including name and customer ID.
>    4.1 User can click subject of claim name hyperlink to view key customer information in pop-up with option to access comprehensive customer data.
> 5. User views case manager assignment information.
>    5.1 When case status is NOT closed, user can click case manager name hyperlink to access assignment details (reopened cases allow reassignment).
> 6. User views special handling indicators (SIU, Appeal, Complaint, Attorney, Litigation, Fast Track, VIP) accessible via hyperlink.
> 7. User views key case information including substatus, dates in locale-specific format (DD/MM/YYYY for en_GB), case manager assignment (user or queue), and special handling flags.
> 8. User views claim events section with accordion control displaying all claim events (Death, Accident, Serious Illness, Absence, Accelerated Death, Hospital Services, Wellness), Accident vs. Sickness classification, and ICD Code Summary Table.
>    8.1 When accordion is folded, system displays claim event types summary.
>    8.2 User can click Refresh link to update claim events data (link disabled during refresh process and hidden after claim closure).
> 9. User decides to add or modify claim events and clicks Edit button to initiate edit mode.
>    9.1 If case is in Closed status, only View Details button is available. User clicks View Details to open read-only drawer displaying detailed information for all claim event types with empty values shown as '-' and multi-value fields comma-separated. User closes drawer and returns to case overview.
> 10. System opens Edit Claim Event drawer showing default-selected and greyed out losses (non-editable) and available event type cards for selection.
>     10.1 When subject is not the employee, Absence option is disabled and unticked.
> 11. User selects new event types (death, accident, wellness) and fills in corresponding required information for each event.
> 12. User reviews and modifies Accelerated Death information including Life Expectancy (months) field.
> 13. User configures work schedule with default value of 8 hours for work scheduled hours and fills in additional fields as needed.
> 14. User selects Wellness option and fills in Wellness Visit Date.
> 15. User adds new ICD record and clicks Save button.
> 16. System triggers duplicate case/claim validation.
> 17. System saves updated information, returns to main screen, and triggers update case workflow to cascade event changes to existing Life, CI, and HI claims, creates new Accident claim, and preserves existing DI claims without impact.
> 18. User views updated claim events and newly added ICD records in Claim Events section.

---

#### Feature: Case Manager Assignment
- **Role**: Claim Adjuster
- **Action**: view the assigned case manager and reassign cases to eligible users or queues based on workload and availability
- **Value**: cases are efficiently distributed among active staff, workload is balanced, and case ownership is clearly maintained throughout the claim lifecycle

**Description:**

> **As a** Claim Adjuster,
> **I want to** view the assigned case manager and reassign cases to eligible users or queues based on workload and availability,
> **so that** cases are efficiently distributed among active staff, workload is balanced, and case ownership is clearly maintained throughout the claim lifecycle.


**Key Capabilities:**

> 1. System automatically assigns case manager upon intake completion.
>   1.1 System retrieves eligible users with appropriate claim authority type based on Authority Level and OpenL rules assignment.
>   1.2 System filters users to include only those with Active status and where the system date falls outside their unavailability period.
>   1.3 System applies load balancing by counting active cases (CMMN case status = active) for each eligible user and assigns the case to the user with the smallest active case count.
>   1.4 System assigns the case to the default queue 'claim_management' in addition to the selected user.
>   1.5 System updates the CMMN case manager, Case Header case manager, and assigns the New Case task to the selected case manager.
>   1.6 If no eligible users are available after filtering, system assigns case only to the 'Claim Management' queue without user assignment.
>   1.7 If exactly one eligible user is available, system assigns case to both that user and the 'Claim Management' queue, bypassing load balancing.
> 2. User views case manager information on the Case Overview UI.
>   2.1 System displays case manager name as a hyperlink in the non-editable Case Header section.
>   2.2 System shows either the person's full name (first name + last name) or queue name depending on assignment type.
> 3. User accesses case manager contact details.
>   3.1 User clicks on the case manager name hyperlink.
>   3.2 System opens a pop-up window displaying case manager contact information including address, phone, and email retrieved from EmployeeCommunicationInfo.
>   3.3 System displays preferred contact methods when multiple exist, showing up to 2 items with additional items accessible via tooltip on hover.
>   3.4 System applies UK-specific formatting when locale = en_GB.
> 4. User initiates case reassignment.
>   4.1 User clicks the 'Reassign Case' button from the Case Management pop-up.
>   4.2 System opens the Assign Case form with 'To someone' option selected by default and displays the Assignees search box.
> 5. User searches and selects a new assignee.
>   5.1 User inputs search text in the Assignee field (case-insensitive search triggered after 3 characters).
>   5.2 System displays search results showing Name (hyperlink with hover tooltip), Department, and Role(s) from OrganizationalPerson, organizationAssignments, and RoleAccessProfile data sources.
>   5.3 System filters out users not present in Security MS and displays 'No data is found' if no results match.
>   5.4 User selects an assignee from the search results, enabling the Assign button.
>   5.5 If user selects 'To a Queue' option instead, system displays a queue drop-down box filtered by sourceCd = CAP, and user selects a queue from the list.
> 6. User completes the reassignment.
>   6.1 User optionally inputs Notes in the rich text field with formatting toolbar.
>   6.2 User clicks the 'Assign' button.
>   6.3 System invokes POST /backoffice-platform-work/v1/cases/\{caseId\}/assignment, saves changes to backend, closes the Assign Case form, and updates the Case Manager's Name on the Case Overview UI Header.
>   6.4 If user clicks 'Cancel' or the Close Icon (X), system displays a confirmation modal asking 'Are you sure you want to close this form?', and upon confirmation, closes the form without saving and returns to Case Overview UI.

---

#### Feature: Special Handling
- **Role**: Case Manager
- **Action**: view, manage, and navigate special handling flags (SIU, Appeal, Complaint, Attorney, Litigation, VIP, Fast Track) from the Event Case Overview interface
- **Value**: critical case attributes are immediately visible and accessible, enabling prioritized case handling and compliance with specialized processing requirements

**Description:**

> **As a** Case Manager,
> **I want to** view, manage, and navigate special handling flags (SIU, Appeal, Complaint, Attorney, Litigation, VIP, Fast Track) from the Event Case Overview interface,
> **so that** critical case attributes are immediately visible and accessible, enabling prioritized case handling and compliance with specialized processing requirements.


**Key Capabilities:**

> 1. User searches for a case by case number and navigates to the Event Case Overview page.
> 2. System displays comprehensive Event Case Consolidated View with three hierarchical sections:
>    2.1 Case Header Line showing case number, color-coded status badge (Incomplete=Gray, Open=Green, Closed=Blue), case substatus, and action dropdown menu.
>    2.2 Key Case Information section displaying member and subject of claim identifiers, event and reporting dates, reporting method, case manager assignment, and special handling flags.
>    2.3 Member Detail section presenting personal information, employment details, work schedule, contact information, and dependent relationships.
> 3. Special handling flags are displayed as comma-separated values with visual toggles in the Key Case Information section, including: SIU, Appeal, Complaint, Attorney, Litigation, VIP, and Fast Track.
> 4. User can click on any special handling hyperlink or flag to navigate to the special handling module.
> 5. Upon clicking special handling flag, system redirects user to dedicated special handling module where user can view detailed information and manage flags based on privileges.
> 6. User with appropriate privileges (Create/Update Special Handling) can add, modify, or remove special handling flags within the special handling module.
> 7. All changes to special handling flags are saved and immediately reflected in the Event Case Overview upon returning to the page.
> 8. User can access related case information and perform navigation actions:
>    8.1 Clicking member name or subject of claim name opens respective information popups with option to view complete customer portfolio in CEM.
>    8.2 Clicking case manager name opens Case Manager Info popup with navigation to case management module (enabled when case status is NOT closed or for reopened claims).
>    8.3 Clicking dependent names navigates to individual customer portfolio pages in CEM.
>    8.4 Using 'I want to' dropdown menu provides filtered action options based on current case status.
> 9. All UI elements follow DSM library standards with locale-specific formatting for dates, phone numbers, and addresses.

---

#### Feature: Case closing reasons
- **Role**: Claims Adjuster
- **Action**: document and apply a specific closure reason when closing an event case from the Case Overview header
- **Value**: the organization maintains accurate case disposition records for reporting, compliance, and business intelligence purposes

**Description:**

> **As a** Claims Adjuster,
> **I want to** document and apply a specific closure reason when closing an event case from the Case Overview header,
> **so that** the organization maintains accurate case disposition records for reporting, compliance, and business intelligence purposes.


**Key Capabilities:**

> 1. User navigates to the Case Overview screen for an active event case.
> 2. User accesses case closure functionality from the Case Header section.
> 3. System presents a list of predefined closure reasons relevant to the case type and current status.
> 4. User selects the appropriate closure reason from the available options.
> 5. User confirms the closure action, triggering system validation and case status update.
> 6. System records the closure reason, timestamp, and user information as part of the case audit trail.
> 7. System updates the case status to 'Closed' and applies business rules for downstream processing (e.g., notifications, reporting, archival workflows).

---

### Epic: Case Actions ("I want to")

#### Feature: Update Case Information
- **Role**: Claim Adjuster
- **Action**: edit and update claim event loss types, loss-specific details, ICD codes, and additional case information (including reporting details, work details, and contact information) from the Case Overview page
- **Value**: case records remain accurate and complete as new information becomes available, ensuring proper claim routing and processing

**Description:**

> **As a** Claim Adjuster,
> **I want to** edit and update claim event loss types, loss-specific details, ICD codes, and additional case information (including reporting details, work details, and contact information) from the Case Overview page,
> **so that** case records remain accurate and complete as new information becomes available, ensuring proper claim routing and processing.


**Key Capabilities:**

> 1. User accesses the Case Overview page and initiates editing of claim events or additional case information.
> 2. For editing Claim Events:
>    2.1 User opens the 'Edit Claim Events' drawer and reviews existing loss types, which appear greyed out and cannot be unselected.
>    2.2 User optionally adds new loss types from available options (Absence, Death, Accelerated Death, Serious Illness, Hospital Services, Accident, Wellness, etc.).
>       2.2.1 If the subject of the case is not the employee, the Absence option is disabled and cannot be selected.
>       2.2.2 Newly added loss type sections appear with empty fields requiring user population.
>    2.3 User updates loss-specific information in corresponding sections and manages ICD codes.
>       2.3.1 If ICD code table is in editing mode, the Save button for claim events is disabled until ICD code editing is completed or cancelled.
>    2.4 User reviews Accident vs. Sickness categorization (disabled during case edit, unchangeable).
>    2.5 User saves changes, which updates the Event case, re-triggers auto-claim creation flow, triggers duplicate case/claim validation, and invokes DXP APIs for event cases and customer data.
> 3. For editing Additional Information:
>    3.1 User updates reporting details including Reporting Method, Date Reported (mandatory), Event Date (mandatory), and Event Description (optional, max 1000 characters).
>       3.1.1 If Event Date is later than earliest date of loss, system displays a warning message but allows the date to be saved.
>    3.2 User updates Work Detail information including Employer, Work State, Occupation, Date of Hire, and Class.
>       3.2.1 When Employer is updated or selected, Work State becomes mandatory, Occupation and Class fields become visible and filterable based on employer context, and Date of Hire becomes mandatory.
>       3.2.2 When Class field is updated, related plan dropdown is refreshed with options appropriate to the selected class.
>       3.2.3 On day 1 (initial case creation), Work Detail fields for Employer and Work State are disabled, and Occupation and Class are hidden if no employer is selected.
>    3.3 User updates Contact Information (phone, email, preferences) and Address information (not displayed for day 1 edits).
>    3.4 User saves changes, which invokes DXP API (GET and PUT /cap-adjuster/v1/event-cases) to persist case information.
> 4. User can cancel or close the form at any time.
>    4.1 If user attempts to cancel or close without saving, system displays confirmation modal 'Are you sure you want to close this form?'.
>    4.2 If user confirms, drawer closes without saving changes; if user cancels, drawer remains open.
> 5. System returns user to the Case Overview main screen after successful save.
> 6. If Case Status is 'Closed', editing is disabled and existing data remains pre-populated but cannot be modified.

---

#### Feature: Add Related Case
- **Role**: Claim Adjuster
- **Action**: add, view, edit, and remove related case relationships through the Case Overview interface
- **Value**: linked cases (e.g., multiple claims from a single incident) are properly tracked with full audit history and bidirectional visibility across all related events

**Description:**

> **As a** Claim Adjuster,
> **I want to** add, view, edit, and remove related case relationships through the Case Overview interface,
> **so that** linked cases (e.g., multiple claims from a single incident) are properly tracked with full audit history and bidirectional visibility across all related events.


**Key Capabilities:**

> 1. User initiates related case addition by clicking 'Add Related Case' button on Case Overview, which opens the Case Relationship Drawer.
> 2. User searches for the target case by entering a Case Number in the mandatory search field (max 50 characters).
>    2.1 System provides auto-suggestion displaying first 5 results with Case#, Claim#, and Subject of Claim.
>    2.2 User may click 'View all' to access full search results table showing Case#, Policy#, Subject of Claim, and Status.
>    2.3 User may apply Advanced search filters (Case#, First/Last Name, Customer#, State, City, Zip Code, Policy#, Tax ID, Business Name) to refine results.
> 3. User selects the target case from search results and chooses a Type of Relationship from mandatory dropdown (sourced from CaseRelationshipType lookup).
>    3.1 If Type of Relationship is 'Other', Note field becomes mandatory and user must provide explanation.
>    3.2 For all other relationship types, Note field remains optional.
> 4. User saves the relationship, triggering system validation to prevent self-linking and duplicate relationships.
>    4.1 If validation fails due to self-linking, system displays error and prevents save until different case is selected.
>    4.2 If duplicate relationship detected (same Case1 + Case2 + Type already exists), system displays error and prevents save until user modifies relationship type or selects different case.
> 5. System creates bidirectional relationship by inserting records for both 'From Case' and 'To Case' simultaneously, generates history records for both linked cases tracking Related From Case, Related To Case, Type of Relationship, and Note.
> 6. System displays relationship in Related Cases Table with columns: To Case (hyperlink), Event Date (MM/DD/YYYY + time), Case Status (color-coded badge), Type of Relationship, Note.
> 7. User may edit an existing relationship by clicking 'Edit' action on a table record.
>    7.1 System opens drawer with pre-filled data and displays 'To Case' field as read-only (Case Number search hidden).
>    7.2 User modifies Type of Relationship and/or Note fields, then saves.
>    7.3 System updates relationship records and generates history for both linked cases simultaneously.
> 8. User may delete an existing relationship by clicking 'Delete' action on a table record.
>    8.1 System displays confirmation modal.
>    8.2 Upon confirmation, system performs soft-delete by updating status to 'Deleted' for both linked cases (records not physically removed).
>    8.3 System generates history records documenting deletion for both cases and filters out deleted records from UI display.
> 9. User may click hyperlinked 'To Case' to navigate to related case.
>    9.1 If linked case intake is incomplete, system navigates to Member Form.
>    9.2 If linked case intake is complete, system navigates to Event Case Overview.
> 10. User may click Refresh button to retrieve and display latest relationship data in Related Cases Table.
>    10.1 If claim is closed, Refresh button is hidden and Related Cases Table becomes view-only (no add/edit/delete actions available).
> 11. User may cancel operation at any time during add or edit by clicking 'Cancel' button, triggering confirmation modal; upon confirmation, drawer closes without saving changes and no records or history are created.

---

#### Feature: Create a new Claim manually
- **Role**: Claim Adjuster
- **Action**: manually create a new claim from an existing event case
- **Value**: I can initiate claims processing for coverages or incidents that were not automatically identified or generated by the system

**Description:**

> **As a** Claim Adjuster,
> **I want to** manually create a new claim from an existing event case,
> **so that** I can initiate claims processing for coverages or incidents that were not automatically identified or generated by the system.


**Key Capabilities:**

> 1. User navigates to an existing Event Case in Case Overview.
> 2. User accesses the Case Actions menu and selects the option to create a new claim manually.
> 3. User specifies the claim details including line of business, coverage type, loss description, and applicable policy information.
> 4. System validates the provided information against policy coverage and event case data.
> 5. Upon successful validation, system creates the new claim and associates it with the current event case.
> 6. System generates a unique claim number and updates the case overview to reflect the newly added claim.
> 7. User is redirected to the claim detail screen or returned to the case overview to continue case management activities.

---

### Epic: Case Lifecycle: Status / Substatus

#### Feature: Case Lifecycle: Status / Substatus
- **Role**: Claim Adjuster
- **Action**: manage Event Cases through their complete lifecycle from initiation to closure, including status transitions, sub-status management, and reopening capabilities
- **Value**: claims processing is streamlined, related claims are properly grouped under umbrella Event Cases, and case status accurately reflects business state while preventing premature closure when critical open items exist

**Description:**

> **As a** Claim Adjuster,
> **I want to** manage Event Cases through their complete lifecycle from initiation to closure, including status transitions, sub-status management, and reopening capabilities,
> **so that** claims processing is streamlined, related claims are properly grouped under umbrella Event Cases, and case status accurately reflects business state while preventing premature closure when critical open items exist.


**Key Capabilities:**

> 1. **Initiate Event Case**: User creates new Event Case with required member, policy, and loss event data. System assigns 'Incomplete' status and stores case with unique Event Case Number.
>
> 2. **Submit Event Case for Processing**: User submits incomplete Event Case to advance lifecycle.
>    2.1. System validates all required Event Case data fields.
>    2.2. System evaluates applicability per predefined business rules to determine which claim types are applicable.
>    2.3. System retrieves Policy version data from external policy domain.
>    2.4. Upon successful validation, system transitions status from 'Incomplete' to 'Open'.
>
> 3. **Automated Event Case Finalization**: System automatically executes finalization process after successful submission.
>    3.1. System identifies unique applicable Claim types and Coverages (STD, SMD, LTD, Life, SB) based on applicability evaluation.
>    3.2. System filters out Claim types already generated for this Event Case.
>    3.3. System initiates claim creation process for each applicable claim type.
>    3.4. System executes Claim Automation Flow for each newly created claim.
>    3.5. System transforms and populates data from Event Case to associated Claims and Claim settlements.
>
> 4. **Update Event Case in Draft Mode**: User modifies Event Case details while case remains in Incomplete status. System preserves current 'Incomplete' status without triggering revalidation, allowing iterative data entry.
>
> 5. **Update Open Event Case**: User modifies data on Event Case with 'Open' status.
>    5.1. System reverts status to 'Incomplete' to indicate pending validation.
>    5.2. User must resubmit Event Case to return to 'Open' status.
>    5.3. Resubmission may trigger automated processes (Create, Submit, Finalize commands) based on nature of changes.
>
> 6. **Manage Case Sub-status**: User changes sub-status to provide additional context without altering main lifecycle status (available for Incomplete and Open status only).
>    6.1. System displays sub-status options based on current main status: 'External Info', 'Policy/CEM Info', 'Other' for Incomplete; 'Under Review', 'Specialty Review Needed', 'External Info' for Open.
>    6.2. User selects new sub-status and saves.
>    6.3. System updates sub-status while preserving main status, enabling refined case tracking and routing.
>
> 7. **Close Event Case**: User initiates case closure from Case Overview page via 'I want to' menu.
>    7.1. System displays comprehensive Open Items Review with expandable lists showing: Active Tasks, Active Claims, Unpaid Coverages, Incomplete Payments (hard-stop), Unposted Payments, Unprocessed Balances, Incomplete Premium Waiver Approval Periods (hard-stop).
>    7.2. User selects mandatory Reason (Denied/Withdrawn/Terminated/Closed/Paid/Partially Paid) and enters mandatory closure Note.
>    7.3. System validates no issued payments exist at case or claim level (regular payment, deduction payment, underpayment).
>    7.4. System validates no hard-stop open items exist (Incomplete Payment List, Incomplete Premium Waiver Approval Period List).
>    7.5. If unpaid coverage or unposted payment items exist, system enforces 'Partially Paid' reason selection (except for ATP claims which are exempt).
>    7.6. Upon save, system executes closure sequence: closes associated claims with appropriate reason ('Closed' or 'Partially Paid'), closes the Event Case, completes active CMMN process and related tasks.
>    7.7. System applies UI restrictions to closed case, hiding all add/edit actions except 'Reopen Case', 'View Case Information', and 'Add Case Relationship'.
>
> 8. **Reopen Closed Event Case**: User reopens previously closed case to resume processing.
>    8.1. User selects 'Reopen Case' from 'I want to' menu (only available action on closed case).
>    8.2. User enters mandatory reason for reopening.
>    8.3. System displays confirmation modal requiring explicit user confirmation.
>    8.4. Upon confirmation, system reverts case status to previous status before closure (Incomplete or Open), preserves existing sub-status if set, and re-enables all previously hidden UI actions.
>
> 9. **Post-Lifecycle Navigation**: System displays Case Overview page with current status, sub-status, and appropriate action availability based on lifecycle state. Closed cases display in read-only mode with restricted actions.

---

### Epic: Case Duplication Validation

#### Feature: Case Duplication Validation
- **Role**: Claim Adjuster
- **Action**: review potential duplicate cases identified by the system and, if authorized, override false positive duplication warnings with documented justification
- **Value**: duplicate claims can be identified early and prevented, while legitimate cases flagged incorrectly can proceed without delay

**Description:**

> **As a** Claim Adjuster,
> **I want to** review potential duplicate cases identified by the system and, if authorized, override false positive duplication warnings with documented justification,
> **so that** duplicate claims can be identified early and prevented, while legitimate cases flagged incorrectly can proceed without delay.


**Key Capabilities:**

> 1. Upon accessing Case Overview, system automatically displays a warning alert when case duplicate validation has identified potential matches with scores meeting or exceeding the configured threshold.
> 2. User reviews the warning message indicating possible duplication and accesses detailed duplication information via an actionable hyperlink.
> 3. System presents comprehensive duplication details including:
>    - Subject of Claim information with navigation to customer portfolio
>    - Member identification details
>    - List of potential duplicate cases with individual score breakdowns
>    - Score comparison against threshold for each potential match
> 4. User investigates potential duplicate cases by:
>    - Reviewing score details showing specific matching criteria and point values
>    - Navigating to customer portfolio for Subject of Claim verification
>    - Opening potential duplicate case overviews in separate windows for side-by-side comparison
> 5. If authorized with override privileges, user initiates override process to dismiss false positive duplication warnings.
> 6. System prompts for mandatory override justification through confirmation dialog.
> 7. User provides business reason for override decision and confirms the action.
>    7.1 **Alternate Flow - Cancel Override**: If user cancels the override action, system closes the dialog without saving, retains the warning message on Case Overview, and allows user to close the duplication details drawer.
> 8. Upon successful override submission, system:
>    - Saves override information with audit trail
>    - Removes duplication warning from Case Overview
>    - Refreshes the page and displays success confirmation
>    - Allows case processing to continue without duplication restrictions.

---

### Epic: Claim Events

#### Feature: View/ Edit
- **Role**: Claim Adjuster
- **Action**: view and edit claim events information on a case, including adding new loss types, updating event-specific details, and managing ICD code records
- **Value**: claim events remain accurate and complete throughout the case lifecycle, supporting proper claim adjudication and compliance

**Description:**

> **As a** Claim Adjuster,
> **I want to** view and edit claim events information on a case, including adding new loss types, updating event-specific details, and managing ICD code records,
> **so that** claim events remain accurate and complete throughout the case lifecycle, supporting proper claim adjudication and compliance.


**Key Capabilities:**

> 1. User views the Claim Events section on the case overview page, displaying claim event types, Accident vs. Sickness classification, and ICD code records in a collapsible format.
> 2. When the case status is 'Open' and user has PRIV>CAP>Update Case privilege, user can initiate editing by clicking the Edit button, which opens the Edit Claim Events drawer.
>   2.1. If case status is 'Closed', user can only access a read-only View Details drawer displaying all event information organized by type, with unavailable values shown as '-'.
> 3. User adds new loss types by selecting from available options (Death, Accident, Accelerated Death, Serious Illness, Hospital Services, Dismemberment, ADA - Work Accommodation, Wellness, Absence) via multi-select checkboxes.
>   3.1. Previously selected loss types are greyed out and cannot be unselected; users may only add new types.
>   3.2. If the subject is not the employee, the Absence option is disabled and cannot be selected.
> 4. User completes required information for each selected loss type in expandable loss-specific sections, including event descriptions (optional, max 1000 characters), loss item details, date fields, and other loss-specific attributes.
> 5. User modifies existing loss information such as Accelerated Death life expectancy, death attributes (if associated claim is not closed), or absence work hours (defaulting to 8 for new entries).
> 6. User manages ICD code records by adding, editing, or deleting entries in the ICD Code table, including ICD code, description, primary indicator, and date.
>   6.1. If ICD code table is in editing mode, the Save button is disabled until editing is completed or cancelled.
> 7. User reviews Accident vs. Sickness classification (disabled during edit mode) and ensures all required fields are populated.
> 8. User saves all changes by clicking the Save button, triggering system validation including duplicate case/claim validation.
> 9. System saves updated information, triggers update case workflow, cascades changes to existing Life, CI, and HI claims, and creates new claims for newly added loss types.
> 10. System navigates user back to the case overview main screen displaying updated claim events and ICD records.
> 11. User can refresh claim events data via the Refresh link (disabled during refresh, hidden after case closure) to retrieve the latest information.

---

### Epic: Other Claims

#### Feature: Claim Quick View
- **Role**: Claim Adjuster
- **Action**: view associated claims (TermLife, CI, HI, ACC, Permanent Life) in the Other Claims section, toggle between Claim Cards and Loss View, and navigate to individual claim details
- **Value**: I can quickly assess all related claims for a customer across different coverage types and view them by claim or loss category, enabling efficient case management and decision-making

**Description:**

> **As a** Claim Adjuster,
> **I want to** view associated claims (TermLife, CI, HI, ACC, Permanent Life) in the Other Claims section, toggle between Claim Cards and Loss View, and navigate to individual claim details,
> **so that** I can quickly assess all related claims for a customer across different coverage types and view them by claim or loss category, enabling efficient case management and decision-making.


**Key Capabilities:**

> 1. User opens the Life Case Overview page and views the Other Claims section displaying claim cards for multiple claim types including TermLife, CI (Critical Illness), HI (Hospital Indemnity), ACC (Accident), and Permanent Life claims (Whole Life, Variable Universal Life, etc.).
> 2. Each claim card presents essential information including:
>    2.1. Loss Benefit identifier (claim type and number as a hyperlink).
>    2.2. Loss type and subject of claim (claimant's full name).
>    2.3. Associated policy number and claim manager assignment.
>    2.4. Related event type (Absence) and current claim status with color-coded visual indicators (Incomplete-Gray, Pending-Yellow/Orange, Open-Green, Closed-Blue).
> 3. User navigates to detailed claim information by clicking on a claim number, which opens the claim overview page for the selected claim.
> 4. User toggles between viewing modes:
>    4.1. Claim View: Displays claims as individual cards grouped by claim type.
>    4.2. Loss View: Displays coverage data organized and sorted by different loss types, showing only loss tabs that contain available items.
> 5. System dynamically updates the display based on the selected view mode, ensuring only relevant data and tabs are presented.
> 6. Claim manager information is intelligently displayed based on assignment:
>    6.1. If a user is assigned: Display the user's full name with fallback logic (if first name is blank, hide placeholder; if both names blank, display userId).
>    6.2. If a queue is assigned: Display the queue name.

---

#### Feature: Loss View
- **Role**: Claim Adjuster
- **Action**: view and analyze all coverages organized by loss type in a consolidated tabular format within the Case Overview page, with access to detailed Premium Waiver information, eligibility validation messages, accumulator details, and related claim/policy records
- **Value**: I can efficiently assess all coverages associated with a case grouped by loss type, understand eligibility status, track financial positions, and access detailed supporting information without navigating away from the overview screen

**Description:**

> **As a** Claim Adjuster,
> **I want to** view and analyze all coverages organized by loss type in a consolidated tabular format within the Case Overview page, with access to detailed Premium Waiver information, eligibility validation messages, accumulator details, and related claim/policy records,
> **so that** I can efficiently assess all coverages associated with a case grouped by loss type, understand eligibility status, track financial positions, and access detailed supporting information without navigating away from the overview screen.


**Key Capabilities:**

> 1. User accesses Loss View by toggling from 'Claim View' to 'Loss View' within the Case Overview page.
> 2. System displays all coverages organized into loss-grouped coverage tables with clickable loss type tabs.
>    2.1 Each tab shows loss type name with item count in format '&lt;Loss Type&gt; (&lt;Count&gt;)'.
>    2.2 Loss types are mapped to system entities: Death→DeathLoss, Accelerated Death→AcceleratedLoss, Serious Illness→CILoss, Hospital Services→HILoss, Dismemberment→AccidentalDismembermentLoss, Waiver of Premium→PremiumWaiverLoss.
> 3. System presents coverage data in tabular format with the following columns: Claim (Claim# + Policy# as hyperlinks, sorted alphabetically), Coverage/Eligibility (with tooltip), ICD/CPT Code, Incident Date, Date Range, # Days/# Occurrences, POL Received Date, and financial columns (Gross Amount, Paid, Unpaid with accumulator pop-up).
> 4. User navigates through paginated results with maximum 5 items per page and page jump functionality.
> 5. User accesses linked information through interactive elements:
>    5.1 Clicking Claim# or Policy# hyperlink opens the linked claim or policy detail page in a new browser tab.
>    5.2 Clicking Coverage/Eligibility field with tooltip displays eligibility validation message as defined in eligibility validation specifications.
>    5.3 Clicking financial amount with accumulator indicator displays pop-up showing remaining limits and accumulator details for the selected coverage.
> 6. For Premium Waiver loss types, user expands additional details by clicking the chevron icon to view:
>    6.1 Elimination Period Section (Start Date, End Date, Policy Elimination Period).
>    6.2 Benefit Period Section (Start Date, End Date, Policy Benefit Period, Reserved/Completed/Remaining periods, and Status such as Not Started or In Progress).
>    6.3 Approval Periods Section displaying tabular data with Start Date, End Date, Status, Approver, Date of Status Change, and Note for multiple approval period records.
> 7. For Accident & Health coverages with Burn/Dislocation/Fracture information, system displays Additional Information column with coverage-specific data including Burn Degree, Reduction Type, override indicators, and other relevant metadata.
> 8. All displayed data is view-only, supporting claim lifecycle management, accumulator tracking, and adjudication processes across Accident & Health, Critical Illness, Hospital Indemnity, and Permanent Life claim types.

---

### Epic: Change History

#### Feature: Change History
- **Role**: Claim Adjuster
- **Action**: view, filter, and sort a comprehensive chronological record of all user-initiated changes to Event Cases and Claims
- **Value**: I can audit modifications, understand the evolution of a case or claim, and ensure compliance and accuracy throughout the lifecycle

**Description:**

> **As a** Claim Adjuster,
> **I want to** view, filter, and sort a comprehensive chronological record of all user-initiated changes to Event Cases and Claims,
> **so that** I can audit modifications, understand the evolution of a case or claim, and ensure compliance and accuracy throughout the lifecycle.


**Key Capabilities:**

> 1. User navigates to the Case Overview or Claim Overview UI and opens the 'History' tab to access the change history.
> 2. System retrieves and displays a chronological record of all user-initiated changes in a table format, with newest changes shown first by default (Date and Time descending).
> 3. For Event Cases, the system tracks and displays changes to:
>    3.1. Event Case details, all dependent Claims, settlements, financial adjustments, special handling, case relationships, payment withholdings, case duplicate details, and payments/recoveries.
> 4. For Claims, the system tracks and displays changes to:
>    4.1. Claim and settlement data (including offsets and beneficiaries), special handling, payments/financials.
>    4.2. Relevant Event Case-level changes such as deductions, tax withholdings, and payment inputs.
> 5. System presents all data in business-friendly format by converting lookup codes to readable values, translating entity and attribute names into plain language, and resolving URIs and IDs to meaningful references.
> 6. User applies filters to narrow down history records using:
>    6.1. Component (multi-select filter).
>    6.2. Reference (multi-select filter).
>    6.3. Entity (multi-select filter).
>    6.4. Adjusted by (multi-select filter).
>    6.5. Date range selection for Date and Time column.
> 7. System displays active filter tags for each applied filter, which can be removed individually to adjust the view.
> 8. User sorts columns to reorder history records:
>    8.1. Date and Time column toggles between descending and ascending order.
>    8.2. Component, Reference, Entity, Attribute, and Adjusted by columns toggle between ascending and descending alphabetical order.
>    8.3. Original and New fields are not sortable.
> 9. User clicks on Event Case or Claim numbers displayed as active links to navigate directly to the respective Overview screens.
> 10. User refreshes the history table at any time to retrieve the latest change data from the system.
> 11. System ensures locale-specific formatting (date formats, claim type prefixes for different markets such as UK) is applied to all displayed data.

---
## Initiative: Claim Overview

### Epic: Claim Header

#### Feature: Claim Header Details
- **Role**: Claim Adjuster
- **Action**: view comprehensive claim header information and navigate to related customer, policy, and claim details, including managing special handling flags
- **Value**: I can efficiently access all critical claim information, navigate to related records, and appropriately flag claims requiring special attention in a centralized interface

**Description:**

> **As a** Claim Adjuster,
> **I want to** view comprehensive claim header information and navigate to related customer, policy, and claim details, including managing special handling flags,
> **so that** I can efficiently access all critical claim information, navigate to related records, and appropriately flag claims requiring special attention in a centralized interface.


**Key Capabilities:**

> 1. User accesses Claim Overview page to view comprehensive Claim Header information organized into four main sections: Claim Number (system-generated identifier), Claim Header Information (insured details, event dates, assignee), Subject of Case Information (detailed subject data), and Special Handling status flags.
> 2. System displays claim status using color-coded visual indicators (Gray for Incomplete, Green for Open, Yellow/Orange for Pending, Blue for Closed) with additional sub-status detail for granular tracking.
> 3. User views key claim details including Subject of Claim (insured's name with Customer ID), Date of Loss (earliest if multiple exist), Group Policy/Certificate numbers, Paid To Date (with warning if behind Date of Loss), Claim Manager assignment, Special Handling flags, and ERISA indicator (for CI/HI/Accident claims only).
> 4. User navigates to related records through hyperlinked elements:
>    4.1. Insured Name link navigates to customer details page.
>    4.2. Assignee link navigates to Claim Manager information popup.
>    4.3. Subject of Case link opens subject information popup displaying personal and contact details (Name, Date of Birth, Customer ID, preferred address, phone, email from CEM).
>    4.4. View Detail button navigates to Individual Customer Portfolio in CEM.
>    4.5. Group Policy link opens Master Policy Consolidated View in new browser tab.
>    4.6. Certificate link opens Member Record Consolidated View in new browser tab.
> 5. User manages Special Handling flags by clicking Special Handling hyperlink to open Special Handling drawer with toggle-based interface supporting multiple simultaneous flags (SIU, Appeal, Complaint, Pre-Existing, Policy Exclusion, ATP, ATP With Check, Attorney, Litigation).
>    5.1. If user decides not to make changes, user clicks Cancel or Exit button and system closes drawer without saving changes.
>    5.2. If user completes changes, user clicks Save button and system closes drawer, persists changes, and displays active Special Handling flags on Claim Header.

---

#### Feature: Claim Manager Assignement
- **Role**: Claim Adjuster
- **Action**: have claims automatically assigned upon creation based on authority and workload, and manually reassign claims to users or queues as needed
- **Value**: workload is balanced across the team, claims are managed by authorized personnel, and reassignments can be made efficiently to maintain operational continuity

**Description:**

> **As a** Claim Adjuster,
> **I want to** have claims automatically assigned upon creation based on authority and workload, and manually reassign claims to users or queues as needed,
> **so that** workload is balanced across the team, claims are managed by authorized personnel, and reassignments can be made efficiently to maintain operational continuity.


**Key Capabilities:**

> 1. **Auto-Assignment at Claim Creation**: When a claim is created after intake completion, the system automatically assigns a Claim Manager:
>    1.1. System identifies eligible users with Claim authority type and proper claim authority (via Authority Level or OpenL rules configuration).
>    1.2. System filters out users who are inactive or within an unavailability period.
>    1.3. If no eligible users exist, system assigns claim to default 'Claim Management' queue.
>    1.4. If exactly one eligible user exists, system assigns claim to that user and associates with the queue.
>    1.5. If multiple eligible users exist, system counts active claims (CMMN status = active) for each user and assigns to the user with the smallest workload; in case of tie, assigns to first user in list.
>    1.6. System updates CMMN Claim Manager, Claim Header, and assigns New Claim Task to the selected Claim Manager.
>
> 2. **Display Current Claim Manager**: System displays current Claim Manager information in the Claim Overview Header:
>    2.1. Claim Manager's name appears as a clickable hyperlink (or queue name if assigned to queue).
>    2.2. Link is disabled if claim status is closed; enabled for all other statuses including reopened claims.
>
> 3. **View Claim Manager Details**: User accesses Claim Manager contact information:
>    3.1. User clicks on Claim Manager name hyperlink in Header.
>    3.2. System opens pop-up displaying full name, address, phone numbers, email addresses with preferred contact handling.
>    3.3. System displays contact information with comma separation and truncation with tooltips for overflow.
>    3.4. System displays 'Reassign Claim' button if user has 'Claim: Assign Claims' privilege.
>
> 4. **Initiate Manual Reassignment**: User begins reassignment process:
>    4.1. User clicks 'Reassign Claim' button (requires privileges: PRIV>CAP>Assign Work Case to User AND PRIV>CAP>Assign Work Case to Queue).
>    4.2. System opens Assign Claim form with 'To someone' option selected by default and Assign button disabled until selection made.
>
> 5. **Assign to Individual User**: User assigns claim to a specific claim manager:
>    5.1. User enters minimum 3 characters in assignee search box (case-insensitive).
>    5.2. System displays search results table showing Name (with hover tooltip), Department, and Role(s) sourced from OrganizationalPerson and RoleAccessProfile, filtered to exclude users not in Security MS.
>    5.3. User selects an assignee from results, enabling the Assign button.
>    5.4. User optionally enters Notes in rich text format field.
>    5.5. User clicks Assign button.
>    5.6. System saves assignment via userId, updates Claim Manager in Claim Overview Header, and closes form.
>
> 6. **Assign to Queue**: User assigns claim to a work queue instead of individual:
>    6.1. User selects 'To a Queue' radio button option.
>    6.2. System displays Queue drop-down filtered by sourceCd = CAP.
>    6.3. User selects queue from drop-down, enabling the Assign button.
>    6.4. User optionally enters Notes and clicks Assign.
>    6.5. System saves assignment via queueCd, updates Claim Manager display, and closes form.
>
> 7. **Cancel Reassignment**: User abandons reassignment process:
>    7.1. User clicks Cancel button or attempts to close form.
>    7.2. System displays confirmation modal.
>    7.3. Upon user confirmation, system closes form without saving and returns to Claim Overview with no changes to assignment.

---

### Epic: Special Handling

#### Feature: Special Handling
- **Role**: Claim Adjuster
- **Action**: view and manage special handling flags on a claim directly from the Claim Overview page
- **Value**: claims requiring special attention or procedures are properly identified, tracked, and handled according to business policies and regulatory requirements

**Description:**

> **As a** Claim Adjuster,
> **I want to** view and manage special handling flags on a claim directly from the Claim Overview page,
> **so that** claims requiring special attention or procedures are properly identified, tracked, and handled according to business policies and regulatory requirements.


**Key Capabilities:**

> 1. User accesses the Claim Overview page where the Claim Header displays comprehensive claim information including claim number, status, subject of claim, loss date, policy details, and active special handling flags.
> 2. System displays special handling flags in the Claim Header, showing only currently active flags with hover functionality to reveal the full list of available flags.
> 3. User clicks the Special Handling hyperlink in the Claim Header to open the Special Handling management drawer.
> 4. System presents the Special Handling modal interface allowing user to view current flag status and toggle flags on or off.
> 5. User selects or deselects one or multiple special handling flags based on claim circumstances.
>    5.1. Flags available for manual management include: SIU, Appeal, Complaint, Pre-Existing, Policy Exclusion, ATP, ATP with Check, Attorney, and Litigation.
>    5.2. Display-only flags (Reinsurance, Salvage, Subrogation) are visible but not editable.
> 6. User saves changes by clicking the Save button, causing the system to persist flag updates and refresh the Claim Header display.
>    6.1. Alternate: User clicks Cancel or Exit form button, causing the system to close the drawer without saving any changes.
> 7. System updates the Claim Header to reflect the current set of active special handling flags immediately upon save.

---

### Epic: Fraud check / Duplicate Claim check

#### Feature: Fraud check / Duplicate Claim check
---

### Epic: Beneficiaries

#### Feature: View / Add / Edit Beneficiary details
- **Role**: Claim Adjuster
- **Action**: view, add, edit, and configure beneficiary designations with coverage allocations, guardian assignments, and payment details for Life & Annuity claims
- **Value**: accurate beneficiary information is maintained, coverage allocations comply with policy terms, and payment distributions can be executed correctly to the appropriate payees

**Description:**

> **As a** Claim Adjuster,
> **I want to** view, add, edit, and configure beneficiary designations with coverage allocations, guardian assignments, and payment details for Life & Annuity claims,
> **so that** accurate beneficiary information is maintained, coverage allocations comply with policy terms, and payment distributions can be executed correctly to the appropriate payees.


**Key Capabilities:**

> 1. User navigates to Claim Overview page and accesses the Beneficiaries section, which displays auto-populated policy beneficiaries with warning indicators for beneficiaries without coverage assignments.
> 2. User initiates beneficiary addition process and selects beneficiary from available parties (member, dependent, or other individual/organization).
>    2.1 When subject of claim is the member himself, user can select any party as beneficiary, choose multiple coverages, and assign allocation percentages with system auto-calculating benefit amounts.
>    2.2 When subject of claim is a dependent (spouse or child), system restricts beneficiary selection to the member as default, auto-fills member details, and sets default beneficiary type as Primary with 100% allocation.
>    2.3 When beneficiary is an 'Other' party not in the system, user creates new individual or organization party record, which is then available for beneficiary assignment.
> 3. User optionally assigns guardian or representative payee to a beneficiary, with system validating that guardian is a different party and pre-populating payment details from guardian information.
> 4. User configures beneficiary designation details including beneficiary type, coverage selection, and allocation percentage per coverage, with system auto-calculating corresponding benefit amounts.
> 5. System validates that combined allocation percentages for beneficiaries of the same type under the same coverage do not exceed 100%, preventing over-allocation.
> 6. User edits existing beneficiary information to update personal details, guardian assignment, or payment methods.
>    6.1 When beneficiary designation-related coverage has associated payment schedules or payments, system restricts modification of coverage selection and allocation percentage fields to maintain payment integrity.
> 7. User removes beneficiaries who have no associated payment schedules or payments; system hides remove functionality for beneficiaries or guardians with existing payment records.
> 8. System saves all beneficiary configurations, updates the Beneficiaries table with coverage assignments, and displays guardian indicators where applicable, preparing the claim for payment processing.

---

### Epic: no content

#### Feature: ICD codes
- **Role**: Claim Adjuster
- **Action**: manage ICD codes on claims including defaulting from Event Case, adding, editing, deleting, and validating diagnosis information for TL/ACC/CI/HI/WL/VUL claim types
- **Value**: accurate diagnosis information is maintained on claims to support proper claim adjudication and regulatory compliance

**Description:**

> **As a** Claim Adjuster,
> **I want to** manage ICD codes on claims including defaulting from Event Case, adding, editing, deleting, and validating diagnosis information for TL/ACC/CI/HI/WL/VUL claim types,
> **so that** accurate diagnosis information is maintained on claims to support proper claim adjudication and regulatory compliance.


**Key Capabilities:**

> 1. System automatically defaults ICD Codes and Accident vs. Sickness classification from Event Case to newly created Claims as a one-time, one-direction data copy at the moment of claim creation (applies to both automatic creation during Event Case intake and manual creation via 'I want to' menu).
>    1.1. If ICD Code or Accident vs. Sickness data is updated on Event Case after claim creation, changes are NOT reflected on already created claims.
>    1.2. If ICD Code data is updated directly on the Claim, changes are NOT reflected back on the Event Case.
> 2. User accesses the ICD Codes section on Claim Overview page to view all diagnosis codes associated with the claim in a structured table displaying ICD Code, Description, Primary indicator, Diagnosis Date, and available actions.
> 3. User adds new ICD Codes to the claim by providing required diagnosis information including code selection, optional primary designation, and diagnosis date.
> 4. User edits existing ICD Codes to update diagnosis information, change primary designation, or modify diagnosis dates as clinical information is clarified.
>    4.1. If validation errors are detected during edit (duplicate code, multiple primary codes, no primary code, or future diagnosis date), system displays appropriate error messages and prevents saving until corrected.
> 5. User deletes non-primary ICD Codes that are no longer applicable to the claim (deletion of primary codes is restricted when other non-primary codes exist to enforce business rules).
> 6. System validates all ICD Code operations against business rules to ensure data integrity: uniqueness of codes, single primary designation, at least one primary code exists, and diagnosis dates are not in the future.

---

### Epic: Claim Actions ("I want to")

#### Feature: Policy Refresh
- **Role**: Claim Handler
- **Action**: refresh claim data when a new policy version becomes available
- **Value**: the claim accurately reflects the most current policy terms, eligibility rules, and benefit schedules, ensuring correct benefit calculations and payments

**Description:**

> **As a** Claim Handler,
> **I want to** refresh claim data when a new policy version becomes available,
> **so that** the claim accurately reflects the most current policy terms, eligibility rules, and benefit schedules, ensuring correct benefit calculations and payments.


**Key Capabilities:**

> 1. Claim handler initiates policy refresh from the Claim Overview page when the claim is in 'Pending' or 'Open' status.
> 2. System validates whether a new policy version exists based on the claim's Date of Loss (DOL).
>    2.1 If no new policy version is found, system notifies the user and allows them to return to the Claim Overview page without making changes.
>    2.2 If a new policy version is found, system presents the version number and prompts for confirmation to proceed.
> 3. User reviews the policy version notification and decides to proceed or cancel.
>    3.1 User may access a detailed comparison view of the latest and previous policy versions via a provided link before confirming.
>    3.2 If user cancels, they return to the Claim Overview page and no refresh is executed.
> 4. Upon confirmation, system triggers the policy refresh workflow, which recalculates claim eligibility, benefits, and payments based on updated policy information.
> 5. System applies policy changes affecting eligibility rules (e.g., waiting periods, incurral periods), benefit calculations (e.g., plan changes, benefit schedules, age reduction, maximums), and payment details (e.g., beneficiary updates).
> 6. System generates payment balance adjustments as necessary while preserving any manually overridden values on the claim.
> 7. Claim data is updated to reflect the new policy version, and the claim remains accessible for further processing.

---

#### Feature: Change Claim Sub-status
- **Role**: Claim Handler
- **Action**: update the substatus of an existing claim based on its current main status
- **Value**: the claim's processing stage is accurately tracked and categorized, enabling better workflow management and reporting

**Description:**

> **As a** Claim Handler,
> **I want to** update the substatus of an existing claim based on its current main status,
> **so that** the claim's processing stage is accurately tracked and categorized, enabling better workflow management and reporting.


**Key Capabilities:**

> 1. Claim handler accesses the Change Claim Substatus modal drawer from the claim actions menu for an existing claim with Status = Pending or Open.
> 2. The system displays the current claim information and presents a substatus dropdown populated with options relevant to the claim's current main status:
>    2.1. If claim status is Pending, available substatus options are: Additional POL, Policy Information, Future Claim.
>    2.2. If claim status is Open, available substatus options are: Internal Review, SIU, Payment Scheduled.
>    2.3. If claim status is Closed, the Change Substatus function is disabled and not accessible.
> 3. Claim handler selects the appropriate substatus from the dropdown menu reflecting the current processing stage.
> 4. Claim handler saves the substatus change, which persists the selected value to the claim record (CapLoss.lossSubStatusCd) and closes the modal drawer.
> 5. Alternatively, claim handler may cancel or close the drawer without saving, which dismisses the interface and preserves the original substatus value.

---

#### Feature: Claim Closure
- **Role**: Claim Adjuster
- **Action**: close an existing claim after resolution
- **Value**: the claim lifecycle is properly concluded, work items are completed, and the claim status accurately reflects its finalized state for reporting and compliance purposes

**Description:**

> **As a** Claim Adjuster,
> **I want to** close an existing claim after resolution,
> **so that** the claim lifecycle is properly concluded, work items are completed, and the claim status accurately reflects its finalized state for reporting and compliance purposes.


**Key Capabilities:**

> 1. User initiates claim closure by selecting the close claim action for an existing claim with valid identification information.
> 2. System validates the closure request including performer privileges and claim existence.
> 3. System verifies that claim closure is permitted from the current claim status according to configured lifecycle rules.
>    3.1 If closure is not permitted from the current status, system prevents the action and notifies the user with an appropriate error message, and the process terminates.
> 4. System updates the claim status to Closed upon successful validation.
> 5. System triggers business activity monitoring for the claim closure event.
> 6. System completes associated work management case and tasks linked to the claim.
> 7. System returns the updated claim information confirming the closure.

---

#### Feature: Claim Automatic Closure (Auto-adjudication)
- **Role**: System
- **Action**: automatically close eligible claims and their associated event cases upon payment schedule completion
- **Value**: manual intervention is minimized and claims processing efficiency is improved while maintaining control and accuracy through defined eligibility rules

**Description:**

> **As a** System,
> **I want to** automatically close eligible claims and their associated event cases upon payment schedule completion,
> **so that** manual intervention is minimized and claims processing efficiency is improved while maintaining control and accuracy through defined eligibility rules.


**Key Capabilities:**

> 1. System initiates the auto-closure process when a payment schedule is completed.
> 2. System evaluates whether claims and event cases meet auto-closure criteria:
>    2.1 For claims: verifies claim is in 'Open' state, all related coverages (settlements) are in 'Approved' state, and all related coverages were auto-adjudicated.
>    2.2 For event cases: verifies all claims within the event case meet the auto-closure criteria.
>    2.3 If auto-closure criteria are not met, the process terminates without further action.
> 3. System validates closure eligibility by checking operational readiness:
>    3.1 Confirms at least one related payment exists.
>    3.2 Verifies all related payments are in 'Issued' state.
>    3.3 Checks that no payee balances are in over-payment or under-payment status.
>    3.4 Validates all related automated processes are completed.
>    3.5 Confirms all related tasks are completed (excluding 'New Case' and 'New Claim' tasks).
>    3.6 If closure eligibility rules are not met, the system generates a user task titled 'Auto Adjudication Closure Failed' to notify users for manual intervention, and the process terminates.
> 4. System closes all eligible claims that passed both criteria and eligibility validation.
> 5. System evaluates whether the parent event case can be closed:
>    5.1 Checks if all claims within the event case are now closed.
>    5.2 If not all claims are closed, the process terminates and the event case remains open.
> 6. System closes the event case when all associated claims are confirmed closed, completing the auto-closure process.

---

### Epic: Claim Lifecycle

#### Feature: Claim Lifecycle
- **Role**: Claim Adjuster
- **Action**: manage the complete claim lifecycle through a centralized action menu, including submitting, closing, reopening claims, updating substatuses, refreshing policy data, and creating follow-up tasks
- **Value**: I can efficiently perform all critical claim operations from a single interface, ensuring accurate claim processing, proper status tracking, and timely policy updates without navigating multiple screens

**Description:**

> **As a** Claim Adjuster,
> **I want to** manage the complete claim lifecycle through a centralized action menu, including submitting, closing, reopening claims, updating substatuses, refreshing policy data, and creating follow-up tasks,
> **so that** I can efficiently perform all critical claim operations from a single interface, ensuring accurate claim processing, proper status tracking, and timely policy updates without navigating multiple screens.


**Key Capabilities:**

> 1. User accesses the 'I want to' action menu from the top right of the Claim Overview page to view all available claim lifecycle actions.
> 2. User can submit a claim for processing, triggering the claim submission workflow.
> 3. User can close a claim following established closure protocols and business rules.
> 4. User can reopen a previously closed claim:
>    4.1 System presents a drawer interface for reopening.
>    4.2 User selects a reason code and provides reason details.
>    4.3 Upon reopening, system clears the sub-status to 'N/A'.
>    4.4 User gains ability to reassign the reopened claim to appropriate party.
> 5. User can manually update claim substatus:
>    5.1 System presents substatus change drawer.
>    5.2 Action is disabled for claims in 'Closed' status.
> 6. User with appropriate privileges can create follow-up tasks for closed claims:
>    6.1 Action is only available when claim status is 'Closed'.
>    6.2 User selects task type and inputs note details through task drawer.
> 7. User with policy refresh privileges can refresh policy data:
>    7.1 System checks for new policy versions based on Date of Loss.
>    7.2 If no new version exists, system displays notification modal.
>    7.3 If new version exists, system presents confirmation modal with version details.
>    7.4 Upon confirmation, system executes policy refresh workflow which may impact payments and generate balance adjustments.
> 8. User can save or cancel any drawer-based action before submission.
> 9. Upon completion of any action, system returns to Claim Overview page with updated status and sub-status information.

---

### Epic: Policy Summary

#### Feature: Policy Summary
- **Role**: Claim Adjuster
- **Action**: view comprehensive policy information including coverages, insureds, exclusions, and limitations within the Claim UI
- **Value**: I have immediate access to all relevant policy details needed to make informed claim processing decisions without navigating away from the claim context

**Description:**

> **As a** Claim Adjuster,
> **I want to** view comprehensive policy information including coverages, insureds, exclusions, and limitations within the Claim UI,
> **so that** I have immediate access to all relevant policy details needed to make informed claim processing decisions without navigating away from the claim context.


**Key Capabilities:**

> 1. System displays the Policy Summary component on the Claim Overview page as an integrated part of the Claim UI interface.
> 2. Component presents comprehensive policy information including:
>    2.1 Policy coverages applicable to the claim.
>    2.2 List of insureds under the policy.
>    2.3 Policy exclusions that may affect claim eligibility.
>    2.4 Policy limitations that constrain coverage amounts or conditions.
> 3. Policy information is displayed in read-only format to support claim processing decisions.
> 4. All policy data presented is contextually relevant to the active claim being processed.
> 5. Component provides immediate visibility into policy terms without requiring navigation to external policy management systems.

---

### Epic: Reserving

#### Feature: Reserving
---
## Initiative: Claim Adjudication Benefit Calculations

### Epic: Face Values

#### Feature: Face Values
- **Role**: Claim Adjuster
- **Action**: view, edit, override, and manage face value and benefit amounts across TL, CI, and Accident claims with age reduction rules and policy-based calculations
- **Value**: accurate benefit calculations are maintained, special circumstances can be accommodated through overrides, and claim financial determinations reflect both automated policy data and adjuster expertise

**Description:**

> **As a** Claim Adjuster,
> **I want to** view, edit, override, and manage face value and benefit amounts across TL, CI, and Accident claims with age reduction rules and policy-based calculations,
> **so that** accurate benefit calculations are maintained, special circumstances can be accommodated through overrides, and claim financial determinations reflect both automated policy data and adjuster expertise.


**Key Capabilities:**

> 1. System automatically retrieves and displays face value and benefit amount data from policy upon claim creation with open status, presenting product-specific cards (TL Face Value Card, CI Face Value Card, or Accidental Death Benefit Card) on the Claim Overview page.
> 2. System determines and applies age reduction by calculating member's current age based on Date of Loss and comparing against policy's age reduction schedule, displaying 'Age Reduction Applied' flag with informational tooltip when applicable.
> 3. System calculates and displays face value amounts using product-specific and benefit-type-specific logic:
>    3.1. For TL claims with Multiple of Salary benefit type: displays annual covered earnings, multiplier, and auto-calculated face value when data is available from policy.
>    3.2. For TL claims with Percent of Employee Amount benefit type: calculates dependent face value based on member's face value and percentage rules.
>    3.3. For CI claims with Range Values or Multiple Values benefit type: prompts for manual face value entry when policy data cannot provide specific amount.
>    3.4. For Accident claims: calculates Accidental Death Benefit based on child organized sport indicator and member's age reduction factor.
> 4. Adjuster manages missing data required for face value calculation:
>    4.1. When annual covered earnings is missing for Multiple of Salary benefit type, system displays warning alert and enables 'Edit Annual Covered Earnings' action while disabling override capability.
>    4.2. Adjuster inputs missing annual covered earnings, triggering automatic face value calculation and enabling override functionality.
>    4.3. When benefit amount is missing for dependent claims or specific benefit types, adjuster uses 'Edit Face Value' action with context-sensitive prompts to input required member or subject-of-claim face value.
> 5. Adjuster overrides face value or benefit amount when business circumstances require deviation from calculated values:
>    5.1. Adjuster selects 'Override Face Value' action from action list and inputs adjusted amount in override pop-up.
>    5.2. System saves override, sets override flag, displays overridden amount on card with original value indicator, and protects overridden value from automatic recalculation during policy re-integration and claim updates.
> 6. Adjuster undoes face value override to revert to system-calculated amount:
>    6.1. Adjuster selects 'Undo Override Face Value' action and confirms intent in confirmation modal.
>    6.2. System reverts face value to latest calculated value, removes override flag and original value indicator, clears override flag, and displays success confirmation.
> 7. System triggers recalculation of coverage gross amounts when face value or annual covered earnings updates impact downstream financial calculations.
> 8. System maintains override protection rules ensuring that once override is active, face value recalculation is skipped during event case update processes, policy re-integration, and claim update workflows, while continuing to sync other policy information such as age reduction rule changes.

---

#### Feature: Face Values (IPL)
- **Role**: Claim Adjuster
- **Action**: view and manage face value information for Whole Life (WL) and Variable Universal Life (VUL) product claims, including age reduction calculations and benefit type variations
- **Value**: accurate death benefit calculations are automatically determined and displayed based on policy data, member age, and product-specific benefit rules

**Description:**

> **As a** Claim Adjuster,
> **I want to** view and manage face value information for Whole Life (WL) and Variable Universal Life (VUL) product claims, including age reduction calculations and benefit type variations,
> **so that** accurate death benefit calculations are automatically determined and displayed based on policy data, member age, and product-specific benefit rules.


**Key Capabilities:**

> 1. System automatically retrieves and displays face value financial data from the Policy system when a WL/VUL claim is created with open status.
> 2. System calculates whether age reduction applies by comparing the member's age at Date of Loss (DOL) against the policy's age reduction schedule.
>   2.1 When age reduction applies, system displays 'Age Reduction Applied' flag on the Face Value card with an informational tooltip explaining 'Reduce from Original Face Value'.
>   2.2 When age reduction does not apply, the flag is not displayed on the card.
> 3. System displays benefit type information retrieved from policy data (deathBenefitOption) on the WL/VUL Face Value card, including Face Amount Plus Cash Value, Max Of Face Amount And Cash Value, or Face Amount Only.
> 4. System adjusts face value display logic based on loss type and subject of claim.
>   4.1 When loss type is Death and Subject of Claim is Member, system displays the WL/VUL Face Value card with face value amount and benefit type with no user management actions available.
>   4.2 When Subject of Claim is not Member, system retrieves Face Value as Cash Account from policy integration (VUL products are only available for primary insured/member).
>   4.3 When loss type is Accelerated Death, system integrates with Cash management based on 'POL Received Date' to determine benefit amount when settlement is adjudicated and coverage is saved successfully.
> 5. System triggers automatic recalculation of face value when there are impacts on coverage's Gross Amount calculation, such as manual overrides.
> 6. User can view all face value information on the Claim Overview page with appropriate visual indicators for age reduction and benefit type configurations.

---

#### Feature: Age Reduction
- **Role**: Claim Adjuster
- **Action**: view and verify the accurate face value or accidental death amount on the claim overview page, with product-specific age reduction rules automatically applied based on the associated product line
- **Value**: benefit calculations are accurate, compliant with product-specific rules, and claims are adjudicated correctly according to policy terms

**Description:**

> **As a** Claim Adjuster,
> **I want to** view and verify the accurate face value or accidental death amount on the claim overview page, with product-specific age reduction rules automatically applied based on the associated product line,
> **so that** benefit calculations are accurate, compliant with product-specific rules, and claims are adjudicated correctly according to policy terms.


**Key Capabilities:**

> 1. System identifies the product line associated with the claim upon accessing the claim overview page.
> 2. System routes face value calculation logic to the appropriate product-specific engine based on product line identification.
>    2.1 For Term Life (GTL) claims: System applies Term Life specific age reduction rules and face value variation logic as defined in GTL product specifications.
>    2.2 For Critical Illness (CI) claims: System applies Critical Illness specific age reduction rules and face value variation logic as defined in CI product specifications.
>    2.3 For Individual Permanent Life (IWL) claims: System applies Individual Permanent Life specific age reduction rules and face value variation logic as defined in IWL product specifications.
>    2.4 For Accident (AH) claims: System applies Accident-specific rules and displays 'Accidental Death Amount' instead of standard face value, following AH product specifications.
> 3. System calculates the applicable face value or accidental death amount by applying age-based reduction schedules to the original benefit amount.
> 4. System displays the calculated face value variation or accidental death amount on the claim overview page in a clear, accessible format.
> 5. Claim adjuster reviews the displayed face value information to verify accuracy and support adjudication decisions.

---

### Epic: Accumulators

#### Feature: Configure Accumulators
- **Role**: Claims Adjuster
- **Action**: configure and manage accumulators that track and control payable amounts for coverages throughout the claim lifecycle across Term Life, Critical Illness, Hospital Indemnity, and Accident products
- **Value**: gross amounts are automatically calculated within policy limits, ensuring accurate benefit payments and preventing overpayment while maintaining real-time visibility of used, reserved, and remaining benefit amounts

**Description:**

> **As a** Claims Adjuster,
> **I want to** configure and manage accumulators that track and control payable amounts for coverages throughout the claim lifecycle across Term Life, Critical Illness, Hospital Indemnity, and Accident products,
> **so that** gross amounts are automatically calculated within policy limits, ensuring accurate benefit payments and preventing overpayment while maintaining real-time visibility of used, reserved, and remaining benefit amounts.


**Key Capabilities:**

> 1. **Accumulator Initialization and Configuration**
>    1.1 System creates accumulators upon coverage addition (Confirm button) for non-time-period-restrained and non-dynamic-group-limit accumulators (e.g., per policy, per confinement) with initial state: Reserve=0, Used=0, Remaining=Limit.
>    1.2 System generates accumulators upon coverage save (Save button) for time-period-restrained accumulators (e.g., per calendar year, per benefit year) or dynamic group limit accumulators (e.g., per event per group of Fracture/Dislocation) with initial limit amount for Subject of Claim.
>    1.3 System supports accumulator types across product lines: Term Life (Per Individual, Group Death Limit for master/certificate policies with Basic/Voluntary coverage labels), Critical Illness (Per Event, Per Benefit Year, Per Calendar Year, Per Lifetime Per Individual, Per Policy for master/certificate), Hospital Indemnity (Per Benefit Year, Per Confinement for master/certificate), and Accident (Per Event, Per Calendar Year, Per Lifetime Per Individual for master/certificate).
>    1.4 System calculates and displays gross amount limited by remaining amount in UI popup during coverage addition and save operations.
>
> 2. **Settlement Approval and Reservation**
>    2.1 When coverage is saved as eligible and settlement is approved, system executes Reserve action to move amount from Remaining to Reserve, resulting in: Reserve=allocationGrossAmount, Used=0, Remaining=Limit-allocationGrossAmount.
>    2.2 System applies gross amount calculation formula for TL/CI/HI/Accident: MIN(Coverage Calculated Amount, Claim Coverage Remaining, Group Remaining) to ensure displayed Gross Amount reflects actual maximum claimable amount from accumulator.
>
> 3. **Payment Lifecycle Management**
>    3.1 Upon payment issuance, system executes Use action to move reserved amount to used amount: Reserve=0, Used=allocationGrossAmount, Remaining=Limit-allocationGrossAmount.
>    3.2 When payment is cancelled, system executes Clear action to return used/reserved amount to remaining amount: Reserve=0, Used=0, Remaining=Gross Amount.
>    3.3 When payment is declined, voided, or stopped, system executes Recover, Clear, and Reserve actions to return used amount to reserved amount: Reserve=allocationGrossAmount, Used=0, Remaining=Limit-allocationGrossAmount.
>
> 4. **Coverage Modification Handling**
>    4.1 When coverage is set to non-eligible, system executes Clear action to move reserved amount to remaining amount: Reserve=0, Used=0, Remaining=Gross Amount.
>    4.2 When coverage is cancelled, system executes Clear action for both single and group accumulators to move reserved amount to remaining amount.
>    4.3 For dynamic group limit accumulators (e.g., Death Group, Dislocation/Fracture Group), system adjusts group limit by filtering out settlements with isSettlementCancelled=True and recalculates based on remaining active coverages with maximum benefit amounts.
>
> 5. **Face Value Override and Adjustment**
>    5.1 When Face Value is overridden, system executes Adjust, Clear, and Reserve actions in sequence: first adjusts Remaining Limit, then clears Reserve Amount of coverage/settlement, finally re-reserves based on latest approved settlement.
>    5.2 System updates accumulator values to: Used=0, Reserve=latest settlement Gross Amount, Remaining=latest Limit-latest Gross Amount.
>
> 6. **Recovery and Withholding Operations**
>    6.1 When recovery is performed, system executes Recover action (Used → Reserve) followed by Clear action (Reserve → Remaining).
>    6.2 When payment withholding is performed, system executes Recover action (Used → Reserve) followed by Clear action (Reserve → Remaining).
>
> 7. **Accumulator Value Calculation and Display**
>    7.1 System calculates Limit based on group limits (Policy Face Value or maximum benefit amount among coverage groups for dynamic limits) or individual limits (policy's Maximum Benefit Amount using maxBenefitAmountPct × faceValue or maxBenefitNumber).
>    7.2 System calculates Planned (Reserve) as Gross Amount or #Days/#Occurrences when settlement is approved, with special handling for Coma (TL): whole months + (remaining days/30), rounded to 2 decimals.
>    7.3 System calculates Used as Total Allocation Amount of issued payments, with special handling for Coma (TL): Total Period (months) of issued payment within claim, and for non-Money units with beneficiary payee: Used = Allocation Amount / Unit Amount.
>    7.4 System calculates Limit Remaining using formula: Limit - Planned - Used, displaying 0 or $0 in UI if Planned exceeds limit (backend stores negative value).
>    7.5 System persists all accumulator transactions as records with six action types: Create, Reserve, Use, Recover, Clear, and Adjust.
>
> 8. **Special Coverage Support**
>    8.1 System supports unverified master policy with one coverage per product: Term Life Death Benefit, Accident Coma, HI Ambulance Ground Benefit, CI Hospital Admission.
>    8.2 System handles special coverages claimed once with accidental/death benefit using formula: Min(ADD Face Value × benefit percentage, maxBenefitAmount) for coverages including SeatBeltBenefit, AirBagBenefit, CommonCarrierBenefit, SpouseTrainingBenefit.

---

#### Feature: View accumulator remaining
- **Role**: Claim Adjuster
- **Action**: view detailed accumulator remaining limit information for specific coverages during claim adjudication
- **Value**: I can accurately assess available benefit limits, planned reserves, and amounts already paid to make informed settlement decisions and prevent overpayments

**Description:**

> **As a** Claim Adjuster,
> **I want to** view detailed accumulator remaining limit information for specific coverages during claim adjudication,
> **so that** I can accurately assess available benefit limits, planned reserves, and amounts already paid to make informed settlement decisions and prevent overpayments.


**Key Capabilities:**

> 1. User accesses the Claim Overview page and selects a specific coverage to view accumulator details.
> 2. System displays a pop-up presenting comprehensive remaining limit information structured by limit level (fixed as 'PER LIFETIME PER INDIVIDUAL' for GTL products).
> 3. System calculates and displays five core accumulator metrics:
>    3.1 Limit Amount - determined by coverage type and product-specific configuration rules
>    3.2 Used Amount - total successfully paid amount for the policy
>    3.3 Planned Amount - reserved amount updated when settlement is approved
>    3.4 Unit Amount - formatted as $A/B (e.g., $500/Time) or N/A if not configured
>    3.5 Limit Remaining Amount - calculated as (Limit - Planned - Used)
> 4. System applies product-specific calculation logic based on coverage type:
>    4.1 For GTL Death Coverage: Limit Amount uses latest override face value; additional GROUP DEATH LIMIT section bundles death and accelerated death coverages
>    4.2 For GTL Accelerated Death Coverage: Limit Amount calculated as fixed amount OR percentage of latest override face value
>    4.3 For GTL Other Coverages (SeatBelt, AirBag, CommonCarrier, etc.): Limit Amount determined as minimum of fixed amount and percentage of face value
>    4.4 For TL Coma Benefit: Used Amount displays total months paid; Unit Amount calculated as Gross Amount/Month; Planned Amount calculated as (End Date - Beginning Date + 1) / 30 rounded to 2 decimals
> 5. System handles over-limit scenarios by displaying zero values in UI (0 or $0) for Limit Remaining when Planned exceeds Limit, while storing actual negative values in backend.
> 6. For GTL Death Coverage, system displays additional GROUP DEATH LIMIT section showing bundled accumulator information for death and accelerated death coverages combined.

---

#### Feature: Accumulator Transaction History
- **Role**: Claim Adjuster
- **Action**: view comprehensive accumulator transaction history for Single and Group accumulators associated with a claim
- **Value**: I can accurately track and verify all accumulator-related transactions, ensuring correct benefit calculations and maintaining transparency in claim adjudication decisions

**Description:**

> **As a** Claim Adjuster,
> **I want to** view comprehensive accumulator transaction history for Single and Group accumulators associated with a claim,
> **so that** I can accurately track and verify all accumulator-related transactions, ensuring correct benefit calculations and maintaining transparency in claim adjudication decisions.


**Key Capabilities:**

> 1. User accesses the Accumulator Transaction History function from the Coverage list on the Claim Overview page via a three-dot menu action.
> 2. System retrieves and displays accumulator transaction data filtered by Policy ID and Subject of Claim, excluding technical system transactions that are not relevant to benefit adjudication.
> 3. System presents transaction history in two separate tables—one for Single Accumulators and one for Group Accumulators—to clearly distinguish between individual and shared benefit limits.
> 4. Each transaction history table displays key transaction information including transaction date and time, associated case and claim numbers, transaction description, transaction amount with appropriate formatting (monetary or unit-based), unit type (Day or Money), and extension information (date ranges for Calendar/Benefit Year accumulators or indicators for Group/Premium Waiver accumulators).
> 5. User reviews paginated transaction records (5 rows per page) with sortable columns, defaulting to latest-to-earliest transaction date order, to analyze accumulator usage patterns and verify benefit calculations.
>    5.1 If an accumulator is configured as Per Benefit/Calendar Year and spans multiple calendar or benefit years, system displays separate transaction history tables for each individual year period to maintain year-specific tracking and compliance.
> 6. User closes the transaction history drawer to return to the Claim Overview page and continue claim adjudication activities.

---
## Initiative: Claim Adjudication

### Epic: Claim level Adjudication

#### Feature: Override non-eligible claim
- **Role**: Claim Adjuster
- **Action**: identify claims that have failed eligibility validation at the claim level and override the non-eligible result when business justification exists
- **Value**: claims with valid business reasons can proceed through adjudication despite failing automated eligibility checks, ensuring legitimate claims are not incorrectly denied

**Description:**

> **As a** Claim Adjuster,
> **I want to** identify claims that have failed eligibility validation at the claim level and override the non-eligible result when business justification exists,
> **so that** claims with valid business reasons can proceed through adjudication despite failing automated eligibility checks, ensuring legitimate claims are not incorrectly denied.


**Key Capabilities:**

> 1. System executes eligibility validation at the claim level after claim submission.
> 2. When a claim fails eligibility validation, system displays a visual indicator (yellow exclamation mark) on the claim card within the Claim Overview page.
> 3. Adjuster reviews the claim details and eligibility failure reason to determine if override is appropriate.
> 4. When override is justified, adjuster accesses the override eligibility result functionality to manually override the non-eligible validation result.
> 5. System records the override decision and allows the claim to proceed through the adjudication process despite the failed validation.
> 6. Overridden claim continues through normal claim processing workflow with override status documented.

---

#### Feature: Claim Eligibility
- **Role**: Claim Adjuster
- **Action**: process claim eligibility evaluation through the OpenL rules engine for leave and statutory maternity pay settlement results
- **Value**: eligibility determinations are automated, consistent, and communicated through standardized outbound messages, reducing manual review time and ensuring compliance with business rules

**Description:**

> **As a** Claim Adjuster,
> **I want to** process claim eligibility evaluation through the OpenL rules engine for leave and statutory maternity pay settlement results,
> **so that** eligibility determinations are automated, consistent, and communicated through standardized outbound messages, reducing manual review time and ensuring compliance with business rules.


**Key Capabilities:**

> 1. System evaluates claim eligibility for settlement results through the OpenL rules engine.
> 2. System processes eligibility evaluation for Capitalized Leave Settlement Results (CapLeaveSettlementResult).
> 3. System processes eligibility evaluation for Statutory Maternity Pay Settlement Results (CapSMPSettlementResult).
> 4. System applies configured business rules during eligibility evaluation to determine claim qualification status.
> 5. System generates outbound messages based on eligibility evaluation outcomes.
> 6. System transmits outbound messages to communicate eligibility determination results to downstream systems and stakeholders.
> 7. **Alternate Flow - Connection Error**: If system cannot access eligibility evaluation components due to API connectivity issues, the evaluation process is blocked and requires retry or manual intervention.

---
## Initiative: Coverage Adjudication

### Epic: Coverages

#### Feature: Coverage Adjudication flow (HI)
- **Role**: Claim Adjuster
- **Action**: perform coverage adjudication to determine policy applicability, coverage eligibility, and benefit entitlements for health insurance claims
- **Value**: claims are processed accurately according to policy terms, ensuring correct benefit determination and compliance with coverage rules

**Description:**

> **As a** Claim Adjuster,
> **I want to** perform coverage adjudication to determine policy applicability, coverage eligibility, and benefit entitlements for health insurance claims,
> **so that** claims are processed accurately according to policy terms, ensuring correct benefit determination and compliance with coverage rules.


**Key Capabilities:**

> 1. Adjuster initiates the coverage adjudication process for a health insurance claim.
> 2. System evaluates policy status and member eligibility at the time of service.
> 3. System determines whether the claimed services are covered benefits under the policy terms.
> 4. System applies applicable coverage rules including deductibles, co-insurance, co-payments, and benefit maximums.
> 5. System identifies any exclusions, limitations, or special conditions that apply to the claim.
> 6. System calculates covered amounts and member cost-sharing responsibilities.
> 7. Adjuster reviews system-generated coverage determination and supporting rationale.
> 8. Adjuster finalizes coverage adjudication decision and proceeds to claim payment or denial processing.

---

#### Feature: Coverage Eligibility
- **Role**: Coverage Adjudicator
- **Action**: determine whether an employee/member is eligible for benefits based on their employment start date and the policy's eligibility waiting period configuration
- **Value**: accurate coverage decisions are made by systematically evaluating member eligibility against policy terms and loss dates, ensuring only qualified members receive benefits

**Description:**

> **As a** Coverage Adjudicator,
> **I want to** determine whether an employee/member is eligible for benefits based on their employment start date and the policy's eligibility waiting period configuration,
> **so that** accurate coverage decisions are made by systematically evaluating member eligibility against policy terms and loss dates, ensuring only qualified members receive benefits.


**Key Capabilities:**

> 1. System classifies the employee as New or Existing by comparing the member's Date of Hire with the policy term effective date.
>    1.1 If Date of Hire is earlier than policy term effective date, employee is classified as Existing Employee (eligibilityTypeCd=ExistingEmployees).
>    1.2 If Date of Hire is on or after policy term effective date, employee is classified as New Employee (eligibilityTypeCd=NewEmployees).
> 2. System retrieves the applicable waiting period configuration based on employee classification, including waitingPeriodDefCd (calculation rule), waitingPeriodAmount (numeric value), and waitingPeriodModeCd (time unit).
> 3. System calculates the waiting period end date according to the rule specified by waitingPeriodDefCd.
>    3.1 If waitingPeriodDefCd = 'None': No waiting period applies; waiting period end date equals Date of Hire, member is eligible immediately from Date of Hire.
>    3.2 If waitingPeriodDefCd = 'Amount and mode only': End date = Date of Hire + waitingPeriodAmount (in units of waitingPeriodModeCd); the calculated date is exclusive and member is eligible from that date onwards.
>    3.3 If waitingPeriodDefCd = 'First of month following (amount and mode)': End date = 1st of the month following (Date of Hire + waitingPeriodAmount); always advance to next month even if intermediate date is the 1st; calculated date is exclusive.
>    3.4 If waitingPeriodDefCd = 'First of month coincident with or next following (amount and mode)': End date = Date of Hire + waitingPeriodAmount; if result is not the 1st of a month, advance to 1st of next month; if result is the 1st, use as-is; calculated date is exclusive.
>    3.5 If waitingPeriodDefCd = 'First of month following date of hire': End date = 1st of the month following Date of Hire; always advance even if Date of Hire is the 1st; calculated date is exclusive.
>    3.6 If waitingPeriodDefCd = 'First of month coincident with or next following date of hire': End date = Date of Hire if it falls on the 1st of a month, otherwise 1st of next month; calculated date is exclusive.
> 4. System validates member eligibility by comparing Date of Loss with the calculated waiting period end date.
>    4.1 If Date of Loss is strictly greater than the calculated end date, member is determined 'Eligible'.
>    4.2 If Date of Loss is equal to or less than the calculated end date, member is determined 'NOT Eligible' because the loss occurred during or before the waiting period.
> 5. System generates eligibility determination results and outbound messages for downstream settlement processes (Capital Leave Settlement Result - Eligibility Evaluation and Capital SMP Settlement Result - Eligibility Evaluation).

---

#### Feature: Configure new and change existing coverages
---

#### Feature: Coverage List
- **Role**: Claim Adjuster
- **Action**: add, edit, cancel, and manage coverages on a claim with automated adjudication and accumulator tracking
- **Value**: claims are accurately processed with proper eligibility validation, limit tracking, and audit trails for all coverage decisions

**Description:**

> **As a** Claim Adjuster,
> **I want to** add, edit, cancel, and manage coverages on a claim with automated adjudication and accumulator tracking,
> **so that** claims are accurately processed with proper eligibility validation, limit tracking, and audit trails for all coverage decisions.


**Key Capabilities:**

> 1. User accesses Coverage list on Claim Overview page and initiates coverage addition process.
> 2. User searches and selects one or multiple coverages from available policy coverages filtered by policy configuration and existing claim coverages.
> 3. System executes automated adjudication workflow:
>    3.1 Invokes REST commands based on loss type of selected coverage.
>    3.2 Validates coverage duplication against existing claim coverages.
>    3.3 Calculates gross amount based on coverage configuration and remaining limits.
>    3.4 Generates appropriate accumulators (Calendar Year or Benefit Year) based on incident dates and policy configuration.
> 4. If automated adjudication succeeds, system displays coverage with all calculated details (Incident Date, Date Range, # Days/Occurrences, POL Received Date, Gross Amount, Paid, Unpaid, Remaining Limit, ICD/CPT codes).
> 5. If automated adjudication fails, system presents coverage in Edit Mode requiring manual data completion:
>    5.1 System validates eligibility based on incident date or date range against policy effective period and date of loss.
>    5.2 System automatically calculates # Days/Occurrences from date range (ThroughDate - FromDate + 1, minimum 1 day).
>    5.3 System calculates gross amount in real-time based on # Days/Occurrences and coverage configuration.
>    5.4 User completes required fields and saves to finalize coverage addition.
> 6. User edits existing coverage to modify dates, override calculations, or update coverage details:
>    6.1 User enters Edit Mode and modifies editable attributes (Incident Date, Date Range, # Days/Occurrences, POL Received Date, Gross Amount, ICD/CPT codes).
>    6.2 For authorized users, system enables override checkboxes for # Days/Occurrences and Gross Amount based on coverage configuration.
>    6.3 When override is selected, system accepts manual input and skips automatic calculation, displaying "Over Limit!" warning if value exceeds remaining limit.
>    6.4 When override is unselected, system reverts to automatic calculation based on configured formulas.
>    6.5 System validates manual overrides of # Days/Occurrences against remaining limits using accumulator data.
>    6.6 On save, system re-adjudicates settlement, recalculates gross amount, regenerates accumulators, validates duplication, and updates coverage status.
>    6.7 If coverage has issued payments, system prevents modification of Incident Date and Date Range.
> 7. User cancels coverage when it should no longer be processed:
>    7.1 User selects Cancel Coverage action from coverage actions menu.
>    7.2 User confirms cancellation and provides mandatory Cancel Reason.
>    7.3 System updates coverage with "Cancelled" sub-status, sets isCancelled indicator to True, and displays Cancel Reason in tooltip.
>    7.4 System excludes cancelled coverage from automated coverage workflows but allows manual re-addition.
>    7.5 System hides Edit action and displays Undo Cancellation action.
> 8. User reverses cancellation to restore coverage to active status:
>    8.1 User selects Undo Cancellation action from cancelled coverage actions menu.
>    8.2 User confirms undo action.
>    8.3 System removes Cancelled sub-status and Cancel Reason, sets isCancelled to False, and re-adjudicates settlement to recalculate gross amount and accumulator limits.
> 9. System generates Calendar Year accumulators based on coverage incident dates or date ranges:
>    9.1 For coverages with mandatory Incident Date, system checks if Calendar Year accumulator exists for the incident date's calendar year.
>    9.2 For coverages with mandatory Date Range, system checks if Calendar Year accumulators exist for both beginning and end dates' calendar years.
>    9.3 If date range spans multiple calendar years, system creates separate accumulators for each year involved.
> 10. System generates Benefit Year accumulators based on policy effective date and coverage dates:
>    10.1 System calculates Benefit Year using MM/DD of policy effective date.
>    10.2 For coverages with mandatory Incident Date, system checks if Benefit Year accumulator exists for the benefit year containing the incident date.
>    10.3 For coverages with mandatory Date Range, system checks if Benefit Year accumulators exist for benefit years containing beginning and end dates.
>    10.4 If incident date or date range begins before policy effective date, system marks coverage as non-eligible and does not generate accumulator.
>    10.5 If date range spans multiple benefit years, system creates separate accumulators for each benefit year involved.
> 11. User views accumulator transaction history and remaining limit details through information icons and action menu options.
> 12. System validates all date inputs to prevent future incident dates and dates earlier than date of loss, displaying appropriate error messages and marking settlements as non-eligible when validation fails.

---

#### Feature: Coverages - Add
- **Role**: Claim Adjuster
- **Action**: add, edit, view, and cancel coverages on a claim, including adjudication processing and financial limit management
- **Value**: claims are accurately adjudicated with appropriate coverage limits, supporting compliant payment processing and proper financial controls

**Description:**

> **As a** Claim Adjuster,
> **I want to** add, edit, view, and cancel coverages on a claim, including adjudication processing and financial limit management,
> **so that** claims are accurately adjudicated with appropriate coverage limits, supporting compliant payment processing and proper financial controls.


**Key Capabilities:**

> 1. User views the Coverage List displaying all coverages associated with the claim, including financial summary (Coverage Name, Incident Date, Date Range, # Days/# Occurrences, POL Received Date, Gross Amount, Paid, Unpaid, Remaining Limit Information, ICD/CPT Code) and status information.
> 2. User adds new coverage to the claim by searching and filtering available coverages from policy-based configuration tables, selecting one or multiple coverages, and confirming the selection.
>   2.1 System validates applicable loss types against claim events and triggers settlement adjudication via external API.
>   2.2 If adjudication succeeds, coverage is approved with 'Active' status and accumulator transactions are initialized.
>   2.3 If adjudication fails, system automatically places coverage into Edit Mode requiring manual review and correction before re-adjudication.
>   2.4 User can cancel the add operation without saving any selections.
> 3. User views additional coverage details including remaining limits by calendar/benefit year and accumulator transaction history through dedicated pop-ups and drawer components.
> 4. User edits existing coverage attributes including Incident Date, Date Range, # Days/# Occurrences, Gross Amount, and POL Received Date, with system performing real-time auto-calculations based on configuration rules.
>   4.1 System enforces mandatory field validations, duplication checks, and eligibility checks during save operation.
>   4.2 System triggers re-adjudication and updates accumulator transactions upon successful save.
>   4.3 User can override # Days/# Occurrences for non-money accumulator units or Gross Amount for money-based accumulator units when configuration permits and user has appropriate privileges.
>   4.4 When overridden values exceed temporary remaining limits, system displays warnings but allows user to proceed with acknowledgment.
>   4.5 User can cancel edit operation without saving changes; system preserves original data.
>   4.6 If validation errors occur, system displays error messages and keeps coverage in Edit Mode until corrections are made.
> 5. User cancels coverage by providing a cancellation reason, with system validating for dependencies (beneficiaries, linked coverages, issued payments) before allowing cancellation and setting status to 'Cancelled'.
>   5.1 If dependencies exist, system prevents cancellation and displays error message specifying blocking dependency.
>   5.2 User can undo cancellation to restore coverage to 'Active' status.
> 6. System enforces precondition controls including disabling Add Coverage when plan is not selected or claim is marked non-eligible, and disabling Edit when plan is not selected.
> 7. System restricts field editability based on business rules, permanently disabling Incident Date and Date Range modifications after payment issuance to protect financial transaction integrity.

---

#### Feature: Coverages - Override/Edit
- **Role**: Claim Adjuster
- **Action**: view eligibility validation results at case and claim levels, manually override non-eligible determinations when necessary, and manage automatic validation behavior
- **Value**: authorized users can correct system-determined eligibility outcomes based on business judgment while maintaining visibility into validation logic and override status

**Description:**

> **As a** Claim Adjuster,
> **I want to** view eligibility validation results at case and claim levels, manually override non-eligible determinations when necessary, and manage automatic validation behavior,
> **so that** authorized users can correct system-determined eligibility outcomes based on business judgment while maintaining visibility into validation logic and override status.


**Key Capabilities:**

> 1. User views eligibility status at case overview level, where non-eligible claims are tagged under the Other Claims section with detailed information available via hover tooltip.
> 2. User navigates to claim overview and views eligibility status for each coverage line in the Coverages section, where:
>    - Eligible coverages display with green indicator and 'Eligible' text
>    - Non-eligible coverages display with red indicator, 'Non-Eligible' text, and exclamation mark icon
>    - Hover interactions reveal detailed failure messages for non-eligible determinations
> 3. User corrects eligibility by modifying underlying input parameters (e.g., dates, amounts, member information), triggering automatic re-validation and updated results display.
> 4. User with override privileges manually overrides eligibility determination by:
>    - Entering settlement edit mode
>    - Enabling the override function via checkbox control
>    - Selecting desired eligibility outcome from available options (default set to opposite of current state)
>    - Saving changes to activate the override
>    4.1 If user lacks override privilege, the override checkbox is hidden and manual override is not available
> 5. System suspends automatic eligibility re-validation when an active override is in place, preserving the manual determination even when case or claim data is updated.
> 6. User disables active override by unchecking the override control and saving, which triggers immediate re-validation of eligibility based on current data and displays updated system-determined results.
> 7. System provides visual differentiation for overridden eligibility status through blue information icon with explanatory tooltip message.
> 8. All eligibility validation results are sourced from settlement entities (CISettlement, DeathSettlement, HISettlement, PremiumWaiverSettlement, AccidentSettlement) and displayed consistently across case and claim views.

---

#### Feature: Coverage auto-creation for Death (TL/ACC)
- **Role**: Claims Adjuster
- **Action**: trigger automatic creation and evaluation of death benefit coverages for Term Life and Accidental Death claims upon case initiation
- **Value**: eligible death benefits are identified and adjudicated promptly without manual coverage research, reducing processing time and ensuring beneficiaries receive timely claim decisions

**Description:**

> **As a** Claims Adjuster,
> **I want to** trigger automatic creation and evaluation of death benefit coverages for Term Life and Accidental Death claims upon case initiation,
> **so that** eligible death benefits are identified and adjudicated promptly without manual coverage research, reducing processing time and ensuring beneficiaries receive timely claim decisions.


**Key Capabilities:**

> 1. System automatically identifies applicable Term Life and Accidental Death coverages when a death claim case is created or updated.
> 2. System retrieves active policy information, including base coverage amounts, riders, and effective dates for the insured member.
> 3. System evaluates policy terms and conditions to determine coverage applicability based on date of loss, cause of death, and policy status.
> 4. System auto-creates coverage records for each eligible death benefit, including base death benefit and applicable riders (e.g., Accidental Death and Dismemberment, Waiver of Premium).
> 5. System populates coverage records with benefit amounts, coverage limits, deductibles (if applicable), and relevant policy provisions.
> 6. System flags coverages requiring special handling or additional documentation (e.g., accidental death verification, beneficiary disputes).
> 7. System initiates coverage adjudication workflow immediately upon coverage creation, routing to appropriate adjudication queues.
> 8. System maintains audit trail of auto-created coverages, including creation timestamp, policy source data, and applied business rules.

---

#### Feature: Coverage auto-creation for HI (HI)
- **Role**: Claims Adjudicator
- **Action**: have health insurance coverages automatically created and adjudicated based on policy and claim information
- **Value**: coverage decisions are made consistently, efficiently, and without manual data entry delays

**Description:**

> **As a** Claims Adjudicator,
> **I want to** have health insurance coverages automatically created and adjudicated based on policy and claim information,
> **so that** coverage decisions are made consistently, efficiently, and without manual data entry delays.


**Key Capabilities:**

> 1. System automatically creates coverage records for health insurance claims based on policy configuration and claim details upon claim initiation.
> 2. System evaluates coverage applicability by validating member eligibility, policy status, and benefit plan provisions at the time of loss.
> 3. System determines coverage decisions (approved, denied, pending) based on pre-configured business rules specific to health insurance products.
> 4. System maintains audit trail of all auto-created coverages including creation timestamp, source policy information, and adjudication rationale.
> 5. System supports exception handling for scenarios where automated coverage creation cannot be completed due to incomplete policy data or eligibility gaps.
>   5.1 When policy data is insufficient, system flags coverage for manual review by adjudicator.
>   5.2 When member eligibility cannot be determined, system creates coverage in pending status and generates work item for investigation.
> 6. System allows authorized users to review, modify, or override auto-created coverage decisions with appropriate justification and approval workflow.

---

#### Feature: Coverage Duplication Check
- **Role**: Claim Adjuster
- **Action**: prevent duplicate coverage entries during claim adjudication by validating coverage combinations based on policy, case, coverage type, and temporal parameters
- **Value**: claim settlements are accurate, compliant, and free from erroneous duplicate benefit payments

**Description:**

> **As a** Claim Adjuster,
> **I want to** prevent duplicate coverage entries during claim adjudication by validating coverage combinations based on policy, case, coverage type, and temporal parameters,
> **so that** claim settlements are accurate, compliant, and free from erroneous duplicate benefit payments.


**Key Capabilities:**

> 1. System initiates coverage duplication validation during the adjudication or re-adjudication process for open claims.
> 2. For standard coverages (excluding Coma Benefit, Anesthesia Benefit, Burn Skin Graft Benefit, Child Care Benefit, and Child Education Benefit), the system validates duplicates based on the combination of Policy Number, Case Number, Coverage Name, and Incident Date/Date Range (if mandatory).
> 3. For coverages with default values, validation is triggered when the user confirms the coverage entry; for coverages without default values, validation occurs when the user saves the coverage in edit mode.
> 4. The system applies date range overlap detection rules where end dates are treated as exclusive, meaning overlapping periods are flagged as duplicates (e.g., Period 1: 01/01/2000 - 02/01/2000 overlaps with Period 2: 02/01/2000 - 03/01/2000).
> 5. The system excludes certain entries from duplication validation:
>    5.1 Coverages with missing mandatory parameters in the duplication definition (e.g., incomplete Incident Date or Date Range).
>    5.2 Existing coverages already marked as non-eligible.
> 6. If no duplication is detected, the system marks the coverage as eligible and allows adjudication to proceed.
> 7. If duplication is detected, the system:
>    7.1 Marks the coverage as non-eligible.
>    7.2 Displays the error message: 'The added coverage is duplicated under this case'.
>    7.3 Disables the non-eligible indicator to prevent manual override.
>    7.4 Locks the coverage from further updates until system re-adjudication successfully validates it as non-duplicate.
> 8. For special coverage types, the system applies extended duplication criteria:
>    8.1 **Coma Benefit**: Validates based on Policy Number, Case Number, Coverage Name, Incident Date, and Date Range.
>    8.2 **Anesthesia Benefit and Burn Skin Graft Benefit**: Validates based on Policy Number, Case Number, Coverage Name, Incident Date, and Surgery/Burn link.
>    8.3 **Child Care Benefit and Child Education Benefit**: Validates based on Policy Number, Case Number, Coverage Name, Incident Date, Date Range, and Child Name (excluding non-eligible coverages).
>    8.4 **Term Life Coverage**: Validates based on Policy Number, Case Number, Coverage Name, Incident Date, Date Range, and Coverage Label.
> 9. All special coverage validations are triggered when the user saves the coverage in edit mode and follow the same overlap rules and exclusions as standard coverages.

---

#### Feature: Cancel/Undo Cancel Coverage
- **Role**: Coverage Adjuster
- **Action**: cancel an approved coverage settlement and undo the cancellation when needed, including managing accumulator reservations, payment implications, and overpayment balances
- **Value**: coverage decisions can be reversed or corrected while maintaining accurate financial tracking and accumulator integrity across individual and group limits

**Description:**

> **As a** Coverage Adjuster,
> **I want to** cancel an approved coverage settlement and undo the cancellation when needed, including managing accumulator reservations, payment implications, and overpayment balances,
> **so that** coverage decisions can be reversed or corrected while maintaining accurate financial tracking and accumulator integrity across individual and group limits.


**Key Capabilities:**

> 1. **Cancel Coverage Process**
>    1.1 User marks the coverage settlement as cancelled by setting cancellation indicator and providing mandatory cancellation reason.
>    1.2 System unreserves accumulator amounts based on payment status:
>       - If no payment was made: Reserved amounts return to Remaining for both Individual and Group Accumulators.
>       - If payment was made: System generates Overpayment Balance equal to payment amount while maintaining Used and Remaining amounts unchanged.
>    1.3 System triggers payment rescheduling for coverages with approved payment records, hiding affected payment records from UI while retaining backend data.
>    1.4 System locks the cancelled coverage from all automated processes including policy updates, claim updates, re-adjudication, and payment rescheduling until explicitly unlocked.
>
> 2. **Undo Cancellation Process**
>    2.1 User initiates cancellation reversal, clearing the cancellation indicator and removing the cancellation reason requirement.
>    2.2 System restores accumulator reservations and handles payments based on original payment state:
>       - If payment was not made: Reserved amounts are restored from Remaining to Reserved for both accumulators.
>       - If payment was made but not issued: Payment is removed from Payment List and accumulators are re-reserved (payment must be manually recreated if needed).
>       - If payment was issued: Payment remains unchanged, Overpayment Balance is cleared to $0, and accumulator amounts remain unchanged.
>    2.3 System re-adjudicates the settlement to recalculate eligibility and gross amounts, unless Override checkbox is enabled (which preserves overridden values).
>    2.4 System reserves the recalculated gross amount in accumulators for approved settlements.
>    2.5 System triggers payment rescheduling or recalculation based on payment state, restoring payment visibility in UI where applicable and removing overpayment balances for issued or failed payments.
>
> 3. **Accumulator Management Throughout Lifecycle**
>    3.1 System maintains three states for Individual and Group Accumulators: Reserved (held for pending settlement), Used (consumed by processed settlement), and Remaining (available limit).
>    3.2 System moves amounts between accumulator states based on cancellation/undo operations and payment status.
>
> 4. **Payment State Handling**
>    4.1 System differentiates payment handling logic based on payment status (Approved, Issued, Failed) during both cancellation and restoration operations.
>    4.2 System maintains payment allocation links between settlements and payments throughout the lifecycle.

---

### Epic: Benefit Calculations : Life Products

#### Feature: Death Benefit calculations
- **Role**: Claim Adjuster
- **Action**: calculate the gross amount for death benefit settlements based on policy face value, benefit amounts, accumulator limits, and configured formulas, with the ability to apply manual overrides when necessary
- **Value**: accurate and consistent benefit payments are determined in compliance with policy terms, accumulator constraints, and regulatory requirements

**Description:**

> **As a** Claim Adjuster,
> **I want to** calculate the gross amount for death benefit settlements based on policy face value, benefit amounts, accumulator limits, and configured formulas, with the ability to apply manual overrides when necessary,
> **so that** accurate and consistent benefit payments are determined in compliance with policy terms, accumulator constraints, and regulatory requirements.


**Key Capabilities:**

> 1. System evaluates whether a Gross Amount Override is active for the settlement by checking the isGrossAmountOverrided flag.
>   1.1 If override is active (flag = True), the system applies the manually entered override amount directly to the settlement gross amount field and terminates the calculation process, bypassing all standard calculation steps.
>   1.2 If override is not active (flag = False), the system proceeds with standard calculation logic.
> 2. System retrieves required policy data including Face Value Amount and Benefit Amount from the associated policy record.
> 3. System calculates the Accumulator Remaining Amount by applying logic defined in the Accumulator Calculation Details business rules, incorporating Settlement Used Amount, Coverage Remaining Amount, and Group Remaining Amount.
> 4. System determines the numberOfUnits value based on override indicator:
>   4.1 If numberOfUnitsOverrideInd = False, system calculates the minimum of numberOfUnits and remainingAmount.
>   4.2 If numberOfUnitsOverrideInd = True, system retrieves the manually overridden numberOfUnits value.
> 5. System retrieves the coverage-specific calculation formula configured in OpenL Coverage-based Configurations and Rules.
> 6. System executes the gross amount calculation by applying the configured formula using policy face amount, benefit amount, accumulator remaining amounts, and determined numberOfUnits.
> 7. System generates the final Gross Amount for the settlement, constrained by the minimum of face amount and calculated remaining amount as per formula configuration.

---

#### Feature: Accelerated Death Benefit calculations
- **Role**: Claims Adjuster
- **Action**: calculate the gross amount for Accelerated Death Benefit settlements based on policy face value, accumulator remaining amounts, and configured formulas, with support for manual overrides
- **Value**: settlements are accurately calculated within policy limits and accumulator constraints, ensuring compliance with benefit rules while allowing adjuster discretion when needed

**Description:**

> **As a** Claims Adjuster,
> **I want to** calculate the gross amount for Accelerated Death Benefit settlements based on policy face value, accumulator remaining amounts, and configured formulas, with support for manual overrides,
> **so that** settlements are accurately calculated within policy limits and accumulator constraints, ensuring compliance with benefit rules while allowing adjuster discretion when needed.


**Key Capabilities:**

> 1. System evaluates whether gross amount has been manually overridden by checking the override flag.
>    1.1 **Override Path**: If gross amount is overridden, system applies the manual override value directly and bypasses automatic calculation.
> 2. For automatic calculation path, system retrieves policy data including Face Value Amount and Benefit Amount from the policy record.
> 3. System calculates remaining accumulator amounts at both coverage and group levels following defined accumulator calculation rules to determine available benefit balances.
> 4. System retrieves the calculation formula configured for the specific settlement and coverage type.
> 5. System determines the number of benefit units to apply.
>    5.1 **Units Override**: If number of units is overridden, system uses the manual override value; otherwise calculates minimum of configured units and remaining amount.
> 6. System applies the calculation formula using the constraint hierarchy: Gross Amount equals the minimum of Face Amount and remaining amount, where remaining amount equals Settlement Used Amount plus the minimum of coverage remaining amount and group remaining amount.
> 7. System saves the final calculated or overridden gross amount to the settlement record for downstream processing and payment execution.

---

#### Feature: View calculation formula
- **Role**: Claim Adjuster
- **Action**: view the gross amount calculation formula and computed values for a specific life product coverage
- **Value**: I can understand how the benefit amount was calculated, verify the accuracy of the computation, and explain the calculation to stakeholders

**Description:**

> **As a** Claim Adjuster,
> **I want to** view the gross amount calculation formula and computed values for a specific life product coverage,
> **so that** I can understand how the benefit amount was calculated, verify the accuracy of the computation, and explain the calculation to stakeholders.


**Key Capabilities:**

> 1. User selects a coverage from the Claim Overview page's coverage list to view its calculation details.
> 2. System displays a pop-up containing the gross amount calculation formula and computed values.
> 3. Pop-up presents two primary sections:
>    3.1 FORMULA DESCRIPTION section displays the business-readable formula sourced from the GTL Coverage Configuration Table.
>    3.2 CALCULATION CONTENT section shows the actual calculation with parameter values substituted and the final computed result.
> 4. System adapts display format based on coverage payment structure:
>    4.1 For 'Across Years' payment structure: Formula description shows 'Yearly Gross Amount: [Formula]'; Calculation content displays separate lines for each year using format '[Year1 - Year2]: [Calculation] = $[Result]'.
>    4.2 For 'Recurring Payments' structure (Monthly, Bi-Monthly, Weekly, Bi-weekly): Formula description shows '[X] Amount: [Formula]' where X is the payment frequency; Calculation content shows 'Per [Unit]: [Calculation] = $[Result]'.
>    4.3 For standard coverage structure: Standard format '[Calculation] = $[Result]' is applied.
> 5. System handles edge cases in calculation display:
>    5.1 When a formula parameter is unavailable, system displays 'N/A' for that parameter.
>    5.2 When a calculated value is negative, system displays '0' instead of the negative amount.
> 6. System applies appropriate data formatting: monetary values with two decimal places, units as integers, percentages as integers with % symbol, and special percentage conversion for Age Reduction% and Child Organized Sport Benefit parameters.

---

### Epic: Special Coverage Process

#### Feature: Process Recurrence Benefits
- **Role**: Claim Adjuster
- **Action**: manage and view recurrence coverage information for Critical Illness (CI) claims
- **Value**: accurate coverage determination and benefit processing can be performed for recurring critical illness events

**Description:**

> **As a** Claim Adjuster,
> **I want to** manage and view recurrence coverage information for Critical Illness (CI) claims,
> **so that** accurate coverage determination and benefit processing can be performed for recurring critical illness events.


**Key Capabilities:**

> 1. User accesses the Critical Illness claim overview page to view recurrence coverage information.
> 2. System displays a dedicated recurrence coverage list containing all coverage items applicable to recurring critical illness events for the selected claim.
> 3. User reviews recurrence coverage details to determine benefit eligibility and applicable policy provisions.
> 4. User interacts with the recurrence coverage list to access detailed coverage information necessary for adjudication decisions.
> 5. System maintains recurrence coverage data within the claim context, ensuring coverage information remains associated with the specific CI claim throughout the adjudication lifecycle.

---

#### Feature: Process Special Coverages (ACC)
- **Role**: Claim Adjuster
- **Action**: manage and record Accident Special Coverage details (Child Education/Care, Burn Skin Graft, Burn/Dislocation/Fracture) for claim cases
- **Value**: accurate tracking of treatment periods, eligibility, and financial limits is maintained for specialized accident-related coverages

**Description:**

> **As a** Claim Adjuster,
> **I want to** manage and record Accident Special Coverage details (Child Education/Care, Burn Skin Graft, Burn/Dislocation/Fracture) for claim cases,
> **so that** accurate tracking of treatment periods, eligibility, and financial limits is maintained for specialized accident-related coverages.


**Key Capabilities:**

> 1. User accesses the Claim Overview page to view existing Accident Special Coverage entries in a list format displaying Incident Date, Date Range, Days/Occurrences, PDL Received Date, Gross Amount, Paid Amount, Remaining Limit, Child Name, and Eligibility status.
> 2. User initiates adding a new coverage entry by accessing the Edit Coverage Form.
> 3. User selects the required Child Name from a dropdown populated with parties associated with the case.
> 4. User enters the required Date Range using a calendar selector to record the treatment period (start and end dates), with dates formatted according to user locale settings.
> 5. User submits the coverage entry by saving the form, creating a new coverage record persisted to the system.
> 6. User views the newly added coverage in the Coverage List with Child Name and Date Range displayed in MM/DD/YYYY-MM/DD/YYYY format.
>    6.1. **Alternate Flow - Cancel Entry**: If the user clicks Cancel during coverage entry, the system discards all entered data and returns to the Coverage List view without saving changes.
>    6.2. **Exception Flow - Missing Child Name**: If Child Name is not selected when attempting to save, the system displays error message 'Child Name is required' and prevents form submission.
>    6.3. **Exception Flow - Missing Date Range**: If Date Range is not provided when attempting to save, the system displays error message 'Date Range is required' and prevents form submission.
>    6.4. **Exception Flow - Invalid Date Logic**: If the Beginning Date in Date Range is not later than the Date of Loss, the system displays error message 'The Beginning Date must be later than the Date of Loss' and prevents form submission until corrected.

---
## Initiative: Waiver of Premium

### Epic: Waiver of Premium

#### Feature: Premium Waiver Process: Claims
- **Role**: Claim Adjuster
- **Action**: manage Premium Waiver settlement details by viewing, editing, and configuring Elimination Period (EP), Benefit Period (BP), and Approval Period (AP) information, including the complete lifecycle of approval periods from creation to completion
- **Value**: accurate premium waiver calculations are automatically triggered, proper accumulator logic is applied, and settlement periods are managed efficiently with appropriate access controls

**Description:**

> **As a** Claim Adjuster,
> **I want to** manage Premium Waiver settlement details by viewing, editing, and configuring Elimination Period (EP), Benefit Period (BP), and Approval Period (AP) information, including the complete lifecycle of approval periods from creation to completion,
> **so that** accurate premium waiver calculations are automatically triggered, proper accumulator logic is applied, and settlement periods are managed efficiently with appropriate access controls.


**Key Capabilities:**

> 1. User accesses the Premium Waiver settlement details by navigating to the Unfolded View of Elimination Period, Benefit Period, and Approval Period information.
>    1.1 User expands the settlement record by clicking the downward arrow icon to display detailed period information.
> 2. User manages Elimination Period configuration.
>    2.1 User clicks the pencil icon against the elimination period record to update elimination period details.
> 3. User manages Benefit Period configuration.
>    3.1 User clicks the pencil icon against the benefit period record to update benefit period details.
> 4. User adds new Premium Waiver Approval Periods.
>    4.1 User clicks the 'Add Approval Period' button (displayed as blue plus icon with text) to open the approval period entry interface.
>    4.2 User enters required approval period information in the slide-out window.
>    4.3 User saves the new approval period, triggering automatic system processing.
> 5. User updates existing Premium Waiver Approval Periods.
>    5.1 User clicks the pencil icon against an approval period record to modify approval details.
>    5.2 User changes the Approval Status to 'Completed' when the approval period concludes.
>    5.3 User saves the updated approval period, triggering completion workflow.
> 6. System automatically processes period changes upon save operations.
>    6.1 When adding an approval period: System closes the drawer, returns to main page, hides edit icons for EP and BP sections, and calculates Reserved units per Premium Waiver Accumulator logic.
>    6.2 When completing an approval period: System closes the drawer, returns to main page, hides edit icons for EP and BP sections, and calculates Completed units per Premium Waiver Accumulator logic.
> 7. System enforces privilege-based access control for all premium waiver period management operations.

---

#### Feature: Premium Waiver Process: related Policy impact
---

#### Feature: Premium Waiver Process: related Billing impact
- **Role**: Claims Adjuster
- **Action**: process premium waiver claims for policyholders who become critically ill, seriously injured, or disabled, and coordinate with the Billing system to waive premiums for approved periods
- **Value**: policyholders can maintain their insurance benefits without premium payment obligations during periods of disability or critical illness

**Description:**

> **As a** Claims Adjuster,
> **I want to** process premium waiver claims for policyholders who become critically ill, seriously injured, or disabled, and coordinate with the Billing system to waive premiums for approved periods,
> **so that** policyholders can maintain their insurance benefits without premium payment obligations during periods of disability or critical illness.


**Key Capabilities:**

> 1. Claims Adjuster creates a claim with Premium Waiver coverage when a policyholder reports critical illness, serious injury, or disability.
> 2. System validates premium payment status through integration with Billing subsystem to confirm policy eligibility:
>    2.1 System retrieves current policy status (Paid/active/inforce, Cancelled for non-payment, or Pending cancellation).
>    2.2 System retrieves and displays 'Paid To Date' information on the Claims header for reference.
>    2.3 If policy is cancelled for non-payment or pending cancellation, system identifies ineligibility which impacts benefit payment decisions.
> 3. Claims Adjuster manually reviews Disability data and supporting documentation to determine waiver eligibility.
> 4. Claims Adjuster approves premium waiver for specific time periods (designated as 'Approval Periods' in the system) based on disability assessment.
> 5. System transmits approved and completed period data to the Billing system as the basis for premium waiver application.
> 6. Billing system receives approval period data and performs appropriate premium corrections, suspending premium obligations for the approved timeframes.
> 7. Future enhancement will enable system to retrieve unpaid premium amounts from Billing and automatically populate the Gross amount field for Premium Waiver processing.

---
## Initiative: Manage Claim Payment

### Epic: Create Payment Action

#### Feature: Payment Frequency/Scheduling
- **Role**: Claim Adjuster
- **Action**: create, calculate, schedule, and process claim payments with configurable frequencies and automated allocation management across multiple payees and claim types
- **Value**: eligible claimants receive accurate, timely payments with proper tax withholdings, deductions, and offsets while maintaining compliance with authority limits and reducing manual calculation errors

**Description:**

> **As a** Claim Adjuster,
> **I want to** create, calculate, schedule, and process claim payments with configurable frequencies and automated allocation management across multiple payees and claim types,
> **so that** eligible claimants receive accurate, timely payments with proper tax withholdings, deductions, and offsets while maintaining compliance with authority limits and reducing manual calculation errors.


**Key Capabilities:**

> 1. User initiates payment creation from Case or Claim UI and selects mandatory payee (individual, organization, or provider).
> 2. User defines payment allocations by specifying claim, allocation type (Indemnity/Expense/Ex-gratia/Interest Only), coverage or benefit, and allocation period details.
>    2.1 For indemnity payments: user selects specific claim coverage or benefit; system includes benefit amounts and interest amounts.
>    2.2 For expense payments: user enters amount manually; system excludes from accumulators but enforces authority limits.
>    2.3 For ex-gratia payments: user manually enters amount for policy limit exceptions, uninsured losses, or out-of-policy-term payments.
>    2.4 For DI claims with approval periods: user specifies period dates, payment frequency (weekly/monthly), and partial disability attributes.
>    2.5 For TL and SB claims: user can override interest amounts during preview stage.
> 3. System validates allocation inputs by checking for duplicates, verifying claim status is 'open', and confirming claim and coverage eligibility.
> 4. User initiates payment calculations and system executes dry run to generate preview of scheduled payments.
> 5. User reviews calculation preview and confirms to proceed with payment creation.
> 6. System checks for existing payment schedules in status 'open', 'active', or 'suspended' for the same claim.
>    6.1 If existing schedule found: system merges newly added allocations with payment allocation inputs from existing schedule.
>    6.2 If existing schedule is in 'open', 'approved', or 'suspended' status: system conditionally deactivates it and cancels any actual payments in 'approved' status.
> 7. System performs automated payment calculation and scheduling by collecting financial data, generating payment items, and splitting payments by frequency and claim type rules.
>    7.1 For single occurrence/lump sum payments (common in TL and SB claims): system schedules payment for same day as approval without additional scheduling rules.
>    7.2 For recurrent payments: system applies time-period scheduling rules (weekly for STD, monthly for LTD) to split approved periods into payment chunks with assigned post dates.
>    7.3 For partial disability cases: system defaults frequency to single occurrence and schedules for immediate payment.
> 8. System calculates payment amounts using formula: Net Payment = (AGBA) - (Offsets) - (Overpayment Withholding) - (Pre-tax Deductions) - (Federal & FICA taxes) - (Post-tax Deductions).
>    8.1 System calculates AGBA by prorating GBA (Gross Benefit Amount) using claim-specific rates: 1/5 or 1/7 for STD/SMD claims, 1/30 for LTD claims.
>    8.2 System applies offsets (disability claims only) using potentially different proration rates from main benefit.
>    8.3 System calculates Federal and State tax withholding based on predefined periods and amounts; applies FICA taxes automatically per configuration rules.
>    8.4 System withholds deductions (pre-tax and post-tax) based on defined deduction periods and amounts.
>    8.5 System automatically creates separate deduction payments for non-sponsor-based deduction withholding types (child support, tax liens).
> 9. System creates new payment schedule entity with status 'open' and validates user authority level limits.
>    9.1 If user has sufficient authority and no overpayment conditions exist: system auto-approves payment schedule, changes status to 'Active', and displays payments as 'pending post'.
>    9.2 If user lacks sufficient authority: payment schedule remains in status requiring approval, payments display as 'pending', and appropriately authorized user must approve via UI payment list component.
> 10. System displays combined payments list for all payees with appropriate status indicators on Case and Claim overview screens.
> 11. System executes automated payment generation and posting services on planned post date to create actual payments, assign payment numbers, and dispatch to Payment Hub for processing.
>    11.1 If user needs to create payments for another payee or add new allocations: user repeats payment creation process (only one payee per iteration).
>    11.2 If user needs to cancel, update, or suspend payments: user initiates respective action which triggers payment schedule deactivation and recalculation workflows.
>    11.3 If deductions are added after payment creation: system triggers automatic payment recalculation following calculation and scheduling automation flow.
>    11.4 If Claims UI initiates Stop or Void actions for check payments: system sends request to Payment Hub and synchronizes payment state based on Payment Hub decision.
>    11.5 If system encounters exceptions during automated payment generation and posting: user intervention is required to resolve issues.

---

#### Feature: Payment Details
- **Role**: Claim Adjuster
- **Action**: create or update claim payments with detailed allocation information including payees, payment methods, coverage selections, and allocation types
- **Value**: payments are accurately processed with proper allocation to coverages, beneficiaries, and guardians, reducing errors and ensuring compliance with payment rules

**Description:**

> **As a** Claim Adjuster,
> **I want to** create or update claim payments with detailed allocation information including payees, payment methods, coverage selections, and allocation types,
> **so that** payments are accurately processed with proper allocation to coverages, beneficiaries, and guardians, reducing errors and ensuring compliance with payment rules.


**Key Capabilities:**

> 1. User initiates payment creation from Claim or Event Case Overview Page, triggering the system to retrieve the latest payment template.
> 2. User enters payment details in Step 1 - Detail including:
>    2.1 Selecting payee from available parties (member, subject of claim, beneficiaries, guardians, additional parties).
>    2.2 When payee is a guardian, specifying the beneficiary via 'On Behalf Of' field, which determines claim and coverage loading based on the selected beneficiary or payee.
>    2.3 Selecting payment method (auto-populated from Event Case or Claim Wrapper attributes based on payee role).
>    2.4 Selecting claim (preselected if initiated from claim overview).
> 3. User selects allocation type and enters corresponding details:
>    3.1 For Indemnity allocations: selects coverages from claim-specific API endpoints (varies by claim type: TL/CI/HI/ACC, STD, or LTD), with coverage options filtered based on guardian status and beneficiary designations.
>    3.2 For Expense allocations: manually inputs expense amount and description (max 25 characters).
>    3.3 For Ex Gratia allocations: manually inputs ex gratia amount.
>    3.4 For Indemnity allocations with recurring payments (TL claims): system automatically applies recurring payment template and populates allocation periods from date ranges.
> 4. User optionally configures interest-only payment flag (when set to 'Yes', system automatically sets Gross Amount to 0 in Step 2).
> 5. User optionally adds EOB remarks by multi-selecting pre-defined codes or entering custom text in 'Other EOB Remarks'.
> 6. User clicks Calculate button, triggering system to:
>    6.1 Validate payment method via payment hub integration.
>    6.2 Check for duplicate allocations based on claim type-specific rules (payee + claim + coverage + date range for TL/CI/HI/ACC; payee + claim + coverage + allocation period for disability).
>    6.3 Verify claim status supports selected allocation type (Indemnity requires Open status).
>    6.4 If validation succeeds, advance to Step 2 - Allocation page with generated allocations; if validation fails, display error messages for user correction.
> 7. User reviews and edits allocation details in Step 2, then submits payment or saves draft and exits.
> 8. For updating existing payments:
>    8.1 User clicks 'Update Payment' button when existing payment exists.
>    8.2 System loads existing payment template in update wizard.
>    8.3 User edits payment details in Step 1 and allocation details in Step 2 (Post Date is not editable; adding new allocations is not supported).
>    8.4 User clicks 'Update' button to finalize payment changes.
> 9. User can manage allocations by deleting unwanted allocations before calculation.
> 10. Upon successful submission, payment is processed and financial data is collected per business rules.

---

#### Feature: Payment Allocation Details
- **Role**: Claim Adjuster
- **Action**: review, adjust, and validate payment allocations across claims and coverages before finalizing payment creation or update
- **Value**: payment accuracy is ensured, allocation conflicts are prevented, and all beneficiary, coverage, and regulatory requirements are met before funds are disbursed

**Description:**

> **As a** Claim Adjuster,
> **I want to** review, adjust, and validate payment allocations across claims and coverages before finalizing payment creation or update,
> **so that** payment accuracy is ensured, allocation conflicts are prevented, and all beneficiary, coverage, and regulatory requirements are met before funds are disbursed.


**Key Capabilities:**

> 1. User accesses Step 2 'Allocations' tab in the payment wizard to review all proposed payment allocations.
> 2. System presents Total Allocations summary grouped by post date, displaying the sum of allocation amounts for each date in chronological order.
> 3. System displays Allocation List Table with rows grouped by claim, showing claim identification (loss type and number), coverage details (type, name, net amount), and alert warnings (e.g., when Premiums Paid to Date is earlier than Date of Loss/Date of Incident).
> 4. User expands individual allocation rows via expandable accordion to view detailed allocation information specific to product type.
>    4.1 For Life, Critical Illness, and Hospital Indemnity allocations: system displays coverage information (incident date, date range, occurrences, proof of loss received date), interest calculation fields, post date, and payment preview breakdown (gross amount, previously paid, remaining limit, net amount, indemnity/expense, deductions, interest, EOB remarks).
>    4.2 For Disability allocations: system displays allocation period (benefit date range), partial disability indicator with current earnings field, payment frequency, interest calculations (when POL received date is provided), and detailed breakdown including Gross Benefit Amount, offsets, Adjusted GBA, deductions, taxes (Federal, FICA, State), rehabilitation benefits, and COLA (for LTD only).
>    4.3 For Expense Payment allocations: system displays allocation details as read-only without recalculation functionality.
>    4.4 For Ex Gratia Payment allocations: system displays allocation details as read-only without recalculation functionality.
> 5. When payee is a beneficiary, system auto-allocates gross amount based on beneficiary percentage according to case life payment item generation rules.
> 6. User updates editable fields in allocation details (e.g., interest paid up to date, amount to calculate interest on, payment frequency for Term Life recurring).
>    6.1 For Disability allocations with Single Occurrence frequency and POL received date: user updates 'Interest Paid Up To Date' and 'Amount to Calculate Interest On' fields; system disables create/update button until recalculation is performed.
>    6.2 For Term Life recurring payment coverages: user updates Payment Frequency selection (Weekly, Biweekly, Semi-Monthly, or Monthly); system applies proration logic for allocation periods shorter than the frequency cycle and generates multiple payments as needed.
> 7. Upon any modification to allocation fields, system displays soft warning and disables 'Create' button, alerting user that recalculation is required.
> 8. User clicks 'Recalculate' button to refresh allocation data.
> 9. System recalculates net amounts, interest, prorated amounts, and all dependent fields based on latest inputs, removes soft warning, and re-enables 'Create' button.
>    9.1 For Term Life recurring coverages: system adjusts actual payment amount based on selected payment frequency and allocation period, removes irrelevant sub-ledger items (keeping only Indemnity), and validates for overlapping allocation periods (same Claim + same Coverage code).
> 10. System performs validation checks before enabling payment submission.
>    10.1 For Disability allocations: system validates allocation period selection against duplication rules (same Payee + Claim No. + Coverage + Allocation Period); overlapping periods with exclusive end dates trigger validation error "The Allocation Period is duplicated/overlapped in payment allocation".
>    10.2 For Term Life recurring allocations: system validates that allocation periods for the same Claim and Coverage code do not overlap; overlap triggers error "The allocation period cannot overlap".
> 11. User proceeds to create or update payment once all validations pass and recalculation is complete.
> 12. System submits payment for creation or update and continues downstream payment processing workflows.

---

#### Feature: Configure EOB Remarks
- **Role**: Claim Adjuster
- **Action**: create and manage claim payments with allocation details and assign EOB (Explanation of Benefits) remarks through a multi-step wizard
- **Value**: accurate payment processing with clear benefit explanations are documented for payees, ensuring compliance and transparency in claims settlement

**Description:**

> **As a** Claim Adjuster,
> **I want to** create and manage claim payments with allocation details and assign EOB (Explanation of Benefits) remarks through a multi-step wizard,
> **so that** accurate payment processing with clear benefit explanations are documented for payees, ensuring compliance and transparency in claims settlement.


**Key Capabilities:**

> 1. User accesses Payment Wizard from case or claim level to initiate payment creation or update existing payments.
>    1.1 If no payment exists, user sees 'Create Payment' option with all available payees displayed.
>    1.2 If payments exist, user sees 'Update Payment' option with only payees having existing payment records displayed.
> 2. User selects required payee from alphabetically sorted list containing additional parties, beneficiaries (excluding guardians), and guardian parties.
>    2.1 If guardian is selected as payee, user must designate the beneficiary in 'On Behalf Of' field.
> 3. User selects associated claim with status Pending or Open, filtered based on payee role and beneficiary relationships.
>    3.1 At claim-level payment creation, claim field defaults to current claim and is disabled.
> 4. User specifies allocation type by selecting one of three options:
>    4.1 **Indemnity**: User selects coverage from eligible approved/closed settlements, views read-only allocation period (for Term Life recurring and Disability products), and optionally flags as Interest Only.
>    4.2 **Expense**: User enters expense amount (≥0) and required description.
>    4.3 **Ex Gratia**: User enters ex gratia amount (≥0) and required description.
> 5. User optionally adds payment description text for additional context.
> 6. User configures EOB remarks to document payment explanations and adjustments:
>    6.1 In Update Payment mode, user selects from multi-select dropdown of pre-defined EOB codes or 'Other' option.
>    6.2 Selected remarks display as removable labels for easy management.
>    6.3 If 'Other' is selected, user enters custom text in 'Other EOB Remarks' text box.
>    6.4 System auto-generates automated EOB remarks via OpenL rules during claim processing based on payment allocation characteristics (e.g., guardian designation triggers EOB001, salary adjustment triggers EOB002, amount overrides trigger EOB003).
> 7. User manages multiple allocations by adding new allocation rows or deleting existing ones.
>    7.1 In Create Payment mode, last allocation cannot be deleted.
>    7.2 In Update Payment mode, all allocations can be deleted and 'Add Allocation' is disabled.
> 8. User validates and progresses by clicking 'Calculate' button, which checks for duplicate allocations and navigates to Step 2 (Allocations) in Create mode.
>    8.1 In Update Payment mode, user clicks 'Update' to save changes without navigating to Step 2.
>    8.2 User can cancel at any time to close wizard without saving changes.
> 9. System processes payment allocation and generates comprehensive EOB documentation combining automated rule-based remarks and manual adjuster-added remarks for transparent benefit explanation.

---

#### Feature: Allocation Type: Indemnity, Expense, Ex Gratia
- **Role**: Claim Adjuster
- **Action**: review, update, and submit payment allocations across multiple claim types (Life, CI/HI, Disability, Accident, Absence, Term Life) with support for Indemnity, Expense, and Ex Gratia allocation types
- **Value**: payments are accurately allocated, calculated with appropriate interest and deductions, and submitted for processing with complete audit trails and validation

**Description:**

> **As a** Claim Adjuster,
> **I want to** review, update, and submit payment allocations across multiple claim types (Life, CI/HI, Disability, Accident, Absence, Term Life) with support for Indemnity, Expense, and Ex Gratia allocation types,
> **so that** payments are accurately allocated, calculated with appropriate interest and deductions, and submitted for processing with complete audit trails and validation.


**Key Capabilities:**

> 1. User navigates to the Allocations tab (Step 2) in the Payment Wizard after completing the Detail step, where the system displays total allocations grouped by post date with corresponding amounts.
> 2. User reviews the allocation summary showing payments grouped by post date (earliest to latest) with total net amounts per post date.
> 3. User reviews the allocation list displaying claim details including LOB, loss number, type, coverage name, and calculated net amounts, with visual warnings for premiums not paid to date when payment date precedes incident dates.
> 4. User expands individual allocation rows to view detailed information tailored to claim type:
>    4.1 For Life/CI/HI claims: coverage details (incident date, date range, days/occurrences, POL received date), payment preview (gross amount, previously paid, remaining limit, net amount, indemnity/expense/ex gratia breakdowns, deductions, interest, indebtedness, restored death benefit), and interest calculation fields.
>    4.2 For Disability claims: allocation period, partial payment indicator, current earnings, payment frequency, GBA/AGBA, offsets by type with date ranges, deductions by type with date ranges, taxes (Federal/FICA/State) with date ranges, rehabilitation amounts, COLA details for LTD, and interest components when applicable.
>    4.3 For Term Life Recurring claims: hybrid allocation details combining disability and non-disability elements with allocation period, configurable payment frequency (Weekly/Monthly/Biweekly/Semi-Monthly), automatic proration based on gross amount mode, and overlap validation.
> 5. User reviews EOB remarks displayed at the bottom of allocation details showing automated and manual remarks in alphanumeric ascending order (Code - Description format).
> 6. User updates editable payment values in the allocation preview (interest fields, payment frequency for Term Life, or other enabled inputs) as needed.
>    6.1 When Expense allocation type is selected, system enforces read-only mode preventing any edits to allocation details.
>    6.2 When Ex Gratia allocation type is selected, system enforces read-only mode preventing any edits to allocation details.
>    6.3 For Disability allocations with Single Occurrence frequency and POL received date, user can update Interest Paid Up To Date and Amount to Calculate Interest On fields.
>    6.4 For Term Life recurring payments, user can modify Payment Frequency to adjust payment installment calculations within the allocation period.
> 7. System disables the Create button and displays a soft warning indicating changes have been made requiring recalculation.
> 8. User triggers recalculation by clicking the Recalculate or Recalculate Allocation button to refresh payment schedule preview via REST API.
> 9. System recalculates all dependent values (net amounts, interest, proration, installments), removes warning alerts, and re-enables the Create button.
>    9.1 For Term Life recurring payments, system automatically adjusts payment amounts based on selected frequency and calculates number of installments within allocation period with proration logic (weekly&lt;7 days uses daily proration over 7, monthly&lt;30 days uses daily proration over 30, biweekly&lt;14 days uses daily proration over 14, semi-monthly&lt;15 days uses daily proration over 15).
>    9.2 System validates allocation period duplication for Disability claims (same Payee + Claim No. + Coverage + overlapping Allocation Period with exclusive end dates) and displays error if detected.
>    9.3 System validates allocation period overlap for Term Life recurring claims (same Claim + same Coverage code) and displays error if detected.
> 10. User submits the payment allocation by clicking the Create button, or cancels the process to abort without saving changes.
> 11. System processes the submission, creates payment records with all allocation details, associates EOB remarks, and prepares payment schedule for downstream processing.

---

#### Feature: Payment Frequency
- **Role**: Claim Adjuster
- **Action**: create a payment for an eligible claim or event case, triggering automated payment schedule generation, approval, and issuance
- **Value**: payments are accurately scheduled, duplicate payments are prevented, and approved payments are issued efficiently without manual intervention

**Description:**

> **As a** Claim Adjuster,
> **I want to** create a payment for an eligible claim or event case, triggering automated payment schedule generation, approval, and issuance,
> **so that** payments are accurately scheduled, duplicate payments are prevented, and approved payments are issued efficiently without manual intervention.


**Key Capabilities:**

> 1. User initiates payment creation from the Claim or Event Case Overview page via the Payments & Recoveries component.
> 2. System executes Build Payment Schedule Flow to prepare payment generation:
>    2.1 System deactivates any existing payment schedules with status 'Active', 'Suspended', or 'Open' within the same payment level to enforce single active schedule rule.
>    2.2 System cancels any existing payments in 'Approved' state within the payment level to prevent duplicate payments.
>    2.3 System executes Payment Scheduling Service using rule engine to convert financial data into calculated payment schedule (including both issued and future payments).
>    2.4 System initializes and activates the new Payment Schedule.
>    2.5 System evaluates remaining non-issued payments and completes the schedule if no future payments are pending.
>    **2.3-ALT: If payment scheduling errors occur**, system creates task 'Payment Scheduling Process Failed' and terminates process.
>    **2.4-ALT: If payment schedule activation fails**, system creates task 'Review Payment Schedule' and terminates process.
> 3. User completes and submits the Payment Process.
> 4. System closes the Create Payment drawer, refreshes the Payments Allocations List, and displays the newly created payment record with status 'Pending'.
> 5. System automatically executes Generate Payment Job and updates payment status to 'Approved'.
> 6. System automatically executes Issue Payment Job and validates payee payment method:
>    6.1 If valid payment method exists, system updates payment status to 'Issued'.
>    **6.1-ALT: If no valid payment method exists**, system updates payment status to 'Cancelled'.
> 7. User verifies final payment status and can perform post-issuance actions:
>    **7.1-ALT: If user needs to stop issued payment**, user initiates Request Stop Payment action.
>    **7.2-ALT: If user needs to decline or void issued payment**, user initiates Decline/Void Payment action.

---

#### Feature: Addition & Reductions
- **Role**: Claim Adjuster
- **Action**: create a claim payment action and apply financial additions or reductions to adjust the payment amount based on policy provisions, deductibles, and other financial factors
- **Value**: the final payment amount accurately reflects all applicable adjustments, ensuring correct disbursement and regulatory compliance

**Description:**

> **As a** Claim Adjuster,
> **I want to** create a claim payment action and apply financial additions or reductions to adjust the payment amount based on policy provisions, deductibles, and other financial factors,
> **so that** the final payment amount accurately reflects all applicable adjustments, ensuring correct disbursement and regulatory compliance.


**Key Capabilities:**

> 1. User initiates the creation of a new payment action within an active claim.
> 2. User specifies the base payment amount and selects the payee (claimant, provider, vendor, or other party).
> 3. User applies one or more additions to increase the payment amount, such as:
>    3.1 Additional coverage amounts (e.g., supplemental benefits, policy riders).
>    3.2 Interest accrued due to delayed payment.
>    3.3 Cost-of-living adjustments or inflation-based increases.
>    3.4 Reimbursements for approved expenses.
> 4. User applies one or more reductions to decrease the payment amount, such as:
>    4.1 Deductibles as defined in the policy.
>    4.2 Copayments or coinsurance amounts.
>    4.3 Prior payments or advances already issued on the claim.
>    4.4 Subrogation recoveries or third-party reimbursements.
>    4.5 Depreciation or betterment adjustments for property claims.
>    4.6 Penalty reductions due to policy violations or fraud findings.
> 5. System calculates the net payment amount by applying all additions and reductions to the base amount.
> 6. User reviews a detailed breakdown showing the base amount, each addition, each reduction, and the final net payment amount.
> 7. User adds notes or justifications for each adjustment to maintain an audit trail.
> 8. User submits the payment action for approval or processing based on authority limits.
> 9. System validates that the final net payment amount does not violate policy limits or business rules:
>    9.1 If validation fails, system displays specific error messages and prevents submission.
>    9.2 If the net payment amount is negative or zero, system prompts user to confirm or adjust the entries.
> 10. Upon successful submission, system records the payment action with all adjustments and updates the claim financial summary.

---

#### Feature: Dividends
---

#### Feature: FICA
- **Role**: Claim Adjuster
- **Action**: configure FICA tax exemptions and ensure accurate FICA tax calculations for claim payments based on federal tax regulations and individual exemption status
- **Value**: claim payments comply with federal tax withholding requirements while properly handling tax-exempt individuals

**Description:**

> **As a** Claim Adjuster,
> **I want to** configure FICA tax exemptions and ensure accurate FICA tax calculations for claim payments based on federal tax regulations and individual exemption status,
> **so that** claim payments comply with federal tax withholding requirements while properly handling tax-exempt individuals.


**Key Capabilities:**

> 1. System automatically calculates FICA taxes for all payments in the Payment Schedule based on configured tax rules for the applicable payment year.
> 2. System applies FICA Social Security Tax (FSST/OASDI) calculation:
>    2.1 Applies 6.2% rate to calendar year earnings.
>    2.2 Monitors cumulative earnings against annual threshold ($142,800-$176,100 depending on year 2021-2025).
>    2.3 Stops applying FSST once the threshold is reached for that calendar year.
> 3. System applies FICA Medicare Tax (FMT/AFMT) calculation:
>    3.1 Applies base 1.45% rate to all calendar year earnings without limit.
>    3.2 Monitors cumulative earnings against $200,000 threshold.
>    3.3 Once threshold is reached, applies Additional FICA Medicare Tax (AFMT) at combined rate of 2.35% (1.45% base + 0.9% additional) to all subsequent earnings.
> 4. System displays comprehensive tax calculation results in Summary of Taxes table including Year, FICA SS Taxable Wages, FICA Medicare Taxable Wages, Federal/State Taxable Wages, Tax Withheld amounts, and Excludable Taxable Wages.
> 5. User manages individual FICA exemption status:
>    5.1 User accesses Edit FICA Exempt Dialog from Event Case Overview Summary of Taxes component.
>    5.2 User configures FICA SS Exempt indicator to exempt individual from Social Security tax.
>    5.3 User configures FICA Medicare Exempt indicator to exempt individual from Medicare tax.
>    5.4 User saves exemption configuration, triggering system-wide recalculation of all payments (past and future) in the actual Payment Schedule.
>    5.5 **Alternate Flow - Cancellation**: If user clicks Cancel, system displays confirmation modal asking 'Are you sure you want to close this form?' with Yes/No options; selecting Yes closes dialog without saving, selecting No returns user to dialog.
> 6. System applies exemption status to exclude exempt individuals from applicable FICA tax calculations for all affected payments.
> 7. System establishes default exemption status for new Event Cases:
>    7.1 Inherits default values from Individual Customer tax exemption profile for both FICA SS and Medicare exemptions.
>    7.2 If no exemption value exists, defaults both indicators to No (False).
>    7.3 **Exception**: For GIP product in BE jurisdiction, system defaults both exemption indicators to Yes (True).

---

#### Feature: Interest
- **Role**: Claims Payment Processor
- **Action**: automatically calculate state-specific interest amounts on payment template allocations based on configurable rules, apply thresholds, and generate corresponding payment additions and splits
- **Value**: accurate interest calculations are applied in compliance with state regulations, ensuring claimants receive proper interest payments without manual calculation errors

**Description:**

> **As a** Claims Payment Processor,
> **I want to** automatically calculate state-specific interest amounts on payment template allocations based on configurable rules, apply thresholds, and generate corresponding payment additions and splits,
> **so that** accurate interest calculations are applied in compliance with state regulations, ensuring claimants receive proper interest payments without manual calculation errors.


**Key Capabilities:**

> 1. System determines which state(s) to use for interest calculations based on allocation configuration and loss type:
>    1.1 If allocation has an interest state override code set, use that state exclusively.
>    1.2 If loss type is 'Death' and no override exists, evaluate interest across three states: beneficiary state, decedent state, and plan holder state.
>    1.3 For all other loss types without override, use only the beneficiary state from the allocation.
>
> 2. System retrieves state-specific interest calculation rules from configuration data source for each applicable state, including interest rate, threshold amounts, time thresholds, calculation method (compound/simple, annual/monthly), and day calculation type (Proof of Loss/Date of Loss/Date of Service).
>
> 3. System establishes calculation parameters for each state:
>    3.1 Determines the 'paid up to date' by using the allocation's interest paid-up-to date if specified, otherwise defaults to current payment date.
>    3.2 Calculates number of days late based on configured day type by subtracting the relevant reference date (POL received date, DOL, or DOS) from the paid-up-to date.
>    3.3 Identifies the calculation base amount using allocation's interest calculate-on amount if specified, otherwise uses allocation gross amount.
>    3.4 Validates calculation inputs and flags as invalid if interest rate is missing or number of days late is negative or not set.
>
> 4. System calculates interest amount for each state using applicable formula:
>    4.1 If allocation has an interest override amount set, uses that value directly and bypasses formula calculation.
>    4.2 If validation failed, sets interest amount to zero.
>    4.3 For annual compound interest: Interest Amount = Calculate On Amount × ((1 + Interest Rate / 365) ^ Number Of Days Late) - Calculate On Amount.
>    4.4 For annual simple interest: Interest Amount = Number Of Days Late × (Interest Rate / 365) × Calculate On Amount.
>    4.5 For monthly simple interest: Interest Amount = Number Of Days Late × (Interest Rate / 30) × Calculate On Amount.
>    4.6 Applies threshold rules: sets interest amount to zero if calculated amount is below configured threshold amount OR number of days late is below configured time threshold.
>
> 5. System selects the applicable state result by identifying which state calculation produced the highest interest amount.
>
> 6. System generates a payment template addition record with type 'INTEREST' containing all calculation metadata (state, rate, thresholds, paid-up-to date, days late, calculation method) and assigns a unique addition number with prefix 'A'.
>    6.1 If no applicable state exists (all calculations resulted in zero or invalid), skips addition generation.
>
> 7. System creates an allocation addition split result linking the generated addition to the allocation with the calculated interest amount as the applied amount.
>    7.1 If interest amount equals zero, generates the template addition but skips the split result creation.
>
> 8. System adjusts the payment item gross amount to zero if the allocation is designated as interest-only, otherwise retains the original gross amount.

---

### Epic: Payment List

#### Feature: Payment List
- **Role**: Claim Adjuster
- **Action**: view, manage, and execute actions on claim payment records including regular payments, underpayments, and deduction payments across their lifecycle states
- **Value**: payment operations are efficiently tracked, controlled, and executed with appropriate authorization and audit trail, ensuring accurate financial processing and compliance

**Description:**

> **As a** Claim Adjuster,
> **I want to** view, manage, and execute actions on claim payment records including regular payments, underpayments, and deduction payments across their lifecycle states,
> **so that** payment operations are efficiently tracked, controlled, and executed with appropriate authorization and audit trail, ensuring accurate financial processing and compliance.


**Key Capabilities:**

> 1. User views payment records in the Payments & Recoveries section on Case Overview page, displaying Regular Payments, Underpayments, and Deduction Payments in tabular format with key information: Post Date, Transaction Type/ID, Claim types with ASO tags, Payee information, Payment amounts with status indicators, Coverage name and benefit periods (for Absence claims), and Payment method details.
> 2. User sorts payment list by Post Date, Payment Made To/From, or Payment Amount in ascending/descending order, with pagination displaying 5 records per page.
> 3. User expands individual payment records using fold/unfold buttons to view detailed allocation information:
>    3.1 For Life/Critical Illness/Hospital Indemnity products: Indemnity amounts (or Expense for expense payments), Deductions grouped by type (displayed as red negative values), Interest amounts, Indebtedness, and Restored Death Benefit.
>    3.2 For Absence products: GBA (Gross Benefit Amount), Offsets grouped by type with date ranges (displayed as red negative values), AGBA (Adjusted Gross Benefit Amount), Deductions with date ranges, Taxes (Federal, FICA, State) with date ranges, Rehabilitation amounts with date ranges, and COLA with detailed calculation information including percentage type, accumulated percentage, and increase type.
> 4. User views EOB Remarks as hyperlinks with mouseover tooltip display for additional payment details.
> 5. User accesses 'Select Payments Action' dropdown to execute schedule-level operations, with available actions dynamically displayed based on payment schedule status:
>    5.1 For Open status: Create Payment, Update Payment, Cancel All Payments (hidden if issued payments exist), Generate Payment (if schedule exists), Post Recovery, and Authority Approval button for users with Activate Payment Schedule privilege (changes status from Open to Active when clicked).
>    5.2 For Active status: Create Payment, Update Payment, Suspend All Payments, Cancel All Payments (hidden if issued payments exist), Generate Payment, and Post Recovery.
>    5.3 For Suspended status: Create Payment, Update Payment, Unsuspend All Payments, Cancel All Payments (hidden if issued payments exist), Generate Payment (if schedule exists), and Post Recovery.
> 6. User executes Generate Payment action to post payments that have reached their post dates, transitioning status from Pending Post to Issued.
> 7. User executes schedule-level actions (Suspend/Unsuspend/Cancel All Payments) with system displaying confirmation modal, executing command via REST API, and providing success/error notification with automatic status and action dropdown refresh.
> 8. User manages upcoming payments (where paymentDate > lastGeneratedPaymentDate) with system displaying only Payment Schedules with status 'Open', 'Active', or 'Suspended', without three-dots action menu.
> 9. User manages posted payments/single payments (where paymentDate ≤ lastGeneratedPaymentDate) retrieved via PaymentSearch API, with Payment Method details (EFT with masked account numbers, Check) displayed after issuance.
> 10. User executes payment-level actions on Issued payments via three-dots ellipsis menu:
>    10.1 Request Issue (disabled for ATP claims).
>    10.2 Decline/Void Payment with confirmation modal and status update notification.
>    10.3 Request Stop with payment stop failure alerts displayed if request fails.
> 11. User manages Underpayments with additional actions in ellipsis menu:
>    11.1 Approve Payment (available for Pending Approval status, requires Approve Underpayment privilege) with confirmation modal and status update.
>    11.2 Disapprove Payment to cancel underpayment with reason message requirement.
> 12. System integrates with Payment Hub backend services via DXP CAP Adjuster API for all payment operations, ensuring real-time status synchronization and payment method execution.
> 13. System supports localization with multiple currency locales (USD, GBP) and date formats (MM/DD/YYYY or DD/MM/YYYY) based on user locale.

---

### Epic: Payment Lifecycle/Actions

#### Feature: Payment Lifecycle / Payment Actions
- **Role**: Claim Adjuster
- **Action**: manage the complete lifecycle of claim payments from creation through issuance, including handling exceptions and alternate payment scenarios
- **Value**: payments are processed accurately, efficiently, and in compliance with business rules while maintaining appropriate state tracking and audit trails throughout the payment lifecycle

**Description:**

> **As a** Claim Adjuster,
> **I want to** manage the complete lifecycle of claim payments from creation through issuance, including handling exceptions and alternate payment scenarios,
> **so that** payments are processed accurately, efficiently, and in compliance with business rules while maintaining appropriate state tracking and audit trails throughout the payment lifecycle.


**Key Capabilities:**

> 1. User initiates payment creation from Claim or Event Case Overview page, generating a unique payment number and setting initial state to 'Approved'.
> 2. User requests payment issuance, transitioning the payment from 'Approved' to 'Issue Requested' state.
>    2.1 If payment issue request fails to reach Payment Hub, the system automatically reverts payment to 'Approved' state for retry.
> 3. System processes payment issuance, sending payment information to check-writing system or bank integration layer and updating state to 'Issued'.
>    3.1 When the issued payment is the last one from its payment schedule, system evaluates Payment Schedule completion rules and triggers Payment Schedule completion command if applicable.
> 4. User may cancel an approved payment before issuance, optionally adding a cancellation message and setting state to 'Canceled' (terminal state).
> 5. User may request to stop an issued payment (primarily for CHECK method), transitioning state to 'Stop Requested' and sending stop request to Payment Hub.
>    5.1 If Payment Hub successfully stops the payment, system automatically updates state to 'Failed' with failure reason.
>    5.2 If Payment Hub cannot stop the payment, system automatically reverts state to 'Issued', indicating payment will be paid.
> 6. System handles payment failures at any stage (voided, stopped, or declined) by executing Fail Payment command and updating state to 'Failed' with appropriate failure reason message (terminal state).
> 7. User accesses payment management capabilities through Payments and Recoveries List and Payment Allocations List sections on Claim or Event Case Overview.
> 8. System supports both manual payment creation and automated payment generation via recurring job scheduling.
> 9. System enforces privilege-based access control for all payment lifecycle commands to ensure appropriate authorization levels.

---

### Epic: Payment Approval Flow

#### Feature: Payment Approval Flow
- **Role**: Claim Adjuster
- **Action**: request and obtain authority approval for payment schedules that exceed my authorization limit
- **Value**: high-value payments are properly reviewed and approved by authorized personnel before activation, ensuring financial controls and compliance

**Description:**

> **As a** Claim Adjuster,
> **I want to** request and obtain authority approval for payment schedules that exceed my authorization limit,
> **so that** high-value payments are properly reviewed and approved by authorized personnel before activation, ensuring financial controls and compliance.


**Key Capabilities:**

> 1. User creates a payment schedule with a gross amount that exceeds their configured authority limit for the applicable line of business.
> 2. System executes authority validation via BR>Case Payment Schedule Activation business rule and places the payment schedule in Pending Approval status.
> 3. System displays Authority Approval button and warning icon in the Payments & Recoveries section to indicate approval is required.
> 4. User can view the reason for pending approval by clicking the warning icon, which displays an authority limit violation message specific to the line of business.
> 5. User attempts to approve the payment schedule by clicking the Authority Approval button.
>    5.1. If the user lacks sufficient authority limit, the system displays an error message and denies the approval action.
>    5.2. If the user has sufficient authority limit, the system executes the Activate Payment Schedule logic and changes the payment schedule status to Active.
> 6. User with insufficient authority must escalate to a user with sufficient authority level to complete the approval.
> 7. Upon successful authority approval, the payment schedule is activated and becomes eligible for payment generation.
>    7.1. If the Payee's Preferred Payment Method is Check or EFT and valid, payment generation proceeds normally.
>    7.2. If the Payee's Preferred Payment Method is not Check/EFT or does not exist, the system cancels the single payment and exits the flow.

---

### Epic: Recovery Payment

#### Feature: Post Recovery action
- **Role**: Claims Financial Specialist
- **Action**: manage the complete lifecycle of recovery payments from initiation through issuance, cancellation, stop requests, and failure handling, and create or manage recovery records within the claims payment system
- **Value**: recovery payments are accurately tracked, controlled through each state transition, and properly integrated with payment processing systems while maintaining comprehensive audit trails and handling exceptions

**Description:**

> **As a** Claims Financial Specialist,
> **I want to** manage the complete lifecycle of recovery payments from initiation through issuance, cancellation, stop requests, and failure handling, and create or manage recovery records within the claims payment system,
> **so that** recovery payments are accurately tracked, controlled through each state transition, and properly integrated with payment processing systems while maintaining comprehensive audit trails and handling exceptions.


**Key Capabilities:**

> 1. User accesses Payments & Recoveries information from the Claim Overview page to view and manage recovery payment records.
> 2. User creates new recovery payment with unique payment number following the Financial Transaction Number Generation pattern and sets initial state to Approved.
> 3. User requests payment issuance, which updates state to Issue Requested and initiates automated payment issue process through the Payment Hub.
> 4. System issues payment by updating state to Issued and sends payment information to check-writing system or bank integration layer.
>    4.1 If the payment is the last one from the schedule, system executes Claim Payment Schedule completion rules and determines whether to trigger Payment Schedule completion command.
> 5. User monitors payment state transitions through available states: Approved, Canceled, Issue Requested, Issued, Stop Requested, and Failed.
> 6. User performs post-recovery actions on existing recovery records from the Event Case or Claim Overview Payment List.
> 7. **Alternate Flow - Cancel Payment Before Issuance**: If payment needs to be canceled before or during issue process, user cancels payment by adding optional cancellation message, updating state to Canceled (payment must not be issued).
> 8. **Alternate Flow - Payment Issue Failure**: If payment cannot be sent to Payment Hub during issue process, system automatically executes Request Issue Payment Failed command, returning payment to Approved state for retry after issue resolution.
> 9. **Alternate Flow - Stop Issued Payment**: If payment needs to be stopped after issuance, user requests stop payment which updates state to Stop Requested and sends stop request to Payment Hub; state automatically updates to either Issued or Failed based on stop success.
>    9.1 If Payment Hub fails to stop payment, user or system executes Cancel Request Stop Payment command, returning state to Issued (payment will be paid).
> 10. **Alternate Flow - Payment Failure Handling**: If payment fails due to third party or system issues, user or system updates payment state to Failed and records failure reason (Voided, Stopped - Check, or Declined - EFT) as provided by third party or user.

---
## Initiative: Manage Claim Balances

### Epic: Recalculation Triggers

#### Feature: Recalculation Flow
- **Role**: Claim Adjuster
- **Action**: ensure claim balances are automatically recalculated when triggering events occur (e.g., payment posting, reserve adjustment, recovery entry, or transaction reversal)
- **Value**: financial accuracy is maintained in real-time and claim reserves reflect the most current obligation without manual intervention

**Description:**

> **As a** Claim Adjuster,
> **I want to** ensure claim balances are automatically recalculated when triggering events occur (e.g., payment posting, reserve adjustment, recovery entry, or transaction reversal),
> **so that** financial accuracy is maintained in real-time and claim reserves reflect the most current obligation without manual intervention.


**Key Capabilities:**

> 1. System automatically triggers balance recalculation when any of the following events occur:
>    1.1 A new payment is posted to the claim
>    1.2 An existing payment is modified or reversed
>    1.3 Claim reserves are increased or decreased
>    1.4 A recovery or subrogation amount is recorded
>    1.5 A transaction is voided or reversed
>    1.6 Deductible or coinsurance amounts are applied
> 2. Upon trigger event detection, system initiates recalculation workflow that:
>    2.1 Captures the current state of all financial transactions associated with the claim
>    2.2 Calculates total incurred amount (reserves + payments)
>    2.3 Determines outstanding balance (reserves - payments)
>    2.4 Applies any recoveries, salvage, or subrogation amounts
>    2.5 Adjusts for policy limits, deductibles, and coinsurance
> 3. System processes recalculation in real-time or near-real-time:
>    3.1 For simple transactions, calculation completes synchronously before transaction confirmation
>    3.2 For complex multi-coverage or multi-claimant scenarios, calculation may process asynchronously with status notification
> 4. Recalculation engine applies business rules consistently:
>    4.1 Respects coverage limits and does not allow balances to exceed policy maximums
>    4.2 Applies payment priority rules when multiple coverages are involved
>    4.3 Handles split payments and partial settlements appropriately
> 5. System maintains complete audit trail:
>    5.1 Records timestamp and triggering event for each recalculation
>    5.2 Logs before and after balance states
>    5.3 Captures user or system process that initiated the trigger
> 6. Upon successful recalculation:
>    6.1 Updated balances are immediately reflected in claim summary views
>    6.2 Related financial reports are refreshed
>    6.3 Any downstream systems or interfaces are notified of balance changes
> 7. If recalculation encounters errors:
>    7.1 System logs detailed error information for investigation
>    7.2 Transaction may be held in pending state pending resolution
>    7.3 Appropriate user notifications or alerts are generated

---

#### Feature: Recalculation due class change
- **Role**: Claims System
- **Action**: automatically recalculate claim balances and financial reserves when a claimant's classification changes
- **Value**: claim financials remain accurate and reflect the current benefit entitlements based on the updated claimant classification

**Description:**

> **As a** Claims System,
> **I want to** automatically recalculate claim balances and financial reserves when a claimant's classification changes,
> **so that** claim financials remain accurate and reflect the current benefit entitlements based on the updated claimant classification.


**Key Capabilities:**

> 1. System monitors claimant classification fields for any changes throughout the claim lifecycle.
> 2. Upon detection of a class change event, system automatically initiates a recalculation process for all affected claim balances.
> 3. Recalculation engine re-evaluates benefit entitlements, coverage limits, deductibles, and co-insurance percentages based on the new classification.
> 4. System updates all financial reserves, payment schedules, and outstanding balance amounts to reflect the new class-based benefit structure.
> 5. All recalculated values are logged with timestamps, reason codes, and audit trail entries linking to the class change trigger event.
> 6. System generates notifications or work queue items for claims adjusters when recalculation results in significant financial variance requiring review.

---

### Epic: Manage Balances

#### Feature: Balancing per Payee and claim
- **Role**: Claim Adjuster
- **Action**: manage payment balances by reviewing discrepancies between scheduled and issued payments per payee and claim, and apply appropriate balance resolution actions (reduce payment, post recovery, waive overpayment, pay underpayment, or add external overpayment)
- **Value**: payment accuracy is maintained, overpayments and underpayments are systematically addressed, and accumulators reflect the true financial state of each claim

**Description:**

> **As a** Claim Adjuster,
> **I want to** manage payment balances by reviewing discrepancies between scheduled and issued payments per payee and claim, and apply appropriate balance resolution actions (reduce payment, post recovery, waive overpayment, pay underpayment, or add external overpayment),
> **so that** payment accuracy is maintained, overpayments and underpayments are systematically addressed, and accumulators reflect the true financial state of each claim.


**Key Capabilities:**

> 1. System automatically triggers payment recalculation when event case, claim, or benefit details are updated, or when user manually changes payment allocations through payment management UI.
> 2. Case and claim are readjudicated upon update, and applicability rules determine if new claims should be automatically created based on new information (e.g., death event triggers new claim types).
> 3. Balance service calculates payment discrepancies by comparing issued payment allocations with scheduled payment allocations, considering issued balance transaction allocations and expenses.
> 4. User reviews balance information by selecting a payee in the Balance UI, where balance is displayed per payee (Balance = 0 indicates no discrepancy; Balance > 0 indicates underpayment/carrier owes money; Balance &lt; 0 indicates overpayment/insured owes money).
&gt; 5. System automatically performs self-balancing by checking if balance items can offset each other and generates self-balance transactions to maintain ledger and accumulator accuracy.
> 6. User applies balance resolution actions through Balance UI component Action menu based on balance state and business circumstances:
>    6.1. **Reduce Payment (Overpayment Withholding)** - When overpayment exists (Balance &lt; 0) AND future payments are planned:
&gt;       6.1.1. User adds overpayment withholding and specifies amount to withhold.
>       6.1.2. System automatically withholds specified amount during payment scheduling from future payments until overpayment is eliminated.
>       6.1.3. Withholding amount is considered in total balance only when payment with withholding is issued.
>       6.1.4. Accumulator is reverted when payment with overpayment withholding is issued.
>    6.2. **Post Recovery** - When overpayment exists (Balance &lt; 0) AND no future payments exist to withhold:
&gt;       6.2.1. User adds recovery to record that amount has been returned without consequent payment transactions.
>       6.2.2. System automatically generates recovery payment in 'issued' status.
>       6.2.3. Recovery transaction becomes visible in Balance UI transaction section and can be previewed in Payment and Recovery List UI.
>       6.2.4. Amount is considered in total balance immediately upon saving.
>       6.2.5. Accumulator is reverted when recovery achieves 'issued' status.
>       6.2.6. Recovery follows simple two-state lifecycle: Issued → Cancelled (terminal state).
>    6.3. **Waive Overpayment** - When overpayment exists (Balance &lt; 0) AND carrier decides to forgive overpayment:
&gt;       6.3.1. User adds overpayment waive transaction to reduce overpayment by amount carrier will not attempt to recover.
>       6.3.2. Amount is considered in total balance immediately upon saving.
>       6.3.3. Accumulator is reverted when overpayment waive achieves 'issued' status.
>       6.3.4. Waive follows simple two-state lifecycle: Issued → Cancelled (terminal state).
>    6.4. **Pay Underpayment** - When underpayment exists (Balance > 0):
>       6.4.1. User adds underpayment transaction with optional selection to compensate withholding.
>       6.4.2. System automatically generates underpayment payment with 'pending' status.
>       6.4.3. Payment can be previewed in Payment and Recovery List UI.
>       6.4.4. Payment undergoes standard approval process.
>       6.4.5. Payment is issued following standard business process including integration with payment hub.
>       6.4.6. Amount is considered in total balance only upon issuing underpayment.
>       6.4.7. Accumulator is reverted during issuing and generation process.
>       6.4.8. Underpayment follows full payment processing lifecycle identical to regular payments.
>    6.5. **Add External Overpayment** - When overpayment occurred outside specific Claims Case and Claim (can be added regardless of current balance state):
>       6.5.1. User adds external overpayment to post overpayment that occurred outside the specific Claims Case and Claim.
>       6.5.2. Amount is considered in total balance immediately upon saving.
>       6.5.3. External overpayment does NOT impact accumulator.
>       6.5.4. External overpayment follows simple two-state lifecycle: Issued → Cancelled (terminal state).
> 7. When any balancing payment changes status (e.g., to cancelled), system may reverse amount allocations and impact accumulator amounts accordingly.
> 8. User can refresh policy data for both AH Disability and LA Life claims through Claim Overview interface.
> 9. User can view all historical changes to cases and claims through History and Case Overview interfaces.

---

#### Feature: Balance Activities / Recalculated Payments / Payment Withholdings
- **Role**: Claim Adjuster
- **Action**: view comprehensive payment balance information for specific payees within event cases or for selected payee-claim combinations through the Payments & Recoveries Component
- **Value**: I can understand and monitor payment balances associated with payees and claims, enabling accurate financial oversight and reconciliation

**Description:**

> **As a** Claim Adjuster,
> **I want to** view comprehensive payment balance information for specific payees within event cases or for selected payee-claim combinations through the Payments & Recoveries Component,
> **so that** I can understand and monitor payment balances associated with payees and claims, enabling accurate financial oversight and reconciliation.


**Key Capabilities:**

> 1. User accesses the Payments & Recoveries Component from the Case overview page to view balance and recalculation records.
> 2. System displays comprehensive payment balance information for all payees associated with the event case by default.
> 3. User can filter balance information to view specific payee and claim combinations, enabling focused review of financial obligations.
> 4. Balance list presents detailed records including balance activities, recalculated payment information, and payment withholding data for selected scope.
> 5. User reviews balance and recalculation records to understand current payment status, historical balance changes, and outstanding financial obligations for payees and claims.

---

### Epic: Taxes

#### Feature: Tax & Withholding Management
- **Role**: Claim Adjuster
- **Action**: view, manage, and track tax-related information including withholdings for event cases and claims
- **Value**: tax obligations are accurately recorded, compliant, and easily auditable throughout the claim lifecycle

**Description:**

> **As a** Claim Adjuster,
> **I want to** view, manage, and track tax-related information including withholdings for event cases and claims,
> **so that** tax obligations are accurately recorded, compliant, and easily auditable throughout the claim lifecycle.


**Key Capabilities:**

> 1. User accesses tax-related information through a dedicated Taxes Tab interface that displays tax summary information for the selected event case or claim.
> 2. User reviews existing withholding entries through a Withholdings List that displays all current withholding records associated with the event case or claim.
> 3. User manages withholding entries through the Manage Withholdings workflow:
>    3.1 User adds new withholding entries by initiating the Add process, entering required withholding details (such as tax type, amount, jurisdiction), and saving the entry to the system.
>    3.2 User modifies existing withholding entries by selecting a withholding record, editing the pre-populated details, and saving the updated information.
>    3.3 User views detailed information for individual withholding entries to review tax obligation details.
> 4. User accesses comprehensive tax overview through the Summary of Taxes functionality, which aggregates and displays consolidated tax data across all withholdings for the event case or claim.
> 5. All withholding changes are tracked and reflected in real-time across the tax summary views and withholdings list.

---

#### Feature: Summary of Taxes
- **Role**: Claim Adjuster
- **Action**: access, view, and manage tax-related data including year-to-date earnings and FICA exemption indicators within the Claims module
- **Value**: tax-related earnings data and exemption statuses are accurately tracked and maintained for compliant claim processing and reporting

**Description:**

> **As a** Claim Adjuster,
> **I want to** access, view, and manage tax-related data including year-to-date earnings and FICA exemption indicators within the Claims module,
> **so that** tax-related earnings data and exemption statuses are accurately tracked and maintained for compliant claim processing and reporting.


**Key Capabilities:**

> 1. User accesses the Summary of Taxes functionality from the Claims module to manage tax-related data.
> 2. User manages year-to-date (YTD) earnings records:
>    2.1 User views the comprehensive earnings list associated with the claim.
>    2.2 User adds new YTD earnings records when additional earnings data needs to be captured.
>    2.3 User edits existing YTD earnings records to correct or update earnings information.
> 3. User manages FICA exemption indicators:
>    3.1 User tracks exemption statuses associated with specific claims.
>    3.2 User maintains FICA exemption indicator records to reflect current exemption eligibility.
> 4. All tax-related data modifications are recorded and maintained within the claim record for audit and reporting purposes.

---

### Epic: Deductions

#### Feature: UI Display / Add Deduction
- **Role**: Claim Adjuster
- **Action**: add, edit, and manage financial deductions on submitted Event Cases with existing Claims, including sponsor-based health and welfare deductions and non-sponsor-based court-ordered deductions, and ensure appropriate deduction payments are generated when creating claim payments
- **Value**: claim payment amounts are accurately reduced and diverted to appropriate third parties or sponsors per legal obligations and policy terms, ensuring compliance with court orders, tax regulations, and employment benefits agreements

**Description:**

> **As a** Claim Adjuster,
> **I want to** add, edit, and manage financial deductions on submitted Event Cases with existing Claims, including sponsor-based health and welfare deductions and non-sponsor-based court-ordered deductions, and ensure appropriate deduction payments are generated when creating claim payments,
> **so that** claim payment amounts are accurately reduced and diverted to appropriate third parties or sponsors per legal obligations and policy terms, ensuring compliance with court orders, tax regulations, and employment benefits agreements.


**Key Capabilities:**

> 1. User navigates to the Event Case overview page and accesses the 'Deductions' tab to view existing deductions and add new deduction records.
> 2. User initiates deduction creation by selecting the deduction type and linking it to one or more existing Claims within the Event Case.
>    2.1 For CI, HI, and TL claims, system restricts deduction type selection to only Child Support and Wage Garnishment, and enforces percentage-based calculation method (weekly/monthly amounts not permitted).
>    2.2 System prevents deduction creation if no Claims exist in the Event Case (at least one Claim is prerequisite).
>    2.3 System prevents deduction creation for Life and Supplemental Benefits Claims when deduction type is Tax Withholding.
> 3. User enters deduction details including amount or percentage calculation, effective dates, and third party information if applicable to the deduction type.
>    3.1 For Sponsor-based Health & Welfare deductions (Insurance Premium, Saving Accounts, Union Dues, job-related, non-job-related), system captures data for aggregation across Sponsor's claims with external reporting to employer.
>    3.2 For Non-sponsor-based deductions (Child Support, Wage Garnishment), system captures third party payee information for automatic secondary payment generation.
> 4. User saves the deduction record, triggering system to update the Event Case and execute automation processes (case created, submitted, finalized workflow stages).
> 5. System generates appropriate BAM messages (Update BAM, Create BAM, Submit BAM) to maintain audit trail and support system integration.
> 6. When user creates a payment for a claim that has bound deductions, system automatically processes deduction application:
>    6.1 System maps deduction information from Event Case into the payment template.
>    6.2 Payment scheduler OpenL rules are invoked to generate scheduled deduction payment records.
>    6.3 System stores master payment and deduction payment records in payment schedule entity.
>    6.4 Payment relationship builder (_api_payment_generation OpenL) establishes masterPaymentNumber linkage between master payment and associated deduction payments.
>    6.5 System executes generatePayment workflow: invokes payment endpoint, loops through payment records, invokes initPayment command for each record, and generates actual master payment and deduction payment transactions.
>    6.6 For Child Support or Wage Garnishment deductions, system automatically generates secondary Deduction Payment to the specified third party.
>    6.7 For Sponsor-based deductions, system aggregates deduction amounts across all of the Sponsor's (Employer's) claims for external reporting and payment to Sponsor rather than generating individual third party payments.
> 7. User can edit or delete existing deductions from the Deductions List page, triggering updated BAM messages and Event Case automation processes.
> 8. System displays appropriate error messages when Kraken rules errors or OpenL rules errors occur during deduction processing, referencing Event Case Domain Rules Specification or applicable technical documentation.

---
## Initiative: Claim Party Management

### Epic: Party Information

#### Feature: View / Add Parties
- **Role**: Claim Adjuster
- **Action**: add new parties (individuals or organizations) to a case with complete contact and address information
- **Value**: all relevant parties are accurately recorded and associated with the case for proper claim processing and communication

**Description:**

> **As a** Claim Adjuster,
> **I want to** add new parties (individuals or organizations) to a case with complete contact and address information,
> **so that** all relevant parties are accurately recorded and associated with the case for proper claim processing and communication.


**Key Capabilities:**

> 1. User initiates the add party process which opens a slide-out form interface.
> 2. User selects the party type to determine whether adding an individual person or an organization.
>    2.1 When adding an individual party, user provides personal identification information including name components, date of birth, and gender selection.
>    2.2 When adding an organization party, user provides business identification information including organization name and optional tax identifiers.
> 3. User specifies contact preferences and provides corresponding contact information.
>    3.1 If phone contact is preferred, user must provide a valid phone number meeting length and format requirements.
>    3.2 If email contact is preferred (default), user must provide a valid email address.
> 4. User enters complete address information including address type, street details, and geographic location.
>    4.1 When United States is selected as country, user must provide state and zip code information with US-specific validation.
>    4.2 When operating in UK locale, system adapts field labels, formats, and validation rules to UK standards (county instead of state, UK postal code format, UK phone format).
> 5. System validates all entered data against business rules including mandatory field checks, format validations, and locale-specific requirements.
>    5.1 If validation fails, system prevents submission and displays specific error messages indicating which fields require correction.
> 6. User submits the completed party information and system persists the data by creating the customer record and establishing the party role association with the case.
> 7. Upon successful save, system returns user to the party management interface with the newly added party available for further case operations.
>    7.1 If user cancels the operation before submission, system prompts for confirmation and discards all entered data if confirmed.

---

#### Feature: Individual / Organization
- **Role**: Claim Adjuster
- **Action**: add a new party (Individual or Organization) to an existing case by providing complete party information, contact details, and address, with dynamic field requirements based on party type, context, and system locale
- **Value**: all relevant parties (e.g., claimants, members, beneficiaries, organizations) are accurately captured and linked to the case, ensuring complete case documentation and enabling proper communication and processing workflows

**Description:**

> **As a** Claim Adjuster,
> **I want to** add a new party (Individual or Organization) to an existing case by providing complete party information, contact details, and address, with dynamic field requirements based on party type, context, and system locale,
> **so that** all relevant parties (e.g., claimants, members, beneficiaries, organizations) are accurately captured and linked to the case, ensuring complete case documentation and enabling proper communication and processing workflows.


**Key Capabilities:**

> 1. User initiates 'Add New Party' action from an open case, which launches a slide-out form window.
> 2. User selects the party type (Individual or Organization), which dynamically adjusts the form fields and validation rules.
> 3. User completes the party information section:
>    3.1 For Individual: First Name, Last Name (mandatory), Middle Name (optional), Date of Birth (conditional mandatory based on context), Gender (optional).
>    3.2 For Organization: Organization Name (mandatory), Tax Identification (optional), EIN (optional, validated format).
>    3.3 If the party is being added as a Member, Subject of Case, or Beneficiary, Date of Birth becomes mandatory.
> 4. User provides contact information and selects contact preference:
>    4.1 If 'Phone' is selected as Contact Preference, Phone Number becomes mandatory (10-20 digits, locale-specific masking applied).
>    4.2 If 'Email' is selected as Contact Preference (default), Email Address becomes mandatory.
>    4.3 The non-preferred contact method remains optional but is validated if provided.
> 5. User enters address information with mandatory fields including Address Line 1, Country, City, State/Province (or County for UK locale), and Zip/Postal Code:
>    5.1 If system locale is set to United Kingdom (en_GB), date format changes to DD/MM/YYYY, State/Province is relabeled as 'County' with UK-specific values, and Zip Code validates UK postcode format.
>    5.2 If system locale is set to USA (default), date format is MM/DD/YYYY, State/Province uses US states, and Zip Code validates US format (5 or 9 digits).
> 6. User clicks 'Add Party' button to save the party information, which triggers a REST API call to persist data to IndividualCustomer or OrganizationCustomer endpoints and assigns the party role to the case.
> 7. Upon successful save, the system returns the user to the Add Party window and the party is linked to the case.
> 8. Alternate Flow - User Cancels Entry:
>    8.1 If user clicks 'Cancel' button during form entry, system displays a confirmation modal ('Are you sure you want to close this form?').
>    8.2 If user selects 'Yes', form closes without saving and user returns to previous screen.
>    8.3 If user selects 'No', modal closes and user remains in form to continue editing.
> 9. Alternate Flow - User Closes All Windows:
>    9.1 If user clicks 'Close (X)' button during form entry, system displays a confirmation modal ('Are you sure you want to close this form?').
>    9.2 If user selects 'Yes', all slide-out windows close without saving and user returns to main case view.
>    9.3 If user selects 'No', modal closes and user remains in form to continue editing.

---

#### Feature: Vendor (Individual / Facility)
- **Role**: Claim Adjuster
- **Action**: search for and add a vendor (individual or facility) to an event case, configure their service type filters, and assign an EFT/ACH payment method
- **Value**: vendor relationships are properly established with accurate payment routing for claim-related services

**Description:**

> **As a** Claim Adjuster,
> **I want to** search for and add a vendor (individual or facility) to an event case, configure their service type filters, and assign an EFT/ACH payment method,
> **so that** vendor relationships are properly established with accurate payment routing for claim-related services.


**Key Capabilities:**

> 1. User initiates vendor addition by opening the Add New Party Form and selects party type (Individual, Organization, Vendor Individual, or Vendor Facility) using radio button controls.
> 2. For vendor party types, user searches for vendors by entering name/location criteria and optionally filtering by service type(s) from a multi-select dropdown populated from the Provider Service lookup.
> 3. System displays paginated search results (6 per page) showing matching vendors with their name, location, and assigned service types, with single-selection via radio button.
> 4. User selects a vendor from search results, which enables the Service Types Filter (pre-populated with the vendor's available services) for additional refinement.
> 5. Upon vendor selection, system enables the Payment Method Configuration dropdown and retrieves all active EFT/ACH payment methods associated with the selected vendor from Provider Management Studio.
>    5.1. If an inactive payment method was previously used as a claim payment method, system displays it with an '(Inactive)' suffix to indicate its status.
>    5.2. User may add a new EFT/ACH payment method during this process, which automatically becomes the default selection upon creation.
>    5.3. User may remove a selected payment method if needed before finalizing the configuration.
> 6. User saves the vendor configuration, and system creates the vendor relationship to the event case with relationship type 'Case' by default, then closes all slide-out windows.
>    6.1. If user clicks Close button after vendor selection but before saving, system returns to the previous window while retaining selected vendor data for later resumption.
>    6.2. If user clicks Cancel button, system returns to the previous window without saving any configuration.

---
## Initiative: Integration

### Epic: Policy Integration

#### Feature: Policy Search
- **Role**: Claims System
- **Action**: integrate with the Policy system to retrieve policy information, locate applicable policy versions based on Date of Loss, and adjudicate coverages throughout the claim lifecycle
- **Value**: claims are processed against the correct policy version with accurate coverage determinations based on loss details and insured relationships

**Description:**

> **As a** Claims System,
> **I want to** integrate with the Policy system to retrieve policy information, locate applicable policy versions based on Date of Loss, and adjudicate coverages throughout the claim lifecycle,
> **so that** claims are processed against the correct policy version with accurate coverage determinations based on loss details and insured relationships.


**Key Capabilities:**

> 1. System retrieves policy image from Policy system for all policies found based on Event Date.
>   1.1 System excludes archived policy versions from the response during retrieval.
> 2. System locates the applicable policy version based on Date of Loss (DOL).
>   2.1 For CapAbsence claim types, system applies business rule BR>CapAbsence>Locate Policy Version to determine the correct policy version.
>   2.2 For CapNonAbsence claim types, system applies business rule BR>CapNonAbsence>Locate Policy Version to determine the correct policy version.
> 3. System adjudicates or re-adjudicates applicable coverages and benefits based on Loss type and Relationship to Insured.
>   3.1 For CWCP claims, system maps Relationship to Insured to the Insured Role in CP, which must be one of: Primary Insured, Spouse, or Child.
>   3.2 For CWMP claims, system derives Relationship to Insured from CEM (Customer Entity Management).
> 4. System executes the integration workflow during multiple claim lifecycle events, including case creation and auto-adjudication flows.

---

### Epic: Customer Integration

#### Feature: Retrieve Customer data
- **Role**: System Integration
- **Action**: retrieve customer data from external customer management systems through API or integration layer
- **Value**: accurate and up-to-date customer information is available within the application without manual data entry

**Description:**

> **As a** System Integration,
> **I want to** retrieve customer data from external customer management systems through API or integration layer,
> **so that** accurate and up-to-date customer information is available within the application without manual data entry.


**Key Capabilities:**

> 1. System initiates customer data retrieval request to external customer management system using a unique customer identifier (e.g., Customer ID, Policy Number, SSN).
> 2. Integration layer establishes secure connection with the external system using appropriate authentication and authorization protocols.
> 3. System receives customer data payload including demographics, contact information, policy associations, and other relevant attributes.
> 4. Retrieved customer data is validated for completeness and data quality before being persisted or displayed in the application.
> 5. System handles integration responses and updates the application state accordingly.
>   5.1 If customer is found, data is made available to downstream processes or user interfaces.
>   5.2 If customer is not found, system logs the event and presents appropriate messaging.
>   5.3 If integration fails or times out, system implements retry logic or error handling procedures.
> 6. Audit trail is maintained for all customer data retrieval transactions including timestamp, requesting user, and data returned.

---

### Epic: Claim-Billing Integration

#### Feature: Integration for Premium Paid to Date
- **Role**: Claims Adjuster
- **Action**: verify policy premium payment status and paid-to-date information from the Billing system to validate coverage eligibility and process Premium Waiver adjustments
- **Value**: only coverages with premiums paid through or beyond the loss date are eligible for benefit payments, and approved premium waivers are accurately applied to policyholder billing accounts

**Description:**

> **As a** Claims Adjuster,
> **I want to** verify policy premium payment status and paid-to-date information from the Billing system to validate coverage eligibility and process Premium Waiver adjustments,
> **so that** only coverages with premiums paid through or beyond the loss date are eligible for benefit payments, and approved premium waivers are accurately applied to policyholder billing accounts.


**Key Capabilities:**

> 1. The Claims system requests and receives policy payment status from the Billing system to determine if the policy is Active/in-force, Cancelled for non-payment, or Pending cancellation.
> 2. The Claims system retrieves the 'Paid To Date' value from the Billing system.
> 3. The 'Paid To Date' value is displayed on the Claims header for adjuster visibility.
> 4. The Claims system validates coverage eligibility by comparing premium payment status and the 'Paid To Date' value against the loss date.
>    4.1 If the policy is Cancelled for non-payment or Pending cancellation, and premiums were not paid through or beyond the loss date, coverages are determined ineligible for benefit payments.
>    4.2 If premiums are paid through or beyond the loss date, coverages are determined eligible for benefit payments.
> 5. For claims with Premium Waiver coverage, the adjuster manually investigates Disability data associated with the claim.
> 6. The adjuster approves the Premium Waiver for specific periods (Approval Periods) based on disability determination.
> 7. Once an approval period is marked as both 'Approved' and 'Completed,' the Claims system prepares the data for transmission to Billing.
>    7.1 If an approval period is not marked as both 'Approved' and 'Completed,' the data is not transmitted to Billing and no premium waiver action occurs.
> 8. Approved and Completed approval period data is transmitted from the Claims system to the Billing system.
> 9. The Billing system receives the approval period data and performs premium corrections by waiving premiums for the approved periods.

---

#### Feature: Key points of inbound/outbound integration
---

### Epic: Payment Hub Integration

#### Feature: Payment Hub Integration
- **Role**: Claims Adjuster
- **Action**: process claim payments and underpayments through the integrated Payment Hub system with automated event monitoring and exception handling
- **Value**: payments are reliably issued, tracked, and reconciled across systems while maintaining accurate payment state throughout the lifecycle

**Description:**

> **As a** Claims Adjuster,
> **I want to** process claim payments and underpayments through the integrated Payment Hub system with automated event monitoring and exception handling,
> **so that** payments are reliably issued, tracked, and reconciled across systems while maintaining accurate payment state throughout the lifecycle.


**Key Capabilities:**

> 1. **Payment Issuance Initiation**: System initiates payment or underpayment issuance requests through scheduled payment issuing or underpayment issuing business processes.
> 2. **Payment Data Collection and Outbound Generation**: System collects all required payment data including payment methods and details, then generates outbound payment per requirements and creates a domain correlation ID to link Payment Hub records with Claim's Payment records.
> 3. **Payment Hub Submission**: System sends payment creation request to Payment Hub and monitors for 'Outbound Payment Created' event confirmation.
> 4. **Payment Issuance Triggering**: Upon receiving 'Outbound Payment Created' event, system triggers payment or underpayment issuance in Claims.
> 5. **Successful Payment Processing**: System monitors for 'Outbound Payment Paid' event from Payment Hub, verifies payment state is not 'StopRequested', and completes payment lifecycle.
> 6. **Payment Stop/Cancel Request Handling**:
>    6.1. User initiates stop, cancel, or fail payment request after outbound payment is created in Payment Hub.
>    6.2. System sends cancellation or fail request to Payment Hub while maintaining unchanged payment state in Claims until confirmation is received.
>    6.3. If Payment Hub cancellation fails, system executes 'cancelRequestStopPayment' or 'cancelRequestStopUnderpayment' command and displays failure notification ('Payment Stop is failed.' or 'Underpayment Stop is failed.') with INFO severity message (Code: CheckPaymentStopFail or CheckUnderPaymentStopFail).
>    6.4. If Payment Hub successfully cancels payment, system receives 'Outbound Payment Canceled' event, triggers fail payment/underpayment action, and sets appropriate message based on payment state (CheckUserStop with 'Stopped' message if state = 'Stop Requested', or CheckSystemFail with 'Voided' message if state ≠ 'Stop Requested').
> 7. **Payment Hub Processing Failure Handling**: When 'Outbound Payment Failed' event is received during Payment Hub processing, system triggers fail payment/underpayment action and sets method-specific failure messages (CheckSystemFail/'Voided' for CHECK when not stop-requested, CheckUserStop/'Stopped' for CHECK when stop-requested, EFTSystemFail/'Declined' for EFT).
> 8. **Payment Paid During Stop Request Exception**: When 'Outbound Payment Paid' event is received while payment state = 'StopRequested', system executes cancel request stop command and displays notification that payment has been paid by Payment Hub with stop failure message (Code: CheckPaymentPaidInPH or CheckUnderPaymentPaidInPH).

---
## Initiative: No-touch flow

### Epic: No-touch flow

#### Feature: Wellness benefit
- **Role**: Claims Adjuster
- **Action**: have the system automatically adjudicate and create payments for eligible Wellness benefit claims on Critical Illness, Hospital Indemnity, or Accident policies when only Wellness event type is selected
- **Value**: eligible members receive timely Wellness benefit payments without manual intervention, reducing processing time and operational costs while ensuring accurate compliance with policy rules and waiting periods

**Description:**

> **As a** Claims Adjuster,
> **I want to** have the system automatically adjudicate and create payments for eligible Wellness benefit claims on Critical Illness, Hospital Indemnity, or Accident policies when only Wellness event type is selected,
> **so that** eligible members receive timely Wellness benefit payments without manual intervention, reducing processing time and operational costs while ensuring accurate compliance with policy rules and waiting periods.


**Key Capabilities:**

> 1. System evaluates comprehensive pre-conditions to determine Wellness claim eligibility for automated adjudication, including policy status validation, event case configuration, coverage assignment, eligibility requirements, and payment method availability.
> 2. System applies the core business rule that automated payment is only created when 'Wellness' is the sole event type selected during Event Case intake, excluding claims with multiple event types (e.g., Wellness + Absence or Wellness + Hospital Services).
> 3. System verifies that the Wellness coverage settlement is in 'Approved' status, confirming that both the Claim and Wellness coverage meet all eligibility requirements.
> 4. System automatically submits the claim and changes its status to 'Open' to enable payment processing.
> 5. System creates automated payment allocations with predefined properties (Payee as Member, Wellness Visit Date as Allocation Incident Date) for each eligible policy.
> 6. System initiates scheduled payment issuing process to generate and distribute payments via member's defined payment method (Check or EFT).
> 7. After all payments are issued, system attempts automatic closure of the case and associated claims through the Auto Adjudication Automatic Closure process.
> 8. When multiple policies exist for the same member, system independently evaluates each policy against all pre-conditions and creates payment allocations only for policies that fully qualify.
>    8.1 If only one policy meets all waiting period requirements while another does not, system creates payment only for the qualifying policy (partial payment scenario).
> 9. When coverage limits are defined and reached (e.g., maximum visits per year exhausted), system sets the Gross Benefit Amount (GBA) to $0 and terminates automated payment processing.
> 10. When applicability rule fails due to multiple event types being selected, system does not create automated payment and requires manual adjudication.
> 11. When pre-conditions fail (Event Case reason is not 'Other', Subject is not the Member, policy is inactive, event dates precede policy effective date, waiting periods not satisfied, or no valid payment method), system does not assign Wellness coverage or create automated payments.

---
## Initiative: Other Configurations

### Epic: Other Configurations

#### Feature: Configure coverage-based claim properties
- **Role**: System Administrator
- **Action**: configure coverage-based claim properties and define field override capabilities for 'Gross Amount' and '# Days / # Occurrences' based on Coverage Limit Unit type, calculation method, and specific benefit types
- **Value**: the system enforces consistent business rules for field editability across different coverage configurations, preventing data entry errors and ensuring compliance with product-specific calculation logic

**Description:**

> **As a** System Administrator,
> **I want to** configure coverage-based claim properties and define field override capabilities for 'Gross Amount' and '# Days / # Occurrences' based on Coverage Limit Unit type, calculation method, and specific benefit types,
> **so that** the system enforces consistent business rules for field editability across different coverage configurations, preventing data entry errors and ensuring compliance with product-specific calculation logic.


**Key Capabilities:**

> 1. System evaluates Coverage Limit Unit type (money vs. non-money) and calculation method (auto-calculated vs. user-editable) to determine field override eligibility for coverage configurations.
> 2. System applies mutual exclusivity rule ensuring 'Gross Amount' and '# Days / # Occurrences' fields cannot be overridden simultaneously.
> 3. For money-based Coverage Limit Units:
>    3.1. When Gross Amount is auto-calculated, system allows override of 'Gross Amount' field while keeping '# Days / # Occurrences' non-overridable.
>    3.2. When Gross Amount is user-editable, system denies override for both fields as manual editing is already enabled.
> 4. For non-money-based Coverage Limit Units:
>    4.1. When Number of Units is auto-calculated, system allows override of '# Days / # Occurrences' field while keeping 'Gross Amount' non-overridable.
>    4.2. When Number of Units is user-editable, system denies override for both fields as manual editing is already enabled.
>    4.3. When Number of Units defaults to 1, system denies override for both fields maintaining the fixed default value.
> 5. System applies special restriction rules:
>    5.1. For Coverage Limit Unit 'Day' with accumulator type 'per Benefit Year' or 'Calendar Year', system denies override for both fields.
>    5.2. For specific TL benefits (Ambulance Air Benefit, Ambulance Ground Benefit, Waiver Of Premium Benefit, Wellness Benefit, Coma), system denies override for both fields.
> 6. System maintains configuration data in product-specific Excel files:
>    6.1. Individual-Coverage-based Configuration table for Individual Products (PL).
>    6.2. Group-Coverage-based Configuration table for Group Products (TL, Accident, CI, HI).
>    6.3. Group-Coverage-based Configuration table (Non-dental) for non-dental group product configurations.

---

#### Feature: Premium Paid to Date process
- **Role**: Claims Processor
- **Action**: validate that premiums are paid to date before processing claim payments, with automatic warnings and investigation tasks triggered when validation fails
- **Value**: claims are not paid when premiums are outstanding, reducing financial risk and ensuring policy compliance

**Description:**

> **As a** Claims Processor,
> **I want to** validate that premiums are paid to date before processing claim payments, with automatic warnings and investigation tasks triggered when validation fails,
> **so that** claims are not paid when premiums are outstanding, reducing financial risk and ensuring policy compliance.


**Key Capabilities:**

> 1. System validates PPTD against claim dates when claim is created with PPTD set by billing data, when claim DOL/DOI/beginning date is updated, or when payment schedule is activated for manual and automatic approval payments.
> 2. System applies claim-type-specific validation rules:
>   2.1 For STD, LTD, and SMD claims: validates that PPTD is not before Date of Loss (DOL) defined on claim header.
>   2.2 For Life, CI, HI, and ACC claims/coverages: validates that PPTD is not before DOL OR Date of Incident (DOI) OR Beginning Date of Date Range for all coverages within the claim (excluding Premium Waiver coverage).
> 3. When validation conditions are met (PPTD falls before relevant dates), system displays warning message in Claim Overview Header beside PTD field.
>   3.1 If validation conditions are not met (PPTD is greater than or equal to all relevant dates), system skips warning display and continues validation process.
> 4. System checks if payment schedule is active for the claim.
>   4.1 If payment schedule is active, system displays warning in both Create/Update Payment drawer and Allocations Detail section.
>   4.2 If payment schedule is not active, system skips payment screen warnings and proceeds to investigation task check.
> 5. System verifies whether an active investigation task named 'Premiums possibly not Paid to Date' already exists for the claim.
>   5.1 If no active task exists, system creates investigation task 'Premiums possibly not Paid to Date' for the allocated claim.
>   5.2 If active task already exists, system skips task creation to prevent duplicates.
> 6. System completes validation process after all warnings are displayed and tasks are created as needed.

---

#### Feature: Calendar Full Month Calculation
- **Role**: System Administrator
- **Action**: configure and apply full month calculation rules to determine benefit payment period end dates from given start dates
- **Value**: monthly benefits are calculated consistently across varying calendar months, month-end variations, and leap years, ensuring accurate and timely GBA payment processing

**Description:**

> **As a** System Administrator,
> **I want to** configure and apply full month calculation rules to determine benefit payment period end dates from given start dates,
> **so that** monthly benefits are calculated consistently across varying calendar months, month-end variations, and leap years, ensuring accurate and timely GBA payment processing.


**Key Capabilities:**

> 1. System evaluates benefit period start date against prioritized business rules to calculate the full month end date.
> 2. Rule evaluation follows strict priority sequence:
>    2.1 Rule 1 (Highest Priority): If start date is the last day of any month, set full month end date to the last day of the next month.
>    2.2 Rule 2 (Second Priority): If start date falls on January 28, 29, 30, or 31, set full month end date to the last day of February in the same year (automatically handling leap year variations).
>    2.3 Rule 3 (Default): If neither Rule 1 nor Rule 2 applies, calculate full month end date by adding one month to start date and subtracting one day.
> 3. System applies the first matching rule and terminates evaluation, ensuring only one calculation method is used per period.
> 4. Calculation automatically handles leap year detection when Rule 2 is applied, adjusting February end dates to the 28th or 29th accordingly.
> 5. Each successfully calculated full month period triggers one monthly GBA benefit payment.
> 6. System maintains date format consistency using ISO standard (YYYY-MM-DD) throughout all calculations.

---

#### Feature: Common Rounding Rules
- **Role**: System Administrator
- **Action**: configure and manage common rounding rules that can be applied across various calculation processes within the system
- **Value**: consistent and standardized rounding behavior is enforced across all financial calculations, ensuring accuracy, compliance, and predictability in monetary computations

**Description:**

> **As a** System Administrator,
> **I want to** configure and manage common rounding rules that can be applied across various calculation processes within the system,
> **so that** consistent and standardized rounding behavior is enforced across all financial calculations, ensuring accuracy, compliance, and predictability in monetary computations.


**Key Capabilities:**

> 1. System Administrator accesses the Other Configurations section to manage Common Rounding Rules.
> 2. Administrator defines rounding rules by specifying rounding methodologies (e.g., round up, round down, round to nearest, banker's rounding).
> 3. Administrator configures decimal precision settings for each rounding rule (e.g., round to 2 decimal places, whole numbers).
> 4. Administrator assigns descriptive names and identifiers to rounding rules for easy reference across the system.
> 5. Administrator sets the scope and applicability of each rounding rule (e.g., applicable to all calculations, specific to certain transaction types).
> 6. System validates the configured rounding rules to ensure mathematical integrity and prevents conflicting rule definitions.
> 7. Administrator saves and activates the rounding rules, making them available for use in calculation processes throughout the system.
> 8. System applies the configured rounding rules consistently across all designated financial calculations and transactions.

---

#### Feature: Timezone Support
- **Role**: System Administrator
- **Action**: configure and manage timezone settings across the insurance system to ensure accurate timestamp recording, display, and processing for multi-regional operations
- **Value**: all users see accurate, localized time information and system processes execute at the correct time regardless of geographic location

**Description:**

> **As a** System Administrator,
> **I want to** configure and manage timezone settings across the insurance system to ensure accurate timestamp recording, display, and processing for multi-regional operations,
> **so that** all users see accurate, localized time information and system processes execute at the correct time regardless of geographic location.


**Key Capabilities:**

> 1. System Administrator configures the default system timezone that serves as the baseline for all timestamp storage and backend processing.
> 2. Administrator defines supported timezones for different organizational units, branches, or user groups based on operational geography.
> 3. System allows configuration of timezone display preferences at multiple levels (system-wide, organizational unit, or individual user).
> 4. Users view all timestamps (claim submission, policy effective dates, task deadlines, audit logs) converted to their configured local timezone.
> 5. System maintains all timestamps internally in a standardized format (e.g., UTC) to ensure data consistency and enable accurate cross-timezone calculations.
> 6. Administrator configures timezone handling rules for automated processes including scheduled jobs, batch operations, and system notifications.
> 7. System provides timezone conversion capabilities for reporting and analytics to enable accurate performance tracking across regions.
> 8. Configuration supports daylight saving time (DST) adjustments automatically based on regional rules.
> 9. System displays timezone information clearly on user interfaces where timestamp context is critical (e.g., claim filing time, policy inception date).
> 10. Administrator can update timezone configurations with appropriate validation to prevent disruption to active business processes.

---
## Initiative: Auditing

### Epic: Activities

#### Feature: BAMs (Business Activity Monitoring)
- **Role**: System Administrator
- **Action**: access and monitor comprehensive documentation and development tracking for payment lifecycles and claim management processes across multiple insurance product lines
- **Value**: all stakeholders have a centralized, organized reference point for understanding, implementing, and tracking claim and payment lifecycle activities across the enterprise

**Description:**

> **As a** System Administrator,
> **I want to** access and monitor comprehensive documentation and development tracking for payment lifecycles and claim management processes across multiple insurance product lines,
> **so that** all stakeholders have a centralized, organized reference point for understanding, implementing, and tracking claim and payment lifecycle activities across the enterprise.


**Key Capabilities:**

> 1. System provides a central reference hub that aggregates documentation related to payment lifecycles and claim management processes across all insurance product lines.
> 2. Users can navigate to related documentation pages covering:
>    2.1 Payment lifecycles and case financials.
>    2.2 Underpayments and recoveries.
>    2.3 Product-specific claim processes (Dental, Pet, Life, Accident, Hospital Indemnity, and other lines).
> 3. System maintains outgoing reference links to:
>    3.1 BAM-related functional documentation (e.g., Assign Case workflows).
>    3.2 Wiki page attribute references for metadata and configuration.
> 4. Users can access and track implementation progress through integrated JIRA ticket references (51 tickets ranging from EISDEVTS-22866 to EISDEVTS-83953).
> 5. System supports cross-functional visibility by consolidating 23 incoming reference topics into a single navigation index.
> 6. Users can monitor and audit activity across claim and payment lifecycles through the BAM framework, ensuring alignment between documentation, development, and operational execution.

---
## Initiative: Claim Workflow

### Epic: Define Claim Workflows

#### Feature: Contestability workflow
- **Role**: Claims Adjuster
- **Action**: process claims through automated adjudication and payment workflows while managing exceptions that require manual intervention
- **Value**: claims are efficiently processed with automated closure and payment generation, while ensuring proper oversight and resolution of exceptions that cannot be handled automatically

**Description:**

> **As a** Claims Adjuster,
> **I want to** process claims through automated adjudication and payment workflows while managing exceptions that require manual intervention,
> **so that** claims are efficiently processed with automated closure and payment generation, while ensuring proper oversight and resolution of exceptions that cannot be handled automatically.


**Key Capabilities:**

> 1. System performs automated adjudication on eligible claims to determine payment decisions without manual intervention.
> 2. Upon successful automated adjudication, system automatically generates payments and schedules them for processing.
> 3. System automatically closes claims when all adjudication and payment generation steps complete successfully.
> 4. System monitors automated processes and generates exception tasks when automation fails or requires human review:
>    4.1 When automated claim closure fails, system creates manual review task requiring user to investigate and manually complete closure.
>    4.2 When automated payment generation encounters errors, system creates manual review task requiring user to review case and manually create or correct payment.
>    4.3 When payment scheduling process fails to execute properly, system creates manual review task requiring user to manually schedule payment.
>    4.4 When payments fail during processing, system creates manual review task requiring user to investigate failure reason and take corrective action.
>    4.5 When payments are canceled in the system, system creates manual review task requiring user to review cancellation and determine next steps.
>    4.6 When underpayments require authorization, system creates approval task requiring user to review and approve or reject the underpayment.
>    4.7 When underpayment records are canceled, system creates manual review task requiring user to review cancellation and take appropriate action.
>    4.8 When claims require policy data updates or verification, system creates policy refresh review task requiring user to refresh policy information.
>    4.9 When payee account balance discrepancies are detected, system creates manual review task requiring user to verify and resolve balance issues.
>    4.10 When payment schedules require validation, system creates manual review task requiring user to review and correct schedule as needed.
> 5. User reviews exception tasks from their work queue, investigates root causes, and takes corrective actions to resolve exceptions.
> 6. User completes manual intervention steps to allow interrupted payment processes to continue or complete.
> 7. System maintains audit trail of all automated decisions, exception generation, and manual resolution actions.

---

### Epic: Manual Task Definition

#### Feature: Manual Task Definition
- **Role**: Claims Administrator
- **Action**: define and create CAP Absence Task types (CAP Event Task and Follow Up Task) with configurable date/time parameters, queue assignments, and priority settings
- **Value**: event cases and follow-up activities are systematically tracked, assigned to appropriate queues, and completed within defined timeframes

**Description:**

> **As a** Claims Administrator,
> **I want to** define and create CAP Absence Task types (CAP Event Task and Follow Up Task) with configurable date/time parameters, queue assignments, and priority settings,
> **so that** event cases and follow-up activities are systematically tracked, assigned to appropriate queues, and completed within defined timeframes.


**Key Capabilities:**

> 1. Administrator defines task definition templates for two primary CAP Absence Task types using REST Update task definition API:
>    1.1 CAP Event Task (definitionId: CAP-002.CapEventTask) for reviewing new event cases associated with CapLoss entities.
>    1.2 Follow Up Task (definitionId: CAP-007.FollowUpTask) for managing follow-up activities associated with CapEventCase entities.
> 2. Administrator configures core task definition attributes including:
>    2.1 Definition name, entity type, and description.
>    2.2 Effective date (date-only format) when the definition becomes active.
>    2.3 Optional expiration date to control definition lifecycle.
>    2.4 Preferred queue assignment (default: claim_management queue).
>    2.5 Default priority level (read-only: priority 2 for CAP Event Task, priority 3 for Follow Up Task).
>    2.6 Extension parameters with types defined in OpenL.
> 3. Administrator or user creates individual task instances from defined templates using REST Create task API with date/time parameters:
>    3.1 Select date type options (PERIOD, DATE, or DEFAULT) for both warning and due date calculations.
>    3.2 For CAP Event Task: configure warningDateTime as P2D period and dueDateTime as P3D period.
>    3.3 For Follow Up Task: configure optional user-selected warningDateTime and required user-selected dueDateTime.
> 4. System automatically assigns created tasks to the configured preferred queue (claim_management) for claims staff to process.
> 5. When expiration date is not specified in task definition:
>    5.1 Task definition remains active indefinitely without lifecycle constraints.
> 6. System applies read-only default priority values that cannot be overridden during task creation to maintain consistent prioritization rules.

---

### Epic: Queue Configuration

#### Feature: Queue Configuration
- **Role**: System Administrator
- **Action**: configure multiple specialized queues with role-based access and control privileges to organize and route work items across different functional areas (Appeal, Claim Data Maintenance, Claim Management, Medical Review, SIU, Supervisor, Vocational, and Claim Reinsurance)
- **Value**: work items are systematically routed to appropriate team members, access is controlled based on user roles and responsibilities, and operational efficiency is maintained through structured task assignment and completion workflows

**Description:**

> **As a** System Administrator,
> **I want to** configure multiple specialized queues with role-based access and control privileges to organize and route work items across different functional areas (Appeal, Claim Data Maintenance, Claim Management, Medical Review, SIU, Supervisor, Vocational, and Claim Reinsurance),
> **so that** work items are systematically routed to appropriate team members, access is controlled based on user roles and responsibilities, and operational efficiency is maintained through structured task assignment and completion workflows.


**Key Capabilities:**

> 1. System administrator configures multiple specialized queues for different functional areas including Appeal Queue, Claim Data Maintenance Queue, Claim Management Queue, Medical Review Queue, SIU Queue, Supervisor Queue, Vocational Queue, and Claim Reinsurance Queue.
> 2. Administrator defines access privileges for each queue to control which users can view work items in specific queues.
>    2.1 For Claim Management Queue, 'Access Claim Management Queue' privilege is assigned to users who need to view claim management tasks.
>    2.2 For queues requiring open access (e.g., Claim Reinsurance Queue), no access privilege is required, allowing all users to view work items.
>    2.3 For queues with restricted access, users without appropriate privileges cannot view the queue or its contents.
> 3. Administrator configures control privileges to govern which users can perform task operations (assign, update, complete) on work items.
>    3.1 For Claim Management Queue, 'Control Claim Management Queue' privilege enables users to assign tasks to team members, update task information or status, and complete tasks to remove them from the active queue.
>    3.2 For queues with open control (e.g., Claim Reinsurance Queue), no control privilege is required, allowing all users to perform all task operations.
>    3.3 Users with access privilege but without control privilege can view queue work items but cannot perform any task operations.
> 4. System routes and organizes work items into appropriate queues based on functional purpose: appeals, data maintenance, general claim management, medical reviews, special investigations, supervisor oversight, vocational rehabilitation, and reinsurance processing.
> 5. Authorized users access their assigned queues, view work items organized within those queues, and perform permitted operations based on their privilege levels to process work items through completion.

---
## Initiative: Notes

### Epic: Note Definition

#### Feature: Note Definition
- **Role**: System Administrator
- **Action**: define and configure note templates, categories, and metadata structures for standardized documentation across claims, policies, and customer interactions
- **Value**: users can capture consistent, structured information that supports compliance, audit trails, and efficient case management

**Description:**

> **As a** System Administrator,
> **I want to** define and configure note templates, categories, and metadata structures for standardized documentation across claims, policies, and customer interactions,
> **so that** users can capture consistent, structured information that supports compliance, audit trails, and efficient case management.


**Key Capabilities:**

> 1. Administrator accesses the Note Definition configuration interface within system administration settings.
> 2. Administrator creates new note definition templates specifying:
>    2.1 Note category and subcategory for organizational classification
>    2.2 Required and optional metadata fields
>    2.3 Text format requirements and character limits
>    2.4 Visibility and access controls by role
>    2.5 Applicable business contexts (claims, policies, customer service, etc.)
> 3. Administrator configures note definition properties including:
>    3.1 Mandatory field indicators
>    3.2 Default values and dropdown selections
>    3.3 Validation rules for data entry
>    3.4 System-generated timestamp and user attribution settings
> 4. Administrator associates note definitions with specific workflows or business events for automatic prompting.
> 5. Administrator establishes note definition versioning and effective dating to support compliance and audit requirements.
> 6. Administrator saves and activates note definitions making them available to appropriate user roles.
> 7. System validates configuration completeness and applies note definitions across designated functional areas.

---
## Initiative: Document Management

### Epic: Inbound Document Management

#### Feature: Inbound Document Management
- **Role**: Document Administrator
- **Action**: generate, review, approve, and deliver business documents through on-demand and approval-based workflows with automated prefilling, validation, and multi-channel delivery
- **Value**: documents are accurate, compliant, properly reviewed, and delivered efficiently through the appropriate channels while maintaining audit trails and task management

**Description:**

> **As a** Document Administrator,
> **I want to** generate, review, approve, and deliver business documents through on-demand and approval-based workflows with automated prefilling, validation, and multi-channel delivery,
> **so that** documents are accurate, compliant, properly reviewed, and delivered efficiently through the appropriate channels while maintaining audit trails and task management.


**Key Capabilities:**

> 1. User initiates document generation through either on-demand workflow or system-triggered approval workflow based on document type and business rules.
> 2. **On-Demand Generation Workflow:**
>   2.1 User selects appropriate document template from available options.
>   2.2 System verifies all preconditions and prerequisites are met before allowing generation to proceed.
>     2.2.1 If preconditions are not fulfilled, system prevents generation and notifies user without proceeding further.
>   2.3 System automatically prefills available data fields from associated business entities.
>   2.4 System determines if manual editing is required based on template configuration.
>     2.4.1 If editing is needed, user configures document details including payee selection, entity selection, delivery method, structured information options, and free text updates.
>     2.4.2 If no editing is needed, system skips configuration and proceeds directly to preview.
>   2.5 System displays document preview for user review.
>     2.5.1 If user identifies needed changes, system returns to configuration step for editing.
>     2.5.2 If preview is satisfactory, user proceeds to generation.
>   2.6 User initiates final document generation.
>   2.7 System validates document content and verifies all mandatory fields are completed.
>     2.7.1 If mandatory fields are incomplete, system returns to configuration for completion.
>   2.8 System prompts user for final approval and confirmation.
>     2.8.1 If user cancels generation, system terminates process and sends cancellation notification via e-mail.
>   2.9 Upon confirmation, system generates final document and associates it with relevant business entity.
>   2.10 System uploads document to electronic folder (eFolder) for permanent storage.
>   2.11 System determines if follow-up task is needed for document preview.
>     2.11.1 If task is required, system generates and assigns task marking it as Task Generated.
>   2.12 System checks selected delivery method.
>     2.12.1 If delivery method is e-mail, system sends document via e-mail, notifies user about successful delivery, and confirms e-mail sent.
>     2.12.2 If delivery method is not e-mail, system completes process after eFolder upload.
> 3. **Approval-Based Generation Workflow:**
>   3.1 System trigger initiates automated document creation process.
>   3.2 System generates initial draft document with prefilled data.
>   3.3 System uploads draft document to eFolder.
>   3.4 System determines if approval is required based on document configuration.
>     3.4.1 If approval is not required, system skips approval workflow and proceeds directly to final document generation.
>   3.5 If approval is required, system generates approval task and assigns to designated approver.
>   3.6 Approver accesses task and previews document content.
>   3.7 Approver evaluates document and makes approval decision.
>     3.7.1 If document is not approved, system terminates process immediately without generating final document.
>   3.8 Upon approval, system generates final approved document.
>   3.9 System uploads final document to eFolder.
>   3.10 System checks delivery method configuration.
>     3.10.1 If delivery method is e-mail, system sends document via e-mail and notifies user about successful delivery.
>     3.10.2 If delivery method is not e-mail, system proceeds to completion.
>   3.11 System marks process as Document Generated.
>   3.12 System optionally generates review task if additional review is configured.
> 4. System maintains complete audit trail of all document generation activities, approvals, deliveries, and associated tasks throughout both workflows.

---

### Epic: Outbound Document Management

#### Feature: Outbound Document Management
- **Role**: Claims Adjuster
- **Action**: generate, review, approve, and deliver outbound documents through an automated workflow with conditional approval and multi-channel delivery
- **Value**: documents are accurate, compliant, properly approved, and efficiently delivered to recipients through the appropriate channel

**Description:**

> **As a** Claims Adjuster,
> **I want to** generate, review, approve, and deliver outbound documents through an automated workflow with conditional approval and multi-channel delivery,
> **so that** documents are accurate, compliant, properly approved, and efficiently delivered to recipients through the appropriate channel.


**Key Capabilities:**

> 1. System initiates document generation based on a triggering event (e.g., claim status change, milestone completion, user action).
> 2. System generates the document based on predefined templates and case-specific data and uploads it to the electronic folder (eFolder) for storage and audit purposes.
> 3. System evaluates business rules to determine if approval is required for the document type.
>    3.1 If approval is required, system creates an approval task and assigns it to the appropriate user or role.
>    3.2 If approval is not required, system proceeds directly to document preview.
> 4. User reviews the document via preview functionality to assess content, accuracy, and completeness.
> 5. User makes an approval decision on the document.
>    5.1 If document is approved, system evaluates the configured delivery method.
>    5.2 If document is not approved, system generates a review task for document revision, triggers document regeneration with required changes, uploads the revised document to eFolder, and returns to the approval workflow (creating an iterative revision cycle until approval is achieved).
> 6. System determines delivery method based on configuration and recipient preferences.
>    6.1 If delivery method is email, system sends the document to designated recipient(s) and notifies the user with delivery confirmation.
>    6.2 If delivery method is not email (e.g., print, portal, manual distribution), system completes the process without automated delivery or notification.
> 7. Process completes with the finalized, approved document stored in eFolder and delivered (if applicable).

---

### Epic: eFolder

#### Feature: Configure eFolder Structure
- **Role**: System Administrator
- **Action**: configure and customize the eFolder structure to define how documents are organized, categorized, and stored within the document management system
- **Value**: documents are systematically organized according to business requirements, enabling efficient retrieval, compliance with retention policies, and consistent document handling across the organization

**Description:**

> **As a** System Administrator,
> **I want to** configure and customize the eFolder structure to define how documents are organized, categorized, and stored within the document management system,
> **so that** documents are systematically organized according to business requirements, enabling efficient retrieval, compliance with retention policies, and consistent document handling across the organization.


**Key Capabilities:**

> 1. Administrator accesses the eFolder configuration module within the Document Management system.
> 2. Administrator defines the hierarchical folder structure, including parent folders, subfolders, and naming conventions aligned with business taxonomy.
> 3. Administrator assigns document categories and types to specific folders to control what content can be stored in each location.
> 4. Administrator configures folder-level security and access permissions based on user roles and business rules.
> 5. Administrator establishes metadata requirements and indexing rules for documents within each folder to enable search and retrieval.
> 6. Administrator defines retention policies and lifecycle rules at the folder level to automate document archival and disposal.
> 7. Administrator validates the eFolder configuration by testing document upload, categorization, and access scenarios.
> 8. Administrator publishes the eFolder structure to make it available across the system for end users and automated processes.
> 9. Administrator monitors eFolder usage and adjusts the structure as business needs evolve.

---
## Initiative: Administration

### Epic: User Management

#### Feature: User roles and Privileges
- **Role**: System Administrator
- **Action**: define and manage a hierarchical role-based access control (RBAC) system where actors are assigned specific roles with inherited privileges
- **Value**: claim operations are executed with appropriate authority levels, operational efficiency is maintained through role reusability, and security is enforced through structured privilege inheritance

**Description:**

> **As a** System Administrator,
> **I want to** define and manage a hierarchical role-based access control (RBAC) system where actors are assigned specific roles with inherited privileges,
> **so that** claim operations are executed with appropriate authority levels, operational efficiency is maintained through role reusability, and security is enforced through structured privilege inheritance.


**Key Capabilities:**

> 1. System supports hierarchical role-based access control (RBAC) model where actors (persons, groups, or systems) are assigned specific roles that determine their privileges within the claim processing system.
> 2. Role hierarchy operates on an inheritance model with three ascending privilege levels:
>    2.1 **Customer Service Representative (Level 1)** - Base level role providing privileges for initiating and updating losses, managing claim parties, policy writing, recording loss information, and handling customer inquiries and complaints.
>    2.2 **Claim Adjuster (Level 2)** - Inherits all CSR privileges and adds investigative capabilities including loss adjudication, settlement processing, claim queue management, inspecting losses, interviewing parties, reviewing reports, and assessing property damage.
>    2.3 **Claim Supervisor (Level 3)** - Inherits all Claim Adjuster privileges and adds supervisory authorities including loss closure, settlement approval, payment issuance, recovery management, overpayment handling, and access to specialized queues (Appeal, Medical Review, SIU, Supervisor, Vocational).
> 3. System enforces strict privilege inheritance where higher-level roles automatically inherit all privileges of lower-level roles without ability to bypass the hierarchy.
> 4. System provides specialized functional roles for specific operational domains:
>    4.1 **CAP Financial Integration** role grants privileges for managing payments, balances, recovery operations, underpayment handling, and payment schedule management within the CAP sub-system.
>    4.2 **System User** role (automated role) contains all CAP sub-system privileges necessary for controlling and orchestrating automated workflows without human intervention.
> 5. System supports dynamic role assignment, allowing the same actor to assume different roles depending on operational situation and business needs.
> 6. Role definitions are created once and reused across multiple areas to minimize duplication and maintain consistency.
> 7. When automated system processes need to execute claim operations, the System User role is invoked to drive processes programmatically.
> 8. When an actor needs to perform functions across multiple responsibility areas, role assignment flexibility allows operational adaptation without creating new role definitions.
> 9. Access to specialized processing queues (Appeal, Medical Review, SIU, Supervisor, Vocational) is restricted to Claim Supervisor role or higher privilege levels.

---

#### Feature: Configure Authority levels
- **Role**: System Administrator
- **Action**: configure authority level limits that define approval thresholds for claim payment schedules based on payment amount and subtype
- **Value**: the system can automatically approve payments within authorized limits and route exceptions for manual review, ensuring compliance with organizational approval policies

**Description:**

> **As a** System Administrator,
> **I want to** configure authority level limits that define approval thresholds for claim payment schedules based on payment amount and subtype,
> **so that** the system can automatically approve payments within authorized limits and route exceptions for manual review, ensuring compliance with organizational approval policies.


**Key Capabilities:**

> 1. Administrator configures authority level limits by defining maximum approval amounts for each combination of authority level (0-5) and payment subtype.
> 2. For each authority level, administrator specifies approval thresholds for applicable payment subtypes including Life, Disability, Expense, Underpayment, Ex Gratia, Overpayment Waive, Dental, Pet, and Dental/Pet-Underpayment.
> 3. Administrator can set specific dollar limits (e.g., $10,000, $50,000) or unlimited approval authority for given authority level and subtype combinations.
> 4. When a claim payment is submitted for approval, the system automatically evaluates the payment against the submitting approver's authority level configuration.
>    4.1 System retrieves the Max Amount configuration for the approver's authority level and the payment's subtype.
>    4.2 System compares the payment amount against the configured Max Amount threshold.
> 5. If configuration exists for the authority level and subtype combination AND the payment amount is within or equal to the Max Amount, system sets approval status to 'Approved' and payment proceeds without manual intervention.
> 6. System routes payment for manual review when approval threshold validation fails.
>    6.1 If no Max Amount configuration exists for the authority level and subtype combination, system sets approval status to 'Review' and requires manual review by appropriate authority.
>    6.2 If payment amount exceeds the configured Max Amount, system sets approval status to 'Review' and requires manual review by higher authority level or designated reviewer.
> 7. Configuration supports special rules including zero-dollar limits to block specific payment types and unlimited authority for senior approval levels across all subtypes.

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