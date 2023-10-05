# Handles the definition of the HL7 segments
class hl7Segment(object):
	def __init__(self, code, description, fields):
		self.code = code
		self.description = description
		self.fields = fields

	# Gets a segment object based on his code. If no object is found in the segmentList with the following code None is returned.
	def getSegmentByCode(self, code, segmentList):
		for listItem in segmentList:
			if (listItem.code == code):
				return listItem
		return None

	# Loads the entire segment list
	def loadSegmentList(self):
		hl7SegmentList = []
		
		hl7SegmentList.append(hl7Segment("ACC", "Accident segment", {
		    "fields": [
		        "Accident Date/Time",
		        "Accident Code",
		        "Accident Location",
		        "Auto Accident State",
		        "Accident Job Related Indicator",
		        "Accident Death Indicator"
		    ]
		}))
		hl7SegmentList.append(hl7Segment("ADD", "Addendum segment", {
		    "fields": [
		        "Addendum Continuation Pointer"
		    ]
		}))
		hl7SegmentList.append(hl7Segment("AIG", "Appointment information - general resource segment", {
		    "fields": [
		        "Set ID - AIG",
		        "Segment Action Code",
		        "Resource ID",
		        "Resource Type",
		        "Resource Group",
		        "Resource Quantity",
		        "Resource Quantity Units",
		        "Start Date/Time",
		        "Start Date/Time Offset",
		        "Start Date/Time Offset Units",
		        "Duration",
		        "Duration Units",
		        "Allow Substitution Code",
		        "Filler Status Code"
		    ]
		}))
		hl7SegmentList.append(hl7Segment("AIL", "Appointment information - location resource segment", {
		    "fields": [
		        "Set ID - AIL",
		        "Segment Action Code",
		        "Location Resource ID",
		        "Location Type-AIL",
		        "Location Group",
		        "Start Date/Time",
		        "Start Date/Time Offset",
		        "Start Date/Time Offset Units",
		        "Duration",
		        "Duration Units",
		        "Allow Substitution Code",
		        "Filler Status Code"
		    ]
		}))
		hl7SegmentList.append(hl7Segment("AIP", "Appointment information - personnel resource segment", {
		    "fields": [
		        "Set ID - AIP",
		        "Segment Action Code",
		        "Personnel Resource ID",
		        "Resource Role",
		        "Resource Group",
		        "Start Date/Time",
		        "Start Date/Time Offset",
		        "Start Date/Time Offset Units",
		        "Duration",
		        "Duration Units",
		        "Allow Substitution Code",
		        "Filler Status Code"
		    ]
		}))
		hl7SegmentList.append(hl7Segment("AIS", "Appointment information - service segment", {
		    "fields": [
		        "Set ID - AIS",
		        "Segment Action Code",
		        "Universal Service ID",
		        "Start Date/Time",
		        "Start Date/Time Offset",
		        "Start Date/Time Offset Units",
		        "Duration",
		        "Duration Units",
		        "Allow Substitution Code",
		        "Filler Status Code"
		    ]
		}))
		hl7SegmentList.append(hl7Segment("AL1", "Patient allergy information segment", {
		    "fields": [
		        "Set ID - AL1",
		        "Allergy Type",
		        "Allergy Code/Mnemonic/Description",
		        "Allergy Severity",
		        "Allergy Reaction",
		        "Identification Date"
		    ]
		}))
		hl7SegmentList.append(hl7Segment("APR", "Appointment preferences segment", {
		    "fields": [
		        "Time Selection Criteria",
		        "Resource Selection Criteria",
		        "Location Selection Criteria",
		        "Slot Spacing Criteria",
		        "Filler Override Criteria"
		    ]
		}))
		hl7SegmentList.append(hl7Segment("ARQ", "Appointment request segment", {
		    "fields": [
		        "Placer Appointment ID",
		        "Filler Appointment ID",
		        "Occurrence Number",
		        "Placer Group Number",
		        "Schedule ID",
		        "Request Event Reason",
		        "Appointment Reason",
		        "Appointment Type",
		        "Appointment Duration",
		        "Appointment Duration Units",
		        "Requested Start Date/Time Range",
		        "Priority-ARQ",
		        "Repeating Interval",
		        "Repeating Interval Duration",
		        "Placer Contact Person",
		        "Placer Contact Phone Number",
		        "Placer Contact Address",
		        "Placer Contact Location",
		        "Entered by Person",
		        "Entered by Phone Number",
		        "Entered by Location",
		        "Parent Placer Appointment ID",
		        "Parent Filler Appointment ID"
		    ]
		}))
		hl7SegmentList.append(hl7Segment("AUT", "Authorization Information", {
		    "fields": [
		        "Authorizing Payor, Plan ID",
		        "Authorizing Payor, Company ID",
		        "Authorizing Payor, Company Name",
		        "Authorization Effective Date",
		        "Authorization Expiration Date",
		        "Authorization Identifier",
		        "Reimbursement Limit",
		        "Requested Number of Treatments",
		        "Authorized Number of Treatments",
		        "Process Date"
		    ]
		}))
		hl7SegmentList.append(hl7Segment("BHS", "Batch header segment", {
		    "fields": [
		        "Batch Field Separator",
		        "Batch Encoding Characters",
		        "Batch Sending Application",
		        "Batch Sending Facility",
		        "Batch Receiving Application",
		        "Batch Receiving Facility",
		        "Batch Creation Date/Time",
		        "Batch Security",
		        "Batch Name/ID/Type",
		        "Batch Comment",
		        "Batch Control ID",
		        "Reference Batch Control ID"
		    ]
		}))
		hl7SegmentList.append(hl7Segment("BLG", "Billing segment", {
		    "fields": [
		        "When to Charge",
		        "Charge Type",
		        "Account ID"
		    ]
		}))
		hl7SegmentList.append(hl7Segment("BTS", "Batch trailer segment", {
		    "fields": [
		        "Batch Message Count",
		        "Batch Comment",
		        "Batch Totals"
		    ]
		}))
		hl7SegmentList.append(hl7Segment("CDM", "Charge description master segment", {
		    "fields": [
		        "Primary Key Value - CDM",
		        "Charge Code Alias",
		        "Charge Description Short",
		        "Charge Description Long",
		        "Description Override Indicator",
		        "Exploding Charges",
		        "Procedure Code",
		        "Active/Inactive Flag",
		        "Inventory Number",
		        "Resource Load",
		        "Contract Number",
		        "Contract Organization",
		        "Room Fee Indicator"
		    ]
		}))
		hl7SegmentList.append(hl7Segment("CM0", "Clinical study master segment", {
		    "fields": [
		        "Set ID - CM0",
		        "Sponsor Study ID",
		        "Alternate Study ID",
		        "Title of Study",
		        "Chairman of Study",
		        "Last IRB Approval Date",
		        "Total Accrual to Date",
		        "Last Accrual Date",
		        "Contact for Study",
		        "Contact's Tel. Number",
		        "Contact's Address"
		    ]
		}))
		hl7SegmentList.append(hl7Segment("CM1", "Clinical study phase master segment", {
		    "fields": [
		        "Set ID - CM1",
		        "Study Phase Identifier",
		        "Description of Study Phase"
		    ]
		}))
		hl7SegmentList.append(hl7Segment("CM2", "Clinical study schedule master segment", {
		    "fields": [
		        "Set ID - CM2",
		        "Scheduled Time Point",
		        "Description of Time Point",
		        "Events Scheduled This Time Point"
		    ]
		}))
		hl7SegmentList.append(hl7Segment("CSP", "Clinical study phase segment", {
		    "fields": [
		        "Study Phase Identifier",
		        "Date/time Study Phase Began",
		        "Date/time Study Phase Ended",
		        "Study Phase Evaluability"
		    ]
		}))
		hl7SegmentList.append(hl7Segment("CSR", "Clinical study registration segment", {
		    "fields": [
		        "Sponsor Study ID",
		        "Alternate Study ID",
		        "Institution Registering the Patient",
		        "Sponsor Patient ID",
		        "Alternate Patient ID - CSR",
		        "Date/Time Of Patient Study Registration",
		        "Person Performing Study Registration",
		        "Study Authorizing Provider",
		        "Date/time Patient Study Consent Signed",
		        "Patient Study Eligibility Status",
		        "Study Randomization Date/time",
		        "Randomized Study Arm",
		        "Stratum for Study Randomization",
		        "Patient Evaluability Status",
		        "Date/time Ended Study",
		        "Reason Ended Study"
		    ]
		}))
		hl7SegmentList.append(hl7Segment("CSS", "Clinical study data schedule segment", {
		    "fields": [
		        "Study Scheduled Time Point",
		        "Study Scheduled Patient Time Point",
		        "Study Quality Control Codes"
		    ]
		}))
		hl7SegmentList.append(hl7Segment("CTD", "Contact Data", {
		    "fields": [
		        "Contact Role",
		        "Contact Name",
		        "Contact Address",
		        "Contact Location",
		        "Contact Communication Information",
		        "Preferred Method Of Contact",
		        "Contact Identifiers"
		    ]
		}))
		hl7SegmentList.append(hl7Segment("CTI", "Clinical trial identification segment", {
		    "fields": [
		        "Sponsor Study ID",
		        "Study Phase Identifier",
		        "Study Scheduled Time Point"
		    ]
		}))
		hl7SegmentList.append(hl7Segment("DB1", "Disability segment", {
		    "fields": [
		        "Set ID - DB1",
		        "Disabled Person Code",
		        "Disabled Person Identifier",
		        "Disabled Indicator",
		        "Disability Start Date",
		        "Disability End Date",
		        "Disability Return to Work Date",
		        "Disability Unable to Work Date"
		    ]
		}))
		hl7SegmentList.append(hl7Segment("DG1", "Diagnosis segment", {
		    "fields": [
		        "Set ID - DG1",
		        "Diagnosis Coding Method",
		        "Diagnosis Code - DG1",
		        "Diagnosis Description",
		        "Diagnosis Date/Time",
		        "Diagnosis Type",
		        "Major Diagnostic Category",
		        "Diagnostic Related Group",
		        "DRG Approval Indicator",
		        "DRG Grouper Review Code",
		        "Outlier Type",
		        "Outlier Days",
		        "Outlier Cost",
		        "Grouper Version And Type",
		        "Diagnosis Priority",
		        "Diagnosing Clinician",
		        "Diagnosis Classification",
		        "Confidential Indicator",
		        "Attestation Date/Time"
		    ]
		}))
		hl7SegmentList.append(hl7Segment("DRG", "Diagnosis related group segment", {
		    "fields": [
		        "Diagnostic Related Group",
		        "DRG Assigned Date/Time",
		        "DRG Approval Indicator",
		        "DRG Grouper Review Code",
		        "Outlier Type",
		        "Outlier Days",
		        "Outlier Cost",
		        "DRG Payor",
		        "Outlier Reimbursement",
		        "Confidential Indicator"
		    ]
		}))
		hl7SegmentList.append(hl7Segment("DSC", "Continuation pointer segment", {
		    "fields": [
		        "Continuation Pointer"
		    ]
		}))
		hl7SegmentList.append(hl7Segment("DSP", "Display data segment", {
		    "fields": [
		        "Set ID - DSP",
		        "Display Level",
		        "Data Line",
		        "Logical Break Point",
		        "Result ID"
		    ]
		}))
		hl7SegmentList.append(hl7Segment("EQL", "Embedded query language segment", {
		    "fields": [
		        "Query Tag",
		        "Query/ Response Format Code",
		        "EQL  Query Name",
		        "EQL  Query Statement"
		    ]
		}))
		hl7SegmentList.append(hl7Segment("ERQ", "Event replay query segment", {
		    "fields": [
		        "Query Tag",
		        "Event Identifier",
		        "Input Parameter List"
		    ]
		}))
		hl7SegmentList.append(hl7Segment("ERR", "Error segment", {
		    "fields": [
		        "Error Code and Location"
		    ]
		}))
		hl7SegmentList.append(hl7Segment("EVN", "Event type segment", {
		    "fields": [
		        "Event Type Code",
		        "Recorded Date/Time",
		        "Date/Time Planned Event",
		        "Event Reason Code",
		        "Operator ID",
		        "Event Occurred"
		    ]
		}))
		hl7SegmentList.append(hl7Segment("FAC", "Facility segment", {
		    "fields": [
		        "Facility ID-FAC",
		        "Facility Type",
		        "Facility Address",
		        "Facility Telecommunication",
		        "Contact Person",
		        "Contact Title",
		        "Contact Address",
		        "Contact Telecommunication",
		        "Signature Authority",
		        "Signature Authority Title",
		        "Signature Authority Address",
		        "Signature Authority Telecommunication"
		    ]
		}))
		hl7SegmentList.append(hl7Segment("FHS", "File header segment", {
		    "fields": [
		        "File Field Separator",
		        "File Encoding Characters",
		        "File Sending Application",
		        "File Sending Facility",
		        "File Receiving Application",
		        "File Receiving Facility",
		        "File Creation Date/Time",
		        "File Security",
		        "File Name/ID",
		        "File Header Comment",
		        "File Control ID",
		        "Reference File Control ID"
		    ]
		}))
		hl7SegmentList.append(hl7Segment("FT1", "Financial transaction segment", {
		    "fields": [
		        "Set ID - FT1",
		        "Transaction ID",
		        "Transaction Batch ID",
		        "Transaction Date",
		        "Transaction Posting Date",
		        "Transaction Type",
		        "Transaction Code",
		        "Transaction Description",
		        "Transaction Description - Alt",
		        "Transaction Quantity",
		        "Transaction Amount - Extended",
		        "Transaction Amount - Unit",
		        "Department Code",
		        "Insurance Plan ID",
		        "Insurance Amount",
		        "Assigned Patient Location",
		        "Fee Schedule",
		        "Patient Type",
		        "Diagnosis Code - FT1",
		        "Performed By Code",
		        "Ordered By Code",
		        "Unit Cost",
		        "Filler Order Number",
		        "Entered By Code",
		        "Procedure Code",
		        "Procedure Code Modifier"
		    ]
		}))
		hl7SegmentList.append(hl7Segment("FTS", "File trailer segment", {
		    "fields": [
		        "File Batch Count",
		        "File Trailer Comment"
		    ]
		}))
		hl7SegmentList.append(hl7Segment("GOL", "Goal Detail", {
		    "fields": [
		        "Action Code",
		        "Action Date/Time",
		        "Goal ID",
		        "Goal Instance ID",
		        "Episode of Care ID",
		        "Goal List Priority",
		        "Goal Established Date/Time",
		        "Expected Goal Achieve Date/Time",
		        "Goal Classification",
		        "Goal Management Discipline",
		        "Current Goal Review Status",
		        "Current Goal Review Date/Time",
		        "Next Goal Review Date/Time",
		        "Previous Goal Review Date/Time",
		        "Goal Review Interval",
		        "Goal Evaluation",
		        "Goal Evaluation Comment",
		        "Goal Life Cycle Status",
		        "Goal Life Cycle Status Date/Time",
		        "Goal Target Type",
		        "Goal Target Name"
		    ]
		}))
		hl7SegmentList.append(hl7Segment("GT1", "Guarantor segment", {
		    "fields": [
		        "Set ID - GT1",
		        "Guarantor Number",
		        "Guarantor Name",
		        "Guarantor Spouse Name",
		        "Guarantor Address",
		        "Guarantor Ph Num-Home",
		        "Guarantor Ph Num-Business",
		        "Guarantor Date/Time Of Birth",
		        "Guarantor Sex",
		        "Guarantor Type",
		        "Guarantor Relationship",
		        "Guarantor SSN",
		        "Guarantor Date - Begin",
		        "Guarantor Date - End",
		        "Guarantor Priority",
		        "Guarantor Employer Name",
		        "Guarantor Employer Address",
		        "Guarantor Employer Phone Number",
		        "Guarantor Employee ID Number",
		        "Guarantor Employment Status",
		        "Guarantor Organization Name",
		        "Guarantor Billing Hold Flag",
		        "Guarantor Credit Rating Code",
		        "Guarantor Death Date And Time",
		        "Guarantor Death Flag",
		        "Guarantor Charge Adjustment Code",
		        "Guarantor Household Annual Income",
		        "Guarantor Household Size",
		        "Guarantor Employer ID Number",
		        "Guarantor Marital Status Code",
		        "Guarantor Hire Effective Date",
		        "Employment Stop Date",
		        "Living Dependency",
		        "Ambulatory Status",
		        "Citizenship",
		        "Primary Language",
		        "Living Arrangement",
		        "Publicity Code",
		        "Protection Indicator",
		        "Student Indicator",
		        "Religion",
		        "Mother s Maiden Name",
		        "Nationality",
		        "Ethnic Group",
		        "Contact Person s Name",
		        "Contact Person s Telephone Number",
		        "Contact Reason",
		        "Contact Relationship",
		        "Job Title",
		        "Job Code/Class",
		        "Guarantor Employer s Organization Name",
		        "Handicap",
		        "Job Status",
		        "Guarantor Financial Class",
		        "Guarantor Race"
		    ]
		}))
		hl7SegmentList.append(hl7Segment("IAM", "Patient adverse reaction information - unique iden", {
		    "fields": [
		        "Set ID - IAM",
		        "Allergen Type Code",
		        "Allergen Code/Mnemonic/Description",
		        "Allergy Severity Code",
		        "Allergy Reaction Code",
		        "Allergy Action Code",
		        "Allergy Unique Identifier",
		        "Action Reason",
		        "Sensitivity to Causative Agent Code",
		        "Allergen Group Code/Mnemonic/Description",
		        "Onset Date",
		        "Onset Date Text",
		        "Reported Date/Time",
		        "Reported By",
		        "Relationship to Patient Code",
		        "Alert Device Code",
		        "Allergy Clinical Status Code",
		        "Statused by Person",
		        "Statused by Organization",
		        "Statused at Date/Time"
		    ]
		}))
		hl7SegmentList.append(hl7Segment("IN1", "Insurance segment", {
		    "fields": [
		        "Set ID - IN1",
		        "Insurance Plan ID",
		        "Insurance Company ID",
		        "Insurance Company Name",
		        "Insurance Company Address",
		        "Insurance Co Contact Person",
		        "Insurance Co Phone Number",
		        "Group Number",
		        "Group Name",
		        "Insured s Group Emp ID",
		        "Insured s Group Emp Name",
		        "Plan Effective Date",
		        "Plan Expiration Date",
		        "Authorization Information",
		        "Plan Type",
		        "Name Of Insured",
		        "Insured s Relationship To Patient",
		        "Insured s Date Of Birth",
		        "Insured s Address",
		        "Assignment Of Benefits",
		        "Coordination Of Benefits",
		        "Coord Of Ben. Priority",
		        "Notice Of Admission Flag",
		        "Notice Of Admission Date",
		        "Report Of Eligibility Flag",
		        "Report Of Eligibility Date",
		        "Release Information Code",
		        "Pre-Admit Cert",
		        "Verification Date/Time",
		        "Verification By",
		        "Type Of Agreement Code",
		        "Billing Status",
		        "Lifetime Reserve Days",
		        "Delay Before L.R. Day",
		        "Company Plan Code",
		        "Policy Number",
		        "Policy Deductible",
		        "Policy Limit - Amount",
		        "Policy Limit - Days",
		        "Room Rate - Semi-Private",
		        "Room Rate - Private",
		        "Insured s Employment Status",
		        "Insured s Sex",
		        "Insured s Employer s Address",
		        "Verification Status",
		        "Prior Insurance Plan ID",
		        "Coverage Type",
		        "Handicap",
		        "Insured s ID Number"
		    ]
		}))
		hl7SegmentList.append(hl7Segment("IN2", "Insurance additional information segment", {
		    "fields": [
		        "Insured s Employee ID",
		        "Insured s Social Security Number",
		        "Insured s Employer s Name and ID",
		        "Employer Information Data",
		        "Mail Claim Party",
		        "Medicare Health Ins Card Number",
		        "Medicaid Case Name",
		        "Medicaid Case Number",
		        "Military Sponsor Name",
		        "Military ID Number",
		        "Dependent Of Military Recipient",
		        "Military Organization",
		        "Military Station",
		        "Military Service",
		        "Military Rank/Grade",
		        "Military Status",
		        "Military Retire Date",
		        "Military Non-Avail Cert On File",
		        "Baby Coverage",
		        "Combine Baby Bill",
		        "Blood Deductible",
		        "Special Coverage Approval Name",
		        "Special Coverage Approval Title",
		        "Non-Covered Insurance Code",
		        "Payor ID",
		        "Payor Subscriber ID",
		        "Eligibility Source",
		        "Room Coverage Type/Amount",
		        "Policy Type/Amount",
		        "Daily Deductible",
		        "Living Dependency",
		        "Ambulatory Status",
		        "Citizenship",
		        "Primary Language",
		        "Living Arrangement",
		        "Publicity Code",
		        "Protection Indicator",
		        "Student Indicator",
		        "Religion",
		        "Mother s Maiden Name",
		        "Nationality",
		        "Ethnic Group",
		        "Marital Status",
		        "Insured s Employment Start Date",
		        "Employment Stop Date",
		        "Job Title",
		        "Job Code/Class",
		        "Job Status",
		        "Employer Contact Person Name",
		        "Employer Contact Person Phone Number",
		        "Employer Contact Reason",
		        "Insured s Contact Person s Name",
		        "Insured s Contact Person Phone Number",
		        "Insured s Contact Person Reason",
		        "Relationship To The Patient Start Date",
		        "Relationship To The Patient Stop Date",
		        "Insurance Co. Contact Reason",
		        "Insurance Co Contact Phone Number",
		        "Policy Scope",
		        "Policy Source",
		        "Patient Member Number",
		        "Guarantor s Relationship To Insured",
		        "Insured s Phone Number - Home",
		        "Insured s Employer Phone Number",
		        "Military Handicapped Program",
		        "Suspend Flag",
		        "Copay Limit Flag",
		        "Stoploss Limit Flag",
		        "Insured Organization Name And ID",
		        "Insured Employer Organization Name And ID",
		        "Race",
		        "HCFA Patient s Relationship to Insured"
		    ]
		}))
		hl7SegmentList.append(hl7Segment("IN3", "Insurance additional information, certification segment", {
		    "fields": [
		        "Set ID - IN3",
		        "Certification Number",
		        "Certified By",
		        "Certification Required",
		        "Penalty",
		        "Certification Date/Time",
		        "Certification Modify Date/Time",
		        "Operator",
		        "Certification Begin Date",
		        "Certification End Date",
		        "Days",
		        "Non-Concur Code/Description",
		        "Non-Concur Effective Date/Time",
		        "Physician Reviewer",
		        "Certification Contact",
		        "Certification Contact Phone Number",
		        "Appeal Reason",
		        "Certification Agency",
		        "Certification Agency Phone Number",
		        "Pre-Certification Req/Window",
		        "Case Manager",
		        "Second Opinion Date",
		        "Second Opinion Status",
		        "Second Opinion Documentation Received",
		        "Second Opinion Physician"
		    ]
		}))
		hl7SegmentList.append(hl7Segment("LCC", "Location charge code segment", {
		    "fields": [
		        "Primary Key Value - LCC",
		        "Location Department",
		        "Accommodation Type",
		        "Charge Code"
		    ]
		}))
		hl7SegmentList.append(hl7Segment("LCH", "Location characteristic segment", {
		    "fields": [
		        "Primary Key Value - LCH",
		        "Segment Action Code",
		        "Segment Unique Key",
		        "Location Characteristic ID",
		        "Location Characteristic Value"
		    ]
		}))
		hl7SegmentList.append(hl7Segment("LDP", "Location department segment", {
		    "fields": [
		        "Primary Key Value - LDP",
		        "Location Department",
		        "Location Service",
		        "Specialty Type",
		        "Valid Patient Classes",
		        "Active/Inactive Flag",
		        "Activation Date  LDP",
		        "Inactivation Date - LDP",
		        "Inactivated Reason",
		        "Visiting Hours",
		        "Contact Phone"
		    ]
		}))
		hl7SegmentList.append(hl7Segment("LOC", "Location identification segment", {
		    "fields": [
		        "Primary Key Value - LOC",
		        "Location Description",
		        "Location Type - LOC",
		        "Organization Name - LOC",
		        "Location Address",
		        "Location Phone",
		        "License Number",
		        "Location Equipment"
		    ]
		}))
		hl7SegmentList.append(hl7Segment("LRL", "Location relationship segment", {
		    "fields": [
		        "Primary Key Value - LRL",
		        "Segment Action Code",
		        "Segment Unique Key",
		        "Location Relationship ID",
		        "Organizational Location Relationship Value",
		        "Patient Location Relationship Value"
		    ]
		}))
		hl7SegmentList.append(hl7Segment("MFA", "Master file acknowledgment segment", {
		    "fields": [
		        "Record-Level Event Code",
		        "MFN Control ID",
		        "Event Completion Date/Time",
		        "MFN Record Level Error Return",
		        "Primary Key Value   MFA",
		        "Primary Key Value Type - MFA"
		    ]
		}))
		hl7SegmentList.append(hl7Segment("MFE", "Master file entry segment", {
		    "fields": [
		        "Record-Level Event Code",
		        "MFN Control ID",
		        "Effective Date/Time",
		        "Primary Key Value - MFE",
		        "Primary Key Value Type"
		    ]
		}))
		hl7SegmentList.append(hl7Segment("MFI", "Master file identification segment", {
		    "fields": [
		        "Master File Identifier",
		        "Master File Application Identifier",
		        "File-Level Event Code",
		        "Entered Date/Time",
		        "Effective Date/Time",
		        "Response Level Code"
		    ]
		}))
		hl7SegmentList.append(hl7Segment("MRG", "Merge patient information segment-", {
		    "fields": [
		        "Prior Patient Identifier List",
		        "Prior Alternate Patient ID",
		        "Prior Patient Account Number",
		        "Prior Patient ID",
		        "Prior Visit Number",
		        "Prior Alternate Visit ID",
		        "Prior Patient Name"
		    ]
		}))
		hl7SegmentList.append(hl7Segment("MSA", "Message acknowledgment segment", {
		    "fields": [
		        "Acknowledgement Code",
		        "Message Control ID",
		        "Text Message",
		        "Expected Sequence Number",
		        "Delayed Acknowledgment Type",
		        "Error Condition"
		    ]
		}))
		hl7SegmentList.append(hl7Segment("MSH", "Message header segment", {
		    "fields": [
		        "Field Separator",
		        "Encoding Characters",
		        "Sending Application",
		        "Sending Facility",
		        "Receiving Application",
		        "Receiving Facility",
		        "Date/Time Of Message",
		        "Security",
		        "Message Type",
		        "Message Control ID",
		        "Processing ID",
		        "Version ID",
		        "Sequence Number",
		        "Continuation Pointer",
		        "Accept Acknowledgment Type",
		        "Application Acknowledgment Type",
		        "Country Code",
		        "Character Set",
		        "Principal Language Of Message",
		        "Alternate Character Set Handling Scheme"
		    ]
		}))
		hl7SegmentList.append(hl7Segment("NCK", "System Clock", {
		    "fields": [
		        "System Date/Time"
		    ]
		}))
		hl7SegmentList.append(hl7Segment("NK1", "Next of kin / associated parties segment", {
		    "fields": [
		        "Set ID - NK1",
		        "NK Name",
		        "Relationship",
		        "Address",
		        "Phone Number",
		        "Business Phone Number",
		        "Contact Role",
		        "Start Date",
		        "End Date",
		        "Next of Kin / Associated Parties Job Title",
		        "Next of Kin / Associated Parties Job Code/Class",
		        "Next of Kin / Associated Parties Employee Number",
		        "Organization Name - NK1",
		        "Marital Status",
		        "Sex",
		        "Date/Time Of Birth",
		        "Living Dependency",
		        "Ambulatory Status",
		        "Citizenship",
		        "Primary Language",
		        "Living Arrangement",
		        "Publicity Code",
		        "Protection Indicator",
		        "Student Indicator",
		        "Religion",
		        "Mother s Maiden Name",
		        "Nationality",
		        "Ethnic Group",
		        "Contact Reason",
		        "Contact Person s Name",
		        "Contact Person s Telephone Number",
		        "Contact Person s Address",
		        "Next of Kin/Associated Party s Identifiers",
		        "Job Status",
		        "Race",
		        "Handicap",
		        "Contact Person Social Security Number"
		    ]
		}))
		hl7SegmentList.append(hl7Segment("NPU", "Bed status update segment", {
		    "fields": [
		        "Bed Location",
		        "Bed Status"
		    ]
		}))
		hl7SegmentList.append(hl7Segment("NSC", "Application status change", {
		    "fields": [
		        "Network Change Type",
		        "Current CPU"
		    ]
		}))
		hl7SegmentList.append(hl7Segment("NST", "Application control level statistics", {
		    "fields": [
		        "Statistics Available",
		        "Source Identifier"
		    ]
		}))
		hl7SegmentList.append(hl7Segment("NTE", "Notes and comments segment", {
		    "fields": [
		        "Set ID - NTE",
		        "Source of Comment",
		        "Comment",
		        "Comment Type"
		    ]
		}))
		hl7SegmentList.append(hl7Segment("OBR", "Observation request segment", {
		    "fields": [
		        "Set ID - OBR",
		        "Placer Order Number",
		        "Filler Order Number",
		        "Universal Service ID",
		        "Priority-OBR",
		        "Requested Date/time",
		        "Observation Date/Time  ",
		        "Observation End Date/Time  ",
		        "Collection Volume *",
		        "Collector Identifier *",
		        "Specimen Action Code *",
		        "Danger Code",
		        "Relevant Clinical Info.",
		        "Specimen Received Date/Time *",
		        "Specimen Source",
		        "Ordering Provider",
		        "Order Callback Phone Number",
		        "Placer Field 1",
		        "Placer Field 2",
		        "Filler Field 1 +",
		        "Filler Field 2 +",
		        "Results Rpt/Status Chng - Date/Time +",
		        "Charge to Practice +",
		        "Diagnostic Serv Sect ID",
		        "Result Status +",
		        "Parent Result +",
		        "Quantity/Timing",
		        "Result Copies To",
		        "Parent Number",
		        "Transportation Mode",
		        "Reason for Study",
		        "Principal Result Interpreter +",
		        "Assistant Result Interpreter +",
		        "Technician +",
		        "Transcriptionist +",
		        "Scheduled Date/Time +",
		        "Number of Sample Containers *",
		        "Transport Logistics of Collected Sample *",
		        "Collector s Comment *",
		        "Transport Arrangement Responsibility",
		        "Transport Arranged",
		        "Escort Required",
		        "Planned Patient Transport Comment",
		        "Procedure Code",
		        "Procedure Code Modifier"
		    ]
		}))
		hl7SegmentList.append(hl7Segment("OBX", "Observation/result segment", {
		    "fields": [
		        "Set ID - OBX",
		        "Value Type",
		        "Observation Identifier",
		        "Observation Sub-ID",
		        "Observation Value",
		        "Units",
		        "References Range",
		        "Abnormal Flags",
		        "Probability",
		        "Nature of Abnormal Test",
		        "Observation Result Status",
		        "Date Last Obs Normal Values",
		        "User Defined Access Checks",
		        "Date/Time of the Observation",
		        "Producer's ID",
		        "Responsible Observer",
		        "Observation Method"
		    ]
		}))
		hl7SegmentList.append(hl7Segment("ODS", "Dietary orders, supplements, and preferences segment", {
		    "fields": [
		        "Type",
		        "Service Period",
		        "Diet, Supplement, or Preference Code",
		        "Text Instruction"
		    ]
		}))
		hl7SegmentList.append(hl7Segment("ODT", "Diet tray instructions segment", {
		    "fields": [
		        "Tray Type",
		        "Service Period",
		        "Text Instruction"
		    ]
		}))
		hl7SegmentList.append(hl7Segment("OM1", "General segment", {
		    "fields": [
		        "Sequence Number - Test/Observation Master File",
		        "Producer's Test/Observation ID",
		        "Permitted Data Types",
		        "Specimen Required",
		        "Producer ID",
		        "Observation Description",
		        "Other Test/Observation IDs for the Observation",
		        "Other Names",
		        "Preferred Report Name for the Observation",
		        "Preferred Short Name or Mnemonic for Observation",
		        "Preferred Long Name for the Observation",
		        "Orderability",
		        "Identity of Instrument Used to Perform this Study",
		        "Coded Representation of Method",
		        "Portable",
		        "Observation Producing Department/Section",
		        "Telephone Number of Section",
		        "Nature of Test/Observation",
		        "Report Subheader",
		        "Report Display Order",
		        "Date/Time Stamp for any change in Definition for the Observation",
		        "Effective Date/Time of Change",
		        "Typical Turn-Around Time",
		        "Processing Time",
		        "Processing Priority",
		        "Reporting Priority",
		        "Outside Site",
		        "Address of Outside Site",
		        "Phone Number of Outside Site",
		        "Confidentiality Code",
		        "Observations Required to Interpret the Obs",
		        "Interpretation of Observations",
		        "Contraindications to Observations",
		        "Reflex Tests/Observations",
		        "Rules that Trigger Reflex Testing",
		        "Fixed Canned Message",
		        "Patient Preparation",
		        "Procedure Medication",
		        "Factors that may Effect the Observation",
		        "Test/Observation Performance Schedule",
		        "Description of Test Methods",
		        "Kind of Quantity Observed",
		        "Point Versus Interval",
		        "Challenge Information",
		        "Relationship Modifier",
		        "Target Anatomic Site Of Test",
		        "Modality Of Imaging Measurement"
		    ]
		}))
		hl7SegmentList.append(hl7Segment("OM2", "Numeric observation segment", {
		    "fields": [
		        "Sequence Number - Test/Observation Master File",
		        "Units of Measure",
		        "Range of Decimal Precision",
		        "Corresponding SI Units of Measure",
		        "SI Conversion Factor",
		        "Reference",
		        "Critical Range for Ordinal & Continuous Obs",
		        "Absolute Range for Ordinal & Continuous Obs",
		        "Delta Check Criteria",
		        "Minimum Meaningful Increments"
		    ]
		}))
		hl7SegmentList.append(hl7Segment("OM3", "Categorical test/observation segment", {
		    "fields": [
		        "Sequence Number - Test/Observation Master File",
		        "Preferred Coding System",
		        "Valid Coded  Answers ",
		        "Normal Text/Codes for Categorical Observations",
		        "Abnormal Text/Codes for Categorical Observations",
		        "Critical Text Codes for Categorical Observations",
		        "Value Type"
		    ]
		}))
		hl7SegmentList.append(hl7Segment("OM4", "Observations that require specimens segment", {
		    "fields": [
		        "Sequence Number - Test/Observation Master File",
		        "Derived Specimen",
		        "Container Description",
		        "Container Volume",
		        "Container Units",
		        "Specimen",
		        "Additive",
		        "Preparation",
		        "Special Handling Requirements",
		        "Normal Collection Volume",
		        "Minimum Collection Volume",
		        "Specimen Requirements",
		        "Specimen Priorities",
		        "Specimen Retention Time"
		    ]
		}))
		hl7SegmentList.append(hl7Segment("OM5", "Observation batteries (sets", {
		    "fields": [
		        "Sequence Number - Test/Observation Master File",
		        "Test/Observations Included within an Ordered Test Battery",
		        "Observation ID Suffixes"
		    ]
		}))
		hl7SegmentList.append(hl7Segment("OM6", "Observations that are calculated from other observations segment", {
		    "fields": [
		        "Sequence Number - Test/Observation Master File",
		        "Derivation Rule"
		    ]
		}))
		hl7SegmentList.append(hl7Segment("ORC", "Common order segment", {
		    "fields": [
		        "Order Control",
		        "Placer Order Number",
		        "Filler Order Number",
		        "Placer Group Number",
		        "Order Status",
		        "Response Flag",
		        "Quantity/Timing",
		        "Parent Order",
		        "Date/Time of Transaction",
		        "Entered By",
		        "Verified By",
		        "Ordering Provider",
		        "Enterer s Location",
		        "Call Back Phone Number",
		        "Order Effective Date/Time",
		        "Order Control Code Reason",
		        "Entering Organization",
		        "Entering Device",
		        "Action By",
		        "Advanced Beneficiary Notice Code",
		        "Ordering Facility Name",
		        "Ordering Facility Address",
		        "Ordering Facility Phone Number",
		        "Ordering Provider Address"
		    ]
		}))
		hl7SegmentList.append(hl7Segment("PCR", "Possible causal relationship segment", {
		    "fields": [
		        "Implicated Product",
		        "Generic Product",
		        "Product Class",
		        "Total Duration Of Therapy",
		        "Product Manufacture Date",
		        "Product Expiration Date",
		        "Product Implantation Date",
		        "Product Explantation Date",
		        "Single Use Device",
		        "Indication For Product Use",
		        "Product Problem",
		        "Product Serial/Lot Number",
		        "Product Available For Inspection",
		        "Product Evaluation Performed",
		        "Product Evaluation Status",
		        "Product Evaluation Results",
		        "Evaluated Product Source",
		        "Date Product Returned To Manufacturer",
		        "Device Operator Qualifications",
		        "Relatedness Assessment",
		        "Action Taken In Response To The Event",
		        "Event Causality Observations",
		        "Indirect Exposure Mechanism"
		    ]
		}))
		hl7SegmentList.append(hl7Segment("PD1", "Patient Additional Demographic", {
		    "fields": [
		        "Living Dependency",
		        "Living Arrangement",
		        "Patient Primary Facility",
		        "Patient Primary Care Provider Name & ID No.",
		        "Student Indicator",
		        "Handicap",
		        "Living Will",
		        "Organ Donor",
		        "Separate Bill",
		        "Duplicate Patient",
		        "Publicity Code",
		        "Protection Indicator"
		    ]
		}))
		hl7SegmentList.append(hl7Segment("PDC", "Product detail country segment", {
		    "fields": [
		        "Manufacturer/Distributor",
		        "Country",
		        "Brand Name",
		        "Device Family Name",
		        "Generic Name",
		        "Model Identifier",
		        "Catalogue Identifier",
		        "Other Identifier",
		        "Product Code",
		        "Marketing Basis",
		        "Marketing Approval ID",
		        "Labeled Shelf Life",
		        "Expected Shelf Life",
		        "Date First Marketed",
		        "Date Last Marketed"
		    ]
		}))
		hl7SegmentList.append(hl7Segment("PEO", "Product experience observation segment", {
		    "fields": [
		        "Event Identifiers Used",
		        "Event Symptom/Diagnosis Code",
		        "Event Onset Date/Time",
		        "Event Exacerbation Date/Time",
		        "Event Improved Date/Time",
		        "Event Ended Data/Time",
		        "Event Location Occurred Address",
		        "Event Qualification",
		        "Event Serious",
		        "Event Expected",
		        "Event Outcome",
		        "Patient Outcome",
		        "Event Description From Others",
		        "Event From Original Reporter",
		        "Event Description From Patient",
		        "Event Description From Practitioner",
		        "Event Description From Autopsy",
		        "Cause Of Death",
		        "Primary Observer Name",
		        "Primary Observer Address",
		        "Primary Observer Telephone",
		        "Primary Observer s Qualification",
		        "Confirmation Provided By",
		        "Primary Observer Aware Date/Time",
		        "Primary Observer s identity May Be Divulged"
		    ]
		}))
		hl7SegmentList.append(hl7Segment("PES", "Product experience sender segment", {
		    "fields": [
		        "Sender Organization Name",
		        "Sender Individual Name",
		        "Sender Address",
		        "Sender Telephone",
		        "Sender Event Identifier",
		        "Sender Sequence Number",
		        "Sender Event Description",
		        "Sender Comment",
		        "Sender Aware Date/Time",
		        "Event Report Date",
		        "Event Report Timing/Type",
		        "Event Report Source",
		        "Event Reported To"
		    ]
		}))
		hl7SegmentList.append(hl7Segment("PID", "Patient identification segment", {
		    "fields": [
		        "Set ID - PID",
		        "Patient ID",
		        "Patient Identifier List",
		        "Alternate Patient ID - PID",
		        "Patient Name",
		        "Mother s Maiden Name",
		        "Date/Time Of Birth",
		        "Sex",
		        "Patient Alias",
		        "Race",
		        "Patient Address",
		        "County Code",
		        "Phone Number - Home",
		        "Phone Number - Business",
		        "Primary Language",
		        "Marital Status",
		        "Religion",
		        "Patient Account Number",
		        "SSN Number - Patient",
		        "Driver's License Number - Patient",
		        "Mother's Identifier",
		        "Ethnic Group",
		        "Birth Place",
		        "Multiple Birth Indicator",
		        "Birth Order",
		        "Citizenship",
		        "Veterans Military Status",
		        "Nationality",
		        "Patient Death Date and Time",
		        "Patient Death Indicator"
		    ]
		}))
		hl7SegmentList.append(hl7Segment("PR1", "Procedures segment", {
		    "fields": [
		        "Set ID - PR1",
		        "Procedure Coding Method",
		        "Procedure Code",
		        "Procedure Description",
		        "Procedure Date/Time",
		        "Procedure Functional Type",
		        "Procedure Minutes",
		        "Anesthesiologist",
		        "Anesthesia Code",
		        "Anesthesia Minutes",
		        "Surgeon",
		        "Procedure Practitioner",
		        "Consent Code",
		        "Procedure Priority",
		        "Associated Diagnosis Code",
		        "Procedure Code Modifier"
		    ]
		}))
		hl7SegmentList.append(hl7Segment("PRA", "Practitioner detail segment", {
		    "fields": [
		        "Primary Key Value - PRA",
		        "Practitioner Group",
		        "Practitioner Category",
		        "Provider Billing",
		        "Specialty",
		        "Practitioner ID Numbers",
		        "Privileges",
		        "Date Entered Practice"
		    ]
		}))
		hl7SegmentList.append(hl7Segment("PRB", "Problem Detail", {
		    "fields": [
		        "Action Code",
		        "Action Date/Time",
		        "Problem ID",
		        "Problem Instance ID",
		        "Episode of Care ID",
		        "Problem List Priority",
		        "Problem Established Date/Time",
		        "Anticipated Problem Resolution Date/Time",
		        "Actual Problem Resolution Date/Time",
		        "Problem Classification",
		        "Problem Management Discipline",
		        "Problem Persistence",
		        "Problem Confirmation Status",
		        "Problem Life Cycle Status",
		        "Problem Life Cycle Status Date/Time",
		        "Problem Date of Onset",
		        "Problem Onset Text",
		        "Problem Ranking",
		        "Certainty of Problem",
		        "Probability of Problem",
		        "Individual Awareness of Problem",
		        "Problem Prognosis",
		        "Individual Awareness of Prognosis",
		        "Family/Significant Other Awareness of Problem/Prognosis",
		        "Security/Sensitivity"
		    ]
		}))
		hl7SegmentList.append(hl7Segment("PRC", "Pricing segment", {
		    "fields": [
		        "Primary Key Value - PRC",
		        "Facility ID - PRC",
		        "Department",
		        "Valid Patient Classes",
		        "Price",
		        "Formula",
		        "Minimum Quantity",
		        "Maximum Quantity",
		        "Minimum Price",
		        "Maximum Price",
		        "Effective Start Date",
		        "Effective End Date",
		        "Price Override Flag",
		        "Billing Category",
		        "Chargeable Flag",
		        "Active/Inactive Flag",
		        "Cost",
		        "Charge On Indicator"
		    ]
		}))
		hl7SegmentList.append(hl7Segment("PRD", "Provider Data", {
		    "fields": [
		        "Provider Role",
		        "Provider Name",
		        "Provider Address",
		        "Provider Location",
		        "Provider Communication Information",
		        "Preferred Method Of Contact",
		        "Provider Identifiers",
		        "Effective Start Date of Provider Role",
		        "Effective End Date of Provider Role"
		    ]
		}))
		hl7SegmentList.append(hl7Segment("PSH", "Product summary header segment", {
		    "fields": [
		        "Report Type",
		        "Report Form Identifier",
		        "Report Date",
		        "Report Interval Start Date",
		        "Report Interval End Date",
		        "Quantity Manufactured",
		        "Quantity Distributed",
		        "Quantity Distributed Method",
		        "Quantity Distributed Comment",
		        "Quantity in Use",
		        "Quantity in Use Method",
		        "Quantity in Use Comment",
		        "Number of Product Experience Reports Filed by Facility",
		        "Number of Product Experience Reports Filed by Distributor"
		    ]
		}))
		hl7SegmentList.append(hl7Segment("PTH", "Pathway", {
		    "fields": [
		        "Action Code",
		        "Pathway ID",
		        "Pathway Instance ID",
		        "Pathway Established Date/Time",
		        "Pathway Life Cycle Status",
		        "Change Pathway Life Cycle Status Date/Time"
		    ]
		}))
		hl7SegmentList.append(hl7Segment("PV1", "Patient visit segment", {
		    "fields": [
		        "Set ID - PV1",
		        "Patient Class",
		        "Assigned Patient Location",
		        "Admission Type",
		        "Preadmit Number",
		        "Prior Patient Location",
		        "Attending Doctor",
		        "Referring Doctor",
		        "Consulting Doctor",
		        "Hospital Service",
		        "Temporary Location",
		        "Preadmit Test Indicator",
		        "Re-admission Indicator",
		        "Admit Source",
		        "Ambulatory Status",
		        "VIP Indicator",
		        "Admitting Doctor",
		        "Patient Type",
		        "Visit Number",
		        "Financial Class",
		        "Charge Price Indicator",
		        "Courtesy Code",
		        "Credit Rating",
		        "Contract Code",
		        "Contract Effective Date",
		        "Contract Amount",
		        "Contract Period",
		        "Interest Code",
		        "Transfer to Bad Debt Code",
		        "Transfer to Bad Debt Date",
		        "Bad Debt Agency Code",
		        "Bad Debt Transfer Amount",
		        "Bad Debt Recovery Amount",
		        "Delete Account Indicator",
		        "Delete Account Date",
		        "Discharge Disposition",
		        "Discharged to Location",
		        "Diet Type",
		        "Servicing Facility",
		        "Bed Status",
		        "Account Status",
		        "Pending Location",
		        "Prior Temporary Location",
		        "Admit Date/Time",
		        "Discharge Date/Time",
		        "Current Patient Balance",
		        "Total Charges",
		        "Total Adjustments",
		        "Total Payments",
		        "Alternate Visit ID",
		        "Visit Indicator",
		        "Other Healthcare Provider"
		    ]
		}))
		hl7SegmentList.append(hl7Segment("PV2", "Patient visit - additional information segment", {
		    "fields": [
		        "Prior Pending Location",
		        "Accommodation Code",
		        "Admit Reason",
		        "Transfer Reason",
		        "Patient Valuables",
		        "Patient Valuables Location",
		        "Visit User Code",
		        "Expected Admit Date/Time",
		        "Expected Discharge Date/Time",
		        "Estimated Length of Inpatient Stay",
		        "Actual Length of Inpatient Stay",
		        "Visit Description",
		        "Referral Source Code",
		        "Previous Service Date",
		        "Employment Illness Related Indicator",
		        "Purge Status Code",
		        "Purge Status Date",
		        "Special Program Code",
		        "Retention Indicator",
		        "Expected Number of Insurance Plans",
		        "Visit Publicity Code",
		        "Visit Protection Indicator",
		        "Clinic Organization Name",
		        "Patient Status Code",
		        "Visit Priority Code",
		        "Previous Treatment Date",
		        "Expected Discharge Disposition",
		        "Signature on File Date",
		        "First Similar Illness Date",
		        "Patient Charge Adjustment Code",
		        "Recurring Service Code",
		        "Billing Media Code",
		        "Expected Surgery Date & Time",
		        "Military Partnership Code",
		        "Military Non-Availability Code",
		        "Newborn Baby Indicator",
		        "Baby Detained Indicator"
		    ]
		}))
		hl7SegmentList.append(hl7Segment("QAK", "Query Acknowledgement", {
		    "fields": [
		        "Query Tag",
		        "Query Response Status"
		    ]
		}))
		hl7SegmentList.append(hl7Segment("QRD", "Original-style query definition segment", {
		    "fields": [
		        "Query Date/Time",
		        "Query Format Code",
		        "Query Priority",
		        "Query ID",
		        "Deferred Response Type",
		        "Deferred Response Date/Time",
		        "Quantity Limited Request",
		        "Who Subject Filter",
		        "What Subject Filter",
		        "What Department Data Code",
		        "What Data Code Value Qual.",
		        "Query Results Level"
		    ]
		}))
		hl7SegmentList.append(hl7Segment("QRF", "Original style query filter segment", {
		    "fields": [
		        "Where Subject Filter",
		        "When Data Start Date/Time",
		        "When Data End Date/Time",
		        "What User Qualifier",
		        "Other QRY Subject Filter",
		        "Which Date/Time Qualifier",
		        "Which Date/Time Status Qualifier",
		        "Date/Time Selection Qualifier",
		        "When Quantity/Timing Qualifier"
		    ]
		}))
		hl7SegmentList.append(hl7Segment("RDF", "Table row definition segment", {
		    "fields": [
		        "Number of Columns per Row",
		        "Column Description"
		    ]
		}))
		hl7SegmentList.append(hl7Segment("RDT", "Table row data segment", {
		    "fields": [
		        "Column Value"
		    ]
		}))
		hl7SegmentList.append(hl7Segment("RF1", "Referral Infomation", {
		    "fields": [
		        "Referral Status",
		        "Referral Priority",
		        "Referral Type",
		        "Referral Disposition",
		        "Referral Category",
		        "Originating Referral Identifier",
		        "Effective Date",
		        "Expiration Date",
		        "Process Date",
		        "Referral Reason",
		        "External Referral Identifier"
		    ]
		}))
		hl7SegmentList.append(hl7Segment("RGS", "Resource group segment", {
		    "fields": [
		        "Set ID - RGS",
		        "Segment Action Code",
		        "Resource Group ID"
		    ]
		}))
		hl7SegmentList.append(hl7Segment("ROL", "Role", {
		    "fields": [
		        "Role Instance ID",
		        "Action Code",
		        "Role-ROL",
		        "Role Person",
		        "Role Begin Date/Time",
		        "Role End Date/Time",
		        "Role Duration",
		        "Role Action Reason"
		    ]
		}))
		hl7SegmentList.append(hl7Segment("RQ1", "Requisition detail-1 segment", {
		    "fields": [
		        "Anticipated Price",
		        "Manufacturer ID",
		        "Manufacturer s Catalog",
		        "Vendor ID",
		        "Vendor Catalog",
		        "Taxable",
		        "Substitute Allowed"
		    ]
		}))
		hl7SegmentList.append(hl7Segment("RQD", "Requisition detail segment", {
		    "fields": [
		        "Requisition Line Number",
		        "Item Code - Internal",
		        "Item Code - External",
		        "Hospital Item Code",
		        "Requisition Quantity",
		        "Requisition Unit of Measure",
		        "Dept. Cost Center",
		        "Item Natural Account Code",
		        "Deliver To ID",
		        "Date Needed"
		    ]
		}))
		hl7SegmentList.append(hl7Segment("RXA", "Pharmacy/treatment administration segment", {
		    "fields": [
		        "Give Sub-ID Counter",
		        "Administration Sub-ID Counter",
		        "Date/Time Start of Administration",
		        "Date/Time End of Administration",
		        "Administered Code",
		        "Administered Amount",
		        "Administered Units",
		        "Administered Dosage Form",
		        "Administration Notes",
		        "Administering Provider",
		        "Administered-at Location",
		        "Administered Per",
		        "Administered Strength",
		        "Administered Strength Units",
		        "Substance Lot Number",
		        "Substance Expiration Date",
		        "Substance Manufacturer Name",
		        "Substance Refusal Reason",
		        "Indication",
		        "Completion Status",
		        "Action Code-RXA",
		        "System Entry Date/Time"
		    ]
		}))
		hl7SegmentList.append(hl7Segment("RXC", "Pharmacy/treatment component order segment", {
		    "fields": [
		        "RX Component Type",
		        "Component Code",
		        "Component Amount",
		        "Component Units",
		        "Component Strength",
		        "Component Strength Units"
		    ]
		}))
		hl7SegmentList.append(hl7Segment("RXD", "Pharmacy/treatment dispense segment", {
		    "fields": [
		        "Dispense Sub-ID Counter",
		        "Dispense/Give Code",
		        "Date/Time Dispensed",
		        "Actual Dispense Amount",
		        "Actual Dispense Units",
		        "Actual Dosage Form",
		        "Prescription Number",
		        "Number of Refills Remaining",
		        "Dispense Notes",
		        "Dispensing Provider",
		        "Substitution Status",
		        "Total Daily Dose",
		        "Dispense-To Location",
		        "Needs Human Review",
		        "Pharmacy/Treatment Supplier s Special Dispensing Instructions",
		        "Actual Strength",
		        "Actual Strength Unit",
		        "Substance Lot Number",
		        "Substance Expiration Date",
		        "Substance Manufacturer Name",
		        "Indication",
		        "Dispense Package Size",
		        "Dispense Package Size Unit",
		        "Dispense Package Method"
		    ]
		}))
		hl7SegmentList.append(hl7Segment("RXE", "Pharmacy/treatment encoded order segment", {
		    "fields": [
		        "Quantity/Timing",
		        "Give Code",
		        "Give Amount - Minimum",
		        "Give Amount - Maximum",
		        "Give Units",
		        "Give Dosage Form",
		        "Provider s Administration Instructions",
		        "Deliver-to Location",
		        "Substitution Status",
		        "Dispense Amount",
		        "Dispense Units",
		        "Number Of Refills",
		        "Ordering Provider s DEA Number",
		        "Pharmacist/Treatment Supplier s Verifier ID",
		        "Prescription Number",
		        "Number of Refills Remaining",
		        "Number of Refills/Doses Dispensed",
		        "D/T of Most Recent Refill or Dose Dispensed",
		        "Total Daily Dose",
		        "Needs Human Review",
		        "Pharmacy/Treatment Supplier s Special Dispensing Instructions",
		        "Give Per",
		        "Give Rate Amount",
		        "Give Rate Units",
		        "Give Strength",
		        "Give Strength Units",
		        "Give Indication",
		        "Dispense Package Size",
		        "Dispense Package Size Unit",
		        "Dispense Package Method"
		    ]
		}))
		hl7SegmentList.append(hl7Segment("RXG", "Pharmacy/treatment give segment", {
		    "fields": [
		        "Give Sub-ID Counter",
		        "Dispense Sub-ID Counter",
		        "Quantity/Timing",
		        "Give Code",
		        "Give Amount - Minimum",
		        "Give Amount - Maximum",
		        "Give Units",
		        "Give Dosage Form",
		        "Administration Notes",
		        "Substitution Status",
		        "Dispense-To Location",
		        "Needs Human Review",
		        "Pharmacy/Treatment Supplier s Special Administration Instructions",
		        "Give Per",
		        "Give Rate Amount",
		        "Give Rate Units",
		        "Give Strength",
		        "Give Strength Units",
		        "Substance Lot Number",
		        "Substance Expiration Date",
		        "Substance Manufacturer Name",
		        "Indication"
		    ]
		}))
		hl7SegmentList.append(hl7Segment("RXO", "Pharmacy/treatment order segment", {
		    "fields": [
		        "Requested Give Code",
		        "Requested Give Amount - Minimum",
		        "Requested Give Amount - Maximum",
		        "Requested Give Units",
		        "Requested Dosage Form",
		        "Provider s Pharmacy/Treatment Instructions",
		        "Provider s Administration Instructions",
		        "Deliver-to Location",
		        "Allow Substitutions",
		        "Requested Dispense Code",
		        "Requested Dispense Amount",
		        "Requested Dispense Units",
		        "Number Of Refills",
		        "Ordering Provider s DEA Number",
		        "Pharmacist/Treatment Supplier s Verifier ID",
		        "Needs Human Review",
		        "Requested Give Per",
		        "Requested Give Strength",
		        "Requested Give Strength Units",
		        "Indication",
		        "Requested Give Rate Amount",
		        "Requested Give Rate Units",
		        "Total Daily Dose"
		    ]
		}))
		hl7SegmentList.append(hl7Segment("RXR", "Pharmacy/treatment route segment", {
		    "fields": [
		        "Route",
		        "Site",
		        "Administration Device",
		        "Administration Method",
		        "Routing Instruction"
		    ]
		}))
		hl7SegmentList.append(hl7Segment("SCH", "Schedule activity information segment", {
		    "fields": [
		        "Placer Appointment ID",
		        "Filler Appointment ID",
		        "Occurrence Number",
		        "Placer Group Number",
		        "Schedule ID",
		        "Event Reason",
		        "Appointment Reason",
		        "Appointment Type",
		        "Appointment Duration",
		        "Appointment Duration Units",
		        "Appointment Timing Quantity",
		        "Placer Contact Person",
		        "Placer Contact Phone Number",
		        "Placer Contact Address",
		        "Placer Contact Location",
		        "Filler Contact Person",
		        "Filler Contact Phone Number",
		        "Filler Contact Address",
		        "Filler Contact Location",
		        "Entered by Person",
		        "Entered by Phone Number",
		        "Entered by Location",
		        "Parent Placer Appointment ID",
		        "Parent Filler Appointment ID",
		        "Filler Status Code"
		    ]
		}))
		hl7SegmentList.append(hl7Segment("SPR", "Stored procedure request definition segment", {
		    "fields": [
		        "Query Tag",
		        "Query/ Response Format Code",
		        "Stored Procedure Name",
		        "Input Parameter List"
		    ]
		}))
		hl7SegmentList.append(hl7Segment("STF", "Staff identification segment", {
		    "fields": [
		        "Primary Key Value - STF",
		        "Staff ID Code",
		        "Staff Name",
		        "Staff Type",
		        "Sex",
		        "Date/Time Of Birth",
		        "Active/Inactive Flag",
		        "Department",
		        "Hospital Service",
		        "Phone",
		        "Office/Home Address",
		        "Institution Activation Date",
		        "Institution Inactivation Date",
		        "Backup Person ID",
		        "E-Mail Address",
		        "Preferred Method Of Contact",
		        "Marital Status",
		        "Job Title",
		        "Job Code/Class",
		        "Employment Status",
		        "Additional Insured on  Auto",
		        "Driver s License Number - Staff",
		        "Copy  Auto Ins",
		        "Auto Ins. Expires",
		        "Date Last DMV Review",
		        "Date Next DMV Review"
		    ]
		}))
		hl7SegmentList.append(hl7Segment("TXA", "Document notification segment", {
		    "fields": [
		        "Set ID - TXA",
		        "Document Type",
		        "Document Content Presentation",
		        "Activity Date/Time",
		        "Primary Activity Provider Code/Name",
		        "Origination Date/Time",
		        "Transcription Date/Time",
		        "Edit Date/Time",
		        "Originator Code/Name",
		        "Assigned Document Authenticator",
		        "Transcriptionist Code/Name",
		        "Unique Document Number",
		        "Parent Document Number",
		        "Placer Order Number",
		        "Filler Order Number",
		        "Unique Document File Name",
		        "Document Completion Status",
		        "Document Confidentiality Status",
		        "Document Availability Status",
		        "Document Storage Status",
		        "Document Change Reason",
		        "Authentication Person, Time Stamp",
		        "Distributed Copies"
		    ]
		}))
		hl7SegmentList.append(hl7Segment("UB1", "UB82 data segment", {
		    "fields": [
		        "Set ID - UB1",
		        "Blood Deductible",
		        "Blood Furnished-Pints Of",
		        "Blood Replaced-Pints",
		        "Blood Not Replaced-Pints",
		        "Co-Insurance Days",
		        "Condition Code",
		        "Covered Days -",
		        "Non Covered Days -",
		        "Value Amount & Code",
		        "Number Of Grace Days",
		        "Special Program Indicator",
		        "PSRO/UR Approval Indicator",
		        "PSRO/UR Approved Stay-Fm",
		        "PSRO/UR Approved Stay-To",
		        "Occurrence",
		        "Occurrence Span",
		        "Occur Span Start Date",
		        "Occur Span End Date",
		        "UB-82 Locator 2",
		        "UB-82 Locator 9",
		        "UB-82 Locator 27",
		        "UB-82 Locator 45"
		    ]
		}))
		hl7SegmentList.append(hl7Segment("UB2", "UB92 data segment", {
		    "fields": [
		        "Set ID - UB2",
		        "Co-Insurance Days",
		        "Condition Code",
		        "Covered Days",
		        "Non-Covered Days",
		        "Value Amount & Code",
		        "Occurrence Code & Date",
		        "Occurrence Span Code/Dates",
		        "UB92 Locator 2",
		        "UB92 Locator 11",
		        "UB92 Locator 31",
		        "Document Control Number",
		        "UB92 Locator 49",
		        "UB92 Locator 56",
		        "UB92 Locator 57",
		        "UB92 Locator 78",
		        "Special Visit Count"
		    ]
		}))
		hl7SegmentList.append(hl7Segment("URD", "Results/update definition segment", {
		    "fields": [
		        "R/U Date/Time",
		        "Report Priority",
		        "R/U Who Subject Definition",
		        "R/U What Subject Definition",
		        "R/U What Department Code",
		        "R/U Display/Print Locations",
		        "R/U Results Level"
		    ]
		}))
		hl7SegmentList.append(hl7Segment("URS", "Unsolicited selection segment", {
		    "fields": [
		        "R/U Where Subject Definition",
		        "R/U When Data Start Date/Time",
		        "R/U When Data End Date/Time",
		        "R/U What User Qualifier",
		        "R/U Other Results Subject Definition",
		        "R/U Which Date/Time Qualifier",
		        "R/U Which Date/Time Status Qualifier",
		        "R/U Date/Time Selection Qualifier",
		        "R/U Quantity/Timing Qualifier"
		    ]
		}))
		hl7SegmentList.append(hl7Segment("VAR", "Variance", {
		    "fields": [
		        "Variance Instance ID",
		        "Documented Date/Time",
		        "Stated Variance Date/Time",
		        "Variance Originator",
		        "Variance Classification",
		        "Variance Description"
		    ]
		}))
		hl7SegmentList.append(hl7Segment("VTQ", "Virtual table query request segment", {
		    "fields": [
		        "Query Tag",
		        "Query/ Response Format Code",
		        "VT Query Name",
		        "Virtual Table Name",
		        "Selection Criteria"
		    ]
		}))

		return hl7SegmentList