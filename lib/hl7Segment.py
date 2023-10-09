# Handles the definition of the HL7 segments
class hl7Segment(object):
	def __init__(self, code, description):
		self.code = code
		self.description = description
		self.fields = {}

	# Gets a segment object based on his code. If no object is found in the segmentList with the following code None is returned.
	def getSegmentByCode(self, code, segmentList):
		for listItem in segmentList:
			if (listItem.code == code):
				return listItem
		return None

	# Load a segment and fields data based on version number
	def loadSegmentDefinition(self, version):
		import json

		file = open('./lib/definitions/' + version + '.json', 'r')
		all_fields = json.load(file)
		try:
			self.fields = all_fields[self.code]
		except:
			pass

	# Loads the entire segment list
	def loadSegmentList(self, version = "2.5.1"):
		hl7SegmentList = []

		seg = hl7Segment("ABS", "Abstract")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("ACC", "Accident")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("ADD", "Addendum")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("ADJ", "Adjustment")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("AFF", "Professional Affiliation")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("AIG", "Appointment Information - General Resource")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("AIL", "Appointment Information - Location Resource")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("AIP", "Appointment Information - Personnel Resource")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("AIS", "Appointment Information")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("AL1", "Patient Allergy Information")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("APR", "Appointment Preferences")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("ARQ", "Appointment Request")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("ARV", "Access Restriction")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("AUT", "Authorization Information")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("BHS", "Batch Header")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("BLC", "Blood Code")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("BLG", "Billing")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("BPO", "Blood product order")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("BPX", "Blood product dispense status")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("BTS", "Batch Trailer")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("BTX", "Blood Product Transfusion/Disposition")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("BUI", "Blood Unit Information")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("CDM", "Charge Description Master")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("CDO", "Cumulative Dosage")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("CER", "Certificate Detail")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("CM0", "Clinical Study Master")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("CM1", "Clinical Study Phase Master")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("CM2", "Clinical Study Schedule Master")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("CNS", "Clear Notification")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("CON", "Consent Segment")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("CSP", "Clinical Study Phase")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("CSR", "Clinical Study Registration")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("CSS", "Clinical Study Data Schedule Segment")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("CTD", "Contact Data")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("CTI", "Clinical Trial Identification")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("DB1", "Disability")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("DG1", "Diagnosis")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("DMI", "DRG Master File Information")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("DON", "Donation")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("DRG", "Diagnosis Related Group")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("DSC", "Continuation Pointer")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("DSP", "Display Data")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("ECD", "Equipment Command")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("ECR", "Equipment Command Response")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("EDU", "Educational Detail")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("EQP", "Equipment/log Service")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("EQU", "Equipment Detail")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("ERR", "Error")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("EVN", "Event Type")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("FAC", "Facility")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("FHS", "File Header")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("FT1", "Financial Transaction")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("FTS", "File Trailer")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("GOL", "Goal Detail")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("GP1", "Grouping/Reimbursement - Visit")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("GP2", "Grouping/Reimbursement - Procedure Line Item")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("GT1", "Guarantor")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("Hxx", "any HL7 segment")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("IAM", "Patient Adverse Reaction Information")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("IAR", "Allergy Reaction")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("IIM", "Inventory Item Master")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("ILT", "Material Lot")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("IN1", "Insurance")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("IN2", "Insurance Additional Information")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("IN3", "Insurance Additional Information, Certification")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("INV", "Inventory Detail")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("IPC", "Imaging Procedure Control Segment")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("IPR", "Invoice Processing Results")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("ISD", "Interaction Status Detail")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("ITM", "Material Item")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("IVC", "Invoice Segment")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("IVT", "Material Location")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("LAN", "Language Detail")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("LCC", "Location Charge Code")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("LCH", "Location Characteristic")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("LDP", "Location Department")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("LOC", "Location Identification")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("LRL", "Location Relationship")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("MFA", "Master File Acknowledgment")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("MFE", "Master File Entry")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("MFI", "Master File Identification")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("MRG", "Merge Patient Information")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("MSA", "Message Acknowledgment")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("MSH", "Message Header")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("NCK", "System Clock")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("NDS", "Notification Detail")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("NK1", "Next of Kin / Associated Parties")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("NPU", "Bed Status Update")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("NSC", "Application Status Change")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("NST", "Application control level statistics")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("NTE", "Notes and Comments")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("OBR", "Observation Request")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("OBX", "Observation/Result")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("ODS", "Dietary Orders, Supplements, and Preferences")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("ODT", "Diet Tray Instructions")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("OM1", "General Segment")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("OM2", "Numeric Observation")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("OM3", "Categorical Service/Test/Observation")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("OM4", "Observations that Require Specimens")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("OM5", "Observation Batteries (Sets)")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("OM6", "Observations that are Calculated from Other Observations")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("OM7", "Additional Basic Attributes")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("OMC", "Supporting Clinical Information Segment")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("OMP", "Pharmacy/Treatment Order Message")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("ORC", "Common Order")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("ORG", "Practitioner Organization Unit")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("ORP", "Pharmacy/Treatment Order Acknowledgment")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("OVR", "Override Segment")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("PAC", "Shipment Package")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("PCE", "Patient Charge Cost Center Exceptions")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("PCR", "Possible Causal Relationship")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("PD1", "Patient Additional Demographic")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("PDA", "Patient Death and Autopsy")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("PDC", "Product Detail Country")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("PEO", "Product Experience Observation")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("PES", "Product Experience Sender")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("PID", "Patient Identification")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("PKG", "Item Packaging")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("PM1", "Payer Master File Segment")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("PMT", "Payment Information")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("PR1", "Procedures")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("PRA", "Practitioner Detail")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("PRB", "Problem Details")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("PRC", "Pricing")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("PRD", "Provider Data")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("PRT", "Participation Information")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("PSG", "Product/Service Group")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("PSH", "Product Summary Header")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("PSL", "Product/Service Line Item")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("PSS", "Product/Service Section")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("PTH", "Pathway")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("PV1", "Patient Visit")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("PV2", "Patient Visit - Additional Information")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("PYE", "Payee Information")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("QAK", "Query Acknowledgment")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("QID", "Query Identification")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("QPD", "Query Parameter Definition")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("QRD", "Original-Style Query Definition")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("QRF", "Original style query filter")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("QRI", "Query Response Instance")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("RCP", "Response Control Parameter")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("RDF", "Table Row Definition")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("RDT", "Table Row Data")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("REL", "Clinical Relationship Segment")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("RF1", "Referral Information")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("RFI", "Request for Information")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("RGS", "Resource Group")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("RMI", "Risk Management Incident")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("ROL", "Role")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("RQ1", "Requisition Detail-1")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("RQD", "Requisition Detail")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("RRD", "Pharmacy/Treatment Dispense Acknowledgement")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("RXA", "Pharmacy/Treatment Administration")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("RXC", "Pharmacy/Treatment Component Order")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("RXD", "Pharmacy/Treatment Dispense")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("RXE", "Pharmacy/Treatment Encoded Order")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("RXG", "Pharmacy/Treatment Give")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("RXO", "Pharmacy/Treatment Order")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("RXR", "Pharmacy/Treatment Route")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("RXV", "Pharmacy/Treatment Infusion")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("SAC", "Specimen Container detail")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("SCD", "Anti-Microbial Cycle Data")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("SCH", "Scheduling Activity Information")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("SCP", "Sterilizer Configuration (Anti-Microbial Devices)")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("SDD", "Sterilization Device Data")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("SFT", "Software Segment")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("SGH", "Segment Group Header")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("SGT", "Segment Group Trailer")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("SHP", "Shipment")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("SID", "Substance Identifier")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("SLT", "Sterilization Lot")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("SPM", "Specimen")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("STF", "Staff Identification")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("STZ", "Sterilization Parameter")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("TCC", "Test Code Configuration")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("TCD", "Test Code Detail")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("TQ1", "Timing/Quantity")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("TQ2", "Timing/Quantity Relationship")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("TXA", "Transcription Document Header")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("UAC", "User Authentication Credential Segment")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("UB1", "UB82 Data")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("UB2", "Uniform Billing Data")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("URD", "Results/update Definition")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("URS", "Unsolicited Selection")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("VAR", "Variance")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("VND", "Purchasing Vendor")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("ZL7", "(This is a proposed example only)")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)
		seg = hl7Segment("Zxx", "Any Z-Segment")
		seg.loadSegmentDefinition(version)
		hl7SegmentList.append(seg)

		return hl7SegmentList