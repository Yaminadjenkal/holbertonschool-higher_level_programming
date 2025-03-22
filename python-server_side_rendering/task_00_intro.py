#!/usr/bin/python3
import logging
import os


def generate_invitations(template, attendees):
    if not isinstance(template, str):
        logging.error("Template must be a string")
        return
    if not isinstance(attendees, list) or not all(isinstance(attendee, dict) for attendee in attendees):
        logging.error("Attendees must be a list of dictionaries")
        return
    
    if not template or template == "":
        logging.error("Template is empty, no output files generated.")
        return

    if not attendees:
        logging.error("No data provided, no output files generated.")
        return

    for index, attendee in enumerate(attendees, start=1):
        output_filename = f"output_{index}.txt"
        
        if os.path.exists(output_filename):
            logging.warning(f"{output_filename} file already exists")
            continue
        try:
            filled_template = template
            for key, value in attendee.items():
                if value is None:
                    filled_template = filled_template.replace(f"{{{key}}}", "N/A")
                else:
                    filled_template = filled_template.replace(f"{{{key}}}", str(value))

            with open(output_filename, "w") as f:
                f.write(filled_template)
            logging.info(f"{output_filename} invitation generated")

        except Exception as e:
            logging.error(f"{output_filename} invitation not generated: {e}")