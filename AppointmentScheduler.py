import datetime

class Appointment:
    def __init__(self, patient_name, appointment_datetime):
        self.patient_name = patient_name
        self.appointment_datetime = appointment_datetime

    def display_details(self):
        print("Patient Name: " + self.patient_name)
        print("Appointment Date and Time: " + self.appointment_datetime.strftime("%Y-%m-%d %H:%M"))
        print()


class AppointmentScheduler:
    def __init__(self):
        self.appointments = []

    def schedule_appointment(self, appointment):
        self.appointments.append(appointment)

    def cancel_appointment(self, appointment):
        self.appointments.remove(appointment)

    def display_appointments(self):
        print("All Appointments:")
        for appointment in self.appointments:
            appointment.display_details()

    def find_appointments_by_date(self, date):
        appointments_by_date = [appointment for appointment in self.appointments
                                if appointment.appointment_datetime.date() == date.date()]
        return appointments_by_date


# Example usage
scheduler = AppointmentScheduler()

appointment1 = Appointment("John Doe", datetime.datetime(2023, 6, 1, 9, 30))
scheduler.schedule_appointment(appointment1)

appointment2 = Appointment("Jane Smith", datetime.datetime(2023, 6, 1, 10, 0))
scheduler.schedule_appointment(appointment2)

appointment3 = Appointment("Mike Johnson", datetime.datetime(2023, 6, 2, 11, 30))
scheduler.schedule_appointment(appointment3)

scheduler.display_appointments()

cancel_appointment = appointment2
scheduler.cancel_appointment(cancel_appointment)

print("Updated Appointment List:")
scheduler.display_appointments()

target_date = datetime.datetime(2023, 6, 1)
appointments_on_date = scheduler.find_appointments_by_date(target_date)

print("Appointments on", target_date.date())
for appointment in appointments_on_date:
    appointment.display_details()
