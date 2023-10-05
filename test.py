from lib.hl7Event import *
from lib.hl7Segment import *
from lib.hl7TextUtils import *

hl7EventList = hl7Event("","")
hl7EventList = hl7EventList.loadEventList()
hl7SegmentList = hl7Segment("","",{})
hl7SegmentList = hl7SegmentList.loadSegmentList()

STATUS_BAR_HL7 = 'StatusBarHL7'

with open('./Example Message/example.hl7', 'r') as file:
	for line in file:
		header = ""
		body = ""
		segmentCode = ""

		#Segment
		selectedSegment = line


		fields = selectedSegment.split('|')
		fields = re.split(r'(?<!\\)(?:\\\\)*\|', selectedSegment)


		fieldId = 0
		componentId = 1
		subComponentId = 1

		for segmentItem in hl7SegmentList:
			if (segmentItem.code == fields[0]):
				header = segmentItem.code + " - " + segmentItem.description
				segmentCode = segmentItem.code
				segmentFields = segmentItem.fields["fields"]

		header = '<b style="color:#33ccff;">' + header + '</b>'

		for field in fields:

			if (field != ""):

				if(field != "^~\&"):
					components =  re.compile(r'(?<!\\)(?:\\\\)*\^').split(field)

					totalCircunflex = field.count("^")

					for component in components:
						if(component != ""):

							subComponents =  re.compile(r'(?<!\\)(?:\\\\)*&').split(component)

							if(len(subComponents) > 1):

								for subComponent in subComponents:
									if(subComponent != ""):

										regex = "(<)"
										filler = "&lt;"
										subComponent = re.sub(regex, filler, subComponent)
			
										regex = "(>)"
										filler = "&gt;"
										subComponent = re.sub(regex, filler, subComponent)

										try:
											fieldName = segmentFields[fieldId-1]
										except:
											fieldName = ""
			
										body = body + '<br>' + str(fieldId) + "." + str(componentId) + "." + str(subComponentId) + " - " + fieldName + " - " + subComponent


									subComponentId = subComponentId + 1

								subComponentId = 1


							else: 

								regex = "(<)"
								filler = "&lt;"
								component = re.sub(regex, filler, component)
	
								regex = "(>)"
								filler = "&gt;"
								component = re.sub(regex, filler, component)
	
								till = re.compile(r'(?<!\\)(?:\\\\)*~').split(component)

								if segmentCode == 'MSH' and fieldId > 1:
									fieldCounter = fieldId + 1
								else:
									fieldCounter = fieldId

								try:
									fieldName = segmentFields[fieldId-1]
								except:
									fieldName = ""

								if(totalCircunflex > 0):
									for tillItem in till:
										body = body + '<br>' + str(fieldCounter) + "." + str(componentId) + " - " + fieldName + " - " + tillItem
								else:
									for tillItem in till:
										body = body + '<br>' + str(fieldCounter) + " - " + fieldName + " - " + tillItem

						componentId = componentId + 1

					componentId = 1

				else:
					if len(selectedSegment) > 3:
						if selectedSegment[3] == '|':
							body = body + '<br>' + str(1) + " - " + selectedSegment[3] + "\n"
					if len(fields) > 0:
						body = body + '<br>' + str(2) + " - " + fields[1] + "\n"

			fieldId = fieldId + 1

		message = header + body
		message = message.replace("\&", "\&amp;")

		print(message)