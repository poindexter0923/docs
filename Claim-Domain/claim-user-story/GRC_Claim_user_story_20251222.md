---
title: "GRC Wiki Structure with User Story 20251222"
date: 2025-12-22
---


## Initiative: Foundation & Policy Integration

### Epic: Common Claim Processing Framework & Integrations

#### Feature: As a Claims Adjuster, I want to retrieve and display Premium Paid to Date from the Billing system, so that I can verify policy payment status before processing claim payments
- **Role**: Claim Adjuster
- **Action**: retrieve and validate Premium Paid to Date from the Billing system against the Date of Loss to determine claim payment eligibility
- **Value**: I can verify the policy is in good standing with current premium payments before authorizing claim benefits, preventing inappropriate payments on delinquent policies

**Description:**

> As a **Claim Adjuster**,
> I want to **retrieve and validate Premium Paid to Date from the Billing system against the Date of Loss to determine claim payment eligibility**,
> So that **I can verify the policy is in good standing with current premium payments before authorizing claim benefits, preventing inappropriate payments on delinquent policies**


**Key Capabilities:**

> 1. Upon claim creation, system automatically requests Premium Paid to Date from Billing system using member record identifier
> 2. System receives and displays premium payment status in claim workspace for adjuster review
> 3. System evaluates Premium Paid to Date against Date of Loss to determine payment eligibility
>     3.1 If premiums are current through date of loss, system allows normal claim processing
>     3.2 If premiums are insufficient, system displays warning indicator signaling payment ineligibility
> 4. Adjuster reviews payment status and warning indicators to determine appropriate claim handling actions
> 5. System maintains premium payment status throughout claim lifecycle for audit and compliance purposes


**Acceptance Criteria:**

> 1. **Given** a new claim is created, **When** the system initiates, **Then** Premium Paid to Date is automatically retrieved from Billing system using member record information
> 2. **Given** Billing system returns premium data, **When** data is received, **Then** Premium Paid to Date is displayed in claim workspace for adjuster access
> 3. **Given** Premium Paid to Date is before Date of Loss, **When** system evaluates eligibility, **Then** warning indicator is displayed and claim is flagged as ineligible for payment
> 4. **Given** Premium Paid to Date meets or exceeds Date of Loss, **When** adjuster reviews status, **Then** system permits normal claim adjudication without payment restrictions
> 5. **Given** premium data is unavailable, **When** retrieval fails, **Then** system prevents claim processing until payment status is confirmed


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=716870179"
> ]

---

#### Feature: As a Claims Adjuster, I want to manage Premium Waiver approval periods with automatic validation of dates and state transitions, so that waiver premium data is accurately sent to Billing for premium adjustments
- **Role**: Claim Adjuster
- **Action**: manage Premium Waiver approval periods with automatic validation and billing transmission
- **Value**: premium waiver benefits are accurately tracked and premium adjustments are timely communicated to Billing for policyholder relief during disability periods

**Description:**

> As a **Claim Adjuster**,
> I want to **manage Premium Waiver approval periods with automatic validation and billing transmission**,
> So that **premium waiver benefits are accurately tracked and premium adjustments are timely communicated to Billing for policyholder relief during disability periods**.


**Key Capabilities:**

> 1. Upon claim creation for policies with Premium Waiver coverage, system calculates elimination period and benefit period boundaries based on date of loss and policy terms
> 2. User is able to approve waiver periods by providing start and end dates with mandatory status transition to 'Approved'
>     2.1 System validates period against elimination/benefit period boundaries, prevents overlapping periods, and ensures consecutive period sequencing
>     2.2 Upon successful approval, system transmits waiver effective date to Billing and locks start date from further modification
> 3. User is able to complete approved waiver periods by updating end dates and transitioning status to 'Completed'
>     3.1 System transmits waiver expiration date to Billing and locks all period data from modification
> 4. System enforces state-based workflow preventing simultaneous multiple approved periods and requiring completion before subsequent approvals


**Acceptance Criteria:**

> 1. **Given** claim is created with Premium Waiver coverage, **When** date of loss and policy terms are available, **Then** system calculates and displays elimination period and benefit period boundaries
> 2. **Given** user approves waiver period with valid dates, **When** approval is submitted within benefit period and after appropriate elimination threshold, **Then** system saves approval, transmits effective date to Billing, and prevents start date editing
> 3. **Given** approved period exists, **When** user attempts to approve another period without completing the first, **Then** system prevents approval and prompts for completion
> 4. **Given** user completes approved period, **When** completion is submitted with valid end date within benefit period, **Then** system transmits expiration date to Billing and locks all period data
> 5. **Given** validation rules are violated, **When** user submits approval or completion, **Then** system prevents submission and displays business rule violation reason
> 6. **Given** multiple completed periods exist, **When** user creates new approval, **Then** system enforces start date occurs after latest completed period end date


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=681711540"
> ]

---

#### Feature: As a System Administrator, I want to configure accumulator settings for different coverage types (TL, CI, HI, Accident, Premium Waiver), so that the system accurately tracks paid amounts and remaining benefits according to policy terms
- **Role**: Claim Manager
- **Action**: configure accumulator settings across coverage types to automate benefit tracking and calculation
- **Value**: the system accurately monitors paid amounts and remaining entitlements throughout the policy lifecycle, ensuring compliance with policy terms

**Description:**

> As a **Claim Manager**,
> I want to **configure accumulator settings across coverage types to automate benefit tracking and calculation**,
> So that **the system accurately monitors paid amounts and remaining entitlements throughout the policy lifecycle, ensuring compliance with policy terms**.


**Key Capabilities:**

> 1. User is able to establish accumulator definitions aligned to policy term coverage types and benefit structures
> 2. System automatically captures payment events and updates accumulator balances in real-time
> 3. System calculates remaining benefits by applying policy term limits against accumulated paid amounts
> 4. Upon threshold breach, system triggers notifications and enforces benefit exhaustion rules
> 5. User is able to configure accumulator reset rules based on policy anniversary or calendar periods
> 6. System maintains audit trail of all accumulator adjustments and recalculations


**Acceptance Criteria:**

> 1. **Given** valid coverage types are defined, **When** accumulator configuration is applied, **Then** system tracks payments and calculates remaining benefits per policy terms
> 2. **Given** payment is processed, **When** accumulator threshold is reached, **Then** system prevents overpayment and alerts stakeholders
> 3. **Given** policy period resets, **When** anniversary date occurs, **Then** system reinitializes accumulators according to configuration rules
> 4. **Given** incomplete policy term data, **When** configuration is attempted, **Then** system prevents activation until prerequisites are satisfied
> 5. **Given** multiple coverage types exist, **When** payment applies, **Then** system allocates amounts to correct accumulators automatically


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=618282181"
> ]

---

#### Feature: As a Claims Adjuster, I want to validate claim eligibility based on member effectiveness and eligibility waiting periods, so that only eligible claims are processed for payment
- **Role**: Claim Adjuster
- **Action**: validate claim eligibility based on member effectiveness and eligibility waiting periods
- **Value**: only eligible claims are processed for payment, reducing improper payments and ensuring policy compliance

**Description:**

> As a **Claim Adjuster**,
> I want to **validate claim eligibility based on member effectiveness and eligibility waiting periods**,
> So that **only eligible claims are processed for payment, reducing improper payments and ensuring policy compliance**.


**Key Capabilities:**

> 1. System retrieves member policy information and coverage effective dates upon claim submission
> 2. System validates member status is active at the time of loss or service date
> 3. System evaluates eligibility waiting periods against claim service date and policy inception
> 4. System identifies coverage restrictions or exclusions applicable to the claim
>     4.1 When waiting period has not elapsed, system flags claim for denial
>     4.2 When member is inactive, system prevents claim progression
> 5. System applies eligibility determination results to adjudication workflow
> 6. User is able to review eligibility validation outcomes and override with documented justification when authorized


**Acceptance Criteria:**

> 1. **Given** a claim is submitted, **When** member policy is inactive on service date, **Then** system denies the claim for ineligibility
> 2. **Given** a policy has eligibility waiting periods, **When** claim service date falls within waiting period, **Then** system flags claim as ineligible and prevents payment
> 3. **Given** member is active and waiting periods satisfied, **When** eligibility validation runs, **Then** system approves claim for further adjudication
> 4. **Given** eligibility rules cannot be determined, **When** system encounters incomplete policy data, **Then** claim is suspended for manual review
> 5. **Given** adjuster has override authority, **When** business justification is documented, **Then** system allows eligibility override and logs the action
> 6. **Given** eligibility validation completes, **When** results are stored, **Then** system maintains audit trail of validation criteria and decisions


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=613797286"
> ]

---

#### Feature: As a Claims Adjuster, I want to verify that the claim subject is an insured party on the policy, so that claims are only created against valid policy insureds
- **Role**: Claim Adjuster
- **Action**: verify that the claim subject is an insured party on the associated policy before processing the claim
- **Value**: claims are only created and processed against valid policy insureds, preventing fraudulent or erroneous claim submissions and ensuring regulatory compliance

**Description:**

> As a **Claim Adjuster**,
> I want to **verify that the claim subject is an insured party on the associated policy before processing the claim**,
> So that **claims are only created and processed against valid policy insureds, preventing fraudulent or erroneous claim submissions and ensuring regulatory compliance**.


**Key Capabilities:**

> 1. User initiates claim subject verification against the referenced policy
> 2. System retrieves policy details and validates active coverage status
> 3. System cross-references claim subject identity with policy insured parties list
> 4. Upon successful match, system confirms insured party eligibility and enables claim processing
>     4.1 If no match found, system flags claim as invalid and prevents further processing
> 5. System documents verification outcome in claim record for audit trail
> 6. User is able to review verification results and proceed with adjudication or escalate discrepancies


**Acceptance Criteria:**

> 1. **Given** a claim is submitted, **When** the claim subject verification is initiated, **Then** the system retrieves the associated policy and validates its active status
> 2. **Given** policy data is available, **When** the system compares claim subject identity, **Then** insured party match is confirmed or rejection is triggered
> 3. **Given** claim subject is not found on policy, **When** verification fails, **Then** system prevents claim creation and provides business reasoning
> 4. **Given** claim subject is validated, **When** verification succeeds, **Then** claim processing workflow continues without interruption
> 5. **Given** verification is complete, **When** audit is requested, **Then** system provides complete verification history and timestamps


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=613797286"
> ]

---

#### Feature: As a Claims Adjuster, I want to search and retrieve applicable policy versions based on Date of Loss, so that claims are adjudicated against the correct policy terms
- **Role**: Claim Adjuster
- **Action**: search and retrieve the applicable policy version based on Date of Loss and adjudicate coverages accordingly
- **Value**: claims are processed against accurate policy terms, ensuring correct coverage determination and compliance with contractual obligations

**Description:**

> As a **Claim Adjuster**,
> I want to **search and retrieve the applicable policy version based on Date of Loss and adjudicate coverages accordingly**,
> So that **claims are processed against accurate policy terms, ensuring correct coverage determination and compliance with contractual obligations**


**Key Capabilities:**

> 1. System retrieves policy image for all active policies based on Event Date, excluding archived versions
> 2. System locates the applicable policy version corresponding to the Date of Loss
>     2.1 Upon product type is CapAbsence, system applies specific version location rules
>     2.2 Upon product type is CapNonAbsence, system follows alternate version location logic
> 3. System adjudicates or re-adjudicates coverages and benefits based on loss details and relationship to insured
> 4. System determines relationship context (Covered Person vs Member Person) to apply appropriate adjudication rules
> 5. System executes auto-adjudication workflow to finalize coverage decisions


**Acceptance Criteria:**

> 1. **Given** a claim with Date of Loss, **When** policy retrieval is initiated, **Then** system returns only active policy versions matching Event Date
> 2. **Given** multiple policy versions exist, **When** locating applicable version, **Then** system identifies the version effective on Date of Loss
> 3. **Given** product type is CapAbsence or CapNonAbsence, **When** version location occurs, **Then** system applies product-specific rules
> 4. **Given** applicable policy version is identified, **When** adjudication executes, **Then** coverages are determined based on loss details and insured relationship
> 5. **Given** relationship type differs (Covered Person vs Member), **When** adjudication runs, **Then** system applies corresponding relationship rules
> 6. **Given** archived policy versions exist, **When** retrieval occurs, **Then** system excludes archived versions from results


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=741921991"
> ]

---

#### Feature: As a System Administrator, I want to configure OpenL business rules for claim and case auto-assignment, so that claims are routed to appropriate queues and users based on claim type and authority levels
- **Role**: Claim Manager
- **Action**: configure business rules for automated claim and case routing
- **Value**: claims are intelligently distributed to qualified users and queues based on claim characteristics and user competencies

**Description:**

> As a Claim Manager,
> I want to configure business rules for automated claim and case routing,
> So that claims are intelligently distributed to qualified users and queues based on claim characteristics and user competencies


**Key Capabilities:**

> 1. System administrator configures routing rules based on claim type categories (Disability, Life, Health)
> 2. Upon claim or case creation, system evaluates business rules to determine target assignment queue
> 3. System matches available users against authority criteria (type, subtype, level) and skill parameters (type, value, level)
> 4. When matching user is identified, system assigns claim to individual user; otherwise claim remains in management queue
> 5. Assignment logic operates independently of organizational roles, focusing on competency matching
> 6. Configuration supports client-specific business requirements and can be updated as organization evolves


**Acceptance Criteria:**

> 1. **Given** routing rules are configured for claim type, **When** new claim is created, **Then** system assigns to appropriate management queue automatically
> 2. **Given** user authority and skill profiles exist, **When** system evaluates assignment rules, **Then** claim routes to user matching all configured criteria
> 3. **Given** no users match rule criteria, **When** assignment is attempted, **Then** claim remains in queue without individual assignment
> 4. **Given** multiple claim types configured, **When** different claim types are submitted, **Then** each routes according to its specific rule parameters
> 5. **Given** configuration changes are saved, **When** subsequent claims are processed, **Then** new rules take effect immediately
> 6. **Given** assignment is complete, **When** administrator reviews routing, **Then** system provides audit trail of rule-based assignment decisions


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=734439997"
> ]

---

#### Feature: As a System Administrator, I want to configure FICA tax rates and thresholds by year, so that claim payments are calculated with accurate federal tax withholdings
- **Role**: Claim Adjuster
- **Action**: configure annual FICA tax rates and thresholds
- **Value**: claim payments apply accurate federal payroll tax withholdings aligned with IRS regulations

**Description:**

> As a **Claim Adjuster**,
> I want to **configure annual FICA tax rates and thresholds**,
> So that **claim payments apply accurate federal payroll tax withholdings aligned with IRS regulations**


**Key Capabilities:**

> 1. Configure Social Security tax parameters with 6.2% base rate and annual wage thresholds by calendar year
> 2. Configure Medicare tax parameters with 1.45% base rate and $200,000 threshold for additional 0.9% surtax
> 3. System calculates cumulative calendar year earnings and applies threshold limits to determine tax withholding eligibility
> 4. Upon exceeding Social Security threshold, system stops withholding for remainder of calendar year
>     4.1 Upon exceeding Medicare threshold, system applies combined 2.35% rate
> 5. Manage religious exemption status when IRS Form 4029 documentation is provided
> 6. System maintains historical tax configuration data for audit and retroactive adjustments


**Acceptance Criteria:**

> 1. **Given** new calendar year threshold is configured, **When** payment processing occurs, **Then** system applies updated threshold to earnings calculations
> 2. **Given** cumulative earnings exceed Social Security threshold, **When** subsequent payment is processed, **Then** system withholds no Social Security tax
> 3. **Given** cumulative earnings exceed Medicare threshold, **When** subsequent payment is processed, **Then** system applies 2.35% combined Medicare tax rate
> 4. **Given** religious exemption is documented, **When** payment is processed, **Then** system withholds no FICA taxes
> 5. **Given** invalid or incomplete threshold configuration, **When** payment processing is initiated, **Then** system prevents calculation until valid data is provided
> 6. **Given** mid-year threshold correction, **When** retroactive adjustment is required, **Then** system recalculates affected payments using historical configuration


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=693049539"
> ]

---

#### Feature: As a System Administrator, I want to configure state income tax rates and brackets by state and filing status, so that claim payments are calculated with accurate state tax withholdings
- **Role**: Claim Adjuster
- **Action**: configure and maintain state income tax rates, brackets, and filing requirements by jurisdiction to enable accurate tax withholding calculations on claim payments
- **Value**: claim payments comply with state tax regulations, reducing financial penalties and ensuring correct withholding amounts for multiple tax scenarios

**Description:**

> As a **Claim Adjuster**,
> I want to **configure and maintain state income tax rates, brackets, and filing requirements by jurisdiction to enable accurate tax withholding calculations on claim payments**,
> So that **claim payments comply with state tax regulations, reducing financial penalties and ensuring correct withholding amounts for multiple tax scenarios**


**Key Capabilities:**

> 1. System administrator configures state tax parameters including tax approach type (no tax, flat rate, progressive brackets)
> 2. Administrator defines rate tables by state and filing status with income thresholds for progressive jurisdictions
>     2.1 Upon flat-rate state selection, single percentage rate is applied
>     2.2 Upon progressive state selection, multiple bracket thresholds and rates are configured
> 3. System supports special tax rules for limited-scope states targeting specific income types
> 4. Administrator establishes filing deadlines with state-specific and disaster-related extension capabilities
> 5. Configuration enables multi-state tax calculation when claimant has cross-jurisdiction income sources
> 6. System validates configuration completeness before activation for payment processing


**Acceptance Criteria:**

> 1. **Given** administrator selects a state, **When** configuring tax approach, **Then** system applies appropriate calculation method (no-tax, flat-rate, or progressive brackets)
> 2. **Given** progressive tax state is configured, **When** multiple brackets are defined, **Then** system validates thresholds are sequential and rates correspond to filing status
> 3. **Given** flat-rate state is configured, **When** single rate is entered, **Then** system applies uniform percentage to all taxable income
> 4. **Given** claimant has multi-state income, **When** payment is processed, **Then** system calculates separate tax obligations per applicable jurisdiction
> 5. **Given** configuration is incomplete, **When** administrator attempts activation, **Then** system prevents deployment until required parameters are populated
> 6. **Given** disaster extension applies, **When** deadline is queried, **Then** system returns extended filing date for affected jurisdictions


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=710809888"
> ]

---

#### Feature: As a System Administrator, I want to configure authority level limits for claim payment approvals, so that payment authorization is enforced based on user authority levels and claim subtypes
- **Role**: Claim Manager
- **Action**: configure and enforce payment approval authority limits based on user roles and claim payment subtypes
- **Value**: payment authorization is systematically controlled, reducing unauthorized approvals and ensuring compliance with organizational payment governance policies

**Description:**

> As a **Claim Manager**,
> I want to **configure and enforce payment approval authority limits based on user roles and claim payment subtypes**,
> So that **payment authorization is systematically controlled, reducing unauthorized approvals and ensuring compliance with organizational payment governance policies**.


**Key Capabilities:**

> 1. System administrator defines maximum payment thresholds for each authority level across claim payment subtypes (Life, Disability, Expense, Underpayment, Ex Gratia, Overpayment Waive, Dental, Pet).
> 2. Upon payment submission, system validates user's authority level against configured limits for the specific payment subtype.
> 3. When payment amount is within or equal to the configured maximum, system auto-approves the payment.
>     3.1 If no configuration exists for the authority level and subtype combination, system routes payment for manual review.
>     3.2 If payment exceeds configured limit, system escalates to higher authority for review.
> 4. System supports unlimited authority designation for senior-level users across all subtypes.
> 5. Configuration persists across related processes including underpayment approval, payment schedule activation, and overpayment waiver workflows.


**Acceptance Criteria:**

> 1. **Given** an authority level configuration exists for a payment subtype, **When** the payment amount is within the configured limit, **Then** the system auto-approves the payment without manual intervention.
> 2. **Given** no configuration exists for the user's authority level and payment subtype, **When** payment is submitted, **Then** the system routes to manual review status.
> 3. **Given** the payment amount exceeds the configured authority limit, **When** validation occurs, **Then** the system escalates to review status and notifies higher authority.
> 4. **Given** a user has unlimited authority designation, **When** any payment is submitted, **Then** the system auto-approves regardless of amount or subtype.
> 5. **Given** configuration changes are saved, **When** subsequent payments are processed, **Then** the system applies updated limits immediately.
> 6. **Given** multiple payment subtypes exist, **When** validating authority, **Then** the system applies subtype-specific limits independently.


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=656393091"
> ]

---

#### Feature: As a System Administrator, I want to configure Consumer Price Index (CPI) values by year and type, so that COLA benefit calculations for LTD claims are accurate
- **Role**: Claim Adjuster
- **Action**: configure and maintain annual CPI reference data by index type to support automated COLA benefit calculations
- **Value**: LTD claims receive accurate inflation-adjusted benefit amounts based on current economic indicators

**Description:**

> As a **Claim Adjuster**,
> I want to **configure and maintain annual CPI reference data by index type to support automated COLA benefit calculations**,
> So that **LTD claims receive accurate inflation-adjusted benefit amounts based on current economic indicators**


**Key Capabilities:**

> 1. System maintains annual CPI percentage values for two index types (CPI-U and CPI-W) sourced from government authorities
> 2. User is able to configure CPI values by calendar year and index type for future claim calculations
> 3. System applies configured CPI data to COLA benefit calculations and pre-disability earnings indexing for LTD claims
> 4. Upon encountering unconfigured years, system defaults to 0% inflation rate
>     4.1 System logs instances where default values are applied
> 5. User is able to update historical CPI values when corrections are required
> 6. System validates data completeness before applying CPI to active claims


**Acceptance Criteria:**

> 1. **Given** CPI values are configured for a specific year, **When** COLA calculation executes, **Then** system applies the correct index percentage to benefit amounts
> 2. **Given** no CPI data exists for a claim year, **When** calculation runs, **Then** system applies 0% default and flags for review
> 3. **Given** both CPI-U and CPI-W values exist, **When** user selects index type per policy terms, **Then** system uses the designated index
> 4. **Given** CPI configuration is updated, **When** recalculation is triggered, **Then** affected LTD claims reflect revised indexed amounts
> 5. **Given** incomplete CPI data, **When** user attempts activation, **Then** system prevents application until data integrity is confirmed


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=694527028"
> ]

---

#### Feature: As a System Administrator, I want to configure LTD Reduced Benefit Duration (RBD) schedules by age, so that maximum benefit periods are correctly calculated based on disability onset age
- **Role**: Claim Manager
- **Action**: configure age-based reduced benefit duration schedules
- **Value**: maximum benefit periods are accurately determined based on disability onset age to ensure compliant and consistent claim adjudication

**Description:**

> As a **Claim Manager**,
> I want to **configure age-based reduced benefit duration schedules**,
> So that **maximum benefit periods are accurately determined based on disability onset age to ensure compliant and consistent claim adjudication**


**Key Capabilities:**

> 1. Administrator establishes age-indexed benefit duration schedule with progressive reduction thresholds
> 2. System validates schedule completeness covering all age ranges from under 56 to 69 and older
> 3. Configuration defines maximum benefit months for each age milestone at disability onset
> 4. System publishes schedule for consumption by claim adjudication processes
> 5. Upon claim initiation, system automatically applies appropriate duration based on insured's disability onset age
> 6. Administrator updates schedule to reflect actuarial or regulatory changes


**Acceptance Criteria:**

> 1. **Given** a complete age-duration schedule is configured, **When** a claim is processed, **Then** the system applies the correct maximum benefit duration based on disability onset age
> 2. **Given** disability onset age is under 56, **When** benefit period is calculated, **Then** system assigns 120 months maximum duration
> 3. **Given** disability onset age is 69 or older, **When** calculation occurs, **Then** system assigns 12 months maximum
> 4. **Given** incomplete age range configuration, **When** validation executes, **Then** system prevents schedule activation
> 5. **Given** schedule update is submitted, **When** validation succeeds, **Then** system applies new rules to subsequent claims without retroactive impact


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=709433273"
> ]

---

#### Feature: As a System Administrator, I want to configure Social Security Normal Retirement Age (SSNRA) by birth year, so that LTD maximum benefit period calculations are accurate
- **Role**: Claim Adjuster
- **Action**: configure Social Security Normal Retirement Age thresholds by birth year cohorts to enable automated benefit period calculations
- **Value**: Long-Term Disability maximum benefit period determinations align with federal regulations and ensure accurate benefit duration calculations

**Description:**

> As a **Claim Adjuster**,
> I want to **configure Social Security Normal Retirement Age thresholds by birth year cohorts to enable automated benefit period calculations**,
> So that **Long-Term Disability maximum benefit period determinations align with federal regulations and ensure accurate benefit duration calculations**


**Key Capabilities:**

> 1. System maintains reference table mapping birth year ranges to corresponding retirement ages per federal schedule
> 2. Upon benefit period calculation, system retrieves applicable retirement age threshold based on claimant's birth year
> 3. When claimant birth date falls on January 1, system applies retirement age defined for previous calendar year
>     3.1 System validates birth year against configured cohorts (pre-1938 through 1960+)
>     3.2 System determines retirement age with precision to month increments
> 4. System applies retrieved retirement age to calculate maximum LTD benefit duration endpoint
> 5. Administrator is able to maintain configuration table to reflect legislative amendments to retirement age schedules


**Acceptance Criteria:**

> 1. **Given** a claimant born in 1955, **When** benefit period is calculated, **Then** system applies 66 years 2 months as retirement age threshold
> 2. **Given** a claimant born January 1, 1960, **When** system retrieves retirement age, **Then** system uses 1959 cohort rules (66 years 10 months)
> 3. **Given** birth year predates 1938, **When** calculation executes, **Then** system defaults to 65 years retirement age
> 4. **Given** configuration table is updated, **When** new claim is processed, **Then** system applies current active retirement age mapping
> 5. **Given** birth year falls in 1943-1954 range, **When** threshold is determined, **Then** system assigns 66 years without month increments


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=709433154"
> ]

---

#### Feature: As a System Administrator, I want to configure Official Disability Guidelines (ODG) by ICD code and job severity, so that auto-adjudication scenarios use accurate disability duration guidelines
- **Role**: Claim Adjuster
- **Action**: configure Official Disability Guidelines (ODG) by ICD diagnosis codes and job physical demand severity levels
- **Value**: automated claim adjudication applies evidence-based disability duration guidelines consistently across claims

**Description:**

> As a **Claim Adjuster**,
> I want to **configure Official Disability Guidelines (ODG) by ICD diagnosis codes and job physical demand severity levels**,
> So that **automated claim adjudication applies evidence-based disability duration guidelines consistently across claims**


**Key Capabilities:**

> 1. System retrieves ICD diagnosis code from submitted claim and identifies job physical demand classification
> 2. Configuration mapping associates ICD codes to disability duration recommendations across occupation categories (Sedentary, Light, Medium, Heavy, Very Heavy)
> 3. Duration values increase progressively with job physical demand severity to reflect recovery complexity
> 4. Auto-adjudication rules retrieve configured duration based on claim diagnosis and occupation class
> 5. System applies recommended duration to claim approval decision automatically
> 6. Configuration data remains updatable to reflect evolving ODG guidelines and medical evidence


**Acceptance Criteria:**

> 1. **Given** valid ICD code and occupation class exist on claim, **When** auto-adjudication executes, **Then** system retrieves corresponding ODG duration from configuration
> 2. **Given** job physical demand is Heavy, **When** same diagnosis is assessed, **Then** approved duration exceeds Medium demand duration
> 3. **Given** ICD code lacks ODG mapping, **When** auto-adjudication attempts processing, **Then** system escalates claim for manual review
> 4. **Given** configuration is updated, **When** subsequent claims reference affected ICD codes, **Then** new duration guidelines apply immediately
> 5. **Given** multiple ICD codes map to same condition, **When** any code is submitted, **Then** consistent duration recommendations are applied


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=693049544"
> ]

---

#### Feature: As a System Administrator, I want to configure disability interest rates by state, so that delayed claim payments accrue interest at the correct legal rates
- **Role**: Claim Manager
- **Action**: configure and maintain state-mandated disability interest rates and payment timelines
- **Value**: the system automatically calculates and applies legally compliant penalty interest when disability claim payments are delayed beyond regulatory deadlines

**Description:**

> As a **Claim Manager**,
> I want to **configure and maintain state-mandated disability interest rates and payment timelines**,
> So that **the system automatically calculates and applies legally compliant penalty interest when disability claim payments are delayed beyond regulatory deadlines**


**Key Capabilities:**

> 1. Configure state-specific parameters including interest rate type (fixed annual/monthly or variable formula), payment deadline thresholds, legal citations, and minimum interest thresholds
> 2. Define variable rate calculation formulas linked to external benchmarks (Federal Reserve discount rate, prime lending rates, state tax codes)
> 3. Establish payment timeline rules with standard, expedited, and extended deadlines based on jurisdiction
> 4. Configure exemption conditions for documentation extension requests, good faith delays, and partial dispute scenarios
> 5. Validate configuration completeness ensuring all active states have current rates and statutory references
> 6. Maintain historical rate changes with effective dating for accurate retroactive calculations


**Acceptance Criteria:**

> 1. **Given** state configuration parameters are defined, **When** a disability claim payment exceeds the jurisdiction's deadline, **Then** penalty interest accrues automatically at the configured rate from the late date until payment
> 2. **Given** a state uses variable rate formulas, **When** interest calculation is triggered, **Then** the system dynamically computes the rate using current benchmark values
> 3. **Given** calculated interest falls below the state's minimum threshold, **When** payment is processed, **Then** no interest penalty is assessed
> 4. **Given** valid exemption conditions exist (documentation requests, good faith), **When** applied to the claim, **Then** interest accrual is suspended or waived per state rules
> 5. **Given** partial dispute scenarios, **When** undisputed amounts are identified, **Then** interest applies only to unpaid undisputed portions
> 6. **Given** configuration changes are saved, **When** effective dates are specified, **Then** historical and future claims use applicable rate versions


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=734440664"
> ]

---

#### Feature: As a System Administrator, I want to configure automated offset rules by priority and claim type, so that claim payments are automatically offset against applicable state and federal benefits
- **Role**: Claim Manager
- **Action**: configure priority-based automated offset rules for state and federal benefits integration
- **Value**: claim payments are automatically adjusted against applicable statutory benefits, ensuring compliance and reducing manual processing

**Description:**

> As a **Claim Manager**,
> I want to **configure priority-based automated offset rules for state and federal benefits integration**,
> So that **claim payments are automatically adjusted against applicable statutory benefits, ensuring compliance and reducing manual processing**


**Key Capabilities:**

> 1. Configure offset rules using priority hierarchy (1-9) mapping claim attributes to offset types
>     1.1 Define state-specific program offsets for disability and family leave benefits
>     1.2 Establish cross-claim type coordination rules
> 2. System evaluates claims against configuration rules in priority sequence during payment processing
> 3. Upon matching claim characteristics, system applies corresponding offset type automatically
> 4. When state coverage codes are detected, system assigns jurisdiction-specific offset mechanisms
> 5. System prevents duplicate offsets through priority-based rule precedence
> 6. Integration with payment scheduler applies offset calculations to benefit disbursements


**Acceptance Criteria:**

> 1. **Given** offset rules are configured by priority, **When** a claim matches multiple rules, **Then** system applies the highest priority match only
> 2. **Given** state-specific coverage codes exist, **When** claim is processed, **Then** system assigns corresponding statutory offset type
> 3. **Given** STD claim is processed, **When** cross-claim rules apply, **Then** system configures offsets for related LTD claims
> 4. **Given** no matching offset rule exists, **When** claim is evaluated, **Then** system proceeds without applying offsets
> 5. **Given** offset configuration is incomplete, **When** system attempts processing, **Then** payment execution is prevented until resolution
> 6. **Given** offset type is applied, **When** payment calculation occurs, **Then** statutory benefits are deducted per jurisdictional requirements


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=693049530"
> ]

---

#### Feature: As a Claims Operations Manager, I want the system to automatically update FICA tax rates through a dedicated editor interface, so that tax calculations remain current without manual OpenL Studio updates
- **Role**: Claim Adjuster
- **Action**: maintain current FICA tax rates through a dedicated configuration interface that automatically synchronizes with the claims processing system
- **Value**: tax calculations remain accurate and compliant without requiring manual technical system updates or OpenL Studio expertise

**Description:**

> As a **Claim Adjuster**,
> I want to **maintain current FICA tax rates through a dedicated configuration interface that automatically synchronizes with the claims processing system**,
> So that **tax calculations remain accurate and compliant without requiring manual technical system updates or OpenL Studio expertise**


**Key Capabilities:**

> 1. User accesses tax rate configuration interface and reviews current FICA rates organized by effective year with applicable rates and thresholds
> 2. User updates tax information by adding new year records with updated rates, modifying existing rate configurations, or removing obsolete entries
>     2.1 Upon adding records, system pre-populates with sequential year and current rates as baseline
>     2.2 Upon modification, system validates rate percentages and threshold values in real-time
> 3. System validates all entries against business rules preventing duplicate years, invalid percentages, or incomplete data
> 4. User persists changes to either workspace for review or directly to selected configuration branch
> 5. System applies rate configurations across effective date ranges automatically until superseded by newer records
> 6. User may escalate to advanced configuration mode when complex technical adjustments are required


**Acceptance Criteria:**

> 1. **Given** user has view permissions, **When** accessing configuration interface, **Then** system displays current FICA rates sorted by year with all rate components and thresholds
> 2. **Given** user adds new year record, **When** saving changes, **Then** system prevents duplicate years and enforces percentage ranges 0-100 and non-negative thresholds
> 3. **Given** incomplete required data, **When** attempting to save, **Then** system blocks submission and identifies missing information
> 4. **Given** valid configuration changes, **When** user submits to branch, **Then** system persists entire project updates and applies rates to specified effective periods
> 5. **Given** user lacks edit permissions, **When** accessing interface, **Then** system allows review but restricts all modification operations
> 6. **Given** rates configured for specific year, **When** processing claims, **Then** system applies rates to that year and all subsequent years until next defined rate record


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=724146151"
> ]

---

#### Feature: As a Claims Adjuster, I want to apply common rounding rules consistently across all claim calculations, so that payment amounts are accurate and compliant with policy terms
- **Role**: Claim Adjuster
- **Action**: apply consistent rounding methodologies across all claim financial calculations
- **Value**: payment amounts remain accurate, compliant with policy terms, and mathematically consistent throughout the claim lifecycle

**Description:**

> As a **Claim Adjuster**,
> I want to **apply consistent rounding methodologies across all claim financial calculations**,
> So that **payment amounts remain accurate, compliant with policy terms, and mathematically consistent throughout the claim lifecycle**


**Key Capabilities:**

> 1. System retrieves applicable rounding rules based on claim type, policy terms, and regulatory requirements
> 2. Upon calculating benefit amounts, deductibles, or payment values, system automatically applies designated rounding methodology (round half up, round down, or banker's rounding)
> 3. System validates that all intermediate and final calculation results adhere to the established rounding standards
> 4. When calculations involve multiple steps, system maintains rounding consistency across the entire calculation chain
> 5. System documents applied rounding method in calculation audit trail for compliance verification


**Acceptance Criteria:**

> 1. **Given** a claim calculation requiring monetary rounding, **When** the system performs the calculation, **Then** the designated rounding rule is applied consistently
> 2. **Given** multiple calculation steps in a claim, **When** interim results are computed, **Then** all steps use the same rounding methodology
> 3. **Given** different claim types, **When** calculations are performed, **Then** appropriate rounding rules are selected based on policy configuration
> 4. **Given** a completed calculation, **When** auditing occurs, **Then** the applied rounding method is traceable in system records
> 5. **Given** regulatory compliance requirements, **When** payment amounts are finalized, **Then** rounding methods align with jurisdictional standards


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=693051053"
> ]

---

#### Feature: As a Claims Adjuster, I want to validate duplicate cases and claims to prevent duplicate processing, so that claimants are not paid multiple times for the same loss event
- **Role**: Claim Adjuster
- **Action**: validate and prevent duplicate cases and claims during intake and processing
- **Value**: claimants are protected from duplicate payments for the same loss event and the organization prevents overpayment exposure

**Description:**

> As a Claim Adjuster,
> I want to validate and prevent duplicate cases and claims during intake and processing,
> So that claimants are protected from duplicate payments for the same loss event and the organization prevents overpayment exposure


**Key Capabilities:**

> 1. Upon claim or case intake initiation, system executes duplicate validation process against existing records
> 2. System compares loss event characteristics, claimant identifiers, and coverage attributes to detect potential duplicates
> 3. When duplicate is identified, system prevents new entry creation and links submission to existing case or claim record
> 4. User is able to review flagged potential duplicates and confirm or override system determination with justification
> 5. System maintains audit trail of duplicate validation outcomes and adjuster override decisions
> 6. Upon confirmation of duplicate, system routes user to existing claim record for consolidated processing


**Acceptance Criteria:**

> 1. **Given** a claim submission is received, **When** duplicate validation executes, **Then** system identifies matching existing cases or claims based on defined matching criteria
> 2. **Given** a duplicate is detected, **When** validation completes, **Then** system prevents creation of new claim record and links to existing record
> 3. **Given** potential duplicate is flagged, **When** adjuster reviews, **Then** user can confirm duplicate status or override with documented business justification
> 4. **Given** duplicate validation fails to find matches, **When** processing continues, **Then** new claim proceeds through standard adjudication workflow
> 5. **Given** multiple claims exist for same loss event, **When** duplicate validation occurs, **Then** system consolidates under single case identifier
> 6. **Given** duplicate prevention occurs, **When** process completes, **Then** audit trail captures validation decision and any manual overrides


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=693051053"
> ]

---

#### Feature: As a Claims Adjuster, I want to view standardized EOB remark messages for claim decisions, so that claimants receive clear and consistent explanations of claim outcomes
- **Role**: Claim Adjuster
- **Action**: access and apply standardized Explanation of Benefits (EOB) remark messages when finalizing claim decisions
- **Value**: claimants receive clear, consistent, and compliant explanations of claim outcomes, reducing confusion and improving transparency

**Description:**

> As a **Claim Adjuster**,
> I want to **access and apply standardized Explanation of Benefits (EOB) remark messages when finalizing claim decisions**,
> So that **claimants receive clear, consistent, and compliant explanations of claim outcomes, reducing confusion and improving transparency**.


**Key Capabilities:**

> 1. Upon finalizing a claim decision, the adjuster retrieves applicable EOB remark codes from the common business rules framework.
> 2. System automatically suggests standardized messages based on claim outcome (approved, denied, partially paid, adjusted).
> 3. Adjuster reviews and selects appropriate remark codes aligned with decision rationale.
> 4. System generates EOB documentation incorporating selected remarks for claimant communication.
> 5. When multiple decision factors apply, adjuster composes combined remarks ensuring clarity and completeness.
> 6. System validates remark consistency with claim disposition before finalizing communication.


**Acceptance Criteria:**

> 1. **Given** a claim decision is finalized, **When** the adjuster accesses EOB messaging, **Then** standardized remark codes relevant to the decision type are presented.
> 2. **Given** standardized remarks are selected, **When** EOB is generated, **Then** messaging is consistent with regulatory requirements and claim outcome.
> 3. **Given** multiple decision factors exist, **When** adjuster composes remarks, **Then** system supports combining multiple codes without conflicts.
> 4. **Given** an incomplete remark selection, **When** adjuster attempts finalization, **Then** system prevents submission until required explanations are provided.
> 5. **Given** EOB is issued, **When** claimant receives communication, **Then** remark messages clearly explain decision rationale.
> 6. **Given** audit review, **When** EOB history is examined, **Then** all remark codes are traceable to decision logic.


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=693051053"
> ]

---

#### Feature: As a Claims Adjuster, I want to validate premium paid to date conditions before processing claims, so that only claims with adequate premium payment history are approved
- **Role**: Claim Adjuster
- **Action**: validate premium payment status against policy requirements before authorizing claim processing
- **Value**: only claims with adequate premium payment history are approved, reducing financial risk and ensuring policy compliance

**Description:**

> As a **Claim Adjuster**,
> I want to **validate premium payment status against policy requirements before authorizing claim processing**,
> So that **only claims with adequate premium payment history are approved, reducing financial risk and ensuring policy compliance**.


**Key Capabilities:**

> 1. System retrieves policy premium payment history when claim is submitted for adjudication
> 2. Validation engine applies premium paid-to-date conditions against claim effective dates
> 3. Upon detecting insufficient premium payment, system flags claim for payment hold or denial
> 4. System proceeds with claim processing when premium payment requirements are satisfied
> 5. Adjuster is able to review premium validation results and override with appropriate authorization if business exception applies
> 6. System records validation outcome and rationale for audit trail


**Acceptance Criteria:**

> 1. **Given** a claim is submitted for adjudication, **When** premium payments are current through claim date, **Then** system allows claim to proceed to payment authorization
> 2. **Given** premium payment validation executes, **When** premiums are past due beyond grace period, **Then** system prevents claim payment and notifies adjuster
> 3. **Given** premium status is insufficient, **When** adjuster has override authority, **Then** system allows manual approval with documented justification
> 4. **Given** validation completes, **When** results are recorded, **Then** system maintains audit trail of validation decision and timestamp
> 5. **Given** multiple claims exist for same policy, **When** premium status changes, **Then** system revalidates all pending claims against updated payment status


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=693051053"
> ]

---

#### Feature: As a Claims Adjuster, I want to calculate full calendar months consistently across all claim types, so that benefit periods and waiting periods are accurately determined
- **Role**: Claim Adjuster
- **Action**: apply consistent calendar full month calculation rules across all claim types to accurately determine benefit periods, waiting periods, and coverage durations
- **Value**: temporal calculations are standardized, ensuring accurate benefit determinations, regulatory compliance, and equitable treatment of all claimants regardless of claim type

**Description:**

> As a **Claim Adjuster**,
> I want to **apply consistent calendar full month calculation rules across all claim types to accurately determine benefit periods, waiting periods, and coverage durations**,
> So that **temporal calculations are standardized, ensuring accurate benefit determinations, regulatory compliance, and equitable treatment of all claimants regardless of claim type**


**Key Capabilities:**

> 1. Upon claim submission, system validates eligibility and premium payment status as prerequisites
> 2. System automatically applies standardized calendar full month calculation rules when determining benefit periods
> 3. System consistently calculates waiting periods using full month logic across all claim types
> 4. System determines coverage duration boundaries using uniform temporal calculation standards
> 5. Upon calculation completion, system applies common rounding rules to resulting benefit amounts
> 6. System generates EOB documentation reflecting accurately calculated time-based benefit determinations


**Acceptance Criteria:**

> 1. **Given** a claim requires benefit period calculation, **When** the adjuster initiates adjudication, **Then** the system applies standardized full month rules consistently regardless of claim type
> 2. **Given** waiting period determination is needed, **When** temporal calculation occurs, **Then** the system calculates full months uniformly per AH LA standards
> 3. **Given** multiple claims with identical time parameters, **When** calculations are performed, **Then** all results match demonstrating calculation consistency
> 4. **Given** coverage duration spans partial months, **When** full month logic is applied, **Then** the system accurately determines complete month counts
> 5. **Given** calculation produces benefit amounts, **When** finalization occurs, **Then** the system applies common rounding rules to monetary results
> 6. **Given** adjudication completes, **When** EOB generation occurs, **Then** documentation accurately reflects standardized time-based calculations


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=693051053"
> ]

---

#### Feature: As a Claims Adjuster, I want to use auto-assignment rules for case and claim routing, so that cases are efficiently distributed to appropriate claim management queues
- **Role**: Claim Adjuster
- **Action**: leverage automated assignment rules to route cases and claims to appropriate management queues based on predefined business criteria
- **Value**: workload is distributed efficiently, reducing manual triage effort and ensuring timely claim handling by the right resource

**Description:**

> As a **Claim Adjuster**,
> I want to **leverage automated assignment rules to route cases and claims to appropriate management queues based on predefined business criteria**,
> So that **workload is distributed efficiently, reducing manual triage effort and ensuring timely claim handling by the right resource**.


**Key Capabilities:**

> 1. System evaluates incoming case or claim attributes upon intake completion.
> 2. Auto-assignment logic applies predefined routing rules based on criteria such as claim type, coverage, complexity, and resource availability.
> 3. Case or claim is automatically assigned to designated user queue or adjuster.
> 4. System logs assignment decision and notifies assigned party.
>     4.1 If no eligible resource is available, route to default supervisory queue.
> 5. Adjuster accesses assigned workload through prioritized queue interface.
> 6. System supports reassignment if routing criteria change or escalation is required.


**Acceptance Criteria:**

> 1. **Given** a new claim intake is completed, **When** assignment rules are triggered, **Then** the system routes the claim to the appropriate queue without manual intervention.
> 2. **Given** routing criteria include claim complexity and adjuster capacity, **When** multiple queues qualify, **Then** the system prioritizes based on workload balance.
> 3. **Given** no eligible adjuster is available, **When** assignment fails, **Then** the system escalates to a supervisory queue and notifies management.
> 4. **Given** duplicate claim detection occurs, **When** assignment is attempted, **Then** the system prevents duplicate routing and flags for review.
> 5. **Given** assignment is completed, **When** the adjuster logs in, **Then** the claim appears in their prioritized work queue.
> 6. **Given** reassignment is required, **When** criteria change, **Then** the system supports manual or automated re-routing with audit trail.


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=693051053"
> ]

---

#### Feature: As a System Administrator, I want to configure coverage-based claim processing rules and override options, so that claim adjudication respects policy-specific benefit limits and calculation methods
- **Role**: Claim Adjuster
- **Action**: configure coverage-specific adjudication rules with controlled override permissions for benefit calculations
- **Value**: claim decisions automatically respect policy limits, calculation methods, and prevent conflicting manual adjustments that could violate benefit structures

**Description:**

> As a **Claim Adjuster**,
> I want to **configure coverage-specific adjudication rules with controlled override permissions for benefit calculations**,
> So that **claim decisions automatically respect policy limits, calculation methods, and prevent conflicting manual adjustments that could violate benefit structures**.


**Key Capabilities:**

> 1. System evaluates coverage configuration to determine field override permissions based on limit unit type (monetary vs non-monetary)
> 2. When limit unit is monetary and gross amount auto-calculates, system permits gross amount override while blocking unit quantity override
> 3. When limit unit is non-monetary and units auto-calculate, system permits unit override while blocking gross amount override
> 4. System enforces mutual exclusivity preventing simultaneous override of gross amount and occurrence units
> 5. Upon detecting special benefit types or specific accumulator periods, system blocks all override permissions
> 6. System applies configuration across group and individual product lines with coverage-specific rule inheritance


**Acceptance Criteria:**

> 1. **Given** coverage has monetary limit unit with auto-calculated gross amount, **When** adjudicator accesses claim, **Then** system enables gross amount override and disables unit override
> 2. **Given** coverage has non-monetary limit unit with auto-calculated units, **When** adjudicator processes claim, **Then** system enables unit override and disables gross amount override
> 3. **Given** coverage uses day-based limits with benefit/calendar year accumulator, **When** system evaluates permissions, **Then** both override options are blocked
> 4. **Given** coverage belongs to special benefit exclusion list, **When** adjudication begins, **Then** system prevents all override attempts
> 5. **Given** either field is editable or defaults to fixed value, **When** configuration loads, **Then** system blocks both override permissions
> 6. **Given** adjudicator attempts simultaneous overrides, **When** submission occurs, **Then** system rejects transaction with constraint violation


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=520070945"
> ]

---
## Initiative: Claims Intake & Event Case Creation

### Epic: Leave Claims Integration & Management

#### Feature: As a Claims Examiner, I want to initiate FMLA Leave Case intake with absence details, so that I can create an Event Case with associated Leave Claims in both EIS and the Integration Partner system
- **Role**: Claim Adjuster
- **Action**: initiate FMLA Leave Case intake with absence details and create an Event Case with associated Leave Claims synchronized across EIS and Integration Partner systems
- **Value**: I can establish compliant leave management workflows that align with federal, state, and local regulations while ensuring seamless data coordination between systems

**Description:**

> As a **Claim Adjuster**,
> I want to **initiate FMLA Leave Case intake with absence details and create an Event Case with associated Leave Claims synchronized across EIS and Integration Partner systems**,
> So that **I can establish compliant leave management workflows that align with federal, state, and local regulations while ensuring seamless data coordination between systems**


**Key Capabilities:**

> 1. User is able to initiate leave case intake by providing member identity, absence reason, absence period details, and event information
>     1.1 Upon incomplete information submission, system creates case in incomplete state and assigns review error task
>     1.2 Upon duplicate period detection, system prevents case creation and notifies user of existing open cases
> 2. System automatically creates Event Case and Leave Claims in both EIS and Integration Partner systems based on eligibility rules
> 3. System generates automated tasks for eligibility packet distribution, HR communication, and manager notification
> 4. User is able to collect supporting documentation through correspondence workflows that auto-complete tasks upon letter sending
> 5. System synchronizes coverage details, approval statuses, absence timelines, and accumulator information between systems
> 6. User is able to approve absences and trigger automated notification workflows to insured parties and HR representatives


**Acceptance Criteria:**

> 1. **Given** absence details are complete and no duplicate period exists, **When** intake is submitted, **Then** Event Case and Leave Claims are created in both systems with automated tasks assigned
> 2. **Given** mandatory information is missing, **When** case creation is attempted, **Then** system creates incomplete case and assigns review error task to adjuster
> 3. **Given** duplicate absence period exists, **When** case submission occurs, **Then** system prevents creation and displays error notification with existing case reference
> 4. **Given** correspondence tasks are completed, **When** letters are sent from Integration Partner system, **Then** tasks auto-complete and documents appear in EIS eFolder
> 5. **Given** approval is completed in Integration Partner system, **When** data synchronization occurs, **Then** coverage details, approval statuses, and timelines display in EIS
> 6. **Given** case closure is initiated, **When** case status changes to closed, **Then** all open tasks are auto-completed in both systems


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=801774413"
> ]

---

#### Feature: As a Claims Examiner, I want to receive validation errors when Case intake lacks required information or contains duplicate absence periods, so that I can correct the submission before Case creation
- **Role**: Claim Adjuster
- **Action**: receive validation errors when case intake lacks required information or contains duplicate absence periods, enabling correction before case creation
- **Value**: I can ensure data quality, prevent duplicate case processing, and maintain compliance with leave management regulations by addressing errors early in the intake process

**Description:**

> As a **Claim Adjuster**,
> I want to **receive validation errors when case intake lacks required information or contains duplicate absence periods, enabling correction before case creation**,
> So that **I can ensure data quality, prevent duplicate case processing, and maintain compliance with leave management regulations by addressing errors early in the intake process**


**Key Capabilities:**

> 1. Upon case intake completion, system validates required information against Integration Partner system eligibility rules and existing case data
> 2. When required member details, absence reason, initial absence date, date last worked, or actively at work date are missing, system creates case in Incomplete state
> 3. When submitted absence period overlaps with existing open or completed cases, system prevents case creation and flags duplicate period conflict
> 4. System automatically generates TXT>Review Case Error task assigned to Case Owner or Claim Management queue
> 5. Task description provides specific error details including missing information elements or conflicting case references
> 6. Claim Adjuster can access incomplete case, review validation errors, correct submission data, and resubmit for case creation


**Acceptance Criteria:**

> 1. **Given** case intake missing required member or absence details, **When** intake is completed, **Then** system creates case in Incomplete state and generates Review Case Error task
> 2. **Given** case intake with duplicate absence period, **When** system detects overlap with existing open cases, **Then** case remains incomplete with error message identifying conflicting case number
> 3. **Given** Review Case Error task created, **When** task is assigned, **Then** task description contains specific validation failure reasons and actionable correction guidance
> 4. **Given** incomplete case corrected, **When** resubmitted with complete information, **Then** system successfully creates Event Case and FMLA Leave Claim in both EIS and Integration Partner systems
> 5. **Given** validation errors corrected, **When** case creation succeeds, **Then** system auto-completes Review Case Error task and initiates standard case workflow
> 6. **Given** duplicate period error, **When** Claim Adjuster reviews, **Then** system prevents case creation until conflicting period is resolved or modified


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=801774413"
> ]

---

#### Feature: As a Claims Examiner, I want to navigate between EIS and the Integration Partner system via a Leave Management link, so that I can review Case and Claim details in both systems seamlessly
- **Role**: Claim Adjuster
- **Action**: navigate seamlessly between the enterprise claims system and the integrated absence management platform to access consolidated case and claim information
- **Value**: I can efficiently review and adjudicate leave-related claims by accessing comprehensive absence data across both systems without manual lookups or duplicate data entry

**Description:**

> As a **Claim Adjuster**,
> I want to **navigate seamlessly between the enterprise claims system and the integrated absence management platform to access consolidated case and claim information**,
> So that **I can efficiently review and adjudicate leave-related claims by accessing comprehensive absence data across both systems without manual lookups or duplicate data entry**


**Key Capabilities:**

> 1. System establishes case eligibility for cross-platform navigation based on absence reason classification and completeness validation
> 2. User reviews case details and claim attributes within the primary claims environment
> 3. User initiates navigation to the integrated absence management platform via system-generated access point
> 4. System executes secure transfer maintaining session context and case identifiers
> 5. User accesses extended absence period details and employer-specific leave policies in partner system
>     5.1 When duplicate absence periods are detected, system prevents navigation and surfaces resolution task
>     5.2 When employer information is incomplete, system withholds navigation and triggers data remediation workflow


**Acceptance Criteria:**

> 1. **Given** a complete leave case with valid absence reason, **When** the adjuster accesses case details, **Then** the system provides navigation capability to the partner platform
> 2. **Given** duplicate absence periods exist, **When** case creation occurs, **Then** the system blocks navigation and generates error resolution task identifying conflicting cases
> 3. **Given** missing employer data, **When** case intake completes, **Then** the system prevents cross-platform access until required information is supplemented
> 4. **Given** successful navigation initiation, **When** the adjuster transfers to partner system, **Then** case context and claim identifiers persist across platforms
> 5. **Given** user credentials validated in both systems, **When** cross-platform transfer occurs, **Then** authentication seamlessly authorizes access without re-login


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=801782594"
> ]

---

#### Feature: As a Claims Examiner, I want to access automatically created tasks for letter generation (Send Eligibility Packet, HR Communication, Manager Communication), so that I can collect information needed to determine leave eligibility
- **Role**: Claim Adjuster
- **Action**: access and process automatically generated correspondence tasks to collect required information for leave eligibility determination
- **Value**: I can systematically gather documentation from employees, HR, and managers to assess leave requests in compliance with federal, state, and local regulations

**Description:**

> As a **Claim Adjuster**,
> I want to **access and process automatically generated correspondence tasks to collect required information for leave eligibility determination**,
> So that **I can systematically gather documentation from employees, HR, and managers to assess leave requests in compliance with federal, state, and local regulations**


**Key Capabilities:**

> 1. Upon event case and leave claim creation, system automatically generates correspondence tasks (Send Eligibility Packet, HR Communication, Manager Communication) assigned to case owner or claim management queue
> 2. User accesses tasks from case-level work queue and navigates to integrated correspondence creation interface via embedded task links
> 3. User creates and sends required letters through integration partner system to collect eligibility information from stakeholders
>     3.1 When letters are sent, corresponding tasks automatically complete
>     3.2 User returns to case management system
> 4. User reviews received responses and attaches documentation to case repository for eligibility assessment
> 5. User reviews eligibility details and coverage information synchronized from integration partner system to support approval decisions


**Acceptance Criteria:**

> 1. **Given** leave case intake is completed, **When** system processing occurs, **Then** correspondence tasks appear in case-level work queue assigned per business rules
> 2. **Given** user accesses correspondence task, **When** task link is activated, **Then** user navigates to integrated letter creation interface with case context preserved
> 3. **Given** user completes and sends letter, **When** transmission confirms, **Then** originating task automatically completes and letter appears in case repository
> 4. **Given** stakeholder response is received, **When** user attaches documentation, **Then** information is available for eligibility review across integrated systems
> 5. **Given** incomplete information at intake, **When** system validation fails, **Then** case enters incomplete state with error review task generated
> 6. **Given** user requires additional case context, **When** navigating between systems, **Then** bidirectional navigation maintains workflow continuity


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=801774413"
> ]

---

#### Feature: As a Claims Examiner, I want to create and send correspondence letters from the Integration Partner system and have them automatically appear in the EIS eFolder, so that I can maintain a complete audit trail of all communications
- **Role**: Claim Adjuster
- **Action**: create and send correspondence letters from the Integration Partner system that automatically synchronize to the EIS eFolder
- **Value**: I can maintain a complete audit trail of all leave-related communications and ensure compliance with regulatory documentation requirements

**Description:**

> As a **Claim Adjuster**,
> I want to **create and send correspondence letters from the Integration Partner system that automatically synchronize to the EIS eFolder**,
> So that **I can maintain a complete audit trail of all leave-related communications and ensure compliance with regulatory documentation requirements**


**Key Capabilities:**

> 1. Upon receiving correspondence generation task, user is able to navigate from EIS task to Integration Partner letter creation interface
> 2. User is able to compose and send required letters (eligibility packets, designation notices, HR/manager communications) within Integration Partner system
> 3. When letter is finalized and sent, system automatically transfers document to EIS eFolder 'Other' section for unified access
> 4. User is able to review all sent correspondence directly from EIS eFolder without switching systems
> 5. Upon successful letter transmission, originating task auto-completes and user returns to EIS workflow
> 6. System maintains bidirectional document visibility ensuring complete audit trail across both platforms


**Acceptance Criteria:**

> 1. **Given** correspondence task is assigned, **When** user accesses task details, **Then** system provides direct navigation link to Integration Partner letter creation interface
> 2. **Given** letter is composed in Integration Partner system, **When** user finalizes and sends correspondence, **Then** document automatically appears in EIS eFolder 'Other' section within defined SLA
> 3. **Given** letter transmission is successful, **When** system confirms delivery, **Then** originating task auto-completes and user is returned to EIS environment
> 4. **Given** multiple letters are sent for same case, **When** user accesses EIS eFolder, **Then** all correspondence appears chronologically with complete metadata
> 5. **Given** document synchronization fails, **When** error occurs, **Then** system prevents task completion and alerts user to resolution requirement
> 6. **Given** case is closed, **When** audit review is required, **Then** all correspondence remains accessible in EIS eFolder with complete traceability


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=801774413"
> ]

---

#### Feature: As a Claims Examiner, I want to review FMLA Claim eligibility information and absence timelines synced from the Integration Partner system, so that I can make informed approval decisions based on current coverage and accumulator data
- **Role**: Claim Adjuster
- **Action**: review synchronized FMLA eligibility information and absence timelines from the Integration Partner system
- **Value**: I can make informed approval decisions based on current coverage, accumulator data, and regulatory compliance

**Description:**

> As a **Claim Adjuster**,
> I want to **review synchronized FMLA eligibility information and absence timelines from the Integration Partner system**,
> So that **I can make informed approval decisions based on current coverage, accumulator data, and regulatory compliance**


**Key Capabilities:**

> 1. Initiate Leave case intake by providing member, event, and absence details (reason, period, dates)
> 2. System automatically creates Event Case with FMLA Claim in both systems and applies regulatory eligibility rules
>     2.1 Upon incomplete information, case is created in Incomplete state with review task assigned
>     2.2 When duplicate absence period is detected, case flagged with error notification
> 3. Collect additional information by processing case-level tasks and sending correspondence from Integration Partner system
> 4. Review eligibility information including coverage details, approval statuses, absence timelines, and accumulator data synchronized from Integration Partner
> 5. Approve absences based on retrieved coverage and regulatory compliance information
> 6. Close case and claim upon employee return-to-work confirmation


**Acceptance Criteria:**

> 1. **Given** case intake is complete with required information, **When** intake is submitted, **Then** system creates Event Case and FMLA Claim in both systems with eligibility rules applied
> 2. **Given** correspondence tasks are generated, **When** adjuster sends letters, **Then** tasks auto-complete and letters appear in eFolder
> 3. **Given** eligibility review is initiated, **When** system retrieves data from Integration Partner, **Then** coverage details, approval statuses, timelines, and accumulators are synchronized to EIS
> 4. **Given** case lacks required information, **When** intake is submitted, **Then** case is created in Incomplete state with review task assigned
> 5. **Given** absence approval is completed, **When** notification letters are sent, **Then** return-to-work task is created at case level
> 6. **Given** employee confirms return-to-work, **When** adjuster closes case, **Then** all open tasks are auto-completed


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=801774413"
> ]

---

#### Feature: As a Claims Examiner, I want to initiate the Absence Approval process and generate designation and adjudication letters, so that I can notify the insured and HR of the approved leave periods
- **Role**: Claim Adjuster
- **Action**: initiate the absence approval process and generate designation and adjudication letters
- **Value**: I can notify the insured and HR of approved leave periods in compliance with federal, state, and local regulations

**Description:**

> As a **Claim Adjuster**,
> I want to **initiate the absence approval process and generate designation and adjudication letters**,
> So that **I can notify the insured and HR of approved leave periods in compliance with federal, state, and local regulations**


**Key Capabilities:**

> 1. Retrieve eligibility and coverage data from integrated absence management system upon approval initiation
>     1.1 When adjuster triggers approval, system synchronizes coverage details, approval statuses, absence timelines, and remaining accumulators
> 2. Review approval information including coverage status, absence periods, and entitlement balances
> 3. Generate and dispatch designation notices to insured, HR, and manager stakeholders
>     3.1 Upon letter creation, system auto-completes notification tasks and stores correspondence in electronic folder
> 4. Establish return-to-work reminder task as placeholder for future employee notification
> 5. If incomplete eligibility data exists, system creates review error task to collect missing information before proceeding
> 6. If duplicate absence period detected, system flags case for date modification or duplicate resolution


**Acceptance Criteria:**

> 1. **Given** valid eligibility data exists, **When** adjuster initiates approval, **Then** system retrieves coverage, timelines, and accumulator information without manual data entry
> 2. **Given** approval information is synced, **When** adjuster reviews absence details, **Then** system displays approval statuses and remaining entitlements for all applicable coverage types
> 3. **Given** approval is confirmed, **When** adjuster generates letters, **Then** system creates designation notices for insured, HR, and manager, auto-completes tasks, and stores documents
> 4. **Given** letters are dispatched, **When** system processes completion, **Then** return-to-work task is created and assigned per business rules
> 5. **Given** incomplete case data, **When** approval is attempted, **Then** system prevents progression and generates error task for information collection
> 6. **Given** duplicate absence period, **When** case is submitted, **Then** system flags error and prompts date modification


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=801774413"
> ]

---

#### Feature: As a Claims Examiner, I want to receive and manage Return to Work reminders and verification tasks, so that I can ensure timely communication with the employee about their return date
- **Role**: Claim Adjuster
- **Action**: receive and manage Return to Work reminders and verification tasks
- **Value**: I can ensure timely communication with the employee about their return date and maintain compliance with leave regulations

**Description:**

> As a **Claim Adjuster**,
> I want to **receive and manage Return to Work reminders and verification tasks**,
> So that **I can ensure timely communication with the employee about their return date and maintain compliance with leave regulations**


**Key Capabilities:**

> 1. Upon Leave absence approval completion, system automatically creates Return to Work reminder task assigned to Case Manager or Claim Management queue
> 2. User is able to receive notification when Return to Work task becomes due based on approved absence end date
> 3. User is able to communicate return-to-work reminder to employee through multiple channels (email, SMS, letter)
> 4. Upon sending return-to-work reminder, system automatically generates Verify Return to Work follow-up task
> 5. User is able to process verification task when employee confirms their return, documenting actual return date
> 6. Upon case closure, system automatically completes all outstanding return-to-work tasks


**Acceptance Criteria:**

> 1. **Given** Leave absence approved, **When** approval notification sent, **Then** system creates Return to Work reminder task with due date aligned to absence end date
> 2. **Given** Return to Work task due, **When** Claim Adjuster accesses task, **Then** system provides employee contact details and approved return date
> 3. **Given** reminder communication sent, **When** submission confirmed, **Then** system creates Verify Return to Work task and assigns to appropriate queue
> 4. **Given** employee confirms return, **When** Claim Adjuster processes verification task, **Then** system enables case closure workflow
> 5. **Given** case closed, **When** closure processed, **Then** system auto-completes all open return-to-work tasks
> 6. **Given** multiple channels available, **When** Claim Adjuster selects communication method, **Then** system supports email, SMS, or letter generation


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=801774413"
> ]

---

#### Feature: As a Claims Operations Manager, I want to automatically close Cases and Claims when the employee returns to work and auto-complete remaining open tasks, so that the leave management process is efficiently concluded
- **Role**: Claim Adjuster
- **Action**: automatically close Leave Cases and associated Claims when an employee returns to work, with all remaining open tasks auto-completed
- **Value**: the leave management process concludes efficiently without manual intervention, reducing administrative burden and ensuring timely case resolution

**Description:**

> As a **Claim Adjuster**,
> I want to **automatically close Leave Cases and associated Claims when an employee returns to work, with all remaining open tasks auto-completed**,
> So that **the leave management process concludes efficiently without manual intervention, reducing administrative burden and ensuring timely case resolution**


**Key Capabilities:**

> 1. System verifies employee return to work notification through designated verification process
> 2. Upon return confirmation, system automatically initiates case closure workflow across EIS and Integration Partner systems
>     2.1 System identifies all open tasks associated with the Leave Case at case level
>     2.2 System validates no blocking conditions exist for automated closure
> 3. System auto-completes all remaining open tasks including correspondence, communication, and administrative tasks
> 4. System updates case and claim status to closed state with return-to-work date recorded
> 5. System synchronizes closure information bidirectionally between EIS and Integration Partner systems in real-time
> 6. System generates closure confirmation notification to Claim Adjuster and updates work queue


**Acceptance Criteria:**

> 1. **Given** an employee has returned to work and verification is confirmed, **When** the Claim Adjuster processes the verification task, **Then** the system automatically closes the Leave Case and all associated Claims
> 2. **Given** automated closure is triggered, **When** open tasks exist under the Case, **Then** all tasks are auto-completed without manual intervention
> 3. **Given** case closure is initiated, **When** blocking conditions exist (e.g., incomplete compliance requirements), **Then** system prevents automated closure and notifies Claim Adjuster of required actions
> 4. **Given** closure completes successfully, **When** systems synchronize, **Then** closure status reflects consistently across EIS and Integration Partner system
> 5. **Given** tasks are auto-completed, **When** closure finalizes, **Then** audit trail captures automated actions with timestamp and return-to-work date
> 6. **Given** closure notification is generated, **When** Claim Adjuster reviews work queue, **Then** closed case is removed from active work assignments


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=801774413"
> ]

---

#### Feature: As a Claims Examiner, I want to view New Claim and New Case notifications for FMLA Leave Claims, so that I can prioritize and track newly created cases in my work queue
- **Role**: Claim Adjuster
- **Action**: view and prioritize new FMLA claim and event case notifications in my work queue
- **Value**: I can efficiently identify, prioritize, and track newly created leave claims requiring review and processing

**Description:**

> As a **Claim Adjuster**,
> I want to **view and prioritize new FMLA claim and event case notifications in my work queue**,
> So that **I can efficiently identify, prioritize, and track newly created leave claims requiring review and processing**


**Key Capabilities:**

> 1. Upon employee submission of FMLA leave request, system automatically creates event case and associated claims in pending status
> 2. System displays 'New Claim' notification for each FMLA claim and 'New Case' notification for the associated event case in adjuster work queue
> 3. User is able to view consolidated notifications across EIS and AbsenceSoft systems from centralized work queue
> 4. System generates task assignments including eligibility verification, HR communication, and manager notification requirements
> 5. User is able to prioritize cases based on submission date, absence reason, and regulatory timelines
> 6. When case requires action, system provides navigation to detailed claim information and supporting documentation in eFolder


**Acceptance Criteria:**

> 1. **Given** employee submits FMLA claim, **When** case intake process completes, **Then** system creates notifications visible in adjuster work queue within 24 hours
> 2. **Given** multiple new claims exist, **When** adjuster accesses work queue, **Then** system displays both claim-level and case-level notifications with key identifiers
> 3. **Given** notification requires action, **When** adjuster selects notification, **Then** system navigates to appropriate case details and associated tasks
> 4. **Given** claim created via REST API or manual entry, **When** case established, **Then** system generates consistent notifications regardless of creation method
> 5. **Given** integrated systems synchronization, **When** data updates occur, **Then** notification status reflects current state without manual refresh
> 6. **Given** case assigned to adjuster, **When** regulatory timeline approaches, **Then** system escalates notification priority


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=781715772"
> ]

---

### Epic: Claims Intake & Event Case Creation

#### Feature: As a Claims Adjuster, I want to search for and select a member to initiate a new event case, so that I can begin the claims intake process for the correct insured party
- **Role**: Claim Adjuster
- **Action**: search for and select an insured member to initiate an event case
- **Value**: I can establish the correct member context and begin the multi-line claims intake process efficiently

**Description:**

> As a **Claim Adjuster**,
> I want to **search for and select an insured member to initiate an event case**,
> So that **I can establish the correct member context and begin the multi-line claims intake process efficiently**


**Key Capabilities:**

> 1. User initiates event case intake and searches for existing member records or adds a new member to the system
> 2. Upon member selection, user provides employment details to establish the employer-member relationship
> 3. User confirms member information and initiates case creation
> 4. System validates minimum required data and creates the event case entity
> 5. System automatically evaluates policy applicability and generates eligible claims based on coverage types (Life, Critical Illness, Hospital Indemnity, Accident, Accelerated Death)
> 6. User navigates to case overview to view the created event case and associated claims ready for processing


**Acceptance Criteria:**

> 1. **Given** a valid member search query, **When** the adjuster submits the search, **Then** the system returns matching member records for selection
> 2. **Given** member selection is complete, **When** the adjuster provides employment details and creates the case, **Then** the system validates minimum required data and establishes the event case
> 3. **Given** an event case is created, **When** the system evaluates applicability, **Then** eligible claims are automatically generated based on active policy coverages
> 4. **Given** a policy has a canceled status, **When** the system validates policy eligibility, **Then** the system prevents claim generation and notifies the user
> 5. **Given** incomplete or invalid data, **When** the system validates intake information, **Then** the system prevents case creation until corrections are made
> 6. **Given** case creation is successful, **When** the process completes, **Then** the user is directed to case overview with all generated claims visible


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=553164384"
> ]

---

#### Feature: As a Claims Adjuster, I want to enter case details including loss event, employment information, and claim event selection, so that the system can evaluate applicability and create applicable claims
- **Role**: Claim Adjuster
- **Action**: initiate event case intake by capturing loss event details, employment information, and claim event selection to trigger automated applicability and eligibility evaluation
- **Value**: the system automatically creates applicable claims across Life, Absence, and Supplemental Benefits lines, reducing manual effort and ensuring consistent case management

**Description:**

> As a **Claim Adjuster**,
> I want to **initiate event case intake by capturing loss event details, employment information, and claim event selection to trigger automated applicability and eligibility evaluation**,
> So that **the system automatically creates applicable claims across Life, Absence, and Supplemental Benefits lines, reducing manual effort and ensuring consistent case management**.


**Key Capabilities:**

> 1. User provides member identification and employment information to establish case foundation.
> 2. User selects applicable claim event type (Death, Critical Illness, Hospital Indemnity, Accelerated Death, or Accident) and supplies required event details.
> 3. User adds relevant parties and submits intake form for validation.
> 4. Upon successful validation, system creates Event Case and evaluates applicability rules against active policies.
> 5. System automatically generates applicable losses and claims based on product codes and selected claim events.
> 6. System performs eligibility evaluation and auto-adjudicates qualifying claims, calculating benefit amounts when criteria are satisfied.


**Acceptance Criteria:**

> 1. **Given** member and employment information are provided, **When** intake form is submitted, **Then** system validates minimum data requirements before creating Event Case.
> 2. **Given** claim event type is selected, **When** applicability evaluation executes, **Then** system generates applicable claims only for active policies matching product code rules.
> 3. **Given** policies have Canceled status, **When** system evaluates claim availability, **Then** system prevents claim generation for invalid policies.
> 4. **Given** Event Case is created, **When** system evaluates eligibility, **Then** qualifying claims are auto-adjudicated with calculated benefit amounts.
> 5. **Given** intake validation fails, **When** submission is attempted, **Then** system prevents case creation and displays correction requirements.
> 6. **Given** claims are generated, **When** user navigates to Case Overview, **Then** all related claims and case details are visible in unified view.


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=553164384"
> ]

---

#### Feature: As a Claims Adjuster, I want to add and manage parties (claimant, beneficiary, employer, etc.) with their roles and contact information, so that all relevant stakeholders are properly documented in the case
- **Role**: Claim Adjuster
- **Action**: register and manage stakeholder relationships within an event case
- **Value**: all relevant parties are properly documented and their roles are clearly established for accurate claim processing and communication

**Description:**

> As a **Claim Adjuster**,
> I want to **register and manage stakeholder relationships within an event case**,
> So that **all relevant parties are properly documented and their roles are clearly established for accurate claim processing and communication**.


**Key Capabilities:**

> 1. Navigate to party management interface during event case intake workflow
> 2. Identify party types and their relationships to the case (claimant, beneficiary, employer, dependent)
> 3. Capture stakeholder identity and contact information at case level
> 4. Validate party information completeness before case submission
>     4.1 Upon incomplete data, system prevents intake completion
>     4.2 User is able to correct and resubmit party details
> 5. Establish party-to-claim associations automatically based on claim type and coverage rules
> 6. Modify or add stakeholders post-intake when case circumstances change


**Acceptance Criteria:**

> 1. **Given** adjuster completes party registration during intake, **When** event case is submitted, **Then** system applies party information consistently across all auto-generated claims.
> 2. **Given** minimum party data requirements are not satisfied, **When** adjuster attempts submission, **Then** system prevents case creation and identifies missing stakeholder information.
> 3. **Given** multiple claim types are created under one event case, **When** party roles are defined, **Then** system establishes appropriate party-to-claim relationships based on coverage applicability rules.
> 4. **Given** adjuster adds a new party post-intake, **When** changes are saved, **Then** system updates case-level party registry and propagates to relevant claims.
> 5. **Given** party contact information is captured, **When** case overview is displayed, **Then** system presents complete stakeholder registry with roles and contact details.


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=553164384"
> ]

---

#### Feature: As a Claims Examiner, I want the system to automatically evaluate applicability rules after intake submission, so that applicable claims are created without manual intervention
- **Role**: Claim Adjuster
- **Action**: leverage automated applicability evaluation to create and adjudicate eligible claims upon intake submission
- **Value**: claims are initiated without manual intervention, reducing processing time and ensuring consistent rule-based decisions

**Description:**

> As a Claim Adjuster,
> I want to leverage automated applicability evaluation to create and adjudicate eligible claims upon intake submission,
> So that claims are initiated without manual intervention, reducing processing time and ensuring consistent rule-based decisions.


**Key Capabilities:**

> 1. System receives intake submission and initiates the claims case creation process
> 2. System executes applicability evaluation using predefined business rules to determine which claim types qualify based on policy status, loss date alignment, and provided evidence
> 3. System automatically creates applicable claims with pending status and assigns relevant coverages or benefits per claim type
>     3.1 When multiple applicability results exist for the same claim type, system applies aggregation logic
> 4. System performs automated adjudication to calculate initial benefit amounts using intake data and policy information
> 5. System assigns the claims case to appropriate user or queue based on predefined routing rules
> 6. User reviews the opened claims case and all auto-created claims for further processing decisions


**Acceptance Criteria:**

> 1. **Given** valid intake data is submitted, **When** applicability rules execute successfully, **Then** system creates all qualifying claims with pending status without manual intervention
> 2. **Given** policy effective date precedes loss date and policy is active, **When** applicability evaluation runs, **Then** system proceeds with claim creation
> 3. **Given** multiple applicability results share identical claim type, **When** system applies aggregation logic, **Then** only consolidated claims are created
> 4. **Given** claims require benefit assignment, **When** adjudication completes, **Then** system calculates benefit amounts and assigns coverages automatically
> 5. **Given** automated adjudication succeeds, **When** case assignment rules execute, **Then** system routes case to designated user or queue
> 6. **Given** insufficient data exists for automatic creation, **When** applicability evaluation completes, **Then** system prevents claim creation and flags case for manual review


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=761792141"
> ]

---

#### Feature: As a Claims Operations Manager, I want the system to automatically create applicable claims based on policy coverage and loss event type, so that claims processing begins immediately without manual claim creation
- **Role**: Claim Adjuster
- **Action**: automatically create applicable claims based on policy coverage validation and loss event evaluation upon event case intake completion
- **Value**: claims processing begins immediately without manual intervention, reducing processing time and ensuring consistent eligibility evaluation across all claim types

**Description:**

> As a **Claim Adjuster**,
> I want to **automatically create applicable claims based on policy coverage validation and loss event evaluation upon event case intake completion**,
> So that **claims processing begins immediately without manual intervention, reducing processing time and ensuring consistent eligibility evaluation across all claim types**


**Key Capabilities:**

> 1. Upon intake finalization, system evaluates applicability by retrieving valid policy versions and matching coverages against reported loss events and absence reasons
> 2. System creates pending claims automatically when validation rules confirm applicability and data completeness, applying aggregation logic for duplicate claim types
> 3. System maps event case data to claims, assigns handling queues and review tasks, and sets business flags for specialized processing workflows
> 4. System executes automated adjudication including eligibility evaluation, coverage assignment, benefit calculation, and accumulator creation for approved coverages
>     4.1 If validation identifies data issues, claim creation is suspended pending exception resolution
>     4.2 System distinguishes automated versus manual claims via internal generation flags for downstream service routing


**Acceptance Criteria:**

> 1. **Given** event case intake is finalized with valid policy and loss event data, **When** applicability evaluation executes, **Then** system creates all eligible claims with pending status and assigns to processing queues
> 2. **Given** multiple applicability results return identical claim types, **When** system applies aggregation logic, **Then** single consolidated claim is created without duplicates
> 3. **Given** automated claims are created, **When** adjudication executes, **Then** system assigns appropriate coverages, calculates benefits, and creates accumulators based on policy configurations
> 4. **Given** intake data contains validation issues, **When** applicability evaluation completes, **Then** system prevents claim creation and triggers exception handling workflow
> 5. **Given** claims require specialized handling, **When** system evaluates claim type and policy attributes, **Then** appropriate sub-statuses and processing flags are automatically assigned
> 6. **Given** claims and tasks are created, **When** auto-assignment rules execute, **Then** work items are routed to designated queues or examiners per configuration


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=761792149"
> ]

---

#### Feature: As a Claims Adjuster, I want to view the created event case and associated claims in a unified case overview, so that I can manage all related claims together
- **Role**: Claim Adjuster
- **Action**: access a consolidated view of the event case and all associated claims after intake completion
- **Value**: I can efficiently manage, monitor, and process all related claims under a single event case without navigating multiple systems

**Description:**

> As a **Claim Adjuster**,
> I want to **access a consolidated view of the event case and all associated claims after intake completion**,
> So that **I can efficiently manage, monitor, and process all related claims under a single event case without navigating multiple systems**


**Key Capabilities:**

> 1. Upon intake completion and automation execution, system presents unified event case overview interface
> 2. User is able to review event case metadata including loss event details, key dates, and case status
> 3. User is able to view all auto-generated claims linked to the event case with claim-specific attributes
> 4. User is able to access party information and roles associated with the case and individual claims
> 5. User is able to navigate to detailed claim processing workflows from the consolidated view
> 6. System displays financial summaries and case-level aggregations across associated claims


**Acceptance Criteria:**

> 1. **Given** intake is submitted and automation completes, **When** user accesses event case overview, **Then** system displays case header with event details and all associated claims
> 2. **Given** multiple claims are auto-created, **When** user views overview, **Then** system presents each claim with status, coverage type, and key dates
> 3. **Given** parties are defined during intake, **When** overview loads, **Then** system displays party roles for case and claim levels
> 4. **Given** user requires detailed processing, **When** user selects a claim, **Then** system navigates to claim-specific management interface
> 5. **Given** financial data exists, **When** overview is accessed, **Then** system aggregates and displays case-level financial summaries
> 6. **Given** case status is incomplete, **When** overview loads, **Then** system prevents claim processing until case finalization


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=761792148"
> ]

---

#### Feature: As a Claims Adjuster, I want to enter loss event details including date of loss, cause of loss, location, and claim type, so that the system can properly classify and route the claim
- **Role**: Claim Adjuster
- **Action**: capture and classify loss event information to initiate motor claim processing
- **Value**: the system can properly categorize, assess liability, and route the claim through appropriate processing workflows

**Description:**

> As a **Claim Adjuster**,
> I want to **capture and classify loss event information to initiate motor claim processing**,
> So that **the system can properly categorize, assess liability, and route the claim through appropriate processing workflows**


**Key Capabilities:**

> 1. User is able to record temporal loss event data including incident occurrence timing
> 2. User is able to document incident causation and circumstances through structured classification hierarchies
> 3. User is able to specify geographic loss and service location information
> 4. User is able to classify claim type and provide preliminary liability assessment
> 5. User is able to select claim processing approach based on business needs
>     5.1 When full processing is required, user selects customer version update
>     5.2 When documentation only is needed, user selects notification mode
> 6. User is able to identify vehicle damage severity and business insurance status, with capability to add additional involved parties before submitting the claim


**Acceptance Criteria:**

> 1. **Given** all required loss event data is provided, **When** the adjuster submits the claim, **Then** the system creates the claim record with proper classification and routing
> 2. **Given** mandatory causation information is missing, **When** submission is attempted, **Then** the system prevents claim creation until requirements are satisfied
> 3. **Given** multiple vehicles are non-drivable, **When** the adjuster identifies all affected vehicles, **Then** the system captures all vehicle status information
> 4. **Given** additional parties are involved, **When** the adjuster adds party information, **Then** the system associates all parties with the loss event
> 5. **Given** the adjuster abandons the intake process, **When** cancellation is requested, **Then** the system discards unsaved data without creating a claim record


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=576489516"
> ]

---

#### Feature: As a Claims Adjuster, I want to add coverage details including damage type, reserves, and deductibles to a claim, so that the claim is properly configured for adjudication
- **Role**: Claim Adjuster
- **Action**: configure coverage details including damage classification and financial parameters for a claim
- **Value**: the claim contains accurate coverage information enabling proper adjudication and reserve allocation

**Description:**

> As a **Claim Adjuster**,
> I want to **configure coverage details including damage classification and financial parameters for a claim**,
> So that **the claim contains accurate coverage information enabling proper adjudication and reserve allocation**


**Key Capabilities:**

> 1. User initiates coverage addition process displaying available first-party coverage options with associated limits and deductibles
> 2. User selects applicable coverage type from mutually exclusive options
> 3. User classifies damage category for the coverage being added
> 4. System presents contextual damage detail capture interface aligned to selected damage classification
> 5. User provides damage specifics corresponding to the selected category
> 6. System validates and persists coverage configuration to the claim record
>     6.1 Upon cancellation at any stage, system discards uncommitted coverage data


**Acceptance Criteria:**

> 1. **Given** user initiates coverage addition, **When** system presents options, **Then** available first-party coverages with limits and deductibles are displayed
> 2. **Given** user selects coverage type and damage classification, **When** proceeding to detail capture, **Then** system displays contextual fields matching damage category
> 3. **Given** user completes damage details, **When** submitting configuration, **Then** system persists coverage with all associated attributes to claim record
> 4. **Given** user cancels during configuration, **When** cancellation is confirmed, **Then** system discards all uncommitted coverage data without updating claim
> 5. **Given** incomplete damage information, **When** user attempts submission, **Then** system prevents persistence until required details are provided


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=571475105"
> ]

---

#### Feature: As a Claims Adjuster, I want to add and edit parties (insured, third parties, claimants) with their contact information and roles, so that all relevant parties are properly identified and contacted
- **Role**: Claim Adjuster
- **Action**: manage parties and their roles throughout the claim lifecycle
- **Value**: all relevant stakeholders are properly identified, contactable, and assigned appropriate responsibilities

**Description:**

> As a **Claim Adjuster**,
> I want to **manage parties and their roles throughout the claim lifecycle**,
> So that **all relevant stakeholders are properly identified, contactable, and assigned appropriate responsibilities**


**Key Capabilities:**

> 1. User initiates party association to case with designated role assignment
> 2. User searches existing parties using identification criteria or creates new party records when no match exists
> 3. System retrieves and displays candidate matches based on search parameters
> 4. User selects appropriate party from results and confirms role assignment
> 5. User updates party contact and address information as circumstances change
> 6. System maintains party relationship history and role assignments across case lifecycle


**Acceptance Criteria:**

> 1. **Given** valid search criteria, **When** user initiates party search, **Then** system returns matching candidates with sufficient detail for accurate selection
> 2. **Given** no matching party exists, **When** user provides minimum required information, **Then** system creates new party record and assigns designated role
> 3. **Given** party is associated with case, **When** user modifies contact details, **Then** system updates information and maintains audit trail
> 4. **Given** user attempts incomplete submission, **When** mandatory information is missing, **Then** system prevents record creation until requirements satisfied
> 5. **Given** user cancels operation mid-process, **When** confirmation requested, **Then** system discards unsaved changes upon confirmation


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=564681805"
> ]

---

#### Feature: As a Claims Adjuster, I want to navigate through multi-step intake wizard with Previous/Next buttons and step indicators, so that I can efficiently complete the intake process and review my entries
- **Role**: Claim Adjuster
- **Action**: navigate through a sequential intake workflow with bidirectional controls
- **Value**: I can efficiently progress through intake stages, review previous entries, and maintain data integrity throughout the case creation process

**Description:**

> As a Claim Adjuster,
> I want to navigate through a sequential intake workflow with bidirectional controls,
> So that I can efficiently progress through intake stages, review previous entries, and maintain data integrity throughout the case creation process


**Key Capabilities:**

> 1. User initiates case creation and selects member information to unlock progression
> 2. Upon member selection, user advances to case detail stage where loss event information is captured
> 3. User proceeds to additional parties stage to document involved entities
> 4. User is able to navigate backward to any previously visited stage to review or modify entries
> 5. When intake is complete, user finalizes submission and system transitions to case management workspace
> 6. System tracks completion status of each workflow stage throughout navigation


**Acceptance Criteria:**

> 1. **Given** intake workflow is initiated, **When** no member is selected, **Then** system prevents progression to subsequent stages
> 2. **Given** user is on any stage beyond first, **When** backward navigation is requested, **Then** system returns to previous stage preserving all entered data
> 3. **Given** user completes a stage, **When** advancing forward, **Then** system marks stage as visited and enables access to next milestone
> 4. **Given** all required stages are visited, **When** user finalizes intake, **Then** system creates event case and transitions to overview workspace
> 5. **Given** user navigates between stages, **When** returning to previously visited steps, **Then** system displays previously captured information without data loss


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=565742515"
> ]

---

#### Feature: As a System Administrator, I want the system to validate that required policy data exists and is active before creating claims, so that claims are only created against valid policies
- **Role**: Claim Intaker
- **Action**: enable the system to automatically validate policy eligibility and create claims upon case intake submission
- **Value**: claims are only generated against valid, active policies, reducing processing errors and ensuring regulatory compliance

**Description:**

> As a **Claim Intaker**,
> I want to **enable the system to automatically validate policy eligibility and create claims upon case intake submission**,
> So that **claims are only generated against valid, active policies, reducing processing errors and ensuring regulatory compliance**


**Key Capabilities:**

> 1. Upon intake submission, system initiates applicability evaluation to determine eligible claim types based on loss events and policy data
> 2. System retrieves and validates policy versions by matching master policies or certificates to the employee and employer, ensuring only active versions within loss date range are considered
> 3. System evaluates coverage applicability using configurable business rules, mapping loss events and absence reasons to eligible claim types
> 4. When validation confirms eligibility and data completeness, system automatically creates claims with pending status and assigns to processing queues
> 5. System executes adjudication to calculate benefit amounts, assign coverages, and create accumulators for limit tracking
> 6. If policy validation fails or required data is missing, system prevents claim creation and flags case for manual review


**Acceptance Criteria:**

> 1. **Given** intake data is submitted, **When** associated policy does not exist or is inactive, **Then** system prevents claim creation and notifies user of policy validation failure
> 2. **Given** valid policy exists, **When** coverage dates do not align with loss date, **Then** system blocks claim generation and flags discrepancy
> 3. **Given** policy and coverage validation passes, **When** applicability rules confirm eligibility, **Then** system creates claims automatically with pending status and assigns to default queue
> 4. **Given** multiple claim types are applicable, **When** aggregation logic detects duplicates, **Then** system consolidates into single claim per type
> 5. **Given** claim is auto-created, **When** adjudication completes, **Then** system assigns coverages, calculates benefits, and creates accumulators without manual intervention
> 6. **Given** auto-creation completes, **When** isGenerated flag is true, **Then** system distinguishes automated claims from manual entries for audit purposes


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=761792149"
> ]

---

#### Feature: As a Claims Examiner, I want the system to automatically assign coverages and calculate initial benefit amounts during claim creation, so that claims are ready for adjudication without manual setup
- **Role**: Claim Adjuster
- **Action**: automate claim creation, coverage assignment, and benefit calculation upon case intake completion
- **Value**: claims are immediately ready for adjudication without manual configuration, reducing processing time and human error

**Description:**

> As a **Claim Adjuster**,
> I want to **automate claim creation, coverage assignment, and benefit calculation upon case intake completion**,
> So that **claims are immediately ready for adjudication without manual configuration, reducing processing time and human error**.


**Key Capabilities:**

> 1. **Applicability Evaluation**: System validates intake data completeness, retrieves applicable policy versions (Master Policies and Certificates) based on event dates, and applies configurable business rules to determine eligible claim types (STD, Life, DI).
> 2. **Automated Claim Creation**: Upon successful validation, system generates claims with 'Pending' status, maps event case data to claim records, assigns claims to processing queues, and creates review tasks automatically.
> 3. **Coverage and Benefit Adjudication**: System evaluates eligibility, assigns applicable coverages (e.g., Core, BuyUp for Disability), and calculates initial benefit amounts using intake, CEM, and policy data.
> 4. **Accumulator Initialization**: System creates accumulators and calculates limit amounts for claims with assigned benefits.
>     4.1 When validation indicates claim type is not applicable, system prevents automatic creation and flags for manual review.
>     4.2 For ASO service claims, system applies special handling flags based on policy configuration.


**Acceptance Criteria:**

> 1. **Given** intake data is complete and valid policy versions exist, **When** the system evaluates applicability, **Then** eligible claim types are identified and claims are created automatically with 'Pending' status.
> 2. **Given** a claim is auto-created, **When** the adjudication process executes, **Then** applicable coverages are assigned and initial benefit amounts are calculated without manual intervention.
> 3. **Given** intake data is insufficient or policy is invalid, **When** validation occurs, **Then** system prevents automatic claim creation and flags the case for manual adjuster review.
> 4. **Given** multiple claims of the same type exist, **When** aggregation logic applies, **Then** system consolidates claims according to business rules.
> 5. **Given** a claim receives auto-assigned benefits, **When** accumulator management executes, **Then** system creates accumulators and calculates total limit amounts.
> 6. **Given** special claim types (TL/SB, DI with ASO), **When** claims are created, **Then** system applies specialized handling logic and sets appropriate flags automatically.


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=761792149"
> ]

---

#### Feature: As a Claims Adjuster, I want to cancel the intake process at any step with appropriate data handling, so that incomplete intakes do not clutter the system
- **Role**: Claim Adjuster
- **Action**: cancel the intake process at any stage with appropriate data handling based on intake progression
- **Value**: the system maintains data integrity and prevents incomplete or abandoned intakes from cluttering operational records

**Description:**

> As a Claim Adjuster,
> I want to cancel the intake process at any stage with appropriate data handling based on intake progression,
> So that the system maintains data integrity and prevents incomplete or abandoned intakes from cluttering operational records


**Key Capabilities:**

> 1. User is able to initiate cancellation at any step during the structured intake wizard before final submission
>     1.1 When cancellation occurs before claims case initiation, system terminates process without storing intake data
>     1.2 Upon cancellation after claims case initiation, system closes the case with appropriate closure reason
> 2. System evaluates intake progression state to determine appropriate data handling strategy
> 3. System prevents creation of orphaned claims or event cases when user abandons the intake workflow
> 4. System records cancellation timestamp and reason for audit trail purposes when case has been initiated
> 5. User is able to distinguish cancelled intakes from active pending cases in workload views


**Acceptance Criteria:**

> 1. **Given** user cancels intake before submitting initial data, **When** cancellation is confirmed, **Then** no claims case or related records are created in the system
> 2. **Given** user cancels intake after claims case has been initiated, **When** cancellation is processed, **Then** system assigns 'closed' status with cancellation reason to the event case
> 3. **Given** intake cancellation occurs mid-workflow, **When** system processes cancellation, **Then** no orphaned claims or incomplete benefit assignments remain in the database
> 4. **Given** claims case was closed due to intake cancellation, **When** user views workload dashboard, **Then** cancelled cases are excluded from active pending claims counts
> 5. **Given** cancellation occurs at any stage, **When** audit log is reviewed, **Then** system captures cancellation timestamp, user identity, and stage at which cancellation occurred


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=761792141"
> ]

---

#### Feature: As a Claims Adjuster, I want to create multiple claims within a single event case for different loss events and policy coverages, so that related claims are managed together
- **Role**: Claim Adjuster
- **Action**: create and manage multiple interrelated claims within a unified event case for different loss events and policy coverages
- **Value**: related claims arising from the same incident are consolidated, enabling coordinated adjudication, consistent data management, and streamlined payment processing across multiple benefit types

**Description:**

> As a **Claim Adjuster**,
> I want to **create and manage multiple interrelated claims within a unified event case for different loss events and policy coverages**,
> So that **related claims arising from the same incident are consolidated, enabling coordinated adjudication, consistent data management, and streamlined payment processing across multiple benefit types**.


**Key Capabilities:**

> 1. Initiate event case upon loss notification, capturing common information (member, employer, dependent, parties, diagnoses) applicable across all related claims.
> 2. Create multiple claim records under the event case, each linked to specific policy coverages (STD, LTD, Life, HI, CI, Accident) while inheriting shared event data.
> 3. Adjudicate individual claims independently, applying coverage-specific rules and benefit calculations while maintaining event case context.
>     3.1 When disability extends beyond STD duration and LTD policy exists, system automatically transitions to LTD claim creation at appropriate timing.
>     3.2 If claim is non-payable (FMLA leave, ASO arrangement, Premium Waiver), system applies special handling without payment disbursement.
> 4. Apply financial adjustments and deductions at event case level (tax withholdings, offsets) affecting all associated claims consistently.
> 5. Generate coordinated payments across claims, ensuring benefit coordination rules prevent duplicate payments for overlapping periods.
> 6. Close event case upon resolution of all constituent claims or administrative completion for non-payable scenarios.


**Acceptance Criteria:**

> 1. **Given** loss event reported, **When** event case created, **Then** system establishes shared data repository (member, employer, diagnoses) accessible to all subsequent claims under the case.
> 2. **Given** multiple applicable coverages exist, **When** adjuster creates claims, **Then** each claim links to correct policy coverage while inheriting event case common data without duplication.
> 3. **Given** STD claim active beyond benefit duration threshold, **When** LTD eligibility confirmed, **Then** system automatically creates LTD claim preventing overlapping benefit payment periods.
> 4. **Given** claim designated non-payable (FMLA, ASO, Premium Waiver), **When** adjudication occurs, **Then** system processes administratively without generating payment transactions.
> 5. **Given** Self Bill scenario, **When** claim created, **Then** system links to Master Policy and identifies employee class for correct benefit plan allocation.
> 6. **Given** all constituent claims resolved, **When** case closure initiated, **Then** system prevents closure if any claim remains in open or pending status.


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=761792143"
> ]

---

### Epic: Dental Claim Intake & Processing

#### Feature: As a Claims Adjuster, I want to search and select a policy and patient to initiate a dental claim, so that I can begin the claim intake process with the correct policyholder and beneficiary information
- **Role**: Claim Adjuster
- **Action**: search and associate a dental policy with the appropriate patient to initiate claim intake
- **Value**: the claim is linked to the correct policyholder and beneficiary, ensuring accurate adjudication and reducing processing errors

**Description:**

> As a **Claim Adjuster**,
> I want to **search and associate a dental policy with the appropriate patient to initiate claim intake**,
> So that **the claim is linked to the correct policyholder and beneficiary, ensuring accurate adjudication and reducing processing errors**.


**Key Capabilities:**

> 1. User initiates dental claim intake from customer portfolio
>     1.1 When customer is individual policyholder with single certificate, system auto-selects policy
>     1.2 When individual holds multiple certificates, system presents policy options for selection
> 2. User searches policy using policyholder identifiers or certificate number
> 3. System displays matching insureds under the organization's master policy scope
> 4. User selects policy from results and reviews policy details including plan and group information
> 5. User selects patient from eligible parties on the certificate (primary insured or dependents)
> 6. System confirms policy-patient association and enables claim intake progression


**Acceptance Criteria:**

> 1. **Given** user has claim creation privileges, **When** initiating claim from individual policyholder with single certificate, **Then** system auto-associates policy and proceeds to patient selection
> 2. **Given** user searches by valid policyholder identifier, **When** matches exist under organization's master policy, **Then** system displays eligible policies with coverage details
> 3. **Given** user searches with unsupported criteria or dependent-only parties, **When** search executes, **Then** system returns no results
> 4. **Given** policy is selected, **When** user chooses patient from certificate members, **Then** system establishes claim context and enables next intake stage
> 5. **Given** organization customer context, **When** user removes policy selection, **Then** system resets to search state


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=767862072"
> ]

---

#### Feature: As a Claims Adjuster, I want to select a provider and capture claim intake information including received date, source, transaction type, and payee type, so that I can establish the foundational claim details
- **Role**: Claim Adjuster
- **Action**: select a healthcare provider and establish foundational claim intake details including transaction metadata and payee designation
- **Value**: the claim can be properly attributed to the correct provider network status and processed with accurate administrative context for adjudication

**Description:**

> As a **Claim Adjuster**,
> I want to **select a healthcare provider and establish foundational claim intake details including transaction metadata and payee designation**,
> So that **the claim can be properly attributed to the correct provider network status and processed with accurate administrative context for adjudication**.


**Key Capabilities:**

> 1. User searches and selects healthcare provider using identifiers from administrative system
> 2. System retrieves and displays provider credentials, network participation status, and contact information
> 3. User captures claim receipt metadata including source channel and transaction classification
> 4. User designates payee type to establish payment routing rules
> 5. User is able to remove and reselect provider if initial selection requires correction
>     5.1 Upon removal, system clears provider attribution and re-enables search capability
> 6. System validates provider network status against policy effective dates and coverage provisions


**Acceptance Criteria:**

> 1. **Given** valid provider credentials are entered, **When** search is executed, **Then** system returns matching providers with current network status and administrative details
> 2. **Given** provider is selected, **When** user proceeds with intake, **Then** system associates claim with provider's network designation for benefit calculation
> 3. **Given** incomplete intake metadata, **When** user attempts submission, **Then** system prevents progression until required administrative fields are populated
> 4. **Given** provider is selected, **When** user removes selection, **Then** system clears provider association and enables new search without data carryover
> 5. **Given** all intake elements are captured, **When** user completes provider selection step, **Then** system establishes claim foundation enabling downstream adjudication workflows


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=784770698"
> ]

---

#### Feature: As a Claims Adjuster, I want to add and manage dental services with procedure codes, quantities, charges, and clinical details, so that I can accurately document all submitted dental procedures
- **Role**: Claim Adjuster
- **Action**: Add, edit, and manage dental service records with procedure codes, charges, and clinical details during claim intake
- **Value**: I can accurately document and maintain all submitted dental procedures to support proper claim adjudication and payment processing

**Description:**

> As a **Claim Adjuster**,
> I want to **add, edit, and manage dental service records with procedure codes, charges, and clinical details during claim intake**,
> So that **I can accurately document and maintain all submitted dental procedures to support proper claim adjudication and payment processing**


**Key Capabilities:**

> 1. User initiates dental claim intake and selects appropriate claim type to configure required service attributes
> 2. User adds service records by searching and selecting procedure codes, then providing quantities and charges
>     2.1 Upon Orthodontics claim type selection, system enables payment frequency and treatment duration fields
>     2.2 Upon Predetermination claim types, system waives service date requirement
> 3. User accesses comprehensive service editing to update basic attributes and extended clinical details
> 4. User provides supplementary clinical information including preauthorization, oral cavity areas, tooth identifiers, and diagnosis codes
> 5. User saves service records with option to continue adding multiple services sequentially
> 6. User is able to cancel unsaved entries or revert edits to previously saved service records


**Acceptance Criteria:**

> 1. **Given** user selects Orthodontics claim type, **When** adding service, **Then** system requires payment frequency and treatment duration fields
> 2. **Given** user selects Predetermination claim types, **When** submitting service, **Then** system permits submission without service date
> 3. **Given** user searches procedure codes, **When** entering characters, **Then** system displays matching codes for selection
> 4. **Given** user edits existing service record, **When** canceling changes, **Then** system reverts to previously saved values
> 5. **Given** user adds new service and cancels, **When** cancel action occurs, **Then** system removes unsaved service entry
> 6. **Given** user saves service with extended details, **When** submission completes, **Then** system persists all basic and clinical attributes for adjudication


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=770573468"
> ]

---

#### Feature: As a Claims Adjuster, I want to capture additional claim information including place of treatment, accident details, and missing teeth, so that I can document the full context of the dental claim
- **Role**: Claim Adjuster
- **Action**: capture supplemental dental claim details including treatment location, accident circumstances, and missing teeth information
- **Value**: I can establish complete clinical context and causation for accurate adjudication and payment determination

**Description:**

> As a **Claim Adjuster**,
> I want to **capture supplemental dental claim details including treatment location, accident circumstances, and missing teeth information**,
> So that **I can establish complete clinical context and causation for accurate adjudication and payment determination**


**Key Capabilities:**

> 1. User is able to document treatment setting and specify treatment causation
>     1.1 Upon selecting accident-related causation, system enables capture of accident date and jurisdiction
> 2. User is able to record pre-existing missing teeth using anatomical tooth maps
>     2.1 System provides primary dentition map for pediatric patients
>     2.2 System provides secondary dentition map for adult patients
> 3. User is able to add clinical remarks and special handling instructions
> 4. System persists all supplemental information to the claim record for downstream adjudication processes


**Acceptance Criteria:**

> 1. **Given** adjuster is documenting a dental claim, **When** treatment causation involves an accident, **Then** system captures accident date and state/province
> 2. **Given** prosthetic or restorative services are claimed, **When** adjuster records missing teeth, **Then** system associates anatomically correct tooth identifiers to the claim
> 3. **Given** adjuster uses primary tooth map, **When** teeth are selected, **Then** system records alphanumeric designations (A-T)
> 4. **Given** adjuster uses secondary tooth map, **When** teeth are selected, **Then** system records numeric designations (1-32)
> 5. **Given** all supplemental data is captured, **When** adjuster saves the information, **Then** system makes data available for adjudication rules and benefit calculations


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=769149532"
> ]

---

#### Feature: As a Claims Adjuster, I want to add and manage fees and concessions associated with the claim, so that I can accurately track all financial adjustments
- **Role**: Claim Adjuster
- **Action**: add and manage fees and concessions associated with dental claims
- **Value**: I can accurately track all financial adjustments and ensure proper settlement processing

**Description:**

> As a **Claim Adjuster**,
> I want to **add and manage fees and concessions associated with dental claims**,
> So that **I can accurately track all financial adjustments and ensure proper settlement processing**


**Key Capabilities:**

> 1. User is able to initiate fee capture process within the claim intake workflow
> 2. User is able to define fee details including fee classification and monetary amount for each financial adjustment
> 3. Upon submission of fee information, system automatically creates and adjudicates settlement records
> 4. System applies payment scheduling rules to determine appropriate payment timing and sequence
> 5. System automatically generates and issues payment transactions based on adjudicated settlements
> 6. User is able to review captured fees and associated payment outcomes within the claim financial summary


**Acceptance Criteria:**

> 1. **Given** user has appropriate privileges, **When** initiating fee capture, **Then** system provides interface to add new fee entries
> 2. **Given** fee details are entered, **When** user submits the claim, **Then** system automatically creates settlement records without manual intervention
> 3. **Given** settlement is created, **When** business rules are applied, **Then** system schedules payments according to configured payment scheduling rules
> 4. **Given** payment is scheduled, **When** processing conditions are met, **Then** system automatically issues payment
> 5. **Given** incomplete fee information, **When** user attempts submission, **Then** system prevents progression until required financial data is provided
> 6. **Given** fees are successfully captured, **When** reviewing claim financials, **Then** all fee adjustments and resulting payments are traceable


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=809868562"
> ]

---

#### Feature: As a Claims Adjuster, I want to upload supporting documents during the claim intake process, so that I can attach necessary documentation to the claim
- **Role**: Claim Adjuster
- **Action**: attach supporting documentation during dental claim intake
- **Value**: the claim record includes all necessary evidence for accurate adjudication and compliance

**Description:**

> As a **Claim Adjuster**,
> I want to **attach supporting documentation during dental claim intake**,
> So that **the claim record includes all necessary evidence for accurate adjudication and compliance**.


**Key Capabilities:**

> 1. User initiates document attachment during claim intake workflow
> 2. User submits documents through available intake channels
>     2.1 Upon validation failure, system rejects non-compliant files with error notification
>     2.2 User is able to remove rejected files and resubmit compliant documents
> 3. System validates document integrity and format compliance
> 4. System stores approved documents in designated claim repository
> 5. User progresses to subsequent intake stages or completes submission
> 6. System makes attached documents accessible for claim review and adjudication activities


**Acceptance Criteria:**

> 1. **Given** the adjuster is in the document attachment stage, **When** compliant documents are submitted, **Then** system accepts and stores files in the intake repository
> 2. **Given** documents fail format or size validation, **When** submission occurs, **Then** system prevents storage and notifies user of non-compliance
> 3. **Given** no documents are attached, **When** user proceeds, **Then** system allows intake continuation without mandatory documentation
> 4. **Given** claim submission is complete, **When** accessing the claim record, **Then** all attached documents are retrievable from the intake repository
> 5. **Given** documents are successfully uploaded, **When** claim processing initiates, **Then** intake completion task is created for workflow tracking


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=783159944"
> ]

---

#### Feature: As a Claims Adjuster, I want to review all captured claim information across policy, patient, provider, services, and additional details before submission, so that I can verify accuracy and completeness
- **Role**: Claim Adjuster
- **Action**: review and validate all captured claim information across policy, patient, provider, services, and supporting documentation before final submission
- **Value**: I can ensure data accuracy, completeness, and regulatory compliance, reducing downstream claim processing errors and potential payment delays

**Description:**

> As a **Claim Adjuster**,
> I want to **review and validate all captured claim information across policy, patient, provider, services, and supporting documentation before final submission**,
> So that **I can ensure data accuracy, completeness, and regulatory compliance, reducing downstream claim processing errors and potential payment delays**.


**Key Capabilities:**

> 1. User accesses comprehensive review interface displaying aggregated claim information from all prior intake stages (policy selection, patient demographics, provider details, service line items, missing teeth indicators, uploaded documentation).
> 2. System presents consolidated view enabling verification of data consistency and completeness across all claim components.
> 3. User initiates claim submission triggering automated validation against dental loss business rules.
> 4. Upon validation success, system confirms submission and transitions claim to adjudication workflow.
>     4.1 If validation fails, system prevents submission and surfaces business rule violations for remediation.
> 5. User can navigate backward to previous intake steps to modify information before resubmitting.


**Acceptance Criteria:**

> 1. **Given** all mandatory intake steps are completed, **When** user accesses review screen, **Then** system displays consolidated claim information spanning policy, patient, provider, services, and attachments.
> 2. **Given** user initiates submission, **When** claim data is incomplete or violates dental validation rules, **Then** system blocks submission and identifies specific deficiencies.
> 3. **Given** claim passes all validation checks, **When** submission is confirmed, **Then** system persists claim record and initiates adjudication process.
> 4. **Given** user identifies errors during review, **When** navigating to prior steps, **Then** system preserves existing data and allows targeted corrections.
> 5. **Given** validation rules are applied, **When** claim contains missing teeth indicators, **Then** system verifies consistency with service codes and policy provisions.


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=784765806"
> ]

---

#### Feature: As a Claims Adjuster, I want to navigate through the four-step claim intake process using step indicators and buttons, so that I can move forward and backward through the workflow efficiently
- **Role**: Claim Adjuster
- **Action**: navigate through a multi-step dental claim intake process with ability to progress forward, return to previous stages, and manage workflow state
- **Value**: I can efficiently guide claim submission through validation checkpoints while maintaining flexibility to review, modify, or suspend work in progress

**Description:**

> As a **Claim Adjuster**,
> I want to **navigate through a multi-step dental claim intake process with ability to progress forward, return to previous stages, and manage workflow state**,
> So that **I can efficiently guide claim submission through validation checkpoints while maintaining flexibility to review, modify, or suspend work in progress**


**Key Capabilities:**

> 1. User initiates claim intake by selecting policy and patient information
>     1.1 Upon selection completion, system enables claim initialization
> 2. User provides claim details subject to business validation rules before advancement
>     2.1 When validation fails, user corrects information without losing context
> 3. User attaches supporting documentation as evidence
> 4. User reviews aggregated claim data and submits for adjudication
>     4.1 Upon submission, system locates policy version and creates claim record
> 5. User is able to save incomplete work and resume later at any stage
> 6. User is able to withdraw or cancel claim with appropriate closure reasons


**Acceptance Criteria:**

> 1. **Given** policy and patient are selected, **When** user initiates claim, **Then** system enables navigation and draft persistence capabilities
> 2. **Given** user is on claim details stage, **When** advancing without satisfying validation, **Then** system prevents progression and highlights deficiencies
> 3. **Given** user navigates backward, **When** returning to previous stage, **Then** system preserves entered data through draft mechanism
> 4. **Given** user completes review stage, **When** submitting claim, **Then** system validates completeness, locates policy version, and creates claim record
> 5. **Given** user saves and exits, **When** reopening draft, **Then** system restores workflow to last completed stage
> 6. **Given** user withdraws or cancels, **When** confirming action, **Then** system closes claim with appropriate business reason without creating claim record


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=778308726"
> ]

---

#### Feature: As a Claims Adjuster, I want to save my work in progress and exit the claim intake form, so that I can resume the claim later without losing data
- **Role**: Claim Adjuster
- **Action**: save in-progress work during claim intake and exit without completing submission
- **Value**: I can resume claim processing later without data loss and manage workload efficiently

**Description:**

> As a **Claim Adjuster**,
> I want to **save in-progress work during claim intake and exit without completing submission**,
> So that **I can resume claim processing later without data loss and manage workload efficiently**


**Key Capabilities:**

> 1. User initiates dental claim intake by selecting policy and patient information
> 2. Upon claim initialization, system enables progress preservation capability
> 3. User provides claim details across multiple intake stages (claim information, document uploads, review)
> 4. User is able to save work-in-progress at any stage after claim initiation without enforcing validation rules
>     4.1 System persists all entered data regardless of completeness
>     4.2 System confirms data preservation and closes intake workspace
> 5. User is able to retrieve saved claim draft and resume from last saved state
> 6. User completes remaining intake stages and submits claim for adjudication


**Acceptance Criteria:**

> 1. **Given** claim intake is initiated, **When** user invokes save-and-exit function, **Then** system persists all entered data without validation enforcement
> 2. **Given** incomplete claim data exists, **When** user saves and exits, **Then** system does not reject submission due to missing required information
> 3. **Given** user saves work in progress, **When** user re-accesses the claim, **Then** system restores exact state from last save point
> 4. **Given** claim is in draft status, **When** user attempts final submission, **Then** system enforces full validation rules
> 5. **Given** user initiates but has not yet saved claim, **When** save function is invoked, **Then** system prevents save operation until claim initialization completes


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=778308726"
> ]

---

#### Feature: As a Claims Adjuster, I want to withdraw or close an incomplete claim intake, so that I can abandon the claim creation process when necessary
- **Role**: Claim Adjuster
- **Action**: withdraw or close an incomplete dental claim intake process
- **Value**: I can efficiently abandon claim creation when business circumstances change or information is unavailable, preventing incomplete or erroneous claims from entering the system

**Description:**

> As a **Claim Adjuster**,
> I want to **withdraw or close an incomplete dental claim intake process**,
> So that **I can efficiently abandon claim creation when business circumstances change or information is unavailable, preventing incomplete or erroneous claims from entering the system**


**Key Capabilities:**

> 1. User initiates dental claim intake by selecting policy and patient, triggering claim creation
> 2. Upon claim initiation, user is able to withdraw the claim at any workflow stage, marking it as 'Abandoned'
>     2.1 System prompts confirmation before executing withdrawal
>     2.2 System terminates intake process and exits workflow
> 3. Alternatively, user is able to close the claim, marking it as 'Canceled' with similar confirmation flow
> 4. System prevents accidental abandonment through mandatory confirmation dialogs for both withdrawal and closure actions
> 5. Upon confirmation, system formally closes claim with appropriate reason code and exits intake interface


**Acceptance Criteria:**

> 1. **Given** claim intake is initiated past policy selection, **When** user chooses to withdraw, **Then** system prompts confirmation and closes claim with 'Abandoned' reason upon approval
> 2. **Given** claim intake is in progress, **When** user chooses to close, **Then** system prompts confirmation and closes claim with 'Canceled' reason upon approval
> 3. **Given** user declines withdrawal or closure confirmation, **When** responding to system prompt, **Then** system returns user to current intake step without data loss
> 4. **Given** claim is withdrawn or closed, **When** process completes, **Then** system exits intake interface and prevents further modifications
> 5. **Given** withdrawal or closure is requested, **When** system prompts confirmation, **Then** system clearly communicates data loss implications before proceeding


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=778308726"
> ]

---

#### Feature: As a Claims Adjuster, I want to submit the completed dental claim and receive confirmation of successful submission, so that the claim enters the adjudication workflow
- **Role**: Claim Adjuster
- **Action**: Complete and submit dental claim intake through a multi-stage workflow to initiate adjudication
- **Value**: The claim enters the adjudication workflow with validated data, enabling timely processing and payment decisions

**Description:**

> As a **Claim Adjuster**,
> I want to **complete and submit dental claim intake through a multi-stage workflow to initiate adjudication**,
> So that **the claim enters the adjudication workflow with validated data, enabling timely processing and payment decisions**.


**Key Capabilities:**

> 1. User initiates claim creation by selecting policy and patient from existing customer records
> 2. System generates claim with initial incomplete status and unique identifier upon data capture
> 3. User progresses through staged intake process: claim information, service details, additional data, and document uploads
>     3.1 Upon data validation issues, user can save partial progress and exit
>     3.2 User may close claim with specific reason before submission
> 4. User reviews consolidated claim information before final submission
> 5. System submits claim and transitions status to Open or Pending based on auto-adjudication outcomes
> 6. User receives submission confirmation and accesses newly created claim overview


**Acceptance Criteria:**

> 1. **Given** policy and patient are selected, **When** user initiates creation, **Then** system generates claim with unique number and Incomplete status
> 2. **Given** claim data is entered across stages, **When** user navigates between stages, **Then** system persists data incrementally
> 3. **Given** user chooses save and exit, **When** data is incomplete, **Then** system saves partial data without validation enforcement
> 4. **Given** all required information is provided, **When** user submits claim, **Then** system validates data and transitions status to Open or Pending
> 5. **Given** submission fails validation, **When** submission is attempted, **Then** system retains Incomplete status and displays failure notification
> 6. **Given** submission succeeds, **When** user confirms, **Then** system provides access to claim overview for adjudication workflow


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=776641258"
> ]

---
## Initiative: Coverage Evaluation & Adjudication

### Epic: Accident Claim Adjudication

#### Feature: As a Claims Adjuster, I want to automatically transition cases through their lifecycle states (Initialization → Open → Closed), so that manual state management is eliminated and cases progress efficiently.
- **Role**: Claim Adjuster
- **Action**: automatically transition accident cases through their complete lifecycle from initialization to closure without manual state intervention
- **Value**: manual processing overhead is eliminated, operational efficiency improves, and cases progress seamlessly through evaluation and settlement stages

**Description:**

> As a **Claim Adjuster**,
> I want to **automatically transition accident cases through their complete lifecycle from initialization to closure without manual state intervention**,
> So that **manual processing overhead is eliminated, operational efficiency improves, and cases progress seamlessly through evaluation and settlement stages**.


**Key Capabilities:**

> 1. System initializes case event and automatically transitions to Open state upon loss information capture
> 2. System creates damage loss entity, validates policy applicability, and transitions to Open when eligibility confirms
>     2.1 Upon pending applicability result, system pauses progression until resolution
> 3. System creates or retrieves claim, performs adjudication with coverage selection and calculation, then transitions to approved settlement
>     3.1 When adjudication disapproves, system halts and enables readjudication capability
> 4. System automatically approves settlement and closes when conditions satisfy
> 5. System automatically closes parent case when all associated claims reach closure
> 6. System enforces product-specific state machine rules governing available transitions and actions at each lifecycle stage


**Acceptance Criteria:**

> 1. **Given** loss applicability confirms positive, **When** case initializes, **Then** system transitions case to Open and loss to Open without manual intervention
> 2. **Given** claim adjudication completes successfully, **When** coverage evaluation and calculation finish, **Then** system approves claim and proceeds to settlement creation
> 3. **Given** claim adjudication returns disapproved, **When** approval fails, **Then** system halts progression and enables readjudication workflow
> 4. **Given** settlement conditions satisfy, **When** automatic approval processes, **Then** system transitions settlement to Approved and Closed states
> 5. **Given** all claims under case reach closed status, **When** final claim closes, **Then** system automatically closes parent case
> 6. **Given** loss applicability remains pending, **When** evaluation incomplete, **Then** system prevents downstream claim creation until resolution


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=826868745"
> ]

---

#### Feature: As a Claims Adjuster, I want to automatically transition losses through their lifecycle states (Initialization → Open → Closed), so that loss processing is streamlined without manual intervention.
- **Role**: Claim Adjuster
- **Action**: automatically transition losses and associated claims through their lifecycle states from initialization to closure
- **Value**: loss processing is streamlined without manual intervention, reducing processing time and operational overhead

**Description:**

> As a **Claim Adjuster**,
> I want to **automatically transition losses and associated claims through their lifecycle states from initialization to closure**,
> So that **loss processing is streamlined without manual intervention, reducing processing time and operational overhead**.


**Key Capabilities:**

> 1. Upon case creation, system initializes case lifecycle and transitions to Open status when loss is applicable.
> 2. System evaluates loss applicability by retrieving policy information and automatically opens qualifying losses.
> 3. When loss is opened, system creates associated claim(s) and transitions to Pending status for adjudication.
> 4. System performs eligibility validation and coverage calculation, transitioning approved claims to settlement processing.
> 5. Upon settlement approval, system closes settlement and evaluates case closure conditions.
>     5.1 If adjudication outcome is Disapproved, claim is rejected and closure evaluation triggers.
>     5.2 Readjudication option allows reprocessing when corrections are needed.
> 6. When all claims reach closed status, system automatically closes parent case per business rules.


**Acceptance Criteria:**

> 1. **Given** a new case is created, **When** loss applicability check passes, **Then** system transitions case and loss to Open status without manual action.
> 2. **Given** loss is opened, **When** policy coverage is valid, **Then** system creates claim(s) and transitions to Pending status automatically.
> 3. **Given** claim is adjudicated, **When** eligibility and calculation approve coverage, **Then** system advances to settlement processing.
> 4. **Given** settlement is approved, **When** closure conditions are met, **Then** system closes settlement and evaluates case closure.
> 5. **Given** loss applicability fails, **When** validation returns negative result, **Then** system prevents loss submission and halts progression.
> 6. **Given** all claims are closed, **When** case closure rule executes, **Then** system automatically closes parent case.


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=826868745"
> ]

---

#### Feature: As a Claims Adjuster, I want to automatically transition claims through their lifecycle states (Initialization → Open → Adjudicated), so that claim processing is expedited without manual state changes.
- **Role**: Claim Adjuster
- **Action**: automatically progress claims through lifecycle states from initialization to settlement without manual intervention
- **Value**: claim processing efficiency is maximized, manual workload is reduced, and settlement turnaround times are accelerated

**Description:**

> As a **Claim Adjuster**,
> I want to **automatically progress claims through lifecycle states from initialization to settlement without manual intervention**,
> So that **claim processing efficiency is maximized, manual workload is reduced, and settlement turnaround times are accelerated**


**Key Capabilities:**

> 1. System automatically initiates case and transitions to open status upon event receipt
> 2. System processes loss information, retrieves policy data, evaluates applicability, and progresses eligible losses to claim creation
>     2.1 When loss is not applicable, system maintains pending status until resolution
> 3. System creates or identifies existing claims and advances through adjudication workflow stages
> 4. System performs coverage evaluation, eligibility verification, and settlement calculation without manual triggers
> 5. System approves or disapproves settlements based on adjudication results and closes approved settlements
>     5.1 User is able to initiate readjudication when results require review
> 6. System automatically closes case when all associated claims reach closure


**Acceptance Criteria:**

> 1. **Given** a case event is received, **When** initialization completes, **Then** system transitions case to open status without manual action
> 2. **Given** loss data is processed and policy retrieved, **When** loss applicability is confirmed, **Then** system creates claim and advances to open status
> 3. **Given** loss applicability check fails, **When** evaluation completes, **Then** system retains loss in pending status until conditions are met
> 4. **Given** claim is submitted, **When** adjudication executes, **Then** system progresses through pending, adjudicating, eligibility, and calculation states sequentially
> 5. **Given** adjudication completes with approval, **When** settlement processes, **Then** system advances to approved and closed status
> 6. **Given** all claims are closed, **When** closure condition is met, **Then** system automatically closes parent case


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=826868745"
> ]

---

#### Feature: As a Claims Adjuster, I want to automatically calculate settlement amounts and transition settlements to approval status based on loss and policy information, so that settlement decisions are made consistently and quickly.
- **Role**: Claim Adjuster
- **Action**: automatically calculate settlement amounts and transition settlements to approval status based on loss and policy information
- **Value**: settlement decisions are made consistently and quickly without manual intervention

**Description:**

> As a **Claim Adjuster**,
> I want to **automatically calculate settlement amounts and transition settlements to approval status based on loss and policy information**,
> So that **settlement decisions are made consistently and quickly without manual intervention**.


**Key Capabilities:**

> 1. System evaluates loss applicability upon damage loss submission and progresses eligible losses to claim creation.
> 2. System automatically adjudicates claims by selecting applicable coverage and transitioning through eligibility and calculation stages.
> 3. System calculates settlement amounts based on captured loss and policy information without manual intervention.
> 4. System evaluates settlement decision and transitions approved settlements to closed status.
>     4.1 When settlement is disapproved, system enables readjudication option for re-evaluation.
> 5. System automatically closes case when all associated claims reach closed status.


**Acceptance Criteria:**

> 1. **Given** a damage loss is submitted, **When** applicability evaluation returns positive, **Then** system creates claim and progresses to adjudication.
> 2. **Given** claim enters adjudication, **When** coverage is selected, **Then** system calculates settlement based on loss and policy data.
> 3. **Given** settlement calculation completes, **When** decision criteria are met, **Then** system transitions settlement to approved status.
> 4. **Given** settlement is disapproved, **When** adjuster initiates readjudication, **Then** system re-evaluates settlement eligibility.
> 5. **Given** all claims are closed, **When** final claim reaches closed status, **Then** system automatically closes the case.
> 6. **Given** incomplete loss data, **When** applicability evaluation fails, **Then** system prevents claim creation and retains loss in incomplete state.


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=826868745"
> ]

---

#### Feature: As a System Administrator, I want to configure state machine actions and statuses for each product, so that the auto-adjudication workflow behaves according to product-specific business rules.
- **Role**: Claim Manager
- **Action**: configure state machine actions and statuses for each insurance product to enable automated adjudication workflows that comply with product-specific business rules
- **Value**: the auto-adjudication system automatically processes claims through their complete lifecycle—from case initialization to settlement closure—according to predefined business rules, reducing manual intervention and ensuring consistent claim handling

**Description:**

> As a **Claim Manager**,
> I want to **configure state machine actions and statuses for each insurance product to enable automated adjudication workflows that comply with product-specific business rules**,
> So that **the auto-adjudication system automatically processes claims through their complete lifecycle—from case initialization to settlement closure—according to predefined business rules, reducing manual intervention and ensuring consistent claim handling**.


**Key Capabilities:**

> 1. Configure product-specific state machine definitions with available commands and allowed states for case, loss, claim, and settlement lifecycles
> 2. Define state transition rules where case automatically progresses from Incomplete to Open upon claim submission, and to Closed when all claims are resolved
> 3. Establish loss applicability validation logic that determines whether loss transitions to Open or remains Pending based on policy coverage evaluation
> 4. Configure claim adjudication workflow stages from Pending through Open to Adjudicating states with coverage selection and eligibility verification
> 5. Define settlement approval pathways where approved settlements automatically close, while disapproved settlements return to Pending for readjudication
> 6. Associate available actions with each state to control permitted operations and enforce business rule compliance throughout the lifecycle


**Acceptance Criteria:**

> 1. **Given** product-specific configuration is defined, **When** case is created, **Then** system automatically initializes case in Incomplete state and transitions to Open upon claim submission
> 2. **Given** loss applicability check is performed, **When** result is Yes, **Then** loss transitions to Open state; **When** result is No, **Then** loss remains in Pending state
> 3. **Given** claim adjudication is completed, **When** approved, **Then** settlement enters Approved state and transitions to Closed; **When** disapproved, **Then** settlement enters Disapproved then Pending for readjudication
> 4. **Given** all claims under a case are closed, **When** final claim closure occurs, **Then** case automatically transitions to Closed state without manual intervention
> 5. **Given** state machine configuration defines available commands, **When** lifecycle action is requested, **Then** system validates command availability for current state before execution
> 6. **Given** product-specific business rules are configured, **When** automated workflow executes, **Then** system enforces configured state transitions and action permissions throughout entire lifecycle


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=826868745"
> ]

---

#### Feature: As a Claims Operations Manager, I want cases to automatically close when all related claims are closed, so that case closure is enforced consistently without manual oversight.
- **Role**: Claim Manager
- **Action**: enable automated case closure when all associated claims reach closed status
- **Value**: case lifecycle management is consistent and scalable without requiring manual oversight or intervention

**Description:**

> As a **Claim Manager**,
> I want to **enable automated case closure when all associated claims reach closed status**,
> So that **case lifecycle management is consistent and scalable without requiring manual oversight or intervention**


**Key Capabilities:**

> 1. System monitors real-time status of all claims associated with a case event
> 2. Upon detection that all related claims have transitioned to closed status, system triggers automated case closure evaluation
> 3. System validates case closure eligibility based on configured business rules and state machine logic
> 4. System executes automated case lifecycle transition from open to closed status
>     4.1 If eligibility criteria are not met, system retains case in current state
> 5. System records closure timestamp and rationale for audit trail purposes
> 6. System notifies relevant stakeholders of automated case closure completion


**Acceptance Criteria:**

> 1. **Given** all claims under a case are closed, **When** the final claim closure is processed, **Then** the system automatically transitions the case to closed status without manual action
> 2. **Given** at least one claim remains open, **When** other claims are closed, **Then** the system prevents case closure and maintains current case status
> 3. **Given** case closure is triggered, **When** validation rules are satisfied, **Then** system records closure metadata including timestamp and triggering event
> 4. **Given** automated closure fails validation, **When** the system detects rule violations, **Then** case remains in current state and generates exception notification
> 5. **Given** case closure completes successfully, **When** lifecycle transition executes, **Then** system publishes closure event to downstream systems and stakeholders


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=826868745"
> ]

---

#### Feature: As a Claims Adjuster, I want to perform adjudication actions (Approve, Disapprove, Readjudicate) on claims based on eligibility and coverage calculations, so that claim decisions are made with proper evaluation of policy terms.
- **Role**: Claim Adjuster
- **Action**: execute adjudication actions on claims by evaluating eligibility, coverage terms, and settlement calculations
- **Value**: claim decisions are made accurately with proper policy evaluation and automated lifecycle transitions

**Description:**

> As a **Claim Adjuster**,
> I want to **execute adjudication actions on claims by evaluating eligibility, coverage terms, and settlement calculations**,
> So that **claim decisions are made accurately with proper policy evaluation and automated lifecycle transitions**


**Key Capabilities:**

> 1. Initiate claim adjudication process upon claim reaching adjudicating state
> 2. Select applicable coverage and execute eligibility verification against policy terms
> 3. Calculate settlement amount based on loss information and coverage limits
> 4. Approve claim when eligibility and calculations satisfy policy requirements, transitioning to settlement processing
> 5. Disapprove claim when eligibility or coverage conditions are not met, terminating claim process
> 6. Readjudicate claim to re-execute coverage selection and eligibility calculations upon settlement exceptions


**Acceptance Criteria:**

> 1. **Given** claim is in adjudicating state, **When** adjudicator executes eligibility and calculation, **Then** system determines approval or disapproval based on policy terms
> 2. **Given** adjudication result is approved, **When** process completes, **Then** system transitions claim to settlement processing state
> 3. **Given** adjudication result is disapproved, **When** decision is finalized, **Then** system terminates claim process without settlement creation
> 4. **Given** settlement requires readjudication, **When** exception is triggered, **Then** system returns claim to adjudication process for re-evaluation
> 5. **Given** all claims reach closed state, **When** case termination rule executes, **Then** system automatically closes parent case
> 6. **Given** settlement is approved, **When** final validation completes, **Then** system transitions settlement to closed state


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=826868745"
> ]

---

### Epic: Hospital Indemnity Claim Adjudication

#### Feature: As a Claims Adjuster, I want to initiate and automatically progress a Hospital Indemnity claim through case, loss, and claim creation states, so that claims are processed efficiently without manual state transitions.
- **Role**: Claim Adjuster
- **Action**: initiate and automatically progress a Hospital Indemnity claim through case, loss, and claim lifecycle states with automated settlement determination
- **Value**: claims are processed efficiently without manual state transitions, reducing processing time and ensuring consistent eligibility evaluation

**Description:**

> As a **Claim Adjuster**,
> I want to **initiate and automatically progress a Hospital Indemnity claim through case, loss, and claim lifecycle states with automated settlement determination**,
> So that **claims are processed efficiently without manual state transitions, reducing processing time and ensuring consistent eligibility evaluation**.


**Key Capabilities:**

> 1. System automatically transitions case from initialization to open state upon policy information capture
> 2. System evaluates loss applicability against policy coverage and automatically opens loss when applicable
> 3. System creates and opens claim automatically based on loss determination without manual entry
> 4. System adjudicates claim by applying eligibility rules and calculating settlement amounts
> 5. System automatically approves or disapproves settlement based on eligibility evaluation and transitions to closed state
>     5.1 When disapproved, system closes case without settlement approval
>     5.2 User is able to trigger re-adjudication for reassessment when business conditions warrant review


**Acceptance Criteria:**

> 1. **Given** valid policy information is captured, **When** case is initialized, **Then** system automatically transitions case to open state
> 2. **Given** case is open, **When** loss applicability evaluation succeeds, **Then** system automatically opens loss and creates associated claim
> 3. **Given** claim is created, **When** system adjudicates, **Then** eligibility rules are applied and settlement amount is calculated
> 4. **Given** eligibility evaluation is complete, **When** criteria are met, **Then** system automatically approves settlement and closes case
> 5. **Given** eligibility evaluation fails, **When** adjudication completes, **Then** system disapproves settlement and closes case
> 6. **Given** claim is closed, **When** re-adjudication is triggered, **Then** system re-evaluates claim through complete adjudication process


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=541994924"
> ]

---

#### Feature: As a Claims Adjuster, I want to adjudicate a Hospital Indemnity claim by validating request data and verifying the claim can transition from its current status, so that only valid adjudication requests are processed.
- **Role**: Claim Adjuster
- **Action**: adjudicate a Hospital Indemnity claim by validating eligibility and transitioning claim status to initiate settlement
- **Value**: only valid claims progress through adjudication, ensuring compliance with policy coverage and lifecycle rules while expediting settlement processing

**Description:**

> As a **Claim Adjuster**,
> I want to **adjudicate a Hospital Indemnity claim by validating eligibility and transitioning claim status to initiate settlement**,
> So that **only valid claims progress through adjudication, ensuring compliance with policy coverage and lifecycle rules while expediting settlement processing**


**Key Capabilities:**

> 1. System validates adjudication request against authorization and data completeness requirements
> 2. System verifies claim status permits adjudication command per lifecycle configuration
>     2.1 Upon validation failure, system rejects request with appropriate error notification
> 3. System transitions claim status to Open upon successful validation
> 4. System retrieves policy header and coverage data for applicable policy version
> 5. System initiates settlement creation process with required policy and claim data
> 6. System completes business activity tracking and returns updated claim image to adjuster


**Acceptance Criteria:**

> 1. **Given** a claim in eligible status, **When** adjuster submits adjudication request with valid credentials, **Then** system transitions claim to Open and initiates settlement creation
> 2. **Given** a claim in ineligible status, **When** adjudication is attempted, **Then** system prevents processing and returns status incompatibility error
> 3. **Given** incomplete or unauthorized request, **When** validation executes, **Then** system rejects adjudication without status change
> 4. **Given** successful adjudication, **When** process completes, **Then** system returns claim image with updated status and policy data
> 5. **Given** settlement creation initiation, **When** policy data retrieval occurs, **Then** system stores accurate coverage information for applicable policy version


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=541994998"
> ]

---

#### Feature: As a Claims Adjuster, I want to retrieve and apply applicable policy header and coverage data during claim adjudication, so that settlement calculations are based on the correct policy terms.
- **Role**: Claim Adjuster
- **Action**: retrieve and apply applicable policy header and coverage data during claim adjudication to ensure accurate settlement calculations
- **Value**: settlement determinations are based on verified policy terms, reducing financial errors and ensuring contractual compliance

**Description:**

> As a **Claim Adjuster**,
> I want to **retrieve and apply applicable policy header and coverage data during claim adjudication to ensure accurate settlement calculations**,
> So that **settlement determinations are based on verified policy terms, reducing financial errors and ensuring contractual compliance**.


**Key Capabilities:**

> 1. User initiates claim adjudication with appropriate system privileges and claim identification
> 2. System validates the adjudication request and confirms lifecycle transition eligibility from current claim status
> 3. Upon validation success, system transitions claim to Open status
> 4. System retrieves policy header and coverage data from the applicable policy version
>     4.1 Policy header attributes are extracted and stored
>     4.2 Coverage-specific terms and limits are captured
> 5. System initiates settlement creation service using retrieved policy data
> 6. System completes adjudication and returns updated claim image to user


**Acceptance Criteria:**

> 1. **Given** a valid claim identification and adjudication request, **When** user possesses required privileges, **Then** system validates request and proceeds with adjudication workflow
> 2. **Given** claim status permits adjudication, **When** lifecycle validation completes, **Then** system transitions claim to Open status
> 3. **Given** claim is transitioned to Open, **When** settlement creation initiates, **Then** system retrieves and stores policy header and coverage data from correct policy version
> 4. **Given** incomplete or invalid lifecycle transition, **When** validation fails, **Then** system prevents adjudication and returns appropriate error notification
> 5. **Given** policy data retrieval completes, **When** settlement service executes, **Then** calculations reflect retrieved policy terms
> 6. **Given** adjudication completes successfully, **When** process finalizes, **Then** system returns updated claim image with persisted policy data references


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=541994998"
> ]

---

#### Feature: As a Claims Adjuster, I want to receive an error notification when attempting to adjudicate a claim from an invalid status, so that I understand why the action cannot be performed and can take corrective action.
- **Role**: Claim Adjuster
- **Action**: receive clear error notifications when attempting to adjudicate claims from invalid statuses
- **Value**: I understand adjudication constraints and can take appropriate corrective actions without processing delays

**Description:**

> As a **Claim Adjuster**,
> I want to **receive clear error notifications when attempting to adjudicate claims from invalid statuses**,
> So that **I understand adjudication constraints and can take appropriate corrective actions without processing delays**.


**Key Capabilities:**

> 1. User initiates adjudication process for a hospital indemnity claim
> 2. System validates request data and verifies user privileges
> 3. System evaluates current claim status against configured lifecycle rules to determine adjudication eligibility
> 4. Upon detecting invalid status transition, system halts adjudication workflow
> 5. System generates descriptive error notification explaining why adjudication cannot proceed from current state
> 6. User reviews error details and determines appropriate corrective action based on claim status requirements


**Acceptance Criteria:**

> 1. **Given** a claim in non-adjudicable status, **When** adjuster attempts adjudication, **Then** system prevents status transition and returns error notification
> 2. **Given** error notification received, **When** adjuster reviews message, **Then** system clearly identifies the invalid status constraint
> 3. **Given** valid claim status, **When** adjudication initiated, **Then** system proceeds with status update and settlement initiation
> 4. **Given** adjudication blocked, **When** error occurs, **Then** claim remains in original status without partial updates
> 5. **Given** lifecycle rule violation, **When** system detects it, **Then** process exits without triggering settlement or business activity modules


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=541994998"
> ]

---

#### Feature: As a Claims Adjuster, I want to view the updated claim image after adjudication is completed, so that I can verify the claim status and settlement details.
- **Role**: Claim Adjuster
- **Action**: adjudicate hospital indemnity claims and verify the resulting claim status with settlement details
- **Value**: I can ensure accurate claim processing, validate proper status transitions, and confirm settlement calculations are correctly applied before finalizing the claim decision

**Description:**

> As a **Claim Adjuster**,
> I want to **adjudicate hospital indemnity claims and verify the resulting claim status with settlement details**,
> So that **I can ensure accurate claim processing, validate proper status transitions, and confirm settlement calculations are correctly applied before finalizing the claim decision**


**Key Capabilities:**

> 1. User initiates claim adjudication by submitting claim identification for processing
> 2. System validates request authorization and verifies lifecycle status transition eligibility
>     2.1 If status transition is invalid, system prevents adjudication and notifies user
> 3. Upon validation success, system transitions claim to Open status
> 4. System automatically retrieves applicable policy header and coverage data, then generates settlement calculations
> 5. System executes adjudication business rules and finalizes loss determination
> 6. User is able to review updated claim image containing status and settlement details


**Acceptance Criteria:**

> 1. **Given** valid adjudication request with proper privileges, **When** claim status allows transition, **Then** system updates claim to Open status and creates settlement
> 2. **Given** claim in non-adjudicable status, **When** adjudication is attempted, **Then** system prevents execution and returns status error notification
> 3. **Given** successful adjudication, **When** process completes, **Then** system returns complete claim image with updated status and settlement details
> 4. **Given** adjudication initiation, **When** settlement is created, **Then** system retrieves and stores policy header and applicable coverage version data
> 5. **Given** completed adjudication, **When** user reviews claim, **Then** all settlement calculations and status updates are visible in claim image


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=541994998"
> ]

---

#### Feature: As a System Administrator, I want to configure state machine actions and statuses for Hospital Indemnity claims, so that the available claim lifecycle transitions and commands are controlled per product requirements.
- **Role**: Claim Manager
- **Action**: configure state machine actions and lifecycle transitions for Hospital Indemnity claims to enforce product-specific business rules and automated adjudication workflows
- **Value**: claim processing follows standardized lifecycle stages with controlled transitions, enabling automated adjudication from case creation through settlement approval while maintaining compliance with product requirements

**Description:**

> As a **Claim Manager**,
> I want to **configure state machine actions and lifecycle transitions for Hospital Indemnity claims to enforce product-specific business rules and automated adjudication workflows**,
> So that **claim processing follows standardized lifecycle stages with controlled transitions, enabling automated adjudication from case creation through settlement approval while maintaining compliance with product requirements**.


**Key Capabilities:**

> 1. Configure product-specific state machine with business states and allowable transitions for case, loss, claim, and settlement entities
> 2. System evaluates policy applicability and automatically creates case with transitions from Incomplete to Open status
> 3. System initiates claim lifecycle through initialization, opens pending claims, and progresses to adjudicating status
> 4. System performs automated eligibility verification applying configured business rules and transitions to Approved or Disapproved status
>     4.1 Upon disapproval, system halts progression to settlement
>     4.2 Upon approval, system enables readjudication capability for re-evaluation
> 5. System processes settlement initialization and advances to approval status
> 6. System closes case upon successful settlement completion


**Acceptance Criteria:**

> 1. **Given** state machine is configured for Hospital Indemnity product, **When** policy evaluation determines loss applicability, **Then** system creates case and transitions through defined lifecycle stages automatically
> 2. **Given** claim requires adjudication, **When** eligibility rules are applied, **Then** system transitions claim to Approved status and initiates settlement or transitions to Disapproved status and halts progression
> 3. **Given** approved claim requires re-evaluation, **When** readjudication is initiated, **Then** system recalculates eligibility and settlement amounts per configured rules
> 4. **Given** settlement is approved, **When** all entities complete lifecycle, **Then** system transitions case to Closed status
> 5. **Given** loss applicability is negative, **When** policy processing completes, **Then** system prevents case creation and terminates process


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=541994924"
> ]

---

#### Feature: As a Claims Operations Manager, I want to automatically approve settlements upon completion of eligibility and calculation rules during auto-adjudication, so that approved claims are processed without manual intervention.
- **Role**: Claim Adjuster
- **Action**: automatically approve settlements upon successful eligibility verification and calculation completion during auto-adjudication
- **Value**: approved claims are processed and settled without manual intervention, reducing processing time and operational costs

**Description:**

> As a **Claim Adjuster**,
> I want to **automatically approve settlements upon successful eligibility verification and calculation completion during auto-adjudication**,
> So that **approved claims are processed and settled without manual intervention, reducing processing time and operational costs**


**Key Capabilities:**

> 1. System initiates case and loss processing, automatically transitioning from initialization to open status
> 2. Upon loss applicability validation, system creates claims and progresses them to adjudicating state
> 3. System performs eligibility verification and executes calculation rules against policy and loss information
>     3.1 When eligibility is approved, system proceeds to settlement processing
>     3.2 When eligibility is disapproved, claim transitions to disapproved state without settlement
> 4. Upon eligibility approval, system calculates settlement amount and automatically advances settlement to approved status without manual intervention
> 5. System closes case and claims upon settlement approval completion
> 6. User is able to trigger readjudication for closed cases when reprocessing is required


**Acceptance Criteria:**

> 1. **Given** loss information meets claim creation criteria, **When** case is initiated, **Then** system automatically creates claims and transitions them to adjudicating state
> 2. **Given** claim is in adjudicating state, **When** eligibility verification completes with approved result, **Then** system progresses to settlement calculation without manual intervention
> 3. **Given** eligibility is disapproved, **When** adjudication completes, **Then** system transitions claim to disapproved state and does not create settlement
> 4. **Given** eligibility is approved and calculation completes, **When** settlement amount is determined, **Then** system automatically approves settlement without manual review
> 5. **Given** settlement is approved, **When** processing completes, **Then** system automatically closes case and associated claims
> 6. **Given** case is closed, **When** readjudication is triggered, **Then** system restarts adjudication process from eligibility verification


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=541994924"
> ]

---

### Epic: Leave Claim Adjudication & Settlement

#### Feature: As a Claims Adjuster, I want to initiate a leave claim settlement, so that I can begin the adjudication process for a claimant's leave benefits
- **Role**: Claim Adjuster
- **Action**: initiate a leave claim settlement and trigger automated adjudication
- **Value**: the adjudication process begins promptly with validated policy data and proper authorization controls

**Description:**

> As a **Claim Adjuster**,
> I want to **initiate a leave claim settlement and trigger automated adjudication**,
> So that **the adjudication process begins promptly with validated policy data and proper authorization controls**


**Key Capabilities:**

> 1. System validates adjuster authorization and policy existence before accepting settlement request
> 2. System generates unique settlement identifier using product-specific numbering pattern
> 3. System initializes settlement record with provided claimant and benefit details
> 4. System transitions settlement status from Initialized to Adjudicating
> 5. System triggers automated adjudication workflow to evaluate leave benefit eligibility
> 6. System returns settlement confirmation with unique identifier for subsequent tracking


**Acceptance Criteria:**

> 1. **Given** adjuster has initiation privilege and valid policy number, **When** settlement is requested, **Then** system creates settlement with unique identifier
> 2. **Given** policy number does not exist, **When** settlement is initiated, **Then** system rejects request with policy validation error
> 3. **Given** settlement is successfully initialized, **When** system processes request, **Then** status progresses to Adjudicating automatically
> 4. **Given** adjuster lacks initiation privilege, **When** settlement is attempted, **Then** system denies access based on authorization rules
> 5. **Given** settlement creation succeeds, **When** adjudication is triggered, **Then** system invokes settlement adjudication business activity
> 6. **Given** all validations pass, **When** settlement is saved, **Then** system returns complete settlement image with identification details


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=619721324"
> ]

---

#### Feature: As a Claims Adjuster, I want to adjudicate a leave settlement by running validation rules and calculating benefit amounts, so that I can determine eligibility and payment amounts based on policy coverage and limits
- **Role**: Claim Adjuster
- **Action**: adjudicate leave settlements through automated validation and benefit calculation
- **Value**: eligibility and payment determinations are accurate, compliant with policy terms, and efficiently processed

**Description:**

> As a **Claim Adjuster**,
> I want to **adjudicate leave settlements through automated validation and benefit calculation**,
> So that **eligibility and payment determinations are accurate, compliant with policy terms, and efficiently processed**.


**Key Capabilities:**

> 1. System validates adjudication request against settlement status and lifecycle configuration for the product
> 2. Settlement status transitions to Pending upon successful validation
> 3. System executes adjudication business logic to evaluate eligibility and calculate benefit amounts
> 4. Upon completion, system returns settlement details and policy image for adjuster review
>     4.1 When lifecycle rules prohibit status transition, system prevents adjudication and notifies adjuster
> 5. Adjuster can override eligibility results or calculation attributes when authorized by privilege controls


**Acceptance Criteria:**

> 1. **Given** a valid settlement exists, **When** adjuster initiates adjudication with proper privileges, **Then** system validates request and updates status to Pending
> 2. **Given** settlement status incompatible with lifecycle rules, **When** adjudication attempted, **Then** system prevents action and returns error notification
> 3. **Given** adjudication triggered, **When** business logic executes, **Then** system calculates benefit amounts per policy terms and returns settlement with policy image
> 4. **Given** adjuster has override privileges, **When** overriding eligibility or calculation parameters, **Then** system accepts modifications and completes adjudication
> 5. **Given** adjudication completes, **When** response generated, **Then** settlement and policy snapshot are returned to adjuster


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=619721318"
> ]

---

#### Feature: As a Claims Adjuster, I want to override settlement eligibility results and calculation attributes when necessary, so that I can handle exceptional cases with proper authorization
- **Role**: Claim Adjuster
- **Action**: override settlement eligibility results and calculation attributes during adjudication when exceptional circumstances require deviation from standard automated determinations
- **Value**: I can resolve complex cases that fall outside standard business rules while maintaining proper governance through privilege-based controls and audit trails

**Description:**

> As a **Claim Adjuster**,
> I want to **override settlement eligibility results and calculation attributes during adjudication when exceptional circumstances require deviation from standard automated determinations**,
> So that **I can resolve complex cases that fall outside standard business rules while maintaining proper governance through privilege-based controls and audit trails**


**Key Capabilities:**

> 1. System validates adjuster privileges and settlement lifecycle status before accepting adjudication requests
> 2. Adjuster initiates settlement adjudication providing settlement identification and any override parameters
> 3. Upon eligibility override request, system enforces specific privilege requirement before processing
>     3.1 System validates Override Settlement Eligibility Result privilege when eligibility override code is provided
>     3.2 System validates Override Settlement Calculation Attributes privilege when benefit period or elimination period overrides are specified
> 4. System transitions settlement to Pending status upon successful validation
> 5. System triggers business activity monitoring for adjudication event and returns updated settlement with policy image
> 6. When lifecycle state transition is invalid, system prevents action and returns error notification


**Acceptance Criteria:**

> 1. **Given** adjuster has adjudication privilege **when** initiating settlement adjudication without overrides **then** system processes request and transitions settlement to Pending status
> 2. **Given** adjuster lacks override privilege **when** attempting to override eligibility or calculation attributes **then** system rejects request with authorization error
> 3. **Given** settlement status does not permit adjudication per product configuration **when** adjudication is requested **then** system prevents action and notifies adjuster of invalid state transition
> 4. **Given** valid override privileges exist **when** adjuster provides override parameters **then** system applies overrides and completes adjudication successfully
> 5. **Given** successful adjudication **when** processing completes **then** system returns updated settlement data with policy image and triggers monitoring event
> 6. **Given** incomplete or invalid settlement identification **when** adjudication is requested **then** system prevents processing and returns validation error


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=619721318"
> ]

---

#### Feature: As a Claims Examiner, I want to approve a leave settlement after validating eligibility and reviewing settlement results, so that the claim is authorized for payment
- **Role**: Claim Adjuster
- **Action**: approve a leave settlement after validating eligibility, lifecycle status, and business rule compliance
- **Value**: the claim is authorized for payment with accurate eligibility verification and proper status progression

**Description:**

> As a **Claim Adjuster**,
> I want to **approve a leave settlement after validating eligibility, lifecycle status, and business rule compliance**,
> So that **the claim is authorized for payment with accurate eligibility verification and proper status progression**


**Key Capabilities:**

> 1. System validates request and confirms settlement is linked to a covered loss
> 2. System verifies approve action is permissible from current settlement status per product lifecycle configuration
> 3. System evaluates eligibility business rules and validates settlement result attributes
>     3.1 When critical severity messages exist, system prevents approval and returns validation errors
> 4. Upon successful validation, system transitions settlement status to Approved
> 5. System triggers business activity monitoring event for audit purposes
> 6. System returns updated settlement image to user


**Acceptance Criteria:**

> 1. **Given** a valid settlement with linked loss, **When** user approves settlement, **Then** system validates lifecycle status transition is permitted
> 2. **Given** settlement in valid status, **When** eligibility rules pass without critical messages, **Then** system updates status to Approved
> 3. **Given** critical severity messages in settlement results, **When** user attempts approval, **Then** system prevents approval and returns error details
> 4. **Given** invalid status transition, **When** user attempts approval, **Then** system returns error pch0004 and maintains current status
> 5. **Given** successful approval, **When** process completes, **Then** system triggers monitoring event and returns settlement image
> 6. **Given** user lacks approval privileges, **When** approval is attempted, **Then** system denies action


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=619721319"
> ]

---

#### Feature: As a Claims Examiner, I want to disapprove a leave settlement when it fails validation, so that ineligible claims are rejected and not paid
- **Role**: Claim Adjuster
- **Action**: disapprove a leave settlement that fails validation criteria
- **Value**: ineligible claims are rejected and prevented from payment, ensuring proper claim governance and financial control

**Description:**

> As a **Claim Adjuster**,
> I want to **disapprove a leave settlement that fails validation criteria**,
> So that **ineligible claims are rejected and prevented from payment, ensuring proper claim governance and financial control**


**Key Capabilities:**

> 1. System validates the disapproval request and verifies adjuster privileges
> 2. System evaluates whether settlement can transition to disapproved status based on product lifecycle configuration
> 3. Upon successful validation, system updates settlement status to 'Disapproved'
> 4. System triggers monitoring event for audit and tracking purposes
> 5. System returns updated settlement information confirming the disapproval action
>     5.1 If status transition is invalid, system prevents action and provides appropriate error notification


**Acceptance Criteria:**

> 1. **Given** a settlement exists and adjuster has approval privileges, **When** disapproval is requested, **Then** system validates request and privilege authorization
> 2. **Given** valid disapproval request, **When** current settlement status allows transition, **Then** settlement status updates to 'Disapproved'
> 3. **Given** settlement status prohibits disapproval, **When** action is attempted, **Then** system rejects request and notifies that action cannot be performed from current status
> 4. **Given** settlement is successfully disapproved, **When** process completes, **Then** system triggers business monitoring event and returns settlement confirmation
> 5. **Given** disapproved settlement, **When** stored in system, **Then** payment processing is prevented for that claim


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=619721322"
> ]

---

#### Feature: As a Claims Adjuster, I want to re-adjudicate a settlement after updating claim details, so that I can recalculate benefits based on new or corrected information
- **Role**: Claim Adjuster
- **Action**: re-adjudicate an existing settlement after claim details have been updated or corrected
- **Value**: benefits are recalculated accurately to reflect the current claim information and ensure proper payment amounts

**Description:**

> As a **Claim Adjuster**,
> I want to **re-adjudicate an existing settlement after claim details have been updated or corrected**,
> So that **benefits are recalculated accurately to reflect the current claim information and ensure proper payment amounts**


**Key Capabilities:**

> 1. User initiates re-adjudication for an existing settlement
> 2. System validates authorization and verifies settlement eligibility for re-adjudication based on current status and product lifecycle rules
> 3. System transitions settlement status to adjudicating state
> 4. System triggers benefit recalculation process incorporating updated claim information
>     4.1 Upon invalid status transition, system prevents re-adjudication and notifies user of constraint
> 5. System persists updated settlement with recalculated benefits
> 6. System returns updated settlement details to user for review


**Acceptance Criteria:**

> 1. **Given** a settlement exists with eligible status, **When** adjuster requests re-adjudication with proper authorization, **Then** system transitions settlement to adjudicating status and recalculates benefits
> 2. **Given** settlement status does not permit re-adjudication per product lifecycle, **When** re-adjudication is requested, **Then** system prevents action and returns status constraint error
> 3. **Given** re-adjudication completes successfully, **When** process finishes, **Then** system persists updated settlement and returns complete settlement image
> 4. **Given** request lacks proper authorization, **When** re-adjudication is attempted, **Then** system rejects request during validation phase


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=619721323"
> ]

---

#### Feature: As a Claims Operations Manager, I want to close a leave settlement after approval or disapproval, so that the claim lifecycle is finalized and the settlement record is archived
- **Role**: Claim Adjuster
- **Action**: finalize and close an approved or disapproved leave settlement
- **Value**: the claim lifecycle is completed and settlement records are properly archived for compliance and audit purposes

**Description:**

> As a **Claim Adjuster**,
> I want to **finalize and close an approved or disapproved leave settlement**,
> So that **the claim lifecycle is completed and settlement records are properly archived for compliance and audit purposes**


**Key Capabilities:**

> 1. System validates adjuster privileges and settlement eligibility for closure
> 2. System verifies settlement status transition aligns with product lifecycle configuration
> 3. System updates settlement status to Closed upon validation success
> 4. System triggers business activity monitoring event for audit trail
> 5. System returns finalized settlement record to confirm completion
>     5.1 When status transition is invalid, system prevents closure and notifies adjuster


**Acceptance Criteria:**

> 1. **Given** a valid settlement with proper adjuster privileges, **When** closure is requested, **Then** system transitions settlement to Closed status
> 2. **Given** settlement status incompatible with closure, **When** closure is attempted, **Then** system rejects action and provides status conflict notification
> 3. **Given** successful closure, **When** status update completes, **Then** system triggers monitoring event and archives settlement record
> 4. **Given** missing privileges, **When** closure is requested, **Then** system prevents operation and notifies adjuster
> 5. **Given** completed closure, **When** settlement record is retrieved, **Then** system returns finalized settlement with Closed status confirmed


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=619721321"
> ]

---

#### Feature: As a System Administrator, I want to configure leave settlement adjudication business rules for covered weekly earnings, elimination periods, and maximum benefit durations, so that settlement calculations comply with product specifications
- **Role**: Claim Adjuster
- **Action**: configure settlement adjudication rules to automate benefit calculations for leave claims across multiple leave types
- **Value**: settlement determinations remain consistent with product specifications and regulatory requirements while reducing manual calculation errors

**Description:**

> As a **Claim Adjuster**,
> I want to **configure settlement adjudication rules to automate benefit calculations for leave claims across multiple leave types**,
> So that **settlement determinations remain consistent with product specifications and regulatory requirements while reducing manual calculation errors**


**Key Capabilities:**

> 1. System establishes covered weekly earnings baseline from historical compensation data
> 2. System calculates elimination period duration and through-date before benefit eligibility
> 3. System computes gross weekly benefit amount based on configured formulas
> 4. System determines maximum benefit duration applying leave-type-specific rules
>     4.1 General Leave rules applied when claim categorized as general
>     4.2 Paid Family Leave rules applied for PFL claims
>     4.3 Military Leave rules applied for service-related absences
> 5. System establishes benefit start date following elimination period completion
> 6. System calculates benefit end date constrained by maximum duration limits


**Acceptance Criteria:**

> 1. **Given** leave claim with earnings history, **When** adjudication initiates, **Then** system derives covered weekly earnings per configured rules
> 2. **Given** configured elimination period rules, **When** calculating eligibility, **Then** system determines waiting period and through-date accurately
> 3. **Given** leave type specification, **When** determining duration, **Then** system applies corresponding maximum benefit rules (General/PFL/Military)
> 4. **Given** elimination period completion, **When** establishing payment window, **Then** system calculates benefit start and end dates within maximum duration
> 5. **Given** all calculation inputs available, **When** adjudication completes, **Then** system produces gross weekly amount ready for payment processing
> 6. **Given** incomplete claim data, **When** attempting calculation, **Then** system prevents adjudication until prerequisites satisfied


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=622789236"
> ]

---

#### Feature: As a Claims Adjuster, I want to validate that a policy exists before creating a settlement, so that settlements are only created for valid policies and data integrity is maintained
- **Role**: Claim Adjuster
- **Action**: initiate settlement adjudication with mandatory policy validation to ensure data integrity and prevent processing invalid claims
- **Value**: settlements are created only against verified policies, maintaining system data integrity and preventing downstream processing errors

**Description:**

> As a **Claim Adjuster**,
> I want to **initiate settlement adjudication with mandatory policy validation to ensure data integrity and prevent processing invalid claims**,
> So that **settlements are created only against verified policies, maintaining system data integrity and preventing downstream processing errors**.


**Key Capabilities:**

> 1. Adjuster requests settlement creation providing policy reference information
> 2. System validates request completeness and policy existence against authoritative policy repository
>     2.1 Upon policy verification failure, system rejects request with diagnostic error notification
> 3. System initializes settlement record with unique identifier and transitional status
> 4. System generates settlement number per configured product model pattern
> 5. System persists validated settlement data and advances status to adjudicating
> 6. System triggers automated settlement adjudication workflow and returns settlement confirmation


**Acceptance Criteria:**

> 1. **Given** valid policy reference, **When** adjuster initiates settlement, **Then** system creates settlement with unique identifier and adjudicating status
> 2. **Given** non-existent policy number, **When** settlement creation attempted, **Then** system prevents settlement creation and returns policy validation error
> 3. **Given** incomplete request data, **When** submission occurs, **Then** system blocks processing until mandatory information provided
> 4. **Given** successful settlement initialization, **When** process completes, **Then** system triggers adjudication workflow automatically
> 5. **Given** settlement created, **When** confirmation returned, **Then** response includes settlement number and associated entity references


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=619721324"
> ]

---

#### Feature: As a Claims Adjuster, I want to verify that settlement state transitions are valid before executing commands, so that settlements follow the correct lifecycle and prevent invalid state changes
- **Role**: Claim Adjuster
- **Action**: validate settlement state transitions before executing lifecycle commands to ensure settlements follow the correct progression from adjudication through approval to closure
- **Value**: settlements maintain data integrity, prevent invalid state changes, and enforce proper approval workflows throughout the claim coverage lifecycle

**Description:**

> As a **Claim Adjuster**,
> I want to **validate settlement state transitions before executing lifecycle commands to ensure settlements follow the correct progression from adjudication through approval to closure**,
> So that **settlements maintain data integrity, prevent invalid state changes, and enforce proper approval workflows throughout the claim coverage lifecycle**


**Key Capabilities:**

> 1. System initiates settlement adjudication transitioning claim coverage to adjudicating state upon authorized request
> 2. System executes adjudication rules evaluating payment eligibility based on coverage terms, limits, and deductibles, transitioning to pending state
> 3. System processes approval decision transitioning coverage to approved or disapproved state based on validation outcomes
> 4. Upon re-adjudication request from pending, approved, or disapproved states, system returns coverage to adjudicating state for reprocessing
> 5. System finalizes settlement by transitioning approved or disapproved coverage to terminal closed state
> 6. When state transition is invalid or privilege insufficient, system prevents command execution and maintains current state


**Acceptance Criteria:**

> 1. **Given** settlement is in initial state, **When** adjudication is requested with valid privilege, **Then** system transitions to adjudicating state
> 2. **Given** settlement is in adjudicating state, **When** adjudication completes, **Then** system transitions to pending state with calculated amounts
> 3. **Given** settlement is in pending state, **When** approval command executes, **Then** system transitions to approved or disapproved state based on validation
> 4. **Given** settlement is in approved or disapproved state, **When** closure is requested, **Then** system transitions to terminal closed state
> 5. **Given** settlement is in closed state, **When** any transition command is attempted, **Then** system prevents execution maintaining terminal state
> 6. **Given** settlement is in pending, approved, or disapproved state, **When** re-adjudication is requested, **Then** system transitions back to adjudicating state


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=579239081"
> ]

---

### Epic: Critical Illness Claim Adjudication

#### Feature: As a Claims Adjuster, I want to automatically transition a Critical Illness claim through its lifecycle states (from initialization to open to approval), so that claims are processed efficiently without manual state management.
- **Role**: Claim Adjuster
- **Action**: automatically transition critical illness claims through their complete lifecycle states from initialization to closure based on configured business rules and eligibility verification
- **Value**: claims are processed efficiently without manual state management, reducing processing time and human error while ensuring consistent adjudication outcomes

**Description:**

> As a **Claim Adjuster**,
> I want to **automatically transition critical illness claims through their complete lifecycle states from initialization to closure based on configured business rules and eligibility verification**,
> So that **claims are processed efficiently without manual state management, reducing processing time and human error while ensuring consistent adjudication outcomes**.


**Key Capabilities:**

> 1. System initiates case event and automatically transitions from initialization to open state upon capturing loss information.
> 2. System processes related damage losses sequentially, validating applicability and retrieving policy information.
>     2.1 If loss is not applicable, system skips to next loss in sequence.
> 3. System creates or updates claim based on existence check, then transitions through pending to open state and executes coverage selection.
> 4. System initiates settlement adjudication, performs eligibility verification and benefit calculations, then transitions through approval workflow.
>     4.1 Upon invalid eligibility, system disapproves and closes settlement.
>     4.2 Upon processing error, system readjudicates for reprocessing.
> 5. System automatically closes case when all associated claims reach closed state.


**Acceptance Criteria:**

> 1. **Given** loss information is captured, **when** case initialization triggers, **then** system automatically transitions case to open state and begins damage loss processing.
> 2. **Given** damage losses are identified, **when** sequential processing occurs, **then** system validates applicability and retrieves policy data for applicable losses only.
> 3. **Given** claim eligibility is confirmed, **when** adjudication executes, **then** system creates or updates claim and transitions through configured lifecycle states.
> 4. **Given** settlement adjudication completes, **when** eligibility and calculations are valid, **then** system approves and closes settlement automatically.
> 5. **Given** settlement validation fails, **when** invalid status is returned, **then** system disapproves and closes settlement without manual intervention.
> 6. **Given** all claims reach closed state, **when** final claim closes, **then** system automatically closes parent case.


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=543268170"
> ]

---

#### Feature: As a Claims Adjuster, I want to adjudicate a Critical Illness claim by validating the request and updating the claim status to Open, so that the claim can proceed to settlement processing.
- **Role**: Claim Adjuster
- **Action**: adjudicate a critical illness claim by validating eligibility, transitioning the claim to active status, and initiating settlement processes
- **Value**: the claim progresses through the appropriate lifecycle stages toward timely resolution and payment, ensuring compliance with business rules and policy terms

**Description:**

> As a **Claim Adjuster**,
> I want to **adjudicate a critical illness claim by validating eligibility, transitioning the claim to active status, and initiating settlement processes**,
> So that **the claim progresses through the appropriate lifecycle stages toward timely resolution and payment, ensuring compliance with business rules and policy terms**.


**Key Capabilities:**

> 1. System validates the adjudication request against privilege requirements and claim existence
> 2. System verifies that claim status transition complies with configured lifecycle rules
> 3. System updates claim status to Open upon successful validation
> 4. System initiates settlement creation process and retrieves applicable policy header and coverage data
>     4.1 Upon policy data retrieval, system stores version-specific coverage details
> 5. System triggers business activity monitoring for adjudication tracking
> 6. System returns updated claim information to the adjuster confirming status progression


**Acceptance Criteria:**

> 1. **Given** a valid claim and adjuster with adjudication privileges, **When** adjudication is requested, **Then** the system validates request and updates status to Open
> 2. **Given** claim status does not permit adjudication per lifecycle configuration, **When** adjudication is attempted, **Then** system prevents transition and notifies adjuster of invalid action
> 3. **Given** successful status transition, **When** settlement creation initiates, **Then** system retrieves and stores applicable policy coverage data
> 4. **Given** adjudication completes, **When** system returns claim image, **Then** updated status and settlement details are reflected
> 5. **Given** any validation failure, **When** processing halts, **Then** system provides actionable error context without data loss


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=543268184"
> ]

---

#### Feature: As a Claims Adjuster, I want to retrieve and apply applicable policy coverage data during claim adjudication, so that settlement calculations are based on the correct policy terms.
- **Role**: Claim Adjuster
- **Action**: retrieve and apply applicable policy coverage data during claim adjudication
- **Value**: settlement calculations are based on the correct policy terms

**Description:**

> As a **Claim Adjuster**,
> I want to **retrieve and apply applicable policy coverage data during claim adjudication**,
> So that **settlement calculations are based on the correct policy terms**


**Key Capabilities:**

> 1. User initiates adjudication for an eligible claim with proper authorization
> 2. System validates claim lifecycle status and performer privileges to ensure command execution is permitted
> 3. Upon successful validation, system transitions claim to 'Open' status
> 4. System retrieves applicable policy header and coverage data for the relevant policy version
>     4.1 When policy data is unavailable or incomplete, system halts adjudication and notifies user
> 5. System initiates settlement creation process with retrieved policy terms
> 6. User receives updated claim record confirming adjudication completion and policy application


**Acceptance Criteria:**

> 1. **Given** a valid claim and authorized adjuster, **When** adjudication is requested, **Then** system validates lifecycle status and privilege access
> 2. **Given** lifecycle validation succeeds, **When** adjudication proceeds, **Then** claim transitions to 'Open' status
> 3. **Given** claim is in 'Open' status, **When** settlement initiation begins, **Then** system retrieves and stores applicable policy version coverage data
> 4. **Given** policy data is successfully retrieved, **When** settlement creation completes, **Then** system confirms adjudication and returns updated claim record
> 5. **Given** lifecycle status prevents adjudication, **When** validation fails, **Then** system prevents status transition and notifies user of restriction
> 6. **Given** adjudication completes, **When** user reviews claim, **Then** applied policy terms are visible and traceable


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=543268184"
> ]

---

#### Feature: As a Claims Adjuster, I want to receive an error notification when attempting to adjudicate a claim from an invalid status, so that I understand why the action cannot be performed and can take corrective action.
- **Role**: Claim Adjuster
- **Action**: receive error notifications when attempting to adjudicate claims from invalid statuses
- **Value**: I understand why adjudication cannot proceed and can identify the necessary corrective actions to move the claim to a valid state

**Description:**

> As a **Claim Adjuster**,
> I want to **receive error notifications when attempting to adjudicate claims from invalid statuses**,
> So that **I understand why adjudication cannot proceed and can identify the necessary corrective actions to move the claim to a valid state**.


**Key Capabilities:**

> 1. System validates adjuster privileges and claim existence upon adjudication request
> 2. System evaluates current claim status against configured lifecycle transition rules
> 3. When claim status prohibits adjudication, system blocks the command execution
>     3.1 System generates error notification indicating action cannot be performed from existing status
>     3.2 Process terminates without status change
> 4. Upon successful validation, system transitions claim to Open status and initiates settlement creation
> 5. System retrieves policy header and coverage data for settlement processing


**Acceptance Criteria:**

> 1. **Given** a claim in non-adjudicable status, **When** adjuster attempts adjudication, **Then** system returns error message and prevents status transition
> 2. **Given** adjudication command fails validation, **When** error is triggered, **Then** system provides specific notification explaining status constraint
> 3. **Given** claim in valid status with proper privileges, **When** adjudication is requested, **Then** system transitions claim to Open and initiates settlement
> 4. **Given** lifecycle rules prohibit transition, **When** validation occurs, **Then** claim status remains unchanged and no settlement data is created


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=543268184"
> ]

---

#### Feature: As a System Administrator, I want to configure state machine commands and statuses for Critical Illness claims, so that the system enforces the correct workflow transitions and available actions for each product.
- **Role**: Claim Manager
- **Action**: configure state machine commands and statuses for Critical Illness claim workflows
- **Value**: the system enforces correct workflow transitions, validates claim progression through adjudication stages, and ensures only permissible actions are available at each claim status

**Description:**

> As a **Claim Manager**,
> I want to **configure state machine commands and statuses for Critical Illness claim workflows**,
> So that **the system enforces correct workflow transitions, validates claim progression through adjudication stages, and ensures only permissible actions are available at each claim status**


**Key Capabilities:**

> 1. Configure claim lifecycle states and permissible transitions from initialization through closure
> 2. Define commands available at each claim status (Open, Adjudicating, Approved, Disapproved, Readjudicate)
> 3. Establish validation rules for state transitions based on adjudication outcomes (Invalid, Error, Approved)
>     3.1 When outcome is Invalid, system transitions claim to Disapproved then Closed
>     3.2 When outcome is Error, system transitions to Readjudicate for reprocessing
> 4. Configure automatic case closure triggers when all associated claims reach closed status
> 5. Map coverage selection and eligibility check requirements to adjudication stage configurations


**Acceptance Criteria:**

> 1. **Given** claim status is Open, **When** adjudication is initiated, **Then** system transitions to Adjudicating state and enforces configured coverage selection
> 2. **Given** adjudication outcome is Invalid, **When** processing completes, **Then** system automatically transitions through Disapproved to Closed without manual approval
> 3. **Given** adjudication outcome is Error, **When** system evaluates result, **Then** claim transitions to Readjudicate state enabling reprocessing
> 4. **Given** adjudication outcome is Approved, **When** validation succeeds, **Then** system progresses through Approve, Pending, Approved, to Closed states
> 5. **Given** multiple claims exist under single case, **When** final claim reaches Closed, **Then** system automatically closes parent case
> 6. **Given** configured state machine, **When** user attempts invalid transition, **Then** system prevents action and maintains current status


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=543268170"
> ]

---

#### Feature: As a Claims Operations Manager, I want the system to automatically close a case when all related claims are closed, so that case lifecycle management is completed without manual intervention.
- **Role**: Claim Manager
- **Action**: enable the system to automatically close a case when all related critical illness claims reach closed status
- **Value**: case lifecycle management is completed without manual intervention, reducing operational overhead and ensuring timely case resolution

**Description:**

> As a **Claim Manager**,
> I want to **enable the system to automatically close a case when all related critical illness claims reach closed status**,
> So that **case lifecycle management is completed without manual intervention, reducing operational overhead and ensuring timely case resolution**.


**Key Capabilities:**

> 1. Upon case initialization, system transitions case from incomplete to open status and creates case record.
> 2. System processes related damage losses sequentially, verifying loss applicability before opening loss records.
> 3. System checks for existing claims and either updates or creates new claim records, transitioning to open status.
> 4. System performs automated adjudication including eligibility and benefit calculations.
>     4.1 When adjudication is invalid, settlement transitions to disapproved and closed.
>     4.2 If error occurs, system automatically reprocesses adjudication.
> 5. Upon successful adjudication approval, settlement transitions through pending to approved and closed states.
> 6. When all associated claims reach closed status, system automatically closes the parent case without manual intervention.


**Acceptance Criteria:**

> 1. **Given** a case is open with multiple critical illness claims, **When** all claims transition to closed status, **Then** the system automatically closes the case.
> 2. **Given** a case has mixed claim statuses, **When** one or more claims remain open or in error state, **Then** the case remains open until all claims are resolved.
> 3. **Given** adjudication completes with approved outcome, **When** settlement transitions to closed, **Then** the system evaluates case closure eligibility based on all associated claims.
> 4. **Given** adjudication encounters errors, **When** settlement enters error state, **Then** system automatically reprocesses without requiring manual intervention.
> 5. **Given** loss applicability check fails, **When** system determines loss is not applicable, **Then** processing continues to next loss in sequence without halting case flow.
> 6. **Given** all claims are closed, **When** system evaluates case status, **Then** case lifecycle completes and case transitions to closed state automatically.


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=543268170"
> ]

---

#### Feature: As a Claims Adjuster, I want to initiate, create, update, submit, and close Critical Illness claims through a defined set of use cases, so that all claim operations follow a consistent and controlled workflow.
- **Role**: Claim Adjuster
- **Action**: manage the complete lifecycle of Critical Illness claims from initiation through closure, including adjudication and status management
- **Value**: all claim operations follow a consistent, controlled workflow ensuring accurate evaluation of policy coverage and medical evidence while maintaining proper documentation and status tracking throughout the process

**Description:**

> As a **Claim Adjuster**,
> I want to **manage the complete lifecycle of Critical Illness claims from initiation through closure, including adjudication and status management**,
> So that **all claim operations follow a consistent, controlled workflow ensuring accurate evaluation of policy coverage and medical evidence while maintaining proper documentation and status tracking throughout the process**


**Key Capabilities:**

> 1. User is able to initiate new Critical Illness claims when qualifying diagnosis events occur during active policy coverage periods
> 2. User is able to establish and document comprehensive claim details with all required policy and medical information
> 3. User is able to modify claim information throughout processing to reflect updated medical evidence or policy details
> 4. User is able to submit completed claims for formal evaluation and adjudication workflow
> 5. User is able to adjudicate claims by evaluating medical evidence against policy coverage terms to determine approval or denial outcomes
> 6. User is able to close claims upon final determination or reopen previously closed claims when new information, appeals, or corrections necessitate additional processing


**Acceptance Criteria:**

> 1. **Given** a valid Critical Illness policy is active, **When** the adjuster initiates a claim for a covered diagnosis event, **Then** the system creates a new claim record enabling subsequent lifecycle stages
> 2. **Given** claim information is established, **When** the adjuster updates details during processing, **Then** the system maintains audit history while preserving data integrity
> 3. **Given** required claim information is complete, **When** the adjuster submits for adjudication, **Then** the system validates completeness and advances the claim to evaluation status
> 4. **Given** a claim is submitted, **When** adjudication evaluates medical evidence against policy terms, **Then** the system records the determination outcome with supporting rationale
> 5. **Given** adjudication is finalized, **When** the adjuster closes the claim, **Then** the system prevents further modifications unless formally reopened
> 6. **Given** a closed claim requires revision, **When** the adjuster reopens with valid justification, **Then** the system restores editing capabilities while preserving original closure documentation


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=543268179"
> ]

---

#### Feature: As a Claims Adjuster, I want to receive the updated claim image after adjudication is completed, so that I can verify the claim has been processed correctly with all relevant data.
- **Role**: Claim Adjuster
- **Action**: complete the adjudication process and receive the updated claim image
- **Value**: I can verify the claim has been processed correctly with all relevant data and confirm proper status transitions

**Description:**

> As a **Claim Adjuster**,
> I want to **complete the adjudication process and receive the updated claim image**,
> So that **I can verify the claim has been processed correctly with all relevant data and confirm proper status transitions**


**Key Capabilities:**

> 1. System validates adjudication request and verifies performer privileges
> 2. System confirms claim lifecycle transition eligibility from current status to Open status
> 3. System transitions claim status to Open and retrieves applicable policy header and coverage data
> 4. System initiates settlement creation service with required policy information
>     4.1 Upon policy data retrieval failure, system halts adjudication process
> 5. System triggers business activity monitoring for adjudication completion
> 6. System returns complete claim image containing updated status, settlement details, and policy data


**Acceptance Criteria:**

> 1. **Given** a valid claim in adjudicable status, **When** adjudication is requested with proper privileges, **Then** system transitions claim to Open status and returns updated claim image
> 2. **Given** claim status incompatible with adjudication, **When** adjudication is attempted, **Then** system prevents execution and returns lifecycle violation error
> 3. **Given** successful status transition, **When** settlement creation initiates, **Then** system retrieves and persists policy header and coverage data
> 4. **Given** adjudication completes, **When** claim image is returned, **Then** response contains current status, settlement information, and policy identifiers
> 5. **Given** performer lacks required privileges, **When** adjudication is requested, **Then** system prevents submission with authorization error


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=543268184"
> ]

---

### Epic: Common Claim Processing & Business Rules

#### Feature: As a Claims Adjuster, I want to initiate claim coverage adjudication, so that I can begin the evaluation process for determining claim eligibility and payment amounts
- **Role**: Claim Adjuster
- **Action**: initiate and manage the claim coverage adjudication lifecycle from initial evaluation through final settlement closure
- **Value**: I can systematically determine claim payment eligibility, calculate accurate settlement amounts based on policy coverages and limits, and guide coverage decisions through approval or disapproval to final closure

**Description:**

> As a **Claim Adjuster**,
> I want to **initiate and manage the claim coverage adjudication lifecycle from initial evaluation through final settlement closure**,
> So that **I can systematically determine claim payment eligibility, calculate accurate settlement amounts based on policy coverages and limits, and guide coverage decisions through approval or disapproval to final closure**


**Key Capabilities:**

> 1. Initiate coverage adjudication by requesting settlement evaluation, transitioning coverage to active adjudication state.
> 2. Execute adjudication rules to determine payment eligibility and calculate settlement amounts based on insurable risk coverages, policy limits, and deductibles.
> 3. Approve validated coverage to authorize payment readiness.
>     3.1 Upon validation failure, disapprove coverage to prevent payment processing.
> 4. Re-adjudicate coverage from pending, approved, or disapproved states when new information requires re-evaluation.
> 5. Close finalized coverage from approved or disapproved states to complete the settlement lifecycle.


**Acceptance Criteria:**

> 1. **Given** adjudication is initiated, **When** the request is submitted, **Then** coverage transitions to adjudicating state and becomes available for evaluation.
> 2. **Given** coverage is in adjudicating state, **When** adjudication executes, **Then** system calculates payment amounts using policy rules and transitions coverage to pending state.
> 3. **Given** coverage is pending, **When** approval criteria are met, **Then** coverage transitions to approved state; **When** criteria fail, coverage transitions to disapproved state.
> 4. **Given** coverage requires re-evaluation, **When** re-adjudication is requested from pending/approved/disapproved states, **Then** coverage returns to adjudicating state for updated assessment.
> 5. **Given** coverage is approved or disapproved, **When** closure is initiated, **Then** coverage transitions to closed state and settlement lifecycle completes.
> 6. **Given** user lacks required privileges, **When** attempting state transitions, **Then** system prevents unauthorized actions and maintains current state.


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=322702644"
> ]

---

#### Feature: As a Claims Adjuster, I want to execute adjudication rules to determine claimant eligibility and calculate payment amounts, so that I can move the claim to pending approval status
- **Role**: Claim Adjuster
- **Action**: execute adjudication rules to determine claimant eligibility and calculate settlement amounts based on coverage terms
- **Value**: the claim coverage transitions to pending approval status with validated payment calculations, enabling efficient downstream approval workflows

**Description:**

> As a **Claim Adjuster**,
> I want to **execute adjudication rules to determine claimant eligibility and calculate settlement amounts based on coverage terms**,
> So that **the claim coverage transitions to pending approval status with validated payment calculations, enabling efficient downstream approval workflows**.


**Key Capabilities:**

> 1. Initiate settlement adjudication process, transitioning claim coverage to adjudicating state
> 2. Execute automated business rules to validate claimant eligibility for payment
> 3. Calculate settlement amounts applying policy coverages, deductibles, and limits against claimed losses
> 4. Transition claim coverage from adjudicating to pending approval status upon successful rule execution
>     4.1 Upon validation failure, escalate for manual review or disapproval workflow
> 5. Support re-adjudication when coverage details require updates or recalculation
> 6. Maintain audit trail of adjudication decisions and calculation methodologies


**Acceptance Criteria:**

> 1. **Given** claim coverage in initial state, **When** adjudication is requested, **Then** system transitions coverage to adjudicating state with proper authorization validation
> 2. **Given** coverage in adjudicating state, **When** eligibility rules execute, **Then** system determines claimant payment qualification based on policy terms
> 3. **Given** eligible claimant, **When** calculation rules run, **Then** system computes settlement amounts applying coverages, limits, and deductibles accurately
> 4. **Given** successful adjudication, **When** processing completes, **Then** system transitions claim coverage to pending approval status
> 5. **Given** adjudication rule failure, **When** eligibility cannot be confirmed, **Then** system prevents approval transition and flags for review
> 6. **Given** pending or approved coverage, **When** re-adjudication is triggered, **Then** system returns to adjudicating state allowing rule re-execution


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=322702644"
> ]

---

#### Feature: As a Claims Adjuster, I want to re-adjudicate claim coverage with updated details, so that I can recalculate eligibility and payment amounts based on new information
- **Role**: Claim Adjuster
- **Action**: re-adjudicate claim coverage with updated details to recalculate eligibility and payment amounts
- **Value**: accurate claim settlements reflect current policy terms, coverage limits, and claimant circumstances

**Description:**

> As a **Claim Adjuster**,
> I want to **re-adjudicate claim coverage with updated details to recalculate eligibility and payment amounts**,
> So that **accurate claim settlements reflect current policy terms, coverage limits, and claimant circumstances**


**Key Capabilities:**

> 1. User initiates re-adjudication from Pending, Approved, or Disapproved coverage states with updated claim details
> 2. System transitions coverage back to Adjudicating state and validates user privileges for re-adjudication authority
> 3. System executes adjudication rules engine to recalculate claimant payment eligibility against policy coverage parameters
> 4. System recalculates payment amounts applying updated coverage limits, deductibles, and insurable risk item values
> 5. System transitions coverage to Pending state upon completion, ready for approval workflow
>     5.1 If coverage fails validation rules, system routes to Disapproval path
> 6. User reviews recalculated settlement and proceeds to approval or disapproval decision


**Acceptance Criteria:**

> 1. **Given** coverage exists in Pending, Approved, or Disapproved state, **When** adjuster initiates re-adjudication with updated details, **Then** system transitions coverage to Adjudicating state and executes calculation rules
> 2. **Given** re-adjudication completes successfully, **When** system applies updated coverage limits and deductibles, **Then** payment amounts are recalculated and coverage moves to Pending state
> 3. **Given** updated details fail eligibility rules, **When** re-adjudication executes, **Then** system routes coverage toward Disapproval path with validation failure reasons
> 4. **Given** user lacks re-adjudication privileges, **When** re-adjudication is attempted, **Then** system prevents state transition and notifies insufficient authorization
> 5. **Given** coverage is in Closed state, **When** re-adjudication is requested, **Then** system prevents transition as Closed is terminal state
> 6. **Given** re-adjudication completes, **When** adjuster reviews results, **Then** historical adjudication details are preserved for audit trail


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=322702644"
> ]

---

#### Feature: As a Claims Examiner, I want to approve claim coverage after validation, so that the claim is ready for payment processing
- **Role**: Claim Adjuster
- **Action**: approve claim coverage after successful adjudication and validation
- **Value**: the claim progresses to payment processing with verified eligibility and calculated settlement amounts

**Description:**

> As a **Claim Adjuster**,
> I want to **approve claim coverage after successful adjudication and validation**,
> So that **the claim progresses to payment processing with verified eligibility and calculated settlement amounts**


**Key Capabilities:**

> 1. Initiate coverage adjudication to transition claim from initial state to active processing
> 2. Execute adjudication rules to evaluate claimant eligibility, calculate settlement amounts based on policy coverages, limits, and deductibles
> 3. Approve settlement when validation succeeds, advancing coverage to payment-ready state
>     3.1 Upon validation failure, disapprove settlement and document rejection rationale
>     3.2 When reprocessing required, re-adjudicate from pending, approved, or disapproved states
> 4. Finalize claim coverage by closing approved or disapproved settlements as terminal state


**Acceptance Criteria:**

> 1. **Given** claim coverage initiated, **When** adjudication rules execute, **Then** system transitions to pending state with calculated settlement amount
> 2. **Given** pending coverage passes validation, **When** approval submitted, **Then** system updates state to approved and enables payment processing
> 3. **Given** validation fails, **When** disapproval action triggered, **Then** system prevents payment and records disapproved state
> 4. **Given** coverage in pending/approved/disapproved state, **When** re-adjudication requested, **Then** system resets to adjudicating and re-executes rules
> 5. **Given** approved or disapproved coverage, **When** closure initiated, **Then** system finalizes to terminal closed state
> 6. **Given** user lacks required privilege, **When** state transition attempted, **Then** system prevents unauthorized action


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=322702644"
> ]

---

#### Feature: As a Claims Examiner, I want to disapprove claim coverage when validation fails, so that the claim is marked as ineligible for payment
- **Role**: Claim Adjuster
- **Action**: disapprove claim coverage when validation fails during adjudication
- **Value**: ineligible claims are systematically rejected, preventing improper payments and ensuring policy compliance

**Description:**

> As a **Claim Adjuster**,
> I want to **disapprove claim coverage when validation fails during adjudication**,
> So that **ineligible claims are systematically rejected, preventing improper payments and ensuring policy compliance**.


**Key Capabilities:**

> 1. System adjudicates settlement by executing validation rules against policy coverages, limits, and deductibles
> 2. Upon validation failure, adjuster reviews adjudication results in Pending state
> 3. Adjuster disapproves settlement, transitioning coverage to Disapproved state
>     3.1 If additional review needed, adjuster re-adjudicates settlement to update details and re-run validation
> 4. Adjuster closes disapproved settlement, finalizing coverage lifecycle in terminal Closed state


**Acceptance Criteria:**

> 1. **Given** coverage is in Pending state **When** validation rules fail **Then** system enables disapproval action with required privilege
> 2. **Given** adjuster disapproves settlement **When** disapproval is executed **Then** coverage transitions to Disapproved state
> 3. **Given** coverage is Disapproved **When** adjuster initiates closure **Then** system transitions coverage to terminal Closed state
> 4. **Given** coverage is Disapproved **When** re-adjudication is needed **Then** system permits return to Adjudicating state
> 5. **Given** coverage reaches Closed state **When** terminal state is achieved **Then** system prevents further state transitions


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=322702644"
> ]

---

#### Feature: As a Claims Operations Manager, I want to close claim coverage in approved or disapproved status, so that the claim lifecycle is finalized
- **Role**: Claim Adjuster
- **Action**: finalize claim coverage by closing it in either approved or disapproved status
- **Value**: the claim lifecycle reaches completion and coverage decisions are formally recorded

**Description:**

> As a **Claim Adjuster**,
> I want to **finalize claim coverage by closing it in either approved or disapproved status**,
> So that **the claim lifecycle reaches completion and coverage decisions are formally recorded**


**Key Capabilities:**

> 1. Initiate claim coverage and transition to adjudicating state
> 2. Execute adjudication rules to calculate payment amounts based on coverage limits and deductibles, transitioning coverage to pending state
> 3. Review pending coverage and approve when validation passes, transitioning to approved state
>     3.1 Upon validation failure, disapprove coverage and transition to disapproved state
> 4. Re-adjudicate coverage from pending, approved, or disapproved states when coverage details require updates
> 5. Close coverage from approved or disapproved states to finalize the claim lifecycle
> 6. System enforces state-based command privileges throughout the coverage lifecycle


**Acceptance Criteria:**

> 1. **Given** coverage is in approved state, **When** closure is initiated, **Then** system transitions coverage to closed state successfully
> 2. **Given** coverage is in disapproved state, **When** closure is initiated, **Then** system transitions coverage to closed state successfully
> 3. **Given** coverage is in pending or adjudicating state, **When** closure is attempted, **Then** system prevents closure until approval or disapproval decision is rendered
> 4. **Given** coverage is closed, **When** any lifecycle command is attempted, **Then** system prevents further state transitions
> 5. **Given** user lacks close settlement privilege, **When** closure is attempted, **Then** system denies the operation
> 6. **Given** coverage reaches closed state, **When** queried, **Then** system records final status as approved or disapproved accurately


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=322702644"
> ]

---

#### Feature: As a Claims Adjuster, I want to initiate a new claim with an auto-generated claim number, so that each claim has a unique identifier for tracking
- **Role**: Claim Adjuster
- **Action**: initiate a new claim with automated unique identifier assignment
- **Value**: each claim is distinctly tracked throughout its lifecycle, ensuring accurate processing and audit compliance

**Description:**

> As a **Claim Adjuster**,
> I want to **initiate a new claim with automated unique identifier assignment**,
> So that **each claim is distinctly tracked throughout its lifecycle, ensuring accurate processing and audit compliance**.


**Key Capabilities:**

> 1. User initiates claim creation triggering unique identifier generation according to product model configuration
> 2. System creates claim record in preliminary status awaiting validation
>     2.1 Upon generation error, system prevents submission until issue resolution
>     2.2 User is able to review preliminary claim data before validation
> 3. System assigns required privileges for initiation command execution
> 4. User is able to proceed to claim validation phase or close preliminary record if cancellation required


**Acceptance Criteria:**

> 1. **Given** authorized user triggers claim initiation, **When** system processes request, **Then** unique identifier is generated per product pattern and claim enters preliminary status
> 2. **Given** identifier generation fails, **When** system detects error, **Then** claim remains inaccessible for submission until corrective action taken
> 3. **Given** claim in preliminary status, **When** user reviews record, **Then** system provides closure or validation path options
> 4. **Given** user lacks initiation privilege, **When** creation attempted, **Then** system prevents command execution


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=395621562"
> ]

---

#### Feature: As a Claims Adjuster, I want to update claim details throughout the lifecycle, so that I can maintain accurate claim information
- **Role**: Claim Adjuster
- **Action**: manage claim progression through lifecycle states and update claim information at each stage
- **Value**: accurate claim information is maintained and claims move efficiently from initiation through closure with appropriate payment decisions

**Description:**

> As a **Claim Adjuster**,
> I want to **manage claim progression through lifecycle states and update claim information at each stage**,
> So that **accurate claim information is maintained and claims move efficiently from initiation through closure with appropriate payment decisions**.


**Key Capabilities:**

> 1. Initiate new claim with system-generated unique identifier in Incomplete state for initial data gathering
> 2. Validate and create claim to transition from Incomplete to Pending state upon successful policy retrieval
> 3. Update claim details at any active state without triggering unintended state transitions
> 4. Submit claim for payment processing to transition from Pending to Open state when payment decision is made
>     4.1 Alternatively, create lump sum payment and close immediately from Pending state
>     4.2 Or cancel claim without payments directly to Closed state
> 5. Close claim after all payments issued or when cancellation is appropriate
> 6. Reopen closed claim to return to previous active state when additional processing is required


**Acceptance Criteria:**

> 1. **Given** user initiates claim, **when** system generates claim number, **then** claim enters Incomplete state with unique identifier per product model pattern
> 2. **Given** claim is in Incomplete state with valid data, **when** user creates claim, **then** system validates data, retrieves policy details, and transitions to Pending state
> 3. **Given** claim is in any active state, **when** user updates claim information, **then** system saves changes without altering current state or triggering unintended transitions
> 4. **Given** claim is in Pending state, **when** user submits for payment, **then** claim transitions to Open state indicating payment obligation
> 5. **Given** claim created in Incomplete with system error, **when** user attempts submission, **then** system prevents progression and requires closure and recreation
> 6. **Given** claim is Closed, **when** user reopens claim, **then** system restores to last active state before closure with appropriate sub-status handling


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=395621562"
> ]

---

#### Feature: As a Claims Adjuster, I want to create a claim by retrieving related policy details, so that the claim moves to pending status with validated policy information
- **Role**: Claim Adjuster
- **Action**: create a claim by retrieving and validating related policy details
- **Value**: the claim transitions to pending status with accurate policy information, enabling informed adjudication decisions

**Description:**

> As a **Claim Adjuster**,
> I want to **create a claim by retrieving and validating related policy details**,
> So that **the claim transitions to pending status with accurate policy information, enabling informed adjudication decisions**


**Key Capabilities:**

> 1. Upon claim initiation, system generates unique claim number and establishes incomplete state with required data entry
> 2. Adjuster executes claim creation command to trigger policy detail retrieval and validation
> 3. System validates claim data completeness and retrieves associated policy coverage information
> 4. Upon successful validation, claim transitions from incomplete to pending state
>     4.1 If validation fails due to system error, adjuster reviews issue, closes claim, resolves problem, and recreates claim
> 5. Adjuster confirms policy details are accessible for subsequent adjudication activities
> 6. Claim remains in pending state awaiting submission decision or additional information gathering


**Acceptance Criteria:**

> 1. **Given** claim is in incomplete state, **When** adjuster initiates claim creation with valid data, **Then** system retrieves policy details and transitions claim to pending status
> 2. **Given** claim creation is triggered, **When** policy details cannot be retrieved, **Then** system prevents state transition and maintains incomplete status
> 3. **Given** claim is in pending state, **When** adjuster accesses claim record, **Then** validated policy coverage information is available for review
> 4. **Given** system error occurs during creation, **When** claim remains incomplete, **Then** system prevents submission until adjuster closes and recreates claim
> 5. **Given** claim creation succeeds, **When** unique claim number is generated, **Then** number follows product model pattern per business rules
> 6. **Given** claim reaches pending state, **When** adjuster reviews claim, **Then** system displays no payment decision has been made


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=395621562"
> ]

---

#### Feature: As a Claims Examiner, I want to submit a claim to open status, so that the claim is approved for payment processing
- **Role**: Claim Adjuster
- **Action**: submit a validated claim to open status for payment processing authorization
- **Value**: the claim is approved and authorized for payment disbursement, enabling timely settlement and closure

**Description:**

> As a **Claim Adjuster**,
> I want to **submit a validated claim to open status for payment processing authorization**,
> So that **the claim is approved and authorized for payment disbursement, enabling timely settlement and closure**


**Key Capabilities:**

> 1. System validates claim completeness and retrieves associated policy coverage details
> 2. User reviews validated claim data and confirms eligibility for payment approval
> 3. Upon authorization, user submits claim transitioning status from Pending to Open
>     3.1 System verifies user has Submit Loss privilege before processing
>     3.2 If submission fails validation, claim remains in Pending status for correction
> 4. System approves claim for payment processing and updates lifecycle state
> 5. User is able to update claim details or set sub-status within Open state without reverting approval
> 6. If closure needed, user closes claim from Open status completing the lifecycle


**Acceptance Criteria:**

> 1. **Given** claim is in Pending status with complete validated data, **When** authorized user submits claim, **Then** system transitions claim to Open status and enables payment processing
> 2. **Given** user lacks Submit Loss privilege, **When** submission is attempted, **Then** system prevents status transition and displays authorization error
> 3. **Given** claim has validation errors, **When** submission is attempted from Pending, **Then** system prevents transition and identifies incomplete data requirements
> 4. **Given** claim is in Open status, **When** user updates claim information, **Then** system maintains Open status without reverting approval
> 5. **Given** claim is successfully submitted to Open, **When** associated case status is reviewed, **Then** case status must be Open per business rules
> 6. **Given** claim requires closure after submission, **When** user initiates close action from Open status, **Then** system transitions claim to Closed status completing lifecycle


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=395621562"
> ]

---

#### Feature: As a Claims Operations Manager, I want to close a claim, so that all payments have been issued or the claim has been cancelled
- **Role**: Claim Adjuster
- **Action**: finalize and close a claim after all payment obligations are fulfilled or the claim is cancelled
- **Value**: the claim lifecycle is completed, ensuring financial and operational accountability while maintaining accurate claim status records

**Description:**

> As a **Claim Adjuster**,
> I want to **finalize and close a claim after all payment obligations are fulfilled or the claim is cancelled**,
> So that **the claim lifecycle is completed, ensuring financial and operational accountability while maintaining accurate claim status records**.


**Key Capabilities:**

> 1. User initiates claim closure action from active claim states (Incomplete, Pending, or Open)
> 2. System validates closure eligibility based on payment status and business rules
>     2.1 Upon validation success, system transitions claim to Closed state
>     2.2 If validation fails due to incomplete payments or pending activities, system prevents closure
> 3. System records closure timestamp, reason code, and finalizing user for audit purposes
> 4. Upon closure, system updates case status mapping and removes claim from active workqueues
> 5. User is able to document closure rationale (payments complete vs. cancellation)
> 6. System ensures closed claim can only be modified through formal reopen process


**Acceptance Criteria:**

> 1. **Given** a claim in Open state with all payments issued, **When** adjuster initiates closure, **Then** system transitions claim to Closed state successfully
> 2. **Given** a claim in Pending state, **When** adjuster closes claim without payment, **Then** system records cancellation and transitions to Closed state
> 3. **Given** a claim with pending payment obligations, **When** closure is attempted, **Then** system prevents closure and alerts user to outstanding activities
> 4. **Given** a closed claim, **When** adjuster attempts direct modification, **Then** system blocks action and requires formal reopen process
> 5. **Given** proper user privileges (Close Loss), **When** closure is initiated, **Then** system permits action; otherwise access is denied
> 6. **Given** successful closure, **When** claim reaches Closed state, **Then** system removes claim from active processing queues


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=395621562"
> ]

---

#### Feature: As a Claims Adjuster, I want to reopen a closed claim, so that I can return it to the previous status for further processing or correction
- **Role**: Claim Adjuster
- **Action**: reopen a closed claim to restore it to a previous active status
- **Value**: I can correct errors, process additional payments, or incorporate new information discovered after claim closure

**Description:**

> As a **Claim Adjuster**,
> I want to **reopen a closed claim to restore it to a previous active status**,
> So that **I can correct errors, process additional payments, or incorporate new information discovered after claim closure**


**Key Capabilities:**

> 1. Adjuster initiates claim reopening process for a claim in Closed status
> 2. System validates adjuster privileges (PRIV>Reopen Loss) and claim eligibility for reopening
> 3. Upon validation, system restores claim to its state immediately before closure OR to Incomplete status based on business rules
> 4. System re-enables update capabilities appropriate to the restored claim status (Incomplete, Pending, or Open)
> 5. Adjuster performs necessary corrections, updates, or processes additional payments
> 6. Upon completion, adjuster follows standard lifecycle progression to re-close the claim


**Acceptance Criteria:**

> 1. **Given** a claim in Closed status, **When** authorized adjuster initiates reopening, **Then** system validates privileges and restores claim to pre-closure or Incomplete status
> 2. **Given** claim successfully reopened, **When** status is restored, **Then** appropriate update commands become available based on the restored status
> 3. **Given** insufficient privileges, **When** reopening is attempted, **Then** system prevents action and maintains Closed status
> 4. **Given** reopened claim, **When** adjuster completes corrections, **Then** claim can progress through standard lifecycle to closure
> 5. **Given** claim in non-Closed status, **When** reopen command is attempted, **Then** system rejects the action as invalid


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=395621562"
> ]

---

#### Feature: As a Claims Adjuster, I want to set and update claim sub-status, so that I can track detailed workflow states within each main claim status
- **Role**: Claim Adjuster
- **Action**: set and update claim sub-status values to track granular workflow states within the primary claim lifecycle stages
- **Value**: I can maintain visibility of detailed claim progression and operational milestones without altering the main status, enabling better case management and reporting

**Description:**

> As a **Claim Adjuster**,
> I want to **set and update claim sub-status values to track granular workflow states within the primary claim lifecycle stages**,
> So that **I can maintain visibility of detailed claim progression and operational milestones without altering the main status, enabling better case management and reporting**


**Key Capabilities:**

> 1. User is able to assign sub-status designations to claims while in Incomplete, Pending, or Open states without triggering primary state transitions
> 2. Upon sub-status update execution, system validates privilege requirements specific to current claim state per authorization matrix
> 3. User is able to modify sub-status iteratively as claim investigation or adjudication milestones are reached
> 4. System maintains sub-status history alongside primary status transitions to support audit and workflow analysis
> 5. When updating claim details or performing adjudication activities, user can independently set sub-status to reflect concurrent operational context


**Acceptance Criteria:**

> 1. **Given** a claim exists in Incomplete, Pending, or Open state, **When** the adjuster sets a sub-status, **Then** the system records the sub-status without changing the primary claim state
> 2. **Given** insufficient privileges for the current state, **When** sub-status assignment is attempted, **Then** the system prevents the update and enforces authorization requirements
> 3. **Given** a claim undergoes multiple sub-status changes, **When** viewing claim history, **Then** the system displays the complete chronological sub-status trail
> 4. **Given** a claim transitions to Closed state, **When** reviewing final records, **Then** the last assigned sub-status is preserved in the claim audit log
> 5. **Given** concurrent claim update operations, **When** sub-status is modified, **Then** the system processes the change independently without blocking other claim attribute updates


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=395621562"
> ]

---

### Epic: Disability Claim Adjudication & Benefits

#### Feature: As a Claims Adjuster, I want to validate disability claim technical requirements before adjudication, so that critical errors are identified early and prevent invalid claim processing
- **Role**: Claim Adjuster
- **Action**: validate disability claim technical requirements before adjudication
- **Value**: critical errors are identified early and invalid claim processing is prevented

**Description:**

> As a **Claim Adjuster**,
> I want to **validate disability claim technical requirements before adjudication**,
> So that **critical errors are identified early and invalid claim processing is prevented**


**Key Capabilities:**

> 1. Upon claim coverage adjudication initiation, system executes technical validation checks for critical errors
>     1.1 When critical error detected, system adds diagnostic message to claim record
>     1.2 System immediately halts adjudication workflow to prevent downstream processing
> 2. User is able to review validation error messages and identify specific technical deficiencies
> 3. System prevents progression to elimination period calculation until all critical errors resolved
> 4. When validation passes, system enables transition to benefit period and financial attribute calculation stages
> 5. Upon any subsequent claim data modification, system re-triggers technical validation to maintain data integrity
> 6. System logs validation outcome and timestamp for audit trail and compliance reporting


**Acceptance Criteria:**

> 1. **Given** a claim with critical technical errors, **When** adjudication process initiates, **Then** system halts workflow immediately and prevents benefit calculations
> 2. **Given** validation detects critical errors, **When** error condition occurs, **Then** system records diagnostic messages without proceeding to elimination period determination
> 3. **Given** a technically valid claim, **When** validation completes successfully, **Then** system permits progression to benefit calculation and eligibility evaluation stages
> 4. **Given** validation has passed, **When** claim data is subsequently modified, **Then** system re-executes technical validation before permitting further adjudication
> 5. **Given** incomplete or inconsistent claim data, **When** technical validation executes, **Then** system prevents submission and requires data remediation before proceeding


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=610902003"
> ]

---

#### Feature: As a Claims Adjuster, I want to evaluate claimant eligibility for disability benefits based on policy and claim details, so that only qualified claimants receive benefits
- **Role**: Claim Adjuster
- **Action**: evaluate claimant eligibility for disability benefits and process adjudication decisions based on policy provisions and claim information
- **Value**: only qualified claimants receive appropriate disability benefits with accurate payment amounts and proper claim status tracking

**Description:**

> As a **Claim Adjuster**,
> I want to **evaluate claimant eligibility for disability benefits and process adjudication decisions based on policy provisions and claim information**,
> So that **only qualified claimants receive appropriate disability benefits with accurate payment amounts and proper claim status tracking**


**Key Capabilities:**

> 1. Evaluate claimant eligibility against policy provisions and claim details to determine qualification for disability benefits
> 2. Calculate gross benefit amounts using approved formulas and apply proration rules when partial period coverage applies
> 3. Determine taxable portion of benefit payments according to tax regulations and policy terms
> 4. Generate payment line items for approved disability claims with accurate benefit and tax amounts
> 5. Validate adjudication outcomes and decisions to prevent invalid or inconsistent results
> 6. Assign appropriate claim status and sub-status, including automated future claim designation when effective date is deferred


**Acceptance Criteria:**

> 1. **Given** claim details and policy provisions are available, **When** adjuster evaluates eligibility, **Then** system determines qualification status based on all applicable business rules
> 2. **Given** claimant is eligible, **When** benefit calculation is performed, **Then** system computes accurate gross benefit amount and applies proration if required
> 3. **Given** benefit amount is calculated, **When** tax determination executes, **Then** system identifies correct taxable percentage per regulations
> 4. **Given** adjudication is complete, **When** validation runs, **Then** system prevents processing if outcomes are invalid or inconsistent
> 5. **Given** claim has future effective date, **When** status assignment occurs, **Then** system automatically applies future claim sub-status
> 6. **Given** adjudication is approved, **When** payment processing initiates, **Then** system generates complete payment line items with accurate amounts


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=477468931"
> ]

---

#### Feature: As a Claims Adjuster, I want to calculate elimination period through dates for disability claims, so that benefit payment start dates are accurately determined
- **Role**: Claim Adjuster
- **Action**: calculate elimination period through dates and benefit payment timelines for disability claims
- **Value**: benefit payment start dates are accurately determined and maximum benefit periods are properly calculated with gap adjustments

**Description:**

> As a **Claim Adjuster**, I want to **calculate elimination period through dates and benefit payment timelines for disability claims**, so that **benefit payment start dates are accurately determined and maximum benefit periods are properly calculated with gap adjustments**.


**Key Capabilities:**

> 1. System validates claim technical requirements and retrieves policy coverage configuration for benefit calculations
> 2. System calculates elimination period through dates and maximum benefit start dates based on policy terms
> 3. System computes financial benefit attributes including covered earnings, benefit amounts, taxable percentages, and proration rates
> 4. System evaluates eligibility criteria and determines auto-adjudication qualification using business rules
> 5. System establishes approval periods and calculates benefit durations including used and remaining periods
>     5.1 When non-payable gaps occur before benefit end date, system extends maximum benefit end date by gap duration
>     5.2 Upon insertion of new gap periods, system re-evaluates subsequent periods for additional extensions
> 6. System validates adjudication results and updates eligibility status if critical errors are detected without manual override


**Acceptance Criteria:**

> 1. **Given** valid claim and policy data, **when** adjudication executes, **then** elimination period through date is calculated and benefit start date is established correctly
> 2. **Given** policy benefit duration configuration, **when** system calculates periods, **then** maximum benefit duration is computed in calendar weeks without proration
> 3. **Given** approved and non-payable periods exist, **when** calculating benefit end dates, **then** non-payable gaps extending within maximum benefit window extend the end date accordingly
> 4. **Given** new gap period is inserted between existing periods, **when** system re-evaluates, **then** previously excluded periods now within extended window further adjust benefit end date
> 5. **Given** critical errors detected during validation, **when** eligibility is not manually overridden, **then** system updates eligibility status to ineligible
> 6. **Given** all calculations complete successfully, **when** adjudication finalizes, **then** benefit used duration and remaining duration are accurately computed for payment processing


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=610902003"
> ]

---

#### Feature: As a Claims Adjuster, I want to calculate financial benefit attributes including covered earnings, minimum/maximum benefit amounts, and taxable percentages, so that accurate benefit payments are generated
- **Role**: Claim Adjuster
- **Action**: adjudicate disability claims by evaluating eligibility, calculating financial benefits, determining approval periods, and validating results to enable accurate benefit payments
- **Value**: benefit payments are calculated accurately based on policy terms, eligibility rules, and approved periods while ensuring compliance with business rules and eliminating manual errors

**Description:**

> As a **Claim Adjuster**,
> I want to **adjudicate disability claims by evaluating eligibility, calculating financial benefits, determining approval periods, and validating results to enable accurate benefit payments**,
> So that **benefit payments are calculated accurately based on policy terms, eligibility rules, and approved periods while ensuring compliance with business rules and eliminating manual errors**


**Key Capabilities:**

> 1. Upon claim submission, system validates technical requirements and halts processing if critical errors are detected
> 2. System calculates elimination period end date and maximum benefit period based on policy coverage terms
> 3. System computes financial attributes including covered earnings, minimum/maximum benefit amounts, taxable percentages, prorating rates, and rehabilitation/partial disability parameters from policy and claim data
> 4. System evaluates insured eligibility against disability criteria and determines if claim qualifies for auto-adjudication
> 5. User is able to establish approval periods manually or system generates periods automatically; system calculates benefit duration including start date, used duration, and remaining duration with gap extension logic for non-payable periods
> 6. System validates adjudication results, identifies critical errors, and updates eligibility status accordingly


**Acceptance Criteria:**

> 1. **Given** technical validation detects critical errors, **when** adjudication initiates, **then** system halts processing immediately and surfaces error messages without proceeding to subsequent steps
> 2. **Given** policy terms define benefit duration, **when** system calculates maximum benefit period, **then** elimination period, maximum benefit start/end dates, and duration are computed according to policy provisions
> 3. **Given** claim and policy data are available, **when** financial attributes are calculated, **then** covered earnings, benefit amounts, taxable percentages, and disability parameters are determined accurately using business rules
> 4. **Given** eligibility criteria are defined, **when** system evaluates eligibility, **then** insured status is determined and auto-adjudication suitability is assessed
> 5. **Given** approval periods exist, **when** benefit duration is calculated, **then** system computes used and remaining duration with non-payable periods extending benefit end dates per chronological gap extension rules
> 6. **Given** adjudication completes, **when** validation executes, **then** system identifies errors and updates eligibility status if critical issues are found and overrides are not present


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=610902003"
> ]

---

#### Feature: As a Claims Adjuster, I want to calculate maximum benefit periods including start dates, end dates, and benefit duration, so that benefit payment limits are properly enforced
- **Role**: Claim Adjuster
- **Action**: calculate maximum benefit periods including start dates, end dates, and benefit duration
- **Value**: benefit payment limits are properly enforced and aligned with policy terms

**Description:**

> As a Claim Adjuster,
> I want to calculate maximum benefit periods including start dates, end dates, and benefit duration,
> So that benefit payment limits are properly enforced and aligned with policy terms.


**Key Capabilities:**

> 1. System calculates maximum benefit start date based on elimination period through date plus one day
> 2. System determines initial maximum benefit end date using policy coverage duration converted from calendar weeks to days
> 3. System extends maximum benefit end date when non-payable approval periods occur prior to calculated end date
>     3.1 Upon encountering non-payable period, system adds period duration to maximum benefit end date
>     3.2 When non-payable period ends beyond current maximum benefit end date, system does not extend
> 4. System reevaluates all benefit period calculations when new approval periods are inserted
> 5. System calculates benefit used duration by totaling all approved period durations
> 6. System determines benefit remaining duration by subtracting used duration from maximum benefit duration


**Acceptance Criteria:**

> 1. **Given** elimination period through date is established, **When** benefit period calculation executes, **Then** maximum benefit start date equals elimination period through date plus one day
> 2. **Given** policy coverage defines benefit duration in calendar weeks, **When** system calculates maximum benefit end date, **Then** duration is converted to days without proration
> 3. **Given** non-payable approval period occurs before maximum benefit end date, **When** system processes gap extension, **Then** maximum benefit end date extends by non-payable period duration
> 4. **Given** non-payable approval period is inserted after initial calculation, **When** system reevaluates, **Then** all subsequent periods and dates are recalculated in chronological order
> 5. **Given** multiple approved periods exist, **When** benefit used duration is calculated, **Then** total equals sum of all approved period durations
> 6. **Given** benefit used duration equals maximum benefit duration, **When** system calculates remaining duration, **Then** result equals zero and no further benefits are payable


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=610902003"
> ]

---

#### Feature: As a Claims Adjuster, I want to manage approval periods for disability claims, so that I can track which periods are approved, non-payable, or pending review
- **Role**: Claim Adjuster
- **Action**: manage and track approval periods for disability claims throughout the benefit lifecycle
- **Value**: accurate benefit duration tracking, proper eligibility determination, and compliant payment processing are ensured

**Description:**

> As a **Claim Adjuster**,
> I want to **manage and track approval periods for disability claims throughout the benefit lifecycle**,
> So that **accurate benefit duration tracking, proper eligibility determination, and compliant payment processing are ensured**


**Key Capabilities:**

> 1. System validates technical prerequisites and calculates foundational benefit parameters (elimination period, max benefit duration, weekly covered earnings)
> 2. System evaluates insured eligibility and determines auto-adjudication qualification
> 3. User establishes approval periods manually, or system applies auto-generated periods from adjudication evaluation
>     3.1 Upon manual entry, user designates periods as Approved, Non-Payable, or Pending
>     3.2 When auto-adjudication qualifies, system creates periods without user intervention
> 4. System calculates benefit start date, duration consumed, and remaining entitlement based on Approved periods
> 5. System extends max benefit end date when Non-Payable periods create gaps within the benefit window
> 6. System validates adjudication results and updates eligibility status if critical errors surface


**Acceptance Criteria:**

> 1. **Given** technical validations pass, **When** adjudication executes, **Then** system calculates elimination period, max benefit duration, and financial attributes without errors
> 2. **Given** eligibility evaluation completes, **When** approval periods are established, **Then** system distinguishes Approved periods (counted toward benefit usage) from Non-Payable periods (potential gap extensions)
> 3. **Given** Non-Payable periods exist within the benefit window, **When** max benefit end date is calculated, **Then** system extends the end date by gap duration and processes cascading extensions chronologically
> 4. **Given** Non-Payable period ends after max benefit end date, **When** extension logic applies, **Then** system excludes that period from extending the end date
> 5. **Given** critical errors emerge during validation, **When** eligibility status lacks override, **Then** system forces eligibility to Not Eligible
> 6. **Given** benefit periods finalize, **When** user reviews claim, **Then** system displays benefit used duration and remaining duration accurately


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=610902003"
> ]

---

#### Feature: As a Claims Adjuster, I want to validate adjudication results and identify critical errors affecting eligibility, so that claim eligibility status is accurately determined and EOB messages are set
- **Role**: Claim Adjuster
- **Action**: validate adjudication results and identify critical errors affecting eligibility determination
- **Value**: claim eligibility status is accurately determined and Explanation of Benefits (EOB) messages are properly set to support payment decisions

**Description:**

> As a **Claim Adjuster**,
> I want to **validate adjudication results and identify critical errors affecting eligibility determination**,
> So that **claim eligibility status is accurately determined and Explanation of Benefits (EOB) messages are properly set to support payment decisions**


**Key Capabilities:**

> 1. System executes final adjudication result validation after all coverage calculations and eligibility evaluations are completed
> 2. System identifies critical errors within adjudication results by applying validation business rules
>     2.1 Upon detecting critical errors, system generates Explanation of Benefits (EOB) messages documenting specific validation failures
> 3. System evaluates whether eligibility status override is applied to the claim
>     3.1 When no override exists and critical errors are present, system updates eligibility status to 'Not Eligible'
>     3.2 When override is present, system preserves adjuster-determined eligibility status regardless of critical errors
> 4. System finalizes claim adjudication outcome with validated eligibility status and complete EOB messaging for downstream payment processing


**Acceptance Criteria:**

> 1. **Given** adjudication process completes all financial and eligibility calculations, **When** validation executes, **Then** system identifies all critical errors per validation business rules and generates corresponding EOB messages
> 2. **Given** critical errors exist and eligibility status has no override, **When** validation completes, **Then** system updates eligibility status to 'Not Eligible'
> 3. **Given** critical errors exist but eligibility status is overridden, **When** validation completes, **Then** system preserves the overridden eligibility status and documents errors via EOB messages only
> 4. **Given** no critical errors are detected, **When** validation completes, **Then** system maintains eligibility status determined during eligibility evaluation step
> 5. **Given** validation completes successfully, **When** adjuster reviews results, **Then** all EOB messages clearly communicate reasons affecting eligibility determination


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=610902003"
> ]

---

#### Feature: As a Claims Adjuster, I want to adjudicate State Mandated Product (SMP) claims with coverage validation and benefit calculations, so that SMP claims are processed according to regulatory requirements
- **Role**: Claim Adjuster
- **Action**: adjudicate SMP disability claims with automated coverage validation, eligibility evaluation, and regulatory-compliant benefit calculations
- **Value**: SMP claims are processed accurately according to state regulatory requirements, ensuring compliant benefit determinations and appropriate payment approvals

**Description:**

> As a **Claim Adjuster**,
> I want to **adjudicate SMP disability claims with automated coverage validation, eligibility evaluation, and regulatory-compliant benefit calculations**,
> So that **SMP claims are processed accurately according to state regulatory requirements, ensuring compliant benefit determinations and appropriate payment approvals**


**Key Capabilities:**

> 1. System retrieves master policy coverage details matching claim coverage code and plan
> 2. System validates coverage existence, benefit type support, and claim information completeness before adjudication
> 3. System evaluates claim eligibility against policy terms and regulatory requirements
>     3.1 Upon eligibility confirmation, system proceeds to benefit calculations
>     3.2 Upon critical eligibility errors, system halts processing and denies claim
> 4. System calculates covered weekly earnings, minimum/maximum benefit thresholds, gross benefit amounts (core and buy-up), and applies rounding rules
> 5. System determines elimination period through date, maximum benefit start/end dates, benefit duration, and generates approval periods with accumulator validation
> 6. System produces settlement result with taxable percentage and final validation checks


**Acceptance Criteria:**

> 1. **Given** a claim with valid SMP coverage code and plan, **When** adjudication initiates, **Then** system retrieves matching master policy coverage and proceeds to validation
> 2. **Given** missing coverage or unsupported benefit type, **When** validation executes, **Then** system returns critical error and marks claim ineligible without further processing
> 3. **Given** an eligible claim passing validation, **When** benefit calculation executes, **Then** system computes weekly earnings, gross benefit amounts (core and buy-up), and applies minimum/maximum thresholds per regulatory rules
> 4. **Given** MAPML coverage type, **When** benefit calculation occurs, **Then** system calculates both low and high benefit amounts per specialized logic
> 5. **Given** completed benefit calculations, **When** approval period generation executes, **Then** system produces approval periods, calculates total benefit duration in days (approved periods only), and validates against accumulator limits
> 6. **Given** calculation or validation failures at any stage, **When** critical errors occur, **Then** system halts adjudication and prevents settlement result creation


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=610902014"
> ]

---

#### Feature: As a Claims Adjuster, I want to calculate Gross Benefit Amount (GBA) for disability claims including minimum, maximum, and weekly amounts, so that benefit payments comply with policy limits
- **Role**: Claim Adjuster
- **Action**: calculate and validate Gross Benefit Amount (GBA) for disability claims with policy-compliant minimum, maximum, and weekly benefit thresholds
- **Value**: benefit payments are accurately computed, comply with policy limits, and maintain regulatory and contractual obligations

**Description:**

> As a **Claim Adjuster**,
> I want to **calculate and validate Gross Benefit Amount (GBA) for disability claims with policy-compliant minimum, maximum, and weekly benefit thresholds**,
> So that **benefit payments are accurately computed, comply with policy limits, and maintain regulatory and contractual obligations**


**Key Capabilities:**

> 1. System evaluates claimant eligibility against policy criteria and coverage conditions
> 2. System calculates Gross Benefit Amount using configured formulas, including minimum and maximum thresholds
> 3. System applies proration factors when coverage periods are partial or benefit adjustments are required
>     3.1 When benefit duration exceeds policy limits, system validates against accumulator thresholds
> 4. System computes taxable percentage of benefit payments per regulatory requirements
> 5. System validates adjudication results against business rules to prevent inconsistent decisions
> 6. System generates payment line items and finalizes benefit payment structure


**Acceptance Criteria:**

> 1. **Given** a claimant meets eligibility criteria, **When** benefit calculation is triggered, **Then** system computes GBA within configured minimum and maximum policy limits
> 2. **Given** partial coverage periods exist, **When** proration is applied, **Then** system adjusts benefit amounts proportionally
> 3. **Given** adjudication results are generated, **When** validation rules execute, **Then** system prevents processing of inconsistent or invalid decisions
> 4. **Given** benefit amounts are calculated, **When** taxable percentage is computed, **Then** system accurately determines tax-subject portions per regulations
> 5. **Given** benefit duration tracking is active, **When** limits are approached, **Then** system enforces accumulator thresholds
> 6. **Given** all calculations pass validation, **When** payment items are generated, **Then** system produces complete and compliant payment records


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=477468931"
> ]

---

#### Feature: As a Claims Adjuster, I want to adjudicate Long-Term Disability (LTD) claims with COLA adjustments and additional benefits, so that long-term disability benefits are calculated with cost-of-living adjustments and survivor benefits
- **Role**: Claim Adjuster
- **Action**: adjudicate Long-Term Disability claims with cost-of-living adjustments and survivor benefits
- **Value**: claimants receive accurate long-term disability benefits that reflect cost-of-living increases and comprehensive coverage including survivor benefits

**Description:**

> As a **Claim Adjuster**,
> I want to **adjudicate Long-Term Disability claims with cost-of-living adjustments and survivor benefits**,
> So that **claimants receive accurate long-term disability benefits that reflect cost-of-living increases and comprehensive coverage including survivor benefits**


**Key Capabilities:**

> 1. System validates technical requirements and halts adjudication upon critical errors preventing claim processing
> 2. System calculates elimination period and comprehensive financial parameters including covered earnings, benefit amounts, taxable percentages, and disability-related attributes
> 3. System evaluates insured eligibility for benefits and manages manually entered approval periods
> 4. System determines maximum benefit period by calculating end dates based on both duration limits and age restrictions, selecting the greater value
>     4.1 Upon non-payable approval periods, system extends maximum benefit end date if periods fall within current calculated end date
> 5. System executes cost-of-living adjustment calculations and pre-disability earnings indexing
> 6. System validates adjudication results and updates eligibility status to not eligible when critical errors detected without override


**Acceptance Criteria:**

> 1. **Given** claim meets technical requirements, **when** adjudication initiates, **then** system calculates elimination period and all required financial attributes without critical errors
> 2. **Given** financial attributes calculated, **when** eligibility evaluation executes, **then** system determines initial eligibility status based on coverage rules
> 3. **Given** maximum benefit duration and age parameters exist, **when** benefit period calculates, **then** system determines maximum benefit end date as greater of duration-based or age-based calculations
> 4. **Given** non-payable approval periods exist within benefit period, **when** calculating maximum benefit end date, **then** system extends end date by gap durations chronologically
> 5. **Given** cost-of-living parameters configured, **when** COLA calculations execute, **then** system determines adjustment periods and indexed earnings
> 6. **Given** adjudication validation detects critical errors without eligibility override, **when** validation completes, **then** system updates eligibility status to not eligible and records explanations


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=610902016"
> ]

---

#### Feature: As a Claims Adjuster, I want to adjudicate LTD Survivor Benefits based on main benefit eligibility and beneficiary data, so that survivor benefits are properly calculated and paid when the insured passes away
- **Role**: Claim Adjuster
- **Action**: adjudicate survivor benefits eligibility and entitlements when an insured with active LTD coverage passes away
- **Value**: survivor beneficiaries receive accurate and timely benefit payments in accordance with policy provisions and main benefit status

**Description:**

> As a **Claim Adjuster**,
> I want to **adjudicate survivor benefits eligibility and entitlements when an insured with active LTD coverage passes away**,
> So that **survivor beneficiaries receive accurate and timely benefit payments in accordance with policy provisions and main benefit status**.


**Key Capabilities:**

> 1. Upon triggering event (initial data entry, data modification, main benefit re-adjudication, or policy refresh), system initiates survivor benefit adjudication process
> 2. System evaluates eligibility against main LTD benefit status and beneficiary information
> 3. When critical errors exist and no manual override applies, system marks benefit as not eligible and halts adjudication
> 4. When eligibility criteria are satisfied or manually overridden, system proceeds with benefit calculation and status updates
> 5. If benefit is cancelled, system locks coverage and prevents propagation, re-adjudication, and payment scheduling until cancellation is reversed
> 6. System finalizes eligibility determination and updates benefit status accordingly


**Acceptance Criteria:**

> 1. **Given** survivor benefit data is newly entered, **When** adjudication is triggered, **Then** system evaluates eligibility and updates benefit status
> 2. **Given** beneficiary or notes data is modified, **When** change is saved, **Then** system re-adjudicates survivor benefit automatically
> 3. **Given** main LTD benefit is re-adjudicated, **When** main adjudication completes, **Then** survivor benefit is re-evaluated based on updated main benefit status
> 4. **Given** critical errors exist without override, **When** eligibility is evaluated, **Then** system marks benefit as not eligible and prevents further adjudication
> 5. **Given** benefit is cancelled, **When** any propagation or re-adjudication event occurs, **Then** system maintains locked status and skips all processing
> 6. **Given** eligibility is confirmed, **When** adjudication completes successfully, **Then** system updates benefit status and enables payment processing


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=778306438"
> ]

---

#### Feature: As a Claims Operations Manager, I want to automatically set 'Future Claim' sub-status for disability claims, so that claims with future effective dates are properly categorized and tracked
- **Role**: Claim Adjuster
- **Action**: automatically categorize and track disability claims with future effective dates through system-driven sub-status assignment
- **Value**: claims requiring deferred processing are properly identified and managed without manual intervention, improving operational efficiency and reducing tracking errors

**Description:**

> As a **Claim Adjuster**,
> I want to **automatically categorize and track disability claims with future effective dates through system-driven sub-status assignment**,
> So that **claims requiring deferred processing are properly identified and managed without manual intervention, improving operational efficiency and reducing tracking errors**


**Key Capabilities:**

> 1. System evaluates disability claim eligibility and temporal attributes during intake and adjudication workflow
> 2. Upon detection of future effective dates or predefined deferral conditions, automated business rules trigger sub-status assignment
> 3. System applies 'Future Claim' sub-status flag to categorize claims requiring deferred processing
> 4. Claim enters monitoring queue for future activation based on effective date thresholds
> 5. System validates adjudication results and prevents premature benefit calculation or payment generation
> 6. User is able to track and report on future claims through standardized sub-status filtering


**Acceptance Criteria:**

> 1. **Given** a disability claim with effective date beyond current processing date, **When** eligibility evaluation completes, **Then** system automatically assigns 'Future Claim' sub-status
> 2. **Given** 'Future Claim' sub-status is set, **When** benefit calculation is attempted, **Then** system defers payment item generation until effective date threshold is met
> 3. **Given** multiple claims with future dates, **When** queried by sub-status, **Then** system returns all claims flagged as 'Future Claim' for tracking purposes
> 4. **Given** claim reaches effective date threshold, **When** system performs scheduled review, **Then** 'Future Claim' sub-status is automatically removed and adjudication proceeds
> 5. **Given** invalid adjudication results, **When** validation rules execute, **Then** system prevents status advancement regardless of effective date


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=477468931"
> ]

---

### Epic: Event Case Intake & Multi-Claim Management

#### Feature: As a Claims Adjuster, I want to submit an Event Case and have the system automatically retrieve applicable policies based on Event Date and customer/member registry, so that I can efficiently process claims without manual policy lookup.
- **Role**: Claim Adjuster
- **Action**: Submit an Event Case and automatically retrieve applicable policy versions based on Event Date and customer registry matching, enabling system-driven claim creation across multiple lines of business without manual policy lookup
- **Value**: I can efficiently adjudicate multiple related claims under the correct policy versions, reduce manual errors in policy selection, and accelerate claim intake by leveraging automated policy discovery and eligibility validation

**Description:**

> As a **Claim Adjuster**,
> I want to **submit an Event Case and automatically retrieve applicable policy versions based on Event Date and customer registry matching, enabling system-driven claim creation across multiple lines of business without manual policy lookup**,
> So that **I can efficiently adjudicate multiple related claims under the correct policy versions, reduce manual errors in policy selection, and accelerate claim intake by leveraging automated policy discovery and eligibility validation**


**Key Capabilities:**

> 1. Upon Event Case submission, system searches policies matching customer or member registry and Event Date within policy effective periods, excluding cancelled or expired policies.
> 2. System groups policy versions by number, selects latest version, and validates Event Date against policy term and cancellation transaction dates.
> 3. When creating claims, system determines LOB-specific Date of Loss (Death, Diagnosis, Service Date, or Accident Date) to identify applicable historical policy version.
> 4. System creates claims under correct policy version, placing claims in 'Incomplete' status when Date of Loss conflicts with policy effective dates or archived versions are identified.
> 5. For multi-loss events, system uses earliest Date of Loss for version search but validates each loss individually for eligibility, applying special rules for combined Death and Accident scenarios.


**Acceptance Criteria:**

> 1. **Given** an Event Case with valid Event Date and customer registry, **When** policies exist matching registry and date criteria, **Then** system retrieves all applicable policy versions excluding cancelled or expired policies.
> 2. **Given** multiple policy versions for a policy number, **When** Event Date falls within valid periods, **Then** system selects the latest version and proceeds to claim creation.
> 3. **Given** a claim creation trigger, **When** LOB-specific Date of Loss is determined, **Then** system identifies the exact policy version effective at that Date of Loss.
> 4. **Given** Date of Loss precedes Policy Effective Date or falls in archived version, **When** claim is created, **Then** system sets claim status to 'Incomplete' for manual review.
> 5. **Given** Event Date before any Policy Effective Date, **When** policy search executes, **Then** system prevents claim generation and terminates process.
> 6. **Given** multiple losses in Event Case, **When** determining policy version, **Then** system uses earliest Date of Loss for search but validates each loss individually for eligibility.


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=631127383"
> ]

---

#### Feature: As a Claims Adjuster, I want the system to filter out expired or cancelled policies during policy retrieval, so that only valid policies are considered for claim creation.
- **Role**: Claim Adjuster
- **Action**: automatically filter out expired or cancelled policies during policy retrieval based on event date validation
- **Value**: only valid, active policies are evaluated for claim creation, reducing manual review effort and preventing invalid claim generation

**Description:**

> As a **Claim Adjuster**,
> I want to **automatically filter out expired or cancelled policies during policy retrieval based on event date validation**,
> So that **only valid, active policies are evaluated for claim creation, reducing manual review effort and preventing invalid claim generation**.


**Key Capabilities:**

> 1. Upon event case submission, system retrieves all policies associated with the employer or member registry.
> 2. System validates event date against policy effective date and filters policies where event date precedes effective date.
> 3. System excludes policies where event date exceeds term expiration date or cancellation transaction effective date.
> 4. System selects the latest policy version per policy number and applies date-based filtering rules.
> 5. When event date falls outside valid policy periods, system prevents claim generation.
> 6. System provides filtered list of eligible policies for subsequent claim creation workflow.


**Acceptance Criteria:**

> 1. **Given** event case is submitted, **When** event date precedes policy effective date, **Then** system excludes policy and prevents claim generation.
> 2. **Given** policy has expiration date, **When** event date exceeds expiration date, **Then** system filters out policy from eligible list.
> 3. **Given** policy has cancellation transaction, **When** event date exceeds cancellation effective date, **Then** system excludes policy.
> 4. **Given** multiple policy versions exist, **When** filtering is applied, **Then** system evaluates only the latest version per policy number.
> 5. **Given** all policies fail eligibility filters, **When** retrieval completes, **Then** system terminates claim creation process.
> 6. **Given** policies pass eligibility validation, **When** adjuster reviews results, **Then** only active valid policies appear for claim creation.


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=631127383"
> ]

---

#### Feature: As a Claims Adjuster, I want the system to locate the correct policy version based on the Date of Loss for Life/CI/HI/Accident claims, so that claims are created against the appropriate policy version in effect at the time of loss.
- **Role**: Claim Adjuster
- **Action**: automatically locate and validate the applicable policy version based on the line-of-business-specific Date of Loss
- **Value**: claims are adjudicated against the accurate policy terms in effect at the time of loss, ensuring coverage accuracy and reducing manual research effort

**Description:**

> As a **Claim Adjuster**,
> I want to **automatically locate and validate the applicable policy version based on the line-of-business-specific Date of Loss**,
> So that **claims are adjudicated against the accurate policy terms in effect at the time of loss, ensuring coverage accuracy and reducing manual research effort**.


**Key Capabilities:**

> 1. Upon Event Case submission, system retrieves eligible policies using Event Date and member/employer identifiers, filtering for active coverage periods
> 2. System groups policies by number and selects latest version, excluding expired or cancelled policies
> 3. When creating claim, system applies line-specific Date of Loss criteria (Death Date for Term Life, Diagnosis Date for CI, Service Date for HI, Accident Date for Accident)
> 4. System locates exact policy version where transaction effective date precedes the Date of Loss
>     4.1 If Date of Loss precedes policy effective date, claim is created in Incomplete status
>     4.2 If Date of Loss falls in archived version, claim is created in Incomplete status
> 5. For multiple losses, system uses earliest Date of Loss for version retrieval while validating each loss individually


**Acceptance Criteria:**

> 1. **Given** an Event Case with valid Event Date, **when** submitted, **then** system retrieves all eligible policies matching customer and date criteria with latest versions
> 2. **Given** a Life/CI/HI/Accident claim with Date of Loss, **when** creating claim, **then** system locates policy version where transaction effective date is on or before Date of Loss
> 3. **Given** Date of Loss precedes policy effective date, **when** processing claim, **then** system creates claim in Incomplete status and alerts adjuster
> 4. **Given** Date of Loss falls in archived policy version, **when** processing claim, **then** system creates claim in Incomplete status
> 5. **Given** Event Date precedes policy effective date, **when** submitted, **then** system halts claim generation and notifies user
> 6. **Given** multiple loss dates in single event, **when** processing, **then** system uses earliest date for version location while validating each loss separately


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=631127383"
> ]

---

#### Feature: As a Claims Adjuster, I want the system to handle multi-loss Event Cases by using the earliest Date of Loss for policy version search while validating each loss individually, so that all losses are properly evaluated against the correct policy version.
- **Role**: Claim Adjuster
- **Action**: adjudicate multi-loss event cases using earliest loss date for policy version determination while validating each loss independently
- **Value**: all losses are evaluated against the correct policy version with accurate eligibility determination regardless of multiple loss dates

**Description:**

> As a **Claim Adjuster**,
> I want to **adjudicate multi-loss event cases using earliest loss date for policy version determination while validating each loss independently**,
> So that **all losses are evaluated against the correct policy version with accurate eligibility determination regardless of multiple loss dates**


**Key Capabilities:**

> 1. Upon event case submission, system retrieves applicable policies matching member or employer registry against event date
> 2. System filters policies based on event date eligibility and excludes terminated or cancelled versions
> 3. When claim creation initiates, system identifies policy version using earliest loss date across all losses (death, diagnosis, accident, service dates)
>     3.1 System applies line-of-business specific loss date definitions
> 4. System validates each individual loss date independently for coverage eligibility determination
> 5. Upon validation completion, system creates claims with appropriate status based on policy effective date alignment
>     5.1 If loss date precedes policy effective date, system marks claim incomplete


**Acceptance Criteria:**

> 1. **Given** multiple losses exist in event case, **When** policy version search executes, **Then** system uses earliest loss date while validating each loss date separately for eligibility
> 2. **Given** event date precedes all policy effective dates, **When** event case submits, **Then** system prevents claim generation completely
> 3. **Given** claim loss date falls in archived policy version, **When** claim creates, **Then** system assigns incomplete status
> 4. **Given** death and accident losses coexist, **When** member effectiveness validates, **Then** system applies accident waiting period and creates single term life claim
> 5. **Given** policy version search completes, **When** applicable version identified, **Then** system creates claim linked to correct policy version with appropriate status


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=631127383"
> ]

---

#### Feature: As a Claims Adjuster, I want the system to validate Event Case information against applicability rules and automatically generate appropriate losses and claims, so that claims are created only when all eligibility criteria are met.
- **Role**: Claim Adjuster
- **Action**: validate Event Case information against applicability rules and automatically generate appropriate losses and claims
- **Value**: claims are created only when all eligibility criteria are met, ensuring accuracy and reducing manual processing effort

**Description:**

> As a **Claim Adjuster**,
> I want to **validate Event Case information against applicability rules and automatically generate appropriate losses and claims**,
> So that **claims are created only when all eligibility criteria are met, ensuring accuracy and reducing manual processing effort**.


**Key Capabilities:**

> 1. User completes event case intake and submits loss information for processing
> 2. System retrieves applicable policy version and validates event data against defined eligibility criteria
>     2.1 Upon validation failure or missing policy, system prevents loss and claim creation
> 3. System automatically generates losses and links them to newly created claims per applicability rules
> 4. System evaluates policy plan configuration to determine coverage auto-generation feasibility
>     4.1 When exactly one plan exists, system auto-generates coverages and executes adjudication
>     4.2 When multiple or zero plans exist, coverage creation is deferred for manual intervention
> 5. User reviews auto-generated claims and coverages via event case overview interface
> 6. System executes eligibility checks and calculates benefit amounts automatically


**Acceptance Criteria:**

> 1. **Given** event case meets all applicability criteria, **When** intake is completed, **Then** system generates losses, claims, and coverages per defined rules
> 2. **Given** policy retrieval fails or additional criteria unmet, **When** validation executes, **Then** system prevents claim generation and notifies adjuster
> 3. **Given** policy contains exactly one plan, **When** claim is created, **Then** system auto-generates coverages and triggers adjudication workflow
> 4. **Given** policy contains multiple or zero plans, **When** claim is created, **Then** system creates claim without coverages and requires manual coverage selection
> 5. **Given** claims are auto-generated, **When** adjuster accesses event case, **Then** system displays all linked claims with coverage status
> 6. **Given** coverages exist, **When** adjudication runs, **Then** system validates eligibility and calculates benefit amounts automatically


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=639744020"
> ]

---

#### Feature: As a Claims Adjuster, I want the system to automatically map Event Case intake data to loss data models and generate claims with linked losses, so that manual data entry is eliminated and data consistency is ensured.
- **Role**: Claim Adjuster
- **Action**: automatically transform Event Case intake data into structured losses, claims, and coverages using policy-driven applicability rules
- **Value**: manual data entry is eliminated, data consistency across losses and claims is ensured, and adjudication begins immediately upon intake completion

**Description:**

> As a **Claim Adjuster**,
> I want to **automatically transform Event Case intake data into structured losses, claims, and coverages using policy-driven applicability rules**,
> So that **manual data entry is eliminated, data consistency across losses and claims is ensured, and adjudication begins immediately upon intake completion**.


**Key Capabilities:**

> 1. User completes Event Case intake by selecting loss type and submitting required information.
> 2. System retrieves the applicable policy version based on mapped product codes and validates Event Case data against Additional Criteria rules.
> 3. Upon validation success, system generates losses and maps Event Case data to loss data models automatically.
> 4. System creates claims and links generated losses according to Claim Applicability rules.
> 5. If exactly one plan exists under the policy, system auto-generates coverages; otherwise, coverage generation is deferred.
> 6. System executes auto-adjudication flow, verifying coverage eligibility and calculating gross amounts.


**Acceptance Criteria:**

> 1. **Given** Event Case intake is completed, **When** policy retrieval locates a valid policy version, **Then** system generates losses mapped to the correct loss data model.
> 2. **Given** Additional Criteria are not met, **When** validation executes, **Then** system prevents loss and claim creation and exits the process.
> 3. **Given** multiple or no plans exist under the policy, **When** claim is created, **Then** system defers coverage generation and displays no coverages on Claim Overview.
> 4. **Given** exactly one plan exists, **When** claim is created, **Then** system auto-generates coverages and displays them in the coverage table.
> 5. **Given** coverages are generated, **When** Claim Overview is accessed, **Then** system completes eligibility checks and gross amount calculations.
> 6. **Given** no valid policy is found, **When** policy retrieval fails, **Then** system prevents claim creation and notifies the adjuster.


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=639744020"
> ]

---

#### Feature: As a Claims Adjuster, I want the system to automatically generate coverages under claims when a single plan exists under the policy, so that coverage setup is expedited and ready for adjudication.
- **Role**: Claim Adjuster
- **Action**: leverage automated coverage generation when a policy contains a single plan, enabling immediate adjudication readiness upon claim creation
- **Value**: coverage setup is expedited, manual configuration effort is eliminated, and claims can proceed to adjudication faster with reduced processing time

**Description:**

> As a **Claim Adjuster**,
> I want to **leverage automated coverage generation when a policy contains a single plan, enabling immediate adjudication readiness upon claim creation**,
> So that **coverage setup is expedited, manual configuration effort is eliminated, and claims can proceed to adjudication faster with reduced processing time**.


**Key Capabilities:**

> 1. System retrieves applicable policy version based on claim product mapping and validates event case information against predefined applicability criteria
> 2. Upon successful validation, system generates losses and claims according to applicability rules and data mapping definitions
> 3. When exactly one plan exists under the policy, system automatically generates coverages linked to the claim per coverage automation rules
>     3.1 If multiple or zero plans exist, coverage generation is bypassed and manual setup is required
> 4. System executes auto-adjudication workflow including eligibility verification and benefit calculation for generated coverages
> 5. User accesses claim overview to review auto-generated coverages and adjudication results in coverage table


**Acceptance Criteria:**

> 1. **Given** an event case with valid policy mapping and a single plan, **When** claim intake is completed, **Then** system auto-generates coverages and initiates adjudication without manual intervention
> 2. **Given** a policy with multiple plans, **When** claim creation occurs, **Then** system bypasses coverage generation and displays empty coverage table requiring manual setup
> 3. **Given** event case information fails applicability criteria validation, **When** intake is submitted, **Then** system prevents claim and loss creation and notifies user of validation failure
> 4. **Given** no valid policy is retrieved, **When** intake is processed, **Then** system halts claim generation and exits workflow
> 5. **Given** auto-generated coverages exist, **When** user navigates to claim overview, **Then** system displays coverages with adjudication status and calculated amounts


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=639744020"
> ]

---

#### Feature: As a Claims Adjuster, I want the system to run auto-adjudication checks on auto-generated coverages including eligibility validation and gross amount calculation, so that claims are ready for review without manual adjudication setup.
- **Role**: Claim Adjuster
- **Action**: enable automated claim structure generation with auto-adjudication upon event case intake
- **Value**: claims are ready for review without manual adjudication setup, reducing processing time and ensuring consistency

**Description:**

> As a **Claim Adjuster**,
> I want to **enable automated claim structure generation with auto-adjudication upon event case intake**,
> So that **claims are ready for review without manual adjudication setup, reducing processing time and ensuring consistency**.


**Key Capabilities:**

> 1. Upon completing event case intake, system retrieves applicable policy version and validates against claim applicability rules
> 2. System generates losses, claims, and coverages when event information meets defined criteria and single plan exists under policy
>     2.1 When multiple or zero plans exist, coverage auto-generation is suppressed
> 3. System maps event case data to loss and claim data models according to pre-defined mappings
> 4. System executes auto-adjudication including coverage eligibility validation and gross amount calculation for generated coverages
> 5. User is able to navigate to claim overview and review auto-generated coverage details with adjudication results


**Acceptance Criteria:**

> 1. **Given** event case intake is completed, **When** policy retrieval succeeds and applicability criteria are met, **Then** system generates losses and claims per configured rules
> 2. **Given** exactly one plan exists under the policy, **When** claim is generated, **Then** system auto-generates coverages and executes adjudication checks
> 3. **Given** multiple or zero plans exist, **When** claim is generated, **Then** system suppresses coverage auto-generation and displays empty coverage table
> 4. **Given** policy retrieval fails or criteria are not met, **When** intake is completed, **Then** system prevents claim and loss creation
> 5. **Given** coverages are auto-generated, **When** user views claim overview, **Then** system displays eligibility status and calculated gross amounts


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=639744020"
> ]

---

#### Feature: As a Claims Adjuster, I want the system to create claims in 'Incomplete' status when the Date of Loss falls before policy effective date or in an archived policy version, so that I am alerted to potential coverage gaps requiring investigation.
- **Role**: Claim Adjuster
- **Action**: automatically flag claims with potential coverage gaps when loss dates precede policy inception or fall within archived policy periods
- **Value**: I am immediately alerted to investigate temporal coverage discrepancies before adjudication, reducing erroneous payments and ensuring regulatory compliance

**Description:**

> As a **Claim Adjuster**,
> I want to **automatically flag claims with potential coverage gaps when loss dates precede policy inception or fall within archived policy periods**,
> So that **I am immediately alerted to investigate temporal coverage discrepancies before adjudication, reducing erroneous payments and ensuring regulatory compliance**.


**Key Capabilities:**

> 1. Upon event case submission, system retrieves all policy versions matching member or employer identifiers where event date meets or exceeds policy effective date
> 2. System determines line-of-business-specific date of loss by applying hierarchical date selection rules (earliest diagnostic, service, or incident date)
> 3. System locates applicable policy version by matching transaction effective dates against calculated date of loss
> 4. When date of loss precedes policy effective date, system creates claim in incomplete status and triggers coverage gap alert
> 5. When date of loss falls within archived policy version, system creates claim in incomplete status for manual review
> 6. User is able to access flagged claims with temporal mismatch indicators for investigation workflow


**Acceptance Criteria:**

> 1. **Given** event date precedes all policy effective dates, **When** event case is submitted, **Then** system prevents claim generation and halts processing
> 2. **Given** date of loss precedes policy effective date but event date is valid, **When** claim creation executes, **Then** system generates claim in incomplete status with pre-coverage flag
> 3. **Given** date of loss matches archived policy version transaction date, **When** policy version location completes, **Then** system creates claim in incomplete status for adjuster review
> 4. **Given** multiple loss dates exist in event case, **When** system determines date of loss, **Then** earliest date is used for version matching while all dates undergo individual eligibility validation
> 5. **Given** claim is created in incomplete status due to temporal mismatch, **When** adjuster accesses claim, **Then** system presents coverage gap indicators without requiring external research
> 6. **Given** policy expiration or cancellation date precedes event date, **When** policy retrieval filtering executes, **Then** system excludes expired/cancelled policies from claim association


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=631127383"
> ]

---

#### Feature: As a Claims Adjuster, I want the system to stop claim generation when Event Date is before policy effective date, so that claims are not created for losses occurring before policy inception.
- **Role**: Claim Adjuster
- **Action**: validate policy eligibility before claim creation by comparing event timing against policy effective dates
- **Value**: claims are only generated for losses covered under active policy periods, preventing processing of ineligible claims and reducing adjudication errors

**Description:**

> As a **Claim Adjuster**,
> I want to **validate policy eligibility before claim creation by comparing event timing against policy effective dates**,
> So that **claims are only generated for losses covered under active policy periods, preventing processing of ineligible claims and reducing adjudication errors**.


**Key Capabilities:**

> 1. Upon event case submission, system retrieves applicable policies by matching event date against policy effective dates and customer registry information
> 2. System filters policies where event date precedes policy effective date or exceeds expiration/cancellation dates
> 3. When event date falls before all applicable policy effective dates, system halts claim generation process immediately
> 4. System determines line-of-business-specific date of loss for eligible policies
> 5. Upon identifying policy version mismatches, system creates claim in incomplete status for adjuster review
> 6. System validates each date of loss individually when multiple events exist under single case


**Acceptance Criteria:**

> 1. **Given** event date precedes policy effective date, **When** event case is submitted, **Then** system prevents claim generation and stops processing
> 2. **Given** event date falls within policy coverage period, **When** claim-specific date of loss precedes policy effective date, **Then** system creates claim in incomplete status
> 3. **Given** multiple events exist, **When** earliest date of loss is determined, **Then** system validates each event date individually against coverage periods
> 4. **Given** policy has cancellation transaction, **When** event date exceeds cancellation effective date, **Then** system excludes policy from eligibility
> 5. **Given** policy version is archived, **When** date of loss falls within archived period, **Then** system creates claim in incomplete status requiring manual adjudication


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=631127383"
> ]

---

### Epic: Claim Coverage Configuration & Limits Management

#### Feature: As a Claims Adjuster, I want to add coverages to a claim from the policy's available coverage list, so that I can process multiple benefits for a single claim event
- **Role**: Claim Adjuster
- **Action**: associate and adjudicate multiple policy coverages to a single claim event through systematic validation and calculation workflows
- **Value**: I can process comprehensive benefit entitlements accurately while maintaining policy limits and ensuring regulatory compliance across all coverage types

**Description:**

> As a **Claim Adjuster**,
> I want to **associate and adjudicate multiple policy coverages to a single claim event through systematic validation and calculation workflows**,
> So that **I can process comprehensive benefit entitlements accurately while maintaining policy limits and ensuring regulatory compliance across all coverage types**


**Key Capabilities:**

> 1. User initiates coverage association by selecting from policy-eligible coverage inventory filtered against claim loss type and existing coverages
> 2. System executes automated adjudication workflow validating incident eligibility, policy effective periods, and calculating gross amounts based on configured formulas and limit levels
> 3. Upon validation failure, system enters manual adjudication mode enabling authorized overrides of calculated amounts or unit quantities with privilege enforcement
> 4. System dynamically generates and updates benefit year or calendar year accumulators when coverage incidents span multiple periods or policy boundaries
> 5. User manages coverage lifecycle through cancellation with mandatory reason codes and reversible undo operations that trigger re-adjudication workflows
> 6. System prevents duplicate coverage assignments and enforces remaining limit validations displaying warnings when overridden amounts exceed temporary available balances


**Acceptance Criteria:**

> 1. **Given** eligible policy coverages exist, **When** user initiates coverage addition, **Then** system filters selection by loss type and excludes already-assigned coverages while validating user privileges
> 2. **Given** coverage requires incident date or date range, **When** system validates eligibility, **Then** adjudication prevents future dates and ensures incident falls within policy effective periods per limit level configuration
> 3. **Given** date range is captured, **When** system calculates units, **Then** formula applies (ThroughDate - FromDate + 1) and triggers real-time gross amount recalculation unless override is active
> 4. **Given** authorized override is applied, **When** user modifies gross amount or units, **Then** system bypasses calculation and validates against temporary remaining limits displaying over-limit warnings when applicable
> 5. **Given** coverage spans multiple benefit or calendar years, **When** adjudication completes successfully, **Then** system generates separate accumulators for each period and updates settlement status to approved
> 6. **Given** coverage is cancelled with reason, **When** user executes undo cancellation, **Then** system re-adjudicates eligibility, recalculates amounts, updates accumulators, and removes cancelled sub-status


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=521345837"
> ]

---

#### Feature: As a Claims Adjuster, I want the system to automatically adjudicate and calculate gross amounts when I add a coverage, so that I can quickly determine if the coverage is eligible and payable
- **Role**: Claim Adjuster
- **Action**: automatically adjudicate coverage eligibility and calculate gross amounts upon adding claim coverages
- **Value**: I can efficiently determine coverage eligibility and payable amounts without manual calculation, reducing processing time and errors.

**Description:**

> As a **Claim Adjuster**,
> I want to **automatically adjudicate coverage eligibility and calculate gross amounts upon adding claim coverages**,
> So that **I can efficiently determine coverage eligibility and payable amounts without manual calculation, reducing processing time and errors.**


**Key Capabilities:**

> 1. User initiates coverage selection from policy-filtered available coverages.
> 2. System executes automatic adjudication by validating coverage eligibility against policy effective periods, incident dates, and limit levels.
>     2.1 Upon successful adjudication, system calculates gross amounts based on configured formulas and unit calculations.
>     2.2 When adjudication fails, system enables manual data entry mode for correction.
> 3. System generates and updates accumulators for Benefit Year or Calendar Year limit tracking based on configured limit levels.
> 4. User is able to override calculated amounts when authorized, with system validating overrides against remaining limits.
> 5. System recalculates amounts in real-time when dates or units are modified during editing.
> 6. Upon coverage cancellation or reactivation, system re-adjudicates eligibility and recalculates accumulator impacts.


**Acceptance Criteria:**

> 1. **Given** a coverage is selected for addition, **When** automatic adjudication executes successfully, **Then** system displays approved status with calculated gross amount and updates accumulators.
> 2. **Given** adjudication fails validation rules, **When** system enables manual entry mode, **Then** user can provide required date information and system recalculates upon save.
> 3. **Given** incident dates span multiple calendar or benefit years, **When** coverage is saved, **Then** system generates separate accumulators for each applicable period.
> 4. **Given** user overrides calculated amounts with proper authorization, **When** override value exceeds remaining limits, **Then** system displays over-limit warning but allows save.
> 5. **Given** coverage has issued payments, **When** user attempts editing, **Then** system prevents modification of date fields while allowing other editable attributes.
> 6. **Given** cancelled coverage is reactivated, **When** undo cancellation executes, **Then** system re-adjudicates eligibility and recalculates gross amounts and accumulators.


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=521345837"
> ]

---

#### Feature: As a Claims Adjuster, I want to edit coverage details including dates, gross amounts, and occurrence counts when auto-adjudication fails, so that I can manually correct data and trigger re-adjudication
- **Role**: Claim Adjuster
- **Action**: manually edit and correct coverage details to trigger re-adjudication when automated settlement processing fails
- **Value**: claims are accurately adjudicated and approved despite initial auto-adjudication failures, ensuring proper benefit calculations and timely claim resolution

**Description:**

> As a **Claim Adjuster**,
> I want to **manually edit and correct coverage details to trigger re-adjudication when automated settlement processing fails**,
> So that **claims are accurately adjudicated and approved despite initial auto-adjudication failures, ensuring proper benefit calculations and timely claim resolution**.


**Key Capabilities:**

> 1. Upon auto-adjudication failure, system presents coverage in editable state with validation warnings displayed.
> 2. User is able to correct incident dates, date ranges, and validate coverage falls within policy effective periods and configured benefit/calendar years.
> 3. User is able to override gross amounts and occurrence counts when system calculations are incorrect, with validation against remaining accumulator limits.
>     3.1 System validates overridden values against temporary remaining limits and displays warnings when thresholds exceeded.
>     3.2 When overrides applied, system disables auto-calculation for affected fields.
> 4. User submits corrected coverage data triggering re-adjudication process with eligibility validation, gross amount recalculation, and accumulator updates.
> 5. System generates or updates benefit year and calendar year accumulators based on corrected incident dates and date ranges.
> 6. Upon successful re-adjudication, system updates settlement status to approved and initiates accumulator for certificate policy.


**Acceptance Criteria:**

> 1. **Given** auto-adjudication fails during coverage addition, **When** adjuster accesses coverage record, **Then** system presents editable fields with current validation errors and warnings displayed.
> 2. **Given** adjuster corrects incident date or date range, **When** dates fall within policy effective period and configured limit periods, **Then** system recalculates occurrences and gross amounts accordingly.
> 3. **Given** adjuster overrides gross amount or occurrence count, **When** overridden value exceeds accumulator remaining limits, **Then** system displays over-limit warning but permits save with audit trail.
> 4. **Given** adjuster saves corrected coverage data, **When** all mandatory validations pass, **Then** system executes re-adjudication workflow with eligibility validation and benefit calculations.
> 5. **Given** re-adjudication completes successfully, **When** settlement status updates to approved, **Then** system generates appropriate benefit/calendar year accumulators and updates certificate policy accumulators.
> 6. **Given** validation failures occur during save, **When** mandatory data incomplete or dates invalid, **Then** system prevents submission and displays specific error messages for correction.


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=521345837"
> ]

---

#### Feature: As a Claims Adjuster, I want to view remaining limits and accumulator balances for each coverage, so that I can understand how much benefit remains available under policy limits
- **Role**: Claim Adjuster
- **Action**: access remaining limit and accumulator balance information for claim coverages
- **Value**: I can determine available benefit capacity under policy limits and make informed adjudication decisions

**Description:**

> As a **Claim Adjuster**,
> I want to **access remaining limit and accumulator balance information for claim coverages**,
> So that **I can determine available benefit capacity under policy limits and make informed adjudication decisions**


**Key Capabilities:**

> 1. User retrieves accumulator information from claim coverage records to assess benefit availability
> 2. System displays limit parameters including maximum allowable amount, utilized benefits, planned reserves, and remaining capacity
> 3. System calculates accumulators based on calendar year periods (Jan 1 - Dec 31) or benefit year periods (policy anniversary cycles)
>     3.1 Upon calendar year limit level, system generates or retrieves accumulators aligned to incident or service date range calendar years
>     3.2 Upon benefit year limit level, system generates or retrieves accumulators aligned to policy effective date anniversary cycles
> 4. When service dates span multiple accumulator periods, system creates separate accumulators for each period involved
> 5. System associates party demographic information to ensure accurate accumulator calculations for the claim subject
> 6. For specific coverage types, user is able to view specialized limit information such as fracture-related remaining benefits


**Acceptance Criteria:**

> 1. **Given** a coverage with calendar year limits, **When** the adjuster accesses remaining limit information, **Then** system displays accumulator balances for each calendar year affected by the claim service dates
> 2. **Given** a coverage with benefit year limits, **When** service dates fall within a policy anniversary period, **Then** system calculates remaining limits based on the correct benefit year cycle
> 3. **Given** service dates spanning multiple accumulator periods, **When** system processes the coverage, **Then** separate accumulators are created for each period with appropriate limit allocations
> 4. **Given** incomplete or invalid date information, **When** system attempts accumulator generation, **Then** system prevents processing and maintains data integrity
> 5. **Given** existing accumulators for the period, **When** adjuster retrieves limit information, **Then** system displays current values without creating duplicate records
> 6. **Given** special coverage types with supplemental limit rules, **When** adjuster views remaining limits, **Then** system presents all applicable limit categories including specialized benefit constraints


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=552020506"
> ]

---

#### Feature: As a Claims Operations Manager, I want the system to automatically generate and manage calendar year and benefit year accumulators based on coverage dates, so that benefit limits are properly tracked across policy periods
- **Role**: Claim Adjuster
- **Action**: automatically generate and manage benefit period accumulators based on coverage effective dates and claim submission timing
- **Value**: benefit limits are accurately tracked across policy periods without manual intervention, ensuring proper claim adjudication and preventing overpayment

**Description:**

> As a **Claim Adjuster**,
> I want to **automatically generate and manage benefit period accumulators based on coverage effective dates and claim submission timing**,
> So that **benefit limits are accurately tracked across policy periods without manual intervention, ensuring proper claim adjudication and preventing overpayment**.


**Key Capabilities:**

> 1. System associates claim subject party data to enable accumulator calculations upon coverage adjudication.
> 2. Upon saving coverage with per-calendar-year limits, system evaluates incident or date range against existing accumulators and generates new calendar-year accumulators when none exist for the relevant year(s).
>     2.1 When date ranges cross calendar years, system creates separate accumulators for each year.
> 3. Upon saving coverage with per-benefit-year limits, system validates dates against policy effective date and generates benefit-year accumulators anchored to policy anniversary cycles.
>     3.1 If claim dates precede policy effective date, coverage is deemed ineligible and no accumulator is created.
> 4. System displays remaining limit metrics (used, planned, remaining) for each applicable limit level.
> 5. When fracture-related accident coverage exists, system presents specialized group fracture limit information.


**Acceptance Criteria:**

> 1. **Given** a coverage with per-calendar-year limits and claim dates within 2023, **when** adjudication is saved, **then** system generates a 2023 calendar-year accumulator if none exists.
> 2. **Given** a coverage with date range spanning 12/15/2023-01/10/2024, **when** adjudication is saved, **then** system creates distinct accumulators for both 2023 and 2024.
> 3. **Given** a coverage with per-benefit-year limits and policy effective date of 05/25/2019, **when** claim with incident date 06/01/2022 is saved, **then** system generates accumulator for benefit year 05/25/2022-05/24/2023.
> 4. **Given** claim dates precede policy effective date, **when** validation occurs, **then** coverage is marked ineligible and no accumulator is created.
> 5. **Given** existing accumulators for a benefit period, **when** another claim for same period is adjudicated, **then** system reuses existing accumulator without duplication.
> 6. **Given** user accesses remaining limit information, **when** data is retrieved, **then** system displays current used, planned, and remaining values for all applicable limit levels.


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=552020506"
> ]

---

#### Feature: As a Claims Adjuster, I want to cancel a coverage and specify a cancellation reason, so that I can remove erroneous or duplicate coverage records and adjust accumulator reserves accordingly
- **Role**: Claim Adjuster
- **Action**: cancel or reinstate coverage records with appropriate reason documentation and financial adjustments
- **Value**: erroneous or duplicate coverage records are removed, accumulator reserves are accurately adjusted, and financial integrity is maintained throughout the claim lifecycle

**Description:**

> As a **Claim Adjuster**,
> I want to **cancel or reinstate coverage records with appropriate reason documentation and financial adjustments**,
> So that **erroneous or duplicate coverage records are removed, accumulator reserves are accurately adjusted, and financial integrity is maintained throughout the claim lifecycle**.


**Key Capabilities:**

> 1. User is able to initiate coverage cancellation by marking coverage status and documenting mandatory business justification
> 2. Upon cancellation, system releases reserved amounts back to remaining coverage limits based on payment allocation status
>     2.1 When no payments exist, reserved amounts return to available limits
>     2.2 When payments are made, system generates overpayment balances
> 3. System triggers payment rescheduling process and manages visibility of approved payment records
> 4. System locks cancelled coverage from policy updates, claim propagation, and re-adjudication until reversal
> 5. User is able to reverse cancellation, triggering settlement re-adjudication and accumulator re-reservation
> 6. Upon reversal, system restores payment records and clears overpayment balances based on original payment status


**Acceptance Criteria:**

> 1. **Given** coverage cancellation is initiated, **When** cancellation reason is provided, **Then** system marks coverage as cancelled and locks it from further processing
> 2. **Given** cancelled coverage has no payment allocations, **When** unreserve process executes, **Then** reserved amounts return to remaining limits
> 3. **Given** cancelled coverage has approved payments, **When** unreserve process executes, **Then** system generates overpayment balances equal to payment amounts
> 4. **Given** coverage is locked as cancelled, **When** policy or claim updates occur, **Then** system prevents re-adjudication until cancellation is reversed
> 5. **Given** cancellation reversal is initiated, **When** system re-adjudicates settlements, **Then** accumulator limits are recalculated and reserved amounts restored
> 6. **Given** reversal completes with issued payments, **When** payment records are restored, **Then** overpayment balances are cleared and payment visibility is restored


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=699244693"
> ]

---

#### Feature: As a Claims Adjuster, I want to undo a coverage cancellation and have the system re-adjudicate the settlement, so that I can restore a previously cancelled coverage with updated calculations
- **Role**: Claim Adjuster
- **Action**: reverse a coverage cancellation and trigger automated settlement re-adjudication with updated financial calculations
- **Value**: previously cancelled coverages can be restored with accurate reserve allocations, payment schedules, and accumulator limits without manual recalculation

**Description:**

> As a **Claim Adjuster**,
> I want to **reverse a coverage cancellation and trigger automated settlement re-adjudication with updated financial calculations**,
> So that **previously cancelled coverages can be restored with accurate reserve allocations, payment schedules, and accumulator limits without manual recalculation**


**Key Capabilities:**

> 1. User initiates reversal of cancelled coverage status and clears mandatory cancellation reason
> 2. System re-adjudicates settlement to recalculate eligibility, gross amounts, and accumulator limits
>     2.1 Upon override flag activation, system displays user-defined eligibility and gross amounts instead of recalculated values
> 3. System restores accumulator reserves for approved settlements without payment allocations
> 4. When payments were approved but not issued before cancellation, system restores reserves and requires manual payment recreation
> 5. When payments were issued before cancellation, system clears overpayment balances while preserving issued payment records and used accumulator amounts
> 6. System triggers payment rescheduling and displays previously hidden payment records


**Acceptance Criteria:**

> 1. **Given** coverage was cancelled without payment issuance, **When** reversal is executed, **Then** system restores reserved amounts to accumulators and reduces remaining limits accordingly
> 2. **Given** coverage was cancelled after payment issuance, **When** reversal is executed, **Then** system clears overpayment balance to zero and preserves issued payment records unchanged
> 3. **Given** override flag is inactive, **When** re-adjudication occurs, **Then** system recalculates eligibility and gross amounts based on current policy and accumulator limits
> 4. **Given** override flag is active, **When** re-adjudication occurs, **Then** system displays manually overridden eligibility status and gross amounts
> 5. **Given** no payment allocations exist, **When** reversal is executed, **Then** system skips payment rescheduling and balance adjustment processes
> 6. **Given** reversal completes successfully, **When** user views coverage, **Then** system unlocks coverage for future adjudication and updates


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=699244693"
> ]

---

#### Feature: As a Claims Adjuster, I want the system to calculate gross amounts based on policy limits, accumulator balances, and coverage-specific formulas, so that benefit payments are accurate and compliant with policy terms
- **Role**: Claim Adjuster
- **Action**: have the system automatically calculate settlement gross amounts using policy limits, accumulator balances, and coverage-specific formulas
- **Value**: benefit payments are accurate, compliant with policy terms, and calculated consistently without manual computation errors

**Description:**

> As a **Claim Adjuster**,
> I want to **have the system automatically calculate settlement gross amounts using policy limits, accumulator balances, and coverage-specific formulas**,
> So that **benefit payments are accurate, compliant with policy terms, and calculated consistently without manual computation errors**


**Key Capabilities:**

> 1. System evaluates whether gross amount is manually overridden and bypasses calculation when override is active
> 2. System retrieves policy data including face value, benefit amounts, and applicable accumulator balances
> 3. System calculates accumulator remaining amounts based on coverage and group-level limits
> 4. System applies coverage-specific formulas to determine gross amount using minimum thresholds between face amounts and remaining limits
>     4.1 When unit override indicator is true, system uses manually specified unit values
>     4.2 When unit override indicator is false, system calculates units as minimum of specified units and remaining amounts
> 5. System persists calculated gross amount to settlement record for payment processing


**Acceptance Criteria:**

> 1. **Given** no manual override is set, **When** system calculates gross amount, **Then** result equals minimum of face amount and remaining accumulator balance
> 2. **Given** gross amount override is enabled, **When** adjuster provides override value, **Then** system saves override amount directly and skips formula calculation
> 3. **Given** policy has face value and accumulator limits, **When** calculation executes, **Then** system applies coverage-specific formula with correct data inputs
> 4. **Given** multiple accumulator levels exist (coverage and group), **When** determining remaining amount, **Then** system uses minimum of coverage and group remaining balances
> 5. **Given** unit override indicator is false, **When** calculating units, **Then** system applies minimum logic between specified units and remaining amounts
> 6. **Given** calculation completes successfully, **When** result is persisted, **Then** gross amount is available for downstream payment processing


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=700748712"
> ]

---

#### Feature: As a Claims Adjuster, I want to add recurring coverages (such as Coma benefits) with date range validation and maximum limit enforcement, so that multi-month benefits are properly tracked and do not exceed policy maximums
- **Role**: Claim Adjuster
- **Action**: configure and validate recurring coverages with date range enforcement and policy maximum tracking
- **Value**: multi-period benefits are accurately tracked, prevent overpayment, and comply with policy limits without manual calculation errors

**Description:**

> As a **Claim Adjuster**,
> I want to **configure and validate recurring coverages with date range enforcement and policy maximum tracking**,
> So that **multi-period benefits are accurately tracked, prevent overpayment, and comply with policy limits without manual calculation errors**.


**Key Capabilities:**

> 1. User is able to select eligible recurring coverage types filtered by active policy terms and existing claim coverages
> 2. Upon coverage selection, system initiates automated adjudication workflow based on loss classification rules
> 3. User is able to define benefit period boundaries with system validation against policy maximum duration limits
>     3.1 When benefit period exceeds configured policy maximum, system prevents submission with limit notification
>     3.2 When multiple benefit periods accumulate beyond remaining available duration, system flags non-eligibility
> 4. System calculates benefit amounts automatically after temporal validation succeeds, applying payment frequency rules
> 5. When adding subsequent benefit periods, system validates against approved settlement date ranges to prevent temporal overlaps
> 6. System retrieves and enforces policy-level maximum limits through integrated policy data services


**Acceptance Criteria:**

> 1. **Given** a claim requires recurring coverage, **When** the adjuster initiates coverage addition, **Then** system presents only policy-eligible coverages excluding already-added types
> 2. **Given** benefit period boundaries are defined, **When** the period exceeds policy maximum duration, **Then** system prevents submission and displays remaining allowable duration
> 3. **Given** multiple benefit periods exist, **When** cumulative duration exceeds policy lifetime maximum, **Then** system adjudicates as non-eligible with accumulated limit violation notification
> 4. **Given** approved settlements exist for the coverage, **When** new benefit period overlaps existing approved dates, **Then** system prevents creation with temporal conflict notification
> 5. **Given** temporal validation succeeds, **When** benefit period is saved, **Then** system calculates financial amounts based on configured payment frequency rules
> 6. **Given** benefit periods require modification, **When** date range is incomplete, **Then** system prevents submission until required temporal data is provided


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=639732020"
> ]

---

#### Feature: As a Claims Adjuster, I want to view and override coverage eligibility results when validation fails, so that I can manually approve coverages that fail automated eligibility checks when appropriate
- **Role**: Claim Adjuster
- **Action**: review failed automated eligibility validations and apply manual overrides when business judgment warrants coverage approval
- **Value**: claims with legitimate coverage can be processed even when automated rules produce false negatives, ensuring customers receive appropriate benefits while maintaining control over exceptions

**Description:**

> As a **Claim Adjuster**,
> I want to **review failed automated eligibility validations and apply manual overrides when business judgment warrants coverage approval**,
> So that **claims with legitimate coverage can be processed even when automated rules produce false negatives, ensuring customers receive appropriate benefits while maintaining control over exceptions**


**Key Capabilities:**

> 1. Review eligibility adjudication outcomes for coverages at case and claim levels with detailed validation failure explanations
> 2. Assess whether failed validations represent true ineligibility or system limitation requiring override
> 3. Correct underlying claim or policy data elements to resolve eligibility failures and trigger automatic re-validation
> 4. Apply manual eligibility override when authorized, selecting alternative eligibility determination with documented justification
>     4.1 When override privilege unavailable, user can only attempt data correction approach
> 5. System prevents automatic re-validation once override applied, preserving manual decision until explicitly removed
> 6. Remove existing overrides to restore automated eligibility determination with immediate re-validation


**Acceptance Criteria:**

> 1. **Given** eligibility validation has failed, **When** adjuster reviews coverage status, **Then** system presents detailed failure reasons enabling informed override decisions
> 2. **Given** adjuster possesses override privilege, **When** override is applied, **Then** system accepts manual eligibility determination and suppresses automatic re-validation on subsequent updates
> 3. **Given** override is not appropriate, **When** adjuster modifies claim data, **Then** system automatically re-executes validation rules and updates eligibility status
> 4. **Given** adjuster lacks override privilege, **When** viewing ineligible coverage, **Then** system prevents override capability while permitting data correction attempts
> 5. **Given** override exists, **When** adjuster removes override, **Then** system immediately re-validates eligibility using current automated rules
> 6. **Given** override applied, **When** reviewing coverage, **Then** system clearly indicates manual override status distinguishing from automated determinations


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=557948275"
> ]

---

#### Feature: As a Claims Adjuster, I want to view face value information for different product types on the claim overview, so that I can verify the correct benefit amount is being used for coverage calculations
- **Role**: Claim Adjuster
- **Action**: view and verify product-specific face value information on claim overview
- **Value**: I can ensure correct benefit amounts are applied during coverage calculations based on the product line

**Description:**

> As a **Claim Adjuster**,
> I want to **view and verify product-specific face value information on claim overview**,
> So that **I can ensure correct benefit amounts are applied during coverage calculations based on the product line**


**Key Capabilities:**

> 1. System identifies the policy product type upon claim overview access
> 2. System routes to product-specific face value processing logic
>     2.1 Term Life products apply GTL face value rules
>     2.2 Critical Illness products apply CI face value rules
>     2.3 Individual Permanent Life products apply IWL face value rules
>     2.4 Accident products apply accidental death amount rules
> 3. System calculates and displays benefit amount according to product-specific business rules
> 4. User is able to verify the displayed face value aligns with policy coverage terms


**Acceptance Criteria:**

> 1. **Given** a claim for Term Life product, **When** adjuster accesses claim overview, **Then** system displays face value per GTL calculation rules
> 2. **Given** a claim for Critical Illness product, **When** adjuster accesses claim overview, **Then** system displays face value per CI calculation rules
> 3. **Given** a claim for Individual Permanent Life product, **When** adjuster accesses claim overview, **Then** system displays face value per IWL calculation rules
> 4. **Given** a claim for Accident product, **When** adjuster accesses claim overview, **Then** system displays accidental death amount per AH rules
> 5. **Given** policy lacks face value coverage, **When** adjuster accesses claim overview, **Then** system prevents display of undefined benefit amounts


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=797639863"
> ]

---

### Epic: Claim Recalculation & Payment Adjustment

#### Feature: As a Claims Adjuster, I want to recalculate claim settlements when plan selection changes, so that coverage eligibility and gross amounts are accurately updated
- **Role**: Claim Adjuster
- **Action**: recalculate claim settlements when plan selection changes
- **Value**: coverage eligibility and financial settlements remain accurate and compliant with updated policy terms

**Description:**

> As a **Claim Adjuster**,
> I want to **recalculate claim settlements when plan selection changes**,
> So that **coverage eligibility and financial settlements remain accurate and compliant with updated policy terms**.


**Key Capabilities:**

> 1. User modifies plan selection on an active claim under a master policy containing multiple plans.
> 2. System evaluates existence of prior coverages and settlements.
>     2.1 If no prior coverages exist, system saves the new plan without recalculation.
>     2.2 If coverages exist, system validates settlement eligibility against new plan terms.
> 3. Upon validation, system recalculates gross amounts and updates coverage records, marking invalid coverages as non-eligible and disapproving corresponding settlements.
> 4. System adjusts payment schedules by rescheduling future payments or removing allocations tied to invalid settlements.
> 5. System reconciles actual payments by generating overpayment/underpayment balances when payments have been issued.
> 6. System adjusts accumulators following FIFO rules when balances are recovered through payment actions.


**Acceptance Criteria:**

> 1. **Given** a claim with existing coverages, **when** the user changes the plan selection, **then** the system validates all settlements against the new plan and recalculates gross amounts.
> 2. **Given** a settlement becomes invalid after plan change, **when** validation completes, **then** the system marks coverage as non-eligible and disapproves the settlement.
> 3. **Given** a valid settlement with scheduled payments, **when** recalculation occurs, **then** the system reschedules payments with updated amounts and post dates.
> 4. **Given** actual payments exist with status Issued/Cleared, **when** settlement amounts change, **then** the system automatically generates overpayment or underpayment balances.
> 5. **Given** no prior coverages exist, **when** plan selection changes, **then** the system saves the new plan without triggering recalculation.
> 6. **Given** balance recovery actions are executed, **when** successful, **then** the system adjusts accumulators following FIFO sequence based on original usage dates.


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=604814795"
> ]

---

#### Feature: As a Claims Adjuster, I want to validate coverage eligibility after plan changes and mark invalid coverages as non-eligible, so that only applicable benefits are processed
- **Role**: Claim Adjuster
- **Action**: validate coverage eligibility after plan modifications and adjust settlements, payments, and accumulators accordingly
- **Value**: only applicable benefits are processed and financial integrity is maintained across plan transitions

**Description:**

> As a Claim Adjuster,
> I want to validate coverage eligibility after plan modifications and adjust settlements, payments, and accumulators accordingly,
> So that only applicable benefits are processed and financial integrity is maintained across plan transitions


**Key Capabilities:**

> 1. User initiates plan selection change for claim under master policy
> 2. System evaluates existing coverage settlements against new plan parameters
>     2.1 When coverages exist in new plan, system triggers automatic readjudication and recalculates benefit amounts
>     2.2 When coverages do not exist in new plan, system marks settlements as non-eligible and disapproves coverage records
> 3. System processes payment schedule adjustments for valid coverages and removes payment allocations for invalid settlements
> 4. Upon identifying actual payments already issued, system generates overpayment or underpayment balances based on payment status
> 5. System adjusts accumulator reserves by calculating gross amount variances and restoring remaining balances
> 6. User is able to manually add new coverages applicable under the revised plan


**Acceptance Criteria:**

> 1. **Given** existing coverages under original plan, **When** plan change is initiated, **Then** system evaluates all settlements for eligibility under new plan
> 2. **Given** coverage exists in new plan, **When** readjudication occurs, **Then** system updates existing settlement record with recalculated benefit amounts without creating duplicates
> 3. **Given** coverage does not exist in new plan, **When** system processes invalid settlement, **Then** settlement is marked disapproved, eligibility set to non-eligible, and edit capabilities disabled
> 4. **Given** active payment schedule exists, **When** coverage becomes invalid, **Then** system removes associated payment allocations and regenerates schedule for valid coverages
> 5. **Given** actual payment was issued, **When** settlement amount changes or becomes invalid, **Then** system automatically generates balance adjustment transactions
> 6. **Given** no existing payments processed, **When** accumulator adjustment executes, **Then** system restores amount variance to remaining balance following calculation rules


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=604814795"
> ]

---

#### Feature: As a Claims Adjuster, I want to automatically reschedule payments when coverage changes occur, so that payment allocations reflect the updated claim information
- **Role**: Claim Adjuster
- **Action**: automatically reschedule and adjust payment allocations when policy plan selections change on claims
- **Value**: payment schedules and disbursements accurately reflect current coverage entitlements without manual intervention, preventing overpayments and ensuring compliance

**Description:**

> As a **Claim Adjuster**,
> I want to **automatically reschedule and adjust payment allocations when policy plan selections change on claims**,
> So that **payment schedules and disbursements accurately reflect current coverage entitlements without manual intervention, preventing overpayments and ensuring compliance**.


**Key Capabilities:**

> 1. Upon plan selection change, system triggers recalculation when prior coverages exist and validates settlement eligibility under new plan
> 2. System refreshes valid settlements by recalculating gross amounts, executing eligibility validation, and generating updated payment schedules
> 3. System invalidates settlements when coverage no longer applies, setting records to non-eligible and removing payment allocations
> 4. When actual payments exist, system automatically generates overpay/underpay balances for successfully disbursed payments (Issued/Cleared/StopRequested statuses)
> 5. System executes accumulator adjustments following FIFO rules, clawing back used amounts to remaining balances during recovery actions
> 6. User is able to manually add new coverages for the updated plan following automated recalculation completion


**Acceptance Criteria:**

> 1. **Given** existing coverages on a claim, **When** plan selection changes, **Then** system triggers recalculation and validates all settlement eligibility against new plan rules
> 2. **Given** valid settlements under new plan, **When** recalculation completes, **Then** system regenerates payment schedules with updated amounts and post dates
> 3. **Given** invalid settlements after plan change, **When** coverage no longer applies, **Then** system sets records to non-eligible and removes associated payment allocations
> 4. **Given** actual payments with Issued/Cleared/StopRequested status, **When** settlement amounts change, **Then** system automatically generates overpay/underpay balances
> 5. **Given** balance recovery actions initiated, **When** adjustments process, **Then** system applies FIFO rules to claw back used amounts to remaining balances
> 6. **Given** no existing coverages prior to plan change, **When** plan is saved, **Then** system saves new plan without triggering recalculation processes


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=604814795"
> ]

---

#### Feature: As a Claims Adjuster, I want to automatically generate balance adjustments (overpay/underpay) when issued payments exist and claim amounts change, so that payment discrepancies are captured and resolved
- **Role**: Claim Adjuster
- **Action**: automatically trigger claim recalculation and payment adjustment processes when plan selection changes on a claim with existing settlements and payments
- **Value**: payment discrepancies are identified and resolved through systematic balance generation, ensuring accurate financial reconciliation and policy compliance

**Description:**

> As a **Claim Adjuster**,
> I want to **automatically trigger claim recalculation and payment adjustment processes when plan selection changes on a claim with existing settlements and payments**,
> So that **payment discrepancies are identified and resolved through systematic balance generation, ensuring accurate financial reconciliation and policy compliance**


**Key Capabilities:**

> 1. Upon plan selection change, system triggers recalculation if coverages exist and evaluates settlement validity
> 2. For valid settlements, system re-adjudicates coverage, recalculates gross amounts, and regenerates payment schedules with updated terms
>     2.1 System runs eligibility validation and updates coverage records without creating duplicates
> 3. For invalid settlements (coverage no longer exists in new plan), system marks coverage non-eligible and removes payment allocations
> 4. When issued/cleared payments exist, system automatically generates overpay/underpay balances reflecting paid amount discrepancies
> 5. System adjusts accumulators following FIFO rules, recovering used amounts back to remaining when balances are resolved
> 6. User can manually add new coverages aligned to the updated plan


**Acceptance Criteria:**

> 1. **Given** plan changes with existing coverages, **When** recalculation triggers, **Then** system re-adjudicates valid settlements and recalculates gross amounts automatically
> 2. **Given** invalid settlements after plan change, **When** coverage no longer exists in new plan, **Then** system marks coverage non-eligible and prevents further edits
> 3. **Given** existing payment schedule, **When** settlement validity changes, **Then** system removes invalid allocations or regenerates schedule with new amounts
> 4. **Given** issued/cleared payments exist, **When** settlement becomes invalid or amounts change, **Then** system generates overpay/underpay balance equal to paid amount discrepancy
> 5. **Given** no actual payments issued, **When** settlement changes, **Then** accumulator adjusts used amounts without generating balances
> 6. **Given** balance recovery action completes, **When** overpay/underpay resolved, **Then** accumulator claws back amounts following FIFO rule


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=604814795"
> ]

---

#### Feature: As a Claims Adjuster, I want to adjust accumulators when claim amounts change and no payments have been issued, so that remaining benefit amounts are accurately maintained
- **Role**: Claim Adjuster
- **Action**: recalculate claim financial amounts and adjust benefit accumulators when plan selections or coverage determinations change prior to payment issuance
- **Value**: benefit limits and remaining coverage amounts remain accurate and reflect the current adjudication status, preventing incorrect future claim payments

**Description:**

> As a **Claim Adjuster**,
> I want to **recalculate claim financial amounts and adjust benefit accumulators when plan selections or coverage determinations change prior to payment issuance**,
> So that **benefit limits and remaining coverage amounts remain accurate and reflect the current adjudication status, preventing incorrect future claim payments**.


**Key Capabilities:**

> 1. Upon plan selection modification on an existing claim, system evaluates whether existing coverage records require readjudication
>     1.1 When no prior coverage exists, system saves plan change without financial recalculation
> 2. System re-adjudicates settlements and recalculates gross amounts based on updated plan provisions
>     2.1 When coverage remains valid under new plan, system updates existing coverage record and validates continued eligibility
>     2.2 When coverage becomes invalid, system marks settlement as non-eligible and prevents further processing
> 3. System adjusts benefit accumulators using variance between original and recalculated amounts when no payments have been issued
> 4. Upon successful balance recovery actions, system performs accumulator clawback following first-in-first-out sequence across coverage types


**Acceptance Criteria:**

> 1. **Given** a claim with existing coverage and no issued payments, **When** plan selection changes and coverage remains valid, **Then** system recalculates gross amounts and adjusts accumulators to reflect the difference between original and revised benefit utilization
> 2. **Given** a claim undergoing plan change, **When** coverage becomes invalid under the new plan, **Then** system marks settlement as non-eligible and reverses accumulator impact by restoring previously used amounts to remaining benefits
> 3. **Given** multiple coverage types with outstanding balance amounts, **When** balance recovery action executes successfully, **Then** system claws back recovered amounts from accumulators following first-in-first-out rule across all affected coverages
> 4. **Given** a claim with issued or cleared payments, **When** financial recalculation occurs, **Then** system generates overpayment or underpayment balance but does not adjust accumulators
> 5. **Given** a claim with scheduled but unissued payments, **When** adjudication changes invalidate coverage, **Then** system removes affected payment allocations from the schedule and adjusts accumulators accordingly


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=604814795"
> ]

---

#### Feature: As a Claims Adjuster, I want to clawback accumulator amounts using First In First Out when balance actions recover overpayments, so that benefit limits are properly restored
- **Role**: Claim Adjuster
- **Action**: Clawback accumulator amounts using First In First Out when balance actions recover overpayments
- **Value**: Benefit limits are properly restored to reflect actual paid amounts and maintain accurate accumulator balances across multiple coverage periods

**Description:**

> As a **Claim Adjuster**,
> I want to **clawback accumulator amounts using First In First Out when balance actions recover overpayments**,
> So that **benefit limits are properly restored to reflect actual paid amounts and maintain accurate accumulator balances across multiple coverage periods**


**Key Capabilities:**

> 1. System detects successful balance recovery actions on overpayments
> 2. System identifies all accumulator transactions contributing to the recovered balance amount chronologically
> 3. System executes clawback process using FIFO methodology
>     3.1 Recovers amounts from Used to Reserve status
>     3.2 Clears amounts from Reserve to Remaining status
> 4. System applies clawback across multiple coverage periods when balance spans multiple benefit cycles
> 5. System updates accumulator balances to reflect restored benefit limits in real-time


**Acceptance Criteria:**

> 1. **Given** an overpayment balance exists across multiple coverage periods, **When** a balance recovery action is executed, **Then** the system claws back accumulator amounts in FIFO order starting with the earliest transaction
> 2. **Given** a partial recovery is processed, **When** the recovered amount is less than the oldest accumulator transaction, **Then** only that transaction is adjusted proportionally
> 3. **Given** multiple accumulators contributed to the balance, **When** recovery exceeds the first accumulator's contribution, **Then** the system continues clawback to subsequent accumulators chronologically
> 4. **Given** a clawback is triggered, **When** the process completes, **Then** all affected accumulator balances reflect updated Used, Reserve, and Remaining amounts
> 5. **Given** balance recovery fails, **When** the transaction is declined, **Then** no accumulator adjustments occur


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=604814795"
> ]

---

#### Feature: As a Claims Adjuster, I want to trigger payment recalculation when case-level events change (accident date, deductions, ancillaries, plan updates), so that all related claim allocations are recalculated
- **Role**: Claim Adjuster
- **Action**: trigger automated payment recalculation when critical case or claim attributes change
- **Value**: all related claim allocations and settlement amounts are automatically adjusted, ensuring payment accuracy and generating balance records for issued payments

**Description:**

> As a **Claim Adjuster**,
> I want to **trigger automated payment recalculation when critical case or claim attributes change**,
> So that **all related claim allocations and settlement amounts are automatically adjusted, ensuring payment accuracy and generating balance records for issued payments**.


**Key Capabilities:**

> 1. User is able to modify triggering attributes at case level (accident date, organized sport status, retroactive ancillaries/deductions, payment/plan actions)
>     1.1 Upon case-level change, system recalculates all payments across all associated claims
> 2. User is able to modify triggering attributes at claim level (coverage date ranges, days/occurrences, burn degree, reduction type, dislocation/fracture switches)
>     2.1 Upon claim-level change, system recalculates payments for specific affected claim only
> 3. System automatically recalculates gross settlement amounts and payment allocations using policy-defined multipliers and coverage-specific rules
> 4. When issued payment records exist, system generates or regenerates balance records reflecting underpay/overpay amounts
> 5. User is able to review generated balance records showing calculated differences between original and recalculated amounts


**Acceptance Criteria:**

> 1. **Given** case-level attribute changes, **When** modifications are saved, **Then** system recalculates all claim payments within the case and propagates changes to claim level
> 2. **Given** claim-level attribute changes, **When** modifications are saved, **Then** system recalculates only payments for the specific claim
> 3. **Given** issued payment records exist, **When** recalculation completes, **Then** system generates balance records showing underpay or overpay amounts
> 4. **Given** no issued payment records exist, **When** recalculation completes, **Then** system updates settlement amounts without generating balance records
> 5. **Given** retroactive adjustments, **When** multiple coverages are affected, **Then** system regenerates all impacted balance records within single transaction
> 6. **Given** recalculation triggers, **When** processing completes, **Then** system prevents further actions until all affected amounts are updated


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=613801276"
> ]

---

#### Feature: As a Claims Adjuster, I want to recalculate gross amounts and generate balance records when claim-level coverage attributes change (date range, burn degree, reduction type), so that settlements reflect accurate benefit calculations
- **Role**: Claim Adjuster
- **Action**: recalculate settlement amounts and generate balance records when claim or case coverage attributes are modified
- **Value**: settlements accurately reflect updated benefit calculations and policy terms, ensuring payment integrity and regulatory compliance

**Description:**

> As a **Claim Adjuster**,
> I want to **recalculate settlement amounts and generate balance records when claim or case coverage attributes are modified**,
> So that **settlements accurately reflect updated benefit calculations and policy terms, ensuring payment integrity and regulatory compliance**.


**Key Capabilities:**

> 1. User modifies coverage attributes at case level (accident date, organized sport status, deductions, ancillary activities) or claim level (date ranges, burn degree, reduction type, dislocation/fracture switches).
> 2. System automatically recalculates gross settlement amounts and payment allocations based on updated attributes and policy-defined rules.
> 3. Upon detecting existing issued payments, system compares new gross amounts against prior amounts.
> 4. System generates balance records reflecting underpayment (positive) or overpayment (negative) amounts for each affected payment.
> 5. User reviews generated balance records and adjusts settlement accordingly.
> 6. System propagates case-level attribute changes to all associated claim-level calculations.


**Acceptance Criteria:**

> 1. **Given** coverage attributes are modified, **When** user saves changes, **Then** system recalculates gross amounts using updated policy rules within 2 seconds.
> 2. **Given** issued payments exist, **When** recalculation occurs, **Then** system generates balance records for all affected payments showing difference between new and prior gross amounts.
> 3. **Given** case-level attribute changes, **When** propagation triggers, **Then** all claims under the case reflect updated calculations automatically.
> 4. **Given** multiple attributes change simultaneously, **When** recalculation executes, **Then** system applies cumulative impact correctly without double-counting.
> 5. **Given** balance records are generated, **When** user reviews balances, **Then** system displays clear linkage to triggering attribute changes and calculation basis.


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=613801276"
> ]

---

#### Feature: As a Claims Adjuster, I want to recalculate disability claim payments when earnings, taxable percentages, or elimination periods change, so that benefit amounts remain accurate
- **Role**: Claim Adjuster
- **Action**: recalculate disability claim payments when critical attributes change, ensuring accurate benefit amounts and automatic overpay/underpay balance generation
- **Value**: benefit payments remain accurate and compliant, overpayment and underpayment balances are systematically tracked, and financial reconciliation is automated without manual intervention

**Description:**

> As a **Claim Adjuster**,
> I want to **recalculate disability claim payments when critical attributes change, ensuring accurate benefit amounts and automatic overpay/underpay balance generation**,
> So that **benefit payments remain accurate and compliant, overpayment and underpayment balances are systematically tracked, and financial reconciliation is automated without manual intervention**


**Key Capabilities:**

> 1. Adjuster modifies claim attributes including covered earnings, taxable percentages, elimination periods, benefit periods, or gross benefit amounts
> 2. Adjuster adds or updates retroactive financial elements such as offsets, deductions, tax withholdings, or ancillary activities
>     2.1 Case-level changes (e.g., Actively At Work date, FICA exemptions) propagate to all associated claims
>     2.2 Claim-level changes (e.g., current earnings for partial disability) affect specific claim payments
> 3. System automatically recalculates gross settlement amounts and payment allocation amounts upon save
> 4. Upon existence of issued payment records, system generates balance records identifying overpayment or underpayment amounts
> 5. Adjuster reviews generated balance records and initiates recovery or supplemental payment actions as needed


**Acceptance Criteria:**

> 1. **Given** covered earnings or taxable percentage is modified, **When** adjuster saves changes, **Then** system recalculates gross amounts and allocations without manual intervention
> 2. **Given** retroactive deductions or offsets are added, **When** issued payments exist, **Then** system generates balance records with accurate overpay/underpay amounts
> 3. **Given** elimination period or benefit period dates change, **When** recalculation completes, **Then** all affected payments reflect updated benefit periods
> 4. **Given** case-level attributes change (e.g., AAW date), **When** saved, **Then** system propagates changes to all associated claim-level payments
> 5. **Given** face value or annual covered earnings update, **When** issued payments exist, **Then** system calculates balance as (new amount - previously issued amount)
> 6. **Given** multiple retroactive adjustments, **When** recalculation triggered, **Then** system prevents payment issuance until balance reconciliation completes


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=613801321"
> ]

---

#### Feature: As a Claims Adjuster, I want to recalculate payments when retroactive offsets, deductions, or tax withholdings are added to a disability claim, so that net benefit amounts are correctly adjusted
- **Role**: Claim Adjuster
- **Action**: recalculate benefit payments when retroactive changes impact disability claim financials
- **Value**: net benefit amounts reflect accurate deductions, offsets, and tax withholdings, ensuring compliance and preventing overpayments or underpayments

**Description:**

> As a **Claim Adjuster**,
> I want to **recalculate benefit payments when retroactive changes impact disability claim financials**,
> So that **net benefit amounts reflect accurate deductions, offsets, and tax withholdings, ensuring compliance and preventing overpayments or underpayments**.


**Key Capabilities:**

> 1. System automatically triggers payment recalculation when retroactive attributes are modified at case or claim level (e.g., covered earnings, offsets, deductions, tax withholdings).
> 2. Adjuster updates financial attributes such as covered earnings, taxable percentage, or benefit amounts.
>     2.1 Upon save, system recalculates gross settlement amounts and allocation totals.
> 3. System applies retroactive offsets or deductions to previously issued payments.
>     3.1 Balance records are regenerated to reflect underpayment or overpayment positions.
> 4. System adjusts tax withholdings based on updated taxable percentage or exemption status.
> 5. Adjuster reviews recalculated payment schedules and validates balance adjustments before finalization.


**Acceptance Criteria:**

> 1. **Given** a retroactive offset is added, **When** adjuster saves the change, **Then** system recalculates all affected payments and generates balance adjustment records.
> 2. **Given** covered earnings are updated, **When** calculation is triggered, **Then** gross benefit amounts reflect new earnings basis without manual intervention.
> 3. **Given** tax withholding percentage changes, **When** recalculation executes, **Then** net payment amounts incorporate revised tax deductions.
> 4. **Given** an issued payment exists, **When** retroactive deduction is applied, **Then** system creates underpayment or overpayment balance record.
> 5. **Given** multiple retroactive changes occur, **When** system processes adjustments, **Then** all calculations aggregate correctly across case and claim levels.
> 6. **Given** incomplete data, **When** adjuster attempts to save, **Then** system prevents submission until required attributes are provided.


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=613801321"
> ]

---

### Epic: Automated Adjudication & Payment Generation

#### Feature: As a Claims Adjuster, I want to evaluate whether a Wellness claim is eligible for automated adjudication and payment generation, so that eligible claims are processed without manual intervention
- **Role**: Claim Adjuster
- **Action**: evaluate and process Wellness claims through automated adjudication and payment generation workflow
- **Value**: eligible claims are adjudicated and paid without manual intervention, reducing processing time and operational costs

**Description:**

> As a **Claim Adjuster**,
> I want to **evaluate and process Wellness claims through automated adjudication and payment generation workflow**,
> So that **eligible claims are adjudicated and paid without manual intervention, reducing processing time and operational costs**


**Key Capabilities:**

> 1. System evaluates applicability for automated processing upon Event Case submission when Wellness is the exclusive event type selected
> 2. System validates policy status, waiting periods, benefit limits, coverage applicability, and payment method eligibility against predefined business rules
> 3. Upon successful validation, system submits eligible claims to Open status and schedules payment allocations for each payable coverage
>     3.1 When partial eligibility exists, system creates payments only for claims with satisfied waiting periods
>     3.2 When benefit limits are reached, system creates allocation with zero amount
> 4. System generates and issues payments automatically to Member via configured payment method
> 5. Upon payment completion, system attempts automatic case and claim closure


**Acceptance Criteria:**

> 1. **Given** Wellness is the only event type selected and all eligibility conditions are satisfied, **When** Event Case is submitted, **Then** system creates claims in Open status and generates payment allocations automatically
> 2. **Given** multiple event types are selected including Wellness, **When** Event Case is submitted, **Then** system creates claims in Pending status without automated payments
> 3. **Given** policy waiting periods are not satisfied, **When** eligibility is evaluated, **Then** system prevents payment generation for ineligible policies
> 4. **Given** payment method is undefined or invalid, **When** payment scheduling is attempted, **Then** system blocks automated payment creation
> 5. **Given** benefit limits are reached, **When** payment allocation is created, **Then** system sets gross benefit amount to zero
> 6. **Given** Event Case reason is not 'Other' or subject is not Member, **When** applicability is evaluated, **Then** system prevents Wellness coverage assignment and automated processing


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=806685937"
> ]

---

#### Feature: As a Claims Adjuster, I want to verify that all pre-conditions for Wellness auto-payment are met (active policy, event date validation, member eligibility, payment method), so that only compliant claims proceed to automated payment
- **Role**: Claim Adjuster
- **Action**: verify that all pre-conditions for Wellness auto-payment are met, including active policy validation, event date alignment, member eligibility assessment, and payment method availability
- **Value**: only compliant claims proceed to automated payment processing, reducing manual intervention and ensuring regulatory compliance while accelerating member reimbursement

**Description:**

> As a **Claim Adjuster**,
> I want to **verify that all pre-conditions for Wellness auto-payment are met, including active policy validation, event date alignment, member eligibility assessment, and payment method availability**,
> So that **only compliant claims proceed to automated payment processing, reducing manual intervention and ensuring regulatory compliance while accelerating member reimbursement**.


**Key Capabilities:**

> 1. System validates policy active status and confirms event dates (Event Date, Wellness Visit Date, Date of Loss) occur on or after policy effective date
> 2. System confirms Event Case configuration meets auto-payment criteria: single Wellness event type selected, Subject is Member, Reason set to 'Other'
> 3. System evaluates eligibility rules including both primary claim waiting period and Wellness benefit-specific waiting period completion
> 4. System verifies payment method availability (Check or EFT) is defined in Customer Entity Management for the Member
>     4.1 When multiple policies exist with different waiting periods, system processes only policies meeting eligibility thresholds
> 5. System assesses coverage limits and sets Gross Benefit Amount to zero when utilization thresholds are reached
> 6. Upon successful validation, system transitions claims to 'Open' status enabling automated payment generation; upon failure, claims remain in 'Pending' status requiring manual review


**Acceptance Criteria:**

> 1. **Given** active policy with Event Date on or after effective date, **When** Event Date precedes policy effective date, **Then** system prevents automated processing and flags for manual review
> 2. **Given** Event Case intake with multiple event types, **When** Wellness is not the sole event type selected, **Then** system creates claims in 'Pending' status without automated payment generation
> 3. **Given** Event Case with Reason set to 'Sickness' or 'Accident', **When** validation executes, **Then** system does not assign Wellness coverage and prevents auto-payment
> 4. **Given** multiple policies with varying waiting periods, **When** only subset meets waiting period requirements, **Then** system generates partial payments exclusively for eligible policies
> 5. **Given** Member without defined payment method, **When** pre-condition validation occurs, **Then** system prevents payment allocation creation and requires payment method setup
> 6. **Given** Wellness coverage limit reached, **When** system calculates Gross Benefit Amount, **Then** system sets amount to zero and suppresses payment creation despite other conditions being satisfied


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=806685937"
> ]

---

#### Feature: As a Claims Adjuster, I want to confirm that only Wellness event type was selected during Event Case intake (excluding Accident, Sickness, or other claim events), so that mixed-event cases are excluded from automated payment
- **Role**: Claim Adjuster
- **Action**: validate that only Wellness event type was selected during event case intake, excluding any mixed-event scenarios, to determine automated payment eligibility
- **Value**: the system correctly applies automated adjudication and payment generation only to pure wellness claims, preventing processing errors and ensuring compliance with business rules for CI/HI/ACC claim automation

**Description:**

> As a **Claim Adjuster**,
> I want to **validate that only Wellness event type was selected during event case intake, excluding any mixed-event scenarios, to determine automated payment eligibility**,
> So that **the system correctly applies automated adjudication and payment generation only to pure wellness claims, preventing processing errors and ensuring compliance with business rules for CI/HI/ACC claim automation**


**Key Capabilities:**

> 1. System validates event type selection during intake verification phase for automated adjudication eligibility
>     1.1 Upon single Wellness event type detected, system proceeds with automated adjudication pathway
>     1.2 When multiple event types detected (e.g., Wellness + Hospital Services), system routes to manual adjudication
> 2. System verifies event case reason is set to 'Other' and subject is Member
> 3. System confirms wellness coverage assignment and waiting period satisfaction for all applicable policies
> 4. System creates payment allocations automatically for eligible claims in Open status
> 5. Upon business rule failure, system places claims in Pending status requiring manual adjuster intervention
> 6. System generates audit trail documenting event type validation and adjudication routing decision


**Acceptance Criteria:**

> 1. **Given** event case with only Wellness event type selected and all eligibility conditions met, **When** system evaluates adjudication pathway, **Then** system routes to automated payment generation and creates payment allocations
> 2. **Given** event case with Wellness plus additional event types (e.g., Accident, Sickness, Hospital Indemnity), **When** system validates event selection, **Then** system excludes from automated payment and routes to manual adjudication in Pending status
> 3. **Given** event case with Wellness event but Event Case reason is not 'Other', **When** system evaluates pre-conditions, **Then** system prevents automated payment and wellness coverage assignment
> 4. **Given** event case with Wellness event but Subject is not Member, **When** system validates eligibility, **Then** system blocks automated payment processing
> 5. **Given** multiple policies with varying waiting periods, **When** system processes eligible wellness claim, **Then** system creates payment allocations only for policies with elapsed waiting periods
> 6. **Given** successful automated payment creation, **When** system completes payment issuance, **Then** system initiates automatic case closure process


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=806685937"
> ]

---

#### Feature: As a Claims Operations Manager, I want the system to automatically validate Wellness coverage eligibility including waiting periods and benefit limits, so that only eligible coverages are scheduled for payment
- **Role**: Claim Adjuster
- **Action**: automatically validate Wellness coverage eligibility including waiting periods, benefit limits, and policy requirements to authorize automated payment generation
- **Value**: eligible Wellness claims are processed and paid without manual intervention, reducing processing time and operational costs while ensuring accuracy

**Description:**

> As a Claim Adjuster,
> I want to automatically validate Wellness coverage eligibility including waiting periods, benefit limits, and policy requirements to authorize automated payment generation,
> So that eligible Wellness claims are processed and paid without manual intervention, reducing processing time and operational costs while ensuring accuracy.


**Key Capabilities:**

> 1. System validates pre-conditions: active policy status, event date alignment, member as subject, 'Other' event reason, and configured payment method.
>     1.1 Upon policy inactive or date misalignment, system blocks claim creation and halts automated processing.
> 2. System evaluates Wellness-only applicability: confirms single 'Wellness' event type selected without additional claim events.
>     2.1 When multiple event types detected, system creates claims in 'Pending' status without automated payment.
> 3. System assesses eligibility by verifying both claim-level and Wellness coverage waiting periods are satisfied.
>     3.1 User is able to process partial payments when subset of claims meet waiting period requirements.
> 4. System calculates benefit amounts subject to policy limits and usage caps, setting GBA to zero when limits exhausted.
> 5. System submits eligible claims to 'Open' status and schedules payment allocations with member as payee and wellness visit date as incident date.
> 6. Upon successful payment scheduling, system triggers automated payment issuance and initiates closure process for completed cases.


**Acceptance Criteria:**

> 1. **Given** active policies with Wellness coverage and 'Other' event reason, **When** only Wellness event type selected and all waiting periods satisfied, **Then** system creates claims in 'Open' status and generates payment allocations automatically.
> 2. **Given** multiple event types selected during intake, **When** Wellness included with other claim events, **Then** system creates claims in 'Pending' status without automated payment generation.
> 3. **Given** mixed waiting period compliance across claim types, **When** only subset meets elapsed time requirements, **Then** system creates payment allocations exclusively for qualified claims.
> 4. **Given** Wellness coverage with usage limits, **When** benefit cap reached or policy inactive, **Then** system sets GBA to zero and prevents payment creation.
> 5. **Given** missing payment method or invalid subject, **When** pre-condition validation executed, **Then** system blocks automated processing and prevents claim advancement.
> 6. **Given** all eligibility criteria satisfied, **When** payments scheduled, **Then** system populates member as payee, wellness visit date as incident date, and zero interest calculation.


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=806685937"
> ]

---

#### Feature: As a Claims Operations Manager, I want the system to automatically create payment allocations with correct Wellness-specific settings (Member as payee, Wellness Visit Date as incident date), so that payments are generated with accurate claim data
- **Role**: Claim Adjuster
- **Action**: enable automated evaluation, adjudication, and payment generation for eligible Wellness claims without manual intervention
- **Value**: claims are processed efficiently with accurate payment allocations, reducing manual workload and ensuring timely member reimbursement

**Description:**

> As a **Claim Adjuster**,
> I want to **enable automated evaluation, adjudication, and payment generation for eligible Wellness claims without manual intervention**,
> So that **claims are processed efficiently with accurate payment allocations, reducing manual workload and ensuring timely member reimbursement**


**Key Capabilities:**

> 1. System evaluates claim applicability by verifying Wellness is the sole event type selected, event case reason is 'Other', and subject is the member
> 2. System validates eligibility by confirming approved settlement status, active policy effective dates, and satisfaction of both general and Wellness-specific waiting periods
> 3. System submits qualifying claims to 'Open' status and schedules automated payment allocation with member as payee and Wellness visit date as incident date
> 4. System calculates gross benefit amount per coverage, excluding claims with exhausted limits or unmet waiting periods
> 5. System automatically generates and issues payments via scheduled payment process
> 6. Upon payment issuance completion, system triggers automatic case and claim closure workflow


**Acceptance Criteria:**

> 1. **Given** only Wellness event type selected with member as subject and 'Other' reason, **When** all waiting periods are satisfied and policy is active, **Then** system creates claims in 'Open' status and generates payment allocations with member as payee
> 2. **Given** multiple event types selected during intake, **When** system evaluates applicability, **Then** no automated payments are created regardless of eligibility status
> 3. **Given** waiting period not met for specific coverage, **When** other coverages have satisfied waiting periods, **Then** system creates payments only for eligible coverages
> 4. **Given** coverage benefit limits are exhausted, **When** system calculates gross benefit amount, **Then** no payment allocation is created for that coverage
> 5. **Given** subject of case is not the member, **When** system validates preconditions, **Then** Wellness coverage is not assigned and no automated payment is generated
> 6. **Given** all payments successfully issued, **When** payment generation completes, **Then** system initiates automatic closure process for case and associated claims


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=806685937"
> ]

---

#### Feature: As a Claims Operations Manager, I want the system to determine which claim coverages must be paid automatically based on adjudication rules and event type, so that the correct set of coverages enters the payment scheduling process
- **Role**: Claim Manager
- **Action**: automatically determine, validate, and process eligible claim coverages through adjudication rules to payment issuance without manual intervention
- **Value**: payment accuracy is ensured, processing time is reduced, and operational efficiency increases through rule-based automation aligned with event type and coverage requirements

**Description:**

> As a **Claim Manager**,
> I want to **automatically determine, validate, and process eligible claim coverages through adjudication rules to payment issuance without manual intervention**,
> So that **payment accuracy is ensured, processing time is reduced, and operational efficiency increases through rule-based automation aligned with event type and coverage requirements**


**Key Capabilities:**

> 1. System evaluates which coverages require automatic payment based on claim type (STD applies scenario-specific rules; Wellness/CI/HI/ACC requires 'Wellness' event type selection during intake)
> 2. System validates coverage auto-payment eligibility by verifying approved state, policy status, waiting periods, benefit limits, member payment method, and event date alignment
> 3. Upon eligibility confirmation, system submits claims and builds payment schedules by deactivating prior schedules, canceling duplicate payments, executing rule engine calculations, and activating new schedule
> 4. System generates payments from active schedules through batch job applying generation rules and initializing payment records
> 5. System issues payments by dispatching to Payment Hub when net amount exceeds zero or completing issuance directly for zero/negative amounts
> 6. When payment generation fails or validation errors occur, system creates user tasks with failure reasons and halts automated processing for manual review


**Acceptance Criteria:**

> 1. **Given** STD claim with applicable auto-adjudication scenario, **When** coverage state is Approved and adjudication confirms automatic payment eligibility, **Then** system submits claim and initiates payment scheduling
> 2. **Given** Wellness event type selected during intake for CI/HI/ACC claims, **When** policy active, waiting periods satisfied, and member has valid payment method, **Then** system automatically assigns Wellness coverage and generates payment allocations
> 3. **Given** multiple coverages requiring automatic payment at case level, **When** any coverage fails eligibility validation, **Then** system generates 'Auto Adjudication Payment Generation Failed' task with specific failure reasons and halts processing
> 4. **Given** active payment schedule exists, **When** new schedule activation triggered, **Then** system deactivates prior schedule and cancels approved payments to prevent duplicates
> 5. **Given** payment dispatch validation fails or Payment Hub rejects request, **When** schedule remains active, **Then** system cancels payment, regenerates from schedule, and creates 'Canceled Payments' task if regeneration incomplete
> 6. **Given** all payments successfully issued, **When** no pending payments remain, **Then** system attempts automatic case and claim closure per defined business rules


**Reference URLs:**

> [
>   "/pages/viewpage.action?pageId=556508984",
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=806685937",
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=678438370",
>   "/pages/viewpage.action?pageId=645896452",
>   "/pages/viewpage.action?pageId=494117420"
> ]

---

#### Feature: As a Claims Operations Manager, I want the system to verify that claim coverages are in Approved status before scheduling automated payments, so that only adjudicated and eligible coverages are paid
- **Role**: Claim Adjuster
- **Action**: verify that claim coverages are in Approved status and meet all eligibility criteria before scheduling automated payments
- **Value**: only adjudicated and eligible coverages proceed to payment generation, preventing erroneous disbursements and ensuring compliance with adjudication outcomes

**Description:**

> As a Claim Adjuster,
> I want to verify that claim coverages are in Approved status and meet all eligibility criteria before scheduling automated payments,
> So that only adjudicated and eligible coverages proceed to payment generation, preventing erroneous disbursements and ensuring compliance with adjudication outcomes


**Key Capabilities:**

> 1. System evaluates claim coverages to determine automatic payment eligibility based on adjudication scenario outcomes and coverage status.
> 2. System validates that claim coverage state equals 'Approved' before proceeding to payment scheduling.
>     2.1 For STD claims, system confirms automated payment generation decision was made during adjudication evaluation.
>     2.2 For Wellness events, system verifies coverage applicability to auto-adjudication rules.
> 3. System submits eligible claims using lifecycle commands once validation criteria are satisfied.
> 4. System builds and activates payment schedules only after successful eligibility verification.
> 5. Upon validation failure, system generates user tasks for manual intervention rather than proceeding to payment generation.
> 6. System deactivates existing payment schedules and cancels active payments to prevent duplicate processing before creating new schedules.


**Acceptance Criteria:**

> 1. **Given** a claim coverage in non-Approved status, **When** automated payment eligibility is evaluated, **Then** system prevents payment scheduling and does not proceed to payment generation.
> 2. **Given** an STD claim coverage lacking automated payment decision, **When** eligibility validation executes, **Then** system blocks payment schedule creation and generates intervention task.
> 3. **Given** a claim coverage meeting all approval and eligibility criteria, **When** validation completes successfully, **Then** system proceeds to submit claim and initiate payment scheduling process.
> 4. **Given** multiple claim coverages within a case, **When** eligibility verification runs, **Then** system evaluates each coverage independently and only schedules payments for approved coverages.
> 5. **Given** eligibility validation failure at any checkpoint, **When** system detects incomplete criteria, **Then** automated payment generation terminates and creates user task for manual resolution.
> 6. **Given** successful eligibility verification, **When** payment schedule activation encounters errors, **Then** system generates review task and halts automated payment processing.


**Reference URLs:**

> [
>   "/pages/viewpage.action?pageId=657907234",
>   "/pages/viewpage.action?pageId=556508984",
>   "/pages/viewpage.action?pageId=494117420",
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=678438370",
>   "/pages/viewpage.action?pageId=645896452"
> ]

---

#### Feature: As a Claims Operations Manager, I want the system to automatically submit eligible claims to Open status before scheduling payments, so that claims are ready for payment processing
- **Role**: Claim Adjuster
- **Action**: automatically submit eligible adjudicated claims and generate payment schedules without manual intervention
- **Value**: claims transition seamlessly from coverage evaluation to payment processing, reducing processing time and ensuring timely benefit delivery

**Description:**

> As a **Claim Adjuster**,
> I want to **automatically submit eligible adjudicated claims and generate payment schedules without manual intervention**,
> So that **claims transition seamlessly from coverage evaluation to payment processing, reducing processing time and ensuring timely benefit delivery**


**Key Capabilities:**

> 1. System evaluates adjudicated claim coverages against auto-payment eligibility rules based on claim type and scenario
> 2. System determines whether all eligible coverages within the case can proceed to automated payment
> 3. System submits claims with approved coverages to Open status following standard lifecycle rules
> 4. System schedules payments according to configured payment levels (case-level or claim-level) and allocation settings
> 5. Upon payment scheduling failure, system generates targeted tasks with diagnostic information for manual review
> 6. System validates successful payment scheduling before triggering downstream payment issuance and closure processes


**Acceptance Criteria:**

> 1. **Given** claim coverages are adjudicated and approved, **When** all coverages meet auto-payment criteria, **Then** system submits claims to Open status without manual intervention
> 2. **Given** claims are submitted, **When** payment scheduling is triggered, **Then** system creates payment schedules per configured payment level and allocation rules
> 3. **Given** payment scheduling completes, **When** validation confirms success, **Then** system proceeds to automated payment issuance and closure workflows
> 4. **Given** payment scheduling fails, **When** validation detects errors, **Then** system generates tasks with failure reasons from adjudication or scheduling processes
> 5. **Given** multiple claims in one case, **When** payment level is case-based, **Then** system consolidates payment scheduling at case level
> 6. **Given** wellness or disability scenarios, **When** scheduling payments, **Then** system applies scenario-specific payee and allocation settings


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=678438370"
> ]

---

#### Feature: As a Claims Operations Manager, I want the system to automatically schedule payments for approved coverages and trigger payment issuance, so that eligible claims are processed through the payment pipeline without manual intervention
- **Role**: Claim Adjuster
- **Action**: enable automated payment scheduling and issuance for approved coverages through system-driven adjudication workflows
- **Value**: eligible claims are processed through the payment pipeline without manual intervention, reducing processing time and operational overhead

**Description:**

> As a **Claim Adjuster**,
> I want to **enable automated payment scheduling and issuance for approved coverages through system-driven adjudication workflows**,
> So that **eligible claims are processed through the payment pipeline without manual intervention, reducing processing time and operational overhead**


**Key Capabilities:**

> 1. System evaluates adjudicated coverages against auto-payment eligibility rules based on claim type and coverage approval status
> 2. Upon eligibility confirmation, system submits qualifying claims through lifecycle workflow
> 3. System generates payment schedules per configuration (event-level or claim-level) with appropriate payee and allocation settings
> 4. When scheduling succeeds, system automatically triggers payment issuance process
> 5. If eligibility check or scheduling fails, system generates exception task with failure diagnostic details
> 6. Upon successful payment issuance, system initiates automated case closure workflow


**Acceptance Criteria:**

> 1. **Given** coverages are approved and meet auto-adjudication criteria, **When** payment automation executes, **Then** system generates payment schedules without manual intervention
> 2. **Given** payment level is event-based, **When** scheduling triggers, **Then** single payment schedule created for entire case
> 3. **Given** payment level is claim-based, **When** scheduling triggers, **Then** separate schedules generated per qualifying claim
> 4. **Given** coverage fails eligibility validation, **When** automation detects failure, **Then** system creates exception task with diagnostic messages and halts payment generation
> 5. **Given** payment scheduling fails, **When** error occurs, **Then** system generates failure task and prevents payment issuance
> 6. **Given** payments issued successfully, **When** issuance completes, **Then** system automatically initiates case closure process


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=678438370"
> ]

---

#### Feature: As a Claims Operations Manager, I want the system to generate a user task when automated adjudication and payment generation fails, so that failures are tracked and can be investigated
- **Role**: Claim Manager
- **Action**: receive system-generated tasks when automated payment generation fails
- **Value**: failures are immediately tracked, investigated, and resolved without payment delays or manual oversight gaps

**Description:**

> As a **Claim Manager**,
> I want to **receive system-generated tasks when automated payment generation fails**,
> So that **failures are immediately tracked, investigated, and resolved without payment delays or manual oversight gaps**


**Key Capabilities:**

> 1. System evaluates coverage eligibility for automatic payment per adjudication rules
> 2. System validates whether all required coverages can be processed automatically
> 3. Upon validation failure, system generates automated task for investigation
>     3.1 Task created at case level when payment level is 'Event Case'
>     3.2 Task created per claim when payment level is 'Claim'
> 4. System captures failure reasons from adjudication messages or scheduling errors
> 5. User is able to access diagnostic context for resolution


**Acceptance Criteria:**

> 1. **Given** coverage eligibility check fails, **When** payment cannot be automatically generated, **Then** system creates user task with failure diagnostics
> 2. **Given** payment level is 'Event Case', **When** failure occurs, **Then** system generates single task at case level
> 3. **Given** payment level is 'Claim', **When** failure occurs, **Then** system generates task per affected claim
> 4. **Given** task is generated, **When** user accesses details, **Then** failure source and adjudication messages are available
> 5. **Given** automated process completes, **When** no failures occur, **Then** no exception tasks are created


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=678438370"
> ]

---

### Epic: Accumulator Management & Limit Tracking

#### Feature: As a Claims Adjuster, I want to configure accumulator types for each coverage by product, so that the system can correctly track and limit benefit payments across different accumulation dimensions.
- **Role**: Claim Adjuster
- **Action**: configure accumulator types for each coverage by product to establish benefit payment limits and tracking dimensions
- **Value**: the system automatically monitors benefit consumption across multiple dimensions (per event, lifetime, calendar year) and prevents overpayment while ensuring accurate remaining balance calculations throughout the claim lifecycle

**Description:**

> As a **Claim Adjuster**,
> I want to **configure accumulator types for each coverage by product to establish benefit payment limits and tracking dimensions**,
> So that **the system automatically monitors benefit consumption across multiple dimensions (per event, lifetime, calendar year) and prevents overpayment while ensuring accurate remaining balance calculations throughout the claim lifecycle**.


**Key Capabilities:**

> 1. Configure accumulator types by product line establishing tracking dimensions (Term Life: Per Individual/Group Death Limit; Critical Illness: Per Event/Benefit Year/Lifetime; Hospital Indemnity: Per Confinement; Accident: Per Calendar Year/Lifetime).
> 2. Define limit calculation rules including maximum benefit amounts from policy terms, dynamic group limits derived from face value or maximum coverage amounts, and allocation formulas for specialized coverages.
> 3. Establish accumulator lifecycle actions mapping business events to balance adjustments (Create sets initial limit, Reserve allocates amounts during adjudication, Use consumes upon payment issuance, Recover/Clear handle cancellations and reversals).
> 4. Configure gross amount constraints ensuring calculated coverage amounts never exceed remaining accumulator balances across individual and group limit hierarchies.
>     4.1 Upon coverage cancellation or non-eligibility designation, system releases reserved amounts back to available balance.
>     4.2 When face value is overridden, system adjusts limits and re-reserves based on latest approved settlements.


**Acceptance Criteria:**

> 1. **Given** accumulator types are configured for a product line, **When** coverage is added to a claim, **Then** system generates applicable accumulators with initial limits and calculates gross amounts constrained by remaining balances.
> 2. **Given** coverage is saved as eligible with approved settlement, **When** adjudication completes, **Then** system reserves gross amount reducing remaining balance and displays used/remaining amounts.
> 3. **Given** payment is issued for a coverage, **When** transaction processes successfully, **Then** system moves reserved amount to used amount maintaining accurate consumption tracking.
> 4. **Given** coverage with group limit is cancelled, **When** cancellation processes, **Then** system recalculates dynamic group limits excluding cancelled coverage and adjusts remaining balances for related coverages.
> 5. **Given** payment is declined or voided, **When** reversal occurs, **Then** system recovers used amount back to reserved status maintaining limit integrity.
> 6. **Given** face value override is applied, **When** adjustment processes, **Then** system adjusts accumulator limits, clears existing reserves, and re-reserves based on latest approved settlements.


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=618282188"
> ]

---

#### Feature: As a Claims Adjuster, I want to view accumulator limit details including Limit Amount, Used, Planned, and Remaining values for each coverage, so that I can make informed adjudication decisions within policy constraints.
- **Role**: Claim Adjuster
- **Action**: access and monitor accumulator limit details across multiple limit levels (Per Event, Per Lifetime Per Individual, Per Policy, Per Calendar Year, Per Event Per Group) to track Limit Amount, Used, Planned, and Remaining values throughout the claim lifecycle
- **Value**: I can make informed adjudication decisions that comply with policy constraints, prevent over-payments, and ensure accurate reserve management across different coverage types and limit boundaries

**Description:**

> As a **Claim Adjuster**,
> I want to **access and monitor accumulator limit details across multiple limit levels (Per Event, Per Lifetime Per Individual, Per Policy, Per Calendar Year, Per Event Per Group) to track Limit Amount, Used, Planned, and Remaining values throughout the claim lifecycle**,
> So that **I can make informed adjudication decisions that comply with policy constraints, prevent over-payments, and ensure accurate reserve management across different coverage types and limit boundaries**.


**Key Capabilities:**

> 1. Upon adding coverage to a Critical Illness or Accident claim, system initializes accumulator tied to the subject of claim
> 2. User is able to view accumulator status indicators for each coverage record on claim overview
> 3. User is able to access detailed accumulator breakdown showing Limit Amount, Used, Planned Amount, and Remaining Amount for Money/Days/Times units across applicable limit levels
> 4. When reserve, unreserve, or payment actions occur, system automatically updates accumulator values moving amounts between Remaining, Planned, and Used categories
> 5. System calculates Used Amount based on limit-level-specific time boundaries (benefit year, confinement period, calendar year, or event/group)
> 6. For shared accumulators, system aggregates usage across multiple benefits sharing the same limit level


**Acceptance Criteria:**

> 1. **Given** a coverage is added to a claim, **When** the system initializes the accumulator, **Then** Limit Amount is set and copied to Remaining Amount with zero Used and Planned values
> 2. **Given** adjuster accesses accumulator details, **When** viewing the breakdown, **Then** system displays all applicable limit levels with their respective Limit, Used, Planned, and Remaining values in appropriate units
> 3. **Given** a reserve action is executed, **When** amount is reserved, **Then** system moves specified amount from Remaining to Planned and updates display accordingly
> 4. **Given** payment is approved, **When** settlement is finalized, **Then** system moves amount from Planned to Used and recalculates Remaining Amount within correct time boundary
> 5. **Given** multiple benefits share Per Lifetime Per Individual limit, **When** any benefit triggers reserve/use action, **Then** system updates the shared accumulator affecting all related benefits
> 6. **Given** accumulator values are displayed, **When** Used Amount reaches or exceeds Limit Amount, **Then** system prevents further adjudication that would breach policy constraints


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=616765644"
> ]

---

#### Feature: As a Claims Adjuster, I want the system to automatically initialize accumulators when adding a coverage, so that limit tracking begins immediately and accurately reflects policy constraints.
- **Role**: Claim Adjuster
- **Action**: have the system automatically initialize accumulators when adding coverage to a claim
- **Value**: limit tracking begins immediately and accurately reflects policy constraints, enabling precise adjudication and preventing overpayment

**Description:**

> As a **Claim Adjuster**,
> I want to **have the system automatically initialize accumulators when adding coverage to a claim**,
> So that **limit tracking begins immediately and accurately reflects policy constraints, enabling precise adjudication and preventing overpayment**.


**Key Capabilities:**

> 1. Upon adding coverage to a claim, system creates non-time-period and non-dynamic-group-limit accumulators with initial limit values derived from policy terms or default claim units.
> 2. System establishes baseline tracking by setting Remaining amount equal to Limit and initializing Reserve and Used amounts to zero.
> 3. When coverage is saved with eligible status and settlement approved, system creates time-period and dynamic-group-limit accumulators and reserves the Gross Amount against available limits.
> 4. System calculates and enforces maximum claimable amounts using formula: MIN(Coverage Calculated Amount, Claim Coverage Remaining, Group Remaining).
> 5. User is able to view real-time limit remaining amounts, planned reserves, and used amounts across all applicable accumulator types (Per Individual, Per Event, Per Calendar Year, Per Lifetime, Group Death Limit).
> 6. If coverage involves dynamic group limits, system defaults Limit Remaining to zero until reduction type selection, then updates automatically when maximum benefit coverage changes eligibility status.


**Acceptance Criteria:**

> 1. **Given** a claim adjuster adds a new coverage to a claim, **When** the coverage is added, **Then** system creates all applicable non-time-period accumulators with Limit, Remaining=Limit, Reserve=0, and Used=0.
> 2. **Given** coverage is saved with eligible status and settlement approved, **When** adjudication completes, **Then** system creates time-period accumulators and reserves Gross Amount, updating Remaining=Limit-Reserve.
> 3. **Given** multiple accumulator types apply to a coverage (e.g., Per Event, Per Lifetime, Group Death Limit), **When** initialization occurs, **Then** system creates all configured accumulator instances simultaneously.
> 4. **Given** coverage involves dynamic group limits (Dislocation, Fracture, Covered Loss), **When** coverage is added before reduction type selection, **Then** system defaults Limit Remaining to zero until selection.
> 5. **Given** policy terms define maximum benefit amounts or Face Value constraints, **When** accumulator initializes, **Then** Limit value accurately reflects policy-derived maximum (maxBenefitAmountPct*faceValue or maxBenefitNumber).
> 6. **Given** accumulator initialization fails due to missing policy configuration, **When** error occurs, **Then** system prevents coverage addition and notifies adjuster of configuration gap.


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=618282188"
> ]

---

#### Feature: As a Claims Adjuster, I want the system to reserve planned amounts when coverage is approved and settled, so that the system accurately reflects committed benefit obligations against remaining limits.
- **Role**: Claim Adjuster
- **Action**: automatically reserve adjudicated benefit amounts against policy limits and track utilization throughout the claim lifecycle
- **Value**: the system accurately reflects committed benefit obligations, prevents overpayment, and maintains real-time visibility of remaining policy limits across multiple coverage types and time periods

**Description:**

> As a **Claim Adjuster**,
> I want to **automatically reserve adjudicated benefit amounts against policy limits and track utilization throughout the claim lifecycle**,
> So that **the system accurately reflects committed benefit obligations, prevents overpayment, and maintains real-time visibility of remaining policy limits across multiple coverage types and time periods**


**Key Capabilities:**

> 1. Upon coverage approval, system creates accumulators with initial limits derived from policy face values or maximum benefit amounts
> 2. When settlement is adjudicated and approved, system reserves planned amounts by moving values from remaining to reserved state
>     2.1 System calculates reservations constrained by time periods (calendar year, benefit year, per event) and dynamic group limits
>     2.2 For dynamic group limits, system recalculates maximums when constituent coverages are cancelled or become ineligible
> 3. Upon payment issuance, system moves reserved amounts to used state and updates remaining balances
> 4. When payment lifecycle events occur (cancellation, void, stop, recovery), system performs accumulator adjustments: Clear (reserve→remaining), Recover (used→reserve), or sequential combinations
> 5. If policy face value is overridden, system executes Adjust→Clear→Reserve sequence to recalibrate all accumulator values
> 6. System prevents benefit allocation exceeding calculated gross amounts across individual and group accumulator hierarchies


**Acceptance Criteria:**

> 1. **Given** coverage is added, **When** adjuster confirms coverage details, **Then** system creates accumulators with limit equal to remaining amount and zero reserved/used values
> 2. **Given** settlement is approved, **When** coverage is saved as eligible, **Then** system reserves gross amount (minimum of calculated amount, individual remaining, and group remaining) and reduces available limits accordingly
> 3. **Given** payment is issued, **When** payment processes successfully, **Then** system transfers reserved amount to used state while maintaining limit-remaining balance
> 4. **Given** payment is cancelled/voided/stopped, **When** lifecycle command executes, **Then** system returns amounts through appropriate accumulator actions (Clear or Recover→Clear→Reserve sequence) restoring availability
> 5. **Given** coverage is cancelled or set non-eligible, **When** status change occurs, **Then** system clears all reservations returning amounts to remaining state
> 6. **Given** dynamic group limit exists, **When** constituent coverage with maximum benefit is cancelled, **Then** system recalculates group limit using next highest benefit amount and adjusts all related accumulators


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=618282188"
> ]

---

#### Feature: As a Claims Adjuster, I want the system to update accumulator used amounts when payments are issued, so that the system maintains accurate tracking of consumed benefits across the claim lifecycle.
- **Role**: Claim Adjuster
- **Action**: ensure the system automatically updates accumulator values (reserved, used, remaining amounts) as claim settlements progress through adjudication, payment issuance, and post-payment adjustments
- **Value**: accurate benefit consumption tracking is maintained throughout the claim lifecycle, preventing overpayment and ensuring policy limit compliance without manual intervention

**Description:**

> As a **Claim Adjuster**,
> I want to **ensure the system automatically updates accumulator values (reserved, used, remaining amounts) as claim settlements progress through adjudication, payment issuance, and post-payment adjustments**,
> So that **accurate benefit consumption tracking is maintained throughout the claim lifecycle, preventing overpayment and ensuring policy limit compliance without manual intervention**.


**Key Capabilities:**

> 1. Upon coverage eligibility confirmation, system initializes accumulator tracking with policy-defined limits for applicable time periods and coverage groups.
> 2. When settlement is approved, system reserves the adjudicated gross amount by reducing remaining limit availability and preventing duplicate benefit allocation.
> 3. Upon payment issuance, system transfers reserved amounts to used amounts and updates remaining limits to reflect consumed benefits.
> 4. When payment is cancelled, voided, or stopped, system reverses accumulator transactions and restores amounts to appropriate states (remaining or reserved) based on action type.
> 5. If coverage is modified or cancelled, system recalculates group limits for dynamic accumulator types and clears reserved amounts to restore availability.
> 6. System applies accumulator remaining amounts as maximum limit constraints during gross amount calculation to prevent benefit overutilization.


**Acceptance Criteria:**

> 1. **Given** coverage is saved as eligible with approved settlement, **When** adjudication completes, **Then** system reserves gross amount and updates remaining limit to reflect unavailable funds.
> 2. **Given** payment is successfully issued, **When** payment processing completes, **Then** system moves reserved amount to used amount and maintains accurate remaining limit.
> 3. **Given** payment is cancelled or voided, **When** reversal action executes, **Then** system restores amounts to previous state with reserve cleared or replenished based on action type.
> 4. **Given** coverage is cancelled or set to non-eligible, **When** coverage status changes, **Then** system releases reserved amounts back to remaining limit availability.
> 5. **Given** dynamic group limit applies, **When** coverage within group is cancelled, **Then** system recalculates group limit and adjusts remaining amounts accordingly.
> 6. **Given** policy face value is overridden, **When** configuration changes, **Then** system adjusts limits, clears reserves, and re-reserves based on latest approved settlements.


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=618282188"
> ]

---

#### Feature: As a Claims Adjuster, I want the system to calculate gross amounts limited by remaining accumulator balances, so that benefit payments never exceed policy limits across single and group accumulators.
- **Role**: Claim Adjuster
- **Action**: ensure benefit payments automatically calculate against single and group accumulator limits with dynamic recalculation across policy periods
- **Value**: policy limits are enforced, overpayments are prevented, and accumulator balances accurately reflect utilization across claims and time boundaries

**Description:**

> As a **Claim Adjuster**,
> I want to **ensure benefit payments automatically calculate against single and group accumulator limits with dynamic recalculation across policy periods**,
> So that **policy limits are enforced, overpayments are prevented, and accumulator balances accurately reflect utilization across claims and time boundaries**.


**Key Capabilities:**

> 1. System calculates remaining benefit amounts using minimum of single accumulator balance, prorated daily limits for time period, and group accumulator balance
> 2. When claim period crosses calendar year (Jan 1-Dec 31) or benefit year (policy effective date + 12 months) boundary, system automatically splits calculation into separate periods
>     2.1 Each period updates respective year accumulator independently
>     2.2 System caps payment by actual remaining days when year-end approaches
> 3. System converts between unit-based (days) and monetary accumulators by applying benefit amount multipliers and applicable percentage adjustments
> 4. Upon coverage cancellation or quantity adjustment post-payment, system recalculates group limits dynamically, generates overpayments, and withholds amounts from eligible coverages to offset
> 5. System updates reserve amounts upon claim approval and used amounts upon payment issuance across all linked accumulators
> 6. System maintains accumulator integrity across multiple claims and cases sharing same policy limits


**Acceptance Criteria:**

> 1. **Given** a claim spanning year boundaries, **When** the system processes payment, **Then** calculation splits at year-end date with each period updating separate accumulator balances and payment never exceeds prorated daily limits
> 2. **Given** coverage and group accumulators with different units, **When** calculating remaining amounts, **Then** system converts units to monetary values using benefit amounts and percentage adjustments before comparison
> 3. **Given** multiple coverages under dynamic group limit, **When** one coverage is cancelled post-payment, **Then** system recalculates group limit based on remaining eligible coverages and generates overpayment for ineligible amounts
> 4. **Given** accumulator balances approach limits, **When** adjuster submits claim, **Then** system prevents payment exceeding minimum of single accumulator, group accumulator, and prorated time-based limits
> 5. **Given** post-payment quantity adjustments, **When** recalculation occurs, **Then** system updates used amounts, generates overpayments if new amount is less than paid, and adjusts remaining balances accordingly
> 6. **Given** claim approval, **When** status changes to approved, **Then** system updates reserve amounts; **When** payment issues, **Then** reserve converts to used amount across all affected accumulators


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=715130770"
> ]

---

#### Feature: As a Claims Adjuster, I want the system to handle date ranges that span calendar or benefit year boundaries by splitting accumulators appropriately, so that limits are correctly applied across year transitions.
- **Role**: Claim Adjuster
- **Action**: enable automated splitting of accumulators when claim date ranges span calendar or benefit year boundaries
- **Value**: limits are accurately applied across year transitions, preventing overpayments and ensuring policy compliance without manual intervention

**Description:**

> As a **Claim Adjuster**,
> I want to **enable automated splitting of accumulators when claim date ranges span calendar or benefit year boundaries**,
> So that **limits are accurately applied across year transitions, preventing overpayments and ensuring policy compliance without manual intervention**


**Key Capabilities:**

> 1. System identifies when claim date ranges cross calendar year (Jan 1–Dec 31) or benefit year (policy effective date anniversary) boundaries.
> 2. System automatically splits date range into separate periods at the year boundary, assigning days before the boundary to the prior year and days after to the new year.
> 3. System calculates remaining amounts for each period using formula: min[single accumulator remaining, (remaining days in year × daily benefit), group accumulator remaining].
> 4. Upon settlement approval, system reserves amounts against appropriate year accumulators for each split period.
> 5. Upon payment issuance, system updates Used and Remaining values independently for each year's accumulator tracking.
> 6. System resets benefit limits for new year period while maintaining historical utilization for reporting.


**Acceptance Criteria:**

> 1. **Given** a claim with date range 12/28/2023–01/05/2024, **When** adjudication occurs, **Then** system splits into two periods (12/28–12/31 and 01/01–01/05) with separate accumulator calculations.
> 2. **Given** benefit year starts July 1 with 15-day limit, **When** claim spans 06/25–07/10, **Then** system deducts 6 days from prior year (leaving 9) and 9 days from new year (leaving 6).
> 3. **Given** remaining calendar year days (22) are less than accumulator limit (30 days), **When** calculating payment, **Then** system limits to actual remaining days multiplied by daily benefit rate.
> 4. **Given** settlement approved across year boundary, **When** payment issued, **Then** system updates Reserved and Used amounts independently for each year period without cross-contamination.
> 5. **Given** group accumulator constraints exist, **When** splitting periods, **Then** system applies group limits separately to each year's calculations.
> 6. **Given** year transition occurs, **When** new period begins, **Then** system resets limits for new year while preserving prior year historical data for audit trails.


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=715130770"
> ]

---

#### Feature: As a Claims Adjuster, I want the system to convert non-monetary accumulator units to money amounts for calculation purposes, so that single and group accumulators can be compared and enforced consistently.
- **Role**: Claim Adjuster
- **Action**: convert non-monetary accumulator units to monetary amounts for calculation purposes
- **Value**: single and group accumulators can be compared and enforced consistently regardless of their original measurement units

**Description:**

> As a **Claim Adjuster**,
> I want to **convert non-monetary accumulator units to monetary amounts for calculation purposes**,
> So that **single and group accumulators can be compared and enforced consistently regardless of their original measurement units**


**Key Capabilities:**

> 1. System converts unit-based accumulator amounts (days/trips/occurrences) to monetary equivalents using benefit amount per unit formula
>     1.1 When benefit adjustments apply (age reduction, dependent percentage), system applies modifiers before conversion
> 2. System calculates settlement remaining amounts by comparing converted single accumulator limits against group accumulator monetary limits
> 3. System determines actual remaining amount by combining settlement remaining with settlement used amounts
> 4. Upon completing calculations, system converts monetary results back to original unit measurements when accumulator is unit-based
> 5. System applies converted amounts to determine claim gross benefit allocation and enforce policy limits
> 6. When date ranges cross year boundaries, system splits calculations by period and applies conversions within each year's context


**Acceptance Criteria:**

> 1. **Given** single accumulator measured in days and group accumulator in dollars, **When** adjudicating settlement, **Then** system converts day units to monetary amounts for comparison and enforces minimum of both limits
> 2. **Given** benefit amount adjustments exist (age/dependent percentages), **When** converting units to money, **Then** system applies modifiers before unit conversion calculation
> 3. **Given** calculations complete in monetary terms, **When** original accumulator unit is non-monetary, **Then** system converts results back to unit amounts rounded to two decimals
> 4. **Given** settlement remaining and used amounts calculated, **When** determining actual remaining, **Then** system sums both amounts to establish available benefit
> 5. **Given** date range crosses calendar or benefit year boundary, **When** converting units, **Then** system performs separate conversions for each period within respective year limits
> 6. **Given** conversion produces overpayment condition, **When** recalculating accumulator amounts, **Then** system prevents submission of allocations exceeding converted remaining amounts


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=715130770"
> ]

---

#### Feature: As a Claims Adjuster, I want the system to support accumulator actions including Create, Reserve, Use, Recover, Clear, and Adjust, so that I can manage the full lifecycle of benefit limits through coverage and payment changes.
- **Role**: Claim Adjuster
- **Action**: Manage accumulator lifecycle through Create, Reserve, Use, Recover, Clear, and Adjust actions to track and control benefit limits across coverage adjudication and payment changes
- **Value**: I can accurately monitor and enforce benefit consumption, prevent overpayments, and maintain real-time visibility of remaining coverage limits throughout the claim lifecycle

**Description:**

> As a **Claim Adjuster**,
> I want to **manage accumulator lifecycle through Create, Reserve, Use, Recover, Clear, and Adjust actions to track and control benefit limits across coverage adjudication and payment changes**,
> So that **I can accurately monitor and enforce benefit consumption, prevent overpayments, and maintain real-time visibility of remaining coverage limits throughout the claim lifecycle**


**Key Capabilities:**

> 1. Upon adding coverage, system generates non-time/non-dynamic-group accumulators with initial limits and calculates gross amounts constrained by remaining balances
> 2. Upon saving eligible coverage with approved settlement, system reserves gross amount from remaining balance and generates time-period/dynamic-group accumulators
> 3. When payment is issued, system transfers reserved amount to used amount, updating remaining balance
> 4. When payment is declined/voided/stopped, system recovers used amounts to reserve or clears reserve back to remaining based on payment state
> 5. When coverage is cancelled or set non-eligible, system clears reserved amounts to remaining balance
> 6. When Face Value is overridden or dynamic group limits change, system adjusts limits and re-reserves based on latest approved settlements


**Acceptance Criteria:**

> 1. **Given** coverage is added, **When** accumulator creation is triggered, **Then** system initializes limit and remaining amounts with reserve and used at zero
> 2. **Given** eligible coverage with approved settlement, **When** saved, **Then** system reserves gross amount calculated as MIN(coverage amount, claim remaining, group remaining)
> 3. **Given** payment is issued, **When** accumulator update occurs, **Then** system moves full reserved amount to used amount
> 4. **Given** payment is declined/voided, **When** recovery is triggered, **Then** system returns used amount to reserve maintaining limit integrity
> 5. **Given** coverage is cancelled, **When** accumulator adjustment occurs, **Then** system clears all reserved amounts to remaining for individual and group accumulators
> 6. **Given** Face Value override or dynamic group limit change, **When** adjustment occurs, **Then** system recalculates limits and re-reserves based on latest approved settlement amounts


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=618282188"
> ]

---

#### Feature: As a Claims Adjuster, I want the system to calculate dynamic group limits based on the highest benefit amount within a coverage group, so that group limits accurately reflect policy multipliers and coverage changes.
- **Role**: Claim Adjuster
- **Action**: have the system automatically calculate and enforce dynamic group limits based on the highest benefit amount within coverage groups, applying policy multipliers and reflecting coverage changes
- **Value**: group limits accurately reflect actual policy terms, prevent overpayment across grouped coverages, and ensure compliant benefit adjudication without manual recalculation

**Description:**

> As a **Claim Adjuster**,
> I want to **have the system automatically calculate and enforce dynamic group limits based on the highest benefit amount within coverage groups, applying policy multipliers and reflecting coverage changes**,
> So that **group limits accurately reflect actual policy terms, prevent overpayment across grouped coverages, and ensure compliant benefit adjudication without manual recalculation**.


**Key Capabilities:**

> 1. System generates group-level accumulators when coverage groups are saved, identifying coverages sharing common limit pools
> 2. System identifies the highest base benefit amount within the coverage group automatically upon coverage operations
> 3. System calculates dynamic group limit by applying policy multiplier to the highest identified base amount
>     3.1 Upon coverage amount changes, system recalculates group limit based on new highest amount
> 4. System tracks settled amounts across all coverages within the group against the calculated group limit
> 5. System calculates remaining group capacity as (Multiplier × Highest Base Amount) minus total settled amount across grouped coverages
> 6. System enforces remaining capacity during claim adjudication, preventing payments exceeding dynamic group limit


**Acceptance Criteria:**

> 1. **Given** multiple coverages exist within a coverage group, **When** coverage operations complete, **Then** system identifies and stores the highest base benefit amount as the calculation baseline
> 2. **Given** a policy multiplier is defined, **When** group limit is calculated, **Then** system applies multiplier to highest base amount to determine total group capacity
> 3. **Given** coverage amounts change within the group, **When** coverage is saved, **Then** system recalculates group limit using the new highest base amount without manual intervention
> 4. **Given** indemnity payments are issued across grouped coverages, **When** settled amounts accumulate, **Then** system tracks total usage against the dynamically calculated group limit
> 5. **Given** remaining group capacity is insufficient, **When** adjudication occurs, **Then** system prevents payment approval and notifies adjuster of limit constraint
> 6. **Given** group limit calculations complete, **When** adjudicator reviews claim, **Then** system displays calculated limit, highest base amount, multiplier, and remaining capacity


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=680309580"
> ]

---

#### Feature: As a Claims Adjuster, I want the system to recalculate accumulators when coverages are cancelled or marked non-eligible, so that remaining limits are adjusted to reflect the current active coverage portfolio.
- **Role**: Claim Adjuster
- **Action**: trigger automatic accumulator recalculation when coverages are cancelled or marked non-eligible to adjust remaining policy limits
- **Value**: the available benefit limits accurately reflect the current active coverage portfolio, preventing overpayment and maintaining policy compliance

**Description:**

> As a **Claim Adjuster**,
> I want to **trigger automatic accumulator recalculation when coverages are cancelled or marked non-eligible to adjust remaining policy limits**,
> So that **the available benefit limits accurately reflect the current active coverage portfolio, preventing overpayment and maintaining policy compliance**.


**Key Capabilities:**

> 1. **Coverage Status Change Detection**: System identifies when coverages are cancelled or marked non-eligible, triggering accumulator recalculation workflows.
> 2. **Reserved Amount Clearance**: Upon coverage cancellation or non-eligibility designation, system executes Clear action to return reserved amounts to remaining limit pool.
>     2.1 Single accumulator limits update immediately.
>     2.2 Group accumulators adjust proportionally based on active coverage composition.
> 3. **Dynamic Group Limit Adjustment**: For group accumulators (e.g., Death, Fracture/Dislocation groups), system filters settlements where coverage is cancelled and recalculates maximum benefit among remaining active coverages.
> 4. **Real-time Limit Display**: System updates used, reserved, and remaining amounts across all affected accumulator types (per individual, per event, per calendar year, per lifetime).
> 5. **Transaction Audit Trail**: System persists all accumulator adjustments as transaction records with action type, timestamp, and coverage reference.
> 6. **Re-adjudication Support**: When cancelled coverages are reinstated and saved, system re-reserves amounts and updates limits to reflect restored coverage portfolio.


**Acceptance Criteria:**

> 1. **Given** a coverage with reserved amounts **When** the adjuster cancels the coverage **Then** the system executes Clear action and returns reserved amount to remaining limit for all associated accumulators.
> 2. **Given** a coverage marked eligible with settlement approved **When** the adjuster changes status to non-eligible **Then** the system moves reserved amount to remaining and displays updated limit availability.
> 3. **Given** a dynamic group accumulator (e.g., Group Death Limit) **When** the maximum benefit coverage within the group is cancelled **Then** the system recalculates group limit based on next highest active coverage and adjusts remaining amount accordingly.
> 4. **Given** multiple accumulator types (per event, per calendar year, per policy) **When** a coverage is cancelled **Then** the system updates all applicable accumulator types simultaneously and displays synchronized remaining limits.
> 5. **Given** a cancelled coverage **When** the adjuster reinstates and saves the coverage as eligible **Then** the system re-reserves gross amount and reduces remaining limit to reflect restored coverage.
> 6. **Given** accumulator adjustments occur **When** the system completes recalculation **Then** transaction records persist with action type Clear, adjusted amounts, and coverage reference for audit compliance.


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=618282188"
> ]

---

#### Feature: As a Claims Adjuster, I want the system to display remaining limits as zero or negative values appropriately, so that I can identify when planned amounts exceed policy limits and manage overpayment scenarios.
- **Role**: Claim Adjuster
- **Action**: monitor accumulator-based remaining limits to identify overpayment scenarios and enforce policy constraints during claim adjudication
- **Value**: I can proactively detect when planned payment amounts exceed available policy limits, prevent unauthorized overpayments, and maintain accurate financial tracking across coverage lifecycles

**Description:**

> As a **Claim Adjuster**,
> I want to **monitor accumulator-based remaining limits to identify overpayment scenarios and enforce policy constraints during claim adjudication**,
> So that **I can proactively detect when planned payment amounts exceed available policy limits, prevent unauthorized overpayments, and maintain accurate financial tracking across coverage lifecycles**.


**Key Capabilities:**

> 1. Upon coverage confirmation or save, system calculates gross amounts constrained by MIN(coverage calculated amount, individual remaining, group remaining) and displays current limit consumption status
> 2. When settlement is approved, system reserves planned amounts and reduces remaining balance; displays zero or negative values in UI when planned amounts exceed available limits
> 3. Upon payment issuance, system transitions reserved amounts to used status and recalculates remaining capacity across affected accumulators
> 4. When payment lifecycle events occur (cancellations, voids, stops, recoveries), system executes appropriate action sequences to restore amounts to correct accumulator states
> 5. If face value is overridden or dynamic group limits change, system adjusts limits and recalculates remaining balances across dependent coverages
> 6. System persists all accumulator transactions (Create, Reserve, Use, Recover, Clear, Adjust) and displays aggregate consumption metrics


**Acceptance Criteria:**

> 1. **Given** coverage with remaining limit below planned amount, **When** adjuster confirms coverage, **Then** system displays remaining balance as zero/negative and constrains gross amount calculation to available limit
> 2. **Given** approved settlement, **When** system reserves gross amount, **Then** remaining balance decreases by reserved amount and reflects negative values if exceeding limit
> 3. **Given** issued payment, **When** payment transitions to used status, **Then** system moves reserved amount to used and maintains accurate remaining calculation
> 4. **Given** payment cancellation or void, **When** adjuster processes reversal, **Then** system returns amounts to appropriate state (used to reserved, or reserved to remaining) per action rules
> 5. **Given** face value override, **When** system recalculates limits, **Then** all dependent accumulators reflect updated limit and remaining amounts across affected coverages
> 6. **Given** dynamic group limit with cancelled maximum benefit coverage, **When** system recalculates group limit, **Then** limit adjusts to next highest benefit and remaining balances update accordingly


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=618282188"
> ]

---
## Initiative: Payment Scheduling & Calculation

### Epic: Payment Generation & Posting

#### Feature: As a Claims Adjuster, I want to view generated payments in a consolidated list, so that I can monitor payment status and take necessary actions
- **Role**: Claim Adjuster
- **Action**: monitor generated payments and manage payment lifecycle actions
- **Value**: I can track payment execution status, identify exceptions, and take corrective actions to ensure timely claim settlements

**Description:**

> As a **Claim Adjuster**,
> I want to **monitor generated payments and manage payment lifecycle actions**,
> So that **I can track payment execution status, identify exceptions, and take corrective actions to ensure timely claim settlements**


**Key Capabilities:**

> 1. User is able to view consolidated payment information combining scheduled entries and issued payments with assigned payment numbers
> 2. Upon payment post date passing and issuance completion, system displays only actual payment records while hiding corresponding scheduled entries
> 3. When payment requires cancellation in Approved status, user is able to cancel payment schedule and all non-issued payments
> 4. If issued Check payment requires intervention while in Pending status on Payment Hub, user is able to submit stop payment request
> 5. When issued payment requires voiding, user is able to decline/void payment through Payment Hub integration
> 6. System distinguishes payment processing between Check payments (pending status allowed) and EFT payments (immediate processing to paid status)


**Acceptance Criteria:**

> 1. **Given** payment schedule is approved and payments are generated, **When** adjuster accesses payment list, **Then** system displays both scheduled future payments and issued payments with payment numbers
> 2. **Given** payment post date has passed and payment is issued, **When** payment list is viewed, **Then** system displays only actual payment record and hides scheduled entry
> 3. **Given** payment is in Approved status, **When** adjuster initiates cancellation, **Then** system cancels payment schedule and prevents issuance of non-issued payments
> 4. **Given** Check payment is issued with Pending status on Payment Hub, **When** adjuster submits stop payment request, **Then** system processes stop request via Payment Hub integration
> 5. **Given** payment is issued, **When** adjuster declines/voids payment, **Then** system sets Check payments to Failed-Voided and EFT payments to Failed-Declined
> 6. **Given** payment is generated, **When** adjuster attempts updates, **Then** system prevents modification of actual payments and applies changes only to payment schedule with recalculated balances


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=761792191"
> ]

---

#### Feature: As a Claims Adjuster, I want to cancel approved payments before they are issued, so that I can prevent unwanted payments from being processed
- **Role**: Claim Adjuster
- **Action**: cancel approved payments before they are issued to payees
- **Value**: I can prevent unwanted or erroneous payments from being processed and maintain accurate claim financials

**Description:**

> As a **Claim Adjuster**,
> I want to **cancel approved payments before they are issued to payees**,
> So that **I can prevent unwanted or erroneous payments from being processed and maintain accurate claim financials**


**Key Capabilities:**

> 1. User identifies payment requiring cancellation from the payment list while in 'Approved' status
> 2. User initiates cancellation action on the target payment schedule
> 3. System cancels the payment schedule and all associated non-issued payments
> 4. System updates payment status and recalculates claim financial balances
> 5. Upon cancellation, system prevents the payment from advancing to 'Issued' status
>     5.1 If payment schedule contains multiple payments, all non-issued payments are cancelled
>     5.2 If payment already transitioned to 'Issued' status, cancellation is unavailable and alternative actions apply


**Acceptance Criteria:**

> 1. **Given** a payment in 'Approved' status, **when** the adjuster executes the cancel action, **then** the system cancels the payment schedule and all non-issued payments
> 2. **Given** a payment already in 'Issued' status, **when** the adjuster attempts cancellation, **then** the system prevents cancellation and indicates alternative remediation options
> 3. **Given** successful payment cancellation, **when** the system processes the request, **then** claim financial balances are recalculated and reflected in the payment list
> 4. **Given** a cancelled payment, **when** viewing the payment list, **then** the payment no longer appears as pending issuance
> 5. **Given** an automated payment generation cycle, **when** payments are cancelled before the cycle executes, **then** those payments are excluded from generation and issuing processes


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=761792191"
> ]

---

#### Feature: As a Claims Adjuster, I want to request payment stop for issued check payments, so that I can prevent payment delivery if needed
- **Role**: Claim Adjuster
- **Action**: request payment stop for issued check payments to prevent delivery when circumstances require intervention
- **Value**: I can exercise control over issued check payments and prevent inappropriate disbursements when exceptions occur after payment issuance

**Description:**

> As a **Claim Adjuster**,
> I want to **request payment stop for issued check payments to prevent delivery when circumstances require intervention**,
> So that **I can exercise control over issued check payments and prevent inappropriate disbursements when exceptions occur after payment issuance**


**Key Capabilities:**

> 1. System identifies issued check payments eligible for stop request based on pending status in Payment Hub
> 2. User initiates stop payment request for selected issued check payment through payment management interface
> 3. System validates payment method is check and current status permits stop action
> 4. Upon validation success, system transmits stop request to Payment Hub via API
> 5. System updates payment status to Stop Requested reflecting intervention action
>     5.1 When stop request fails validation, system prevents action and notifies user of ineligibility
> 6. User monitors payment status progression following stop request submission


**Acceptance Criteria:**

> 1. **Given** a check payment with Issued status and Pending status on Payment Hub, **When** adjuster requests payment stop, **Then** system successfully processes stop request and updates status to Stop Requested
> 2. **Given** an EFT payment with Issued status, **When** adjuster attempts stop request, **Then** system prevents action indicating stop unavailable for EFT method
> 3. **Given** a check payment with Paid status on Payment Hub, **When** adjuster attempts stop request, **Then** system prevents action as payment already processed
> 4. **Given** successful stop request submission, **When** system communicates with Payment Hub, **Then** payment delivery process is halted preventing disbursement


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=761792191"
> ]

---

#### Feature: As a Claims Adjuster, I want to decline or void issued payments, so that I can fail payments that should not be processed
- **Role**: Claim Adjuster
- **Action**: decline or void issued payments that should not be processed
- **Value**: I can prevent erroneous or inappropriate payments from being completed and maintain accurate claim financial integrity

**Description:**

> As a **Claim Adjuster**,
> I want to **decline or void issued payments that should not be processed**,
> So that **I can prevent erroneous or inappropriate payments from being completed and maintain accurate claim financial integrity**


**Key Capabilities:**

> 1. User identifies issued payments requiring intervention from the payment list
> 2. User initiates decline or void action on issued payment based on current Payment Hub status
> 3. System executes payment failure via Payment Hub API according to payment method
>     3.1 Check payments transition to Failed-Voided status
>     3.2 EFT payments transition to Failed-Declined status
> 4. System recalculates claim financial balances reflecting the voided payment
> 5. System maintains audit trail of void action and updates payment lifecycle state
> 6. User confirms payment failure completion and reviews updated claim financials


**Acceptance Criteria:**

> 1. **Given** a payment is in Issued status, **When** adjuster initiates decline/void action, **Then** system executes payment failure through Payment Hub API
> 2. **Given** a Check payment is voided, **When** processing completes, **Then** payment status becomes Failed-Voided
> 3. **Given** an EFT payment is declined, **When** processing completes, **Then** payment status becomes Failed-Declined
> 4. **Given** payment is voided successfully, **When** system processes the action, **Then** claim balances recalculate automatically
> 5. **Given** payment void is completed, **When** viewing payment history, **Then** complete audit trail of action is maintained
> 6. **Given** payment is not in Issued status, **When** void action is attempted, **Then** system prevents execution of decline/void operation


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=761792191"
> ]

---

#### Feature: As a Claims Operations Manager, I want the system to automatically generate payments from active payment schedules on their scheduled post dates, so that payments are created without manual intervention
- **Role**: Claim Adjuster
- **Action**: automatically generate and issue payments from active payment schedules on their scheduled post dates without manual intervention
- **Value**: operational efficiency is improved, processing time is reduced, and payment delivery is timely and consistent across all payees

**Description:**

> As a **Claim Adjuster**,
> I want to **automatically generate and issue payments from active payment schedules on their scheduled post dates without manual intervention**,
> So that **operational efficiency is improved, processing time is reduced, and payment delivery is timely and consistent across all payees**


**Key Capabilities:**

> 1. System filters active payment schedules and selects allocations due for payment based on scheduled post date
>     1.1 Upon identifying eligible allocations, system enforces business rules ensuring one active schedule per event case or claim
>     1.2 System regenerates previously failed payments when schedules are updated or rescheduled
> 2. System creates approved payments for eligible allocations and transitions them to issue-requested status
> 3. System validates payment amount and resolves payee data, payment method, and method details from external systems
> 4. Upon successful validation, system dispatches payment to Payment Hub and marks payment as issued
> 5. When payment amount is zero or negative for recovery payments, system marks payment as issued without dispatch
> 6. If critical issues occur during dispatch, system deactivates schedule, cancels payments, and generates task for resolution


**Acceptance Criteria:**

> 1. **Given** active payment schedules exist with allocations due today, **When** payment generation executes, **Then** system creates approved payments for all eligible allocations
> 2. **Given** approved payments are created, **When** payment issuing executes, **Then** system successfully dispatches payments to Payment Hub and assigns issued status
> 3. **Given** payment amount is zero or negative for recovery, **When** issuing validates amount, **Then** system assigns issued status without dispatching to Payment Hub
> 4. **Given** payment data validation fails, **When** dispatch is attempted, **Then** system assigns failed status and generates review task
> 5. **Given** critical issues occur during dispatch, **When** system detects error, **Then** system deactivates schedule, cancels payments, and creates cancellation task
> 6. **Given** user resolves cancellation task, **When** task is marked done, **Then** system reschedules payments for next generation cycle


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=761792192"
> ]

---

#### Feature: As a Claims Operations Manager, I want the system to validate payment data and resolve payment methods before issuing payments, so that only valid payments are dispatched to the Payment Hub
- **Role**: Claim Manager
- **Action**: validate payment data and resolve payment methods before dispatching payments to the Payment Hub
- **Value**: only validated and complete payments are issued, reducing payment failures and manual intervention

**Description:**

> As a **Claim Manager**,
> I want to **validate payment data and resolve payment methods before dispatching payments to the Payment Hub**,
> So that **only validated and complete payments are issued, reducing payment failures and manual intervention**.


**Key Capabilities:**

> 1. System initiates payment issuing process for all approved payments and transitions them to 'Issue Requested' status.
> 2. System retrieves payee information from CEM or Provider Management Studio based on payee type.
> 3. System resolves payment method by checking allocation-level settings, then CEM preferred method, then predefined rules.
> 4. System validates completeness and accuracy of payment data including payee details and payment method information.
> 5. Upon successful validation, system creates outbound payment transaction to Payment Hub and transitions payment to 'Issued' status.
>     5.1 When validation fails, system assigns 'Failed' status and generates review task.
>     5.2 When payment amount is zero or negative, system auto-issues without Payment Hub dispatch.


**Acceptance Criteria:**

> 1. **Given** approved payments exist, **When** issuing process runs, **Then** system transitions all eligible payments to 'Issue Requested' status.
> 2. **Given** payment method is not specified at allocation level, **When** system resolves payment method, **Then** system checks CEM preferred method before applying predefined rules.
> 3. **Given** payee data is incomplete or invalid, **When** system validates payment data, **Then** system prevents Payment Hub dispatch and assigns 'Failed' status.
> 4. **Given** all payment data is valid, **When** system completes validation, **Then** system creates Payment Hub transaction and transitions payment to 'Issued' status.
> 5. **Given** Payment Hub returns failure response, **When** system receives response, **Then** system assigns 'Failed' status and generates manual review task.
> 6. **Given** payment amount is zero or negative, **When** system processes payment, **Then** system auto-issues payment without Payment Hub dispatch.


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=761792192"
> ]

---

#### Feature: As a Claims Operations Manager, I want the system to automatically issue approved payments to the Payment Hub, so that payments are dispatched efficiently without manual processing
- **Role**: Claim Adjuster
- **Action**: automatically generate approved payments from active schedules and dispatch them to the Payment Hub
- **Value**: payments are issued efficiently without manual processing, reducing operational overhead and accelerating payment delivery to payees

**Description:**

> As a **Claim Adjuster**,
> I want to **automatically generate approved payments from active schedules and dispatch them to the Payment Hub**,
> So that **payments are issued efficiently without manual processing, reducing operational overhead and accelerating payment delivery to payees**.


**Key Capabilities:**

> 1. System executes automated payment generation job to identify active payment schedules and select payments due based on payment date criteria.
> 2. System creates actual payments with approved status for eligible payment allocations.
> 3. System executes automated payment issuing job to collect approved payments and initiate dispatch process.
>     3.1 When payment amount is zero or negative, system assigns issued status without hub transaction.
>     3.2 When payment amount is positive, system retrieves and validates payee data from integrated systems.
> 4. System resolves payment method and details from customer or vendor management systems.
> 5. System generates dispatch request to Payment Hub and assigns issued status upon successful transmission.
> 6. Upon dispatch failure or critical validation issues, system creates review tasks and triggers exception workflows for manual intervention.


**Acceptance Criteria:**

> 1. **Given** an active payment schedule with payments due, **When** generation job executes, **Then** system creates approved payments for all eligible allocations based on payment date criteria.
> 2. **Given** approved payments exist, **When** issuing job executes, **Then** system validates payee data and dispatches positive-amount payments to Payment Hub while auto-issuing zero/negative amounts.
> 3. **Given** successful Payment Hub transmission, **When** dispatch completes, **Then** system assigns issued status to payments without manual intervention.
> 4. **Given** Payment Hub returns failure response, **When** dispatch fails, **Then** system assigns failed status and generates review task for manual resolution.
> 5. **Given** critical validation issues during dispatch preparation, **When** errors are detected, **Then** system cancels payments, deactivates schedule, and creates task to trigger rescheduling upon completion.
> 6. **Given** payment method is undefined, **When** system resolves payment details, **Then** system applies predefined rules using customer preferred method or fallback logic.


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=761792192"
> ]

---

#### Feature: As a Claims Operations Manager, I want the system to handle zero or negative payment amounts by marking them as issued without Payment Hub dispatch, so that recovery and adjustment payments are processed correctly
- **Role**: Claim Adjuster
- **Action**: enable automated system processing of payment schedules with special handling for zero or negative payment amounts
- **Value**: recovery and adjustment payments complete without manual intervention while maintaining accurate financial records

**Description:**

> As a **Claim Adjuster**,
> I want to **enable automated system processing of payment schedules with special handling for zero or negative payment amounts**,
> So that **recovery and adjustment payments complete without manual intervention while maintaining accurate financial records**


**Key Capabilities:**

> 1. System automatically generates payments from active schedules where payment date equals or precedes current system time
> 2. Upon payment creation, system assigns 'Approved' status and queues for issuing process
> 3. System evaluates payment amount during issuing:
>     3.1 When amount is zero or negative, system assigns 'Issued' status without Payment Hub dispatch
>     3.2 When amount is positive, system retrieves payee data and creates Payment Hub transaction
> 4. System resolves payment method hierarchy from allocation settings, customer preferences, or predefined rules
> 5. When Payment Hub returns failure, system assigns 'Failed' status and generates review task
> 6. Upon critical validation errors, system deactivates schedule, cancels payments, and triggers automated rescheduling workflow


**Acceptance Criteria:**

> 1. **Given** active payment schedule with zero amount, **When** issuing job executes, **Then** system marks payment 'Issued' without Payment Hub dispatch
> 2. **Given** active payment schedule with negative amount, **When** issuing job executes, **Then** system marks payment 'Issued' and completes process locally
> 3. **Given** active payment schedule with positive amount, **When** issuing job executes, **Then** system retrieves payee data and creates Payment Hub transaction
> 4. **Given** Payment Hub dispatch failure, **When** response received, **Then** system assigns 'Failed' status and generates review task
> 5. **Given** critical validation errors, **When** issuing attempted, **Then** system deactivates schedule and triggers automated rescheduling
> 6. **Given** payment date at or before current time, **When** generation job runs, **Then** system creates payments with 'Approved' status


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=761792192"
> ]

---

#### Feature: As a Claims Operations Manager, I want the system to track payment lifecycle states and enforce valid state transitions, so that payments follow the correct business process flow
- **Role**: Claim Adjuster
- **Action**: track payment progression through predefined lifecycle states and enforce valid state transitions
- **Value**: payments follow the correct business process flow from creation to final disposition with proper audit trail and compliance

**Description:**

> As a **Claim Adjuster**,
> I want to **track payment progression through predefined lifecycle states and enforce valid state transitions**,
> So that **payments follow the correct business process flow from creation to final disposition with proper audit trail and compliance**


**Key Capabilities:**

> 1. System initiates payment in Approved state upon creation with unique identifier
> 2. System progresses payment to Issue Requested when issuing begins and transmits information to Payment Hub
> 3. System advances payment to Issued state upon successful delivery to check-writing or banking system
>     3.1 Upon last payment issued from schedule, system evaluates completion rules and triggers schedule completion when conditions met
> 4. System transitions payment to Canceled state when cancellation is requested with reason documentation
> 5. System manages stop payment workflow by transitioning to Stop Requested then automatically resolving to Issued or Failed based on Payment Hub response
> 6. System captures failure reasons and transitions payment to Failed state when issuing fails or payment is voided/stopped/declined


**Acceptance Criteria:**

> 1. **Given** payment is created, **when** initiation completes, **then** system assigns Approved state with unique payment number
> 2. **Given** payment in Approved state, **when** issue request submitted, **then** system transitions to Issue Requested and notifies Payment Hub
> 3. **Given** payment successfully delivered, **when** confirmation received, **then** system transitions to Issued and evaluates schedule completion if applicable
> 4. **Given** payment requires cancellation, **when** cancellation requested with reason, **then** system transitions to Canceled terminal state
> 5. **Given** issued payment requires stop, **when** stop requested, **then** system transitions to Stop Requested and automatically resolves to Issued or Failed based on hub response
> 6. **Given** payment encounters failure, **when** failure detected with reason code, **then** system transitions to Failed terminal state and records reason


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=761792187",
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=413375737"
> ]

---

#### Feature: As a System Administrator, I want to configure payment generation and issuing jobs to run at scheduled intervals, so that payments are processed automatically without user intervention
- **Role**: Claim Manager
- **Action**: configure automated payment generation and issuing jobs to execute at scheduled intervals
- **Value**: payments are processed systematically without manual intervention, ensuring timely disbursement to payees

**Description:**

> As a **Claim Manager**,
> I want to **configure automated payment generation and issuing jobs to execute at scheduled intervals**,
> So that **payments are processed systematically without manual intervention, ensuring timely disbursement to payees**


**Key Capabilities:**

> 1. System executes payment generation job at configured intervals, identifying active payment schedules eligible for processing and invoking generation rules
> 2. System filters eligible schedules, selects payments due by current date, and creates approved payments including overdue allocations
> 3. System executes payment issuing job, collecting approved payments and generating dispatch requests to Payment Hub
> 4. System retrieves payee data, resolves payment methods and details from enterprise systems, validates payment information
> 5. Upon successful validation, system creates outbound transactions and assigns issued status; for zero/negative amounts, system bypasses dispatch and assigns issued status automatically
> 6. When dispatch fails or critical issues occur, system assigns failure status, generates review tasks, and supports payment regeneration after schedule correction


**Acceptance Criteria:**

> 1. **Given** active payment schedules exist with due dates, **When** generation job executes, **Then** system creates approved payments for all eligible allocations including overdue items
> 2. **Given** approved payments exist, **When** issuing job executes, **Then** system dispatches payments to Payment Hub and assigns issued status upon confirmation
> 3. **Given** payment amount is zero or negative, **When** issuing process runs, **Then** system assigns issued status without creating external dispatch request
> 4. **Given** Payment Hub returns failure response, **When** system receives notification, **Then** payment receives failed status and review task generates for manual intervention
> 5. **Given** critical dispatch issues occur, **When** system detects errors, **Then** payment schedule deactivates, payments cancel, and resolution task creates for user action
> 6. **Given** failed payments have rescheduled allocations, **When** generation job executes, **Then** system includes regenerated payments in processing cycle


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=761792192"
> ]

---

#### Feature: As a Claims Adjuster, I want to manually trigger payment generation and issuing for testing purposes, so that I can verify payment processing workflows
- **Role**: Claim Adjuster
- **Action**: manually trigger payment generation and issuing processes for approved payment schedules in test environments
- **Value**: I can validate payment processing workflows, verify system integrations with Payment Hub, and ensure payment state transitions function correctly before production deployment

**Description:**

> As a **Claim Adjuster**,
> I want to **manually trigger payment generation and issuing processes for approved payment schedules in test environments**,
> So that **I can validate payment processing workflows, verify system integrations with Payment Hub, and ensure payment state transitions function correctly before production deployment**


**Key Capabilities:**

> 1. User initiates manual payment generation for approved payment schedules in test environment
> 2. System generates payments and assigns payment numbers to approved scheduled entries
>     2.1 When payment method is Check, system creates payment with Payment Hub status 'Pending'
>     2.2 When payment method is EFT, system processes immediately and transitions Payment Hub status to 'Paid'
> 3. System transitions payment status from 'Approved' to 'Issued' upon successful generation
> 4. User verifies payment list displays actual payments with assigned numbers while hiding superseded scheduled entries
> 5. User validates payment hub integration and confirms payment state synchronization
> 6. Upon exception, user reviews error conditions and adjusts test data or configuration accordingly


**Acceptance Criteria:**

> 1. **Given** an approved payment schedule exists, **When** user manually triggers payment generation, **Then** system creates payments with assigned numbers and 'Issued' status
> 2. **Given** payments are generated for Check method, **When** Payment Hub receives request, **Then** payments maintain 'Pending' status until further action
> 3. **Given** payments are generated for EFT method, **When** Payment Hub processes request, **Then** payments immediately transition to 'Paid' status
> 4. **Given** payments are issued, **When** user views payment list, **Then** system displays actual payments and hides corresponding scheduled entries
> 5. **Given** payment generation fails, **When** exception occurs, **Then** system prevents status transition and surfaces error details for user resolution
> 6. **Given** manual generation is attempted in production, **When** functionality is restricted, **Then** system prevents execution outside test environments


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=761792191"
> ]

---

### Epic: Payment Scheduling & Calculation

#### Feature: As a Claims Adjuster, I want to create and preview payment schedules with calculated payment amounts and dates, so that I can review and approve payments before they are issued
- **Role**: Claim Adjuster
- **Action**: create and preview payment schedules with calculated amounts and dates for eligible claims
- **Value**: I can ensure accurate financial disbursements are reviewed and approved before issuance

**Description:**

> As a **Claim Adjuster**,
> I want to **create and preview payment schedules with calculated amounts and dates for eligible claims**,
> So that **I can ensure accurate financial disbursements are reviewed and approved before issuance**


**Key Capabilities:**

> 1. User initiates payment creation for eligible open claims by selecting payee and defining allocations with coverage details
> 2. System executes calculation dry run, allowing user to preview computed amounts, dates, and reductions before committing
> 3. System combines new allocations with existing schedules when applicable and deactivates conflicting active schedules
> 4. System calculates net payment amounts by applying deductions, offsets, tax withholdings, and generating payment items based on claim type and frequency
> 5. System routes payment schedule for approval based on user authority, automatically approving or flagging for manual review
> 6. User reviews consolidated payment list showing scheduled payments with status indicators reflecting approval state


**Acceptance Criteria:**

> 1. **Given** an open adjudicated claim **When** user initiates payment creation **Then** system validates eligibility and allows allocation definition for single payee
> 2. **Given** allocations are defined **When** user requests calculation preview **Then** system displays computed amounts, dates, and applied reductions without finalizing
> 3. **Given** calculation preview is satisfactory **When** user confirms creation **Then** system combines with existing schedules or deactivates conflicting ones and generates new schedule
> 4. **Given** payment schedule is created **When** system applies user authority rules **Then** schedule is auto-approved or flagged as pending manual approval
> 5. **Given** schedule requires manual approval **When** authorized user reviews **Then** system transitions schedule to active and payments to pending post status
> 6. **Given** validation fails during allocation or calculation **Then** system prevents schedule creation and generates diagnostic messages


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=761792160"
> ]

---

#### Feature: As a Claims Adjuster, I want to define payment allocations (indemnity, expense, ex-gratia) with payee and claim details, so that I can specify which benefits and amounts should be paid
- **Role**: Claim Adjuster
- **Action**: define payment allocations with payee assignments and claim benefit details to establish what amounts should be paid and to whom
- **Value**: I can accurately specify benefit distributions across indemnity, expense, and ex-gratia categories while ensuring proper payee assignment and compliance with authority limits

**Description:**

> As a **Claim Adjuster**,
> I want to **define payment allocations with payee assignments and claim benefit details to establish what amounts should be paid and to whom**,
> So that **I can accurately specify benefit distributions across indemnity, expense, and ex-gratia categories while ensuring proper payee assignment and compliance with authority limits**


**Key Capabilities:**

> 1. User initiates allocation definition by selecting allocation type (indemnity, expense, or ex-gratia) and associating with target claim
>     1.1 For indemnity allocations: user links to specific coverage or benefit and defines allocation period
>     1.2 For expense and ex-gratia allocations: user enters amount directly without coverage linkage
> 2. User assigns payee from available parties (individuals, organizations, providers) and verifies payment method exists in customer entity management
> 3. System validates allocation data against business rules including authority limits, benefit eligibility, and payee configuration requirements
> 4. User provides allocation-specific financial parameters including benefit amounts, interest overrides, and applicable adjustment periods
> 5. System captures allocation details for downstream payment schedule generation including frequency indicators and proration requirements


**Acceptance Criteria:**

> 1. **Given** user selects indemnity allocation type, **When** defining allocation, **Then** system requires coverage/benefit selection and prevents submission without claim linkage
> 2. **Given** user assigns payee, **When** validating payee configuration, **Then** system confirms payment method exists and adds payee as party with 'Payee' role to case
> 3. **Given** user defines expense or ex-gratia allocation, **When** submitting for approval, **Then** system validates compliance with adjuster's authority limits before accepting
> 4. **Given** multiple allocation types defined on single claim, **When** user completes allocation entry, **Then** system retains all allocations for consolidated payment schedule generation
> 5. **Given** allocation requires period-based calculation, **When** user provides allocation period, **Then** system captures inclusive start and end dates for downstream proration
> 6. **Given** allocation data is incomplete, **When** user attempts submission, **Then** system prevents progression and indicates missing required elements per allocation type


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=761792164"
> ]

---

#### Feature: As a Claims Adjuster, I want to validate payment allocations to ensure no duplicate benefits are paid twice for the same claim event, so that claim integrity is maintained
- **Role**: Claim Adjuster
- **Action**: validate payment allocations against existing benefits to prevent duplicate payments for the same claim event
- **Value**: claim integrity is maintained and overpayments are avoided

**Description:**

> As a **Claim Adjuster**,
> I want to **validate payment allocations against existing benefits to prevent duplicate payments for the same claim event**,
> So that **claim integrity is maintained and overpayments are avoided**.


**Key Capabilities:**

> 1. User submits payment allocation data including allocation type, related claim linkage, and benefit period
> 2. System validates allocation integrity and completeness upon submission
> 3. System verifies no duplicate allocations exist among previously paid or newly submitted benefits for the same claim event
>     3.1 When duplicates detected, system halts processing and generates validation error
>     3.2 When validation passes, system proceeds to payment calculation
> 4. System applies overpayment validation rules upon payment schedule approval
> 5. System creates review tasks when validation exceptions or data errors occur during automated scheduling
> 6. User corrects validation errors and resubmits until integrity checks pass


**Acceptance Criteria:**

> 1. **Given** payment allocation data is submitted, **When** system validates allocation integrity, **Then** duplicate benefit verification executes against existing paid and pending allocations
> 2. **Given** duplicate allocation is detected for same claim event, **When** validation runs, **Then** system prevents payment creation and displays validation error requiring user correction
> 3. **Given** no duplicates exist, **When** validation completes successfully, **Then** system proceeds to payment calculation and scheduling
> 4. **Given** payment schedule is approved, **When** overpayment validation executes, **Then** system confirms no claim integrity violations before activation
> 5. **Given** validation exception occurs during automated scheduling, **When** system detects error, **Then** review task is created for manual intervention


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=761792170"
> ]

---

#### Feature: As a Claims Adjuster, I want to manage payment schedule lifecycle states (Open, Active, Suspended, Completed, Deactivated, Canceled), so that I can control when payments are generated and issued
- **Role**: Claim Adjuster
- **Action**: manage payment schedule lifecycle states to control payment generation and issuance
- **Value**: payment processing is governed through defined approval gates and state controls, ensuring financial accuracy and regulatory compliance

**Description:**

> As a **Claim Adjuster**,
> I want to **manage payment schedule lifecycle states to control payment generation and issuance**,
> So that **payment processing is governed through defined approval gates and state controls, ensuring financial accuracy and regulatory compliance**.


**Key Capabilities:**

> 1. **Initialize Payment Schedule**: System creates schedule in Open state upon validation that no active schedule exists for the same origin source
>     1.1 When duplicate schedule detected, prevent creation and notify adjuster
> 2. **Activate Payment Schedule**: Upon validation against business rules, transition approved schedule to Active state enabling payment generation
>     2.1 If business rule recommends review, maintain Open state pending resolution
> 3. **Generate Scheduled Payments**: When schedule is Active and approved, trigger payment creation process for scheduled disbursements
> 4. **Suspend/Unsuspend Processing**: User is able to temporarily pause Active schedules and resume when investigation concludes
> 5. **Deactivate Schedule**: Upon financial data changes, system automatically deactivates schedule requiring new schedule creation
> 6. **Complete or Cancel Schedule**: Transition schedule to terminal state when all payments issued or processing discontinued


**Acceptance Criteria:**

> 1. **Given** no existing schedule for origin source, **When** adjuster initiates schedule, **Then** system creates schedule in Open state preventing payment generation
> 2. **Given** schedule in Open state meeting business rule criteria, **When** activation requested, **Then** system transitions to Active state enabling payment processing
> 3. **Given** schedule in Active state, **When** payment generation triggered, **Then** system creates payments according to schedule parameters
> 4. **Given** Active schedule requiring temporary hold, **When** adjuster suspends schedule, **Then** payment generation stops and can resume via unsuspend command
> 5. **Given** financial data change invalidating schedule, **When** system detects discrepancy, **Then** schedule automatically deactivates requiring new schedule creation
> 6. **Given** schedule in any non-terminal state, **When** adjuster cancels, **Then** system prevents further payment generation and records cancellation reason


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=761792166",
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=555075586"
> ]

---

#### Feature: As a Claims Adjuster, I want to activate payment schedules based on authority level limits, so that payments requiring higher approval are flagged for review
- **Role**: Claim Adjuster
- **Action**: activate payment schedules based on authority level validation across multiple allocation categories
- **Value**: payments exceeding authority limits are automatically flagged for supervisory review, ensuring financial control and compliance

**Description:**

> As a **Claim Adjuster**,
> I want to **activate payment schedules based on authority level validation across multiple allocation categories**,
> So that **payments exceeding authority limits are automatically flagged for supervisory review, ensuring financial control and compliance**.


**Key Capabilities:**

> 1. System validates applicable LOBs (Disability, Life) against payment schedule allocations
> 2. System evaluates regular LOB allocations against user's line-of-business authority limits
>     2.1 Upon exceeding limits, system generates review flag for LOB allocations
> 3. System validates expense allocations against user's expense authority thresholds
>     3.1 Upon exceeding limits, system generates review flag for expense payments
> 4. System validates ex gratia allocations against user's ex gratia authority levels
>     4.1 Upon exceeding limits, system generates review flag for ex gratia payments
> 5. System determines final activation status: 'Activate' when all validations pass, or 'Review' when any threshold is exceeded
> 6. System routes flagged schedules to authorized approvers based on allocation category


**Acceptance Criteria:**

> 1. **Given** payment schedule with allocations below all authority limits, **When** activation is requested, **Then** system sets status to 'Activate' without review flags
> 2. **Given** payment schedule with LOB allocations exceeding user authority, **When** validation executes, **Then** system sets status to 'Review' and generates LOB authority flag
> 3. **Given** payment schedule with expense allocations exceeding authority, **When** validation executes, **Then** system sets status to 'Review' and generates expense authority flag
> 4. **Given** payment schedule with ex gratia allocations exceeding authority, **When** validation executes, **Then** system sets status to 'Review' and generates ex gratia authority flag
> 5. **Given** multiple allocation categories exceed authority, **When** validation completes, **Then** system generates all applicable review flags
> 6. **Given** payment schedule in 'Review' status, **When** accessed by unauthorized user, **Then** system prevents activation until proper authority approves


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=601635411"
> ]

---

#### Feature: As a Claims Operations Manager, I want the system to automatically calculate payment amounts including adjustments (deductions, taxes, offsets), so that accurate net payment amounts are determined
- **Role**: Claim Adjuster
- **Action**: automatically calculate net payment amounts with applied adjustments including deductions, taxes, and offsets
- **Value**: accurate payment determinations are made efficiently without manual calculation errors, ensuring compliance and reducing processing time

**Description:**

> As a **Claim Adjuster**,
> I want to **automatically calculate net payment amounts with applied adjustments including deductions, taxes, and offsets**,
> So that **accurate payment determinations are made efficiently without manual calculation errors, ensuring compliance and reducing processing time**.


**Key Capabilities:**

> 1. System retrieves approved claim payment base amounts from adjudication decisions
> 2. System applies applicable deductions based on policy terms and claim characteristics
> 3. System calculates tax withholdings according to jurisdiction requirements and payment type
> 4. System processes offsets including subrogation recoveries, overpayment corrections, and inter-claim balances
> 5. System computes final net payment amount and generates calculation breakdown
> 6. Upon completion, system presents calculation summary for adjuster review and approval


**Acceptance Criteria:**

> 1. **Given** an approved claim with payment base amount, **When** calculation is triggered, **Then** system applies all relevant adjustments and produces net payment amount
> 2. **Given** multiple adjustment types apply, **When** calculation executes, **Then** system processes deductions, taxes, and offsets in correct sequence
> 3. **Given** calculation completes, **When** results are generated, **Then** system provides itemized breakdown showing each adjustment component
> 4. **Given** jurisdiction-specific tax rules exist, **When** calculating withholdings, **Then** system applies correct rates based on payment location and type
> 5. **Given** insufficient data for calculation, **When** process initiates, **Then** system prevents completion and flags missing information
> 6. **Given** negative net amount results, **When** calculation finalizes, **Then** system flags for special handling and supervisor review


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=761792171"
> ]

---

#### Feature: As a Claims Operations Manager, I want the system to generate payment schedules from dental settlements with validated financial data, so that dental claim payments are accurately scheduled
- **Role**: Claim Adjuster
- **Action**: automatically generate validated payment schedules from approved dental settlements with financial data
- **Value**: dental claim payments are accurately scheduled and executed without manual intervention, reducing errors and processing time

**Description:**

> As a **Claim Adjuster**,
> I want to **automatically generate validated payment schedules from approved dental settlements with financial data**,
> So that **dental claim payments are accurately scheduled and executed without manual intervention, reducing errors and processing time**


**Key Capabilities:**

> 1. System retrieves approved dental settlement with 'Pay' proposal designation and validates eligibility status
> 2. System extracts financial data from settlement and prepares payment template instance
> 3. System applies rule engine payment scheduling logic to calculate schedule parameters
> 4. System generates and initializes payment schedule with calculated values and configuration
> 5. System performs comprehensive validation of activated schedule
>     5.1 Upon validation failure, process terminates without schedule creation
>     5.2 Upon validation success, payment schedule is activated for execution


**Acceptance Criteria:**

> 1. **Given** dental settlement is in 'Approved' state with 'Pay' proposal, **When** schedule generation is triggered, **Then** system successfully creates and activates validated payment schedule
> 2. **Given** settlement state is not 'Approved' or proposal is not 'Pay', **When** validation executes, **Then** system terminates process without creating schedule
> 3. **Given** rule engine payment scheduling rules are defined, **When** schedule is generated, **Then** system applies rules to calculate accurate schedule parameters
> 4. **Given** payment schedule validation fails, **When** final validation executes, **Then** system prevents activation and terminates process
> 5. **Given** all validations pass, **When** process completes, **Then** system confirms activated schedule is ready for payment execution


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=552021412"
> ]

---

#### Feature: As a Claims Operations Manager, I want the system to apply payment scheduling rules to generate payment allocations with correct gross amounts and payment dates, so that payment schedules are accurately created
- **Role**: Claim Adjuster
- **Action**: apply automated payment scheduling rules to generate accurate payment allocations with calculated gross amounts and scheduled payment dates across claim types
- **Value**: payment schedules are accurately created with correct financial adjustments, ensuring timely and compliant disbursements for dental and orthodontic services

**Description:**

> As a **Claim Adjuster**,
> I want to **apply automated payment scheduling rules to generate accurate payment allocations with calculated gross amounts and scheduled payment dates across claim types**,
> So that **payment schedules are accurately created with correct financial adjustments, ensuring timely and compliant disbursements for dental and orthodontic services**


**Key Capabilities:**

> 1. System validates payment template eligibility before initiating scheduling rules
> 2. Upon validation success, system calculates payment amounts based on claim type: applies full allowed settlement amount for actual services or divides total by treatment duration for orthodontic claims
> 3. System schedules payment dates using configured frequency rules (monthly/quarterly/one-time) and handles calendar edge cases
> 4. System groups allocations by payment date and payee to create unique payment identifiers
> 5. System applies financial adjustments (fees, additions, reductions) to the first upcoming unissued payment net amount
> 6. When claim adjustments occur, system cancels pending payments, retains issued payments, and regenerates remaining schedule with recalculated amounts


**Acceptance Criteria:**

> 1. **Given** valid payment template, **When** scheduling actual services claim, **Then** system generates single payment allocation with gross amount equal to allowed settlement and payment date as schedule creation date
> 2. **Given** orthodontic claim with monthly frequency, **When** calculating payment series, **Then** system divides total amount by treatment months, rounds to two decimals, and adjusts final payment to match total
> 3. **Given** quarterly payment frequency, **When** determining payment dates, **Then** system increments by three calendar months and maps to month-end when same date unavailable
> 4. **Given** multiple allocations with identical payment date and payee, **When** grouping payments, **Then** system consolidates into single payment entity with summed net amount
> 5. **Given** issued payment exists, **When** applying fees or adjustments, **Then** system targets only first upcoming unissued payment and prevents modification of applied adjustments
> 6. **Given** claim adjustment triggered, **When** rescheduling orthodontic payments, **Then** system cancels pending payments, regenerates with new treatment duration, and preserves issued payment history


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=553159046"
> ]

---

#### Feature: As a Claims Operations Manager, I want the system to handle orthodontic payment scheduling with frequency-based calculations (monthly, quarterly, one-time), so that recurring dental payments are correctly distributed
- **Role**: Claim Adjuster
- **Action**: automate orthodontic payment scheduling with frequency-based calculations (monthly, quarterly, one-time) to ensure accurate distribution of recurring dental payments across treatment periods
- **Value**: orthodontic claims are processed efficiently with predictable payment streams aligned to treatment duration, reducing manual calculation errors and ensuring timely provider reimbursements

**Description:**

> As a **Claim Adjuster**,
> I want to **automate orthodontic payment scheduling with frequency-based calculations (monthly, quarterly, one-time) to ensure accurate distribution of recurring dental payments across treatment periods**,
> So that **orthodontic claims are processed efficiently with predictable payment streams aligned to treatment duration, reducing manual calculation errors and ensuring timely provider reimbursements**


**Key Capabilities:**

> 1. System validates payment template eligibility and initiates scheduling rules for orthodontic services
> 2. System calculates individual payment amounts based on frequency type: monthly (total/months), quarterly (total/months×3), or one-time (full amount), with last payment adjusted for rounding
> 3. System establishes first payment date as current system date and generates subsequent payment dates by incrementing months (1 for monthly, 3 for quarterly) with month-end date normalization
> 4. System groups payment allocations by payee and payment date, aggregating gross amounts and mapping allocation details
> 5. System applies financial adjustments (fees, additions, reductions) to earliest upcoming non-issued payment
>     5.1 Upon claim adjustment with issued payments, system cancels pending payments, recalculates benefit amounts, and regenerates payment schedule preserving issued payments
> 6. System returns complete payment schedule with date sequences, net amounts, and allocation mappings


**Acceptance Criteria:**

> 1. **Given** valid orthodontic claim with 12-month treatment and monthly frequency, **When** payment schedule is generated, **Then** system creates 12 payments with amounts totaling benefit amount and dates incrementing by calendar month
> 2. **Given** quarterly frequency with 9-month treatment, **When** schedule is calculated, **Then** system generates 3 payments spaced 3 months apart with amounts equal to (total/9)×3
> 3. **Given** one-time frequency, **When** payment is scheduled, **Then** system creates single payment for full benefit amount dated current system date
> 4. **Given** month-end date (Jan 31) with monthly frequency, **When** next payment date is calculated, **Then** system maps to Feb 29 (leap year) or Feb 28, then Mar 31
> 5. **Given** orthodontic claim adjustment with 2 issued payments, **When** treatment months change from 10 to 12, **Then** system preserves issued payments, cancels pending payments, and regenerates remaining 10 payments with recalculated amounts
> 6. **Given** fees or addition amounts applied to issued payment, **When** claim is adjusted, **Then** system prevents re-editing those adjustments and applies new adjustments only to next upcoming payment


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=553159046"
> ]

---

#### Feature: As a Claims Operations Manager, I want the system to apply payment adjustments (additions and reductions) to upcoming scheduled payments, so that payment amounts can be corrected without rescheduling
- **Role**: Claim Adjuster
- **Action**: apply financial adjustments (fees, additions, and reductions) to upcoming scheduled payments without regenerating the entire payment schedule
- **Value**: payment amounts can be corrected efficiently while preserving the existing payment timeline and maintaining accurate financial records

**Description:**

> As a **Claim Adjuster**,
> I want to **apply financial adjustments (fees, additions, and reductions) to upcoming scheduled payments without regenerating the entire payment schedule**,
> So that **payment amounts can be corrected efficiently while preserving the existing payment timeline and maintaining accurate financial records**


**Key Capabilities:**

> 1. System validates payment template eligibility and identifies the first upcoming payment (excluding issued or stop-requested payments)
> 2. System applies claim-level fees to the net amount of the first upcoming payment
>     2.1 When claim is adjusted, newly added fees automatically apply to next eligible payment
> 3. User is able to add supplemental amounts or apply reductions via adjustment function to modify upcoming payment net amounts
> 4. Upon insufficient first payment amount to offset full reduction, system cascades remaining reduction to subsequent scheduled payments sequentially
> 5. When payment with adjustments fails (declined/voided), system prevents recalculation and locks adjustment records
> 6. System returns updated payment schedule with adjusted net amounts while preserving payment dates and allocation structure


**Acceptance Criteria:**

> 1. **Given** valid payment template with scheduled payments, **When** claim fees are added, **Then** system applies fee sum to first upcoming payment net amount without altering payment date
> 2. **Given** user initiates adjustment with addition amount, **When** first upcoming payment exists, **Then** system increases payment net amount by addition value and updates schedule
> 3. **Given** reduction amount exceeds first payment net amount, **When** adjustment is applied, **Then** system deducts first payment entirely and cascades remainder to subsequent payments
> 4. **Given** payment with adjustments has status issued or stop-requested, **When** user accesses payment, **Then** system prevents further adjustment actions
> 5. **Given** adjusted payment fails with decline or void status, **When** system processes failure, **Then** applied adjustments are locked and excluded from future recalculations
> 6. **Given** orthodontic payment schedule exists, **When** adjustments are applied, **Then** system maintains payment frequency rules and ortho-specific allocation logic


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=553159046"
> ]

---

#### Feature: As a System Administrator, I want to configure payment template models with payment details, frequency configurations, and allocation templates, so that payment scheduling rules have the correct data structure
- **Role**: Claim Manager
- **Action**: configure payment template models with payment details, frequency settings, and allocation structures
- **Value**: payment scheduling rules operate with accurate and reusable data structures that support automated claim disbursement

**Description:**

> As a **Claim Manager**,
> I want to **configure payment template models with payment details, frequency settings, and allocation structures**,
> So that **payment scheduling rules operate with accurate and reusable data structures that support automated claim disbursement**.


**Key Capabilities:**

> 1. System administrator defines foundational payment template structure with payment details and frequency configurations
> 2. Administrator associates payment method templates and allocation templates to payment details
> 3. Administrator configures allocation rules including payable items, payee details, and loss information mappings
> 4. Upon line-of-business requirements, administrator extends base templates with specialized attributes (e.g., dental allocation details)
> 5. System validates template integrity ensuring all required associations (frequency, method, allocation) are properly linked
> 6. System persists template configurations for reuse across payment scheduling operations


**Acceptance Criteria:**

> 1. **Given** valid payment details and frequency configurations, **When** administrator creates a payment template, **Then** system persists the template with all associated components
> 2. **Given** incomplete allocation mappings, **When** administrator attempts to save template, **Then** system prevents submission until all required allocation elements are defined
> 3. **Given** a configured base template, **When** administrator extends it with line-specific attributes, **Then** system maintains inheritance relationships while adding specialized properties
> 4. **Given** an active payment template, **When** referenced in payment scheduling rules, **Then** system applies configured frequency and allocation logic to claim disbursements
> 5. **Given** multiple allocation templates, **When** associated with payment details, **Then** system supports composite allocation structures for complex payment distributions


**Reference URLs:**

> [
>   "/pages/viewpage.action?pageId=526295425",
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=527534393"
> ]

---

#### Feature: As a System Administrator, I want to configure payment schedule models with payment details and allocations, so that payment schedules can be created and managed with proper data relationships
- **Role**: Claim Adjuster
- **Action**: configure and maintain payment schedule data models with associated payment details and allocation rules
- **Value**: payment schedules are created with accurate data structures, ensuring consistent claim payment processing and proper financial tracking

**Description:**

> As a **Claim Adjuster**,
> I want to **configure and maintain payment schedule data models with associated payment details and allocation rules**,
> So that **payment schedules are created with accurate data structures, ensuring consistent claim payment processing and proper financial tracking**


**Key Capabilities:**

> 1. System Administrator accesses authoritative payment schedule data model specification from master repository
> 2. Upon feature requirements, Administrator exports current data model version to standardized format
> 3. Administrator uploads versioned data model specification to documentation platform for traceability
> 4. System validates data model integrity and relationship mappings for payment details and allocations
> 5. Administrator publishes approved data model version, enabling payment schedule creation with proper data structures
> 6. System maintains version history for audit and rollback capabilities


**Acceptance Criteria:**

> 1. **Given** data model updates are required, **When** Administrator exports from master source, **Then** system generates specification in standardized format with complete payment and allocation structures
> 2. **Given** specification is uploaded, **When** documentation platform receives file, **Then** system timestamps and versions the artifact for traceability
> 3. **Given** data model is published, **When** payment schedules are created, **Then** system enforces configured data relationships and allocation rules
> 4. **Given** incomplete or invalid model, **When** validation executes, **Then** system prevents publication and indicates data integrity issues


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=533627742"
> ]

---

### Epic: Payment Recalculation & Balancing

#### Feature: As a Claims Adjuster, I want to automatically recalculate payments when claim or case data is updated, so that payment amounts reflect the most current claim information
- **Role**: Claim Adjuster
- **Action**: automatically recalculate and rebalance payments when case or claim data is updated
- **Value**: payment amounts and schedules continuously reflect current claim information, ensuring accurate compensation without manual intervention

**Description:**

> As a **Claim Adjuster**,
> I want to **automatically recalculate and rebalance payments when case or claim data is updated**,
> So that **payment amounts and schedules continuously reflect current claim information, ensuring accurate compensation without manual intervention**


**Key Capabilities:**

> 1. **Update Case or Claim Data**: User modifies event details, parties, deductions, or benefit information on open cases/claims; system tracks changes and initiates readjudication.
>     1.1 When new claim events are selected, system evaluates applicability and generates additional claims.
>     1.2 Upon data save, system determines if existing payment schedules require rescheduling.
> 2. **Recalculate Payment Schedules**: System merges updated claim settlement data with existing payment templates, deactivates outdated schedules, and generates new schedules maintaining prior approval status.
> 3. **Calculate Balance Per Payee**: System compares issued payments against revised scheduled amounts and existing balance transactions to determine carrier or insured obligations.
> 4. **Apply Balance Resolution**: User selects appropriate balancing action (recovery posting, payment withholding, underpayment issuance, or waiver) based on calculated balance type.
> 5. **Update Accumulators and Finalize**: System adjusts benefit accumulators per transaction type and issues approved underpayment payments through standard payment generation process.


**Acceptance Criteria:**

> 1. **Given** case/claim data is updated on an open case **when** payment schedules exist **then** system automatically triggers payment rescheduling without manual intervention.
> 2. **Given** payment recalculation completes **when** new schedule is generated **then** system preserves the original payment schedule approval status and creates audit history.
> 3. **Given** payments have been issued **when** recalculation occurs **then** system calculates balance per payee comparing issued versus scheduled amounts.
> 4. **Given** overpayment balance exists (insured owes carrier) **when** user reviews balance **then** system enables recovery posting, withholding, or waiver actions.
> 5. **Given** underpayment balance exists (carrier owes insured) **when** user initiates underpayment payment **then** system creates pending payment and issues through standard approval workflow.
> 6. **Given** balance transaction is submitted **when** transaction is issued **then** system updates benefit accumulators appropriately (except external overpayments).


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=761792204"
> ]

---

#### Feature: As a Claims Adjuster, I want to manually update payment allocations or add new payments through the payment management UI, so that I can adjust payment schedules based on specific claim circumstances
- **Role**: Claim Adjuster
- **Action**: manually update payment allocations or add new payment periods to adjust scheduled amounts based on claim circumstances
- **Value**: payment schedules accurately reflect claim changes, corrections, or policy adjustments without disrupting issued payments

**Description:**

> As a Claim Adjuster,
> I want to manually update payment allocations or add new payment periods to adjust scheduled amounts based on claim circumstances,
> So that payment schedules accurately reflect claim changes, corrections, or policy adjustments without disrupting issued payments.


**Key Capabilities:**

> 1. User initiates payment schedule modification by adding new allocation periods or updating existing allocation data through payment management interface
> 2. System merges user-provided payment input with existing payment schedule data and triggers payment scheduler automation
> 3. System deactivates existing payment schedule and generates new schedule with recalculated allocations based on merged input
> 4. Upon schedule approval, system calculates balance by comparing issued payments against scheduled amounts and existing balance transactions
> 5. User reviews balance per payee and applies balancing actions (reduce future payments, post recovery, waive overpayment, or pay underpayment)
> 6. System updates accumulators and generates balance transactions with appropriate status (issued or pending) based on selected balancing method


**Acceptance Criteria:**

> 1. **Given** payment schedule exists with issued payments, **When** user updates allocation data, **Then** system creates new schedule without modifying actual issued payments
> 2. **Given** user merges payment input, **When** system processes recalculation, **Then** new schedule reflects merged data and previous schedule is deactivated
> 3. **Given** payments are issued, **When** system calculates balance, **Then** balance reflects difference between what was paid and what should have been paid
> 4. **Given** overpayment exists, **When** user applies balancing action, **Then** system generates appropriate transaction (recovery/waiver/withholding) and updates total balance
> 5. **Given** underpayment exists, **When** user submits underpayment payment, **Then** system creates payment with pending status for approval workflow
> 6. **Given** balance transaction is saved, **When** system processes accumulator updates, **Then** accumulator reflects transaction impact based on transaction type and status


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=761792204"
> ]

---

#### Feature: As a Claims Adjuster, I want to view the balance calculation for a specific payee, so that I can understand if there is an overpayment or underpayment situation
- **Role**: Claim Adjuster
- **Action**: review calculated balance results for a specific payee to identify and understand payment discrepancies
- **Value**: I can accurately determine whether an overpayment or underpayment situation exists and take appropriate corrective action

**Description:**

> As a **Claim Adjuster**,
> I want to **review calculated balance results for a specific payee to identify and understand payment discrepancies**,
> So that **I can accurately determine whether an overpayment or underpayment situation exists and take appropriate corrective action**


**Key Capabilities:**

> 1. System performs balance calculation for specified payee upon claim or case data updates
> 2. System compares issued payment allocations against scheduled payment allocations
> 3. System factors issued balance transactions and expenses into calculation
> 4. System presents balance interpretation indicating payment status
>     4.1 Balance equals zero indicates neither party owes funds
>     4.2 Positive balance indicates carrier underpayment situation
>     4.3 Negative balance indicates payee overpayment situation
> 5. User is able to access calculation detail showing contributing factors and amounts
> 6. System provides historical tracking of balance changes and triggering events


**Acceptance Criteria:**

> 1. **Given** claim data has been updated, **When** balance calculation executes, **Then** system accurately compares issued versus scheduled allocations for the payee
> 2. **Given** balance calculation completes, **When** adjuster reviews results, **Then** system clearly indicates overpayment (negative), underpayment (positive), or balanced (zero) status
> 3. **Given** balance discrepancy exists, **When** adjuster accesses details, **Then** system displays all contributing factors including issued payments, scheduled payments, balance transactions, and expenses
> 4. **Given** multiple claims exist for payee, **When** balance is calculated, **Then** system aggregates at claim-and-payee or case-and-payee level per business scope
> 5. **Given** calculation includes issued balance transactions, **When** displaying results, **Then** system excludes already-balanced amounts from outstanding discrepancy


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=761792207"
> ]

---

#### Feature: As a Claims Adjuster, I want to apply balance management actions (recovery, waive overpayment, payment reduction, or underpayment) to resolve overpayment or underpayment situations, so that the claim balance is properly reconciled
- **Role**: Claim Adjuster
- **Action**: apply balance management actions to resolve overpayment or underpayment situations
- **Value**: the claim balance is properly reconciled and financial discrepancies are resolved

**Description:**

> As a **Claim Adjuster**,
> I want to **apply balance management actions to resolve overpayment or underpayment situations**,
> So that **the claim balance is properly reconciled and financial discrepancies are resolved**


**Key Capabilities:**

> 1. User selects payee to review associated balance status and identify discrepancies
> 2. Upon detecting non-zero balance, user evaluates available management actions based on balance type
> 3. When overpayment exists with planned future payments, user applies payment reduction through withholding mechanism
> 4. When immediate recovery is needed, user posts recovery transaction generating issued payment for collection
> 5. When overpayment should be forgiven, user waives overpayment updating total balance
> 6. When underpayment identified, user initiates underpayment transaction generating pending payment for approval and issuance


**Acceptance Criteria:**

> 1. **Given** payee with non-zero balance, **When** user accesses balance management, **Then** system displays available actions based on balance type
> 2. **Given** overpayment exists, **When** user applies reduction action, **Then** system generates withholding for future payments and updates balance upon issuance
> 3. **Given** recovery is posted, **When** transaction is saved, **Then** system creates issued payment and increases total balance immediately
> 4. **Given** underpayment is processed, **When** payment is approved and issued, **Then** system decreases total balance and updates accumulator
> 5. **Given** any balance action is completed, **When** transaction is recorded, **Then** system prevents modification or cancellation through standard UI
> 6. **Given** balance transaction is saved, **When** amount allocation occurs, **Then** system reflects changes in balance overview and activity history


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=761792215"
> ]

---

#### Feature: As a Claims Adjuster, I want to post a recovery transaction when an overpayment has been returned by the payee, so that the balance is updated to reflect the recovered amount
- **Role**: Claim Adjuster
- **Action**: post a recovery transaction when overpayment funds are returned by the payee
- **Value**: the claim balance accurately reflects the recovered amount and ensures proper financial reconciliation

**Description:**

> As a **Claim Adjuster**,
> I want to **post a recovery transaction when overpayment funds are returned by the payee**,
> So that **the claim balance accurately reflects the recovered amount and ensures proper financial reconciliation**.


**Key Capabilities:**

> 1. User identifies payee with outstanding overpayment balance requiring recovery action
> 2. User accesses balance management interface to review current balance status and transaction history
> 3. User initiates recovery transaction posting upon confirmation of returned overpayment funds from payee
> 4. System generates recovery payment record in 'issued' status and adjusts payee balance accordingly
> 5. System updates payment accumulator to reflect recovered amount impact on total claim financials
> 6. User verifies balance reconciliation through transaction history and updated balance overview


**Acceptance Criteria:**

> 1. **Given** an overpayment balance exists for a payee, **When** adjuster posts a recovery transaction, **Then** system creates recovery payment in 'issued' status
> 2. **Given** recovery transaction is posted, **When** system processes the transaction, **Then** total balance increases by recovered amount
> 3. **Given** recovery is successfully posted, **When** accumulator is updated, **Then** payment accumulator reflects the recovery impact
> 4. **Given** recovery transaction is completed, **When** user reviews transaction history, **Then** recovery appears in balance activities and payment lists
> 5. **Given** insufficient overpayment data, **When** user attempts recovery posting, **Then** system prevents submission until complete information is provided
> 6. **Given** recovery is posted, **When** balance recalculation occurs, **Then** payee balance accurately reflects recovered funds


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=761792215"
> ]

---

#### Feature: As a Claims Adjuster, I want to waive an overpayment amount, so that I can forgive the overpaid portion and reduce the balance owed by the payee
- **Role**: Claim Adjuster
- **Action**: waive an overpayment amount to forgive the overpaid portion and adjust the balance owed
- **Value**: I can reduce financial burden on payees by forgiving specific overpayment amounts, maintaining positive customer relationships while ensuring accurate balance reconciliation

**Description:**

> As a **Claim Adjuster**,
> I want to **waive an overpayment amount to forgive the overpaid portion and adjust the balance owed**,
> So that **I can reduce financial burden on payees by forgiving specific overpayment amounts, maintaining positive customer relationships while ensuring accurate balance reconciliation**


**Key Capabilities:**

> 1. User accesses balance management interface and selects payee to review current balance status and identify overpayment amounts
> 2. Upon confirming overpayment exists in the balance, user initiates waiver action from available balance management options
> 3. User configures waiver transaction details specifying the forgiven overpayment amount within business authorization limits
> 4. System validates waiver eligibility, processes the transaction, and immediately increases total balance amount upon saving
> 5. System updates accumulator to reflect the waived amount impact and records the transaction in balance activity history
> 6. User reviews confirmation that balance owed has been reduced and waiver is reflected in claim financial records


**Acceptance Criteria:**

> 1. **Given** an overpayment exists for a selected payee, **When** the adjuster initiates waiver action, **Then** the system enables waiver configuration with overpayment amount details
> 2. **Given** no overpayment exists in the balance, **When** the adjuster accesses balance actions, **Then** the system disables and prevents waiver action selection
> 3. **Given** waiver transaction details are configured, **When** the adjuster saves the transaction, **Then** the system immediately increases total balance amount by the waived amount
> 4. **Given** a waiver transaction is successfully saved, **When** the system processes the transaction, **Then** accumulator is updated to reflect the waived amount impact
> 5. **Given** a waiver is completed, **When** the adjuster reviews balance activities, **Then** the waiver transaction appears in the balance transaction history
> 6. **Given** incomplete or invalid waiver data, **When** the adjuster attempts to save, **Then** the system prevents submission until all required information is provided


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=761792215"
> ]

---

#### Feature: As a Claims Adjuster, I want to apply overpayment withholding to future payments, so that overpayment amounts are automatically deducted from scheduled payments
- **Role**: Claim Adjuster
- **Action**: apply overpayment withholding to future scheduled payments so that overpaid amounts are automatically deducted and balanced
- **Value**: overpayment recovery is automated through systematic deductions, ensuring financial accuracy and reducing manual reconciliation efforts

**Description:**

> As a **Claim Adjuster**,
> I want to **apply overpayment withholding to future scheduled payments so that overpaid amounts are automatically deducted and balanced**,
> So that **overpayment recovery is automated through systematic deductions, ensuring financial accuracy and reducing manual reconciliation efforts**.


**Key Capabilities:**

> 1. Adjuster selects payee and reviews balance to verify overpayment existence
> 2. Upon confirming overpayment, adjuster initiates 'Reduce Payment' action and specifies withholding details
> 3. System saves withholding instruction and applies it during payment scheduling processes
> 4. When payments are issued with withholding applied, system automatically:
>     4.1 Deducts overpayment amount from scheduled payment
>     4.2 Updates total balance amount
>     4.3 Impacts accumulator calculations
> 5. Adjuster monitors balance activities and withholding transactions through balance overview
> 6. If no overpayment exists, system prevents withholding action selection


**Acceptance Criteria:**

> 1. **Given** overpayment exists in payee balance, **When** adjuster applies withholding, **Then** system saves instruction and applies deduction to future scheduled payments
> 2. **Given** no overpayment exists, **When** adjuster attempts withholding, **Then** system prevents action selection
> 3. **Given** withholding instruction is active, **When** payment is issued, **Then** system automatically deducts specified amount and updates balance
> 4. **Given** payment with withholding is issued, **When** balance is reviewed, **Then** total balance amount reflects increased recovery and accumulator is updated
> 5. **Given** withholding transaction is saved, **When** adjuster reviews balance activities, **Then** withholding appears in transaction list
> 6. **Given** withholding is applied, **When** backend cancellation occurs, **Then** system reverses amount allocations (note: UI cancellation unavailable)


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=761792215"
> ]

---

#### Feature: As a Claims Adjuster, I want to create an underpayment payment to compensate the payee for amounts owed, so that the underpayment can be approved and issued
- **Role**: Claim Adjuster
- **Action**: initiate and process underpayment payments to compensate payees for owed amounts through balance reconciliation workflow
- **Value**: payees receive accurate compensation for shortfalls, ensuring financial accuracy and compliance with payment obligations

**Description:**

> As a **Claim Adjuster**,
> I want to **initiate and process underpayment payments to compensate payees for owed amounts through balance reconciliation workflow**,
> So that **payees receive accurate compensation for shortfalls, ensuring financial accuracy and compliance with payment obligations**


**Key Capabilities:**

> 1. Adjuster accesses payee balance management and selects specific payee to review balance status and identify underpayment amounts
> 2. Adjuster initiates underpayment transaction through balance action menu, specifying compensation amount and optional withholding offset
> 3. System generates pending underpayment payment record and registers transaction in payee balance activity ledger
> 4. Transaction enters approval workflow where authorized personnel review and validate underpayment justification
> 5. Upon approval and issuance, system decreases total payee balance and updates accumulator records
> 6. Adjuster verifies completed payment appears in payment list with issued status and balance reflects accurate reconciliation


**Acceptance Criteria:**

> 1. **Given** payee has negative balance, **When** adjuster initiates underpayment payment, **Then** system creates pending payment record without immediate balance impact
> 2. **Given** underpayment payment is created, **When** transaction is saved, **Then** system records activity in balance transaction ledger with pending status
> 3. **Given** pending underpayment exists, **When** payment receives approval and issuance, **Then** system decreases total balance and updates accumulator accordingly
> 4. **Given** incomplete or invalid compensation data, **When** adjuster attempts submission, **Then** system prevents transaction creation until requirements are satisfied
> 5. **Given** underpayment payment is issued, **When** adjuster reviews payment list, **Then** system displays payment with issued status and accurate balance reflection
> 6. **Given** optional withholding compensation is selected, **When** payment processes, **Then** system applies appropriate withholding offset to final payment amount


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=761792215"
> ]

---

#### Feature: As a Claims Adjuster, I want to record external overpayment amounts that occurred outside the claim system, so that the total payee balance reflects all overpayment sources
- **Role**: Claim Adjuster
- **Action**: record external overpayment amounts that occurred outside the claim system to reconcile total payee balance across all sources
- **Value**: the system maintains accurate financial records reflecting overpayments from multiple channels, ensuring complete balance visibility for recovery decisions

**Description:**

> As a **Claim Adjuster**,
> I want to **record external overpayment amounts that occurred outside the claim system to reconcile total payee balance across all sources**,
> So that **the system maintains accurate financial records reflecting overpayments from multiple channels, ensuring complete balance visibility for recovery decisions**


**Key Capabilities:**

> 1. User reviews payee balance and identifies discrepancies requiring external overpayment documentation
> 2. User accesses balance management functionality for the selected payee
> 3. User initiates external overpayment recording action
> 4. User provides overpayment transaction details including amount and source information
> 5. Upon submission, system validates data completeness and immediately incorporates amount into total payee balance calculation
>     5.1 System excludes external overpayment from benefit accumulator impacts
>     5.2 System records transaction as non-reversible via user interface
> 6. User verifies updated balance reflects all overpayment sources for subsequent recovery planning


**Acceptance Criteria:**

> 1. **Given** a payee has existing balance, **When** adjuster records external overpayment, **Then** system increases total balance amount by the recorded overpayment value
> 2. **Given** external overpayment is submitted, **When** system processes transaction, **Then** benefit accumulators remain unchanged regardless of overpayment amount
> 3. **Given** overpayment details are incomplete, **When** adjuster attempts submission, **Then** system prevents transaction creation until required information is provided
> 4. **Given** external overpayment is recorded, **When** adjuster views balance activities, **Then** transaction appears with clear identification as external source
> 5. **Given** external overpayment exists, **When** adjuster evaluates recovery options, **Then** total balance calculation includes all internal and external overpayment amounts


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=761792215"
> ]

---

#### Feature: As a Claims Operations Manager, I want the system to automatically trigger payment rescheduling when claim or case data is updated, so that payment schedules are recalculated without manual intervention
- **Role**: Claim Adjuster
- **Action**: enable automatic payment schedule recalculation and balance determination when claim or case data changes
- **Value**: payment accuracy is maintained without manual intervention, reducing administrative burden and preventing payment errors

**Description:**

> As a **Claim Adjuster**,
> I want to **enable automatic payment schedule recalculation and balance determination when claim or case data changes**,
> So that **payment accuracy is maintained without manual intervention, reducing administrative burden and preventing payment errors**


**Key Capabilities:**

> 1. Upon claim or case data update, system automatically triggers payment schedule recalculation using updated settlement information
> 2. System applies payment scheduling business rules to generate revised payment schedule with original status preserved
> 3. When issued payments exist, system calculates balance by comparing issued allocations against scheduled allocations per payee
>     3.1 System identifies overpayment (customer owes carrier) or underpayment (carrier owes customer)
> 4. System automatically performs self-balancing when offsetting balance items exist across payment components
> 5. User selects balance resolution options for remaining imbalances through balancing workflow
> 6. System generates balance transactions to resolve discrepancies and update financial records


**Acceptance Criteria:**

> 1. **Given** active payment schedule exists **when** claim settlement data is modified **then** system recalculates schedule without manual trigger
> 2. **Given** payment schedule is recalculated **when** issued payments exist **then** system automatically determines balance per payee
> 3. **Given** balance items show both overpayment and underpayment **when** self-balancing is possible **then** system generates automatic offsetting transactions
> 4. **Given** balance calculation completes **when** imbalances remain **then** system presents resolution options to user
> 5. **Given** no issued payments exist **when** rescheduling occurs **then** system completes without balance calculation
> 6. **Given** balance transactions are applied **when** financial records update **then** ledger and accumulator values reflect accurate state


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=761792216"
> ]

---

#### Feature: As a Claims Operations Manager, I want the system to automatically perform self-balancing to identify and reconcile offsetting balance items, so that ledger and accumulator records remain accurate
- **Role**: Claim Adjuster
- **Action**: enable automated self-balancing to identify and reconcile offsetting balance items across payment schedules
- **Value**: ledger and accumulator records maintain accuracy without manual intervention, reducing reconciliation effort and financial discrepancies

**Description:**

> As a Claim Adjuster,
> I want to enable automated self-balancing to identify and reconcile offsetting balance items across payment schedules,
> So that ledger and accumulator records maintain accuracy without manual intervention, reducing reconciliation effort and financial discrepancies


**Key Capabilities:**

> 1. Upon payment rescheduling with existing issued payments, system automatically triggers balance calculation service to compare what was paid versus what should be paid versus what is already balanced
> 2. System detects offsetting balance items across different allocation categories (e.g., underpayment in gross benefit versus overpayments in deductions or taxes)
> 3. When offsetting items are identified, system automatically generates self-balance transactions to reconcile the differences without user intervention
> 4. System applies self-balancing prioritization rules, allocating adjustments to oldest balance items first when multiple payments are affected
> 5. Upon completion, system updates ledger and accumulator records to reflect accurate financial positions per payee and balance item
> 6. System supports reversals when subsequent changes undo previous adjustments, maintaining historical accuracy


**Acceptance Criteria:**

> 1. **Given** payment schedule is recalculated with issued payments existing, **When** balance calculation completes, **Then** system identifies all offsetting balance items across allocation categories
> 2. **Given** offsetting balance items are detected, **When** self-balancing executes, **Then** system automatically generates self-balance transactions without requiring manual user action
> 3. **Given** multiple payments contain balance discrepancies, **When** self-balancing allocates adjustments, **Then** oldest items are reconciled first according to prioritization rules
> 4. **Given** self-balance transactions are created, **When** ledger and accumulator updates complete, **Then** financial records reflect accurate net positions per payee
> 5. **Given** claim details revert to previous values, **When** payment rescheduling occurs, **Then** system reverses prior self-balancing allocations appropriately
> 6. **Given** no offsetting items exist, **When** balance calculation completes, **Then** system proceeds without generating unnecessary self-balance transactions


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=761792216"
> ]

---

#### Feature: As a Claims Adjuster, I want to view the history of all changes made to case and claim data, so that I can track what modifications have been made and when
- **Role**: Claim Adjuster
- **Action**: access comprehensive audit history of all case and claim data modifications impacting payment calculations
- **Value**: I can track modifications chronologically, understand root causes of payment imbalances, and ensure compliance with audit requirements during payment recalculation and balancing activities

**Description:**

> As a **Claim Adjuster**,
> I want to **access comprehensive audit history of all case and claim data modifications impacting payment calculations**,
> So that **I can track modifications chronologically, understand root causes of payment imbalances, and ensure compliance with audit requirements during payment recalculation and balancing activities**


**Key Capabilities:**

> 1. User retrieves chronological audit records of case and claim data modifications that triggered payment rescheduling
> 2. System presents modification details including changed attributes, timestamps, user identifiers, and triggering events
> 3. Upon identifying payment imbalance, user correlates balance calculation outcomes with historical data changes
>     3.1 System links balance items to originating data modifications
>     3.2 User traces adjustment sequences across multiple rescheduling cycles
> 4. User validates compliance by verifying audit trail completeness for issued payments and balance transactions
> 5. System enables filtering and export of audit records for regulatory reporting or dispute resolution


**Acceptance Criteria:**

> 1. **Given** payment rescheduling occurred, **When** adjuster accesses audit history, **Then** system displays all case/claim data changes with timestamps and user attribution
> 2. **Given** balance calculation shows underpayment/overpayment, **When** adjuster reviews history, **Then** system correlates balance items to specific data modifications
> 3. **Given** multiple rescheduling events exist, **When** adjuster filters by date range, **Then** system presents sequential modification chain
> 4. **Given** audit record request, **When** export is initiated, **Then** system generates complete compliance-ready report
> 5. **Given** balance transaction exists, **When** adjuster investigates, **Then** system traces transaction to originating scheduled/issued payment changes


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=761792216"
> ]

---

#### Feature: As a Claims Adjuster, I want to update case data such as claim events, deductions, and ancillaries, so that new claims can be automatically created or existing claims can be re-adjudicated based on the updated information
- **Role**: Claim Adjuster
- **Action**: update case or claim data to trigger automated payment recalculation and balance resolution
- **Value**: benefit amounts accurately reflect current claim status, and overpayments or underpayments are systematically identified and resolved without manual intervention

**Description:**

> As a **Claim Adjuster**,
> I want to **update case or claim data to trigger automated payment recalculation and balance resolution**,
> So that **benefit amounts accurately reflect current claim status, and overpayments or underpayments are systematically identified and resolved without manual intervention**


**Key Capabilities:**

> 1. System automatically detects claim or case data changes and triggers payment rescheduling service to recalculate benefit allocations
> 2. System evaluates balance impact by comparing issued payments against updated scheduled amounts to determine overpayment or underpayment conditions
> 3. System calculates balance per payee using four factors: issued payments, scheduled payments, existing balance transactions, and expense adjustments
>     3.1 Balance items are defined by payment type, payee, claim coverage, and benefit category
> 4. System executes self-balancing logic to automatically offset underpayments against overpayments when matching balance items exist across adjustments
> 5. User selects balance resolution options including recovery, waiver, withholding for overpayments, or underpayment issuance based on calculated balance status
> 6. System allocates balance transaction amounts to impacted balance items according to allocation business rules and updates financial ledgers


**Acceptance Criteria:**

> 1. **Given** claim settlement data is updated, **When** an active payment schedule exists, **Then** system automatically recalculates payment allocations without manual adjuster initiation
> 2. **Given** issued payments exist, **When** recalculation completes, **Then** system generates balance calculation comparing what was paid versus what should have been paid per payee
> 3. **Given** balance calculation identifies both overpayments and underpayments, **When** self-balancing conditions are met, **Then** system automatically generates offsetting balance transactions to eliminate matching imbalances
> 4. **Given** balance remains after self-balancing, **When** adjuster accesses balancing component, **Then** system presents appropriate resolution options based on overpayment or underpayment status
> 5. **Given** balance transaction is created, **When** system processes allocation, **Then** amounts are distributed across balance items according to allocation rules and financial adjustments are recorded
> 6. **Given** multiple payments with complex balance scenarios exist, **When** self-balancing executes, **Then** system processes oldest items first and allocates proportionally until all possible balancing is complete


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=761792216"
> ]

---

#### Feature: As a Claims Adjuster, I want to update claim-level data such as covered earnings, benefit amounts, and elimination periods, so that the claim settlement and payment schedule are recalculated with the updated values
- **Role**: Claim Adjuster
- **Action**: update claim-level financial parameters to trigger automated recalculation of payment schedules and settlement balances
- **Value**: claim payments reflect accurate benefit amounts, coverage terms, and deductions without manual recalculation, ensuring financial accuracy and compliance across all active payment schedules

**Description:**

> As a **Claim Adjuster**,
> I want to **update claim-level financial parameters to trigger automated recalculation of payment schedules and settlement balances**,
> So that **claim payments reflect accurate benefit amounts, coverage terms, and deductions without manual recalculation, ensuring financial accuracy and compliance across all active payment schedules**.


**Key Capabilities:**

> 1. Adjuster modifies balance-sensitive financial data at claim, event case, or master policy level (e.g., covered earnings, gross benefit amount, elimination period dates, tax withholding, retroactive offsets/ancillaries)
> 2. System validates financial data completeness and identifies existing open payment templates
> 3. Upon validation success, system retrieves current financial settlement data and updates payment template records
>     3.1 If Build Payment Schedule feature is disabled, process terminates without schedule regeneration
> 4. System triggers automated payment scheduling process using updated financial parameters
> 5. System evaluates previous payment schedule status and applies inheritance rules
>     5.1 When previous schedule is suspended, newly generated schedule inherits suspended status
> 6. System finalizes recalculated payment schedule with updated benefit amounts and adjusted balances


**Acceptance Criteria:**

> 1. **Given** adjuster updates covered earnings or benefit amounts, **When** payment template with Open status exists, **Then** system updates template and triggers automated scheduling process
> 2. **Given** Build Payment Schedule feature is disabled, **When** financial data is modified, **Then** system updates payment template but does not generate new payment schedules
> 3. **Given** previous payment schedule was suspended, **When** recalculation completes, **Then** newly created payment schedule inherits suspended status
> 4. **Given** retroactive deductions or offsets are added at event case level, **When** recalculation executes, **Then** payment balances reflect adjusted amounts across all affected schedules
> 5. **Given** elimination period dates change, **When** system recalculates, **Then** payment start dates and benefit periods align with updated parameters
> 6. **Given** financial data is incomplete or invalid, **When** update is attempted, **Then** system prevents recalculation and notifies adjuster of data deficiencies


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=568302632"
> ]

---

#### Feature: As a Claims Operations Manager, I want the system to automatically recalculate balance when payments are rescheduled and issued payments exist, so that the balance always reflects the current payment status
- **Role**: Claim Adjuster
- **Action**: enable automatic balance recalculation when payment schedules change and issued payments exist
- **Value**: the system maintains accurate payment balances reflecting current obligations between carrier and insured without manual intervention

**Description:**

> As a **Claim Adjuster**,
> I want to **enable automatic balance recalculation when payment schedules change and issued payments exist**,
> So that **the system maintains accurate payment balances reflecting current obligations between carrier and insured without manual intervention**


**Key Capabilities:**

> 1. Upon claim or case data modification, system detects active payment schedules and triggers automated rescheduling
> 2. System applies payment scheduling rules and recalculates schedule using updated settlement data
> 3. When issued payments exist, balance service automatically compares issued allocations against scheduled allocations and issued balance transactions
> 4. System calculates balance per payee by analyzing adjusted gross benefit amounts and financial adjustments
>     4.1 Balance greater than zero indicates carrier owes insured
>     4.2 Balance less than zero indicates insured owes carrier
> 5. System attempts self-balancing by offsetting balance items automatically
> 6. User is able to address remaining imbalances through recovery, waiver, withholding, or underpayment transactions


**Acceptance Criteria:**

> 1. **Given** claim settlement data changes and active payment schedule exists, **When** adjuster saves updates, **Then** system automatically triggers payment rescheduling without manual initiation
> 2. **Given** issued payments exist, **When** rescheduling completes, **Then** system recalculates balance comparing issued versus scheduled allocations per payee
> 3. **Given** no issued payments exist, **When** rescheduling occurs, **Then** system does not create balance calculations
> 4. **Given** balance calculation completes, **When** offsetting balance items identified, **Then** system generates self-balance transaction automatically
> 5. **Given** overpayment detected, **When** balance displays, **Then** system indicates insured owes carrier with negative balance
> 6. **Given** underpayment detected, **When** balance displays, **Then** system indicates carrier owes insured with positive balance


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=761792216"
> ]

---

### Epic: Payment Calculation & Deduction Rules

#### Feature: As a Claims Adjuster, I want to match payment allocations based on standardized rules, so that I can ensure consistent and accurate payment grouping across different LOBs and deduction types
- **Role**: Claim Adjuster
- **Action**: apply standardized matching rules to group payment allocations consistently across different lines of business and deduction contexts
- **Value**: payment accuracy is maintained and allocation grouping follows consistent business logic regardless of product type or deduction scenario

**Description:**

> As a **Claim Adjuster**,
> I want to **apply standardized matching rules to group payment allocations consistently across different lines of business and deduction contexts**,
> So that **payment accuracy is maintained and allocation grouping follows consistent business logic regardless of product type or deduction scenario**


**Key Capabilities:**

> 1. System evaluates allocations against universal matching criteria including loss source, benefit date, benefit period, benefit code, interest flag, deduction type, and master payee
> 2. System applies LOB-specific rules when allocation context is Life (policy source validation) or Disability (ASO type ATP verification)
> 3. System confirms all applicable rules are satisfied simultaneously before designating allocations as matching
> 4. User is able to rely on automated grouping logic that adapts to product context without manual rule selection


**Acceptance Criteria:**

> 1. **Given** allocations with identical universal attributes, **when** all seven base criteria match, **then** system designates them as matching candidates
> 2. **Given** Life LOB allocations, **when** universal rules pass but policy sources differ, **then** system prevents matching
> 3. **Given** Disability LOB allocations, **when** universal rules pass but ASO types are not ATP, **then** system prevents matching
> 4. **Given** mixed LOB allocations, **when** evaluated, **then** system applies correct rule set per product context
> 5. **Given** partial rule compliance, **when** any required criterion fails, **then** system rejects the match


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=583840211"
> ]

---

#### Feature: As a Claims Adjuster, I want to identify applicable payment allocations for financial adjustments (REHAB, INTEREST, OFFSET, DEDUCTIONS, TAXES, WITHHOLDINGS), so that I can correctly apply financial adjustments to the right payments
- **Role**: Claim Adjuster
- **Action**: identify and match applicable payment allocations for financial adjustments across multiple adjustment types
- **Value**: financial adjustments are correctly applied to eligible payments ensuring accurate calculation of rehab, interest, offsets, deductions, taxes, and withholdings

**Description:**

> As a **Claim Adjuster**,
> I want to **identify and match applicable payment allocations for financial adjustments across multiple adjustment types**,
> So that **financial adjustments are correctly applied to eligible payments ensuring accurate calculation of rehab, interest, offsets, deductions, taxes, and withholdings**.


**Key Capabilities:**

> 1. System evaluates financial adjustment type and applies corresponding matching criteria against payment allocations for the same payee
> 2. Upon REHAB or INTEREST adjustments, system matches allocations based on loss source and addition split result numbers
> 3. Upon OFFSET adjustments, system matches allocations using loss source and reduction split result numbers
> 4. When processing DEDUCTION adjustments (percentage/flat/fixed), system validates payee, source alignment, period overlap, and excludes interest-only or expense reserve allocations
> 5. For TAX adjustments (federal/state/FICA), system matches disability LOB allocations within applicable periods and excludes expense reserves
> 6. Upon WITHHOLDINGS, system matches allocations by source alignment and validates payee balance thresholds


**Acceptance Criteria:**

> 1. **Given** a financial adjustment requires allocation matching, **When** the adjuster initiates matching, **Then** system evaluates only allocations for the same payment payee
> 2. **Given** adjustment type is REHAB/INTEREST/OFFSET, **When** matching is performed, **Then** system validates split result numbers and loss source alignment
> 3. **Given** adjustment type is DEDUCTION, **When** evaluating allocations, **Then** system excludes interest-only and expense reserve allocations while validating period and source criteria
> 4. **Given** adjustment type is TAX or FICA, **When** matching allocations, **Then** system restricts matches to disability LOB and excludes expense reserves
> 5. **Given** multiple allocation conditions exist, **When** matching logic is applied, **Then** system enforces AND/OR logic as defined per adjustment type
> 6. **Given** no qualifying allocations exist, **When** matching completes, **Then** system prevents adjustment application and notifies adjuster


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=606248845"
> ]

---

#### Feature: As a Claims Operations Manager, I want to validate payment schedules for overpayment conditions before activation, so that I can prevent erroneous payments and ensure compliance with authority limits
- **Role**: Claim Adjuster
- **Action**: validate payment schedules against overpayment conditions and authority limits before activation
- **Value**: I can prevent erroneous payments, ensure compliance with authority limits, and protect the organization from financial risk

**Description:**

> As a **Claim Adjuster**,
> I want to **validate payment schedules against overpayment conditions and authority limits before activation**,
> So that **I can prevent erroneous payments, ensure compliance with authority limits, and protect the organization from financial risk**


**Key Capabilities:**

> 1. System retrieves payee information and evaluates overpayment balance status upon schedule submission
> 2. System assesses authority level limits to determine whether manual review is required
> 3. Upon detecting payee overpayment balance greater than zero and authority status requiring review, system generates critical validation message
> 4. System determines final activation status based on validation outcome
>     4.1 When no critical messages exist, schedule proceeds to activation
>     4.2 When critical messages are present, schedule is routed for manual review
> 5. System enforces business rules exclusively for Disability and Life product lines


**Acceptance Criteria:**

> 1. **Given** a payment schedule for Disability or Life line of business, **When** the payee has zero overpayment balance, **Then** the system activates the schedule without review
> 2. **Given** a payee with overpayment balance greater than zero, **When** authority level requires review, **Then** the system generates critical message and routes schedule to review status
> 3. **Given** multiple validation checks, **When** any critical message is triggered, **Then** the system prevents automatic activation
> 4. **Given** a payment schedule for non-applicable product lines, **When** validation is initiated, **Then** the system bypasses overpayment validation rules
> 5. **Given** review status assignment, **When** schedule is routed, **Then** the system ensures adjuster with appropriate authority receives notification


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=728245200"
> ]

---

#### Feature: As a Claims Adjuster, I want to generate payment slices from financial data allocations, so that I can create accurate payment schedules with proper grouping by payee, payment date, and payment method
- **Role**: Claim Adjuster
- **Action**: generate calculated payment schedules from validated financial allocations with automated grouping, calculation, and deduction processing
- **Value**: accurate payment schedules are produced efficiently with proper payee grouping, payment method assignments, and automated application of deductions and withholdings without manual intervention

**Description:**

> As a **Claim Adjuster**,
> I want to **generate calculated payment schedules from validated financial allocations with automated grouping, calculation, and deduction processing**,
> So that **accurate payment schedules are produced efficiently with proper payee grouping, payment method assignments, and automated application of deductions and withholdings without manual intervention**


**Key Capabilities:**

> 1. System validates incoming financial data and prevents payment generation when critical validation failures exist
> 2. System generates payment slices based on line-of-business rules, grouping disability allocations by claim and coverage while processing life and expense allocations individually
> 3. System consolidates payment slices into payments grouped by payee, payment date, payment method, and address
> 4. System calculates payments in chronological order to ensure accurate tax threshold application
> 5. System generates third-party deduction payments after primary payment calculation
> 6. Upon overpayment conditions, system applies withholdings to unissued payments starting from earliest date until payee balance is achieved


**Acceptance Criteria:**

> 1. **Given** financial data with critical validation failures, **When** payment generation is initiated, **Then** system prevents payment slice creation and reports invalid status
> 2. **Given** valid disability allocations, **When** payment slices are generated, **Then** system groups by claim and coverage with auto-offset priority sequencing
> 3. **Given** multiple payment slices, **When** consolidation occurs, **Then** system creates distinct payments per unique combination of payee, date, method, and address
> 4. **Given** payments with different dates, **When** calculation executes, **Then** system processes chronologically from earliest to latest
> 5. **Given** calculated payments with deductions, **When** deduction processing completes, **Then** system generates corresponding third-party deduction payments
> 6. **Given** payee overpayment conditions exist, **When** withholding is applied, **Then** system reduces unissued scheduled payments until balance is achieved


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=691643492"
> ]

---

#### Feature: As a Claims Adjuster, I want to calculate payment taxes (Federal, State, FICA) based on applicable allocations and tax periods, so that I can ensure correct tax withholding and compliance
- **Role**: Claim Adjuster
- **Action**: calculate and apply tax withholdings (Federal, State, FICA) to eligible payment allocations based on tax periods and business rules
- **Value**: I ensure accurate tax compliance, correct withholding amounts, and regulatory adherence across all claim payments

**Description:**

> As a **Claim Adjuster**,
> I want to **calculate and apply tax withholdings (Federal, State, FICA) to eligible payment allocations based on tax periods and business rules**,
> So that **I ensure accurate tax compliance, correct withholding amounts, and regulatory adherence across all claim payments**


**Key Capabilities:**

> 1. System identifies applicable allocations by filtering claims in tax scope and excluding non-taxable types (Interest only, Ex gratia, Expense)
> 2. System determines tax applicability based on tax type:
>     2.1 Percentage taxes apply when payment date falls within tax period
>     2.2 Flat-value taxes apply when allocation period overlaps tax period
>     2.3 Extra withholding uses allocation period overlap regardless of payment date
> 3. System calculates total taxable wages by aggregating all applicable allocation amounts
> 4. System computes tax per allocation:
>     4.1 Percentage: Amount × Tax Rate
>     4.2 Extra Withholding: Amount × Duration × Proration Rate
>     4.3 Flat: Tax × Duration × Proration Rate
> 5. System rounds all calculated amounts to two decimal places
> 6. System validates calculation results against regulatory thresholds before finalizing withholding


**Acceptance Criteria:**

> 1. **Given** a claim in tax scope with taxable allocations, **When** processing payment, **Then** system excludes Interest only, Ex gratia, and Expense types from tax calculation
> 2. **Given** percentage tax with payment date inside tax period, **When** calculating tax, **Then** system applies tax percentage to allocation amount and rounds to two decimals
> 3. **Given** flat-value tax with partial allocation period overlap, **When** determining applicability, **Then** system calculates prorated amount using benefit duration and overlap percentage
> 4. **Given** extra withholding category, **When** evaluating applicability, **Then** system uses allocation period overlap instead of payment date condition
> 5. **Given** multiple tax types applicable to same allocation, **When** calculating withholdings, **Then** system processes each tax separately and aggregates total withholding
> 6. **Given** calculation complete, **When** finalizing payment, **Then** system prevents processing if calculated withholding exceeds allocation taxable amount


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=713700428"
> ]

---

#### Feature: As a Claims Adjuster, I want to apply overpayment withholdings to scheduled payments, so that I can recover overpaid amounts from future payments in a controlled manner
- **Role**: Claim Adjuster
- **Action**: apply overpayment withholdings to scheduled payments through automated calculation and allocation
- **Value**: I can systematically recover overpaid amounts from future payments while maintaining accurate claim balance reconciliation and financial control

**Description:**

> As a **Claim Adjuster**,
> I want to **apply overpayment withholdings to scheduled payments through automated calculation and allocation**,
> So that **I can systematically recover overpaid amounts from future payments while maintaining accurate claim balance reconciliation and financial control**


**Key Capabilities:**

> 1. System validates payment balance status to determine withholding eligibility
> 2. User is able to establish withholding parameters including percentage-based or flat-value recovery amounts
> 3. System calculates withholding amounts based on allocation gross amounts, proration rates, and duration
>     3.1 Upon percentage-based withholding, system computes amount from allocation gross totals
>     3.2 When flat-value withholding applies, system prorates based on duration and payment frequency
> 4. System applies withholding caps at total overpayment threshold and recalculates net payment amounts
> 5. System generates withholding allocations with adjustment transactions and suspense handling for unallocated amounts
> 6. User is able to review complete withholding details including allocations, reductions, and balance adjustments


**Acceptance Criteria:**

> 1. **Given** a payment with positive balance, **When** withholding process initiates, **Then** system exits without applying withholdings and preserves original payment
> 2. **Given** valid underpayment scenario, **When** withholding calculations execute, **Then** system generates reduction records for all configured withholdings
> 3. **Given** percentage-based withholding, **When** calculation runs, **Then** system computes amount from allocation gross totals and applies minimum of calculated or overpayment cap
> 4. **Given** flat-value withholding, **When** proration applies, **Then** system calculates based on duration, payment frequency, and appropriate rate number
> 5. **Given** withholding amounts exceed available allocations, **When** allocation generation completes, **Then** system creates suspense allocation for remaining unallocated amounts
> 6. **Given** withholding process completes, **When** payment finalizes, **Then** system recalculates net amounts and populates complete withholding details with allocations and adjustments


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=593277857"
> ]

---

#### Feature: As a Claims Adjuster, I want to generate third-party deduction payments from calculated scheduled payments, so that I can ensure deduction beneficiaries receive their entitled amounts
- **Role**: Claim Adjuster
- **Action**: generate third-party deduction payments from calculated scheduled payments
- **Value**: deduction beneficiaries receive their entitled amounts accurately and efficiently through consolidated payment transactions

**Description:**

> As a Claim Adjuster,
> I want to generate third-party deduction payments from calculated scheduled payments,
> So that deduction beneficiaries receive their entitled amounts accurately and efficiently through consolidated payment transactions


**Key Capabilities:**

> 1. System identifies eligible deductions from calculated scheduled payments based on deduction type and beneficiary presence.
> 2. System groups deductions by type and beneficiary to create consolidated deduction payment items.
>     2.1 Upon grouping, system generates payment allocations inheriting source allocation attributes and summing applicable amounts.
>     2.2 System reuses existing actual payments when matching criteria, otherwise creates new payment records.
> 3. System consolidates payment items by payee, payment date, and payment number to minimize transaction count.
> 4. System generates final outgoing deduction payments with aggregated allocations and calculated net amounts.
> 5. User is able to review generated deduction payments linked to originating scheduled payments for audit purposes.


**Acceptance Criteria:**

> 1. **Given** calculated scheduled payments contain eligible deductions, **When** payment generation is triggered, **Then** system creates deduction payment items only for applicable deduction types with assigned beneficiaries.
> 2. **Given** multiple deductions share the same type and beneficiary, **When** payment items are generated, **Then** system consolidates them into a single payment item with aggregated amounts.
> 3. **Given** an existing actual payment matches payee and allocation criteria, **When** generating deduction payments, **Then** system reuses the existing payment record instead of creating duplicates.
> 4. **Given** deduction payment items are grouped, **When** final payments are created, **Then** system generates one payment per unique combination of payee, payment date, and payment number.
> 5. **Given** all deduction payments are generated, **When** reviewing payment records, **Then** each payment maintains traceable links to source scheduled payment allocations.
> 6. **Given** incomplete or invalid deduction data, **When** attempting payment generation, **Then** system prevents processing and reports validation failures.


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=619718603"
> ]

---

#### Feature: As a Claims Adjuster, I want to calculate interest on late disability payments based on state-specific rules and thresholds, so that I can ensure compliant interest calculations for delayed benefits
- **Role**: Claim Adjuster
- **Action**: calculate and apply state-specific interest on late disability benefit payments based on regulatory thresholds and timing rules
- **Value**: I can ensure compliant interest calculations for delayed benefits, maintain regulatory adherence across jurisdictions, and accurately compensate claimants for payment delays

**Description:**

> As a **Claim Adjuster**,
> I want to **calculate and apply state-specific interest on late disability benefit payments based on regulatory thresholds and timing rules**,
> So that **I can ensure compliant interest calculations for delayed benefits, maintain regulatory adherence across jurisdictions, and accurately compensate claimants for payment delays**


**Key Capabilities:**

> 1. System determines allocation lateness by comparing benefit period completion, proof-of-loss receipt, and payment timing against state-specific thresholds.
> 2. System identifies applicable interest jurisdiction(s) using claimant address data, with special multi-state evaluation for Survivor Benefits considering beneficiary, plan holder, and subject-of-claim states.
> 3. System retrieves state-specific interest rates and threshold configurations, then calculates interest using formula: Principal × Annual Rate × ((Days Late - Threshold) ÷ 365).
>     3.1 Upon missing proof-of-loss date or invalid rate configuration, system defaults interest to zero and proceeds without calculation.
>     3.2 For Survivor Benefits, system calculates interest across all three jurisdictions and selects highest amount with defined tie-breaker rules.
> 4. System generates payment template additions with interest calculation metadata including applicable state, rate, principal, and paid-through date.
> 5. System creates allocation split records linking interest amounts to payment items and adjusts gross payment totals based on interest-only allocation status.
> 6. User is able to override default calculation parameters including interest paid-through date and principal amount during payment finalization workflow.


**Acceptance Criteria:**

> 1. **Given** a disability allocation with benefit period ended and proof-of-loss received beyond state threshold, **When** adjuster initiates payment calculation, **Then** system applies state-specific interest rate and generates payment addition with correct jurisdiction and amount.
> 2. **Given** a Survivor Benefit allocation, **When** system evaluates interest, **Then** system calculates interest for beneficiary state, plan holder situs state, and claimant state, selecting highest amount or applying tie-breaker hierarchy.
> 3. **Given** an allocation missing proof-of-loss receipt date, **When** interest calculation executes, **Then** system bypasses interest calculation, sets interest to zero, and proceeds with standard payment processing without error.
> 4. **Given** calculated days late minus state threshold results in zero or negative value, **When** system evaluates interest eligibility, **Then** system marks calculation invalid and applies zero interest.
> 5. **Given** interest calculation completes successfully, **When** system generates payment records, **Then** payment template includes addition with interest type, applicable state, rate, threshold, calculation basis, and paid-through date.
> 6. **Given** an interest-only allocation designation, **When** system finalizes payment item, **Then** gross payment amount adjusts to zero while preserving interest addition records.


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=737152384"
> ]

---

#### Feature: As a Claims Adjuster, I want to calculate interest on late Life insurance payments based on state-specific rules and loss type, so that I can ensure compliant interest calculations for delayed claims
- **Role**: Claim Adjuster
- **Action**: calculate and apply state-compliant interest on delayed life insurance claim payments based on jurisdictional rules and loss characteristics
- **Value**: payment accuracy is maintained, regulatory compliance is ensured across multiple jurisdictions, and beneficiaries receive entitled interest according to state-mandated thresholds and calculation methods

**Description:**

> As a Claim Adjuster,
> I want to calculate and apply state-compliant interest on delayed life insurance claim payments based on jurisdictional rules and loss characteristics,
> So that payment accuracy is maintained, regulatory compliance is ensured across multiple jurisdictions, and beneficiaries receive entitled interest according to state-mandated thresholds and calculation methods.


**Key Capabilities:**

> 1. System determines applicable jurisdiction(s) based on override settings or loss type—death claims evaluate beneficiary, decedent, and plan holder states
> 2. System retrieves state-specific configuration including interest rates, amount thresholds, time thresholds, and calculation methodology
> 3. System calculates interest using jurisdiction-specific formulas—compound annual, simple annual, or simple monthly based on configuration
>     3.1 Upon calculation, system compares result against amount and time thresholds, nullifying interest if either threshold is unmet
> 4. When multiple jurisdictions apply, system selects the state yielding highest compliant interest amount
> 5. System generates payment adjustment records with detailed interest calculation parameters and allocates interest amount to payment template
> 6. Upon interest-only allocation designation, system adjusts payment item gross amount accordingly


**Acceptance Criteria:**

> 1. **Given** state override is configured, **When** interest calculation initiates, **Then** system uses override jurisdiction regardless of loss type
> 2. **Given** death loss type without override, **When** calculation executes, **Then** system evaluates all three states and selects highest interest result
> 3. **Given** calculated interest below amount threshold or days below time threshold, **When** threshold validation occurs, **Then** system sets interest to zero
> 4. **Given** compound annual interest configuration, **When** system calculates interest, **Then** formula applies daily compounding with 365-day divisor
> 5. **Given** valid interest calculation, **When** system generates addition record, **Then** payment template includes detailed calculation parameters and correct addition type designation
> 6. **Given** missing rate or negative delay days, **When** validation executes, **Then** system marks calculation invalid and prevents interest application


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=591348404"
> ]

---

#### Feature: As a Claims Adjuster, I want to generate payment items for Life insurance recurring payments, so that I can create accurate schedules for ongoing benefit payments with proper period splits and prorations
- **Role**: Claim Adjuster
- **Action**: generate payment items for Life insurance recurring payments with accurate period splits and prorations
- **Value**: ongoing benefit payments are calculated correctly with proper temporal allocation and financial accuracy

**Description:**

> As a **Claim Adjuster**,
> I want to **generate payment items for Life insurance recurring payments with accurate period splits and prorations**,
> So that **ongoing benefit payments are calculated correctly with proper temporal allocation and financial accuracy**


**Key Capabilities:**

> 1. System generates actual payment items by matching payment allocations to executed payments based on payee, claim, and coverage criteria
> 2. System identifies missed payment periods by comparing allocation schedules against actual payment history up to the latest payment date
> 3. System creates upcoming payment items by splitting allocation periods according to frequency rules and calculating payment dates (7 days before period end, adjusted for holidays)
>     3.1 When no actual payments exist, system uses earliest allocation start date as baseline
>     3.2 When multiple overdue periods exist, system merges them into single payment item
> 4. System calculates payable duration using proration rate (1/30 method: full months converted to 30 days plus remainder days)
> 5. System computes prorated gross benefit amount by multiplying gross benefit, payable duration, and proration rate, rounded to two decimals
> 6. System sequences all payment items chronologically by benefit period end date for processing integrity


**Acceptance Criteria:**

> 1. **Given** payment template with allocations, **When** matching actual payments exist, **Then** system generates actual payment items with correct benefit periods and payment dates
> 2. **Given** actual payment history exists, **When** gaps are detected in allocation coverage, **Then** system generates missed payment items for unpaid periods up to latest actual payment date
> 3. **Given** allocation frequency is defined, **When** generating upcoming payments, **Then** system splits periods correctly and calculates payment dates 7 days before period end (adjusted for holidays and current date)
> 4. **Given** allocation period spans partial months, **When** applying 1/30 proration rate, **Then** system calculates payable duration as (full months × 30) + remainder days
> 5. **Given** payable duration is determined, **When** calculating final amount, **Then** system produces prorated gross benefit rounded to two decimals
> 6. **Given** multiple overdue upcoming periods exist, **When** processing allocations, **Then** system merges them into single consolidated payment item


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=628361897"
> ]

---

#### Feature: As a Claims Adjuster, I want to generate payment items for Life insurance non-recurring and Ex Gratia payments, so that I can create accurate one-time payment schedules
- **Role**: Claim Adjuster
- **Action**: generate payment items for Life insurance non-recurring and Ex Gratia payments
- **Value**: I can create accurate one-time payment schedules with proper beneficiary allocation and interest calculations

**Description:**

> As a **Claim Adjuster**,
> I want to **generate payment items for Life insurance non-recurring and Ex Gratia payments**,
> So that **I can create accurate one-time payment schedules with proper beneficiary allocation and interest calculations**


**Key Capabilities:**

> 1. System validates claim type against supported Life insurance categories before proceeding with payment generation
> 2. System locates existing actual payment records matching allocation and payee criteria to determine payment timing
> 3. System evaluates recurrence eligibility based on loss type, coverage type, and frequency to route payment creation
> 4. Upon non-recurring determination, system generates single payment item with beneficiary percentage allocation applied to gross amounts
>     4.1 When multiple accumulator extension terms exist, system splits payment into separate items per period with proportional amounts
> 5. System calculates and applies interest additions when allocation interest details are present
> 6. System produces finalized payment scheduler items ready for execution with complete financial and payee attribution


**Acceptance Criteria:**

> 1. **Given** a supported Life claim type allocation, **When** payment generation initiates, **Then** system proceeds with item creation workflow
> 2. **Given** unsupported claim type, **When** validation occurs, **Then** system terminates process without generating payment items
> 3. **Given** beneficiary payee with allocation percentage, **When** gross amount calculates, **Then** system applies percentage multiplier to template allocation amount
> 4. **Given** multiple accumulator details with different extension terms, **When** payment item generates, **Then** system creates separate items per period with evenly split amounts
> 5. **Given** interest details configured on allocation, **When** payment finalizes, **Then** system calculates and adds interest per defined rules
> 6. **Given** no actual payment found, **When** payment date assigns, **Then** system defaults to current system time


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=583834447"
> ]

---

#### Feature: As a Claims Adjuster, I want to generate payment items for Expense and Ex Gratia reserve allocations, so that I can create accurate payment schedules for non-indemnity reserves
- **Role**: Claim Adjuster
- **Action**: generate payment items from Expense and Ex Gratia reserve allocations
- **Value**: accurate payment schedules can be created for non-indemnity reserves with proper linkage to actual payments and expense tracking

**Description:**

> As a Claim Adjuster,
> I want to generate payment items from Expense and Ex Gratia reserve allocations,
> So that accurate payment schedules can be created for non-indemnity reserves with proper linkage to actual payments and expense tracking


**Key Capabilities:**

> 1. System validates reserve allocation type to determine eligibility for payment item generation (Expense Reserve required)
> 2. System locates corresponding actual payment by matching expense number and payee allocation criteria
> 3. System generates payment item with attributes mapped from actual payment data when match is found
>     3.1 Upon successful match, payment date and actual payment number are populated from actual payment records
>     3.2 Upon no match found, system applies default values using current system time and allocation template data
> 4. System populates payee, provider, claim, policy, and gross amount details from allocation records
> 5. System handles missing actual payment scenarios by creating payment items with alternative data sources
> 6. System maintains linkage between payment items, expense numbers, and allocation records for tracking


**Acceptance Criteria:**

> 1. **Given** an Expense Reserve allocation exists, **When** payment item generation is initiated, **Then** system proceeds with creating payment item from template allocation
> 2. **Given** allocation reserve type is not Expense Reserve, **When** generation process runs, **Then** system skips payment item creation entirely
> 3. **Given** actual payment matching expense number and payee exists, **When** payment item is generated, **Then** system populates payment date and actual payment number from actual payment record
> 4. **Given** no matching actual payment exists, **When** payment item is generated, **Then** system uses current system time for payment date and null for actual payment number
> 5. **Given** payment item generation completes, **When** reviewing output, **Then** all mandatory attributes (payee, claim, policy, gross amount, expense number) are populated from allocation data
> 6. **Given** multiple actual payments exist for same expense, **When** system searches for match, **Then** first payment meeting all criteria is selected


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=609533223"
> ]

---

#### Feature: As a Claims Adjuster, I want to map payment items to payment allocations with all required financial details, so that I can create complete payment records with accurate allocation information
- **Role**: Claim Adjuster
- **Action**: map payment items to payment allocations with comprehensive financial details and line-of-business-specific attributes
- **Value**: complete payment records are generated with accurate allocation information, ensuring proper financial tracking, beneficiary assignments, and regulatory compliance across different claim types

**Description:**

> As a **Claim Adjuster**,
> I want to **map payment items to payment allocations with comprehensive financial details and line-of-business-specific attributes**,
> So that **complete payment records are generated with accurate allocation information, ensuring proper financial tracking, beneficiary assignments, and regulatory compliance across different claim types**.


**Key Capabilities:**

> 1. System transforms payment item groups and templates into structured payment entities by mapping core financial attributes including payee details, payment dates, tax exemptions, and earnings data.
> 2. System calculates Last Work Date by analyzing work periods from template data, absence records, and disability information, then determining date based on payment timing.
> 3. System identifies applicable template allocations for each payment item by matching payable items per defined business rules.
> 4. System generates payment allocations by mapping financial attributes including allocation source, reserve type, gross amounts, loss information, and beneficiary details.
> 5. System applies Line-of-Business-specific mappings, adding proration rates and taxable percentages for Disability claims, or benefit amounts per unit for Life claims.
> 6. System consolidates addition and reduction split results, accumulator details, and expense tracking data into each allocation record.


**Acceptance Criteria:**

> 1. **Given** a payment items group with payee and payment method details, **When** the mapping process executes, **Then** the system creates a payment entity with outgoing direction, populated payee information, and tax exemption attributes from the template.
> 2. **Given** multiple work period sources and a payment date, **When** calculating Last Work Date, **Then** the system sets the date to payment date if it falls within work periods, otherwise uses the latest prior period end date.
> 3. **Given** payment items with specific claim and coverage details, **When** identifying applicable allocations, **Then** the system matches template allocations based on payable item matching rules and creates corresponding payment allocations.
> 4. **Given** a Disability LOB allocation, **When** mapping attributes, **Then** the system includes proration rate, taxable percentage, and benefit duration fields in addition to common allocation attributes.
> 5. **Given** a Life LOB recurring payment allocation, **When** mapping attributes, **Then** the system includes prorated gross amount, prorating rate, and benefit amount per unit.
> 6. **Given** incomplete or mismatched payment item data, **When** attempting allocation mapping, **Then** the system prevents payment generation and identifies missing required financial details.


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=591342879"
> ]

---
## Initiative: Payment Generation & Financial Posting

### Epic: Payment Generation & Financial Posting

#### Feature: As a Claims Operations Manager, I want to configure and schedule the Payment Generation Job using cron expressions, so that payments are generated automatically at specified times and intervals without manual intervention.
- **Role**: Claim Manager
- **Action**: configure and schedule automated payment generation jobs using time-based expressions
- **Value**: payments are generated automatically at specified intervals without manual intervention, ensuring timely disbursements and reducing operational overhead

**Description:**

> As a **Claim Manager**,
> I want to **configure and schedule automated payment generation jobs using time-based expressions**,
> So that **payments are generated automatically at specified intervals without manual intervention, ensuring timely disbursements and reducing operational overhead**


**Key Capabilities:**

> 1. User is able to define automated job schedules using temporal expressions specifying execution frequency (seconds, minutes, hours, days, months, weekdays).
>     1.1 When specifying calendar-based schedules, user can define either specific dates or weekdays but not both simultaneously.
>     1.2 Upon needing multiple execution times, user can specify value lists or ranges within scheduling parameters.
> 2. User is able to configure interval-based execution patterns for regular payment processing cycles.
> 3. System validates scheduling expressions against allowed temporal ranges and operator constraints.
> 4. Upon successful configuration, system registers and activates the payment generation job according to defined schedule.
> 5. System executes payment generation process automatically at each scheduled occurrence without manual triggering.


**Acceptance Criteria:**

> 1. **Given** valid scheduling parameters are provided, **When** job configuration is submitted, **Then** system activates automated payment generation at specified intervals.
> 2. **Given** conflicting calendar specifications exist, **When** validation occurs, **Then** system prevents submission until conflicts are resolved.
> 3. **Given** scheduling expression contains invalid temporal values, **When** configuration is attempted, **Then** system rejects the expression and provides correction guidance.
> 4. **Given** active payment job exists, **When** scheduled execution time occurs, **Then** system initiates payment generation process automatically.
> 5. **Given** multiple execution times are configured, **When** job runs, **Then** system processes payments at each specified occurrence.
> 6. **Given** job execution completes, **When** financial posting occurs, **Then** system records transaction timestamps matching scheduled execution times.


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=339822757"
> ]

---

#### Feature: As a Claims Adjuster, I want to review and manage failed payment transactions, so that I can investigate payment issues and take corrective action.
- **Role**: Claim Adjuster
- **Action**: review and resolve failed payment transactions through automated task management
- **Value**: payment issues are promptly investigated and corrective actions are taken to ensure successful claim settlements

**Description:**

> As a **Claim Adjuster**,
> I want to **review and resolve failed payment transactions through automated task management**,
> So that **payment issues are promptly investigated and corrective actions are taken to ensure successful claim settlements**


**Key Capabilities:**

> 1. System detects payment or underpayment transaction failures automatically
> 2. Upon failure detection, system generates 'Review Failed Payment' task without manual intervention
> 3. Adjuster receives task assignment for investigation of root cause
> 4. Adjuster analyzes transaction failure details and identifies corrective action required
> 5. Adjuster executes resolution steps to retry or adjust payment processing
> 6. System confirms successful payment completion or escalates for additional review


**Acceptance Criteria:**

> 1. **Given** a payment transaction fails, **When** the failure is recorded, **Then** the system automatically creates a 'Review Failed Payment' task
> 2. **Given** an underpayment transaction fails, **When** the failure occurs, **Then** the same automated task creation workflow triggers
> 3. **Given** task is created, **When** adjuster accesses it, **Then** failure details and transaction context are available for investigation
> 4. **Given** adjuster investigates failure, **When** corrective action is taken, **Then** system allows payment reprocessing or escalation
> 5. **Given** resolution is completed, **When** payment succeeds, **Then** task closes and payment posts to financial records
> 6. **Given** incomplete investigation, **When** adjuster attempts closure, **Then** system prevents task completion until resolution is documented


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=653594291"
> ]

---
## Initiative: Lifecycle Maintenance & Case Closure

### Epic: Lifecycle Maintenance & Case Closure

#### Feature: As a Claims Adjuster, I want to close a claim by transitioning it to Closed status, so that I can mark the claim as complete and prevent further modifications
- **Role**: Claim Adjuster
- **Action**: close a claim by transitioning it to Closed status
- **Value**: I can finalize the claim lifecycle, mark it as complete, and prevent further modifications while ensuring proper case and task completion

**Description:**

> As a **Claim Adjuster**,
> I want to **close a claim by transitioning it to Closed status**,
> So that **I can finalize the claim lifecycle, mark it as complete, and prevent further modifications while ensuring proper case and task completion**


**Key Capabilities:**

> 1. System validates the closure request and verifies performer privileges for claim closure authority
> 2. System evaluates lifecycle configuration to determine if closure is permitted from current claim status
>     2.1 If closure is not allowed from current status, system prevents action and notifies performer
> 3. Upon successful validation, system transitions claim to Closed status and triggers closure business activity
> 4. System completes associated case by invoking case management services
> 5. System completes related review tasks and updates task statuses accordingly
> 6. System returns finalized claim image confirming closure completion


**Acceptance Criteria:**

> 1. **Given** a claim exists and performer has closure privileges, **When** closure is requested, **Then** system validates request and checks lifecycle rules
> 2. **Given** current status permits closure, **When** validation succeeds, **Then** claim transitions to Closed status and closure activity triggers
> 3. **Given** closure command cannot execute from current status, **When** validation fails, **Then** system prevents closure and returns appropriate error notification
> 4. **Given** claim closes successfully, **When** status updates, **Then** associated case and tasks complete automatically
> 5. **Given** claim reaches Closed status, **When** closure finalizes, **Then** system prevents further claim modifications
> 6. **Given** closure completes, **When** processing finishes, **Then** system returns updated claim image to performer


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=528757502"
> ]

---

#### Feature: As a Claims Adjuster, I want to reopen a closed claim and restore it to its previous status, so that I can resume processing if new information becomes available
- **Role**: Claim Adjuster
- **Action**: reopen a closed claim and restore it to its previous operational status
- **Value**: I can resume claim processing activities when new information, evidence, or circumstances emerge after initial closure

**Description:**

> As a **Claim Adjuster**,
> I want to **reopen a closed claim and restore it to its previous operational status**,
> So that **I can resume claim processing activities when new information, evidence, or circumstances emerge after initial closure**


**Key Capabilities:**

> 1. System validates performer privileges and claim eligibility for reopen action
> 2. System verifies closed claim exists and reopen command is permitted per lifecycle configuration rules
> 3. System restores claim to its prior operational status before closure
> 4. System reactivates associated work management cases and tasks for continued processing
> 5. System maintains audit trail documenting reopening justification and timestamp
>     5.1 Upon lifecycle violation, system prevents reopening and returns configuration error


**Acceptance Criteria:**

> 1. **Given** a claim in Closed status, **When** authorized adjuster initiates reopen with valid justification, **Then** system restores claim to pre-closure status and reactivates work queues
> 2. **Given** lifecycle rules prohibit reopening, **When** reopen is attempted, **Then** system denies action and returns configuration constraint message
> 3. **Given** performer lacks reopen privileges, **When** command is submitted, **Then** system blocks operation and logs unauthorized attempt
> 4. **Given** successful reopening, **When** claim is restored, **Then** all historical data and attachments remain intact and accessible


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=528757502"
> ]

---

#### Feature: As a Claims Adjuster, I want to validate that a close or reopen action is permitted from the current claim status, so that I can ensure only valid state transitions occur
- **Role**: Claim Adjuster
- **Action**: validate that close or reopen actions are permitted from the current claim status before execution
- **Value**: only valid state transitions occur, preventing invalid claim status changes and maintaining data integrity throughout the claim lifecycle

**Description:**

> As a **Claim Adjuster**,
> I want to **validate that close or reopen actions are permitted from the current claim status before execution**,
> So that **only valid state transitions occur, preventing invalid claim status changes and maintaining data integrity throughout the claim lifecycle**.


**Key Capabilities:**

> 1. System retrieves current claim status and evaluates available actions based on state machine configuration.
> 2. Upon close request, system validates claim is in Incomplete, Pending, or Open status.
>     2.1 System confirms all prerequisite conditions for closure are met.
>     2.2 System prevents closure if payments are pending or required data is incomplete.
> 3. Upon reopen request, system validates claim is in Closed status.
>     3.1 System identifies previous status before closure (Incomplete, Pending, or Open).
>     3.2 System applies all business rules validation for target status.
> 4. System blocks unauthorized transition attempts and provides business-appropriate guidance.
> 5. System logs all transition validation outcomes for audit purposes.


**Acceptance Criteria:**

> 1. **Given** a claim in Open status, **when** adjuster initiates close action, **then** system permits transition to Closed status.
> 2. **Given** a claim in Closed status, **when** adjuster initiates close action, **then** system prevents transition and indicates invalid operation.
> 3. **Given** a claim in Closed status, **when** adjuster initiates reopen action, **then** system permits transition to previous status with rules validation.
> 4. **Given** a claim in Incomplete status, **when** adjuster initiates reopen action, **then** system prevents transition and indicates reopen is unavailable.
> 5. **Given** any invalid transition attempt, **when** validation fails, **then** system maintains current status without change.
> 6. **Given** successful validation, **when** transition executes, **then** system updates status and logs the transition event.


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=528744707"
> ]

---

#### Feature: As a Claims Adjuster, I want to close a settlement by transitioning it through adjudication, approval, and closure states, so that I can finalize settlement processing
- **Role**: Claim Adjuster
- **Action**: transition settlements through adjudication, approval, and closure states to finalize settlement processing
- **Value**: settlements are properly validated, calculated, and closed in compliance with policy terms and business rules

**Description:**

> As a **Claim Adjuster**,
> I want to **transition settlements through adjudication, approval, and closure states to finalize settlement processing**,
> So that **settlements are properly validated, calculated, and closed in compliance with policy terms and business rules**


**Key Capabilities:**

> 1. **Initiate Settlement Adjudication**: Upon loss adjudication trigger, system creates new settlement and transitions to adjudicating state
> 2. **Execute Settlement Calculation**: System validates applicability and eligibility rules, calculates amounts based on coverage limits and deductibles, then transitions to pending state
> 3. **Approve Settlement Decision**: When eligibility rules pass without critical violations, system transitions settlement to approved state
>     3.1 If eligibility fails or critical messages exist, settlement remains pending
> 4. **Process Settlement Denial**: User is able to disapprove pending settlements and transition to disapproved state
> 5. **Trigger Settlement Readjudication**: Upon request or data updates, system reruns validation and calculation processes, returning to adjudicating state
> 6. **Finalize Settlement Closure**: System closes settlements from approved or disapproved states to complete lifecycle


**Acceptance Criteria:**

> 1. **Given** settlement adjudication is requested, **When** loss data is captured, **Then** system creates settlement in adjudicating state and validates applicability rules
> 2. **Given** settlement is adjudicating, **When** eligibility rules and calculations complete successfully, **Then** system transitions to pending state
> 3. **Given** settlement is pending with eligible status and no critical violations, **When** approval is executed, **Then** system transitions to approved state
> 4. **Given** settlement has eligibility failures or critical messages, **When** approval is attempted, **Then** system prevents approval and maintains pending state
> 5. **Given** settlement is approved or disapproved, **When** readjudication is triggered, **Then** system re-executes validation and recalculation processes
> 6. **Given** settlement is approved or disapproved, **When** closure is initiated, **Then** system finalizes and transitions to closed state


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=515224146"
> ]

---

#### Feature: As a Claims Adjuster, I want to provide a reason and note when closing a claim, so that I can document the closure rationale for audit and compliance purposes
- **Role**: Claim Adjuster
- **Action**: finalize claim closure with documented rationale and resolution status
- **Value**: the closure decision is auditable, compliant with regulatory requirements, and reflects accurate financial and operational resolution

**Description:**

> As a **Claim Adjuster**,
> I want to **finalize claim closure with documented rationale and resolution status**,
> So that **the closure decision is auditable, compliant with regulatory requirements, and reflects accurate financial and operational resolution**.


**Key Capabilities:**

> 1. Adjuster initiates closure workflow and selects mandatory closure rationale category aligned with financial resolution status
> 2. System validates claim eligibility based on current status, outstanding financial obligations, and payment completion
>     2.1 When incomplete payments or premium waiver periods exist, system blocks closure until resolved
>     2.2 When unpaid coverages exist, system enforces 'Partially Paid' rationale selection
> 3. Adjuster provides supplementary notes per business rule requirements to document closure context
> 4. Upon successful validation, system transitions claim to closed status, terminates active processes, enforces read-only state, and enables reopening capability


**Acceptance Criteria:**

> 1. **Given** claim is in eligible operational status, **When** adjuster submits closure with valid rationale, **Then** system transitions claim to closed state and terminates all active workflows
> 2. **Given** incomplete payments exist, **When** adjuster attempts closure, **Then** system blocks submission and displays resolution requirements
> 3. **Given** issued payments exist, **When** adjuster selects denial/withdrawal/termination rationale, **Then** system prevents closure due to financial inconsistency
> 4. **Given** unpaid coverages remain, **When** adjuster proceeds with closure, **Then** system enforces 'Partially Paid' rationale selection
> 5. **Given** claim successfully closes, **When** adjuster views claim record, **Then** interface becomes read-only with reopening option available
> 6. **Given** mandatory note rules apply, **When** adjuster omits documentation, **Then** system prevents closure submission


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=536085613"
> ]

---

#### Feature: As a Claims Adjuster, I want to view and validate open items before closing a claim, so that I can ensure all outstanding issues are resolved or documented
- **Role**: Claim Adjuster
- **Action**: validate and resolve outstanding open items before finalizing claim closure
- **Value**: all financial obligations, tasks, and approval periods are completed or properly documented, preventing improper claim closures and ensuring regulatory compliance

**Description:**

> As a **Claim Adjuster**,
> I want to **validate and resolve outstanding open items before finalizing claim closure**,
> So that **all financial obligations, tasks, and approval periods are completed or properly documented, preventing improper claim closures and ensuring regulatory compliance**.


**Key Capabilities:**

> 1. User initiates claim closure process for claims in incomplete, pending, or open status
> 2. System validates payment completeness and flags unissued posted payments as hard stop items
> 3. System enforces closure reason alignment with payment status (e.g., prevents denial reasons when issued payments exist)
> 4. System identifies unpaid coverages or unposted recurring payment allocations and enforces 'Partially Paid' reason selection
> 5. System validates completion of premium waiver approval periods as hard stop requirement
> 6. Upon successful closure, system transitions claim to read-only state and terminates active processes automatically


**Acceptance Criteria:**

> 1. **Given** claim has incomplete posted payments, **When** user attempts closure, **Then** system prevents submission with hard stop alert
> 2. **Given** issued payments exist, **When** user selects denial/withdrawn/terminated reason, **Then** system blocks closure
> 3. **Given** unpaid coverages or unposted payments exist, **When** user attempts closure, **Then** system requires 'Partially Paid' reason selection
> 4. **Given** incomplete premium waiver periods exist, **When** user attempts closure, **Then** system prevents submission with hard stop alert
> 5. **Given** all validations pass, **When** user submits closure, **Then** system updates status, terminates active tasks, and enables read-only mode
> 6. **Given** claim status is closed/denied/terminated, **When** user accesses closure function, **Then** system disables closure action


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=536085613"
> ]

---

#### Feature: As a Claims Adjuster, I want to automatically close related tasks and cases when closing a claim, so that the entire claim lifecycle is properly concluded
- **Role**: Claim Adjuster
- **Action**: automatically close related tasks, processes, and cases when closing a claim to ensure complete lifecycle conclusion
- **Value**: the entire claim lifecycle is properly concluded with all dependencies resolved, preventing orphaned tasks and ensuring data integrity

**Description:**

> As a Claim Adjuster,
> I want to automatically close related tasks, processes, and cases when closing a claim to ensure complete lifecycle conclusion,
> So that the entire claim lifecycle is properly concluded with all dependencies resolved, preventing orphaned tasks and ensuring data integrity


**Key Capabilities:**

> 1. User initiates claim closure by selecting closure action and providing business reason and documentation.
> 2. System validates closure eligibility by checking for hard-stop open items, unpaid coverages, and unposted payments.
>     2.1 If issued payments exist, system restricts Denied/Withdrawn/Terminated reasons.
>     2.2 If unpaid items exist, system enforces 'Partially Paid' reason selection.
> 3. Upon validation success, system automatically terminates active CMMN processes and all related tasks under the claim.
> 4. System updates claim status to 'Closed' and prevents future data cascading from parent case updates.
> 5. System disables all modification actions while preserving view-only access to historical data and transaction history.
> 6. User receives confirmation of successful closure with final status display on claim overview.


**Acceptance Criteria:**

> 1. **Given** a claim with no hard-stop open items, **When** adjuster submits closure with valid reason, **Then** system closes all related tasks and processes automatically and updates claim status to 'Closed'.
> 2. **Given** a claim with issued payments, **When** adjuster selects Denied/Withdrawn/Terminated reason, **Then** system prevents closure and prompts for appropriate reason selection.
> 3. **Given** unpaid coverages or unposted payments exist, **When** adjuster attempts closure, **Then** system enforces 'Partially Paid' reason selection.
> 4. **Given** hard-stop open items exist, **When** adjuster attempts closure, **Then** system prevents submission until items are resolved.
> 5. **Given** claim is successfully closed, **When** parent case is updated, **Then** system prevents data cascading to closed claim.
> 6. **Given** claim is closed, **When** user views claim overview, **Then** all modification actions are hidden except 'Reopen Claim' and 'Follow Up Task'.


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=669747804"
> ]

---

#### Feature: As a Claims Adjuster, I want to restrict editing and modifications on a closed claim, so that claim data integrity is maintained and accidental changes are prevented
- **Role**: Claim Adjuster
- **Action**: restrict modifications and editing capabilities on closed claims
- **Value**: claim data integrity is maintained, accidental changes are prevented, and the claim record remains immutable for audit and compliance purposes

**Description:**

> As a **Claim Adjuster**,
> I want to **restrict modifications and editing capabilities on closed claims**,
> So that **claim data integrity is maintained, accidental changes are prevented, and the claim record remains immutable for audit and compliance purposes**


**Key Capabilities:**

> 1. Upon claim closure, system terminates active case management processes and updates claim status to 'Closed'
> 2. System disables case cascading to prevent upstream changes from impacting closed claim data
> 3. System removes all transactional capabilities including:
>     3.1 Beneficiary management and plan modifications
>     3.2 Coverage adjustments and payment processing actions
>     3.3 Party additions and deduction edits
> 4. System restricts action menu to reopening and follow-up tasks only
> 5. User is able to view historical data including accumulator transactions without editing privileges
> 6. System maintains read-only access to closed claim details for audit and reporting purposes


**Acceptance Criteria:**

> 1. **Given** a claim is closed, **When** user accesses the claim overview, **Then** system hides all add/edit/delete buttons and displays claim in read-only mode
> 2. **Given** a closed claim exists, **When** case-level updates occur, **Then** system prevents data synchronization and preserves original claim snapshot
> 3. **Given** user attempts to modify closed claim data, **When** action is initiated, **Then** system blocks the transaction and prevents any data changes
> 4. **Given** a closed claim, **When** user accesses action menu, **Then** system displays only 'Reopen Claim' and 'Follow Up Task' options
> 5. **Given** historical inquiry need, **When** user views closed claim, **Then** system provides read-only access to all claim components and transaction history


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=669747804"
> ]

---

#### Feature: As a Claims Operations Manager, I want to automatically close claims and event cases when all settlements are approved and payments are issued, so that the closure process is efficient and compliant
- **Role**: Claim Manager
- **Action**: automatically close claims and event cases when all settlements are approved and payments are issued
- **Value**: the closure process is efficient, compliant, and eliminates manual intervention for eligible cases

**Description:**

> As a Claim Manager,
> I want to automatically close claims and event cases when all settlements are approved and payments are issued,
> So that the closure process is efficient, compliant, and eliminates manual intervention for eligible cases


**Key Capabilities:**

> 1. System initiates auto-close evaluation upon payment schedule completion.
> 2. System validates auto-close eligibility based on claim state, settlement approval status, and auto-adjudication confirmation.
> 3. System verifies closure prerequisites including payment issuance, payee balance reconciliation, and task completion.
>     3.1 Upon failure, system generates exception task for manual review.
> 4. System closes all eligible claims within the event case.
> 5. System evaluates event case closure readiness when all associated claims are closed.
> 6. System completes closure and updates lifecycle status accordingly.


**Acceptance Criteria:**

> 1. **Given** payment schedule is completed, **When** all claims meet eligibility criteria and prerequisites, **Then** system closes claims and event case automatically without manual intervention.
> 2. **Given** claim is not in 'Open' state or settlements are unapproved, **When** auto-close is triggered, **Then** system halts process without closing.
> 3. **Given** payments are not fully issued or balances exist, **When** closure prerequisites fail, **Then** system generates 'Auto Adjudication Closure Failed' task.
> 4. **Given** event case has unclosed claims, **When** closure is attempted, **Then** system closes only eligible claims and leaves event case open.
> 5. **Given** all tasks except 'New Case' or 'New Claim' are incomplete, **When** validation occurs, **Then** system prevents closure.
> 6. **Given** all claims closed within event case, **When** event case is open, **Then** system closes event case automatically.


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=657907234"
> ]

---

#### Feature: As a Claims Adjuster, I want to validate closure eligibility based on payment status and open items, so that I can ensure claims are only closed when appropriate conditions are met
- **Role**: Claim Adjuster
- **Action**: validate closure eligibility based on payment status and open items, then process claim closure when conditions are met
- **Value**: claims are properly closed only when business rules are satisfied, preventing premature closure and maintaining data integrity

**Description:**

> As a **Claim Adjuster**,
> I want to **validate closure eligibility based on payment status and open items, then process claim closure when conditions are met**,
> So that **claims are properly closed only when business rules are satisfied, preventing premature closure and maintaining data integrity**


**Key Capabilities:**

> 1. User initiates claim closure workflow after payments have been issued
> 2. System validates closure reason compatibility with payment history
>     2.1 Upon selecting denied/withdrawn/terminated reasons with existing issued payments, system prevents closure
>     2.2 When unpaid coverages or pending payments exist, system enforces 'Partially Paid' reason
> 3. System evaluates open items and identifies hard-stop blocking conditions
> 4. User resolves identified hard-stop items before proceeding
> 5. User confirms closure eligibility and submits closure request
> 6. System finalizes closure by updating claim status, terminating active processes, and restricting further modifications


**Acceptance Criteria:**

> 1. **Given** claim has issued payments, **When** user selects denied/withdrawn/terminated closure reason, **Then** system prevents closure and prompts for valid reason
> 2. **Given** unpaid coverages or pending payments exist, **When** user attempts closure, **Then** system enforces 'Partially Paid' reason selection
> 3. **Given** hard-stop open items exist, **When** user submits closure, **Then** system blocks closure until items are resolved
> 4. **Given** all closure conditions are satisfied, **When** user completes closure process, **Then** system updates claim status to closed and terminates active workflows
> 5. **Given** claim is closed, **When** case updates occur, **Then** system prevents cascading changes to closed claim data
> 6. **Given** ATP claims with non-blocking incomplete payments, **When** no hard-stop items exist, **Then** system allows closure to proceed


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=702098309"
> ]

---

#### Feature: As a Claims Adjuster, I want to manage Event Case lifecycle through creation, submission, and closure states, so that I can coordinate multiple related claims under a single umbrella
- **Role**: Claim Adjuster
- **Action**: manage Event Case lifecycle through creation, submission, and closure states
- **Value**: I can coordinate multiple related claims under a single umbrella and ensure proper state transitions with validation and control

**Description:**

> As a **Claim Adjuster**,
> I want to **manage Event Case lifecycle through creation, submission, and closure states**,
> So that **I can coordinate multiple related claims under a single umbrella and ensure proper state transitions with validation and control**


**Key Capabilities:**

> 1. Initiate Event Case in Incomplete state with required data collection
> 2. Update case draft or modify case details, triggering automated processing when needed
> 3. Submit case for validation, transitioning from Incomplete to Open state and executing applicability rules
> 4. Process case in Open state by setting sub-status, finalizing, or updating details
> 5. Close case upon payment completion or cancellation
>     5.1 Upon closure from Open or Incomplete states, system records final status
> 6. Reopen closed cases to previous state when additional processing required


**Acceptance Criteria:**

> 1. **Given** case is initiated, **When** required data provided, **Then** system creates case in Incomplete state
> 2. **Given** case is Incomplete, **When** submission triggered, **Then** system validates data and transitions to Open state with applicability evaluation
> 3. **Given** case is Open, **When** updates occur, **Then** system transitions back to Incomplete requiring re-submission
> 4. **Given** processing complete, **When** closure triggered, **Then** system transitions to Closed state from Open or Incomplete
> 5. **Given** case is Closed, **When** reopening requested, **Then** system restores previous state preserving sub-status
> 6. **Given** insufficient privileges, **When** action attempted, **Then** system prevents unauthorized state transitions


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=547987768"
> ]

---

### Epic: Payment Processing & Financial Management

#### Feature: As a Claims Adjuster, I want to create and manage payments for claims, so that I can allocate benefits according to predefined strategies
- **Role**: Claim Adjuster
- **Action**: create and manage payments throughout their complete lifecycle from template creation through issuance
- **Value**: benefits are allocated accurately according to predefined strategies, ensuring timely and compliant payment disbursement to payees

**Description:**

> As a Claim Adjuster,
> I want to create and manage payments throughout their complete lifecycle from template creation through issuance,
> So that benefits are allocated accurately according to predefined strategies, ensuring timely and compliant payment disbursement to payees


**Key Capabilities:**

> 1. User initiates payment creation by providing payee information and coverage allocations for template generation
> 2. System retrieves financial details from claims and coverages, then calculates payment amounts with adjustments and tax information through rule engine
> 3. System generates payment schedule with calculated amounts and presents allocation preview for user validation and amendments
> 4. Upon confirmation, system persists payment template and schedule, automatically generating payment definitions when post dates arrive
> 5. System validates authority levels and routes payments for approval, then processes issuance requests to payment hub upon approval
> 6. User manages exceptions through suspension, cancellation, or failure handling (decline/void/stop) with automatic accumulator adjustments and reissuance workflows


**Acceptance Criteria:**

> 1. **Given** valid payee and coverage data, **When** user completes payment creation wizard, **Then** system generates payment template and schedule with accurate calculated amounts
> 2. **Given** payment schedule exists, **When** post date arrives and authority validation passes, **Then** system automatically generates and activates payment definition
> 3. **Given** approved payment, **When** issuance is requested, **Then** system dispatches to payment hub and updates status to Issued with accumulator adjustments
> 4. **Given** insufficient authority level, **When** approval validation fails, **Then** system creates user task and enables manual activation capability
> 5. **Given** issued payment requires cancellation, **When** user initiates failure action (decline/void/stop), **Then** system reverts used amounts to reserved and updates payment status accordingly
> 6. **Given** payment schedule requires modification, **When** user updates allocations for pending or approved payments, **Then** system recalculates schedule and persists new version without disrupting issued payments


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=596026302"
> ]

---

#### Feature: As a Claims Adjuster, I want to view and sort payments and recoveries by date, payee, and amount, so that I can efficiently manage case financials
- **Role**: Claim Adjuster
- **Action**: view, sort, and analyze payments and recoveries across multiple dimensions to maintain comprehensive oversight of case financial activities
- **Value**: I can efficiently track cash flow, identify patterns, reconcile transactions, and ensure financial accuracy across all managed cases

**Description:**

> As a Claim Adjuster,
> I want to view, sort, and analyze payments and recoveries across multiple dimensions to maintain comprehensive oversight of case financial activities,
> So that I can efficiently track cash flow, identify patterns, reconcile transactions, and ensure financial accuracy across all managed cases


**Key Capabilities:**

> 1. User accesses consolidated financial transaction dashboard displaying all payments and recoveries associated with managed cases
> 2. User applies sorting criteria by transaction date, payee identity, payment amount, or transaction type to organize financial data
>     2.1 Upon selecting date sorting, system chronologically orders transactions for cash flow analysis
>     2.2 Upon selecting payee sorting, system groups transactions by recipient for reconciliation
> 3. User filters transaction types including master payments, deduction payments (child support, wage garnishment), tax withholdings (federal, state, FICA), and recovery amounts
> 4. User reviews aggregated financial summaries showing total outflows, withholdings, and net payments per case
> 5. System reflects real-time updates when financial adjustments or new payments are processed


**Acceptance Criteria:**

> 1. **Given** multiple cases with payment history, **When** user accesses financial tracking interface, **Then** system displays all payments and recoveries with sortable columns for date, payee, and amount
> 2. **Given** transactions include master payments and associated deductions, **When** user sorts by payee, **Then** system groups related transactions while maintaining master-deduction relationships
> 3. **Given** financial adjustments are made to a case, **When** user refreshes transaction view, **Then** system reflects updated amounts and withholding calculations without manual intervention
> 4. **Given** user requires audit trail, **When** sorting transactions chronologically, **Then** system preserves complete transaction history with timestamps and adjustment reasons
> 5. **Given** incomplete payment processing, **When** user views financial data, **Then** system distinguishes pending, completed, and failed transactions with appropriate status indicators


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=583842870"
> ]

---

#### Feature: As a Claims Adjuster, I want to manage tax withholdings (Federal and State) and YTD earnings for disability claims, so that accurate taxes are withheld from payments
- **Role**: Claim Adjuster
- **Action**: manage tax withholdings (Federal and State) and Year-to-Date earnings at the event case level for disability claims
- **Value**: accurate tax compliance is maintained, claimants receive properly adjusted benefit payments, and the carrier meets regulatory reporting requirements

**Description:**

> As a **Claim Adjuster**,
> I want to **manage tax withholdings (Federal and State) and Year-to-Date earnings at the event case level for disability claims**,
> So that **accurate tax compliance is maintained, claimants receive properly adjusted benefit payments, and the carrier meets regulatory reporting requirements**


**Key Capabilities:**

> 1. Upon case submission with absence claim event, user is able to access tax management capabilities through the case-level taxes interface.
> 2. System automatically calculates and withholds federal taxes from disability payments per predefined business rules.
> 3. User is able to manually add state and FICA tax withholdings when applicable, linking them to specific disability claims.
> 4. User is able to record and maintain Year-to-Date earnings data at the case level for tax calculation accuracy.
> 5. System prevents tax withholding configuration for life and supplemental benefit claims per business rules.
> 6. When tax adjustments are saved, system updates case financial data and generates compliance audit messages for downstream reporting.


**Acceptance Criteria:**

> 1. **Given** a submitted case with disability claims, **When** the adjuster accesses the case overview, **Then** the system displays tax management capabilities including federal, state, and YTD earnings sections.
> 2. **Given** a disability payment is created, **When** the system processes the payment, **Then** federal taxes are automatically withheld based on configured business rules.
> 3. **Given** state or FICA taxes are required, **When** the adjuster manually adds tax withholdings, **Then** the system links them to existing disability claims and applies them to future payments.
> 4. **Given** tax withholdings are configured, **When** the adjuster attempts to apply them to life or supplemental claims, **Then** the system prevents the action per business restrictions.
> 5. **Given** YTD earnings data is entered, **When** the adjuster saves the information, **Then** the system stores it at the case level for tax calculation purposes.
> 6. **Given** any tax adjustment is modified, **When** the change is committed, **Then** the system generates audit messages and recalculates affected payment schedules.


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=583842870"
> ]

---

#### Feature: As a Claims Adjuster, I want to manage deductions (Child Support, Wage Garnishment, and other types) for applicable claim types, so that benefits can be diverted to third parties as required
- **Role**: Claim Adjuster
- **Action**: configure and apply mandatory benefit deductions to divert payments to authorized third parties
- **Value**: claim payments comply with legal obligations and benefit withholding requirements are automatically enforced

**Description:**

> As a Claim Adjuster,
> I want to configure and apply mandatory benefit deductions to divert payments to authorized third parties,
> So that claim payments comply with legal obligations and benefit withholding requirements are automatically enforced


**Key Capabilities:**

> 1. Upon case submission with eligible claims, adjuster establishes deduction configurations linking third-party obligations to specific claims
>     1.1 When disability claims exist, system permits child support and wage garnishment deductions
>     1.2 System restricts deduction types based on claim category and benefit structure
> 2. Adjuster defines deduction parameters including calculation method, effective periods, and payee details
> 3. During payment processing, system automatically calculates deduction amounts and generates separate third-party payments
> 4. System maintains deduction payment relationships and provides visibility into withheld amounts across benefit payment lifecycle


**Acceptance Criteria:**

> 1. **Given** a submitted case with disability claims, **When** adjuster configures child support or wage garnishment deduction, **Then** system accepts percentage-based or fixed deduction specifications
> 2. **Given** deduction is bound to claim, **When** benefit payment is generated, **Then** system automatically creates corresponding third-party deduction payment linked to master payment
> 3. **Given** claim type is CI/HI/TL, **When** adjuster attempts non-child support/wage garnishment deduction, **Then** system prevents configuration and displays restriction guidance
> 4. **Given** no claims exist, **When** adjuster attempts deduction creation, **Then** system prevents action until qualifying claim is established


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=583842870"
> ]

---

#### Feature: As a Claims Adjuster, I want to view a tax summary showing all withheld taxes (FICA, State, and Federal), so that I can verify tax compliance
- **Role**: Claim Adjuster
- **Action**: review a consolidated tax summary displaying all withheld taxes across FICA, State, and Federal categories for the event case
- **Value**: I can verify tax compliance, ensure accurate withholding calculations, and maintain regulatory adherence before finalizing payments

**Description:**

> As a **Claim Adjuster**,
> I want to **review a consolidated tax summary displaying all withheld taxes across FICA, State, and Federal categories for the event case**,
> So that **I can verify tax compliance, ensure accurate withholding calculations, and maintain regulatory adherence before finalizing payments**


**Key Capabilities:**

> 1. Access the event case overview and navigate to tax management workspace upon case submission and claim creation
> 2. Retrieve consolidated tax summary reflecting all payment-level withholdings across linked disability claims
>     2.1 System aggregates Federal tax withholdings applied automatically through predefined rules
>     2.2 System includes manually added State and FICA tax withholdings
> 3. Review tax summary displaying cumulative withholding amounts categorized by tax type (Federal, State, FICA)
> 4. Cross-reference tax withholding data against claim payment schedules and year-to-date earnings
> 5. Identify discrepancies or missing tax entries requiring correction before payment generation
> 6. When discrepancies exist, initiate corrective actions through tax withholding management processes


**Acceptance Criteria:**

> 1. **Given** an event case with submitted disability claims and associated payments, **When** the adjuster accesses the tax summary, **Then** the system displays aggregated Federal, State, and FICA withholdings for all linked claims
> 2. **Given** Federal taxes applied automatically, **When** the summary is generated, **Then** rule-based Federal withholdings appear without manual entry
> 3. **Given** State or FICA taxes added manually, **When** the summary refreshes, **Then** manually entered withholdings are included in the consolidated view
> 4. **Given** no tax withholdings exist for a claim, **When** the adjuster reviews the summary, **Then** the system displays zero values without blocking access
> 5. **Given** multiple claims under one event case, **When** the summary is displayed, **Then** withholdings are aggregated across all applicable disability claims
> 6. **Given** the adjuster lacks update privileges, **When** accessing the summary, **Then** the system provides read-only visibility to tax data


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=583842870"
> ]

---

#### Feature: As a Claims Adjuster, I want to calculate and view case balance comparing actual payments against scheduled payments, so that I can identify and manage overpayments and underpayments
- **Role**: Claim Adjuster
- **Action**: calculate, monitor, and resolve payment discrepancies by comparing actual disbursements against scheduled obligations at the event case level
- **Value**: I can identify overpayments and underpayments per payee, maintain financial accuracy, execute corrective actions, and ensure regulatory compliance through auditable balance reconciliation

**Description:**

> As a **Claim Adjuster**,
> I want to **calculate, monitor, and resolve payment discrepancies by comparing actual disbursements against scheduled obligations at the event case level**,
> So that **I can identify overpayments and underpayments per payee, maintain financial accuracy, execute corrective actions, and ensure regulatory compliance through auditable balance reconciliation**


**Key Capabilities:**

> 1. System automatically recalculates balance when payment-impacting data changes, comparing actual payments against scheduled obligations per payee
> 2. User reviews balance results showing what was paid, what should have been paid, and discrepancies across payment allocations
> 3. Upon overpayment detection, user executes recovery, withholding, or waiver actions to reconcile excess disbursements
>     3.1 Recovery records incoming repayment from payee
>     3.2 Withholding reduces future scheduled payments
>     3.3 Waiver forgives uncollectable amounts
> 4. Upon underpayment detection, user initiates corrective payment to fulfill outstanding obligations
> 5. When external balance adjustments exist, user manually enters external balance entries for comprehensive reconciliation
> 6. System persists balance results, generates audit trails, and updates accumulator limits reflecting all reconciliation activities


**Acceptance Criteria:**

> 1. **Given** payment data exists, **When** calculation-impacting data changes, **Then** system automatically recalculates balance without manual intervention
> 2. **Given** balance calculation completes, **When** user reviews results, **Then** system displays actual versus scheduled payments with discrepancies per payee and allocation
> 3. **Given** overpayment exists, **When** user executes recovery/withholding/waiver action, **Then** system recalculates balance incorporating adjustment and maintains audit trail
> 4. **Given** underpayment exists, **When** user initiates corrective payment, **Then** system disburses funds and updates balance reflecting fulfillment
> 5. **Given** multiple payees in event case, **When** balances are calculated, **Then** system manages each payee independently allowing different balance states
> 6. **Given** balance action completes, **When** system persists results, **Then** change log captures timestamp, action type, amounts, and accumulator impacts


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=596026305"
> ]

---

#### Feature: As a Claims Adjuster, I want to manage overpayments through recovery, waiver, or withholding from future payments, so that I can resolve overpayment situations appropriately
- **Role**: Claim Adjuster
- **Action**: manage overpayments through recovery, waiver, or withholding mechanisms to reconcile payment discrepancies
- **Value**: I can resolve overpayment situations appropriately, maintain financial accuracy, and ensure proper recovery or adjustment of excess payments

**Description:**

> As a **Claim Adjuster**,
> I want to **manage overpayments through recovery, waiver, or withholding mechanisms to reconcile payment discrepancies**,
> So that **I can resolve overpayment situations appropriately, maintain financial accuracy, and ensure proper recovery or adjustment of excess payments**


**Key Capabilities:**

> 1. System automatically detects overpayment situations by comparing actual payments against scheduled amounts per payee within event case
> 2. User evaluates overpayment context and selects appropriate resolution strategy based on business requirements
> 3. User initiates recovery by recording incoming payment received from payee to offset overpayment balance
>     3.1 Upon recovery entry, system adjusts balance and maintains audit trail
> 4. User applies overpayment withholding by defining amount or percentage to deduct from future scheduled payments
> 5. User executes waiver decision to reduce overpayment without recovery action when business circumstances warrant forgiveness
> 6. System recalculates event case balance incorporating all adjustment actions and maintains complete financial reconciliation history


**Acceptance Criteria:**

> 1. **Given** overpayment detected, **When** user selects resolution method, **Then** system enables recovery, withholding, or waiver action appropriate to overpayment amount
> 2. **Given** recovery initiated, **When** incoming payment recorded, **Then** system reduces overpayment balance by recovered amount and logs transaction
> 3. **Given** withholding configured, **When** future payment scheduled, **Then** system automatically deducts specified amount or percentage from payment
> 4. **Given** waiver executed, **When** user confirms waiver amount, **Then** system reduces overpayment without creating recovery obligation
> 5. **Given** any adjustment action completed, **When** system recalculates, **Then** updated balance reflects adjustment with complete audit trail maintained
> 6. **Given** multiple payees in event case, **When** overpayment managed, **Then** system isolates balance adjustments per affected payee independently


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=596026305"
> ]

---

#### Feature: As a Claims Adjuster, I want to manage underpayments by creating additional payments to payees, so that I can ensure claimants receive correct benefit amounts
- **Role**: Claim Adjuster
- **Action**: manage underpayments by creating additional payments to payees
- **Value**: claimants receive correct benefit amounts and financial obligations are accurately fulfilled

**Description:**

> As a **Claim Adjuster**,
> I want to **manage underpayments by creating additional payments to payees**,
> So that **claimants receive correct benefit amounts and financial obligations are accurately fulfilled**


**Key Capabilities:**

> 1. System triggers balance recalculation when payment-impacting data changes (schedule modifications, payment adjustments, or case updates)
> 2. System calculates payment balance per event case per payee by comparing actual payments against scheduled amounts
> 3. Upon identifying underpayment, adjuster reviews balance details showing what was paid versus what should have been paid
> 4. Adjuster initiates supplemental payment creation to cover the identified shortfall for affected payee
> 5. System processes underpayment payment, updates accumulator limits, and recalculates balance incorporating the adjustment
> 6. System maintains audit trail of balance changes and adjustment activities for regulatory compliance


**Acceptance Criteria:**

> 1. **Given** payment-impacting data changes, **When** balance recalculation triggers, **Then** system accurately calculates underpayment amount per payee within the event case
> 2. **Given** underpayment is identified, **When** adjuster reviews balance information, **Then** system displays payment shortfall with allocation details and affected payees
> 3. **Given** adjuster initiates underpayment resolution, **When** supplemental payment is created, **Then** system generates outgoing payment to correct payee for exact shortfall amount
> 4. **Given** supplemental payment is processed, **When** system recalculates balance, **Then** underpayment is eliminated and balance reflects zero discrepancy
> 5. **Given** multiple payees under one event case, **When** underpayment exists for one payee, **Then** system manages each payee's balance independently without cross-contamination
> 6. **Given** underpayment resolution completes, **When** audit review occurs, **Then** system provides complete trail of balance calculations, adjustments, and payment activities


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=596026305"
> ]

---

#### Feature: As a Claims Adjuster, I want to add external balance adjustments for overpayments or underpayments from external sources, so that case balance reflects all financial adjustments
- **Role**: Claim Adjuster
- **Action**: record external balance adjustments for overpayments or underpayments originating outside the event case scope
- **Value**: the event case balance accurately reflects all financial obligations, including external transactions, enabling complete financial reconciliation and audit compliance

**Description:**

> As a **Claim Adjuster**,
> I want to **record external balance adjustments for overpayments or underpayments originating outside the event case scope**,
> So that **the event case balance accurately reflects all financial obligations, including external transactions, enabling complete financial reconciliation and audit compliance**.


**Key Capabilities:**

> 1. User retrieves current event case balance calculated from actual payments, payment schedules, and existing adjustments per payee.
> 2. Upon identifying external overpayment or underpayment, user initiates external balance adjustment entry.
> 3. User provides adjustment amount (positive for underpayment, negative for overpayment) and links to external payment source context.
> 4. System validates financial privileges and incorporates external balance into overall event case balance calculation.
> 5. System recalculates consolidated balance across all payees and persists adjustment with audit trail.
> 6. User verifies updated balance reflects external adjustment and reviews balance change log for reconciliation.


**Acceptance Criteria:**

> 1. **Given** a valid event case with existing payments, **When** adjuster submits external balance adjustment, **Then** system incorporates adjustment into overall case balance without affecting payment schedule calculations.
> 2. **Given** external underpayment entered, **When** balance recalculates, **Then** system increases payee balance by adjustment amount and creates balance change log entry.
> 3. **Given** external overpayment entered, **When** balance recalculates, **Then** system decreases payee balance and records adjustment separately from internal recovery actions.
> 4. **Given** insufficient financial privileges, **When** user attempts adjustment, **Then** system prevents submission and notifies user of authorization requirements.
> 5. **Given** multiple payees in event case, **When** external adjustment applied, **Then** system updates only specified payee balance while maintaining separate balances for other payees.
> 6. **Given** accumulator-impacting adjustment, **When** balance finalizes, **Then** system tracks affected accumulator type and updates claimant policy limits accordingly.


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=596026305"
> ]

---

#### Feature: As a Claims Adjuster, I want to view an audit trail of balance recalculations and balancing activities, so that I can explain financial changes over time
- **Role**: Claim Adjuster
- **Action**: access comprehensive audit trails of payment balance recalculations and balancing activities across event cases
- **Value**: I can efficiently explain financial changes, reconcile discrepancies, and maintain transparent accountability for payment adjustments over time

**Description:**

> As a **Claim Adjuster**,
> I want to **access comprehensive audit trails of payment balance recalculations and balancing activities across event cases**,
> So that **I can efficiently explain financial changes, reconcile discrepancies, and maintain transparent accountability for payment adjustments over time**


**Key Capabilities:**

> 1. System automatically triggers balance recalculation when payment-affecting data changes, computing actual versus scheduled amounts and producing balance results
> 2. User is able to view comprehensive balance details including payment allocations per payee, differences, and overall balances managed at event case level
> 3. User is able to execute balance management actions: add recovery or waive overpayments, initiate underpayment corrections, or enter external balances
> 4. Upon balance management actions, system recalculates balances incorporating adjustments and updates accumulator limits per claimant and policy
> 5. User is able to review audit trail of recalculations and balancing activities for explaining financial changes over time
> 6. When multiple payees exist, system manages per-payee balances independently with dedicated filtering capabilities


**Acceptance Criteria:**

> 1. **Given** payment data changes occur, **When** recalculation triggers, **Then** system produces new balance calculations and persists change logs without manual intervention
> 2. **Given** balance details are requested, **When** user accesses financial view, **Then** system displays actual payments, scheduled payments, differences, and per-payee balances
> 3. **Given** overpayment exists, **When** user initiates recovery/waiver/withholding, **Then** system processes action and recalculates balance accordingly
> 4. **Given** underpayment identified, **When** user executes payment correction, **Then** system creates outgoing payment and updates balance
> 5. **Given** balance management completed, **When** audit trail accessed, **Then** system displays chronological recalculation history and balancing activities
> 6. **Given** unsupported claim type, **When** balance management attempted, **Then** system prevents processing for non-STD/SMP/CI/HI/Life claims


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=596026305"
> ]

---

#### Feature: As a Claims Adjuster, I want to perform payment actions (Request Issue, Issue, Cancel, Fail, Stop) on individual payments, so that I can manage payment lifecycle and resolve payment issues
- **Role**: Claim Adjuster
- **Action**: Execute payment lifecycle actions (Request Issue, Issue, Cancel, Fail, Stop) and manage payment transactions through their complete financial lifecycle
- **Value**: Payment obligations are fulfilled accurately, payment issues are resolved promptly, and financial integrity is maintained throughout the payment process

**Description:**

> As a Claim Adjuster,
> I want to execute payment lifecycle actions (Request Issue, Issue, Cancel, Fail, Stop) and manage payment transactions through their complete financial lifecycle,
> So that payment obligations are fulfilled accurately, payment issues are resolved promptly, and financial integrity is maintained throughout the payment process


**Key Capabilities:**

> 1. Request payment issuance when payment status reaches Approved, triggering automated dispatch workflow to Payment Hub
>     1.1 Upon successful dispatch, payment transitions to Issue Requested state
>     1.2 If dispatch validation errors occur, payment is canceled and user task is created for resolution
> 2. Issue payment either automatically via system workflow or manually without Payment Hub, updating status to Issued and adjusting accumulator amounts (reducing reserved, increasing used)
> 3. Cancel payment at any lifecycle stage, documenting cancellation reason and preventing further processing
> 4. Fail payment using method-specific actions (Decline for EFT, Void for check), reverting used accumulator amounts back to reserved status
> 5. Request payment stop after Issue Requested state, initiating Payment Hub cancellation process with conditional outcomes
> 6. System automatically handles payment regeneration and reissuance when failed payments (Stopped, Canceled, Voided, Declined) require reprocessing after task resolution


**Acceptance Criteria:**

> 1. **Given** payment status is Approved, **when** Request Issue action is executed, **then** system dispatches to Payment Hub and transitions status to Issue Requested
> 2. **Given** payment status is Issue Requested and dispatch is successful, **when** Issue action is executed, **then** payment moves to Issued and accumulator amounts are adjusted (reserved decreases, used increases)
> 3. **Given** payment exists at any lifecycle stage, **when** Cancel action is executed with reason, **then** payment is canceled and documented
> 4. **Given** EFT payment is issued, **when** Fail: Decline action is executed, **then** payment moves to Failed: Declined and used accumulator reverts to reserved
> 5. **Given** check payment is issued, **when** Fail: Void action is executed, **then** payment moves to Failed: Voided and accumulator amounts reverse
> 6. **Given** payment status is Issue Requested or later, **when** Request Stop is executed and Payment Hub confirms success, **then** payment transitions to Failed: Stop with accumulator reversal


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=596026302"
> ]

---

#### Feature: As a Claims Adjuster, I want to perform bulk payment actions (Suspend, Unsuspend, Cancel, Activate all payments), so that I can efficiently manage entire payment schedules
- **Role**: Claim Adjuster
- **Action**: perform bulk payment actions across entire payment schedules (Suspend, Unsuspend, Cancel, Activate) to efficiently manage payment lifecycles at the benefit case level
- **Value**: I can efficiently control payment generation and issuance for all scheduled payments without manual intervention on individual payments, ensuring proper financial management during claim investigations or policy changes

**Description:**

> As a Claim Adjuster,
> I want to perform bulk payment actions across entire payment schedules (Suspend, Unsuspend, Cancel, Activate) to efficiently manage payment lifecycles at the benefit case level,
> So that I can efficiently control payment generation and issuance for all scheduled payments without manual intervention on individual payments, ensuring proper financial management during claim investigations or policy changes


**Key Capabilities:**

> 1. User initiates bulk action selection for benefit case payment schedule
> 2. System validates payment schedule eligibility and current state for requested bulk operation
> 3. Upon Suspend All Payments: System halts payment schedule and blocks generation of new payments until unsuspended
>     3.1 Existing issued payments remain unaffected
>     3.2 Future payment generation prevented while suspension active
> 4. Upon Unsuspend All Payments: System resumes payment schedule and enables automatic payment generation based on post dates
> 5. Upon Cancel All Payments: System discards all payments including issued payments and triggers overpayment declaration for issued payments
> 6. Upon Activate All Payments: System validates authority levels and activates entire payment series when manual approval required


**Acceptance Criteria:**

> 1. **Given** payment schedule exists with pending payments, **When** user executes Suspend All Payments, **Then** system prevents generation of new payments and maintains suspension until explicitly unsuspended
> 2. **Given** suspended payment schedule, **When** user executes Unsuspend All Payments, **Then** system resumes automatic payment generation according to original schedule
> 3. **Given** payment schedule with issued payments, **When** user executes Cancel All Payments, **Then** system cancels all payments and declares issued payments as overpayments
> 4. **Given** insufficient approval authority, **When** user executes Activate All Payments, **Then** system activates entire payment series with manual approval override
> 5. **Given** bulk action in progress, **When** system encounters validation errors, **Then** system prevents execution and provides actionable error context
> 6. **Given** successful bulk action completion, **When** user views payment schedule, **Then** system reflects updated status for all affected payments


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=596026302"
> ]

---

#### Feature: As a Claims Adjuster, I want to update existing payments by adding, removing, or changing allocations, so that I can adjust payments based on new information
- **Role**: Claim Adjuster
- **Action**: modify existing payment allocations by adding, removing, or changing distribution details
- **Value**: payment amounts accurately reflect updated claim information and ensure proper financial reconciliation

**Description:**

> As a **Claim Adjuster**,
> I want to **modify existing payment allocations by adding, removing, or changing distribution details**,
> So that **payment amounts accurately reflect updated claim information and ensure proper financial reconciliation**


**Key Capabilities:**

> 1. Adjuster initiates payment update process for existing payment in Pending or Approved status
> 2. System retrieves current payment template with existing allocations, payee information, and claim coverage details
> 3. Adjuster modifies allocation data by adding new distributions, removing obsolete allocations, or adjusting amounts and percentages
>     3.1 Upon allocation changes, system recalculates payment schedule and total amounts
>     3.2 System validates allocation changes against coverage limits and accumulator balances
> 4. Adjuster previews updated payment calculations and allocation summaries before persisting changes
> 5. Upon confirmation, system persists updated payment template and regenerates payment schedule reflecting new allocation structure
> 6. System determines balance adjustments by comparing previous version to updated version


**Acceptance Criteria:**

> 1. **Given** a payment in Pending or Approved status, **When** adjuster modifies allocations, **Then** system recalculates payment schedule and displays updated totals
> 2. **Given** allocation changes are submitted, **When** system compares versions, **Then** balance adjustments are identified and financial accumulators updated accordingly
> 3. **Given** an Issued payment is updated, **When** allocations are modified, **Then** system triggers recalculation and generates balancing transactions if needed
> 4. **Given** allocation changes exceed coverage limits, **When** validation occurs, **Then** system prevents submission and notifies adjuster of constraint violations
> 5. **Given** payment update is confirmed, **When** system persists changes, **Then** new payment template version is created maintaining change history
> 6. **Given** allocation modifications are finalized, **When** payment schedule regenerates, **Then** future payment definitions reflect updated distribution structure


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=596026302"
> ]

---

#### Feature: As a Claims Operations Manager, I want deduction payments to be automatically generated for Child Support and Wage Garnishment deductions, so that third-party payments are processed efficiently
- **Role**: Claim Adjuster
- **Action**: automate generation of deduction payments for Child Support and Wage Garnishment obligations when processing claim payments
- **Value**: third-party payment obligations are fulfilled efficiently and compliantly without manual intervention, reducing processing time and errors

**Description:**

> As a **Claim Adjuster**,
> I want to **automate generation of deduction payments for Child Support and Wage Garnishment obligations when processing claim payments**,
> So that **third-party payment obligations are fulfilled efficiently and compliantly without manual intervention, reducing processing time and errors**.


**Key Capabilities:**

> 1. User configures deduction obligations (Child Support or Wage Garnishment) at the event case level linked to eligible claims
>     1.1 Upon configuration, system validates deduction applicability based on claim type and business rules
> 2. User initiates claim payment generation for claims with bound deductions
> 3. System automatically schedules and generates corresponding deduction payments by mapping deduction parameters and calculating amounts
> 4. System establishes payment relationships between master claim payment and associated deduction payments
>     4.1 When generation errors occur, system transitions to failed state for investigation
> 5. System finalizes both master and deduction payments for downstream disbursement processing


**Acceptance Criteria:**

> 1. **Given** a claim has active Child Support or Wage Garnishment deductions, **When** payment is generated, **Then** system creates corresponding deduction payments automatically
> 2. **Given** deduction payments are generated, **When** processing completes, **Then** system establishes trackable relationships between master and deduction payments
> 3. **Given** deduction calculation or generation fails, **When** error occurs, **Then** system transitions to failed state and prevents incomplete payment processing
> 4. **Given** claims lack applicable deduction types, **When** payment is generated, **Then** system processes master payment without creating deduction payments
> 5. **Given** multiple deductions exist, **When** payment is generated, **Then** system creates separate deduction payments for each obligation


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=583842870"
> ]

---

#### Feature: As a Claims Adjuster, I want to manage balance per payee separately, so that I can handle situations where one payee is overpaid while another is underpaid within the same case
- **Role**: Claim Adjuster
- **Action**: manage payment balances separately for each payee within an event case
- **Value**: I can independently resolve overpayment and underpayment situations for different payees without cross-contamination of balances

**Description:**

> As a Claim Adjuster,
> I want to manage payment balances separately for each payee within an event case,
> So that I can independently resolve overpayment and underpayment situations for different payees without cross-contamination of balances


**Key Capabilities:**

> 1. System automatically recalculates balances when payment-impacting data changes, segregating calculations per payee
> 2. User reviews payee-specific balance details comparing actual payments against scheduled amounts
>     2.1 Upon detecting overpayment: User initiates recovery, applies withholding to future payments, or waives the amount
>     2.2 Upon detecting underpayment: User creates supplemental payment to resolve shortfall
> 3. User records external balance adjustments when overpayment/underpayment originates outside event case scope
> 4. System processes selected balance management action and recalculates affected payee's balance independently
> 5. System maintains separate audit trail per payee documenting all balance adjustments and recalculations


**Acceptance Criteria:**

> 1. **Given** multiple payees exist in one event case, **When** balance calculation triggers, **Then** system produces separate balance results for each payee without cross-allocation
> 2. **Given** one payee is overpaid and another underpaid, **When** user resolves overpayment, **Then** system maintains underpaid payee's negative balance unchanged
> 3. **Given** user selects payee-specific balance action, **When** system processes adjustment, **Then** recalculation affects only that payee's balance
> 4. **Given** payment schedule changes, **When** system recalculates, **Then** each payee's balance reflects their specific payment entitlement variances
> 5. **Given** balance adjustment completes, **When** user accesses audit trail, **Then** system displays payee-segregated history of calculations and actions


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=596026305"
> ]

---

### Epic: Pet Insurance Claim Automation

#### Feature: As a Claims Adjuster, I want to adjust a claim and have the settlement automatically re-adjudicated, so that I don't have to manually recalculate benefits and accumulators
- **Role**: Claim Adjuster
- **Action**: adjust a claim and trigger automated settlement re-adjudication
- **Value**: settlement calculations, benefit amounts, and policy accumulators are automatically recalculated without manual intervention, ensuring accuracy and reducing processing time

**Description:**

> As a **Claim Adjuster**,
> I want to **adjust a claim and trigger automated settlement re-adjudication**,
> So that **settlement calculations, benefit amounts, and policy accumulators are automatically recalculated without manual intervention, ensuring accuracy and reducing processing time**.


**Key Capabilities:**

> 1. User completes claim adjustment workflow and submits changes to open claim
> 2. System automatically initiates re-adjudication process upon submission
> 3. System resets loss and settlement statuses to initial states
> 4. System recalculates benefit amounts based on adjusted claim data
> 5. System updates policy accumulators including annual maximums and deductibles
> 6. System executes automatic adjudication and finalizes updated settlement proposal


**Acceptance Criteria:**

> 1. **Given** claim adjustment is submitted, **When** system initiates re-adjudication, **Then** loss and settlement statuses are reset automatically
> 2. **Given** statuses are reset, **When** system recalculates benefits, **Then** benefit amounts reflect adjusted claim data accurately
> 3. **Given** benefits are recalculated, **When** system updates accumulators, **Then** deductible and annual maximum values are correctly adjusted
> 4. **Given** accumulators are updated, **When** automatic adjudication completes, **Then** new settlement proposal is finalized without manual intervention
> 5. **Given** claim is not in Open status, **When** adjustment is attempted, **Then** system prevents re-adjudication process
> 6. **Given** user lacks update privileges, **When** adjustment is submitted, **Then** system blocks re-adjudication workflow


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=818191407"
> ]

---

#### Feature: As a Claims Adjuster, I want the system to reset loss and settlement status when I adjust a claim, so that the claim reflects the most current state
- **Role**: Claim Adjuster
- **Action**: trigger automatic re-adjudication when adjusting a claim to reset loss and settlement status and recalculate benefits
- **Value**: the claim accurately reflects the current state with updated settlement proposals and accumulators without manual recalculation

**Description:**

> As a **Claim Adjuster**,
> I want to **trigger automatic re-adjudication when adjusting a claim to reset loss and settlement status and recalculate benefits**,
> So that **the claim accurately reflects the current state with updated settlement proposals and accumulators without manual recalculation**


**Key Capabilities:**

> 1. User initiates claim adjustment for an open claim with appropriate privileges
> 2. Upon submission, system automatically triggers re-adjudication workflow
> 3. System resets loss and settlement statuses to neutral state
> 4. System recalculates benefit amounts based on adjusted claim data
> 5. System updates annual maximums and deductible accumulators according to business rules
> 6. System executes automatic adjudication and establishes revised settlement proposal


**Acceptance Criteria:**

> 1. **Given** an open claim requiring adjustment, **When** adjuster submits adjustment, **Then** system automatically resets loss and settlement statuses
> 2. **Given** statuses are reset, **When** re-adjudication executes, **Then** system recalculates benefit amounts based on current claim data
> 3. **Given** benefits are recalculated, **When** accumulator rules apply, **Then** system updates annual maximums and deductibles accurately
> 4. **Given** re-adjudication completes, **When** process finishes, **Then** system generates updated settlement proposal
> 5. **Given** user lacks required privileges, **When** adjustment is attempted, **Then** system prevents claim modification
> 6. **Given** claim status is not open, **When** adjustment is attempted, **Then** system blocks re-adjudication workflow


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=818191407"
> ]

---

#### Feature: As a Claims Adjuster, I want the system to recalculate benefit amounts and update accumulators automatically after claim adjustment, so that policy limits and deductibles are accurately tracked
- **Role**: Claim Adjuster
- **Action**: automatically trigger settlement re-adjudication and recalculate benefit amounts with updated accumulators when adjusting a claim
- **Value**: policy limits, deductibles, and settlement proposals remain accurate without manual intervention, reducing processing time and calculation errors

**Description:**

> As a **Claim Adjuster**,
> I want to **automatically trigger settlement re-adjudication and recalculate benefit amounts with updated accumulators when adjusting a claim**,
> So that **policy limits, deductibles, and settlement proposals remain accurate without manual intervention, reducing processing time and calculation errors**


**Key Capabilities:**

> 1. Upon claim adjustment submission, system automatically resets loss and settlement statuses to enable recalculation
> 2. System recalculates benefit amounts based on adjusted claim information
> 3. System updates annual maximum and deductible accumulators according to business rules
> 4. System executes automatic settlement adjudication workflow
> 5. System establishes final settlement proposal reflecting adjusted calculations
> 6. User is able to proceed with settlement approval based on accurate recalculated amounts


**Acceptance Criteria:**

> 1. **Given** an open claim with adjustment privilege, **When** adjuster submits claim adjustment, **Then** system automatically triggers re-adjudication without manual intervention
> 2. **Given** re-adjudication initiated, **When** system processes adjustment, **Then** loss and settlement statuses are reset and benefit amounts recalculated
> 3. **Given** benefit recalculation completed, **When** accumulators are updated, **Then** annual maximum and deductible reflect accurate adjusted values
> 4. **Given** accumulators updated, **When** automatic adjudication executes, **Then** settlement proposal is established with correct financial data
> 5. **Given** incomplete or invalid adjustment data, **When** submission attempted, **Then** system prevents re-adjudication until data integrity is restored
> 6. **Given** re-adjudication completed, **When** process finalized, **Then** settlement status reflects successful adjudication and is ready for approval


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=818191407"
> ]

---

#### Feature: As a Claims Adjuster, I want the system to automatically generate and set a settlement proposal after re-adjudication, so that the claim is ready for settlement without manual intervention
- **Role**: Claim Adjuster
- **Action**: trigger automated re-adjudication and settlement proposal generation after claim adjustment
- **Value**: the claim reaches settlement-ready status without manual intervention, reducing processing time and ensuring calculation accuracy

**Description:**

> As a **Claim Adjuster**,
> I want to **trigger automated re-adjudication and settlement proposal generation after claim adjustment**,
> So that **the claim reaches settlement-ready status without manual intervention, reducing processing time and ensuring calculation accuracy**


**Key Capabilities:**

> 1. Upon submitting claim adjustment, system initiates re-adjudication workflow
> 2. System resets loss and settlement statuses to enable fresh adjudication
> 3. System recalculates benefit amounts based on adjusted claim details
> 4. System updates annual maximum and deductible accumulators per policy rules
> 5. System executes automatic adjudication logic to determine settlement eligibility
> 6. System generates and sets settlement proposal ready for approval or payment processing


**Acceptance Criteria:**

> 1. **Given** a claim adjustment is submitted, **When** re-adjudication triggers, **Then** system resets statuses and recalculates benefits without manual input
> 2. **Given** benefit recalculation completes, **When** accumulator rules apply, **Then** system updates annual limits and deductibles accurately
> 3. **Given** automatic adjudication executes, **When** all validations pass, **Then** system generates settlement proposal marked settlement-ready
> 4. **Given** re-adjudication fails validation, **When** errors occur, **Then** system prevents settlement generation and logs exception for adjuster review
> 5. **Given** settlement proposal is set, **When** adjuster views claim, **Then** settlement details reflect recalculated amounts and updated accumulators


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=818191407"
> ]

---

### Epic: Payment Recalculation & Balance Management

#### Feature: As a Claims Adjuster, I want to generate a new recovery payment, so that I can initiate the recovery process for overpaid amounts
- **Role**: Claim Adjuster
- **Action**: generate and manage recovery payments to reclaim overpaid claim amounts through a controlled lifecycle process
- **Value**: the organization can systematically recover overpayments, maintain accurate claim financial balances, and ensure proper audit trails for recovery transactions

**Description:**

> As a **Claim Adjuster**,
> I want to **generate and manage recovery payments to reclaim overpaid claim amounts through a controlled lifecycle process**,
> So that **the organization can systematically recover overpayments, maintain accurate claim financial balances, and ensure proper audit trails for recovery transactions**


**Key Capabilities:**

> 1. User initiates recovery payment generation from initial state with proper authorization privileges
> 2. Upon successful privilege validation, system transitions recovery to active issued state and records transaction in claim system
> 3. User monitors active recovery payments and identifies recoveries requiring termination
>     3.1 When cancellation is needed, user executes cancellation command with appropriate privileges
>     3.2 System validates current state eligibility and transitions recovery to canceled state
> 4. System enforces state-based transition rules preventing unauthorized status changes
> 5. System maintains recovery audit trail capturing all lifecycle transitions and authorization checkpoints


**Acceptance Criteria:**

> 1. **Given** user possesses initiation privileges, **When** recovery generation is executed, **Then** system creates recovery payment and transitions to issued state
> 2. **Given** user lacks required privileges, **When** recovery generation is attempted, **Then** system prevents transaction and maintains start state
> 3. **Given** recovery is in issued state with proper cancellation privileges, **When** cancellation is executed, **Then** system transitions recovery to canceled state and deactivates payment
> 4. **Given** recovery is not in issued state, **When** cancellation is attempted, **Then** system rejects command and preserves current state
> 5. **Given** recovery lifecycle progresses, **When** state transitions occur, **Then** system records complete audit trail with privilege validation results
> 6. **Given** recovery reaches terminal state, **When** lifecycle concludes, **Then** system finalizes transaction and updates claim financial records


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=561867081"
> ]

---

#### Feature: As a Claims Adjuster, I want to cancel a recovery payment, so that I can correct or reverse an incorrectly initiated recovery
- **Role**: Claim Adjuster
- **Action**: cancel an issued recovery payment to reverse or correct an incorrectly initiated recovery transaction
- **Value**: I can maintain accurate recovery balances, prevent erroneous fund collection, and ensure financial integrity of claim settlements

**Description:**

> As a **Claim Adjuster**,
> I want to **cancel an issued recovery payment to reverse or correct an incorrectly initiated recovery transaction**,
> So that **I can maintain accurate recovery balances, prevent erroneous fund collection, and ensure financial integrity of claim settlements**


**Key Capabilities:**

> 1. User identifies active recovery payment requiring cancellation from issued recovery inventory
> 2. User initiates cancellation command against the issued recovery payment
>     2.1 System validates user possesses Cancel Recovery privilege
>     2.2 System verifies recovery payment is in eligible status (Issued)
> 3. System transitions recovery payment from Issued to Canceled status
> 4. System records cancellation transaction with audit trail and timestamp
> 5. System updates claim financial balances to reflect canceled recovery
> 6. User receives confirmation of successful recovery cancellation with terminal status


**Acceptance Criteria:**

> 1. **Given** a recovery payment in Issued status, **When** authorized adjuster initiates cancellation, **Then** system transitions payment to Canceled status and updates balances
> 2. **Given** user lacks Cancel Recovery privilege, **When** cancellation is attempted, **Then** system prevents action and notifies of insufficient authorization
> 3. **Given** recovery payment in non-Issued status, **When** cancellation is requested, **Then** system rejects command as ineligible
> 4. **Given** successful cancellation, **When** transaction completes, **Then** system creates auditable record with timestamp and user identity
> 5. **Given** canceled recovery, **When** status reaches terminal state, **Then** payment cannot transition to other statuses


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=561867081"
> ]

---

#### Feature: As a Claims Adjuster, I want to generate an underpayment with automatic amount allocation, so that I can issue additional payments to claimants for underpaid amounts
- **Role**: Claim Adjuster
- **Action**: generate and process underpayments with automatic amount allocation to issue additional payments for previously underpaid amounts
- **Value**: claimants receive accurate compensation for underpaid amounts through a controlled approval and issuance process that maintains payment integrity and financial balance

**Description:**

> As a **Claim Adjuster**,
> I want to **generate and process underpayments with automatic amount allocation to issue additional payments for previously underpaid amounts**,
> So that **claimants receive accurate compensation for underpaid amounts through a controlled approval and issuance process that maintains payment integrity and financial balance**


**Key Capabilities:**

> 1. User is able to generate underpayment transactions with system automatically canceling prior pending or approved underpayments for the same payee and allocating amounts using predefined business rules
>     1.1 Upon withholding reversal scenarios, system generates specialized underpayment to revert overpayment withholdings
> 2. User is able to submit underpayment for approval where system evaluates authorization rules and transitions to approved state when criteria are satisfied
> 3. User is able to request underpayment issuance triggering integration with payment hub for disbursement
> 4. When issuance to payment hub fails, system reverts underpayment to approved state for retry
> 5. User is able to request payment stop after issuance or cancel underpayment before issuance with documented reasons
> 6. When payment issuance fails at any stage, system marks underpayment as failed with failure reasons captured


**Acceptance Criteria:**

> 1. **Given** underpayment is generated **When** system identifies existing pending or approved underpayments for same payee **Then** system cancels prior underpayments and creates new transaction with allocated amounts in pending state
> 2. **Given** underpayment requires approval **When** user submits for approval **Then** system evaluates authorization rules and transitions to approved state only when criteria are satisfied, otherwise maintains pending state with error notification
> 3. **Given** approved underpayment **When** issuance is requested **Then** system transmits payment details to payment hub and transitions to issued state upon successful confirmation
> 4. **Given** underpayment in issued state **When** stop request is initiated **Then** system sends cancellation request to bank and transitions to stop requested state
> 5. **Given** underpayment in pending, approved, or issue requested states **When** cancellation is executed **Then** system records cancellation reasons, completes related tasks, and transitions to canceled state
> 6. **Given** payment issuance failure occurs **When** system receives failure notification **Then** underpayment transitions to failed state with failure reasons documented


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=571485075"
> ]

---

#### Feature: As a Claims Adjuster, I want to generate a withholding underpayment to revert overpayment withholdings, so that I can restore amounts that were incorrectly withheld without member approval
- **Role**: Claim Adjuster
- **Action**: generate withholding underpayment transactions to reverse overpayment withholdings that incorrectly reduced issued payments without member approval
- **Value**: restore incorrectly withheld amounts to payees and maintain accurate claim balance records without requiring additional member authorization

**Description:**

> As a **Claim Adjuster**,
> I want to **generate withholding underpayment transactions to reverse overpayment withholdings that incorrectly reduced issued payments without member approval**,
> So that **restore incorrectly withheld amounts to payees and maintain accurate claim balance records without requiring additional member authorization**


**Key Capabilities:**

> 1. System detects overpayment withholdings that reduced issued payments without member approval
> 2. Upon detection, system generates withholding underpayment transaction in Pending state
>     2.1 System cancels existing underpayments for same payee in Approved or Pending state
>     2.2 System applies reverse amount allocation rules and generates unique transaction number
> 3. System evaluates approval rules and updates state to Approved when criteria met
> 4. Upon approval, adjuster requests underpayment issuance, transitioning state to Issue Requested
> 5. System issues underpayment to Payment Hub and confirms successful transmission to payment processor
> 6. If underpayment cannot be issued, adjuster can cancel transaction with documented reason


**Acceptance Criteria:**

> 1. **Given** overpayment withholding occurred without member approval, **When** adjuster initiates reversal, **Then** system generates withholding underpayment in Pending state with reverse allocation applied
> 2. **Given** new underpayment is generated, **When** existing underpayments for same payee exist in Approved or Pending state, **Then** system cancels those prior transactions
> 3. **Given** underpayment is in Pending state, **When** approval rules evaluate successfully, **Then** system transitions underpayment to Approved state
> 4. **Given** underpayment is Approved, **When** issuance is requested, **Then** system transmits payment details to Payment Hub and updates state to Issued upon confirmation
> 5. **Given** underpayment requires cancellation, **When** adjuster provides cancellation reason, **Then** system updates state to Canceled and completes related tasks
> 6. **Given** issuance fails, **When** Payment Hub cannot process, **Then** system reverts state to Approved for retry


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=571485075"
> ]

---

#### Feature: As a Claims Examiner, I want to approve underpayments based on approval rules, so that I can authorize underpayments for issuance
- **Role**: Claim Adjuster
- **Action**: approve underpayments based on approval rules
- **Value**: I can authorize underpayments for issuance and ensure proper financial reconciliation

**Description:**

> As a **Claim Adjuster**,
> I want to **approve underpayments based on approval rules**,
> So that **I can authorize underpayments for issuance and ensure proper financial reconciliation**


**Key Capabilities:**

> 1. System generates underpayment transaction for specific payee, cancels conflicting pending/approved underpayments, allocates amounts per business rules, and assigns unique transaction number
> 2. User is able to approve underpayment by executing approval rules; upon successful rule validation, system transitions underpayment to approved state
>     2.1 When approval rules fail validation, system denies approval and maintains pending state with error notification
> 3. System requests issuance of approved underpayment and transitions to issue-requested state
> 4. System confirms successful transmission to Payment Hub and updates state to issued
> 5. User is able to cancel underpayment in pending or approved states with documented reasons
> 6. System handles issuance failures and enables recovery workflows


**Acceptance Criteria:**

> 1. **Given** underpayment requires approval, **When** user executes approval command, **Then** system validates approval rules and transitions to approved state only if rules pass
> 2. **Given** approval rules fail validation, **When** approval is attempted, **Then** system denies approval, maintains pending state, and returns authority error
> 3. **Given** underpayment is approved, **When** issuance is requested, **Then** system prevents further modifications and initiates Payment Hub transmission
> 4. **Given** existing underpayments in pending/approved states exist, **When** new underpayment is generated for same payee, **Then** system cancels prior underpayments automatically
> 5. **Given** underpayment issuance fails, **When** failure is detected, **Then** system returns to approved state enabling retry
> 6. **Given** underpayment is in terminal state (canceled/failed), **When** user attempts modifications, **Then** system prevents all further commands


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=571485075"
> ]

---

#### Feature: As a Claims Adjuster, I want to cancel an underpayment with documented reasons, so that I can prevent incorrect payments and maintain audit trails
- **Role**: Claim Adjuster
- **Action**: cancel underpayments with documented justification to prevent erroneous disbursements
- **Value**: I can maintain financial integrity and preserve regulatory audit trails

**Description:**

> As a **Claim Adjuster**,
> I want to **cancel underpayments with documented justification to prevent erroneous disbursements**,
> So that **I can maintain financial integrity and preserve regulatory audit trails**


**Key Capabilities:**

> 1. User initiates cancellation for underpayments in Pending or Approved states prior to issuance
>     1.1 System validates user possesses cancellation privileges
> 2. User provides cancellation justification documenting business rationale
> 3. System records cancellation reasons in transaction audit messages
> 4. System transitions underpayment to Canceled state preventing further processing
> 5. System completes all related workflow tasks with Cancelled resolution
> 6. Upon cancellation, underpayments are excluded from balance calculations and issuance workflows


**Acceptance Criteria:**

> 1. **Given** underpayment in Pending or Approved state, **When** adjuster submits cancellation with documented reasons, **Then** system transitions to Canceled state and preserves justification in audit messages
> 2. **Given** cancellation is processed, **When** system completes state transition, **Then** all related workflow tasks are automatically resolved as Cancelled
> 3. **Given** canceled underpayment exists, **When** balance calculations execute, **Then** canceled transactions are excluded from financial computations
> 4. **Given** user lacks cancellation privileges, **When** cancellation is attempted, **Then** system prevents action and notifies user of insufficient authorization
> 5. **Given** underpayment in Issued or Stop Requested state, **When** cancellation is attempted, **Then** system prevents cancellation as transaction has progressed beyond eligible states


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=571485075"
> ]

---

#### Feature: As a Claims Operations Manager, I want to request issuance of approved underpayments to the payment hub, so that underpayments are processed and sent for payment
- **Role**: Claim Adjuster
- **Action**: request issuance of approved underpayments to the payment hub
- **Value**: underpayments are processed and sent for payment, ensuring accurate balance correction and timely reimbursement to payees

**Description:**

> As a **Claim Adjuster**,
> I want to **request issuance of approved underpayments to the payment hub**,
> So that **underpayments are processed and sent for payment, ensuring accurate balance correction and timely reimbursement to payees**.


**Key Capabilities:**

> 1. User is able to request issuance for approved underpayments, triggering transition to 'Issue Requested' state.
>     1.1 System validates underpayment is in 'Approved' state before processing.
>     1.2 Upon validation failure, system returns to approved state for retry.
> 2. System transmits underpayment details to Payment Hub with all required payee and transaction information.
> 3. Upon successful transmission, system updates underpayment state to 'Issued' and confirms payment sent to check-writing or bank integration layer.
> 4. When issuance fails, system reverts underpayment to 'Approved' state and logs failure reason for investigation.
> 5. User is able to monitor issuance status throughout payment hub processing lifecycle.


**Acceptance Criteria:**

> 1. **Given** an underpayment in 'Approved' state, **When** user requests issuance, **Then** system transitions state to 'Issue Requested' and initiates payment hub transmission.
> 2. **Given** successful payment hub acknowledgment, **When** transmission completes, **Then** system updates state to 'Issued' and records confirmation.
> 3. **Given** payment hub transmission failure, **When** error occurs, **Then** system reverts to 'Approved' state and logs failure details.
> 4. **Given** underpayment not in 'Approved' state, **When** issuance requested, **Then** system prevents submission and notifies user of invalid state.
> 5. **Given** issued underpayment, **When** payment hub confirms receipt, **Then** system maintains audit trail of all transmission events.


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=571485075"
> ]

---

#### Feature: As a Claims Operations Manager, I want to handle failed underpayment issuance attempts, so that underpayments can be resubmitted or corrected
- **Role**: Claim Manager
- **Action**: recover and reprocess underpayments when issuance to Payment Hub fails
- **Value**: underpayments are successfully issued to payees and financial balances remain accurate

**Description:**

> As a **Claim Manager**,
> I want to **recover and reprocess underpayments when issuance to Payment Hub fails**,
> So that **underpayments are successfully issued to payees and financial balances remain accurate**


**Key Capabilities:**

> 1. System detects failed underpayment issuance to Payment Hub and transitions transaction from 'Issue Requested' state to 'Failed' state with failure reason captured
> 2. User is able to review failed underpayment details including failure reasons and transaction history
> 3. User corrects underlying issues preventing successful transmission (e.g., payee information, payment method configuration)
> 4. User resets failed underpayment from 'Failed' or returns from 'Issue Requested' back to 'Approved' state to enable resubmission
> 5. User reinitiates issuance process to transmit corrected underpayment to Payment Hub
> 6. Upon successful transmission, system confirms issuance and updates state to 'Issued' for financial reconciliation


**Acceptance Criteria:**

> 1. **Given** underpayment issuance fails, **When** Payment Hub returns error, **Then** system transitions underpayment to 'Failed' state and records failure reason
> 2. **Given** underpayment in 'Issue Requested' state cannot transmit, **When** failure detected, **Then** system reverts state to 'Approved' for correction
> 3. **Given** failed underpayment requires correction, **When** user updates transaction details, **Then** system validates changes and enables resubmission
> 4. **Given** corrected underpayment ready for reissuance, **When** user initiates issuance, **Then** system transmits to Payment Hub and monitors confirmation
> 5. **Given** resubmission succeeds, **When** Payment Hub confirms receipt, **Then** system updates state to 'Issued' and reflects in case balance
> 6. **Given** user lacks recovery privileges, **When** attempting failure recovery, **Then** system prevents action with authorization error


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=571485075"
> ]

---

#### Feature: As a Claims Operations Manager, I want to request stopping of issued underpayments, so that I can prevent payments that should not be processed
- **Role**: Claim Manager
- **Action**: request stopping of issued underpayments to prevent erroneous payment processing
- **Value**: I can proactively halt payments that should not be disbursed, protecting organizational funds and preventing downstream reconciliation efforts

**Description:**

> As a **Claim Manager**,
> I want to **request stopping of issued underpayments to prevent erroneous payment processing**,
> So that **I can proactively halt payments that should not be disbursed, protecting organizational funds and preventing downstream reconciliation efforts**


**Key Capabilities:**

> 1. User is able to initiate stop request for underpayments in 'Issued' state
> 2. System transitions underpayment to 'Stop Requested' status and transmits cancellation instruction to Payment Hub
> 3. Payment Hub processes stop request and confirms feasibility based on payment timing
>     3.1 Upon successful stop, system transitions underpayment to 'Canceled' state
>     3.2 When stop fails (payment already processed), system reverts underpayment to 'Issued' state
> 4. System maintains audit trail of stop request reasons and outcomes
> 5. User receives confirmation of stop request processing result


**Acceptance Criteria:**

> 1. **Given** an underpayment in 'Issued' state, **When** user submits stop request, **Then** system updates status to 'Stop Requested' and notifies Payment Hub
> 2. **Given** Payment Hub confirms successful stop, **When** system receives confirmation, **Then** underpayment transitions to 'Canceled' with appropriate reason code
> 3. **Given** Payment Hub cannot stop payment, **When** system receives failure notification, **Then** underpayment reverts to 'Issued' state
> 4. **Given** underpayment not in 'Issued' state, **When** stop request attempted, **Then** system prevents request and returns business rule violation
> 5. **Given** stop request processed, **When** user views underpayment details, **Then** system displays complete stop request history and outcome


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=571485075"
> ]

---

#### Feature: As a Claims Operations Manager, I want to record failed underpayment payments with documented failure reasons, so that I can track payment failures and maintain compliance records
- **Role**: Claim Adjuster
- **Action**: document failed underpayment transactions with failure reasons for compliance tracking
- **Value**: payment failure history is maintained for audit compliance and operational reporting

**Description:**

> As a **Claim Adjuster**,
> I want to **document failed underpayment transactions with failure reasons for compliance tracking**,
> So that **payment failure history is maintained for audit compliance and operational reporting**.


**Key Capabilities:**

> 1. Identify underpayment transaction requiring failure documentation during or after issuance process
> 2. Capture business failure reasons and attach to underpayment transaction messages
> 3. Transition underpayment state to 'Failed' status permanently
> 4. Preserve complete failure context including reasons, timestamps, and transaction details for compliance audit trail
> 5. Enable retrieval of failed payment records for operational reporting and regulatory review


**Acceptance Criteria:**

> 1. **Given** underpayment issuance fails, **When** failure is documented with reasons, **Then** system transitions state to 'Failed' and preserves failure messages
> 2. **Given** failure reasons are provided, **When** recording failure, **Then** system attaches reasons to transaction messages attribute
> 3. **Given** underpayment enters 'Failed' state, **When** queried for compliance, **Then** system returns complete failure history with documented reasons
> 4. **Given** user lacks failure documentation privilege, **When** attempting to record failure, **Then** system prevents action and maintains current state
> 5. **Given** failed underpayment recorded, **When** generating compliance reports, **Then** system includes failure reason details


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=571485075"
> ]

---

#### Feature: As a Claims Adjuster, I want to generate external balance adjustments with automatic amount allocation, so that I can account for external payments or adjustments in the case balance
- **Role**: Claim Adjuster
- **Action**: generate and manage external balance adjustments with automatic amount allocation to account for external payments or corrections
- **Value**: case financial balances accurately reflect all external transactions and adjustments, ensuring proper claim settlement reconciliation

**Description:**

> As a **Claim Adjuster**,
> I want to **generate and manage external balance adjustments with automatic amount allocation to account for external payments or corrections**,
> So that **case financial balances accurately reflect all external transactions and adjustments, ensuring proper claim settlement reconciliation**


**Key Capabilities:**

> 1. User initiates external balance adjustment by providing adjustment amount, payee information, and business reason
> 2. System executes amount allocation rules to automatically distribute adjustment across transaction categories based on payee and amount parameters
> 3. System generates unique external balance identifier and records transaction in Issued state for balance calculation inclusion
> 4. Upon successful generation, external balance is incorporated into case balance calculations
> 5. When correction is needed, user cancels existing external balance to update state to Canceled and exclude from balance calculations
> 6. System maintains state transition history and enforces privilege validation throughout lifecycle


**Acceptance Criteria:**

> 1. **Given** valid amount and payee data, **When** adjuster generates external balance, **Then** system applies allocation rules and creates Issued transaction with unique identifier
> 2. **Given** external balance in Issued state, **When** included in balance calculation, **Then** case balance reflects the adjustment amount
> 3. **Given** incorrect external balance exists, **When** adjuster cancels transaction, **Then** state updates to Canceled and is excluded from balance calculations
> 4. **Given** insufficient privileges, **When** user attempts generation or cancellation, **Then** system prevents action and notifies of authorization requirement
> 5. **Given** external balance lifecycle event, **When** state transition occurs, **Then** system records audit trail with timestamp and reason


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=577780306"
> ]

---

#### Feature: As a Claims Adjuster, I want to cancel external balance transactions, so that I can correct inaccurate external balance entries
- **Role**: Claim Adjuster
- **Action**: cancel issued external balance transactions to correct inaccurate financial entries
- **Value**: maintain accurate claim balance calculations and financial integrity by excluding erroneous external balance records

**Description:**

> As a **Claim Adjuster**,
> I want to **cancel issued external balance transactions to correct inaccurate financial entries**,
> So that **maintain accurate claim balance calculations and financial integrity by excluding erroneous external balance records**


**Key Capabilities:**

> 1. User initiates cancellation process for an existing external balance transaction in 'Issued' state
> 2. System validates user authorization against privilege requirements for external balance cancellation
> 3. System transitions external balance state from 'Issued' to 'Canceled'
>     3.1 Upon successful state change, transaction retains original allocation details and audit history
>     3.2 System excludes canceled balance from active balance calculations
> 4. System recalculates case financial position excluding the canceled transaction amount
> 5. User is able to view canceled transaction with historical context and cancellation metadata
> 6. System maintains complete transaction lifecycle trail for financial audit and reporting purposes


**Acceptance Criteria:**

> 1. **Given** an external balance transaction exists in 'Issued' state, **When** authorized adjuster executes cancellation, **Then** transaction state updates to 'Canceled' and is excluded from balance calculations
> 2. **Given** user lacks cancellation privileges, **When** cancellation is attempted, **Then** system prevents action and notifies user of insufficient authorization
> 3. **Given** external balance is in 'Canceled' state, **When** case balance is calculated, **Then** system excludes canceled transaction from financial totals
> 4. **Given** cancellation completes successfully, **When** transaction history is reviewed, **Then** original allocation details and cancellation metadata are preserved
> 5. **Given** external balance has dependent financial adjustments, **When** canceled, **Then** system handles dependent records appropriately without data integrity violations
> 6. **Given** multiple external balances exist for same payee, **When** one is canceled, **Then** only specified transaction is excluded from calculations


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=577780306",
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=586725677"
> ]

---

#### Feature: As a Claims Operations Manager, I want to initiate self-balance transactions automatically, so that offsetting payments are recorded in the system
- **Role**: Claim Adjuster
- **Action**: automatically generate and manage self-balance transactions to offset payments for payees with calculated balances
- **Value**: accurate financial reconciliation is maintained without manual intervention, ensuring claim payment integrity and reducing operational overhead

**Description:**

> As a **Claim Adjuster**,
> I want to **automatically generate and manage self-balance transactions to offset payments for payees with calculated balances**,
> So that **accurate financial reconciliation is maintained without manual intervention, ensuring claim payment integrity and reducing operational overhead**.


**Key Capabilities:**

> 1. System identifies all payees with calculated balances for the specified origin source and generates corresponding self-balance transactions
> 2. System initiates each self-balance transaction by persisting it to the database, transitioning to 'Issued' state for active inclusion in calculations
> 3. Transaction remains active and participates in all financial calculations while in 'Issued' state
> 4. Upon business need to reverse, user is able to cancel the self-balance transaction
>     4.1 System transitions transaction to 'Canceled' state, permanently excluding it from all calculations
>     4.2 Canceled state is terminal with no further state transitions permitted


**Acceptance Criteria:**

> 1. **Given** payees have calculated balances for an origin source, **When** the generation process executes, **Then** self-balance transactions are created for all qualifying payees
> 2. **Given** a self-balance transaction is generated, **When** initiation completes, **Then** the transaction persists in 'Issued' state and participates in financial calculations
> 3. **Given** a self-balance transaction is in 'Issued' state, **When** cancellation is requested, **Then** the system transitions it to 'Canceled' state and excludes it from all calculations
> 4. **Given** a self-balance transaction is canceled, **When** any subsequent action is attempted, **Then** the system prevents further state changes
> 5. **Given** multiple self-balance transactions exist, **When** calculations execute, **Then** only non-canceled transactions are included in balance computations


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=660064000"
> ]

---

#### Feature: As a Claims Adjuster, I want to cancel self-balance transactions, so that I can exclude incorrect offsetting entries from balance calculations
- **Role**: Claim Adjuster
- **Action**: cancel self-balance transactions to exclude incorrect offsetting entries from balance calculations
- **Value**: I can ensure accurate financial balance calculations by removing erroneous offsetting transactions from the system

**Description:**

> As a **Claim Adjuster**,
> I want to **cancel self-balance transactions to exclude incorrect offsetting entries from balance calculations**,
> So that **I can ensure accurate financial balance calculations by removing erroneous offsetting transactions from the system**


**Key Capabilities:**

> 1. User identifies self-balance transaction requiring cancellation based on calculated balance discrepancies
> 2. User initiates cancellation process for transaction currently in 'Issued' state
> 3. System transitions transaction state from 'Issued' to 'Canceled' as terminal lifecycle state
> 4. System excludes canceled transaction from all balance calculations and financial aggregations
>     4.1 Upon cancellation, system recalculates affected payee balances excluding canceled entries
> 5. System maintains audit trail of state transition for compliance and reconciliation purposes


**Acceptance Criteria:**

> 1. **Given** a self-balance transaction in 'Issued' state, **When** adjuster initiates cancellation, **Then** system transitions transaction to 'Canceled' state
> 2. **Given** transaction is canceled, **When** system performs balance calculations, **Then** canceled transaction is excluded from all financial computations
> 3. **Given** cancellation request for non-issued transaction, **When** adjuster attempts cancellation, **Then** system prevents state transition and notifies adjuster
> 4. **Given** successful cancellation, **When** adjuster reviews transaction history, **Then** system displays complete audit trail including cancellation timestamp and reason
> 5. **Given** canceled transaction exists, **When** system recalculates payee balances, **Then** updated balances reflect exclusion of canceled offsetting entries


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=660064000"
> ]

---

#### Feature: As a Claims Operations Manager, I want to generate self-balance transactions for all payees with calculated balances, so that offsetting amounts are automatically recorded
- **Role**: Claim Adjuster
- **Action**: automatically generate and manage self-balance transactions for all payees with calculated balances from specified origin sources
- **Value**: offsetting amounts are systematically recorded, ensuring accurate financial reconciliation and reducing manual intervention in balance management

**Description:**

> As a **Claim Adjuster**,
> I want to **automatically generate and manage self-balance transactions for all payees with calculated balances from specified origin sources**,
> So that **offsetting amounts are systematically recorded, ensuring accurate financial reconciliation and reducing manual intervention in balance management**.


**Key Capabilities:**

> 1. System identifies all payees with calculated balances from the designated origin source
> 2. System generates self-balance transactions for identified payees
> 3. System persists transactions in 'Issued' state, making them active for calculations and financial processing
> 4. System maintains transactions in 'Issued' state throughout the calculation lifecycle
>     4.1 Upon cancellation requirement, system transitions transaction to 'Canceled' state
>     4.2 Canceled transactions are permanently excluded from all subsequent calculations
> 5. System ensures all state transitions are automatically tracked for audit purposes


**Acceptance Criteria:**

> 1. **Given** payees have calculated balances from an origin source, **When** generation is triggered, **Then** system creates self-balance transactions for all qualifying payees
> 2. **Given** self-balance transactions are created, **When** persisted, **Then** system sets state to 'Issued' and includes in calculations
> 3. **Given** a transaction is in 'Issued' state, **When** cancellation is requested, **Then** system updates state to 'Canceled' and excludes from all calculations
> 4. **Given** transaction state changes occur, **When** processed, **Then** system maintains complete audit trail
> 5. **Given** transactions exist in any state, **When** balance calculations run, **Then** system only includes 'Issued' state transactions


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=660064000"
> ]

---

#### Feature: As a Claims Examiner, I want to generate overpayment waivers with approval authority validation, so that I can waive overpaid amounts with proper authorization
- **Role**: Claim Adjuster
- **Action**: generate overpayment waivers with approval authority validation and proper allocation management
- **Value**: overpaid amounts can be waived with proper authorization control, ensuring financial accuracy and compliance with approval hierarchies

**Description:**

> As a **Claim Adjuster**,
> I want to **generate overpayment waivers with approval authority validation and proper allocation management**,
> So that **overpaid amounts can be waived with proper authorization control, ensuring financial accuracy and compliance with approval hierarchies**


**Key Capabilities:**

> 1. User initiates overpayment waiver process for identified overpaid amounts
>     1.1 System validates user authority against approval rules to determine waiver authorization level
>     1.2 System allocates waiver amount across affected balance items based on payee and amount
> 2. System generates unique waiver transaction identifier for tracking and audit purposes
> 3. System creates waiver transaction in issued state with documented waiver reason
> 4. When waiver requires correction, user is able to cancel the waiver transaction
> 5. System recalculates financial balance based on waiver state transitions


**Acceptance Criteria:**

> 1. **Given** a claim adjuster with sufficient authority, **When** overpayment waiver is initiated, **Then** system validates approval authority and generates waiver in issued state
> 2. **Given** waiver amount and payee are provided, **When** waiver is generated, **Then** system allocates amount across balance items correctly
> 3. **Given** waiver is issued, **When** balance is calculated, **Then** waived amount is included in balance computation
> 4. **Given** a valid waiver exists, **When** cancellation is requested by authorized user, **Then** system updates state to canceled and excludes from balance
> 5. **Given** insufficient approval authority, **When** waiver generation is attempted, **Then** system prevents transaction creation


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=439134268"
> ]

---

#### Feature: As a Claims Adjuster, I want to cancel overpayment waivers, so that I can correct or reverse incorrectly waived amounts
- **Role**: Claim Adjuster
- **Action**: cancel overpayment waivers to reverse incorrectly waived amounts and restore accurate financial balances
- **Value**: financial accuracy is maintained by excluding erroneous waivers from balance calculations and ensuring correct overpayment management

**Description:**

> As a **Claim Adjuster**,
> I want to **cancel overpayment waivers to reverse incorrectly waived amounts and restore accurate financial balances**,
> So that **financial accuracy is maintained by excluding erroneous waivers from balance calculations and ensuring correct overpayment management**


**Key Capabilities:**

> 1. Adjuster initiates overpayment waiver generation by providing waiver reason and amount allocation details
>     1.1 System validates adjuster authority against approval rules
>     1.2 System allocates amounts based on payee and balance rules
> 2. Upon approval, system generates unique waiver number and transitions waiver to 'Issued' state
> 3. Adjuster is able to cancel issued waivers when corrections are needed
> 4. System transitions waiver from 'Issued' to 'Canceled' state upon cancellation
> 5. When canceled, system excludes waiver from balance calculations automatically
> 6. If authority is insufficient, system prevents waiver generation


**Acceptance Criteria:**

> 1. **Given** an issued overpayment waiver, **When** adjuster initiates cancellation with proper privileges, **Then** system transitions waiver to 'Canceled' state
> 2. **Given** a canceled waiver, **When** balance calculation occurs, **Then** system excludes canceled waiver from balance totals
> 3. **Given** waiver generation request, **When** adjuster lacks sufficient authority, **Then** system prevents waiver creation
> 4. **Given** valid waiver details, **When** generation completes successfully, **Then** system assigns unique waiver number and sets 'Issued' state
> 5. **Given** issued waiver, **When** viewed by adjuster, **Then** system displays waiver reason and allocated amounts
> 6. **Given** cancellation attempt without proper privilege, **Then** system prevents cancellation action


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=439134268"
> ]

---

### Epic: Common Claim Processing Tasks & Error Handling

#### Feature: As a Claims Adjuster, I want to review and resolve auto adjudication closure failures, so that claims can be properly closed and processed without manual intervention delays
- **Role**: Claim Adjuster
- **Action**: review and resolve auto adjudication closure failures to enable proper claim closure
- **Value**: claims are efficiently closed without manual intervention delays and adjudication issues are systematically addressed

**Description:**

> As a **Claim Adjuster**,
> I want to **review and resolve auto adjudication closure failures to enable proper claim closure**,
> So that **claims are efficiently closed without manual intervention delays and adjudication issues are systematically addressed**


**Key Capabilities:**

> 1. System detects auto adjudication failure during claim closure process and generates intervention task
> 2. Adjuster accesses assigned closure failure task with failure details and diagnostic information
> 3. Adjuster reviews adjudication issue root cause and claim data discrepancies
>     3.1 Upon data validation errors, corrects claim information to meet adjudication criteria
>     3.2 When business rule conflicts exist, applies manual adjudication override with justification
> 4. Adjuster resubmits claim for automated closure processing
> 5. System confirms successful adjudication and completes claim closure workflow


**Acceptance Criteria:**

> 1. **Given** auto adjudication closure fails, **When** system detects failure, **Then** intervention task is generated with failure diagnostics
> 2. **Given** adjuster reviews failure task, **When** root cause is identified, **Then** corrective actions are available based on failure type
> 3. **Given** claim data is corrected, **When** resubmitted for adjudication, **Then** system processes closure without errors
> 4. **Given** manual override is required, **When** adjuster provides justification, **Then** claim proceeds to closure
> 5. **Given** adjudication succeeds, **When** closure completes, **Then** task is resolved and claim status updated
> 6. **Given** resolution fails validation, **When** resubmitted, **Then** system prevents closure with diagnostic feedback


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=694524280"
> ]

---

#### Feature: As a Claims Adjuster, I want to review and resolve auto adjudication payment generation failures, so that claim payments are generated accurately and on schedule
- **Role**: Claim Adjuster
- **Action**: review and resolve automated payment generation failures
- **Value**: claim payments are processed accurately and disbursed on schedule without delays

**Description:**

> As a **Claim Adjuster**,
> I want to **review and resolve automated payment generation failures**,
> So that **claim payments are processed accurately and disbursed on schedule without delays**


**Key Capabilities:**

> 1. System notifies adjuster when automated payment generation fails during adjudication cycle
> 2. Adjuster reviews failure context including adjudication closure errors, scheduling failures, or validation exceptions
> 3. Adjuster investigates root cause such as policy data discrepancies, payee balance mismatches, or underpayment conditions
>     3.1 Upon policy refresh issues, adjuster verifies payment accuracy against updated policy information
>     3.2 When balance discrepancies exist, adjuster reconciles payment amounts with expected balances
> 4. Adjuster resolves error by correcting data, obtaining required approvals, or manually generating payment
> 5. System processes corrected payment and closes adjudication cycle
> 6. Adjuster confirms payment scheduled and verifies claim status updated appropriately


**Acceptance Criteria:**

> 1. **Given** automated payment generation fails, **When** adjuster accesses failure notification, **Then** system displays error context and adjudication details
> 2. **Given** payment scheduling error occurs, **When** adjuster corrects underlying issue, **Then** system successfully schedules payment without manual reprocessing
> 3. **Given** underpayment requires approval, **When** adjuster obtains authorization, **Then** system processes reduced payment amount and closes adjudication
> 4. **Given** policy data changed, **When** adjuster verifies payment accuracy, **Then** system reconciles payment against refreshed policy information
> 5. **Given** error resolved, **When** payment processes successfully, **Then** system closes adjudication cycle and updates claim status
> 6. **Given** multiple failures exist, **When** adjuster prioritizes by impact, **Then** system supports batch resolution for similar error types


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=694524280"
> ]

---

#### Feature: As a Claims Examiner, I want to review and manage canceled payments, so that I can understand cancellation reasons and take corrective action
- **Role**: Claim Adjuster
- **Action**: review and resolve canceled payments and payment exceptions
- **Value**: ensure payment integrity, identify root causes of cancellations, and take corrective action to maintain accurate claim financials

**Description:**

> As a **Claim Adjuster**,
> I want to **review and resolve canceled payments and payment exceptions**,
> So that **I can ensure payment integrity, identify root causes of cancellations, and take corrective action to maintain accurate claim financials**


**Key Capabilities:**

> 1. User is able to access the queue of canceled payments and payment exceptions requiring review
> 2. Upon reviewing a canceled payment, user is able to identify the cancellation reason and assess impact on claim balances
> 3. User is able to investigate failed payment generation or scheduling processes and determine root cause
> 4. When balance discrepancies are detected, user is able to reconcile payee accounts and validate payment schedules
> 5. User is able to take corrective action including regenerating payments, adjusting claim financials, or escalating for approval
> 6. User is able to update payment status and document resolution actions for audit trail


**Acceptance Criteria:**

> 1. **Given** a payment is canceled, **when** user accesses the review queue, **then** system displays cancellation reason and related claim context
> 2. **Given** payment generation fails, **when** user investigates the exception, **then** system provides error details and allows manual regeneration
> 3. **Given** balance discrepancies exist, **when** user reconciles accounts, **then** system prevents further processing until discrepancies are resolved
> 4. **Given** corrective action is taken, **when** user documents resolution, **then** system updates payment status and creates audit trail
> 5. **Given** payment scheduling fails, **when** user reviews the exception, **then** system allows manual rescheduling with validation
> 6. **Given** underpayment requires approval, **when** threshold is exceeded, **then** system routes to approval workflow before processing


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=694524280"
> ]

---

#### Feature: As a Claims Adjuster, I want to review and resolve payment scheduling process failures, so that payments are scheduled correctly and delivered on time
- **Role**: Claim Adjuster
- **Action**: review and resolve payment scheduling process failures
- **Value**: payments are scheduled correctly and delivered on time to claimants

**Description:**

> As a **Claim Adjuster**,
> I want to **review and resolve payment scheduling process failures**,
> So that **payments are scheduled correctly and delivered on time to claimants**


**Key Capabilities:**

> 1. System detects payment scheduling process failures and generates resolution task
> 2. Adjuster accesses failed scheduling task with error context and transaction details
> 3. Adjuster investigates root cause of scheduling failure
>     3.1 Upon policy data issues, validates and refreshes policy information
>     3.2 Upon payee account discrepancies, verifies payee balance and account status
> 4. Adjuster resolves identified issues and corrects scheduling parameters
> 5. Adjuster resubmits payment for scheduling execution
> 6. System confirms successful scheduling and proceeds to payment execution phase


**Acceptance Criteria:**

> 1. **Given** a payment scheduling failure occurs, **When** the system detects the error, **Then** a resolution task is automatically generated for the adjuster
> 2. **Given** an adjuster accesses the task, **When** reviewing failure details, **Then** system provides error context and transaction information
> 3. **Given** root cause is identified, **When** adjuster resolves the issue, **Then** system enables payment resubmission
> 4. **Given** corrective actions are applied, **When** payment is resubmitted, **Then** system validates resolution and schedules payment successfully
> 5. **Given** policy or payee data issues exist, **When** adjuster initiates validation, **Then** system prevents scheduling until data is corrected
> 6. **Given** payment is successfully rescheduled, **When** execution proceeds, **Then** system tracks payment through completion


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=694524280"
> ]

---

#### Feature: As a Claims Examiner, I want to review payment schedules and payee balances, so that I can verify payment accuracy and ensure proper fund allocation
- **Role**: Claim Adjuster
- **Action**: review payment schedules and validate payee balances to ensure payment accuracy before disbursement
- **Value**: I can verify proper fund allocation, detect discrepancies, and prevent erroneous payments before execution

**Description:**

> As a **Claim Adjuster**, I want to **review payment schedules and validate payee balances to ensure payment accuracy before disbursement**, so that **I can verify proper fund allocation, detect discrepancies, and prevent erroneous payments before execution**.


**Key Capabilities:**

> 1. User accesses payment schedule review tasks generated by the system for manual verification
> 2. User validates payment amounts, timing, and payee information against claim entitlements
> 3. User reviews payee balance information to confirm accuracy and proper fund allocation
> 4. Upon detecting underpayment, user routes to approval workflow for authorized review
> 5. When discrepancies are identified, user investigates and resolves payment exceptions
> 6. User approves or rejects payment schedules based on validation outcomes


**Acceptance Criteria:**

> 1. **Given** a payment schedule requires review, **when** the user accesses the task, **then** all payment details and payee balances are displayed for validation
> 2. **Given** payment information is validated, **when** the user approves the schedule, **then** payment processing continues to execution
> 3. **Given** an underpayment is detected, **when** the user submits for approval, **then** the system routes to authorized personnel
> 4. **Given** payment discrepancies exist, **when** the user rejects the schedule, **then** the system generates an exception for resolution
> 5. **Given** validation is incomplete, **when** the user attempts to proceed, **then** the system prevents submission
> 6. **Given** payment review fails, **when** an exception occurs, **then** the system creates a manual review task


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=694524280"
> ]

---

#### Feature: As a Claims Adjuster, I want to review and resolve failed payments, so that payment issues are identified and corrected promptly
- **Role**: Claim Adjuster
- **Action**: review and resolve failed payments through systematic investigation of payment failures, scheduling errors, and adjudication issues
- **Value**: payment processing issues are identified and corrected promptly, ensuring timely claim settlements and maintaining financial accuracy

**Description:**

> As a **Claim Adjuster**,
> I want to **review and resolve failed payments through systematic investigation of payment failures, scheduling errors, and adjudication issues**,
> So that **payment processing issues are identified and corrected promptly, ensuring timely claim settlements and maintaining financial accuracy**


**Key Capabilities:**

> 1. System detects payment execution failures and generates review tasks for adjuster action
> 2. User investigates failed payment root causes including adjudication closure errors, payment generation failures, and scheduling issues
> 3. User resolves payment scheduling process failures by diagnosing and correcting timing or configuration errors
>     3.1 When underpayment scenarios detected, user approves or rejects payment before processing
> 4. User reviews canceled payments to understand cancellation reasons and determines corrective actions
> 5. User validates policy refresh impacts on active claims and recalculates affected payment amounts
> 6. User reconciles payee balance discrepancies and corrects payment schedules before finalizing transactions


**Acceptance Criteria:**

> 1. **Given** payment execution fails, **When** system detects failure, **Then** review task is generated for adjuster investigation
> 2. **Given** adjudication closure fails, **When** user receives task, **Then** user completes manual case closure after resolving issues
> 3. **Given** underpayment scenario exists, **When** user reviews task, **Then** payment processing blocked until explicit approval provided
> 4. **Given** payment is canceled, **When** user investigates, **Then** cancellation reason is documented and next steps determined
> 5. **Given** policy data refreshed, **When** impact detected, **Then** user validates affected claims and recalculates payments
> 6. **Given** payee balance discrepancy exists, **When** user reconciles, **Then** system prevents further payments until resolved


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=694524280"
> ]

---

#### Feature: As a Claims Examiner, I want to approve underpayment cases, so that underpaid claims are properly authorized and resolved
- **Role**: Claim Adjuster
- **Action**: review and approve underpayment cases when calculated payment amounts fall below expected thresholds
- **Value**: claims with payment discrepancies are properly authorized, ensuring accurate financial resolution and regulatory compliance

**Description:**

> As a **Claim Adjuster**,
> I want to **review and approve underpayment cases when calculated payment amounts fall below expected thresholds**,
> So that **claims with payment discrepancies are properly authorized, ensuring accurate financial resolution and regulatory compliance**


**Key Capabilities:**

> 1. System detects underpayment condition when calculated payment falls below expected amount
> 2. User receives system-generated task for underpayment approval review
> 3. User evaluates payment discrepancy against claim details and business rules
> 4. User approves or rejects underpayment based on investigation findings
>     4.1 Upon approval, system authorizes payment processing to continue
>     4.2 Upon rejection, system routes claim for payment recalculation or further investigation
> 5. System tracks approval decision for audit and compliance reporting
> 6. Upon cancellation of underpayment, system flags status and creates review task


**Acceptance Criteria:**

> 1. **Given** underpayment is detected, **When** calculated payment is below threshold, **Then** system generates approval task and routes to authorized adjuster
> 2. **Given** approval task is assigned, **When** adjuster reviews case, **Then** system presents payment discrepancy details and claim context
> 3. **Given** adjuster approves underpayment, **When** approval is submitted, **Then** system authorizes payment to proceed and records approval decision
> 4. **Given** adjuster rejects underpayment, **When** rejection is submitted, **Then** system prevents payment and routes for corrective action
> 5. **Given** underpayment is canceled, **When** cancellation occurs, **Then** system creates review task and tracks cancellation status
> 6. **Given** approval decision is made, **When** process completes, **Then** system maintains audit trail of decision and rationale


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=694524280"
> ]

---

#### Feature: As a Claims Operations Manager, I want to perform policy refresh reviews, so that claim processing remains compliant with current policy requirements
- **Role**: Claim Adjuster
- **Action**: initiate and complete policy refresh reviews to validate current policy data against active claims
- **Value**: claim processing remains compliant with current policy terms and prevents payment errors due to outdated policy information

**Description:**

> As a **Claim Adjuster**,
> I want to **initiate and complete policy refresh reviews to validate current policy data against active claims**,
> So that **claim processing remains compliant with current policy terms and prevents payment errors due to outdated policy information**


**Key Capabilities:**

> 1. System triggers policy data validation review when policy refresh is required during claim adjudication workflow
> 2. User is able to review policy data discrepancies and compare current versus refreshed policy terms
> 3. Upon validation completion, system updates claim records with refreshed policy information
> 4. If policy changes impact coverage or limits, system flags claim for adjudication reassessment
> 5. System prevents payment processing until policy refresh review is completed and approved
> 6. User is able to document policy refresh findings and resolution for audit compliance


**Acceptance Criteria:**

> 1. **Given** a claim requires payment adjudication, **When** policy refresh is triggered, **Then** system suspends payment processing until policy validation is completed
> 2. **Given** policy data is refreshed, **When** coverage terms have changed, **Then** system routes claim for reassessment before proceeding
> 3. **Given** policy refresh review is completed, **When** validation is approved, **Then** system resumes adjudication workflow with updated policy data
> 4. **Given** policy data is unavailable or invalid, **When** refresh fails, **Then** system prevents claim progression and notifies user for manual intervention
> 5. **Given** policy refresh is documented, **When** audit review occurs, **Then** system provides complete validation history and resolution records


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=694524280"
> ]

---

### Epic: Underpayment & Approval Management

#### Feature: As a Claims Adjuster, I want to review and approve underpayment cases, so that I can ensure accurate claim settlements and maintain compliance with approval requirements.
- **Role**: Claim Adjuster
- **Action**: review and approve underpayment cases to ensure accurate settlements
- **Value**: I can maintain compliance with approval requirements and prevent financial loss from incorrect claim payments

**Description:**

> As a **Claim Adjuster**,
> I want to **review and approve underpayment cases to ensure accurate settlements**,
> So that **I can maintain compliance with approval requirements and prevent financial loss from incorrect claim payments**


**Key Capabilities:**

> 1. User is able to identify claims flagged as underpayment cases requiring approval
> 2. User is able to review case details including payment history, coverage analysis, and underpayment justification
> 3. User is able to evaluate the underpayment against approval thresholds and policy guidelines
> 4. User is able to approve or reject the underpayment decision with documented rationale
>     4.1 Upon rejection, user is able to specify required corrective actions
> 5. User is able to escalate cases exceeding authority limits to appropriate supervisory level
> 6. System records approval decision and progresses claim to closure workflow


**Acceptance Criteria:**

> 1. **Given** an underpayment case requires review, **When** the adjuster accesses the case, **Then** system presents complete payment analysis and approval requirements
> 2. **Given** approval authority is verified, **When** adjuster approves underpayment, **Then** system progresses claim to closure stage
> 3. **Given** underpayment exceeds authority threshold, **When** adjuster attempts approval, **Then** system enforces escalation to supervisor
> 4. **Given** rejection is submitted, **When** system processes decision, **Then** claim returns to adjudication with documented corrective actions
> 5. **Given** approval decision is recorded, **When** closure proceeds, **Then** system maintains audit trail of approval workflow
> 6. **Given** incomplete justification exists, **When** approval is attempted, **Then** system prevents submission until documentation requirements are met


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=589990738"
> ]

---

#### Feature: As a Claims Operations Manager, I want to track and monitor underpayment cases requiring approval, so that I can ensure timely processing and maintain operational efficiency.
- **Role**: Claim Manager
- **Action**: track and monitor underpayment cases requiring approval through their lifecycle
- **Value**: I can ensure timely processing, maintain operational efficiency, and prevent payment delays

**Description:**

> As a **Claim Manager**,
> I want to **track and monitor underpayment cases requiring approval through their lifecycle**,
> So that **I can ensure timely processing, maintain operational efficiency, and prevent payment delays**


**Key Capabilities:**

> 1. User is able to identify cases flagged as underpayment requiring approval escalation
> 2. User is able to monitor approval status and pending duration across all underpayment cases
> 3. User is able to track approval workflow progression from submission through final authorization
> 4. Upon approval threshold breach, user is able to receive alerts for cases requiring intervention
> 5. User is able to review historical approval patterns to optimize processing workflows
> 6. User is able to generate operational reports on approval cycle times and case volumes


**Acceptance Criteria:**

> 1. **Given** an underpayment case requires approval, **When** submitted to the approval queue, **Then** system records timestamp and assigns tracking status
> 2. **Given** multiple cases pending approval, **When** user accesses monitoring dashboard, **Then** system displays all cases with current approval stage and aging metrics
> 3. **Given** approval exceeds defined timeframe, **When** threshold is breached, **Then** system generates alerts for management intervention
> 4. **Given** approval decision is rendered, **When** case is approved or rejected, **Then** system updates case status and enables subsequent processing
> 5. **Given** operational reporting needs, **When** user requests metrics, **Then** system provides approval cycle analytics and bottleneck identification


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=589990738"
> ]

---

#### Feature: As a Claims Adjuster, I want to identify cases with underpayment conditions, so that I can route them to the appropriate approval workflow.
- **Role**: Claim Adjuster
- **Action**: identify underpayment conditions and route cases to the appropriate approval workflow
- **Value**: claims requiring additional financial review are properly escalated, ensuring payment accuracy and compliance with authorization limits

**Description:**

> As a **Claim Adjuster**,
> I want to **identify underpayment conditions and route cases to the appropriate approval workflow**,
> So that **claims requiring additional financial review are properly escalated, ensuring payment accuracy and compliance with authorization limits**.


**Key Capabilities:**

> 1. System evaluates claim payment against established thresholds and reserve adequacy to detect underpayment conditions
> 2. Upon identifying underpayment, adjuster is able to review financial discrepancies and supporting documentation
> 3. Adjuster submits case for approval workflow assignment based on underpayment severity and organizational authority matrix
> 4. System routes case to appropriate approver (supervisor or manager) based on business rules and approval hierarchy
> 5. Adjuster is able to track approval status and receive notifications on decisions
> 6. Upon approval, adjuster proceeds with payment adjustment or case closure activities


**Acceptance Criteria:**

> 1. **Given** a claim with payment below established thresholds, **When** financial evaluation is performed, **Then** system flags underpayment condition
> 2. **Given** an underpayment is detected, **When** adjuster initiates routing, **Then** system identifies correct approval workflow based on business rules
> 3. **Given** case requires supervisory review, **When** submitted for approval, **Then** system notifies appropriate approver and prevents premature closure
> 4. **Given** insufficient financial documentation, **When** adjuster attempts submission, **Then** system prevents routing until required information is complete
> 5. **Given** approval is granted, **When** adjuster accesses case, **Then** system enables payment adjustment and continued processing
> 6. **Given** approval is denied, **When** decision is rendered, **Then** system returns case to adjuster with denial rationale


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=589990738"
> ]

---

#### Feature: As a System Administrator, I want to configure underpayment approval rules and thresholds, so that the system can automatically identify cases requiring approval.
- **Role**: Claim Manager
- **Action**: configure underpayment approval rules and thresholds
- **Value**: the system can automatically identify and route cases requiring supervisory approval based on predefined business criteria

**Description:**

> As a **Claim Manager**,
> I want to **configure underpayment approval rules and thresholds**,
> So that **the system can automatically identify and route cases requiring supervisory approval based on predefined business criteria**


**Key Capabilities:**

> 1. User is able to define threshold parameters for underpayment approval triggers
> 2. User is able to establish approval routing rules based on payment variance criteria
> 3. User is able to configure multi-tier approval hierarchies when thresholds are breached
> 4. System automatically flags cases exceeding configured thresholds for approval workflow
> 5. User is able to validate and test rule configurations before activation
> 6. System maintains audit trail of rule changes and approvals


**Acceptance Criteria:**

> 1. **Given** threshold rules are configured, **When** an underpayment case meets criteria, **Then** system automatically routes for approval
> 2. **Given** multiple threshold tiers exist, **When** case exceeds specific tier, **Then** appropriate approval authority is assigned
> 3. **Given** invalid rule parameters, **When** user attempts activation, **Then** system prevents implementation until corrected
> 4. **Given** rule modification occurs, **When** changes are saved, **Then** audit log captures configuration history
> 5. **Given** test mode enabled, **When** rules are validated, **Then** system simulates workflow without triggering actual approvals


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=589990738"
> ]

---

### Epic: Claims Closure & Payment Schedule Completion

#### Feature: As a Claims Adjuster, I want to close claims and cases with a mandatory closing reason, so that I can properly document the final status and rationale for claim closure.
- **Role**: Claim Adjuster
- **Action**: close claims and cases with mandatory closure reason after payment schedule completion
- **Value**: final claim status is properly documented with complete rationale, ensuring audit compliance and accurate claims lifecycle tracking

**Description:**

> As a **Claim Adjuster**,
> I want to **close claims and cases with mandatory closure reason after payment schedule completion**,
> So that **final claim status is properly documented with complete rationale, ensuring audit compliance and accurate claims lifecycle tracking**.


**Key Capabilities:**

> 1. System automatically completes payment schedule when final payment is issued and business rules are satisfied
> 2. User reviews payment issuance status across all schedules to verify completion
> 3. User initiates claim or case closure and assigns mandatory closing reason to both entities
> 4. User selects closure sequence: individual claims then case, or case-level closure cascading to all claims
> 5. System executes closure, disables data editing, and finalizes status to 'Closed'
>     5.1 When closure occurs before all payments issued, system continues payment processing
>     5.2 Upon automated adjudication scenarios, system auto-closes claims without manual intervention


**Acceptance Criteria:**

> 1. **Given** all scheduled payments are issued, **When** system evaluates completion rules, **Then** payment schedule status transitions to 'Completed' automatically
> 2. **Given** adjuster initiates closure, **When** closing reason is not provided, **Then** system prevents closure submission until reason is assigned
> 3. **Given** case closure is selected, **When** claims exist under case, **Then** system automatically closes all associated claims with same closing reason
> 4. **Given** claim or case is closed, **When** user attempts data modification, **Then** system restricts all editing and permits preview-only access
> 5. **Given** non-standard closure with pending payments, **When** closure is processed, **Then** system continues payment processing independently of closure status


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=761792199"
> ]

---

#### Feature: As a Claims Adjuster, I want to close claims individually or close the case to automatically close all subordinate claims, so that I have flexibility in my closure workflow.
- **Role**: Claim Adjuster
- **Action**: close claims individually or close the case to automatically close all subordinate claims
- **Value**: I have flexibility in my closure workflow to efficiently finalize claims processing based on case complexity and business requirements

**Description:**

> As a Claim Adjuster,
> I want to close claims individually or close the case to automatically close all subordinate claims,
> So that I have flexibility in my closure workflow to efficiently finalize claims processing based on case complexity and business requirements


**Key Capabilities:**

> 1. User initiates closure by selecting individual claim closure or case-level closure that cascades to all subordinate claims
> 2. User provides mandatory closing reason aligned to business outcome categories
> 3. System validates closing reason against payment status and unpaid benefit rules to ensure data integrity
> 4. System evaluates incomplete activities across seven categories and identifies hard stops that prevent closure
>     4.1 Upon detecting hard stops related to incomplete payments, system prevents closure and requires resolution
>     4.2 Upon detecting soft stops, system presents incomplete activity summary for adjuster review and decision
> 5. System automatically closes active case management processes and associated tasks when closure is approved
> 6. System continues autonomous payment generation and posting for unposted payments after closure without user intervention


**Acceptance Criteria:**

> 1. **Given** adjuster selects case-level closure, **When** system validates no hard stops exist, **Then** system automatically closes case and all subordinate claims with provided closing reason
> 2. **Given** adjuster selects individual claim closure, **When** closure is completed for all claims, **Then** adjuster can subsequently close the case independently
> 3. **Given** closing reason is 'Denied/Withdrawn/Terminated', **When** issued payments exist, **Then** system rejects closure and requires reason correction
> 4. **Given** incomplete payments in 'approved' or 'issue requested' status exist, **When** closure is attempted, **Then** system displays hard stop error and prevents closure
> 5. **Given** soft stop conditions exist, **When** adjuster reviews and approves proceeding, **Then** system closes entity and automatically terminates active processes
> 6. **Given** case is closed with unposted payments, **When** payment jobs execute, **Then** system autonomously generates and posts remaining payments without reopening case


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=761792203"
> ]

---

#### Feature: As a Claims Adjuster, I want the system to validate closing reasons against business rules before allowing case or claim closure, so that invalid closure states are prevented.
- **Role**: Claim Adjuster
- **Action**: validate and execute case or claim closure with business rule enforcement to ensure all mandatory conditions and closing reasons align with payment status and outstanding activities
- **Value**: invalid closure states are prevented, data integrity is maintained, and post-closure autonomous processes can continue without disruption

**Description:**

> As a **Claim Adjuster**,
> I want to **validate and execute case or claim closure with business rule enforcement to ensure all mandatory conditions and closing reasons align with payment status and outstanding activities**,
> So that **invalid closure states are prevented, data integrity is maintained, and post-closure autonomous processes can continue without disruption**.


**Key Capabilities:**

> 1. Adjuster initiates closure for individual claims or entire case, triggering system validation workflow
> 2. System performs incomplete activities assessment and displays outstanding entities including active tasks, unpaid coverage, incomplete payments, and unprocessed balances
> 3. System applies hard stop rules when payments exist in approved, issue requested, or stop requested statuses
>     3.1 Upon hard stop detection, closure is blocked until conditions resolved
> 4. Adjuster selects mandatory closing reason from validated options
> 5. System validates closing reason against payment status business rules and restricts invalid combinations
>     5.1 When issued payments exist, denial reasons are rejected
>     5.2 When unpaid benefits remain, only partially paid reason is permitted
> 6. Upon successful validation, system closes case, claims, and associated process tasks while enabling autonomous payment continuation


**Acceptance Criteria:**

> 1. **Given** incomplete payments in approved or issue requested status exist, **When** adjuster attempts closure, **Then** system blocks closure with hard stop notification
> 2. **Given** issued payments exist in the claim, **When** adjuster selects denied or withdrawn closing reason, **Then** system rejects reason selection and requires valid alternative
> 3. **Given** unpaid benefits remain outstanding, **When** adjuster selects closing reason, **Then** system restricts selection to partially paid reason only
> 4. **Given** all validation rules satisfied, **When** adjuster confirms closure, **Then** system closes case, claims, and active process tasks automatically
> 5. **Given** case or claim closed successfully, **When** user accesses closed entities, **Then** system permits preview only and prevents editing activities
> 6. **Given** unposted payments exist at closure, **When** closure completes, **Then** system continues autonomous payment generation and posting without manual intervention


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=761792203"
> ]

---

#### Feature: As a Claims Adjuster, I want to view a summary of incomplete activities before closing a case or claim, so that I can identify unfinished business processes and make informed closure decisions.
- **Role**: Claim Adjuster
- **Action**: review a comprehensive summary of incomplete activities and business processes before finalizing case or claim closure
- **Value**: I can make informed closure decisions, ensure all business obligations are fulfilled, and prevent premature closure that could result in operational errors or compliance issues

**Description:**

> As a **Claim Adjuster**,
> I want to **review a comprehensive summary of incomplete activities and business processes before finalizing case or claim closure**,
> So that **I can make informed closure decisions, ensure all business obligations are fulfilled, and prevent premature closure that could result in operational errors or compliance issues**


**Key Capabilities:**

> 1. User initiates case or claim closure process through designated business workflow
> 2. System validates closure eligibility by scanning all related business entities for incomplete obligations
> 3. Upon detection of hard-stop conditions (incomplete payments in approved or issue-requested status), system prevents closure and alerts user
> 4. When soft-stop conditions exist (active tasks, unpaid coverage, unprocessed balances), system presents comprehensive activity summary for adjuster review
> 5. User evaluates incomplete activities and assigns mandatory closure reason aligned with payment status business rules
> 6. Upon approval, system executes closure, terminates active processes, and restricts future editing while allowing autonomous payment completion


**Acceptance Criteria:**

> 1. **Given** incomplete payments exist in approved or issue-requested status, **When** user attempts closure, **Then** system prevents closure and displays validation error
> 2. **Given** issued payments exist, **When** user selects Denied or Withdrawn closure reason, **Then** system rejects the reason and requires alternative selection
> 3. **Given** unpaid benefits remain, **When** user assigns closure reason, **Then** system restricts selection to Partially Paid option only
> 4. **Given** all validations pass, **When** user confirms closure, **Then** system closes case, subordinate claims, and active processes while maintaining payment schedule autonomy
> 5. **Given** case is closed, **When** payment schedules remain incomplete, **Then** system continues autonomous payment generation and posting
> 6. **Given** closure is complete, **When** user accesses closed case, **Then** system allows preview only without editing capabilities


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=761792203"
> ]

---

#### Feature: As a Claims Adjuster, I want the system to prevent closure when hard stop conditions exist, so that critical unfinished processes are not bypassed.
- **Role**: Claim Adjuster
- **Action**: prevent case and claim closure when critical hard stop conditions exist
- **Value**: critical unfinished payment processes are not bypassed and data integrity is maintained

**Description:**

> As a Claim Adjuster,
> I want to prevent case and claim closure when critical hard stop conditions exist,
> So that critical unfinished payment processes are not bypassed and data integrity is maintained.


**Key Capabilities:**

> 1. User initiates closure process for case or individual claims
> 2. System validates incomplete activities across payment workflows, tasks, and schedules
> 3. When hard stop conditions detected (payments in approved/issue requested/stop requested status), system blocks closure entirely
>     3.1 System displays categorized incomplete items preventing closure
>     3.2 User must resolve hard stop conditions before retry
> 4. When soft warnings exist (unpaid coverages, unposted payments), system alerts user but allows adjuster discretion to proceed
> 5. Upon validation success, system assigns mandatory closing reason and transitions entities to closed state
> 6. System auto-closes subordinate claims and related processes


**Acceptance Criteria:**

> 1. **Given** payments exist in approved/issue requested/stop requested status, **When** user attempts closure, **Then** system prevents closure and displays hard stop warning
> 2. **Given** no hard stops exist but soft warnings present, **When** user reviews incomplete items, **Then** system allows adjuster to proceed or cancel
> 3. **Given** user attempts closure without mandatory closing reason, **When** submission occurs, **Then** system prevents closure until reason provided
> 4. **Given** closing reason violates business rules (e.g., 'Denied' with issued payments), **When** validation runs, **Then** system blocks inappropriate reason assignment
> 5. **Given** all hard stops resolved, **When** user completes closure, **Then** system closes case and subordinate claims atomically
> 6. **Given** case closed successfully, **When** user accesses entity, **Then** system permits preview-only mode with no editing capability


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=761792203"
> ]

---

#### Feature: As a Claims Adjuster, I want the system to automatically close related CMMN tasks and processes when I close a case or claim, so that dependent workflows are properly terminated.
- **Role**: Claim Adjuster
- **Action**: automatically close related CMMN tasks and processes when closing a case or claim
- **Value**: dependent workflows are properly terminated and system maintains data integrity without manual intervention

**Description:**

> As a Claim Adjuster,
> I want to automatically close related CMMN tasks and processes when closing a case or claim,
> So that dependent workflows are properly terminated and system maintains data integrity without manual intervention.


**Key Capabilities:**

> 1. User validates all activities and payments meet closure eligibility criteria
> 2. User selects closing reason compliant with validation rules (payment status and unpaid benefits determine allowable reasons)
> 3. System validates no hard stops exist (incomplete payments with approved/issue requested/stop requested statuses)
> 4. Upon detecting incomplete activities without hard stops, system presents review list for adjuster approval
> 5. User approves closure decision
> 6. System automatically terminates related CMMN processes and tasks, assigns closed status, and restricts access to preview-only mode
>     6.1 If unposted payments exist, system continues autonomous payment processing post-closure


**Acceptance Criteria:**

> 1. **Given** all hard stop conditions resolved, **When** adjuster approves closure, **Then** system closes case/claims and automatically terminates related CMMN processes and tasks
> 2. **Given** incomplete payment with approved/issue requested/stop requested status exists, **When** adjuster attempts closure, **Then** system prevents closure with warning error
> 3. **Given** issued payments exist, **When** adjuster selects Denied/Withdrawn/Terminated reason, **Then** system blocks selection and enforces alternative reason choice
> 4. **Given** unpaid benefits exist, **When** adjuster selects closing reason, **Then** system restricts selection to Partially Paid only
> 5. **Given** case closure initiated, **When** multiple claims exist under case, **Then** system automatically closes all subordinate claims before closing case
> 6. **Given** case/claim closed, **When** user accesses entity, **Then** system provides preview-only access and continues autonomous payment processing if applicable


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=761792203"
> ]

---

#### Feature: As a Claims Adjuster, I want closed claims and cases to be read-only, so that historical claim data cannot be accidentally modified after closure.
- **Role**: Claim Adjuster
- **Action**: ensure closed claims and cases become read-only to preserve historical integrity
- **Value**: historical claim data remains protected from accidental modifications and maintains audit trail compliance

**Description:**

> As a **Claim Adjuster**,
> I want to **ensure closed claims and cases become read-only to preserve historical integrity**,
> So that **historical claim data remains protected from accidental modifications and maintains audit trail compliance**


**Key Capabilities:**

> 1. User completes payment schedule and verifies all payments are issued through payment status review
> 2. User initiates closure process by selecting closure reason and choosing closure approach (individual claims or entire case)
> 3. System executes closure command and transitions claims and case to closed status with assigned closure reason
> 4. System automatically disables all editing capabilities upon closure confirmation
>     4.1 When closure reason is 'Completed', system validates payment schedule completion and zero balance
>     4.2 When non-standard closure reasons apply, system allows closure with incomplete payment schedules
> 5. User is able to preview and review closed claim data in read-only mode for reference purposes
> 6. System continues processing scheduled payments in background even after case closure


**Acceptance Criteria:**

> 1. **Given** all payments are issued and payment schedule is completed, **When** user closes claim with 'Completed' reason, **Then** system sets claim status to 'Closed' and disables all data editing functions
> 2. **Given** claim or case is closed, **When** user attempts to access the record, **Then** system displays data in preview-only mode without edit controls
> 3. **Given** payments are scheduled but not fully issued, **When** user initiates closure, **Then** system permits closure and continues payment processing in background
> 4. **Given** closure is executed with non-standard reason, **When** payment schedule is incomplete, **Then** system allows closure with non-zero balance and unissued payments
> 5. **Given** case closure is initiated, **When** claims under the case are still open, **Then** system automatically closes all associated claims with same closure reason


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=761792199"
> ]

---

#### Feature: As a Claims Operations Manager, I want the system to automatically complete payment schedules when all payments are issued, so that payment lifecycle is properly tracked without manual intervention.
- **Role**: Claim Adjuster
- **Action**: automatically complete payment schedules upon full payment issuance and initiate claims closure workflow
- **Value**: payment lifecycle tracking is accurate, manual monitoring is eliminated, and closure processes are streamlined to reduce operational overhead

**Description:**

> As a Claim Adjuster,
> I want to automatically complete payment schedules upon full payment issuance and initiate claims closure workflow,
> So that payment lifecycle tracking is accurate, manual monitoring is eliminated, and closure processes are streamlined to reduce operational overhead.


**Key Capabilities:**

> 1. Upon payment issuance, system evaluates payment schedule completion rules and automatically assigns 'Completed' status when all scheduled payments are issued.
> 2. User verifies payment issuance status through payment list or closure summary view before initiating closure activities.
> 3. User initiates closure by selecting either individual claim closure followed by case closure, or case closure triggering automatic closure of all associated claims.
>     3.1 User assigns closing reason during closure initiation.
> 4. System transitions claims and case to 'Closed' status and enforces read-only restrictions on all associated data.
> 5. When early closure occurs (payments scheduled but not issued), system continues payment processing post-closure.
> 6. In automated adjudication scenarios, system closes claims and case automatically upon payment schedule completion.


**Acceptance Criteria:**

> 1. **Given** all scheduled payments are issued, **When** the final payment issuance completes, **Then** the system automatically marks the payment schedule as 'Completed' without user intervention.
> 2. **Given** the payment schedule is completed, **When** the user accesses closure workflows, **Then** the system displays accurate payment status and closure readiness indicators.
> 3. **Given** the user initiates case closure, **When** associated claims are open, **Then** the system automatically closes all claims under the case.
> 4. **Given** the user closes a claim or case, **When** closure is confirmed, **Then** the system enforces read-only access and prevents further data modification.
> 5. **Given** payments are scheduled but not issued, **When** the user closes the case early, **Then** the system continues payment issuance post-closure.
> 6. **Given** automated adjudication is active and payment schedule completes, **When** completion rules are satisfied, **Then** the system automatically closes claims and case without manual intervention.


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=761792199"
> ]

---

#### Feature: As a Claims Adjuster, I want to view payment statuses in the payment list to verify all payments are issued before closing, so that I can confirm payment schedule completion.
- **Role**: Claim Adjuster
- **Action**: review payment statuses in the payment list to verify all scheduled payments are issued before initiating claims and case closure
- **Value**: I can ensure payment schedule completion and make informed closure decisions with accurate financial reconciliation

**Description:**

> As a **Claim Adjuster**,
> I want to **review payment statuses in the payment list to verify all scheduled payments are issued before initiating claims and case closure**,
> So that **I can ensure payment schedule completion and make informed closure decisions with accurate financial reconciliation**


**Key Capabilities:**

> 1. User accesses payment list to preview current payment statuses for the claim or case
> 2. User reviews each payment entry to verify issuance status without automated completion indicators
> 3. User assesses whether payment schedule obligations are fulfilled based on manual review
> 4. Upon confirming payment statuses align with closure criteria, user proceeds to closure workflow
>     4.1 If payments remain unissued, user may proceed with alternate closure path
>     4.2 If all payments issued, user continues standard completion process
> 5. User defines closure reason appropriate to payment completion status
> 6. User executes closure command, triggering system restrictions on further edits


**Acceptance Criteria:**

> 1. **Given** a claim with scheduled payments, **When** the adjuster accesses the payment list, **Then** system displays all payment records with current issuance statuses
> 2. **Given** payment list is displayed, **When** adjuster reviews payment statuses, **Then** system allows manual verification without automated completion indicators
> 3. **Given** payment verification is complete, **When** adjuster initiates closure, **Then** system accepts closure regardless of outstanding payment status
> 4. **Given** closure is executed, **When** system processes closure command, **Then** system restricts all editing activities and enables preview-only mode
> 5. **Given** payments remain unissued, **When** case is closed, **Then** system continues payment processing post-closure
> 6. **Given** closure reason is defined, **When** closure completes, **Then** system assigns appropriate status and closing reason to case and claims


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=761792199"
> ]

---

#### Feature: As a Claims Adjuster, I want to close claims and cases even if payments are not yet generated, so that I can close cases based on business decisions while allowing the system to continue issuing payments.
- **Role**: Claim Adjuster
- **Action**: close claims and cases independently of payment generation status while ensuring system continues payment processing
- **Value**: I can finalize claim decisions based on business requirements without being blocked by pending payments, improving operational efficiency and case throughput

**Description:**

> As a **Claim Adjuster**,
> I want to **close claims and cases independently of payment generation status while ensuring system continues payment processing**,
> So that **I can finalize claim decisions based on business requirements without being blocked by pending payments, improving operational efficiency and case throughput**.


**Key Capabilities:**

> 1. System automatically completes payment schedules when final payment is issued and validates completion rules
> 2. User verifies payment status and initiates closure workflow by selecting mandatory closing reason
> 3. User chooses closure sequence: close individual claims first then case separately, or close case which automatically closes all associated claims
> 4. System applies closure with selected reason, transitions case and claims to closed status, and disables editing while preserving data access
> 5. Upon closure with 'Completed' reason: all payments issued, schedule status completed, payee balances zero
>     5.1 Upon closure with alternate reason: case closed with potential outstanding payments, non-zero balances, or no payment schedule
> 6. System continues processing scheduled payments even after case closure


**Acceptance Criteria:**

> 1. **Given** payment schedule exists **when** last payment is issued and completion rules satisfied **then** system automatically marks schedule as completed without user intervention
> 2. **Given** adjuster initiates closure **when** closing reason is not provided **then** system prevents closure until mandatory reason is selected
> 3. **Given** adjuster closes case with 'Completed' reason **when** closure executes **then** all claims auto-close, payments fully issued, balances zero, editing disabled
> 4. **Given** adjuster closes with non-standard reason **when** closure processes **then** case closes with potential outstanding payments or non-zero balances while maintaining data integrity
> 5. **Given** case is closed **when** scheduled payments remain **then** system continues issuing payments according to schedule
> 6. **Given** case or claim is closed **when** user attempts modification **then** system restricts editing and provides read-only preview access


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=761792199"
> ]

---

### Epic: Dental Insurance Claim Automation & Processing

#### Feature: As a Claims Adjuster, I want to process dental claims through the complete intake and settlement workflow, so that claims are accurately adjudicated and payments are generated efficiently
- **Role**: Claim Adjuster
- **Action**: process dental claims through the complete intake, adjudication, settlement, and payment workflow
- **Value**: claims are accurately adjudicated, approved, and payments are generated efficiently with full lifecycle tracking from intake to closure

**Description:**

> As a **Claim Adjuster**,
> I want to **process dental claims through the complete intake, adjudication, settlement, and payment workflow**,
> So that **claims are accurately adjudicated, approved, and payments are generated efficiently with full lifecycle tracking from intake to closure**


**Key Capabilities:**

> 1. Initiate claim processing upon new intake or reopened claim submission
> 2. Complete intake validation and submit loss details to settlement initialization
> 3. Adjudicate settlement based on coverage rules and approve settlement for payment processing
>     3.1 Upon approval, open loss record for financial tracking
> 4. Build and activate payment schedule to enable automated payment generation
> 5. Execute automated payment generation job and issue payments iteratively
>     5.1 When all scheduled payments are generated and issued, complete payment schedule
> 6. Close settlement and loss records, transitioning claim to 'Closed-Paid' status


**Acceptance Criteria:**

> 1. **Given** a new or reopened dental claim, **When** intake is completed, **Then** system submits loss and initializes settlement
> 2. **Given** settlement is adjudicated, **When** approval is granted, **Then** system opens loss and builds payment schedule
> 3. **Given** payment schedule is activated, **When** payment generation job runs, **Then** system issues payments and tracks completion status
> 4. **Given** not all payments are issued, **When** completion check occurs, **Then** system loops back to payment generation
> 5. **Given** all payments are issued, **When** completion check passes, **Then** system completes payment schedule and closes settlement
> 6. **Given** settlement and loss are closed, **When** final status is reached, **Then** claim status is 'Closed' with reason 'Paid'


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=577775956"
> ]

---

#### Feature: As a Claims Adjuster, I want to adjudicate dental settlements with automated rule evaluation and proposal generation, so that settlement decisions are consistent and compliant with policy rules
- **Role**: Claim Adjuster
- **Action**: adjudicate dental settlements with automated rule evaluation and proposal-based decision routing
- **Value**: settlement decisions are consistent, compliant with policy rules, and efficiently processed through automated workflows

**Description:**

> As a **Claim Adjuster**,
> I want to **adjudicate dental settlements with automated rule evaluation and proposal-based decision routing**,
> So that **settlement decisions are consistent, compliant with policy rules, and efficiently processed through automated workflows**


**Key Capabilities:**

> 1. Initialize settlement upon loss submission to begin adjudication lifecycle.
> 2. Execute automated rule evaluation to generate adjudication proposal (PAY, DENY, PREDET-APPROVE, PREDET-DENY, PEND).
> 3. Route settlement automatically based on proposal outcome.
>     3.1 Auto-approve when proposal indicates PAY or PREDET-APPROVE.
>     3.2 Auto-disapprove when proposal indicates DENY or PREDET-DENY.
>     3.3 Trigger manual review task when proposal indicates PEND.
> 4. Readjudicate settlement with override values to correct errors or reassess decisions.
> 5. Finalize settlement by transitioning to closed or disapproved terminal state.


**Acceptance Criteria:**

> 1. **Given** loss is submitted, **When** settlement initialization is triggered, **Then** settlement enters adjudicating state and invokes rules engine.
> 2. **Given** adjudication completes with PAY/PREDET-APPROVE proposal, **When** system evaluates outcome, **Then** settlement automatically transitions to approved state without manual intervention.
> 3. **Given** adjudication completes with DENY/PREDET-DENY proposal, **When** system evaluates outcome, **Then** settlement automatically transitions to disapproved state.
> 4. **Given** adjudication completes with PEND proposal, **When** system evaluates outcome, **Then** settlement remains pending and review task is created for adjuster.
> 5. **Given** settlement requires correction, **When** readjudication is initiated, **Then** new settlement version is created and lifecycle restarts from adjudicating state.
> 6. **Given** parent claim is closed, **When** readjudication is attempted, **Then** system prevents readjudication action.


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=512754882"
> ]

---

#### Feature: As a Claims Adjuster, I want to approve or disapprove dental settlements based on adjudication results, so that claim decisions are properly authorized before payment processing
- **Role**: Claim Adjuster
- **Action**: authorize or reject dental claim settlements based on system adjudication outcomes
- **Value**: claim decisions are finalized with proper authorization controls before initiating payment workflows

**Description:**

> As a **Claim Adjuster**,
> I want to **authorize or reject dental claim settlements based on system adjudication outcomes**,
> So that **claim decisions are finalized with proper authorization controls before initiating payment workflows**.


**Key Capabilities:**

> 1. System adjudicates dental settlement and generates decision proposal (Pay, Deny, Pend, Predetermination outcomes)
> 2. Upon proposal generation, system automatically routes to approval or disapproval based on outcome type
>     2.1 When proposal indicates Pay or Predetermination Approve, system auto-approves settlement
>     2.2 When proposal indicates Deny or Predetermination Deny, system auto-disapproves settlement
>     2.3 When proposal requires manual review (Pend), system creates review task for adjuster action
> 3. User is able to manually authorize settlement advancing status from Pending to Approved
> 4. User is able to manually reject settlement advancing status from Pending to Disapproved
> 5. User is able to initiate readjudication creating new settlement version with override values when needed
> 6. Upon authorization, settlement advances to closure processing enabling payment workflows


**Acceptance Criteria:**

> 1. **Given** adjudication completes with Pay or Predetermination Approve proposal, **When** system processes result, **Then** settlement automatically transitions to Approved status
> 2. **Given** adjudication completes with Deny or Predetermination Deny proposal, **When** system processes result, **Then** settlement automatically transitions to Disapproved status
> 3. **Given** adjudication completes with Pend proposal, **When** system processes result, **Then** settlement remains Pending and review task is created
> 4. **Given** settlement is in Pending status, **When** adjuster executes approval action, **Then** settlement transitions to Approved status enabling closure
> 5. **Given** settlement is in Pending status, **When** adjuster executes disapproval action, **Then** settlement transitions to Disapproved status
> 6. **Given** settlement requires recalculation, **When** adjuster initiates readjudication with overrides, **Then** system creates new settlement version and returns to adjudication workflow


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=512754882"
> ]

---

#### Feature: As a Claims Adjuster, I want to apply overrides, bypasses, and waivers to dental settlements, so that I can handle exceptions and special circumstances in claim processing
- **Role**: Claim Adjuster
- **Action**: apply overrides, bypasses, and waivers to dental settlements
- **Value**: I can handle exceptions and special circumstances in claim processing with appropriate control and flexibility

**Description:**

> As a **Claim Adjuster**,
> I want to **apply overrides, bypasses, and waivers to dental settlements**,
> So that **I can handle exceptions and special circumstances in claim processing with appropriate control and flexibility**


**Key Capabilities:**

> 1. User initiates exception management for settlement requiring deviation from standard adjudication rules
> 2. User applies claim-level exceptions to affect entire claim processing
>     2.1 Bypass automated logic for duplicate services or clinical reviews
>     2.2 Override or waive preventive/basic services waiting periods
>     2.3 Directly allow or deny service at claim level
> 3. User applies service-level exceptions for granular control over specific services
>     3.1 Bypass service-specific duplicate detection or review requirements
>     3.2 Override CDT code coverage or essential health benefit designation
>     3.3 Waive service category or late entrant waiting periods
> 4. System records all exception actions with settlement details maintaining audit trail
> 5. System processes claim through modified adjudication logic reflecting applied exceptions
> 6. Upon completion, system updates settlement status and generates decision result


**Acceptance Criteria:**

> 1. **Given** a dental settlement requires exception handling, **When** adjuster applies claim-level bypass, **Then** system circumvents specified automated logic rules for entire claim
> 2. **Given** waiting period requirements must be modified, **When** adjuster applies override at claim or service level, **Then** system adjusts waiting period values accordingly
> 3. **Given** specific requirements must be eliminated, **When** adjuster applies waiver, **Then** system removes designated constraints from processing
> 4. **Given** direct adjudication control is needed, **When** adjuster applies allow/deny override, **Then** system supersedes automated decision logic
> 5. **Given** exceptions are applied at service level, **When** processing occurs, **Then** system applies controls only to designated services while maintaining standard processing for others
> 6. **Given** any exception is applied, **When** settlement processing completes, **Then** system maintains complete audit trail of all modifications


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=512754875"
> ]

---

#### Feature: As a Claims Adjuster, I want to readjudicate dental settlements with override values when needed, so that I can correct errors or apply new information without losing the claim history
- **Role**: Claim Adjuster
- **Action**: Readjudicate dental settlements with override values when corrections or new information are available
- **Value**: Errors can be corrected and updated policy/clinical information applied while preserving complete audit trail and settlement history

**Description:**

> As a **Claim Adjuster**,
> I want to **readjudicate dental settlements with override values when corrections or new information are available**,
> So that **errors can be corrected and updated policy/clinical information applied while preserving complete audit trail and settlement history**


**Key Capabilities:**

> 1. System creates new settlement version upon readjudication initiation from Pending, Approved, Disapproved, or Closed states
> 2. User is able to provide override values during readjudication to correct adjudication inputs or apply new coverage information
> 3. Settlement transitions to Adjudicating state and triggers rules engine re-evaluation with updated parameters
> 4. Upon successful re-adjudication, system generates new adjudication proposal and follows automated decision logic
> 5. When parent claim status is Closed, system prevents readjudication to maintain claim finality
> 6. System maintains complete version history across all settlement iterations for audit purposes


**Acceptance Criteria:**

> 1. **Given** settlement is in Pending/Approved/Disapproved/Closed state and claim is not Closed, **When** readjudication is initiated with override values, **Then** system creates new settlement version and transitions to Adjudicating state
> 2. **Given** settlement is readjudicated with overrides, **When** rules engine completes evaluation, **Then** system returns new adjudication proposal and applies automated approval/disapproval logic
> 3. **Given** parent claim status is Closed, **When** readjudication is attempted, **Then** system prevents readjudication and maintains settlement state
> 4. **Given** readjudication creates new version, **When** settlement history is accessed, **Then** all previous versions and decisions remain retrievable
> 5. **Given** re-adjudication proposal is PEND, **When** automated decision logic executes, **Then** settlement remains Pending and manual review task is created


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=512754882"
> ]

---

#### Feature: As a Claims Adjuster, I want to suspend and unsuspend dental claims with their associated payment schedules, so that I can temporarily halt processing when needed and resume without data loss
- **Role**: Claim Adjuster
- **Action**: suspend and unsuspend orthodontic dental claims with automated payment schedule coordination
- **Value**: I can temporarily halt claim processing and payment generation when circumstances require intervention, then resume operations without data loss or manual reconciliation

**Description:**

> As a Claim Adjuster, I want to suspend and unsuspend orthodontic dental claims with automated payment schedule coordination, so that I can temporarily halt claim processing and payment generation when circumstances require intervention, then resume operations without data loss or manual reconciliation.


**Key Capabilities:**

> 1. User initiates suspension action on an open orthodontic dental claim requiring temporary hold
> 2. System transitions claim status to suspended and automatically identifies all associated active payment schedules
> 3. System suspends all active payment schedules simultaneously and halts automated payment generation
> 4. System creates review task to ensure suspended claims receive timely follow-up
> 5. Upon unsuspend action, system restores claim to open status and reactivates all suspended payment schedules
> 6. System resumes automated payment processing from reactivated schedules without data loss


**Acceptance Criteria:**

> 1. **Given** an open orthodontic claim with active payment schedules, **when** adjuster suspends the claim, **then** system sets claim and all associated schedules to suspended status and halts payments
> 2. **Given** a suspended claim, **when** suspension occurs, **then** system automatically generates a review task for workflow tracking
> 3. **Given** a suspended claim with suspended schedules, **when** adjuster unsuspends the claim, **then** system restores claim to open and all schedules to active status
> 4. **Given** reactivated payment schedules, **when** unsuspend completes, **then** system resumes automated payment generation without requiring manual intervention
> 5. **Given** suspension or unsuspend action, **when** processing fails, **then** system prevents partial status updates and maintains data consistency


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=539562616"
> ]

---

#### Feature: As a Claims Operations Manager, I want to automatically generate and issue payments from approved dental settlement payment schedules, so that claim payments are processed efficiently and on schedule
- **Role**: Claim Adjuster
- **Action**: automatically generate and issue payments from approved dental settlement payment schedules
- **Value**: claim payments are processed efficiently, on schedule, and without manual intervention, reducing operational overhead and ensuring timely reimbursement

**Description:**

> As a **Claim Adjuster**,
> I want to **automatically generate and issue payments from approved dental settlement payment schedules**,
> So that **claim payments are processed efficiently, on schedule, and without manual intervention, reducing operational overhead and ensuring timely reimbursement**.


**Key Capabilities:**

> 1. Initialize settlement process upon completion of dental claim intake and loss submission
> 2. Perform settlement adjudication and obtain necessary approval for payment authorization
> 3. Build and activate payment schedule based on approved settlement terms
> 4. Execute automated payment generation job to create scheduled payment requests
>     4.1 Upon job execution, system requests and issues payments automatically
> 5. Monitor payment schedule completion status and trigger subsequent payment cycles until all obligations are fulfilled
> 6. Close settlement, loss, and claim automatically when all payments are successfully issued


**Acceptance Criteria:**

> 1. **Given** an approved dental settlement, **When** the payment schedule is activated, **Then** the system automatically executes payment generation without manual triggers
> 2. **Given** a payment generation job runs, **When** payments are requested, **Then** the system issues payments and records transaction details
> 3. **Given** a payment schedule with multiple installments, **When** not all payments are completed, **Then** the system iterates through payment cycles until all obligations are fulfilled
> 4. **Given** all scheduled payments are issued, **When** completion verification occurs, **Then** the system automatically closes the payment schedule, settlement, loss, and claim
> 5. **Given** incomplete settlement approval, **When** payment schedule activation is attempted, **Then** the system prevents payment generation until approval is obtained


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=577775956"
> ]

---

#### Feature: As a Claims Operations Manager, I want to close dental settlements and losses when all payments are completed, so that claims reach final closure status and records are properly archived
- **Role**: Claim Adjuster
- **Action**: close dental settlements and losses after all payments are completed
- **Value**: claims reach final closure status and records are properly archived for operational efficiency and compliance

**Description:**

> As a **Claim Adjuster**,
> I want to **close dental settlements and losses after all payments are completed**,
> So that **claims reach final closure status and records are properly archived for operational efficiency and compliance**


**Key Capabilities:**

> 1. User is able to adjudicate settlement to determine coverage and payment amounts
> 2. User is able to obtain settlement approval before initiating payment processing
> 3. System generates payments automatically based on activated payment schedule
>     3.1 Upon payment generation job execution, system issues payments to appropriate parties
>     3.2 System verifies payment completion status against schedule
> 4. When all scheduled payments are generated and issued, user is able to complete payment schedule
> 5. User is able to close settlement and loss records sequentially
> 6. System transitions claim to final closed status with paid reason upon completion


**Acceptance Criteria:**

> 1. **Given** settlement is adjudicated and approved, **When** payment schedule is activated, **Then** system generates payments automatically through scheduled job
> 2. **Given** payment generation is in progress, **When** not all payments are completed, **Then** system continues payment cycles until schedule fulfillment
> 3. **Given** all scheduled payments are issued, **When** user completes payment schedule, **Then** system enables settlement closure
> 4. **Given** settlement is closed, **When** user closes loss record, **Then** system transitions claim to closed status with paid reason
> 5. **Given** claim lacks settlement approval, **When** user attempts payment processing, **Then** system prevents payment schedule activation
> 6. **Given** claim is closed, **When** archival is triggered, **Then** system maintains complete audit trail of payment and closure actions


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=577775956"
> ]

---

#### Feature: As a Claims Adjuster, I want to manage pending dental settlements that require manual review, so that I can address claims that cannot be automatically approved or denied
- **Role**: Claim Adjuster
- **Action**: review and resolve dental settlements that require manual intervention after automated adjudication determines they cannot be automatically approved or denied
- **Value**: I can apply professional judgment to complex cases, ensure accurate claim outcomes, and maintain quality control over automated decisions that require human expertise

**Description:**

> As a **Claim Adjuster**,
> I want to **review and resolve dental settlements that require manual intervention after automated adjudication determines they cannot be automatically approved or denied**,
> So that **I can apply professional judgment to complex cases, ensure accurate claim outcomes, and maintain quality control over automated decisions that require human expertise**


**Key Capabilities:**

> 1. System automatically routes settlements to manual review when adjudication engine returns 'PEND' proposal and creates review task
> 2. Adjuster accesses pending settlement details and evaluates business rules engine recommendations against clinical documentation
> 3. Adjuster decides settlement outcome by approving or disapproving based on analysis
>     3.1 Upon approval, settlement transitions to 'Approved' status enabling payment processing
>     3.2 Upon disapproval, settlement transitions to 'Disapproved' status and claim closure
> 4. Adjuster initiates readjudication to return settlement to 'Adjudicating' status when corrections or override values are needed
> 5. System prevents readjudication when parent claim reaches 'Closed' status


**Acceptance Criteria:**

> 1. **Given** automated adjudication results in 'PEND' proposal, **When** settlement reaches 'Pending' status, **Then** system creates review task assigned to Claims Adjuster queue
> 2. **Given** settlement is in 'Pending' status, **When** adjuster approves settlement, **Then** system transitions settlement to 'Approved' status enabling downstream payment workflow
> 3. **Given** settlement is in 'Pending' status, **When** adjuster disapproves settlement, **Then** system transitions settlement to 'Disapproved' status and prevents payment processing
> 4. **Given** settlement requires data correction, **When** adjuster initiates readjudication with override values, **Then** system creates new settlement version and returns to 'Adjudicating' status
> 5. **Given** parent claim is in 'Closed' status, **When** adjuster attempts readjudication, **Then** system prevents command execution


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=512754882"
> ]

---

### Epic: Common Claim Processing Capabilities

#### Feature: As a Claims Adjuster, I want to manage the complete lifecycle of an Event Case from intake through closure, so that all related claims are processed together and consistently
- **Role**: Claim Adjuster
- **Action**: manage the complete lifecycle of an Event Case from intake through closure
- **Value**: all related claims are processed together and consistently under a unified case structure

**Description:**

> As a **Claim Adjuster**,
> I want to **manage the complete lifecycle of an Event Case from intake through closure**,
> So that **all related claims are processed together and consistently under a unified case structure**


**Key Capabilities:**

> 1. Initiate Event Case intake and assign initial claim to establish the case hierarchy
> 2. Review Event Case details and assess status of all related claims within the case
> 3. Execute case adjustments when needed, including event data modifications, financial adjustments, and party information updates
>     3.1 Upon identifying adjustment needs at case level, user is able to modify event case data before proceeding
> 4. Manage individual claim adjustments and updates within the Event Case context
> 5. Process payments and manage financial transactions at both case and claim levels
> 6. Close individual claims and subsequently close the Event Case upon completion of all processing activities


**Acceptance Criteria:**

> 1. **Given** a new loss event is reported, **When** the adjuster initiates intake, **Then** the system creates an Event Case and assigns the initial claim successfully
> 2. **Given** an active Event Case exists, **When** case-level adjustments are required, **Then** the system allows modifications to event data, financials, and party information before claim processing continues
> 3. **Given** multiple claims under one Event Case, **When** individual claim adjustments are needed, **Then** the system permits claim-specific modifications without affecting other claims
> 4. **Given** all claims are finalized, **When** the adjuster closes the Event Case, **Then** the system prevents closure if any claim remains in active status
> 5. **Given** a closed Event Case requires additional processing, **When** the adjuster reopens it, **Then** the system reactivates the case and allows further processing
> 6. **Given** incomplete or missing data, **When** attempting case or claim closure, **Then** the system prevents submission until all required processing is completed


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=540788240"
> ]

---

#### Feature: As a Claims Adjuster, I want to adjust Event Case and Claim data including absence information, so that claim processing reflects accurate and current information
- **Role**: Claim Adjuster
- **Action**: update absence case and claim data including tax withholdings, deductions, absence reasons, and eligibility information to maintain accurate records throughout the claim lifecycle
- **Value**: claim processing reflects current and accurate information, ensuring correct benefit calculations, payment accuracy, and regulatory compliance while supporting informed adjudication decisions

**Description:**

> As a **Claim Adjuster**,
> I want to **update absence case and claim data including tax withholdings, deductions, absence reasons, and eligibility information to maintain accurate records throughout the claim lifecycle**,
> So that **claim processing reflects current and accurate information, ensuring correct benefit calculations, payment accuracy, and regulatory compliance while supporting informed adjudication decisions**


**Key Capabilities:**

> 1. User is able to manage tax withholdings by specifying flat amounts or percentages with effective date ranges for federal income tax deductions
> 2. User is able to configure pre-tax or post-tax deductions as flat amounts or percentages with applicable date ranges
> 3. User is able to update absence reasons, which triggers system re-adjudication and potential creation of new claim types
> 4. User is able to modify absence case attributes including participant work schedules, earnings data, absence periods, party information, and payment preferences
> 5. Upon submission of payment-impacting data, system automatically recalculates benefit amounts and payment allocations
> 6. Upon submission of eligibility-impacting data, system executes automated re-adjudication including applicability evaluation, eligibility determination, and benefit calculation


**Acceptance Criteria:**

> 1. **Given** an absence case in Incomplete or Open status, **When** the adjuster updates tax withholdings or deductions, **Then** system recalculates payment amounts reflecting the updated withholding rules and effective date ranges
> 2. **Given** absence reasons are modified, **When** the adjuster submits changes, **Then** system triggers complete re-adjudication including applicability evaluation and creates new claim types as applicable
> 3. **Given** eligibility-impacting data is updated, **When** system processes changes, **Then** existing claims retain their status even if no longer applicable, and new applicable claims are created
> 4. **Given** case status is Incomplete, **When** absence reasons are managed, **Then** system automatically transitions case to submitted status and executes adjudication workflow
> 5. **Given** payment-related data is modified, **When** system recalculates payments, **Then** withholdings and deductions are prorated correctly based on payment allocation date overlaps
> 6. **Given** multiple ad-hoc updates occur, **When** adjuster performs activities in any sequence, **Then** system maintains data integrity and executes appropriate calculation or adjudication processes for each update type


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=585308318"
> ]

---

#### Feature: As a Claims Adjuster, I want to manage financial adjustments including tax withholdings, deductions, and YTD earnings, so that payment calculations are accurate and compliant
- **Role**: Claim Adjuster
- **Action**: manage financial adjustments including tax withholdings, deductions, and YTD earnings on open absence cases
- **Value**: payment calculations remain accurate, compliant, and reflect current case circumstances throughout the claim lifecycle

**Description:**

> As a **Claim Adjuster**,
> I want to **manage financial adjustments including tax withholdings, deductions, and YTD earnings on open absence cases**,
> So that **payment calculations remain accurate, compliant, and reflect current case circumstances throughout the claim lifecycle**


**Key Capabilities:**

> 1. System validates absence case eligibility based on status ('Incomplete' or 'Open') before allowing adjustments
> 2. User applies tax withholdings using flat amounts or percentages with effective date ranges; system auto-applies to overlapping payment allocations
> 3. User configures deductions (pre-tax/post-tax, flat/percentage) with validity periods applicable across multiple claims
> 4. User updates absence attributes (reasons, dates, earnings, party data) triggering automated case re-adjudication
> 5. Upon financial adjustment completion, system recalculates existing payments and re-evaluates claim eligibility
> 6. When absence reasons change on incomplete cases, system automatically submits case and creates newly applicable claim types


**Acceptance Criteria:**

> 1. **Given** absence case status is 'Closed', **When** adjuster attempts financial adjustment, **Then** system prevents modification and displays appropriate status message
> 2. **Given** valid tax withholding with date range, **When** payment allocation dates overlap, **Then** system applies prorated withholding automatically
> 3. **Given** deduction configured as percentage, **When** multiple claims exist under case, **Then** system applies deduction proportionally to all applicable claims
> 4. **Given** absence reason is modified on 'Open' case, **When** update is saved, **Then** system triggers re-adjudication and recalculates gross benefit amounts
> 5. **Given** YTD earnings are updated, **When** existing payments exist, **Then** system recalculates all affected payment allocations
> 6. **Given** case status is 'Incomplete', **When** financial adjustments are saved, **Then** system submits case and executes automated eligibility evaluation


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=585307910"
> ]

---

#### Feature: As a Claims Adjuster, I want to manage party information, occupation class, preferred payment method, and payment frequency, so that claim payments are directed correctly and processed according to claimant preferences
- **Role**: Claim Adjuster
- **Action**: manage party information, occupation class, preferred payment method, and payment frequency during absence case lifecycle
- **Value**: claim payments are directed correctly, processed according to claimant preferences, and aligned with policy requirements

**Description:**

> As a **Claim Adjuster**,
> I want to **manage party information, occupation class, preferred payment method, and payment frequency during absence case lifecycle**,
> So that **claim payments are directed correctly, processed according to claimant preferences, and aligned with policy requirements**


**Key Capabilities:**

> 1. User accesses absence cases with 'Incomplete' or 'Open' status for data adjustment activities
> 2. User updates party details, occupation classification, payment method preferences, and payment frequency in ad-hoc manner
> 3. System updates absence case data and submits case for re-adjudication when applicable
> 4. System re-evaluates case applicability, recalculates eligibility, and determines gross benefit amounts
>     4.1 Upon certain data changes, system creates new claim types if not already existing
>     4.2 System recalculates payment allocations when financially impactful data is modified
> 5. System preserves existing claims even when case applicability changes post-adjustment


**Acceptance Criteria:**

> 1. **Given** absence case status is 'Incomplete' or 'Open', **When** adjuster updates party or payment configuration data, **Then** system accepts changes and updates case records
> 2. **Given** payment-impacting data is modified, **When** system processes the update, **Then** system automatically recalculates payment allocations and benefit amounts
> 3. **Given** occupation class or absence reason changes, **When** system completes data update, **Then** system triggers re-adjudication and evaluates case applicability for claim types
> 4. **Given** new claim types become applicable, **When** re-adjudication completes, **Then** system creates applicable claims not previously existing
> 5. **Given** case status is 'Closed', **When** adjuster attempts data adjustment, **Then** system prevents modification and notifies adjuster of status restriction


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=585308318"
> ]

---

#### Feature: As a Claims Operations Manager, I want the system to automatically recalculate payments when financial or absence data is updated, so that payment amounts remain accurate without manual intervention
- **Role**: Claim Adjuster
- **Action**: automatically recalculate payments when financial or absence data is updated during case maintenance
- **Value**: payment amounts remain accurate and compliant without manual intervention, reducing errors and processing time

**Description:**

> As a **Claim Adjuster**,
> I want to **automatically recalculate payments when financial or absence data is updated during case maintenance**,
> So that **payment amounts remain accurate and compliant without manual intervention, reducing errors and processing time**


**Key Capabilities:**

> 1. System validates absence case is in 'Open' or 'Incomplete' status before allowing financial adjustments
> 2. User performs ad-hoc financial maintenance activities including tax withholdings, deductions, YTD earnings, absence reasons, work schedules, and payment preferences
>     2.1 When absence reason is modified, system triggers automated re-adjudication based on case status
>     2.2 System applies date-based logic for withholdings and deductions (flat amount or percentage)
> 3. System automatically updates event case data and triggers finalization processes
> 4. System recalculates existing payment allocations based on updated tax withholdings and deductions, applying proration rules
> 5. Upon completion, updated payments reflect current financial parameters without manual recalculation


**Acceptance Criteria:**

> 1. **Given** an absence case in 'Open' status, **When** user updates tax withholding percentage, **Then** system recalculates all affected payment allocations matching the effective date range
> 2. **Given** existing scheduled payments, **When** user adds new deductions with from/through dates, **Then** system applies deductions to overlapping payment periods with correct pre/post-tax treatment
> 3. **Given** user modifies absence reason, **When** case status is 'Incomplete', **Then** system submits case and executes re-adjudication creating applicable claim types
> 4. **Given** YTD earnings are updated, **When** finalization occurs, **Then** system prevents payment submission until recalculation completes successfully
> 5. **Given** absence case status is 'Closed', **When** user attempts financial adjustment, **Then** system prevents modification and notifies user of status constraint


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=585307910"
> ]

---

#### Feature: As a Claims Operations Manager, I want the system to automatically re-adjudicate absence cases and create applicable claim types when absence data is updated, so that all eligible claims are generated without manual intervention
- **Role**: Claim Manager
- **Action**: enable automatic re-adjudication of absence cases and creation of applicable claim types when absence data is updated
- **Value**: all eligible claims are generated without manual intervention, ensuring accurate benefits allocation and reducing processing time

**Description:**

> As a **Claim Manager**,
> I want to **enable automatic re-adjudication of absence cases and creation of applicable claim types when absence data is updated**,
> So that **all eligible claims are generated without manual intervention, ensuring accurate benefits allocation and reducing processing time**


**Key Capabilities:**

> 1. Upon modification of absence-related data (reasons, dates, earnings, participant information), system validates case status is 'Incomplete' or 'Open'
> 2. System automatically evaluates case applicability against all available claim types based on updated absence criteria
> 3. System calculates eligibility and gross benefit amounts for newly applicable claim types
> 4. System creates new claims for applicable types not previously generated
>     4.1 When absence reason changes and case status is 'Incomplete', system auto-submits case
> 5. System recalculates payment allocations when tax withholdings or deductions are modified
> 6. System preserves existing claims even when case becomes ineligible for those claim types


**Acceptance Criteria:**

> 1. **Given** absence case in 'Open' status, **When** absence reason is updated, **Then** system re-adjudicates case and creates newly applicable claim types automatically
> 2. **Given** case status is 'Incomplete', **When** critical absence data changes, **Then** system transitions case to 'Open' and completes adjudication
> 3. **Given** tax withholdings updated, **When** payment dates overlap with withholding periods, **Then** system recalculates payment amounts with prorated withholdings
> 4. **Given** case becomes ineligible for existing claim type, **When** re-adjudication completes, **Then** system retains original claims without deletion
> 5. **Given** case in 'Closed' status, **When** user attempts data modification, **Then** system prevents adjustment process
> 6. **Given** multiple data adjustments performed, **When** any trigger re-adjudication, **Then** system executes only one comprehensive adjudication cycle


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=585308318"
> ]

---

#### Feature: As a Claims Adjuster, I want to generate documents on demand by selecting templates, prefilling data, and customizing content before sending, so that I can create accurate correspondence with claimants
- **Role**: Claim Adjuster
- **Action**: generate and customize claim-related documents using templates with automated data prefill, validate content completeness, and deliver correspondence through selected channels
- **Value**: I can produce accurate, compliant documentation efficiently and communicate with claimants through appropriate delivery methods while maintaining audit trails

**Description:**

> As a **Claim Adjuster**,
> I want to **generate and customize claim-related documents using templates with automated data prefill, validate content completeness, and deliver correspondence through selected channels**,
> So that **I can produce accurate, compliant documentation efficiently and communicate with claimants through appropriate delivery methods while maintaining audit trails**


**Key Capabilities:**

> 1. User initiates on-demand document generation and selects appropriate template for claim correspondence
> 2. System validates preconditions and automatically prefills available claim data into selected template
> 3. User customizes document by selecting payee, entity, delivery method, and modifying structured or free-text content as needed
>     3.1 Upon mandatory fields missing, system prevents progression until requirements are satisfied
> 4. User reviews generated document preview and confirms final generation
> 5. System validates document structure, creates final version, and associates with claim entity in electronic folder
> 6. System delivers document through selected channel and notifies user upon successful transmission


**Acceptance Criteria:**

> 1. **Given** adjuster initiates document generation, **When** preconditions are unmet, **Then** system blocks generation and communicates requirements
> 2. **Given** template selection, **When** claim data exists, **Then** system automatically populates all available fields without manual entry
> 3. **Given** document preview, **When** mandatory fields are incomplete, **Then** system prevents finalization until all required data is provided
> 4. **Given** document finalization, **When** user confirms generation, **Then** system creates document, stores in electronic folder, and links to claim entity
> 5. **Given** email delivery method selected, **When** document is generated, **Then** system transmits via email and notifies user of successful delivery
> 6. **Given** approval workflow configured, **When** triggered generation occurs, **Then** system routes to approver before final document creation


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=644471273"
> ]

---

#### Feature: As a Claims Adjuster, I want to automatically generate and deliver documents based on claim events with approval workflows, so that timely correspondence is sent to claimants without manual generation
- **Role**: Claim Adjuster
- **Action**: automatically generate and deliver documents based on claim events with approval workflows
- **Value**: timely correspondence is sent to claimants without manual generation, reducing processing time and ensuring consistent communication

**Description:**

> As a **Claim Adjuster**,
> I want to **automatically generate and deliver documents based on claim events with approval workflows**,
> So that **timely correspondence is sent to claimants without manual generation, reducing processing time and ensuring consistent communication**


**Key Capabilities:**

> 1. Upon claim event trigger, system initiates automated document generation process
> 2. System stores generated document in electronic folder for record management
> 3. When approval is required, system creates task and routes to designated approver
> 4. User is able to preview and review document content before finalizing decision
> 5. Upon rejection, system generates review task and regenerates document incorporating feedback, repeating approval cycle
> 6. When approved, system delivers document via configured method and notifies user of successful transmission


**Acceptance Criteria:**

> 1. **Given** a qualifying claim event occurs, **When** trigger activates, **Then** system automatically generates appropriate document without manual intervention
> 2. **Given** approval workflow is configured, **When** document is generated, **Then** system routes to designated approver and prevents delivery until approved
> 3. **Given** document is rejected, **When** feedback is provided, **Then** system regenerates document and restarts approval cycle
> 4. **Given** document is approved, **When** email delivery is selected, **Then** system transmits document and confirms delivery to user
> 5. **Given** document workflow completes, **When** finalized, **Then** system stores document in electronic folder with audit trail
> 6. **Given** incomplete or missing data, **When** generation attempts, **Then** system prevents document creation and notifies user of data requirements


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=644471284"
> ]

---

#### Feature: As a Claims Operations Manager, I want the system to automatically process payments and close claims when auto-adjudication criteria are met, so that eligible claims are paid and closed efficiently
- **Role**: Claim Adjuster
- **Action**: automatically adjudicate, generate payments, and close claims that meet predefined eligibility criteria without manual intervention
- **Value**: eligible claims are processed and closed efficiently, reducing operational costs and accelerating payment delivery to claimants

**Description:**

> As a **Claim Adjuster**,
> I want to **automatically adjudicate, generate payments, and close claims that meet predefined eligibility criteria without manual intervention**,
> So that **eligible claims are processed and closed efficiently, reducing operational costs and accelerating payment delivery to claimants**


**Key Capabilities:**

> 1. System evaluates submitted claim against configured auto-adjudication eligibility criteria
> 2. Upon successful validation, system automatically calculates and generates payment amounts based on policy terms and coverage rules
> 3. System initiates payment processing workflow and updates claim financial status
> 4. When payment is confirmed, system automatically generates closure documentation and notifications
> 5. System transitions claim to closed status and archives case records
>     5.1 If auto-adjudication criteria are not met, system routes claim to manual adjudication queue
>     5.2 If payment processing fails, system suspends closure and triggers exception handling


**Acceptance Criteria:**

> 1. **Given** a claim meets all auto-adjudication criteria, **When** the system evaluates it, **Then** payment is generated without manual intervention
> 2. **Given** payment is successfully processed, **When** funds are confirmed, **Then** claim automatically transitions to closed status
> 3. **Given** a claim does not satisfy eligibility rules, **When** auto-adjudication is attempted, **Then** system routes to manual review queue
> 4. **Given** payment processing encounters errors, **When** failure is detected, **Then** system prevents claim closure and notifies appropriate personnel
> 5. **Given** claim is auto-closed, **When** closure completes, **Then** system generates closure documentation and updates all stakeholders


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=483306501"
> ]

---

#### Feature: As a Claims Adjuster, I want to manage the transition of Short-Term Disability claims to Long-Term Disability claims, so that continuous benefits are maintained when eligibility criteria are met
- **Role**: Claim Adjuster
- **Action**: orchestrate the transition of Short-Term Disability claims to Long-Term Disability claims when eligibility thresholds are reached
- **Value**: continuous benefit coverage is maintained without interruption and claimants experience seamless support during extended disability periods

**Description:**

> As a **Claim Adjuster**,
> I want to **orchestrate the transition of Short-Term Disability claims to Long-Term Disability claims when eligibility thresholds are reached**,
> So that **continuous benefit coverage is maintained without interruption and claimants experience seamless support during extended disability periods**.


**Key Capabilities:**

> 1. System monitors approaching STD benefit exhaustion dates and evaluates transition eligibility criteria against policy terms
> 2. Adjuster initiates transition assessment workflow when duration thresholds or medical milestones indicate LTD qualification
>     2.1 System validates continuation of disability status and benefit entitlement
>     2.2 Upon eligibility confirmation, system preserves claim history and case documentation
> 3. System establishes new LTD claim record with inherited data elements while maintaining linkage to original STD claim
> 4. Adjuster reviews and approves benefit recalculation based on LTD policy provisions and updated financial parameters
> 5. System triggers benefit payment adjustments and generates transition notifications to stakeholders
> 6. If transition is denied, system documents rationale and initiates closure procedures for STD claim


**Acceptance Criteria:**

> 1. **Given** STD claim approaches maximum benefit period, **When** eligibility criteria are satisfied, **Then** system initiates transition workflow and notifies adjuster for review
> 2. **Given** transition is approved, **When** LTD claim is created, **Then** all relevant claim data, documentation, and historical context are preserved and linked
> 3. **Given** benefit calculations differ between STD and LTD, **When** transition occurs, **Then** system recalculates payments per LTD policy terms without manual intervention
> 4. **Given** transition assessment is complete, **When** decision is finalized, **Then** system prevents benefit payment gaps and updates stakeholder notifications
> 5. **Given** eligibility requirements are not met, **When** transition is denied, **Then** system documents denial rationale and processes STD claim closure appropriately


**Reference URLs:**

> [
>   "https://wiki.eisgroup.com/pages/viewpage.action?pageId=483306501"
> ]

---
